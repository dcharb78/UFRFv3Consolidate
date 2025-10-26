
import sys, os, importlib, sympy as sp, random
THIS = os.path.dirname(__file__); ROOT = os.path.abspath(os.path.join(THIS, os.pardir))
sys.path.insert(0, ROOT)

# Variable-coupling hyperbolicity
vh = importlib.import_module("src.symbolics.variable_coupling_hyperbolicity")
out = vh.principal_symbol_variable_couplings()
mag = sp.sqrt(sp.symbols('kx', real=True)**2 + sp.symbols('ky', real=True)**2 + sp.symbols('kz', real=True)**2)
assert set([str(s) for s in out["omega_branches"]]) == {str(mag), str(-mag)}
print("WP‑B+: variable‑coupling principal symbol OK.")
