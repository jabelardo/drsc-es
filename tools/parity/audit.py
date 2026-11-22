#!/usr/bin/env python3
"""Source-attribution audit: compare DRSC-ES.html with OG-CSRD and print a Markdown
report (the method behind §3 of PLAN-FULL-PARITY.md).

OG-CSRD tags every section with its source book (og-cite) and every ability with an
inline page reference. The audit uses those tags to split OG content into:
  - books DRSC-ES already covers (see COVERED),
  - the supplements DRSC-ES does not cover yet (see SUPPLEMENTS),
  - OG editorial additions.
It matches DRSC-ES game elements to OG by the English name in brackets
("Nombre [English Name]") and reports:
  1. OG words per chapter by source
  2. Spanish chapter size against the OG words from covered books
  3. Spanish named entries that sit outside their OG chapter
  4. Named OG entries from covered books with no Spanish match

The "errata" column holds abilities OG cites as Errata (CSRD 2025 revisions).

Usage:
  python3 tools/parity/audit.py [--og PATH_OR_URL] [--es DRSC-ES.html] [--refresh] [--out FILE]

By default OG-CSRD is downloaded once from OG_URL into .cache/og-csrd.html.
When a supplement gets translated, move it from SUPPLEMENTS to COVERED; when a
chapter is added to DRSC-ES, add its heading id to ES_TO_OG.
"""
import argparse
import collections
import html
import re
import sys
import unicodedata
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

OG_URL = 'https://callmepartario.github.io/og-csrd/index.html'
CACHE = Path('.cache/og-csrd.html')

# Source books DRSC-ES translates (as named in OG citations) and their ability abbreviations
COVERED = {'Cypher System Rulebook': 'CSR', 'Godforsaken': 'GF', 'The Stars are Fire': 'SF',
           'We Are All Mad Here': 'WAAMH', 'Claim the Sky': 'CTS', 'Stay Alive!': 'SA',
           'Cypher Shorts': 'CS'}
SUPPLEMENTS = {"It's Only Magic": 'IOM', 'Neon Rain': 'NR', 'High Noon at Midnight': 'HNAM',
               'Rust and Redemption': 'RR'}
# OG sections whose citation sits on a sibling heading rather than on the section itself
SOURCE_FIXES = {'optional-rule-cantrips-by-alphabetical-order': "It's Only Magic",
                'mutations-by-alphabetical-order': 'Rust and Redemption',
                # uncited; sits among the Rust and Redemption descriptors (verify in WP2)
                'post-apocalyptic-species-mutant': 'Rust and Redemption'}
# Known naming differences: normalized OG name -> normalized DRSC-ES name
NAME_ALIASES = {
    'air elemental': 'elemental air', 'thorn elemental': 'elemental thorn',
    'water elemental': 'elemental water', 'fire elemental': 'elemental fire',
    'earth elemental': 'elemental earth', 'ichthysians': 'ichthysian',
    'photonomorphs': 'photonomorph', 'jotunn norse giant': 'jotunn',
    'natathim homo aquus': 'natathim', 'wraith homo vacuus': 'wraith sci fi',
    'robber': 'robber thief', 'detonation desiccating': 'detonation dessicating',
    'mind stablizer': 'mind stabilizer', 'wields an enchanted weapon': 'weilds an enchanted weapon',
    'jotunn norse giant': 'jotunn gigante nordico', 'supervillain': 'supervillanos',
    'sphere 23': 'spehre 23', 'empathic ray': 'empathetic ray',
}

