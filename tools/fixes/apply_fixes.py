#!/usr/bin/env python3
"""Apply the pending text corrections in CORRECCIONES.json to the HTML or the ODT.

Each fix replaces visible text (old -> new). Matching ignores markup and treats any run
of whitespace as one space, so it still works when the ODT splits a phrase across
<text:span> elements. Only the characters that actually change are rewritten; the
surrounding markup is kept. A match may not cross a paragraph or heading boundary.

A fix must match exactly once unless it has "all": true. Fixes already applied to the
target (a non-null "applied" value) are skipped.

Usage:
  python3 tools/fixes/apply_fixes.py --target html [--file DRSC-ES.html] [--dry-run] [--record]
  python3 tools/fixes/apply_fixes.py --target odt [--file DOCUMENT.odt] [--dry-run] [--record]
  options: --only ID [--only ID ...]   apply just these fixes

--record writes today's date into "applied" for each fix applied.
Exit status 1 if any pending fix is not found or is ambiguous.
"""
import argparse
import datetime
import html
import json
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

REGISTER = Path('CORRECCIONES.json')
DEFAULTS = {'html': 'DRSC-ES.html', 'odt': 'DOCUMENTO DE REFERENCIA DEL SISTEMA CYPHER.odt'}
# tags that end a block of text: a match may not run across them
BLOCK_END = re.compile(r'^</?(text:p|text:h|p|h[1-6]|li|td|th|div|br|text:line-break|table:table-cell)\b')
ODT_SPACE = re.compile(r'^<text:s(?:\s+text:c="(\d+)")?\s*/>$')
ODT_TAB = re.compile(r'^<text:tab\s*/>$')


def text_view(src):
    """Visible text of src as a list of (char, start, end) in src. Whitespace runs are
    collapsed to one space; block boundaries become '\\n'."""
    out = []
    i, n = 0, len(src)
    in_skip = None
    while i < n:
        c = src[i]
        if c == '<':
            j = src.index('>', i) + 1
            tag = src[i:j]
            low = tag.lower()
            if in_skip:
                if low.startswith('</' + in_skip):
                    in_skip = None
            elif low.startswith('<script') or low.startswith('<style'):
                in_skip = 'script' if low.startswith('<script') else 'style'
            elif BLOCK_END.match(tag):
                out.append(('\n', i, i))
            else:
                m = ODT_SPACE.match(tag)
                if m:
                    out.append((' ', i, j))
                elif ODT_TAB.match(tag):
                    out.append((' ', i, j))
            i = j
            continue
        if in_skip:
            i += 1
            continue
        if c == '&':
            j = src.find(';', i)
            if 0 < j - i < 12:
                ch = html.unescape(src[i:j + 1])
                if ch == '\xa0':
                    ch = ' '
                out.append((ch, i, j + 1))
                i = j + 1
                continue
        out.append((' ' if c.isspace() else c, i, i + 1))
        i += 1
    # collapse whitespace runs
    view = []
    for ch, a, b in out:
        if ch == ' ' and view and view[-1][0] in (' ', '\n'):
            continue
        view.append((ch, a, b))
    return view


