
# IMVP‑020 — PPN Tensor Cleanroom (Units‑Aware)

**Goal.** Replace heuristic Δp→(γ,β) scaling with an explicit, units‑aware weak‑field metric mapping
from UFRF invariants into the standard PPN potentials.

**What this pack contains**
- `src/ppn/ppn_tensor_clean.py`: evaluates a small-parameter ansatz and extracts effective (γ−1), (β−1) with sanity checks.

**Run**
```bash
python3 src/ppn/ppn_tensor_clean.py --U 1e-8 --dp 0.10 --B0 1.0 --A 1.0 --B 1.0
```