# DRSC-ES chapter heading id -> OG chapter heading id
ES_TO_OG = {
    'como-jugar-al-sistema-cypher': 'chapter-3-how-to-play-the-cypher-system',
    'creacion-de-personajes': 'chapter-4-creating-your-character',
    'seleccionar-tipo': 'chapter-5-type',
    'seleccionar-aspecto': 'chapter-6-flavor',
    'descriptores-de-personaje': 'chapter-7-descriptor',
    'seleccionar-rasgo': 'chapter-8-focus',
    'seleccionar-capacidad': 'chapter-9-abilities',
    'listado-de-capacidades': 'chapter-9-abilities',
    'seleccionar-equipo': 'chapter-10-equipment',
    'seleccionar-reglas': 'chapter-11-rules-of-the-game',
    'seleccionar-seguidores-y-facciones': 'chapter-11-a-followers-and-factions',
    'seleccionar-puntos-de-experiencia': 'chapter-12-experience-points',
    'seleccionar-fantasia': 'chapter-13-fantasy',
    'seleccionar-moderno': 'chapter-14-modern',
    'seleccionar-ciencia-ficcion': 'chapter-15-science-fiction',
    'seleccionar-horror': 'chapter-16-horror',
    'seleccionar-romance': 'chapter-17-romance',
    'seleccionar-superheroes': 'chapter-18-superheroes',
    'seleccionar-post-apocaliptico': 'chapter-19-post-apocalyptic',
    'seleccionar-cuentos-de-hadas': 'chapter-20-fairy-tale',
    'seleccionar-historico': 'chapter-21-historical',
    'seleccionar-criaturas': 'chapter-22-creatures',
    'seleccionar-pnjs': 'chapter-23-npcs',
    'seleccionar-cyphers': 'chapter-24-cyphers',
    'seleccionar-dirigir-el-sistema-cypher': 'chapter-25-running-the-cypher-system',
    'cypher-cortos': 'cypher-shorts',
    'atrapado-en-llamas': 'trapped-in-flames',
}
# Named OG entries checked in report 4: an entry heading class plus an id of a kind that
# DRSC-ES labels with its English name (equipment items are named only in Spanish)
ENTRY_CLASSES = {'og-border', 'og-tab', 'og-tab-sub', 'og-h-h6-icon', 'og-h-h5-icon'}
ENTRY_ID = re.compile(r'^(focus|descriptor|creature|npc|cypher)-(?!shorts)|-(species|descriptor|cypher|artifact)-')


class Outline(HTMLParser):
    """Headings with level, id, text, own word count and (for OG) citations."""

    def __init__(self, cite_class=None):
        super().__init__(convert_charrefs=True)
        self.rows = []
        self.cite_class = cite_class
        self.in_h = None
        self.htext = []
        self.skip = 0
        self.cite_depth = 0
        self.cite_buf = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ('script', 'style'):
            self.skip += 1
        if self.cite_depth:
            self.cite_depth += 1
        elif self.cite_class and self.cite_class in (a.get('class') or '').split():
            self.cite_depth, self.cite_buf = 1, []
        m = re.fullmatch(r'h([1-6])', tag)
        if m:
            self.in_h = (int(m.group(1)), a.get('id', ''), a.get('class') or '')
            self.htext = []

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip -= 1
        if self.cite_depth:
            self.cite_depth -= 1
            if self.cite_depth == 0 and self.rows:
                txt = re.sub(r'\s+', ' ', ''.join(self.cite_buf))
                self.rows[-1]['cites'] += [s.strip() for s in re.findall(r'\(([^,()]+?)(?:,[^()]*)?\)', txt)]
        if self.in_h and re.fullmatch(r'h[1-6]', tag):
            t = re.sub(r'\s+', ' ', ''.join(self.htext)).strip()
            self.rows.append({'level': self.in_h[0], 'id': self.in_h[1], 'cls': set(self.in_h[2].split()),
                              'text': t, 'words': 0, 'cites': []})
            self.in_h = None

    def handle_data(self, d):
        if self.skip:
            return
        if self.cite_depth:
            self.cite_buf.append(d)
        elif self.in_h:
            self.htext.append(d)
        elif self.rows:
            self.rows[-1]['words'] += len(d.split())


def canon_source(s):
    s = s.replace('Ruleybook', 'Rulebook').replace('Say Alive', 'Stay Alive')
    if s.startswith('Stay Alive'):
        return 'Stay Alive!'
    if s.startswith('Godforsaken'):
        return 'Godforsaken'
    if s.startswith('We Are All Mad'):
        return 'We Are All Mad Here'
    if 'Editorial' in s:
        return 'OG editorial'
    return s


def bucket(src):
    if src in COVERED:
        return 'covered'
    if src in SUPPLEMENTS:
        return SUPPLEMENTS[src]
    return 'OG'


def norm(name):
    name = ''.join(c for c in unicodedata.normalize('NFD', name) if unicodedata.category(c) != 'Mn')
    name = re.sub(r'\d+\s*\((\d+|∞|infinito)\)\+?', '', name).lower().replace('’', "'")
    name = re.sub(r'^(quick reference:|optional rule:)\s*', '', name)
    return re.sub(r'[^a-z0-9]+', ' ', name).strip()


def load_og(arg, refresh):
    if arg and not re.match(r'https?://', arg):
        return Path(arg).read_text(encoding='utf-8')
    url = arg or OG_URL
    if CACHE.exists() and not refresh and not arg:
        return CACHE.read_text(encoding='utf-8')
    req = urllib.request.Request(url, headers={'User-Agent': 'drsc-es-parity-audit'})
    data = urllib.request.urlopen(req, timeout=120).read().decode('utf-8')
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(data, encoding='utf-8')
    return data


