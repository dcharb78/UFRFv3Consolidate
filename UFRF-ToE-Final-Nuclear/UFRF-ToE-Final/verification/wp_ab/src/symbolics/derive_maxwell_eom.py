
import sympy as sp

# Coordinates and symbols
t, x, y, z = sp.symbols('t x y z', real=True)
coords = (t, x, y, z)

# Minkowski metric diag(+,-,-,-)
eta = sp.diag(1, -1, -1, -1)
eta_inv = eta

# Vector potential components A_mu(x)
A0 = sp.Function('A0')(t, x, y, z)
A1 = sp.Function('A1')(t, x, y, z)
A2 = sp.Function('A2')(t, x, y, z)
A3 = sp.Function('A3')(t, x, y, z)
A = [A0, A1, A2, A3]

# Constants Z, Theta (constant in Maxwell limit)
Z, Theta = sp.symbols('Z Theta', real=True)

# Levi-Civita tensor ε^{μνρσ}
def eps(a,b,c,d):
    return sp.LeviCivita(a,b,c,d)

def d(mu, f):
    return sp.diff(f, coords[mu])

# F_{μν} = ∂_μ A_ν - ∂_ν A_μ
F = sp.MutableDenseNDimArray.zeros(4,4)
for mu in range(4):
    for nu in range(4):
        F[mu,nu] = d(mu, A[nu]) - d(nu, A[mu])

# F^{μν} = η^{μα}η^{νβ} F_{αβ}
F_up = sp.MutableDenseNDimArray.zeros(4,4)
for mu in range(4):
    for nu in range(4):
        s = 0
        for a in range(4):
            for b in range(4):
                s += eta_inv[mu,a]*eta_inv[nu,b]*F[a,b]
        F_up[mu,nu] = sp.simplify(s)

# tilde F^{μν} = (1/2) ε^{μνρσ} F_{ρσ}
tildeF_up = sp.MutableDenseNDimArray.zeros(4,4)
for mu in range(4):
    for nu in range(4):
        s = 0
        for rho in range(4):
            for sig in range(4):
                s += sp.Rational(1,2) * eps(mu,nu,rho,sig) * F[rho,sig]
        tildeF_up[mu,nu] = sp.simplify(s)

# L = -1/4 Z F_{μν}F^{μν} - 1/4 Θ F_{μν} tilde F^{μν}
L = -sp.Rational(1,4)*Z*sum(F[mu,nu]*F_up[mu,nu] for mu in range(4) for nu in range(4)) \
    - sp.Rational(1,4)*Theta*sum(F[mu,nu]*tildeF_up[mu,nu] for mu in range(4) for nu in range(4))

# Euler-Lagrange: ∂_μ (∂L/∂(∂_μ A_ν)) - ∂L/∂A_ν = 0
EL = []
for nu in range(4):
    dL_d_dA = []
    for mu in range(4):
        dL_d_dA_mu = sp.diff(L, sp.diff(A[nu], coords[mu]))
        dL_d_dA.append(dL_d_dA_mu)
    div_term = sum(sp.diff(dL_d_dA[mu], coords[mu]) for mu in range(4))
    dL_dA = sp.diff(L, A[nu])  # zero in vacuum
    EL.append(sp.simplify(div_term - dL_dA))

EL_simplified = [sp.simplify(e) for e in EL]

# Plane-wave ansatz: A_x = A1(t,z), others zero
Ax = sp.Function('Ax')(t, z)
subs_ansatz = {
    A0: 0, A1: Ax, A2: 0, A3: 0,
    sp.diff(Ax, x): 0, sp.diff(Ax, y): 0
}
EL_ansatz = [sp.simplify(e.subs(subs_ansatz)) for e in EL_simplified]
wave_eq = sp.simplify(EL_ansatz[1])

print("Maxwell EL (general) components E^ν(A):")
for i, e in enumerate(EL_simplified):
    print(f"E^{i} =", e)

print("\nPlane-wave reduction (A_x(t,z)):")
print("E^1 =", wave_eq)
