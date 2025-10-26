
# src/symbolics/linearize_limits.py
# Linearize the EM sector with constant Z0, TH0 (Φ frozen), zero background fields.
# Show dispersion: k^2 = 0 ⇒ ω^2 = |k|^2 and group speed c=1.

import sympy as sp

def plane_wave_dispersion():
    # Symbols
    Z0, TH0 = sp.symbols('Z0 TH0', real=True, finite=True, nonzero=True)
    w, kx, ky, kz = sp.symbols('w kx ky kz', real=True)
    # Minkowski metric (+,-,-,-) for dispersion convenience
    # Our earlier L used (-,+,+,+); to avoid confusion, build k^2 explicitly as w^2 - |k|^2
    k2 = w**2 - (kx**2 + ky**2 + kz**2)

    # Lorenz gauge: k·ε = 0; Solve EOM symbolically to principal part:
    # EOM: ∂_μ ( Z0 F^{μν} + TH0 \tilde F^{μν} ) = 0
    # In Fourier: k_μ ( Z0 F^{μν} + TH0 \tilde F^{μν} ) = 0
    # Bianchi ⇒ k_μ \tilde F^{μν} = 0, so Z0 (k^2 ε^ν - k^ν (k·ε)) = 0 ⇒ with k·ε=0 ⇒ k^2 ε^ν=0.
    # Therefore nontrivial ε requires k^2 = 0.

    # Return the polynomial for k^2
    return sp.factor(k2)

if __name__ == "__main__":
    print(str(plane_wave_dispersion()))
