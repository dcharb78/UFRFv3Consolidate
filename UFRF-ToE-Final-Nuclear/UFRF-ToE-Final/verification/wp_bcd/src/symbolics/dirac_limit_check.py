
import sympy as sp
from sympy.physics.matrices import mgamma

E, px, py, pz, m = sp.symbols('E px py pz m', real=True)

p_slash = mgamma(0)*E - mgamma(1)*px - mgamma(2)*py - mgamma(3)*pz
M = p_slash - m*sp.eye(4)
detM = sp.simplify(M.det())
detM_factored = sp.factor(detM)
expected = (E**2 - px**2 - py**2 - pz**2 - m**2)**2

def assert_dispersion():
    return sp.simplify(detM_factored - expected) == 0

if __name__ == "__main__":
    print("det:", detM_factored)
    print("OK:", assert_dispersion())
