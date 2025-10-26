
import sympy as sp

def em_hamiltonian_density():
    # Treat E and B as independent 3-vectors; use symbolic components
    Z, TH = sp.symbols('Z TH', positive=True, real=True)
    E1,E2,E3,B1,B2,B3 = sp.symbols('E1 E2 E3 B1 B2 B3', real=True)
    E2sq = E1**2+E2**2+E3**2
    B2sq = B1**2+B2**2+B3**2
    EdotB = E1*B1 + E2*B2 + E3*B3
    # Lagrangian density in (E,B) form (flat metric): L = 1/2 Z (E^2 - B^2) + Θ E·B
    L = sp.Rational(1,2)*Z*(E2sq - B2sq) + TH*EdotB
    # Canonical momentum Π = ∂L/∂E = Z E + Θ B
    PiE1 = sp.diff(L, E1); PiE2 = sp.diff(L, E2); PiE3 = sp.diff(L, E3)
    # Hamiltonian density H = Π·E - L
    H = (PiE1*E1 + PiE2*E2 + PiE3*E3) - L
    H_simplified = sp.simplify(H)
    target = sp.simplify(sp.Rational(1,2)*Z*(E2sq + B2sq))
    # Return also the symbol handles so callers can substitute numerically
    symbols = dict(Z=Z, TH=TH, E1=E1, E2=E2, E3=E3, B1=B1, B2=B2, B3=B3)
    return sp.simplify(H_simplified - target), sp.simplify(PiE1), sp.simplify(PiE2), sp.simplify(PiE3), symbols

if __name__ == "__main__":
    resid, Pi1, Pi2, Pi3 = em_hamiltonian_density()
    print({"hamiltonian_residual": str(resid), "Pi_components": [str(Pi1), str(Pi2), str(Pi3)]})
