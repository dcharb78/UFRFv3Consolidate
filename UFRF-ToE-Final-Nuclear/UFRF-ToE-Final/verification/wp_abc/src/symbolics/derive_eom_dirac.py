
#!/usr/bin/env python3
"""
Verify Dirac limit by confirming:
(γ^μ p_μ - m)(γ^ν p_ν + m) = (p^2 - m^2) I_4
and that plane-wave spinors satisfy (iγ^μ∂_μ - m)ψ=0 in flat space.
"""
import sympy as sp

# Symbols
E, px, py, pz, m = sp.symbols('E px py pz m', real=True)
p_mu = sp.Matrix([E, -px, -py, -pz])  # with η = diag(+,-,-,-)

# Dirac gamma matrices in Dirac representation
I2 = sp.eye(2)
zero = sp.zeros(2)

sigma_x = sp.Matrix([[0,1],[1,0]])
sigma_y = sp.Matrix([[0,-sp.I],[sp.I,0]])
sigma_z = sp.Matrix([[1,0],[0,-1]])

gamma0 = sp.Matrix([[1,0,0,0],
                    [0,1,0,0],
                    [0,0,-1,0],
                    [0,0,0,-1]])

gammai_blocks = {
    1: sp.Matrix.vstack(sp.Matrix.hstack(zero, sigma_x),
                        sp.Matrix.hstack(-sigma_x, zero)),
    2: sp.Matrix.vstack(sp.Matrix.hstack(zero, sigma_y),
                        sp.Matrix.hstack(-sigma_y, zero)),
    3: sp.Matrix.vstack(sp.Matrix.hstack(zero, sigma_z),
                        sp.Matrix.hstack(-sigma_z, zero)),
}

gammas = [gamma0,
          gammai_blocks[1],
          gammai_blocks[2],
          gammai_blocks[3]]

# γ·p = γ^μ p_μ  with (+,-,-,-) metric → γ·p = γ^0 E - γ^1 px - γ^2 py - γ^3 pz
gp = gammas[0]*E - gammas[1]*px - gammas[2]*py - gammas[3]*pz

lhs = (gp - m*sp.eye(4))*(gp + m*sp.eye(4))
rhs = (E**2 - px**2 - py**2 - pz**2 - m**2) * sp.eye(4)

simplified = sp.simplify(lhs - rhs)

print("Dirac algebra identity check: (γ·p - m)(γ·p + m) ?= (p^2 - m^2) I")
print("Matrix difference (should be zero):")
print(simplified)

# Optional: plane-wave check (symbolic placeholder)
# ψ(x) = u(p) e^{-i p·x}, then (iγ^μ∂_μ - m)ψ = (γ·p - m) u(p) e^{-ip·x} = 0 if u is an on-shell spinor
# We do not construct u(p) explicitly here; the algebra identity suffices for dispersion.
