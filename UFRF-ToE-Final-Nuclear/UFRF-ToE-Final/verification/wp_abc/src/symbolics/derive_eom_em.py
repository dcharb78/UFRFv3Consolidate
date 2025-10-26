
#!/usr/bin/env python3
"""
Derive Euler–Lagrange equations for the abelian gauge sector
L = -1/4 Z(Φ) F_{μν} F^{μν} - 1/4 Θ(Φ) F_{μν} \tilde F^{μν}
and confirm the Maxwell limit Z→1, Θ→0, ∂Φ→0 in flat metric.

We work in Minkowski metric η = diag(+1,-1,-1,-1) for the limit.
"""
import sympy as sp

# Coordinates and fields
t,x,y,z = sp.symbols('t x y z', real=True)
coords = (t,x,y,z)
eta = sp.diag(1,-1,-1,-1)

A0, A1, A2, A3 = [sp.Function(f"A{mu}")(*coords) for mu in range(4)]
A = sp.Matrix([A0, A1, A2, A3])

Phi = sp.Function("Phi")(*coords)

# Helper: derivatives
def d(mu, f):
    return sp.diff(f, coords[mu])

# Field strength F_{μν} = ∂_μ A_ν - ∂_ν A_μ
F = sp.MutableDenseNDimArray([0]*4*4, (4,4))
for mu in range(4):
    for nu in range(4):
        F[mu,nu] = d(mu, A[nu]) - d(nu, A[mu])

# Raise indices: F^{μν} = η^{μα} η^{νβ} F_{αβ}
eta_inv = eta
F_up = sp.MutableDenseNDimArray([0]*4*4, (4,4))
for mu in range(4):
    for nu in range(4):
        s=0
        for a in range(4):
            for b in range(4):
                s += eta_inv[mu,a]*eta_inv[nu,b]*F[a,b]
        F_up[mu,nu] = sp.simplify(s)

# Hodge dual: \tilde F^{μν} = 1/2 ε^{μνρσ} F_{ρσ}, with ε^{0123}=+1
eps = sp.MutableDenseNDimArray([0]*4*4*4*4, (4,4,4,4))
# Levi-Civita symbol
def levi(a,b,c,d):
    from itertools import permutations
    perm = (a,b,c,d)
    base = (0,1,2,3)
    # If any repeated indices, zero
    if len(set(perm)) < 4:
        return 0
    # sign of permutation
    sign = 1
    order = list(perm)
    # compute parity
    swap = 0
    for i in range(4):
        for j in range(i+1,4):
            if order[i] > order[j]:
                swap += 1
    sign = -1 if (swap % 2) else 1
    return sign

Fdual_up = sp.MutableDenseNDimArray([0]*4*4, (4,4))
for mu in range(4):
    for nu in range(4):
        s=0
        for rho in range(4):
            for sig in range(4):
                s += sp.Rational(1,2) * levi(mu,nu,rho,sig) * F[rho,sig]
        Fdual_up[mu,nu] = sp.simplify(s)

# Scalar functions Z(Φ) and Θ(Φ)
Z = sp.Function("Z")(Phi)
Th = sp.Function("Theta")(Phi)

# Invariants
I1 = 0  # F_{μν} F^{μν}
I2 = 0  # F_{μν} \tilde F^{μν}
for mu in range(4):
    for nu in range(4):
        I1 += F[mu,nu]*F_up[mu,nu]
        I2 += F[mu,nu]*Fdual_up[mu,nu]

# Lagrangian density
L = -sp.Rational(1,4)*Z*I1 - sp.Rational(1,4)*Th*I2

# Euler-Lagrange for A_ν: ∂_μ (∂L/∂(∂_μ A_ν)) - ∂L/∂A_ν = 0
# Note: L depends on A via F only, and ∂L/∂A = 0 in abelian case.
# We compute Π^{μν} = ∂L/∂(∂_μ A_ν) and then take ∂_μ Π^{μν}.
Pi = sp.MutableDenseNDimArray([0]*4*4, (4,4))

# Derivative of L w.r.t F_{αβ}: ∂L/∂F_{αβ} = -1/2 Z F^{αβ} - 1/2 Θ \tilde F^{αβ}
# Then ∂L/∂(∂_μ A_ν) = ∂L/∂F_{αβ} * ∂F_{αβ}/∂(∂_μ A_ν)
# and ∂F_{αβ}/∂(∂_μ A_ν) = δ_{αμ}δ_{βν} - δ_{αν}δ_{βμ}
for mu in range(4):
    for nu in range(4):
        s = 0
        for a in range(4):
            for b in range(4):
                dL_dF = -sp.Rational(1,2)*Z*F_up[a,b] - sp.Rational(1,2)*Th*Fdual_up[a,b]
                s += dL_dF * ( (1 if (a==mu and b==nu) else 0) - (1 if (a==nu and b==mu) else 0) )
        Pi[mu,nu] = sp.simplify(s)

# Divergence: EOM^ν = ∂_μ Π^{μν} + extra terms from gradients of Z,Θ.
EOM = [0]*4
for nu in range(4):
    div = 0
    for mu in range(4):
        div += sp.diff(Pi[mu,nu], coords[mu])
    EOM[nu] = sp.simplify(sp.expand(div))

# For presentation, factor the known structure:
# Expected: ∂_μ( Z F^{μν} + Θ \tilde F^{μν} ) + (∂_μ Z) F^{μν} + (∂_μ Θ) \tilde F^{μν} = 0
# Our Pi^{μν} should be -(Z F^{μν} + Θ \tilde F^{μν}), up to sign conventions.
# Let's compute S^{μν} = Z F^{μν} + Θ \tilde F^{μν} and show ∂_μ S^{μν} + extra = 0
S = sp.MutableDenseNDimArray([0]*4*4, (4,4))
for mu in range(4):
    for nu in range(4):
        S[mu,nu] = sp.simplify(Z*F_up[mu,nu] + Th*Fdual_up[mu,nu])

EOM2 = [0]*4
for nu in range(4):
    expr = 0
    for mu in range(4):
        expr += sp.diff(S[mu,nu], coords[mu])
    EOM2[nu] = sp.simplify(sp.expand(expr))

# Maxwell limit: Z=1, Θ=0, ∂Φ=0 ⇒ ∂_μ F^{μν} = 0 (in vacuum)
# We'll substitute Z=1, Th=0, Phi=Phi0 (constant → all derivatives zero).
subs_limit = {
    Z: 1,
    Th: 0,
}

# Make all derivatives of Phi zero by setting Phi to a symbol and then treating its derivatives as zero via substitution
Phi0 = sp.symbols("Phi0", real=True)
Phi_subs = {Phi: Phi0}
# Create derivative-zero substitutions
for mu in range(4):
    Phi_subs[sp.diff(Phi, coords[mu])] = 0

EOM2_lim = [sp.simplify(e.subs(subs_limit).subs(Phi_subs)) for e in EOM2]

print("Derived EOM (compact form): ∂_μ ( Z F^{μν} + Θ \\tilde F^{μν} ) = 0  up to gradients of Z,Θ")
for nu in range(4):
    print(f"EOM2[{nu}] (general) =", EOM2[nu])
print("\nMaxwell limit (Z=1, Θ=0, ∂Φ=0): should give ∂_μ F^{μν} = 0")
for nu in range(4):
    print(f"EOM2_lim[{nu}] =", EOM2_lim[nu])
