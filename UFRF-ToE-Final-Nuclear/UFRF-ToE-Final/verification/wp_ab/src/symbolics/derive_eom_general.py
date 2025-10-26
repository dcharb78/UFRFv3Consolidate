
"""
derive_eom_general.py
---------------------
Symbolically verify (1) Maxwell-with-sources from the UFRF EM Lagrangian with *variable* Z(Φ), Θ(Φ),
and (2) Dirac minimal coupling equation from the spinor sector, including the source current
j^ν = q ψ̄ γ^ν ψ in the gauge-field EOM.

Conventions:
- Metric η = diag(-1, +1, +1, +1)
- ε^{0123} = +1
- L_EM = -1/4 Z(Φ) F_{μν} F^{μν} - 1/4 Θ(Φ) F_{μν} \tilde F^{μν}
- L_ψ = i ψ̄ γ^μ ∂_μ ψ - m ψ̄ ψ - q ψ̄ γ^μ ψ A_μ
- A^μ = η^{μν} A_ν; indices raised with η
- ψ̄ is represented as independent fields φ_j; ψ components as ψ_k; variation w.r.t φ yields Dirac eq for ψ.

We check identities:
(EM)   ∂_μ [ Z F^{μν} + Θ \tilde F^{μν} ] - q ψ̄ γ^ν ψ = 0
(Dirac) i γ^μ ∂_μ ψ - m ψ - q γ^μ A_μ ψ = 0    (from δL/δψ̄ = 0)

All symbols are symbolic; Z(Φ) and Θ(Φ) are treated as generic functions of Φ(x).
"""

import sympy as sp
import json

# ---------- Coordinates & metric ----------
x0, x1, x2, x3 = sp.symbols('x0 x1 x2 x3', real=True)
coords = (x0, x1, x2, x3)
eta = sp.diag(-1, 1, 1, 1)
eta_inv = eta

# ---------- Fields ----------
A = [sp.Function(f"A{mu}")(*coords) for mu in range(4)]                 # gauge field A_μ
phi = sp.Function("Phi")(*coords)                                       # scalar Φ(x)
psi = [sp.Function(f"psi{k}")(*coords) for k in range(4)]               # ψ components
phibar = [sp.Function(f"phibar{j}")(*coords) for j in range(4)]         # ψ̄ components (independent)

# Couplings / parameters
m, q = sp.symbols('m q', real=True)
Zfun = sp.Function("Z")     # Z(Φ)
THfun = sp.Function("TH")   # Θ(Φ)
Z = Zfun(phi)
TH = THfun(phi)

# ---------- Gamma matrices (Dirac rep, metric + - - - for gamma algebra here) ----------
I2 = sp.eye(2); Z2 = sp.zeros(2)
sigma1 = sp.Matrix([[0,1],[1,0]])
sigma2 = sp.Matrix([[0,-sp.I],[sp.I,0]])
sigma3 = sp.Matrix([[1,0],[0,-1]])
gamma0 = sp.Matrix(sp.BlockMatrix([[I2, Z2],[Z2, -I2]]))
gamma1 = sp.Matrix(sp.BlockMatrix([[Z2, sigma1],[-sigma1, Z2]]))
gamma2 = sp.Matrix(sp.BlockMatrix([[Z2, sigma2],[-sigma2, Z2]]))
gamma3 = sp.Matrix(sp.BlockMatrix([[Z2, sigma3],[-sigma3, Z2]]))
gamma = [gamma0, gamma1, gamma2, gamma3]

# ---------- Field strengths ----------
def F_dn(mu, nu):
    return sp.diff(A[nu], coords[mu]) - sp.diff(A[mu], coords[nu])

# F^{μν} = η^{μα} η^{νβ} F_{αβ}
def F_up(mu, nu):
    return sum(eta_inv[mu,a]*eta_inv[nu,b]*F_dn(a,b) for a in range(4) for b in range(4))

# \tilde F^{μν} = (1/2) ε^{μνρσ} F_{ρσ}
def Fdual_up(mu, nu):
    return sp.Rational(1,2)*sum(sp.LeviCivita(mu,nu,r,s)*F_dn(r,s) for r in range(4) for s in range(4))

# ---------- Lagrangian density ----------
# EM pieces
L_em = -sp.Rational(1,4)*Z*sum(F_dn(mu,nu)*F_up(mu,nu) for mu in range(4) for nu in range(4)) \
       -sp.Rational(1,4)*TH*sum(F_dn(mu,nu)*Fdual_up(mu,nu) for mu in range(4) for nu in range(4))

