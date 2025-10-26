#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="${1:-$PWD}"
mkdir -p "$REPO_ROOT/src/fourier"
cp -n "src/fourier/ufrf_fourier_proof.py" "$REPO_ROOT/ufrf_fourier_proof.py"
cp -n "src/fourier/ufrf_fourier_proof.py" "$REPO_ROOT/src/fourier/ufrf_fourier_proof.py"
echo "[fourier] Placed ufrf_fourier_proof.py at repo root and src/fourier/"
echo "Run: python ufrf_fourier_proof.py"
