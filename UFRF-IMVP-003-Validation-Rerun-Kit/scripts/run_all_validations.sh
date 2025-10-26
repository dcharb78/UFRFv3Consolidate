#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="${1:-$PWD}"

echo "[run] Nuclear magic numbers..."
python3 "$REPO_ROOT/validations/nuclear_magic_numbers/validation.py" | tee artifacts/nuclear_validation.log

echo "[run] QED beta function..."
python3 "$REPO_ROOT/validations/beta_function/beta_from_ufrf_concurrent.py" | tee artifacts/beta_function.log

echo "[run] PPN parameters..."
python3 "$REPO_ROOT/validations/ppn_parameters/ppn_complete_derivation.py" | tee artifacts/ppn_parameters.log

echo "[run] Complete. Artifacts and logs are under ./artifacts"
