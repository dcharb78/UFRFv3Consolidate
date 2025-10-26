
import sys, os, importlib, sympy as sp
THIS = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(THIS, os.pardir))
sys.path.insert(0, ROOT)

mod = importlib.import_module("src.symbolics.maxwell_vector_recovery")
det_tt = sp.simplify(mod.vector_maxwell_recovery())
k = sp.symbols('k', real=True)
w = sp.symbols('w', real=True)
expected = sp.simplify(((k - w)**2*(k + w)**2)/(w**2))
assert sp.simplify(det_tt - expected) == 0, "Maxwell dispersion mismatch"
print("WP‑C: Maxwell dispersion w^2 = k^2 verified in vector form.")
