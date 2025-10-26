
# PPN Normalization Kit — Usage & Rationale

**What this does**
- Encodes the near‑REST scaling `(γ−1)=b·κ·Δp²`, `(β−1)=−(a·κ/2)·Δp²` with `a/b=1/φ²`.
- Optional `B0²/U` factor can be folded in by multiplying κ (dimensionless normalization).
- Checks outputs against the project's Cassini/LLR bounds.

**How to run**
```bash
python3 scripts/ppn_delta_p2_driver.py --delta_p 1e-4 --kappa 1.0 --B0_sq_over_U none
```

**Notes**
- Apply the projection law to **observables**, not to the phase `p`; keep `Δp` intrinsic.
- Keep PPN parameters dimensionless.
