
# IMVP‑023 — SU(3) Wilson Loops & 13/26 Diagnostics

**Purpose.** Extend to SU(3) (color) and look for 13/26 fingerprints in loop‑size dependence.
We keep near‑identity links and reunitarize to SU(3) via polar projection.

**Run**
```bash
python3 src/su3/wilson_su3_scan.py --N 16 --Lmax 8 --period 13
python3 src/su3/wilson_su3_scan.py --N 16 --Lmax 8 --period 26
```
