
# Noether & Poynting from UFRF (IMVP‑014)

**Aim.** Connect UFRF's E×B vortex picture to standard energy‑momentum flow:
Poynting vector and energy density; provide a sanity check on plane waves.

## Key relations (vacuum)
- Energy density: u = (ε₀ E² + B²/μ₀)/2
- Poynting vector: S = (1/μ₀) E × B
- Momentum density: g = S/c²

At REST (E=B), impedance matching is perfect, maximizing energy transfer efficiency.

## How to run
```bash
python3 scripts/poynting_plane_wave.py
```
Prints cycle‑averaged u and |S| for a transverse wave and confirms S = u·c.
