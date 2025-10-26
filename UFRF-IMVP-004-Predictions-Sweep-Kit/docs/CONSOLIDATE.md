
# CONSOLIDATE: Predictions Sweep Kit (IMVP‑004)

**Purpose**
Database-/sim-first checks for three high-signal predictions already present in the package:
1) Nuclear shell gap near **14.0 ± 0.25 MeV**
2) Network transition near **137** connections
3) A **28 K** anomaly in 2D materials

**How to run**
```bash
python3 scripts/nuclear_14MeV_scan.py data/nuclear_levels.csv artifacts/14MeV_report.json
python3 scripts/network_137_transition.py 200 200 5 artifacts/net137.json
python3 scripts/materials_28K_scan.py data/material_curve.csv artifacts/28K_report.json
```
