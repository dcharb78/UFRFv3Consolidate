
# src/symbolics/variable_couplings_eom.py
# Symbolic derivation: Euler–Lagrange w.r.t. A_ν for L = -1/4 Z(Φ) F^2 - 1/4 Θ(Φ) F F~ - J·A  (+ scalar terms independent of A).
# Goal: Prove ∂_μ [ Z(Φ) F^{μν} + Θ(Φ) \tilde F^{μν} ] = J^{ν}.

import sympy as sp

def derive_em_eom_variable_couplings():
    # Coordinates and metric
    x0, x1, x2, x3 = sp.symbols('x0 x1 x2 x3', real=True)
    coords = (x0, x1, x2, x3)
    eta = sp.diag(-1, 1, 1, 1)

    # Fields
    A = [sp.Function(f"A{mu}")(*coords) for mu in range(4)]
    Phi = sp.Function("Phi")(*coords)
    J = [sp.Function(f"J{mu}")(*coords) for mu in range(4)]
    Z = sp.Function("Z")(Phi)      # Z(Φ(x))
    TH = sp.Function("TH")(Phi)    # Θ(Φ(x))

    # Raise/lower helpers
    def raise_vec(Vdn):
        return [sum(eta[mu,nu]*Vdn[nu] for nu in range(4)) for mu in range(4)]

    # F_{μν} and raised versions
    F = sp.MutableDenseNDimArray([[sp.diff(A[nu], coords[mu]) - sp.diff(A[mu], coords[nu]) for nu in range(4)] for mu in range(4)])
    Fup = sp.MutableDenseNDimArray([[sum(eta[mu,a]*eta[nu,b]*F[a,b] for a in range(4) for b in range(4)) for nu in range(4)] for mu in range(4)])

    # dual F^{μν} = (1/2) ε^{μνρσ} F_{ρσ}
    eps = sp.LeviCivita
    Fdual_up = sp.MutableDenseNDimArray([[
        sp.Rational(1,2)*sum(eps(mu,nu,r,s)*F[r,s] for r in range(4) for s in range(4))
        for nu in range(4)] for mu in range(4)])

    # Currents with raised index: J^μ = η^{μν} J_ν
    Jup = raise_vec(J)

    # Lagrangian density: -1/4 Z F^2 - 1/4 TH F F~ - J_μ A^μ (only terms depending on A)
    Aup = raise_vec(A)
    F2 = sum(F[mu,nu]*Fup[mu,nu] for mu in range(4) for nu in range(4))
    FstarF = sum(F[mu,nu]*Fdual_up[mu,nu] for mu in range(4) for nu in range(4))
    L = -sp.Rational(1,4)*Z*F2 - sp.Rational(1,4)*TH*FstarF - sum(J[mu]*Aup[mu] for mu in range(4))

    # E-L equations for A_ν
    dL_d_dA = sp.MutableDenseNDimArray([[sp.diff(L, sp.diff(A[nu], coords[mu])) for nu in range(4)] for mu in range(4)])
    divergence = [sum(sp.diff(dL_d_dA[mu,nu], coords[mu]) for mu in range(4)) for nu in range(4)]
    dL_dA = [sp.diff(L, A[nu]) for nu in range(4)]
    EOM = [sp.simplify(divergence[nu] - dL_dA[nu]) for nu in range(4)]

    # Target identity: EOM_ν - ( ∂_μ ( Z F^{μν} + TH F~^{μν} ) - J^ν ) == 0
    target = [sp.simplify(EOM[nu] + (sum(sp.diff(Z*Fup[mu,nu] + TH*Fdual_up[mu,nu], coords[mu]) for mu in range(4)) - Jup[nu]))
              for nu in range(4)]
    target_ok = all(t == 0 for t in target)

    # Expand divergence to expose product rule terms (∂μ Z)F^{μν} etc., for reporting
    expanded_div = [sp.simplify(sum(sp.diff(Z*Fup[mu,nu] + TH*Fdual_up[mu,nu], coords[mu]) for mu in range(4))) for nu in range(4)]

    # Bianchi identity (representative component) still holds: ∂_[α F_{βγ]} = 0
    alpha, beta, gamma = 0, 1, 2
    bianchi = sp.simplify(sp.diff(F[beta,gamma], coords[alpha]) + sp.diff(F[gamma,alpha], coords[beta]) + sp.diff(F[alpha,beta], coords[gamma]))

    return {
        "target_all_zero": target_ok,
        "target_components": [sp.srepr(t) for t in target],
        "bianchi_identity": str(bianchi),
        "expanded_divergence": [str(ed) for ed in expanded_div]
    }

if __name__ == "__main__":
    out = derive_em_eom_variable_couplings()
    import json
    print(json.dumps(out, indent=2))
