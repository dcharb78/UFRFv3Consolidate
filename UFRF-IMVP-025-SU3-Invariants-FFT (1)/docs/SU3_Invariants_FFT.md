
# IMVP‑025 — SU(3) Invariants (Plaquette Action) & 13/26 FFT

**Goal.** Compute gauge‑invariant plaquette action density `S = 1 - Re(tr(U_p)/3)`
on a small SU(3) lattice built from near‑identity links modulated with period 13 or 26.
Fourier‑analyze the *spatial average* of S vs loop size to look for 13/26 fingerprints.

**Run**
```bash
python3 src/su3_invariants/plaquette_fft.py --N 16 --period 13 --Lmax 8
python3 src/su3_invariants/plaquette_fft.py --N 16 --period 26 --Lmax 8
```
