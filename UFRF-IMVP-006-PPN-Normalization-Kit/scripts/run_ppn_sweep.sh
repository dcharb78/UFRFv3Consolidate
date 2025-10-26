#!/usr/bin/env bash
set -euo pipefail
echo "[ppn] Examples:"
python3 scripts/ppn_delta_p2_driver.py --delta_p 1e-4 --kappa 1.0 --B0_sq_over_U none
python3 scripts/ppn_delta_p2_driver.py --delta_p 3e-4 --kappa 0.1 --B0_sq_over_U 1.0
