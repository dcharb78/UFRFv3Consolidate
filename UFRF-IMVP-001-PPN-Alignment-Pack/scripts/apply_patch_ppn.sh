#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="${1:-$PWD}"

echo "[PPN patch] Copying doc notes into repo..."
mkdir -p "$REPO_ROOT/docs" "$REPO_ROOT/discoveries" "$REPO_ROOT/validations/ppn_parameters"

# Drop-in docs (non-destructive)
cp -n "docs/PPN-DeltaP2-PhiRatio.md" "$REPO_ROOT/docs/"
cp -n "docs/Discoveries-PPN-Mapping-Note.md" "$REPO_ROOT/discoveries/ppn_from_orbital_period.md"
cp -n "docs/AXIOMS-Projection-Footnote.md" "$REPO_ROOT/AXIOMS_ProjectionFootnote.md"

echo "[PPN patch] (Optional) add normalization toggle in code:"
echo " - Open validations/ppn_parameters/ppn_complete_derivation.py"
echo " - Add parameter: B0sq_over_U = None  # or 13/(4*math.pi**3)"
echo " - Ensure γ−1 = b*κ*Δp**2 and β−1 = −(a*κ/2)*Δp**2 independent of U"
echo " - Keep a/b = 1/φ**2"

echo "[PPN patch] Done. Review files and integrate snippets as needed."
