
import sympy as sp

x0, x1, x2, x3 = sp.symbols('x0 x1 x2 x3', real=True)
coords = (x0, x1, x2, x3)

eta = sp.diag(1, -1, -1, -1)

def d(mu, f):
    return sp.diff(f, coords[mu])

def raise2(T):
    res = sp.MutableDenseNDimArray.zeros(4,4)
    for mu in range(4):
        for nu in range(4):
            s = 0
            for a in range(4):
                for b in range(4):
                    s += eta[mu,a]*eta[nu,b]*T[a,b]
            res[mu,nu] = sp.simplify(s)
    return res

def contract2(A, B):
    s = 0
    for mu in range(4):
        for nu in range(4):
            s += A[mu,nu]*B[mu,nu]
    return sp.simplify(s)

def divergence2(T):
    out = []
    for nu in range(4):
        s = 0
        for mu in range(4):
            s += d(mu, T[mu,nu])
        out.append(sp.simplify(s))
    return out

def levi(mu, nu, rho, sig):
    return sp.LeviCivita(mu, nu, rho, sig)

def hodge_dual(F_cov):
    res = sp.MutableDenseNDimArray.zeros(4,4)
    for mu in range(4):
        for nu in range(4):
            s = 0
            for rho in range(4):
                for sig in range(4):
                    s += sp.Rational(1,2) * levi(mu,nu,rho,sig) * F_cov[rho,sig]
            res[mu,nu] = sp.simplify(s)
    return res