# Spinor piece: i ψ̄ γ^μ ∂_μ ψ - m ψ̄ ψ - q ψ̄ γ^μ ψ A_μ
# Write with components explicitly.
def dpsi(mu, k):  # ∂_μ ψ_k
    return sp.diff(psi[k], coords[mu])

# i ψ̄ γ^μ ∂_μ ψ
term_dirac_kin = 0
for mu in range(4):
    for j in range(4):
        for k in range(4):
            term_dirac_kin += sp.I * phibar[j] * gamma[mu][j,k] * dpsi(mu, k)

# - m ψ̄ ψ
term_mass = - m * sum(phibar[j]*psi[j] for j in range(4))

# - q ψ̄ γ^μ ψ A_μ
term_gauge = 0
for mu in range(4):
    for j in range(4):
        for k in range(4):
            term_gauge += - q * phibar[j] * gamma[mu][j,k] * psi[k] * A[mu]

L_psi = term_dirac_kin + term_mass + term_gauge

L = L_em + L_psi

# ---------- Euler–Lagrange for A_ν ----------
def EL_for_A(nu):
    # ∂_μ (∂L/∂(∂_μ A_ν)) - ∂L/∂A_ν
    dL_d_dA = [sp.diff(L, sp.diff(A[nu], coords[mu])) for mu in range(4)]
    div_term = sum(sp.diff(dL_d_dA[mu], coords[mu]) for mu in range(4))
    dL_dA = sp.diff(L, A[nu])
    return sp.simplify(div_term - dL_dA)

# Construct target expression: ∂_μ( Z F^{μν} + Θ \tilde F^{μν} ) - j^ν  where j^ν = q ψ̄ γ^ν ψ
def current_nu(nu):
    # j^ν = q ψ̄ γ^ν ψ
    return q * sum(phibar[j]*gamma[nu][j,k]*psi[k] for j in range(4) for k in range(4))

def target_A(nu):
    divergence = 0
    for mu in range(4):
        divergence += sp.diff( Z*F_up(mu,nu) + TH*Fdual_up(mu,nu), coords[mu] )
    return sp.simplify(divergence - current_nu(nu))

EOM_A = [EL_for_A(nu) for nu in range(4)]
TARGET_A = [target_A(nu) for nu in range(4)]
em_ok = all(sp.simplify(EOM_A[nu] - TARGET_A[nu]) == 0 for nu in range(4))

# ---------- Euler–Lagrange for ψ̄ (phibar_j) → Dirac equation for ψ ----------
def EL_for_phibar(j):
    # ∂_μ (∂L/∂(∂_μ phibar_j)) - ∂L/∂phibar_j
    # L has no derivatives of phibar (first-order form), so first term is 0
    return sp.simplify(- sp.diff(L, phibar[j]))

# Expected Dirac operator on ψ:
def dirac_operator_component(j):
    expr = 0
    for mu in range(4):
        # i (γ^μ ψ)_{j} differentiated acts on psi, not gamma (constant)
        for k in range(4):
            expr += sp.I * gamma[mu][j,k] * sp.diff(psi[k], coords[mu])
    # - m ψ_j - q (γ^μ A_μ ψ)_j
    expr += - m*psi[j]
    gauge_term = 0
    for mu in range(4):
        for k in range(4):
            gauge_term += - q * gamma[mu][j,k] * A[mu] * psi[k]
    expr += gauge_term
    return sp.simplify(expr)

EOM_phibar = [EL_for_phibar(j) for j in range(4)]
TARGET_dirac = [dirac_operator_component(j) for j in range(4)]
dirac_ok = all(sp.simplify(EOM_phibar[j] - TARGET_dirac[j]) == 0 for j in range(4))

# ---------- Maxwell limit sanity check (Z→1, Θ→0, ψ→0) ----------
# Substitute Z(Φ)=1, TH(Φ)=0, psi=phibar=0
subs_limit = {Z: 1, TH: 0}
for j in range(4):
    subs_limit[psi[j]] = 0
    subs_limit[phibar[j]] = 0

maxwell_limit_ok = True
for nu in range(4):
    eom_lim = sp.simplify(EOM_A[nu].xreplace(subs_limit))
    # Expect: ∂_μ F^{μν} = 0  ⇒ eom_lim == ∑_μ ∂_μ F^{μν}
    lhs = eom_lim
    rhs = sum(sp.diff(F_up(mu,nu), coords[mu]) for mu in range(4))
    maxwell_limit_ok &= (sp.simplify(lhs - rhs) == 0)

# ---------- Report ----------
result = {
    "em_with_sources_identity": bool(em_ok),
    "dirac_minimal_coupling_identity": bool(dirac_ok),
    "maxwell_limit_ok": bool(maxwell_limit_ok)
}
print(json.dumps(result, indent=2))
