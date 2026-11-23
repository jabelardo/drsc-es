#!/usr/bin/env bash
# Build the DRSC-ES book PDF from DRSC-ES.html: html2typ.py writes book/build/contenido.typ, and
# Typst lays it out with book/plantilla.typ and only the fonts in book/fonts.
# The PDF is untagged (as the old one was): tagging nearly triples its size.
# Requires: python3 and typst on PATH (or set TYPST=/path/to/typst).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$(realpath -m "${1:-$ROOT/DOCUMENTO DE REFERENCIA DEL SISTEMA CYPHER.pdf}")"
TYPST="${TYPST:-typst}"

if ! command -v "$TYPST" >/dev/null 2>&1; then
  echo "error: typst not found. Install it (https://typst.app) or set TYPST=/path/to/typst." >&2
  exit 1
fi

python3 "$ROOT/book/html2typ.py" --es "$ROOT/DRSC-ES.html" --out "$ROOT/book/build/contenido.typ"
"$TYPST" compile \
  --root "$ROOT" \
  --ignore-system-fonts \
  --no-pdf-tags \
  --font-path "$ROOT/book/fonts" \
  "$ROOT/book/libro.typ" \
  "$OUT"
echo "built: $OUT"
