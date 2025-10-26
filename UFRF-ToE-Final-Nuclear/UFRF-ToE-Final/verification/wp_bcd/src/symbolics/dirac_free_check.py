
# src/symbolics/dirac_free_check.py
# Algebraic check: det(γ·p - m) = (p^2 - m^2)^2 for metric η = diag(1,-1,-1,-1).

import sympy as sp

def dirac_det_identity():
    # Symbols
    E, px, py, pz, m = sp.symbols('E px py pz m', real=True)
    # Pauli matrices
    I2 = sp.eye(2)
    sigma_x = sp.Matrix([[0,1],[1,0]])
    sigma_y = sp.Matrix([[0,-sp.I],[sp.I,0]])
    sigma_z = sp.Matrix([[1,0],[0,-1]])

    # Dirac gamma matrices in standard (Dirac) representation with η = diag(1,-1,-1,-1)
    zero = sp.zeros(2)
    gamma0 = sp.diag(I2, -I2)  # block diag(I2, -I2)
    gammai = []
    for s in (sigma_x, sigma_y, sigma_z):
        upper = sp.Matrix.hstack(zero, s)
        lower = sp.Matrix.hstack(-s, zero)
        gammai.append(sp.Matrix.vstack(upper, lower))
    gamma1, gamma2, gamma3 = gammai

    # gamma · p - m = γ^0 E - γ^i p_i - m
    M = E*gamma0 - px*gamma1 - py*gamma2 - pz*gamma3 - m*sp.eye(4)

    detM = sp.factor(M.det())
    p2 = E**2 - (px**2 + py**2 + pz**2)  # with η=(1,-1,-1,-1)
    target = sp.factor((p2 - m**2)**2)

    return sp.simplify(detM - target)

if __name__ == "__main__":
    print(sp.srepr(dirac_det_identity()))
