
import sympy as sp

def plane_wave_dispersion():
    # Coordinates
    x = sp.symbols('x0:4', real=True)  # t,x,y,z
    t,x1,x2,x3 = x
    # Plane wave ansatz: A^ν(x) = ε^ν exp(i k·x), with k·x = -ω t + kx x + ky y + kz z
    ω, kx, ky, kz = sp.symbols('omega kx ky kz', real=True)
    i = sp.I
    phase = -ω*t + kx*x1 + ky*x2 + kz*x3
    # Polarization ε^ν (symbolic constants)
    eps = [sp.symbols(f"eps{nu}", complex=True) for nu in range(4)]
    Aup = [eps[nu]*sp.exp(i*phase) for nu in range(4)]
    # Lorenz gauge: ∂_ν A^ν = 0 -> -i ω ε^0 + i k·ε_spatial = 0
    gauge = -i*ω*eps[0] + i*(kx*eps[1] + ky*eps[2] + kz*eps[3])
    # Maxwell eq in vacuum (Z constant): ∂_μ ∂^μ A^ν - ∂^ν (∂·A) = 0
    # With Lorenz gauge the second term vanishes; we require □ A^ν = 0 -> (-ω^2 + k^2) ε^ν = 0
    k2 = kx**2 + ky**2 + kz**2
    box_on_A = [(-ω**2 + k2)*Aup[nu] for nu in range(4)]
    # Dispersion relation requires (-ω^2 + k^2) = 0
    dispersion = sp.simplify(-ω**2 + k2)
    return sp.simplify(gauge), sp.simplify(dispersion)

def run():
    gauge, dispersion = plane_wave_dispersion()
    print({
        "lorenz_gauge_condition": str(gauge),
        "dispersion_relation": str(dispersion),
        "ok_if_zero": bool(dispersion == 0)
    })

if __name__ == "__main__":
    run()
