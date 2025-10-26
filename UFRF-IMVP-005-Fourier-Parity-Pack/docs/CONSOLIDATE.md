
# CONSOLIDATE: Fourier Proof Parity Pack (IMVP‑005)

**Goal**
Maintain a minimal, runnable orthogonality + phase‑cycle mapping check and ensure the
Index/Guide pointer always resolves.

**Steps**
1) `bash scripts/apply_fourier_pointer.sh /path/to/your/repo`
2) Run:
   ```bash
   python ufrf_fourier_proof.py
   ```
3) Optional: capture output in `artifacts/fourier_proof.log`.
