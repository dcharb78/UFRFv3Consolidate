
# IMVP‑016 — PPN from Cycle Position (Units-aware)

**Purpose.** Turn the informal Δp→(γ−1, β−1) sketch into a small,
units‑aware calculator that compares against published bounds cited in the package.

**What this does**
- Lets you specify Δp (distance from REST in the 13‑cycle), normalization U (Newtonian potential/c²),
  and geometric coefficients (a,b,K,B₀).
- Computes (γ−1) and (β−1) from the toy model and compares to bounds recorded in the docs.
- Prints a caution banner if inputs would overshoot the Cassini/LLR limits.

**How to run**
```bash
python3 src/ppn/ppn_from_cycle.py --dp 0.10 --U 1e-8 --a 1.0 --b 1.0
```
