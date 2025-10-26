
# IMVP‑026 — SU(3) Creutz Ratio & Near‑REST Running

**Goal.** Estimate a finite‑volume running‑coupling proxy from Creutz ratios
\(\chi(R,T) = -\ln\frac{W(R+1,T+1)W(R,T)}{W(R+1,T)W(R,T+1)}\) on synthetic SU(3) fields,
and scan a "REST‑nearness" knob ε that suppresses commutators.
We expect reduced non‑Abelianity (flatter coupling) as ε→0 if UFRF REST→abelianization holds.

**Run**
```bash
python3 src/su3_creutz/creutz_scan.py --N 18 --Lmax 7 --period 13
python3 src/su3_creutz/creutz_scan.py --N 18 --Lmax 7 --period 26
```
