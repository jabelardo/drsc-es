#!/usr/bin/env python3
"""Add fillable form fields to a sheet compiled by Typst.

Reads the <fld> markers (name, kind, page, x, y, w, h in points, origin top-left) that
`typst query` extracts from the sheet source, and adds one widget per marker with PyMuPDF.
Kinds: text, multiline, check (square box), circle (round box).

Usage: add_fields.py fields.json in.pdf out.pdf   (requires: pip install pymupdf)
"""
import json
import sys

import pymupdf

fields_json, src, dst = sys.argv[1:4]
fields = json.load(open(fields_json, encoding='utf-8'))
names = [f['name'] for f in fields]
dupes = {n for n in names if names.count(n) > 1}
assert not dupes, f'duplicate field names: {sorted(dupes)}'
doc = pymupdf.open(src)
for f in fields:
    page = doc[f['page'] - 1]
    r = pymupdf.Rect(f['x'], f['y'], f['x'] + f['w'], f['y'] + f['h'])
    w = pymupdf.Widget()
    w.field_name = f['name']
    w.border_width = 0
    w.fill_color = None
    w.border_color = None
    if f['kind'] in ('check', 'circle'):
        w.field_type = pymupdf.PDF_WIDGET_TYPE_CHECKBOX
        w.rect = r + (1, 1, -1, -1)
        w.text_color = (0.09, 0.37, 0.51)
        w.field_value = False
    else:
        w.field_type = pymupdf.PDF_WIDGET_TYPE_TEXT
        w.text_font = 'Helv'
        w.text_color = (0.07, 0.07, 0.07)
        if f['kind'] == 'multiline':
            w.rect = r + (4, 3, -4, -3)
            w.field_flags |= pymupdf.PDF_TX_FIELD_IS_MULTILINE
            w.text_fontsize = 9
        else:
            w.rect = r + (2, 1, -2, -1)
            w.text_fontsize = 0
    page.add_widget(w)
doc.save(dst, garbage=3, deflate=True)
print(f'{dst}: {len(fields)} fields')
