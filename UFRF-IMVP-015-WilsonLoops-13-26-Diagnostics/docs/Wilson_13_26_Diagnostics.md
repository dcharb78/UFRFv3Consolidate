
# IMVP‑015 — Wilson Loops & 13/26 Harmonics

**Goal.** Provide a gauge‑invariant diagnostic (Wilson loops) and search for
UFRF‑specific 13/26 periodic fingerprints in loop‑size dependence.

**What this does**
- Builds a small 2D periodic SU(2) lattice gauge configuration near identity.
- Injects a mild spatial phase with period `P` (you can set 13 or 26).
- Computes square Wilson loops W(L) for L = 1..L_max.
- FFT analyses the sequence {W(L)} to detect peaks near 1/13 and 1/26.
- Saves a summary JSON in `artifacts/`.

**How to run**
```bash
python3 src/wilson/wilson_13_26_scan.py --N 24 --Lmax 10 --period 13
python3 src/wilson/wilson_13_26_scan.py --N 24 --Lmax 10 --period 26
```
The script prints a compact report and writes `artifacts/wilson_scan.json`.
