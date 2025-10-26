import sys, os, importlib, sympy as sp
# Add project root to module path for 'src' package imports
THIS = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(THIS, os.pardir))
sys.path.insert(0, ROOT)

dirac = importlib.import_module("src.symbolics.dirac_gauge_covariance")
emham = importlib.import_module("src.symbolics.em_hamiltonian_positivity")
emhyp = importlib.import_module("src.symbolics.em_hyperbolicity")

# 4.1 Dirac local U(1) covariance of Dμ
ok, _ = dirac.dirac_local_U1_covariance()
assert ok, "Dirac Dμ covariance under local U(1) failed"

# 4.2 EM Hamiltonian positivity (Θ cancels in H; H = 1/2 Z (E^2 + B^2) with Z>0)
resid, Pi1, Pi2, Pi3, symb = emham.em_hamiltonian_density()
assert sp.simplify(resid) == 0, "Hamiltonian residual not zero"

# Randomized spot checks for Π = Z E + Θ B
import random
for _ in range(3):
    Zv = random.uniform(0.1, 5.0)
    THv = random.uniform(-3.0, 3.0)
    Ev = [random.uniform(-2,2) for __ in range(3)]
    Bv = [random.uniform(-2,2) for __ in range(3)]
    subs = {symb['Z']:Zv, symb['TH']:THv, symb['E1']:Ev[0], symb['E2']:Ev[1], symb['E3']:Ev[2], symb['B1']:Bv[0], symb['B2']:Bv[1], symb['B3']:Bv[2]}
    Pi_num = [float(sp.N(Pi1.subs(subs))), float(sp.N(Pi2.subs(subs))), float(sp.N(Pi3.subs(subs)))]
    expected = [Zv*Ev[0] + THv*Bv[0], Zv*Ev[1] + THv*Bv[1], Zv*Ev[2] + THv*Bv[2]]
    for a,b in zip(Pi_num, expected):
        assert abs(a-b) < 1e-9, "Canonical momentum mismatch"

# 4.3 Hyperbolicity: ω = ±|k| solutions
sol = emhyp.dispersion_relation()
kx,ky,kz = sp.symbols('kx ky kz', real=True)
mag = sp.sqrt(kx**2 + ky**2 + kz**2)
expected = { str(mag), str(-mag) }
assert set([str(s) for s in sol]) == expected, "Dispersion not lightlike"

print("ALL TESTS PASSED (WP‑B): Dirac local U(1), EM Hamiltonian positivity, and hyperbolicity.")
