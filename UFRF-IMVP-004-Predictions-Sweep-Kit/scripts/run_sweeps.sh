#!/usr/bin/env bash
set -euo pipefail
echo "[sweeps] Example commands (edit paths as needed):"
echo "python3 scripts/nuclear_14MeV_scan.py data/nuclear_levels.csv artifacts/14MeV_report.json"
echo "python3 scripts/network_137_transition.py 200 200 5 artifacts/net137.json"
echo "python3 scripts/materials_28K_scan.py data/material_curve.csv artifacts/28K_report.json"
