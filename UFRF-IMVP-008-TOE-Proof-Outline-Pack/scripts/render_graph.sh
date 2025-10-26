#!/usr/bin/env bash
set -euo pipefail
if command -v dot >/dev/null 2>&1; then
  dot -Tpng docs/ufrf_proof_graph.dot -o artifacts/ufrf_proof_graph.png
  echo "[graphviz] Rendered to artifacts/ufrf_proof_graph.png"
else
  echo "[graphviz] 'dot' not found; open docs/ufrf_proof_graph.dot in any DOT viewer."
fi
