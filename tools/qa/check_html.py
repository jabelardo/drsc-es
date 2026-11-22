#!/usr/bin/env python3
"""Read-only QA checks for DRSC-ES.html.

Checks:
  1. Internal anchors: every href="#x" resolves to an id="x".
  2. Duplicate ids: count (fails if above --max-duplicates or above the baseline).
  3. HTML structure: start/end tags of container elements are balanced and nested.
  4. Heading levels: headings that skip a level (reported, not a failure).

With --baseline REF (a git revision) it also compares against that revision's file:
  5. Ids added and removed.
  6. Duplicated ids whose first occurrence is now a different element. Browsers
     follow the first occurrence, so links to that id open something else. A renamed
     element is not a change. Acknowledge intended changes with --allow-target-change.
  7. Words added and removed (a summary of the text difference).

Usage:
  python3 tools/qa/check_html.py [FILE] [--baseline REF [--baseline-file PATH]
                                 [--allow-target-change ID ...]] [--max-duplicates N] [--verbose]

Exit status: 0 when all checks pass, 1 otherwise.
"""
import argparse
import collections
import html
import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

ID_RE = re.compile(r'\bid="([^"]+)"')
HREF_RE = re.compile(r'href="#([^"]+)"')
HEADING_RE = re.compile(r'<h([1-6])[\s>]')

# Elements whose start and end tags must balance. <p>, <li>, <td>, <th>, <tr> and
# table sections may be closed implicitly in HTML, so they get the HTML rules below.
STRICT = {'div', 'table', 'ul', 'ol', 'span', 'section', 'main', 'nav', 'header', 'footer',
          'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'strong', 'em', 'button', 'details',
          'summary', 'figure', 'caption', 'blockquote', 'dl', 'svg'}
OPTIONAL_END = {'p', 'li', 'td', 'th', 'tr', 'thead', 'tbody', 'tfoot', 'dt', 'dd', 'option'}
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source',
        'track', 'wbr', 'path', 'circle', 'rect', 'stop', 'use', 'line', 'polygon', 'ellipse'}
# Start tags that implicitly close an open <p>
CLOSES_P = {'address', 'article', 'aside', 'blockquote', 'details', 'div', 'dl', 'fieldset',
            'figcaption', 'figure', 'footer', 'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
            'header', 'hr', 'main', 'nav', 'ol', 'p', 'pre', 'section', 'table', 'ul'}


class StructureChecker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []      # (tag, line)
        self.errors = []

    def _pop_optional(self, until=None):
        while self.stack and self.stack[-1][0] in OPTIONAL_END and self.stack[-1][0] != until:
            self.stack.pop()

    def handle_starttag(self, tag, attrs):
        line = self.getpos()[0]
        if tag in VOID:
            return
        if tag in CLOSES_P and self.stack and self.stack[-1][0] == 'p':
            self.stack.pop()
        if tag == 'li':
            self._close_sibling('li', {'ul', 'ol'})
        elif tag in ('td', 'th'):
            self._close_sibling(('td', 'th'), {'tr'})
        elif tag == 'tr':
            self._close_sibling('tr', {'table', 'thead', 'tbody', 'tfoot'})
        elif tag in ('dt', 'dd'):
            self._close_sibling(('dt', 'dd'), {'dl'})
        if tag in STRICT or tag in OPTIONAL_END:
            self.stack.append((tag, line))

    def _close_sibling(self, names, parents):
        names = (names,) if isinstance(names, str) else names
        for k in range(len(self.stack) - 1, -1, -1):
            t = self.stack[k][0]
            if t in names:
                del self.stack[k:]
                return
            if t in parents or t in STRICT:
                return

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        line = self.getpos()[0]
        if tag in VOID:
            return
        if tag not in STRICT and tag not in OPTIONAL_END:
            return
        if not any(t == tag for t, _ in self.stack):
            if tag != 'p':   # a stray </p> creates an empty paragraph; browsers cope
                self.errors.append(f'line {line}: </{tag}> without an open <{tag}>')
            return
        # implicitly close optional elements, then the element itself
        while self.stack and self.stack[-1][0] != tag:
            t, l = self.stack.pop()
            if t not in OPTIONAL_END:
                self.errors.append(f'line {line}: </{tag}> closes <{t}> opened at line {l}')
        self.stack.pop()

    def finish(self):
        for t, l in self.stack:
            if t not in OPTIONAL_END:
                self.errors.append(f'line {l}: <{t}> never closed')
        return self.errors


def words(text):
    text = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', text, flags=re.S)
    return collections.Counter(html.unescape(re.sub(r'<[^>]+>', ' ', text)).split())


def id_owner(lines, i):
    """Identify the element an id occurrence belongs to: the enclosing heading's own id
    and its text (two different headings may share an id, so the text matters)."""
    for j in range(i, max(i - 3, -1), -1):
        m = re.search(r'<h([1-6])[^>]*\bid="([^"]+)"', lines[j])
        if m:
            chunk = ' '.join(lines[j:j + 3])
            end = chunk.find('</h%s>' % m.group(1))
            chunk = chunk[:end] if end >= 0 else chunk
            chunk = re.sub(r'<a class="drsc-es-header-anchor".*?</a>', '', chunk)
            return m.group(2), re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', chunk))).strip()
    return 'line', re.sub(r'\s+', ' ', lines[i].strip())[:60]


