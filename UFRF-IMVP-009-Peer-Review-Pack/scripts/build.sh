#!/usr/bin/env bash
set -euo pipefail
if command -v pandoc >/dev/null 2>&1; then
  pandoc -s paper/main.md -o paper/main.pdf
  echo "[peer-review] Built paper/main.pdf"
else
  echo "[peer-review] pandoc not found; keep markdown or convert externally."
fi
