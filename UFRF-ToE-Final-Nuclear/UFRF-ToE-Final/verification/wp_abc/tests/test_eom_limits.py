
import sys, os
from pathlib import Path
ROOT = Path("/mnt/data/UFRF-ToE")
sys.path.insert(0, str(ROOT))

import json, importlib, sympy as sp
m = importlib.import_module("src.symbolics.derive_eom_full")

EOM, target_ok, pi_ok = m.em_eom_with_ZTheta_and_J()
bianchi = m.bianchi_identity_symbolic()
dirac_resid = m.dirac_dispersion_identity()
gauge_ok, diffs = m.gauge_invariance_of_F()

assert target_ok, "EL target identity (∂_μ π^{μν} + J^ν) failed"
assert pi_ok, "Canonical momentum identity π^{μν} = -1/2(Z F^{μν} + Θ F~^{μν}) failed"
assert sp.simplify(bianchi) == 0, "Bianchi identity failed"
assert dirac_resid == 0, "Dirac determinant identity failed"
assert gauge_ok, "Gauge invariance of F failed"

print("ALL TESTS PASSED")
