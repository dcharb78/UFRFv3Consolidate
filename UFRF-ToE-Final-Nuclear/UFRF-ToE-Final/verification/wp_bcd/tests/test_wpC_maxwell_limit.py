
import sys, os, importlib, sympy as sp
THIS = os.path.dirname(__file__); ROOT = os.path.abspath(os.path.join(THIS, os.pardir))
sys.path.insert(0, ROOT)
mx = importlib.import_module("src.symbolics.maxwell_limit")
k2, branches = mx.maxwell_dispersion()
w, kx, ky, kz = sp.symbols('w kx ky kz', real=True)
assert sp.simplify(k2 + w**2 - kx**2 - ky**2 - kz**2) == 0
print("WP‑C: Maxwell dispersion ω^2=|k|^2 recovered.")
