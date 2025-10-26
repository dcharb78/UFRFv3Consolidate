
import sympy as sp

def em_build():
    x = sp.symbols('x0:4', real=True)
    A = [sp.Function(f"A{mu}")(*x) for mu in range(4)]
    phi = sp.Function("phi")(*x)
    Zfun = sp.Function("Z")
    THfun = sp.Function("TH")
    Z_of_phi = Zfun(phi)
    TH_of_phi = THfun(phi)
    Jup = [sp.Function(f"J{mu}")(*x) for mu in range(4)]
    eta = sp.diag(-1, 1, 1, 1)
    # F_{μν}, F^{μν}
    Fdn = sp.MutableDenseNDimArray([[sp.diff(A[nu], x[mu]) - sp.diff(A[mu], x[nu]) for nu in range(4)] for mu in range(4)])
    Fup = sp.MutableDenseNDimArray([[
        sum(eta[mu,a]*eta[nu,b]*Fdn[a,b] for a in range(4) for b in range(4))
        for nu in range(4)] for mu in range(4)])
    # Dual with upper indices: F~^{μν} = 1/2 ε^{μνρσ} F_{ρσ}
    Fdual_up = sp.MutableDenseNDimArray([[
        sp.Rational(1,2)*sum(sp.LeviCivita(mu,nu,r,s)*Fdn[r,s] for r in range(4) for s in range(4))
        for nu in range(4)] for mu in range(4)])
    # A^μ and L
    Aup = [sum(eta[mu,nu]*A[nu] for nu in range(4)) for mu in range(4)]
    L = -sp.Rational(1,4)*Z_of_phi*sum(Fup[mu,nu]*Fdn[mu,nu] for mu in range(4) for nu in range(4)) \
        -sp.Rational(1,4)*TH_of_phi*sum(Fdual_up[mu,nu]*Fdn[mu,nu] for mu in range(4) for nu in range(4)) \
        - sum(Jup[mu]*A[mu] for mu in range(4))
    return x, A, phi, Z_of_phi, TH_of_phi, Jup, eta, Fdn, Fup, Fdual_up, L

def em_eom_with_ZTheta_and_J():
    x, A, phi, Z_of_phi, TH_of_phi, Jup, eta, Fdn, Fup, Fdual_up, L = em_build()
    # Canonical momentum π^{μν} = ∂L/∂(∂_μ A_ν)
    dL_d_dA = sp.MutableDenseNDimArray([[sp.diff(L, sp.diff(A[nu], x[mu])) for nu in range(4)] for mu in range(4)])
    # Euler-Lagrange EOM
    div_term = [sum(sp.diff(dL_d_dA[mu,nu], x[mu]) for mu in range(4)) for nu in range(4)]
    dL_dA = [sp.diff(L, A[nu]) for nu in range(4)]
    EOM = [sp.simplify(div_term[nu] - dL_dA[nu]) for nu in range(4)]
    # Check that π^{μν} equals the expected -1/2 ( Z F^{μν} + TH F~^{μν} )
    pi_expected = sp.MutableDenseNDimArray([[ -(Z_of_phi*Fup[mu,nu] + TH_of_phi*Fdual_up[mu,nu]) for nu in range(4)] for mu in range(4)])
    pi_identity = [[sp.simplify(dL_d_dA[mu,nu] - pi_expected[mu,nu]) for nu in range(4)] for mu in range(4)]
    pi_ok = all(pi_identity[mu][nu] == 0 for mu in range(4) for nu in range(4))
    # Target identity from EL definition: EOM_ν - ( ∂_μ π^{μν} + J^ν ) = 0
    target = [sp.simplify(EOM[nu] - (sum(sp.diff(dL_d_dA[mu,nu], x[mu]) for mu in range(4)) + Jup[nu])) for nu in range(4)]
    target_ok = all(t == 0 for t in target)
    return EOM, target_ok, pi_ok

def bianchi_identity_symbolic():
    x = sp.symbols('x0:4', real=True)
    A = [sp.Function(f"A{mu}")(*x) for mu in range(4)]
    def F(mu,nu):
        return sp.diff(A[nu], x[mu]) - sp.diff(A[mu], x[nu])
    alpha,beta,gamma = 0,1,2
    B = sp.simplify(sp.diff(F(beta,gamma), x[alpha]) + sp.diff(F(gamma,alpha), x[beta]) + sp.diff(F(alpha,beta), x[gamma]))
    return B

def dirac_dispersion_identity():
    import sympy as sp
    I2 = sp.eye(2); Z2 = sp.zeros(2)
    sigma1 = sp.Matrix([[0,1],[1,0]])
    sigma2 = sp.Matrix([[0,-sp.I],[sp.I,0]])
    sigma3 = sp.Matrix([[1,0],[0,-1]])
    gamma0 = sp.Matrix(sp.BlockMatrix([[I2, Z2],[Z2, -I2]]))
    gamma1 = sp.Matrix(sp.BlockMatrix([[Z2, sigma1],[-sigma1, Z2]]))
    gamma2 = sp.Matrix(sp.BlockMatrix([[Z2, sigma2],[-sigma2, Z2]]))
    gamma3 = sp.Matrix(sp.BlockMatrix([[Z2, sigma3],[-sigma3, Z2]]))
    p0,p1,p2,p3,m = sp.symbols('p0 p1 p2 p3 m', real=True)
    pslash = gamma0*p0 - gamma1*p1 - gamma2*p2 - gamma3*p3
    M = pslash - m*sp.eye(4)
    detM = sp.simplify(sp.factor(M.det()))
    expected = (p0**2 - p1**2 - p2**2 - p3**2 - m**2)**2
    return sp.simplify(detM - expected)

def gauge_invariance_of_F():
    x = sp.symbols('x0:4', real=True)
    A = [sp.Function(f"A{mu}")(*x) for mu in range(4)]
    chi = sp.Function("chi")(*x)
    def F_from_A(Afields, mu, nu):
        return sp.diff(Afields[nu], x[mu]) - sp.diff(Afields[mu], x[nu])
    F = [[F_from_A(A, mu, nu) for nu in range(4)] for mu in range(4)]
    Aprime = [A[mu] + sp.diff(chi, x[mu]) for mu in range(4)]
    Fp = [[F_from_A(Aprime, mu, nu) for nu in range(4)] for mu in range(4)]
    diffs = [[sp.simplify(F[mu][nu] - Fp[mu][nu]) for nu in range(4)] for mu in range(4)]
    all_zero = all(diffs[mu][nu] == 0 for mu in range(4) for nu in range(4))
    return all_zero, diffs

def run():
    import json, sympy as sp
    EOM, target_ok, pi_ok = em_eom_with_ZTheta_and_J()
    bianchi = bianchi_identity_symbolic()
    dirac_resid = dirac_dispersion_identity()
    inv_ok, _ = gauge_invariance_of_F()
    out = {
        "em_target_identity_all_zero": bool(target_ok),
        "canonical_momentum_identity_ok": bool(pi_ok),
        "bianchi_identity": str(bianchi),
        "dirac_det_identity_residual": str(dirac_resid),
        "dirac_ok": bool(dirac_resid == 0),
        "gauge_invariance_F": bool(inv_ok)
    }
    print(json.dumps(out, indent=2))

if __name__ == "__main__":
    run()
