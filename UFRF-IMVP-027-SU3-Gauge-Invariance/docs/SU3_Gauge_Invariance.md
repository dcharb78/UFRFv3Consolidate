
# IMVP‑027 — SU(3) Gauge Transformation Invariance (Wilson Loops)

**Goal.** Verify numerically that **traced Wilson loops** `W(L)` are gauge‑invariant by
applying random site‑dependent SU(3) transformations `g(x)` and comparing pre/post values.
This is a sanity gate for all 13/26 diagnostics (they must be truly gauge‑invariant).

**Run**
```bash
python3 src/su3_gauge_invariance/check_invariance.py --N 16 --Lmax 8 --period 13
python3 src/su3_gauge_invariance/check_invariance.py --N 16 --Lmax 8 --period 26
```