def og_chapters(rows):
    ch, out = None, []
    for r in rows:
        if r['level'] <= 3:
            ch = r['id']
        out.append(ch)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--og', help=f'OG-CSRD HTML file or URL (default: {OG_URL}, cached in {CACHE})')
    ap.add_argument('--es', default='DRSC-ES.html')
    ap.add_argument('--refresh', action='store_true', help='download OG-CSRD again')
    ap.add_argument('--out', help='write the report to this file instead of stdout')
    args = ap.parse_args()

    og_html = load_og(args.og, args.refresh)
    es_html = Path(args.es).read_text(encoding='utf-8')
    version = re.search(r'version (\d+\.\d+[a-z]?)\s*\((\d{4}-\d{2}-\d{2})\)', og_html)

    og = Outline('og-cite'); og.feed(og_html); og_rows = og.rows
    es = Outline(); es.feed(es_html); es_rows = es.rows
    og_ch = og_chapters(og_rows)
    og_title = {r['id']: r['text'] for r in og_rows if r['level'] <= 3}

    # effective source per OG heading: own citation, else nearest ancestor's
    stack, eff = [], []
    for r in og_rows:
        while stack and stack[-1][0] >= r['level']:
            stack.pop()
        own = [canon_source(c) for c in r['cites']]
        if r['id'] in SOURCE_FIXES:
            src = SOURCE_FIXES[r['id']]
        elif own:
            non_og = [c for c in own if c != 'OG editorial']
            src = non_og[0] if non_og else 'OG editorial'
        else:
            src = stack[-1][1] if stack else 'OG editorial'
        stack.append((r['level'], src))
        eff.append(src)

    # abilities: split the alphabetical lists per entry by their inline reference
    abbr_bucket = {v: 'covered' for v in COVERED.values()}  # pages without a book name are the Rulebook
    abbr_bucket.update({v: v for v in SUPPLEMENTS.values()})
    abilities = re.findall(r'<li id="(ability-[^"]+)">(.*?)</li>', og_html, re.S)
    ab_words = collections.Counter()
    ab_count = collections.Counter()
    og_ability_names = {}
    for aid, body in abilities:
        refs = re.findall(r'<span class="og-ref">\(([^)]*)\)</span>', body)
        books = [re.match(r"([A-Za-z!&' ]+),", r).group(1).strip() for r in refs if re.match(r"([A-Za-z!&' ]+),", r)]
        if not refs:
            b = 'OG'
        elif books:
            b = abbr_bucket.get(books[0], 'covered')
        elif any(r.strip().startswith('Errata') for r in refs):
            b = 'errata'
        else:
            b = 'covered'
        w = len(html.unescape(re.sub(r'<[^>]+>', ' ', body)).split())
        ab_words[b] += w
        ab_count[b] += 1
        name = re.search(r'<strong>([^<(:]+)', body)
        if name:
            og_ability_names[norm(name.group(1))] = b

    # 1. OG words per chapter by source
    cols = ['covered'] + list(SUPPLEMENTS.values()) + ['errata', 'OG']
    per = collections.defaultdict(collections.Counter)
    for r, ch, src in zip(og_rows, og_ch, eff):
        if ch is None or (r['text'].startswith('Abilities—') and ch == 'chapter-9-abilities'):
            continue
        per[ch][bucket(src)] += r['words']
    per['chapter-9-abilities'].update(ab_words)

    out = []
    p = out.append
    p('# DRSC-ES ↔ OG-CSRD source audit\n')
    p(f'OG-CSRD {"v" + version.group(1) + " (" + version.group(2) + ")" if version else "(version not found)"}; '
      f'DRSC-ES: `{args.es}`. Word counts are English words in OG-CSRD and include OG\'s inline page references.\n')
    p('Covered books: ' + ', '.join(COVERED) + '. Supplements not covered yet: '
      + ', '.join(f'{k} ({v})' for k, v in SUPPLEMENTS.items()) + '.\n')
    p('## 1. OG-CSRD words per chapter by source\n')
    p('| OG chapter | ' + ' | '.join(cols) + ' |')
    p('|---|' + '---:|' * len(cols))
    tot = collections.Counter()
    for ch in dict.fromkeys(c for c in og_ch if c):
        c = per[ch]
        if not sum(c.values()):
            continue
        tot.update(c)
        p(f'| {og_title.get(ch, ch)} | ' + ' | '.join(f'{c[k]:,}' for k in cols) + ' |')
    p('| **Total** | ' + ' | '.join(f'**{tot[k]:,}**' for k in cols) + ' |\n')
    p('Abilities by source: ' + ', '.join(f'{k} {ab_count[k]}' for k in cols if ab_count[k]) + '.\n')

    # 2. Spanish chapter size vs OG covered words
    es_ch_rows, cur = collections.Counter(), None
    es_chapter_of = []
    for r in es_rows:
        if r['level'] <= 3:
            cur = r['id'] if r['id'] in ES_TO_OG else None
        es_chapter_of.append(cur)
        if cur:
            es_ch_rows[cur] += r['words']
    es_title = {r['id']: r['text'] for r in es_rows if r['level'] <= 3}
    p('## 2. Spanish chapter size against OG words from covered books\n')
    p('Spanish usually runs 1.1–1.2 × English; ratios well below 1 suggest missing content, well above 1 misplaced content.\n')
    p('| DRSC-ES chapter | OG chapter | ES words | OG words (covered) | ratio |')
    p('|---|---|---:|---:|---:|')
    by_og = collections.defaultdict(list)
    for es_id, og_id in ES_TO_OG.items():
        by_og[og_id].append(es_id)
    for og_id, es_ids in by_og.items():
        esw = sum(es_ch_rows[e] for e in es_ids)
        ogw = per[og_id]['covered']
        ratio = f'{esw / ogw:.2f}' if ogw else '—'
        names = ' + '.join(es_title.get(e, e) for e in es_ids)
        p(f'| {names} | {og_title.get(og_id, og_id)} | {esw:,} | {ogw:,} | {ratio} |')
    p('')

    # 3. placement of named Spanish entries
    og_idx = collections.defaultdict(set)
    for r, ch in zip(og_rows, og_ch):
        og_idx[norm(r['text'])].add(ch)
    misplaced, matched = [], 0
    es_names = set()
    for r, ch in zip(es_rows, es_chapter_of):
        es_names.add(norm(re.sub(r'\[.*', '', r['text'])))   # names identical in both languages
        m = re.search(r'\[([^\]]*[A-Za-z][^\]]*)\]', r['text'])
        if not m:
            continue
        n = norm(m.group(1))
        es_names.add(n)
        hits = og_idx.get(n)
        if not hits or not ch:
            continue
        matched += 1
        if ES_TO_OG[ch] not in hits:
            misplaced.append((es_title.get(ch, ch), r['text'][:70], ', '.join(sorted(og_title.get(h, h) for h in hits))))
    for m in re.finditer(r'<strong>([^<\[]+)\[([^\]]+)\]', es_html):
        es_names.add(norm(m.group(2)))

    def in_es(og_name):
        n = norm(og_name)
        return n in es_names or NAME_ALIASES.get(n) in es_names
    p('## 3. Spanish named entries outside their OG chapter\n')
    p(f'{matched} Spanish headings carry an English name that matches an OG heading; '
      f'{len(misplaced)} sit outside the OG chapter their Spanish chapter maps to.\n')
    if misplaced:
        p('| DRSC-ES chapter | Entry | OG chapter(s) with that name |')
        p('|---|---|---|')
        for row in misplaced:
            p('| ' + ' | '.join(x.replace('|', '/') for x in row) + ' |')
        p('')

    # 4. named OG entries from covered books with no Spanish match
    missing = []
    for r, ch, src in zip(og_rows, og_ch, eff):
        if r['cls'] & ENTRY_CLASSES and ENTRY_ID.search(r['id']) and r['level'] >= 5 and bucket(src) == 'covered':
            if not in_es(r['text']) and not r['text'].endswith(' by Level'):
                missing.append((og_title.get(ch, ch), r['text'], src))
    ab_missing = sorted(n for n, b in og_ability_names.items() if b == 'covered' and not in_es(n))
    ab_errata = sorted(n for n, b in og_ability_names.items() if b == 'errata' and not in_es(n))
    p('## 4. Named OG entries from covered books with no Spanish match\n')
    p('Candidates for WP2. Some are naming differences rather than gaps; check each one.\n')
    if missing:
        p('| OG chapter | Entry | Source |')
        p('|---|---|---|')
        for row in missing:
            p('| ' + ' | '.join(x.replace('|', '/') for x in row) + ' |')
    p(f'\nAbilities from covered books with no Spanish match: {len(ab_missing)}'
      + (': ' + ', '.join(ab_missing) if ab_missing else '') + '\n')
    p(f'Abilities OG marks as "Errata" (CSRD 2025 revisions) with no Spanish match: {len(ab_errata)}'
      + (': ' + ', '.join(ab_errata) if ab_errata else '') + '\n')

    report = '\n'.join(out)
    if args.out:
        Path(args.out).write_text(report + '\n', encoding='utf-8')
        print(f'wrote {args.out}')
    else:
        print(report)
    return 0


if __name__ == '__main__':
    sys.exit(main())
