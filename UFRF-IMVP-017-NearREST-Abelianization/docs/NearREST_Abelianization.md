
# IMVP‑017 — Near‑REST Abelianization Check

**Hypothesis (to test):** As systems approach REST (E≈B), effective
dynamics abelianize (commutator contribution small vs derivative part).

**What this does**
- Builds a family of SU(2) gauge fields parameterized by ε.
- Measures ratio `R = ⟨|g[A,A]|⟩ / ⟨|∂A|⟩` over the grid.
- Scans ε ∈ {1.0, 0.5, 0.2, 0.1, 0.05} and prints the trend.

**Run**
```bash
python3 src/abelianize/scan_comm_fraction.py
```
