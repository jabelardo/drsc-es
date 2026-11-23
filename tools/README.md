# Herramientas

Checks and generators for `DRSC-ES.html`, and the builds for the PDFs.
They need Python 3.8+ and only the standard library; `render.py` also needs Chrome or
Chromium, and the Typst builds need Typst. Run them from the repository root.

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
- **Arc phrases:** each arc is shown in a first-person phrase, after OG-CSRD's generator
  ("Debo cobrar [venganza] por alguien o por algo"). The phrases live in `FRASES_ARCOS` in the
  script, keyed by the arc's id, and the build fails if an arc has none.
- **When:** re-run it after adding descriptors, flavors, foci or arcs. A new arc also needs a
  phrase in `FRASES_ARCOS`.

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

## `../book/build.sh` — the book PDF

```sh
book/build.sh                          # writes "DOCUMENTO DE REFERENCIA DEL SISTEMA CYPHER.pdf"
book/build.sh /tmp/prueba.pdf          # or any other path
TYPST=/path/to/typst book/build.sh
```

- **What:** `book/html2typ.py` converts `DRSC-ES.html` into `book/build/contenido.typ` (ignored by
  git), and Typst lays it out with `book/libro.typ` (cover and table of contents) and
  `book/plantilla.typ` (every component: part pages, chapter openers, headings, boxes, sidebars,
  quick references, creature bars, tables, the example-of-play dialogue). The PDF replaces the
  one made from the old ODT, which is no longer kept or distributed.
- **Look:** inspired by the layout of the *Cypher System Rulebook* (page size, two columns,
  running heads, page-number circles, chapter openers, coloured boxes and creature bars); no
  images or text are taken from it. Part colours are the ones in `css/drsc-es.css`.
- **Fonts:** only `book/fonts`, all under the SIL Open Font License (texts included): Teko for
  titles, Alegreya Sans for text, Aldrich for labels and running heads. The build passes
  `--ignore-system-fonts`, so the result does not depend on the machine. The two characters these
  fonts lack are handled in the template (the ⚡ cyberware mark is drawn, ℞ becomes "Rx").
- **Checks:** every HTML id becomes a PDF destination, and links to ids missing from the output
  fall back to plain text. The PDF is untagged, as before (tagging nearly triples its size).
- **Chapter-end art:** where a chapter ends with space to spare, the page background draws an
  illustration from `book/assets/arte/` (across both columns below the text, or in the empty right
  column), with edges that fade into the page; smaller spaces get an original vector ornament.
  Placement keeps clear of page-wide floats (wide tables, boxes, chapter openers), which mark where
  they start and end. `book/arte/fuentes.json` maps chapters to Wikimedia Commons files, all public
  domain or CC0, and holds their credits (Spanish title, author, date), which the book prints on its
  last page with the page each one illustrates. No Monte Cook Games art is used: the Cypher System
  Open License forbids it.
- **Refreshing the art (optional):** `python3 book/arte/preparar.py` (needs Pillow and network) checks
  each file's licence through the Commons API, refuses anything that is not public domain or CC0,
  downloads it, tones it as a duotone in its part's colour and records the licence and source. For a
  new entry it drafts the title, author and date from the Commons metadata; edit them in the manifest
  (reruns keep them). It pauses between files because Wikimedia rate-limits bursts (set
  `WIKIMEDIA_CONTACT` to an email or URL of your own for a shorter pause); rerun it to resume.
  `--solo CAPITULO` redoes one image.
- **Requires:** Python 3 (standard library) and Typst 0.15 or later; a full build takes about
  15 seconds.
