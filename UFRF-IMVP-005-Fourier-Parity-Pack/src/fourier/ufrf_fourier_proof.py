
#!/usr/bin/env python3
# Minimal computational checks that mirror the project's documented Fourier claims.
# - Orthogonality: ∫ sin·cos = 0 (numeric)
# - 13-cycle phase mapping helper
# This file can live in repo root as `ufrf_fourier_proof.py`

import math, random

def numeric_dot_sin_cos(period=2*math.pi, samples=100000):
    s = 0.0
    for i in range(samples):
        t = period * (i+0.5) / samples
        s += math.sin(t) * math.cos(t)
    return s * (period / samples)

def phase_to_cycle_position(phi):
    # returns position in [0,13)
    return (phi * 13.0 / (2.0*math.pi)) % 13.0

def demo():
    dot = numeric_dot_sin_cos()
    print(f"[orthogonality] ∫ sin·cos dt ≈ {dot:.12f} (should be ~0)")
    phases = [random.random()*2*math.pi for _ in range(10)]
    positions = [phase_to_cycle_position(p) for p in phases]
    print("[mapping] example cycle positions:", [round(x,3) for x in positions])

if __name__ == "__main__":
    demo()
