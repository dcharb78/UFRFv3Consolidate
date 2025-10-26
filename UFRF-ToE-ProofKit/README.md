
# UFRF – ToE ProofKit (Self‑Contained)

This repository consolidates **axioms, theory, runnable code, validations, current status, and next steps**
for the Unified Fractal Resonance Framework (UFRF) ToE proof effort. It is **self‑contained** and designed
to be the starting point for a new conversation / new run.

## Quick Start

```bash
# from repo root
export PYTHONPATH=$(pwd)
python validations/run_all.py            # run core physics validations
python validations/run_su3_multidim.py   # run SU(3) multi-dimensional fingerprint battery
```

Artifacts (JSON/LOG/plots) are written to `artifacts/`.

## Contents

- `docs/AXIOMS.md` – Five axioms and glossary
- `docs/CORE_THEORY.md` – Trinity, 13‑cycle, REST, projection, Fourier
- `docs/CURRENT_STATUS.md` – What’s green / amber and why
- `docs/NEXT_STEPS.md` – Highest‑value runs to close the ToE proof
- `src/` – Python modules (Maxwell, Dirac, Yang–Mills, PPN, Projection, Nuclear, Ricci‑like flows)
- `validations/` – Runnable batteries (unit‑like and analysis runs)
- `artifacts/` – Results folder (created on first run)

This kit contains **no stubs**: all modules are implemented to run. Some analyses are minimal but complete.
