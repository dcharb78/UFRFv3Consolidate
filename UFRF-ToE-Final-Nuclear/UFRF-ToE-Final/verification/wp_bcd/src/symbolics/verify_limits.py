# -*- coding: utf-8 -*-
"""Maxwell & Dirac limit verification (symbolic)."""
import sympy as sp

def maxwell_bianchi_identity():
    t, x, y, z = sp.symbols('t x y z', real=True)
    coords = (t, x, y, z)
    A = [sp.Function(f"A{mu}")(*coords) for mu in range(4)]
    F = sp.ImmutableDenseNDimArray([[
        sp.diff(A[nu], coords[mu]) - sp.diff(A[mu], coords[nu])
        for nu in range(4)] for mu in range(4)])
    # Check ∂_[α F_{βγ]} = 0 for αβγ = 0,1,2
    alpha, beta, gamma = 0, 1, 2
    expr = (sp.diff(F[beta, gamma], coords[alpha]) +
            sp.diff(F[gamma, alpha], coords[beta]) +
            sp.diff(F[alpha, beta], coords[gamma]))
    return sp.simplify(expr)

def maxwell_vacuum_plane_wave():
    t, x, y, z = sp.symbols('t x y z', real=True)
    coords = (t, x, y, z)
    eta = sp.diag(-1, 1, 1, 1)
    w, k = sp.symbols('omega k', positive=True, real=True)
    A_plane = [sp.Integer(0), sp.cos(k*z - w*t), sp.Integer(0), sp.Integer(0)]
    F_pw = sp.ImmutableDenseNDimArray([[
        sp.diff(A_plane[nu], coords[mu]) - sp.diff(A_plane[mu], coords[nu])
        for nu in range(4)] for mu in range(4)])
    F_pw_up = sp.ImmutableDenseNDimArray([[
        sum(eta[mu,a]*eta[nu,b]*F_pw[a,b] for a in range(4) for b in range(4))
        for nu in range(4)] for mu in range(4)])
    div = [sp.simplify(sum(sp.diff(F_pw_up[mu, nu], coords[mu]) for mu in range(4)))
           for nu in range(4)]
    on_shell = [sp.simplify(d.subs({w: k})) for d in div]
    return div, on_shell

def dirac_dispersion_check():
    I2 = sp.eye(2)
    sigma_x = sp.Matrix([[0, 1],[1, 0]])
    sigma_y = sp.Matrix([[0, -sp.I],[sp.I, 0]])
    sigma_z = sp.Matrix([[1, 0],[0, -1]])
    gamma0 = sp.Matrix([[I2, sp.zeros(2)],[sp.zeros(2), -I2]])
    gamma1 = sp.Matrix([[sp.zeros(2), sigma_x],[-sigma_x, sp.zeros(2)]])
    gamma2 = sp.Matrix([[sp.zeros(2), sigma_y],[-sigma_y, sp.zeros(2)]])
    gamma3 = sp.Matrix([[sp.zeros(2), sigma_z],[-sigma_z, sp.zeros(2)]])
    E, px, py, pz, m = sp.symbols('E px py pz m', real=True)
    gamma_dot_p = E*gamma0 - px*gamma1 - py*gamma2 - pz*gamma3
    M = sp.simplify(gamma_dot_p - m*sp.eye(4))
    det_M = sp.factor(M.det())
    expected = sp.factor((E**2 - (px**2 + py**2 + pz**2) - m**2)**2)
    return sp.simplify(det_M - expected)

if __name__ == "__main__":
    print("Bianchi identity (αβγ=0,1,2):", maxwell_bianchi_identity())
    div, on_shell = maxwell_vacuum_plane_wave()
    print("Maxwell divergence components (general plane wave):", div)
    print("Maxwell divergence on-shell (ω=k):", on_shell)
    print("Dirac dispersion remainder (should be 0):", dirac_dispersion_check())