def escape(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def plan(src, view, flat, fix):
    """Edits (start, end, replacement) in src for every match of the fix, plus the view
    ranges they touch. Returns (edits, view_ranges, count)."""
    old, new = fix['old'], fix['new']
    starts = [m.start() for m in re.finditer(re.escape(old), flat)]
    if not starts or (len(starts) > 1 and not fix.get('all')):
        return [], [], len(starts)
    # common prefix/suffix: only the middle changes
    p = 0
    while p < min(len(old), len(new)) and old[p] == new[p]:
        p += 1
    q = 0
    while q < min(len(old), len(new)) - p and old[-1 - q] == new[-1 - q]:
        q += 1
    mid_new = escape(new[p:len(new) - q])
    edits, ranges = [], []
    for s in starts:
        a, b = s + p, s + len(old) - q      # changed region in the view
        ranges.append((s, s + len(old)))
        if a == b:                          # pure insertion after view[a-1]
            pos = view[a - 1][2]
            edits.append((pos, pos, mid_new))
            continue
        spans = [(view[k][1], view[k][2]) for k in range(a, b)]
        first, last = spans[0][0], spans[-1][1]
        if '<' not in src[first:last]:
            edits.append((first, last, mid_new))
        else:                               # region crosses markup: drop the chars, keep tags
            seg, pos = [mid_new], first
            for x, y in spans:
                seg.append(src[pos:x])
                pos = y
            seg.append(src[pos:last])
            edits.append((first, last, ''.join(seg)))
    return edits, ranges, len(starts)


def run(src, fixes, label):
    """Apply fixes in register order. Non-overlapping fixes are applied together in one
    pass; a fix that overlaps or depends on an earlier one waits for the next pass."""
    ok = True
    applied = []
    pending = list(fixes)
    counts = {}
    while pending:
        view = text_view(src)
        flat = ''.join(ch for ch, _, _ in view)
        taken, batch, later = [], [], []
        for fix in pending:
            edits, ranges, count = plan(src, view, flat, fix)
            counts[fix['id']] = count
            if not edits:
                later.append(fix)
                continue
            if any(a < d and c < b for a, b in ranges for c, d in taken):
                later.append(fix)           # overlaps an edit planned in this pass
                continue
            taken.extend(ranges)
            batch.append((fix, edits))
        if not batch:
            break
        for start, end, rep in sorted((e for _, es in batch for e in es), reverse=True):
            src = src[:start] + rep + src[end:]
        for fix, edits in batch:
            print(f'  [ok] {fix["id"]}: {len(edits)} replacement(s) in {label}')
            applied.append(fix['id'])
        pending = later
    for fix in pending:
        count = counts.get(fix['id'], 0)
        if count == 0:
            print(f'  [not found] {fix["id"]}: "{fix["old"]}"')
        else:
            print(f'  [ambiguous] {fix["id"]}: {count} matches for "{fix["old"]}"')
        ok = False
    return src, applied, ok


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--target', choices=('html', 'odt'), required=True)
    ap.add_argument('--file', help='file to change (default: the repository HTML or ODT)')
    ap.add_argument('--register', default=str(REGISTER))
    ap.add_argument('--only', action='append', metavar='ID')
    ap.add_argument('--dry-run', action='store_true', help='report only; do not write')
    ap.add_argument('--record', action='store_true', help='record the applied fixes in the register')
    args = ap.parse_args()

    reg_path = Path(args.register)
    reg = json.loads(reg_path.read_text(encoding='utf-8'))
    fixes = [f for f in reg['fixes'] if f['applied'].get(args.target) is None]
    if args.only:
        fixes = [f for f in fixes if f['id'] in args.only]
    path = Path(args.file or DEFAULTS[args.target])
    print(f'{len(fixes)} pending fix(es) for {args.target}: {path}')
    if not fixes:
        return 0

    if args.target == 'html':
        src = path.read_text(encoding='utf-8')
        new, applied, ok = run(src, fixes, path.name)
        if applied and not args.dry_run:
            path.write_text(new, encoding='utf-8')
    else:
        with zipfile.ZipFile(path) as z:
            infos = z.infolist()
            data = {i.filename: z.read(i.filename) for i in infos}
        src = data['content.xml'].decode('utf-8')
        new, applied, ok = run(src, fixes, 'content.xml')
        if applied and not args.dry_run:
            data['content.xml'] = new.encode('utf-8')
            tmp = Path(tempfile.mkstemp(suffix='.odt', dir=path.parent)[1])
            with zipfile.ZipFile(tmp, 'w') as out:
                for info in infos:   # keep order; mimetype stays first and stored
                    zi = zipfile.ZipInfo(info.filename, date_time=info.date_time)
                    zi.compress_type = info.compress_type
                    zi.external_attr = info.external_attr
                    out.writestr(zi, data[info.filename])
            shutil.move(tmp, path)

    if args.dry_run:
        print('dry run: nothing written')
    elif applied and args.record:
        today = datetime.date.today().isoformat()
        for f in reg['fixes']:
            if f['id'] in applied:
                f['applied'][args.target] = today
        reg_path.write_text(json.dumps(reg, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(f'recorded {len(applied)} fix(es) in {reg_path}')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
