
import sympy as sp

def maxwell_from_ufrf_limit():
    # Variables
    x = sp.symbols('x0:4', real=True)
    A = [sp.Function(f"A{mu}")(*x) for mu in range(4)]
    J = [sp.Function(f"J{mu}")(*x) for mu in range(4)]
    Z = sp.Symbol('Z', real=True, positive=True)  # treat constant in this check

    # F_{μν} and F^{μν} with Minkowski metric diag(-,+,+,+)
    eta = sp.diag(-1,1,1,1)
    Fdn = sp.MutableDenseNDimArray.zeros(4,4)
    for mu in range(4):
        for nu in range(4):
            Fdn[mu,nu] = sp.diff(A[nu], x[mu]) - sp.diff(A[mu], x[nu])
    Fup = sp.MutableDenseNDimArray.zeros(4,4)
    for mu in range(4):
        for nu in range(4):
            Fup[mu,nu] = sum(eta[mu,alpha]*eta[nu,beta]*Fdn[alpha,beta] for alpha in range(4) for beta in range(4))

    # L_EM = -1/4 Z F_{μν} F^{μν} - J_μ A^μ
    L = -sp.Rational(1,4)*Z*sum(Fdn[mu,nu]*Fup[mu,nu] for mu in range(4) for nu in range(4)) \
        - sum(eta[mu,nu]*J[mu]*A[nu] for mu in range(4) for nu in range(4))

    # Euler-Lagrange for A_ν
    E = []
    for nu in range(4):
        dL_dA = sp.diff(L, A[nu])
        dL_dA_mu = [sp.diff(L, sp.diff(A[nu], x[mu])) for mu in range(4)]
        div = sum(sp.diff(dL_dA_mu[mu], x[mu]) for mu in range(4))
        E.append(sp.simplify(dL_dA - div))  # Eν = 0 are the EOM

    # Expect Maxwell form up to overall sign convention: Eν + Z ∂_μ F^{μν} + J^ν = 0
    residuals = []
    for nu in range(4):
        dF = sum(sp.diff(Fup[mu,nu], x[mu]) for mu in range(4))
        Jup = sum(eta[nu,alpha]*J[alpha] for alpha in range(4))
        residuals.append(sp.simplify(E[nu] + Z*dF + Jup))
    ok = all(r == 0 for r in residuals)
    return ok, [sp.sstr(r) for r in residuals]

def free_dirac_limit():
    # Variation wrt ψ̄ for L = ψ̄(i γ^μ ∂_μ - m) ψ  (A=0, constant mass)
    # We'll treat γ^μ as commuting placeholders Γ^μ; test only algebraic structure.
    x = sp.symbols('x0:4', real=True)
    m = sp.symbols('m', real=True, positive=True)
    psi = sp.Function('psi')(*x)
    psibar = sp.Function('psibar')(*x)
    # Represent (γ ⋅ ∂) ψ as a formal symbol Dpsi; we check Euler-Lagrange yields i(γ⋅∂)ψ - m ψ.
    # Do it explicitly with components Γ^μ ∂_μ ψ and leave Γ^μ as symbols that commute with scalars.
    Gamma = [sp.Symbol(f"Gamma{mu}") for mu in range(4)]
    # Build L density (suppress spinor contraction): L = psibar * ( i Σ Γ^μ ∂_μ ψ  - m ψ )
    Dpsi = sum(Gamma[mu]*sp.diff(psi, x[mu]) for mu in range(4))
    I = sp.I
    L = psibar*(I*Dpsi - m*psi)
    # Euler-Lagrange wrt psibar is simply the bracket:
    EL_psibar = sp.diff(L, psibar)
    # Expect i (Γ·∂) ψ - m ψ
    expected = I*Dpsi - m*psi
    return sp.simplify(EL_psibar - expected) == 0, sp.sstr(sp.simplify(EL_psibar - expected))

if __name__ == "__main__":
    okM, residM = maxwell_from_ufrf_limit()
    okD, residD = free_dirac_limit()
    print({"maxwell_limit_ok": okM, "maxwell_residuals": residM, "dirac_limit_ok": okD, "dirac_residual": residD})
