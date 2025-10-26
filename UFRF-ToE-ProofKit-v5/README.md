
# UFRF – ToE ProofKit v5 (Consolidated)

This self-contained repository unifies the **Maxwell–Dirac–Yang–Mills** action spine (v3) with the
**recursive projection / PPN resonance** engine (v4), plus a **multi-dimensional SU(3) fingerprint battery**.

## Quick Start

```bash
export PYTHONPATH=$(pwd)

# Core physics validations
python validations/run_all_core.py

# PPN recursive resonance
python validations/ppn_recursive_resonance.py

# SU(3) multi-dimensional fingerprint battery
python validations/run_su3_multidim.py
```

Artifacts (JSON/LOG) appear in `artifacts/`.
