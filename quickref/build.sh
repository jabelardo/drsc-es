#!/usr/bin/env bash
# Build the Spanish quick-reference PDF from the Typst source.
# Requires: python3 (+ segno for the QR) and typst on PATH (or set TYPST=/path/to/typst).
set -euo pipefail
cd "$(dirname "$0")"
ROOT="$(cd .. && pwd)"
TYPST="${TYPST:-typst}"
OUT="$ROOT/pdfs/cypher-kur-csqr-kurviak-sistema-cypher-referencia-rapida.pdf"

if ! command -v "$TYPST" >/dev/null 2>&1; then
  echo "error: typst not found. Install it (https://typst.app) or set TYPST=/path/to/typst." >&2
  exit 1
fi

python3 gen_assets.py
mkdir -p "$ROOT/pdfs"
"$TYPST" compile \
  --root "$ROOT" \
  --font-path "$ROOT/quickref/assets/fonts" \
  "$ROOT/quickref/quickref-es.typ" \
  "$OUT"
echo "built: $OUT"
