#!/usr/bin/env bash
# Build the fillable Spanish character sheets (KUR-CSCS, KUR-CSSK) from the Typst sources.
# Requires: typst on PATH (or set TYPST=/path/to/typst) and python3 with pymupdf (pip install pymupdf;
# or set PYTHON=/path/to/python of a virtualenv that has it).
set -euo pipefail
cd "$(dirname "$0")"
ROOT="$(cd .. && pwd)"
TYPST="${TYPST:-typst}"
PYTHON="${PYTHON:-python3}"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
build() {
  local src="$1" out="$2"
  "$TYPST" compile --root "$ROOT" --font-path "$ROOT/quickref/assets/fonts" "$ROOT/sheets/$src" "$TMP/sheet.pdf"
  "$TYPST" eval 'query(<fld>).map(it => it.value)' --in "$ROOT/sheets/$src" --root "$ROOT" --font-path "$ROOT/quickref/assets/fonts" > "$TMP/fields.json"
  "$PYTHON" "$ROOT/sheets/add_fields.py" "$TMP/fields.json" "$TMP/sheet.pdf" "$ROOT/pdfs/$out"
}
mkdir -p "$ROOT/pdfs"
build hoja-de-personaje.typ cypher-kur-cscs-kurviak-sistema-cypher-hoja-de-personaje.pdf
build hoja-de-camarada.typ cypher-kur-cssk-kurviak-sistema-cypher-hoja-de-camarada.pdf
