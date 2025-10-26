# UFRF-ToE ProofKit v8: Validation Guide

This guide describes how to run each validation and check results.

## Environment
Install dependencies:

    conda env create -f environment.yml
    conda activate ufrf-toe

## Validations

Each script is run from the root:

    export PYTHONPATH=$(pwd)

### 1. Maxwell Identity + Action
    python validations/maxwell_bianchi.py
    → Checks Bianchi residual + prints Lagrangian density

### 2. Dirac Spinor + Current
    python validations/dirac_checks.py
    → Verifies j⁰ > 0 and minimal coupling energy shift

### 3. Yang–Mills SU(3) Fingerprint
    python validations/su3_multidim.py
    → Computes chordal 13/26 scores for small loops

### 4. Nuclear Shell Degeneracy
    python validations/nuclear_magic_check.py
    → Compares magic number pattern from degeneracy sums

### 5. Static PPN Extraction
    python validations/ppn_static_extract.py
    → Outputs γ, β and compares to Cassini/LLR bounds

### 6. Dynamic PPN Resonance
    python validations/ppn_dynamic_simulate.py
    → Time-averaged ⟨γ⟩, ⟨β⟩ over beat-driven projection loop

### 7. Projection Law: LoCuSS
    python validations/projection_cv_locusss.py
    → Held-out predictions using α_WL=0.3, α_HSE=0.7

## Expected Artifacts
See `artifacts/` for:
- ppn_dynamic_summary.json
- locusss_projection_summary.json
- su3_fingerprint_summary.json

Each includes SHA256 hashes to ensure reproducibility.