def occurrences(lines):
    occ = collections.defaultdict(list)
    for i, s in enumerate(lines):
        for m in ID_RE.finditer(s):
            occ[m.group(1)].append(i)
    return occ


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('file', nargs='?', default='DRSC-ES.html')
    ap.add_argument('--baseline', help='git revision to compare against (e.g. main, HEAD~1)')
    ap.add_argument('--baseline-file', help='path of the file inside the baseline revision '
                    '(default: FILE relative to the repository root)')
    ap.add_argument('--allow-target-change', action='append', metavar='ID',
                    help='duplicate id whose new target is intended (repeatable)')
    ap.add_argument('--max-duplicates', type=int, help='fail if there are more duplicate ids than this')
    ap.add_argument('--verbose', '-v', action='store_true', help='list every finding')
    args = ap.parse_args()

    path = Path(args.file)
    text = path.read_text(encoding='utf-8')
    lines = text.split('\n')
    failed = False

    def show(items, limit=15):
        items = list(items)
        for x in items if args.verbose else items[:limit]:
            print('    ' + str(x))
        if not args.verbose and len(items) > limit:
            print(f'    ... {len(items) - limit} more (use --verbose)')

    # 1. anchors
    occ = occurrences(lines)
    hrefs = collections.Counter(HREF_RE.findall(text))
    broken = sorted(h for h in hrefs if h not in occ)
    print(f'[anchors] {sum(hrefs.values())} internal links, {len(broken)} broken')
    if broken:
        failed = True
        show(broken)

    # 2. duplicate ids
    dups = {k: v for k, v in occ.items() if len(v) > 1}
    print(f'[duplicate ids] {len(dups)}')
    if args.verbose:
        show(sorted(dups))
    if args.max_duplicates is not None and len(dups) > args.max_duplicates:
        print(f'    more than the allowed {args.max_duplicates}')
        failed = True

    # 3. structure
    sc = StructureChecker()
    sc.feed(text)
    errors = sc.finish()
    print(f'[structure] {len(errors)} errors')
    if errors:
        failed = True
        show(errors)

    # 4. heading levels
    skips = []
    prev = None
    for i, s in enumerate(lines):
        for m in HEADING_RE.finditer(s):
            lv = int(m.group(1))
            if prev and lv > prev + 1:
                hid = ID_RE.search(s[m.start():])
                skips.append(f'line {i + 1}: h{prev} -> h{lv} ({hid.group(1) if hid else "?"})')
            prev = lv
    print(f'[heading levels] {len(skips)} skipped levels (informational)')
    if args.verbose:
        show(skips)

    # 5-7. baseline comparison
    if args.baseline:
        try:
            if args.baseline_file:
                rel = args.baseline_file
            else:
                root = subprocess.run(['git', 'rev-parse', '--show-toplevel'], check=True,
                                      capture_output=True, text=True).stdout.strip()
                rel = path.resolve().relative_to(Path(root).resolve()).as_posix()
            base_text = subprocess.run(['git', 'show', f'{args.baseline}:{rel}'],
                                       check=True, capture_output=True, text=True).stdout
        except subprocess.CalledProcessError as e:
            print(f'[baseline] cannot read {args.baseline}:{path}: {e.stderr.strip()}')
            return 1
        blines = base_text.split('\n')
        bocc = occurrences(blines)
        bids = collections.Counter({k: len(v) for k, v in bocc.items()})
        nids = collections.Counter({k: len(v) for k, v in occ.items()})
        added, removed = nids - bids, bids - nids
        print(f'[ids vs {args.baseline}] {sum(added.values())} added, {sum(removed.values())} removed')
        if added:
            print('  added:'); show(sorted(added))
        if removed:
            print('  removed:'); show(sorted(removed))

        bdups = {k for k, v in bocc.items() if len(v) > 1}
        print(f'[duplicate ids vs {args.baseline}] {len(bdups)} -> {len(dups)}')
        if args.max_duplicates is None and len(dups) > len(bdups):
            print('    duplicate ids increased')
            failed = True

        moved = []
        allowed = set(args.allow_target_change or [])
        for k in sorted(bdups):
            if k in occ:
                was = id_owner(blines, bocc[k][0])
                sigs = [id_owner(lines, i) for i in occ[k]]
                now = sigs[0]
                if was == now:
                    continue
                if was in sigs:
                    changed = True                 # the old target is still there, but no longer first
                else:
                    changed = was[0] != now[0]     # same heading id: the element was renamed
                if changed and k not in allowed:
                    nrefs = hrefs.get(k, 0)
                    moved.append(f'#{k} ({nrefs} links): was "{was[1]}" <{was[0]}>, '
                                 f'now "{now[1]}" <{now[0]}>')
        print(f'[duplicate-id targets vs {args.baseline}] {len(moved)} changed')
        if moved:
            print('    links to these ids may now open a different element:')
            show(moved)
            failed = True

        bw, nw = words(base_text), words(text)
        wa, wr = nw - bw, bw - nw
        print(f'[words vs {args.baseline}] {sum(bw.values())} -> {sum(nw.values())} '
              f'(+{sum(wa.values())} / -{sum(wr.values())})')
        if args.verbose:
            print('  removed:', ' '.join(f'{w}×{n}' if n > 1 else w for w, n in wr.most_common()))
            print('  added:  ', ' '.join(f'{w}×{n}' if n > 1 else w for w, n in wa.most_common()))

    print('FAIL' if failed else 'OK')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
