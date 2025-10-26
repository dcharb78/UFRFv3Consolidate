#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="${1:-$PWD}"

echo "[hygiene] Adding missing __init__.py markers (non-destructive)..."
mkdir -p "$REPO_ROOT/src/analysis/higher_traces" "$REPO_ROOT/src/analysis/quasi_arithmetic"
for p in \
  src/__init__.py \
  src/core/__init__.py \
  src/topology/__init__.py \
  src/analysis/__init__.py \
  src/analysis/higher_traces/__init__.py \
  src/analysis/quasi_arithmetic/__init__.py ; do
  cp -n "$p" "$REPO_ROOT/$p"
done

echo "[hygiene] Adding derivation.md placeholders where missing..."
mkdir -p "$REPO_ROOT/validations/nuclear_magic_numbers" \
         "$REPO_ROOT/validations/beta_function" \
         "$REPO_ROOT/validations/ppn_parameters"
for p in \
  validations/nuclear_magic_numbers/derivation.md \
  validations/beta_function/derivation.md \
  validations/ppn_parameters/derivation.md ; do
  cp -n "$p" "$REPO_ROOT/$p"
done

echo "[hygiene] Done. Review diffs and integrate content as needed."
