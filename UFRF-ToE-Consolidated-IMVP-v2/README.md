
# UFRF-ToE Consolidated (IMVP)

This package consolidates the current **Unified Fractal Resonance Framework (UFRF)**
state into a single, runnable repository with code, docs, and artifacts:

- **Foundations**: Axioms, 13-cycle geometry, REST (E≈B, √φ), projection law.
- **Gauge sector**: U(1) Maxwell kinematics; SU(2)/SU(3) Yang–Mills kinematics,
  gauge-invariance gate, SU(3) REST abelianization scan, Wilson-loop spectra harness.
- **Gravity**: Weak-field metric from UFRF invariant I1 with **PPN extractors**.
- **Projection law**: Multi-technique calibration fitter (ln O = ln O* + d_M α S + ε).

## Quick Start

1) Set PYTHONPATH and run all validations:

```bash
export PYTHONPATH=$(pwd)
python scripts/run_all.py
```

Artifacts will be written to `artifacts/` with JSON/LOG summaries.

## Contents

- `docs/` — theory snapshots & runbook
- `src/` — Python modules (`gauge`, `gravity`, `projection`)
- `validations/` — runnable tests/demos
- `artifacts/` — results from this session and any new runs
- `scripts/run_all.py` — convenience launcher

