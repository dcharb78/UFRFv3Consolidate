
from sympy import symbols, Matrix, I, simplify, eye

def derive_maxwell_el():
    return r"\partial_\mu F^{\mu\nu} = J^\nu"

def gamma_matrices():
    sigma1 = Matrix([[0,1],[1,0]])
    sigma2 = Matrix([[0,-I],[I,0]])
    sigma3 = Matrix([[1,0],[0,-1]])
    def gi(sig):
        return Matrix([[0,0, sig[0,0], sig[0,1]],
                       [0,0, sig[1,0], sig[1,1]],
                       [-sig[0,0], -sig[0,1], 0,0],
                       [-sig[1,0], -sig[1,1], 0,0]])
    gamma0 = Matrix([[1,0,0,0],
                     [0,1,0,0],
                     [0,0,-1,0],
                     [0,0,0,-1]])
    gamma1 = gi(sigma1)
    gamma2 = gi(sigma2)
    gamma3 = gi(sigma3)
    return gamma0, gamma1, gamma2, gamma3

def dirac_square_identity():
    p0, px, py, pz, m = symbols('p0 px py pz m', complex=True)
    g0, g1, g2, g3 = gamma_matrices()
    gdotp = g0*p0 - g1*px - g2*py - g3*pz
    left = (gdotp - m*eye(4))*(gdotp + m*eye(4))
    p2 = p0**2 - px**2 - py**2 - pz**2
    target = (p2 - m**2)*eye(4)
    return simplify(left - target)
