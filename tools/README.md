# Herramientas

Read-only helpers for the parity work in `PLAN-FULL-PARITY.md`. They need Python 3.8+
and only the standard library; `render.py` also needs Chrome or Chromium. Run them from
the repository root.

## `qa/check_html.py` — structure, links and ids

```sh
python3 tools/qa/check_html.py                      # check DRSC-ES.html
python3 tools/qa/check_html.py --baseline main      # also compare with main
python3 tools/qa/check_html.py --baseline main --verbose
```

- **Checks:** internal anchors resolve, duplicate ids, balanced and nested container tags,
  skipped heading levels (informational).
- **With `--baseline REF`:** it also lists ids added and removed, words added and removed,
  and duplicated ids whose first occurrence is now a different element. Browsers follow
  the first occurrence, so links to that id would open something else.
- **Intended changes:** acknowledge them with `--allow-target-change ID`. Exit status 1
  means a check failed.
- **When:** run it before every commit that touches `DRSC-ES.html`, with `--baseline` set
  to the branch point.

## `qa/render.py` — headless render in light and dark

```sh
python3 tools/qa/render.py --out /tmp/shots                          # top of the page
python3 tools/qa/render.py --section seleccionar-fantasia --out /tmp/shots
python3 tools/qa/render.py --section vehiculos-modernos --theme dark --lines 200
```

- **Output:** saves a screenshot per theme and fails if the browser console shows
  anything other than the known `manifest.json` message for `file://` pages.
- **Sections:** `--section ID` renders that part of the page as its own page, inside the
  right part container so colours and styles match. Headless Chrome does not scroll to
  anchors, so this is the way to check a section deep in the page.
- **Chrome:** taken from `$CHROME`, else Chrome or Chromium on `PATH`, else the Flatpak
  apps.

## `parity/audit.py` — source-attribution audit against OG-CSRD

```sh
python3 tools/parity/audit.py --out /tmp/audit.md     # downloads OG-CSRD once into .cache/
python3 tools/parity/audit.py --refresh               # download OG-CSRD again
```

- **Method:** splits OG-CSRD content by source book, then matches DRSC-ES entries by
  their `[English Name]`.
- **Report:**
  - OG words per chapter by source
  - Spanish chapter sizes against OG
  - entries outside their OG chapter
  - named OG entries from covered books with no Spanish match
- **Updating:**
  - When a supplement is translated, move it from `SUPPLEMENTS` to `COVERED`.
  - When a chapter is added, map its heading id in `ES_TO_OG`.
  - For new naming differences, add them to `NAME_ALIASES`.

## `fixes/apply_fixes.py` — apply registered text corrections

`CORRECCIONES.json` lists text corrections (old → new) that apply to both editions. The
ODT keeps its own structure and gets only these corrections, not the HTML reorganisation.

```sh
python3 tools/fixes/apply_fixes.py --target html --dry-run      # what would change
python3 tools/fixes/apply_fixes.py --target html --record       # apply and record in the register
python3 tools/fixes/apply_fixes.py --target odt --record        # same for the ODT
```

- **Matching:** visible text only, ignoring markup and collapsing whitespace, so phrases
  split across ODT `<text:span>` elements still match. Only the characters that change
  are rewritten. When a change crosses markup, old and new are aligned word by word, so
  words that stay keep their links and styles.
- **Self-check:** after applying, the visible text must equal the expected result and
  no link may be left without text; otherwise it reports `[check failed]`, writes
  nothing and exits 1. `--dry-run` runs the same check without writing.
- **Order:** fixes apply in register order. Non-overlapping fixes go in one pass; a fix
  that overlaps or depends on an earlier one is applied in the next pass.
- **Pending fixes:** a fix applies once per format; its `applied` entry records the date.
  It must match exactly once unless it has `"all": true`.
- **Adding a fix:** append an entry with a unique `id`, the exact `old` and `new` text
  (long enough to be unique) and `applied` set to `{"html": null, "odt": null}`.

## `parity/glossary.py` — regenerate the named-element part of `GLOSARIO.md`

```sh
python3 tools/parity/glossary.py           # rewrite the generated section
python3 tools/parity/glossary.py --check   # exit 1 if GLOSARIO.md is out of date
```

It collects every `Nombre [English Name]` pair (headings and ability names) and lists
English names translated in more than one way. The hand-written core terms above the
generated section are kept.

## `generador/build_generador.py` — character sentence generator data

```sh
python3 tools/generador/build_generador.py          # rewrite js/generador-personajes.js
python3 tools/generador/build_generador.py --check  # exit 1 if it is out of date
```

- **What:** collects the core descriptors (Cap. 4), the four types, the flavors (Cap. 5),
  every focus (Cap. 6) and the sample character arcs (Cap. 10), with their ids, and writes
  them into the script behind *Generador de frases de personaje* (Cap. 2).
- **When:** re-run it after adding descriptors, flavors, foci or arcs.

## `../sheets/build.sh` — fillable character sheets

```sh
sheets/build.sh                                   # needs typst and python3 with pymupdf
PYTHON=/path/to/venv/bin/python sheets/build.sh  # if pymupdf lives in a virtualenv
```

- **What:** compiles `sheets/hoja-de-personaje.typ` (KUR-CSCS) and `sheets/hoja-de-camarada.typ`
  (KUR-CSSK) with Typst, then `sheets/add_fields.py` adds a form field for every `<fld>`
  marker the sources leave. Output goes to `pdfs/`.
- **Fonts:** reuses `quickref/assets/fonts` (Teko, Orbitron, Open Sans) and the QR code in
  `quickref/assets/qr.png`.
