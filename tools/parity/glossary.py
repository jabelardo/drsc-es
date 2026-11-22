#!/usr/bin/env python3
"""Regenerate the named-element part of GLOSARIO.md from DRSC-ES.html.

DRSC-ES writes game elements as "Nombre en español [English Name]". This script
collects every such pair (headings and ability names), groups them by kind, lists
English names translated in more than one way, and replaces the text between the
GENERATED markers in GLOSARIO.md. The hand-written part above the markers is kept.

Usage:
  python3 tools/parity/glossary.py [--es DRSC-ES.html] [--glossary GLOSARIO.md] [--check]

--check exits with status 1 if GLOSARIO.md is out of date, without writing it.
"""
import argparse
import collections
import html
import re
import sys
import unicodedata
from pathlib import Path

BEGIN = '<!-- BEGIN GENERATED: tools/parity/glossary.py -->'
END = '<!-- END GENERATED -->'
KINDS = ['Capacidades', 'Rasgos', 'Descriptores', 'Tipos y opciones', 'Cyphers', 'Artefactos',
         'Criaturas', 'PNJs', 'Rituales y trampas', 'Otros']
LEVEL = re.compile(r'\s*(\d+\s*\((\d+|infinito|∞)\)|Variable)\s*\+?\s*$')


def clean(s):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s))).strip()


def fold(s):
    s = ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip()


def collect(text):
    lines = text.split('\n')
    pairs = []          # (kind, english, spanish)
    chapter = section = sub = ''
    for i, line in enumerate(lines):
        m = re.search(r'<h([1-6])[^>]*\bid="([^"]+)"', line)
        if m:
            lv, hid = int(m.group(1)), m.group(2)
            chunk = ' '.join(lines[i:i + 3])
            end = chunk.find('</h%d>' % lv)
            chunk = chunk[:end] if end >= 0 else chunk
            chunk = re.sub(r'<span class="float-end">.*?</span>', '', chunk)
            chunk = re.sub(r'<a class="drsc-es-header-anchor".*?</a>', '', chunk)
            title = clean(chunk)
            if 'referencia-rapida' in hid:
                continue
            b = re.search(r'^(.*?)\[([^\]]*[A-Za-z][^\]]*)\]', title)
            if lv <= 3:
                chapter, section, sub = hid, '', ''
            elif lv == 4 and not b:
                section, sub = title, ''
            elif lv == 5 and not b and 'drsc-es-tabbed-item' not in line:
                sub = title
            if b and lv >= 4:
                es, en = LEVEL.sub('', b.group(1)).strip(), LEVEL.sub('', b.group(2)).strip()
                if es and en:
                    pairs.append((kind_of(chapter, section, sub), en, es))
        for a in re.finditer(r'<strong>([^<\[]+)\[([^\]]+)\]', line):
            es, en = a.group(1).strip(), a.group(2).strip()
            if chapter in ('seleccionar-capacidad', 'listado-de-capacidades'):
                pairs.append(('Capacidades', en, es))
    return pairs


def kind_of(chapter, section, sub):
    s = (sub + ' | ' + section).lower()
    if chapter == 'seleccionar-criaturas':
        return 'Criaturas'
    if chapter == 'seleccionar-pnjs':
        return 'PNJs'
    if 'descriptor' in sub.lower():
        return 'Descriptores'
    if chapter == 'seleccionar-rasgo' or 'rasgo' in s:
        return 'Rasgos'
    if chapter == 'descriptores-de-personaje' or 'descriptor' in s:
        return 'Descriptores'
    if chapter == 'seleccionar-cuentos-de-hadas' and 'bestias y seres' in s:
        return 'Criaturas'
    if chapter == 'seleccionar-tipo' or 'opciones de personaje' in s:
        return 'Tipos y opciones'
    if 'cypher' in s:
        return 'Cyphers'
    if 'artefacto' in s or 'vehículos como' in s or (sub.lower() == 'armas' and 'armamento' in s):
        return 'Artefactos'
    if 'ritual' in s or 'calabozos' in s or 'trampa' in s:
        return 'Rituales y trampas'
    return 'Otros'


def render(pairs):
    by_kind = collections.defaultdict(dict)
    by_en = collections.defaultdict(set)
    for kind, en, es in pairs:
        by_kind[kind].setdefault(en, set()).add(es)
        by_en[fold(en)].add((en, es, kind))
    out = [BEGIN, '',
           '## Nombres de elementos de juego (generado)', '',
           'Extracted from `DRSC-ES.html` ("Nombre [English Name]" in headings and ability names). '
           'Do not edit by hand; run `python3 tools/parity/glossary.py`.', '']
    total = sum(len(v) for v in by_kind.values())
    out.append('| Kind | Entries |')
    out.append('|---|---:|')
    for k in KINDS:
        if by_kind.get(k):
            out.append(f'| [{k}](#{fold(k).replace(" ", "-")}) | {len(by_kind[k])} |')
    out.append(f'| **Total** | **{total}** |')
    out.append('')

    conflicts = []
    for key, items in sorted(by_en.items()):
        spanish = {fold(es) for en, es, kind in items}
        if len(spanish) > 1:
            conflicts.append(items)
    out.append('### Nombres en inglés con más de una traducción')
    out.append('')
    out.append('Review these against §7 of the plan (one canonical Spanish term per English term). '
               'Some are legitimate (an ability and a cypher with the same English name).')
    out.append('')
    if conflicts:
        out.append('| English | Español (kind) |')
        out.append('|---|---|')
        for items in conflicts:
            en = sorted({e for e, _, _ in items})[0]
            es = '; '.join(sorted({f'{s} ({k})' for _, s, k in items}))
            out.append(f'| {en} | {es} |')
    else:
        out.append('None.')
    out.append('')

    for k in KINDS:
        entries = by_kind.get(k)
        if not entries:
            continue
        out.append(f'### {k}')
        out.append('')
        out.append('| English | Español |')
        out.append('|---|---|')
        for en in sorted(entries, key=fold):
            out.append(f'| {en.replace("|", "/")} | {" / ".join(sorted(entries[en])).replace("|", "/")} |')
        out.append('')
    out.append(END)
    return '\n'.join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--es', default='DRSC-ES.html')
    ap.add_argument('--glossary', default='GLOSARIO.md')
    ap.add_argument('--check', action='store_true', help='only report whether the file is up to date')
    args = ap.parse_args()

    generated = render(collect(Path(args.es).read_text(encoding='utf-8')))
    path = Path(args.glossary)
    current = path.read_text(encoding='utf-8') if path.exists() else ''
    if BEGIN in current and END in current:
        new = current[:current.index(BEGIN)] + generated + current[current.index(END) + len(END):]
    else:
        new = current.rstrip('\n') + ('\n\n' if current else '') + generated + '\n'
    if args.check:
        print('up to date' if new == current else f'{path} is out of date')
        return 0 if new == current else 1
    path.write_text(new, encoding='utf-8')
    print(f'wrote {path}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
