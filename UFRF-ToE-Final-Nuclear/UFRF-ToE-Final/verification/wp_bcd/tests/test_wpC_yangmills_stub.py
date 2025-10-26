
import sys, os, importlib, sympy as sp
THIS = os.path.dirname(__file__); ROOT = os.path.abspath(os.path.join(THIS, os.pardir))
sys.path.insert(0, ROOT)

ym = importlib.import_module("src.symbolics.yangmills_stub")
resid, Pi, sy = ym.ym_hamiltonian_positivity()
assert sp.simplify(resid) == 0

subs = {sy["Z"]: 2.3, sy["TH"]: -0.9,
        sy["Ex"]: 0.4, sy["Ey"]:-0.2, sy["Ez"]:0.1,
        sy["Bx"]: 0.3, sy["By"]:-0.5, sy["Bz"]:0.7}

Pi_num = [float(sp.N(p.subs(subs))) for p in Pi]
expected = [2.3*subs[sy["Ex"]] + (-0.9)*subs[sy["Bx"]],
            2.3*subs[sy["Ey"]] + (-0.9)*subs[sy["By"]],
            2.3*subs[sy["Ez"]] + (-0.9)*subs[sy["Bz"]]]
for a,b in zip(Pi_num, expected):
    assert abs(a-b) < 1e-9, "YM canonical momentum mismatch"

branches = [str(s) for s in ym.ym_hyperbolicity_symbol()]
mag = sp.sqrt(sp.symbols('kx', real=True)**2 + sp.symbols('ky', real=True)**2 + sp.symbols('kz', real=True)**2)
assert set(branches) == {str(mag), str(-mag)}
print("WP‑C: Yang–Mills positivity and hyperbolicity around A=0 verified.")
