
import importlib, sympy as sp, sys
sys.path.insert(0, "/mnt/data/UFRF-ToE")

emE = importlib.import_module("src.symbolics.em_energy_hyperbolicity")
emd = importlib.import_module("src.symbolics.em_dispersion")

# 1) Energy positivity via Hamiltonian identity H = (Z/2)(E^2+B^2)
H, Htarget, residual = emE.hamiltonian_density_temporal_gauge()
assert sp.simplify(residual) == 0, "Hamiltonian does not match Z/2 (E^2+B^2)"

# 2) Lorenz gauge and dispersion relation (wave equation)
gauge, dispersion = emd.plane_wave_dispersion()
assert str(dispersion) in ("kx**2 + ky**2 + kz**2 - omega**2","-omega**2 + kx**2 + ky**2 + kz**2"), "Unexpected dispersion form"

print("ALL TESTS PASSED: Positive energy (no ghosts) and lightlike dispersion (hyperbolic).")
