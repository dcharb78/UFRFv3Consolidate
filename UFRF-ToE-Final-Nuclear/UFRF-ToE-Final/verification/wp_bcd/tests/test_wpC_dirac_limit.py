
import sys, os, importlib, sympy as sp
THIS = os.path.dirname(__file__); ROOT = os.path.abspath(os.path.join(THIS, os.pardir))
sys.path.insert(0, ROOT)
dd = importlib.import_module("src.symbolics.dirac_dispersion")
w,kx,ky,kz,m = sp.symbols('w kx ky kz m', real=True)
det = sp.simplify(dd.dirac_determinant(w,kx,ky,kz,m))
# Expect det(D) = (w**2 - k^2 - m^2)^2 for our signature
k2 = w**2 - kx**2 - ky**2 - kz**2 - m**2
assert sp.factor(det - k2**2) == 0
print("WP‑C: Dirac dispersion det(γ·k - m) = (ω^2 - |k|^2 - m^2)^2 verified.")
