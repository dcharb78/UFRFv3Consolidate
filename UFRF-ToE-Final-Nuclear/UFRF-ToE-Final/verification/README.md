# UFRF-ToE Verification Packages

This directory contains standalone verification packages that provide clean, minimal proofs of specific theoretical claims in the UFRF-ToE framework.

## Purpose

These verification packages serve a different purpose than the main codebase:
- **Main codebase**: Complete implementation with full features and development history
- **Verification packages**: Clean, focused proofs for specific work packages

## Packages

### WP-ABC Verification
**Generated**: 2025-10-19 04:51:04  
**Files**: 13 | **Size**: 196KB  
**Work Packages**: A (Core action), B (Invariances), C (Recovery)

**Verifies**:
- UFRF action recovers Maxwell's equations (exact)
- UFRF action recovers free Dirac equation (exact)
- Bianchi identity holds (∂_{[α}F_{βγ]} = 0)
- Gauge invariance under A → A + ∂χ
- Dirac dispersion relation: det(γ·p - m) = (p² - m²)²

**Run**:
```bash
cd wp_abc
python src/symbolics/derive_eom_full.py
python tests/test_eom_limits.py
```

### WP-AB Verification
**Generated**: 2025-10-19 05:07:26  
**Files**: 23 | **Size**: 152KB  
**Work Packages**: A (Core action), B (Invariances & causality)

**Verifies**:
- Dirac local U(1) gauge invariance
- EM Hamiltonian positivity: ℋ = ½Z(E² + B²) for Z > 0
- Hyperbolicity: ω² = |k|² (lightlike characteristic speeds)
- Causality: characteristic speeds ≤ c

**Run**:
```bash
cd wp_ab
python tests/test_wpB_invariance_hyperbolicity.py
python tests/test_wpC_maxwell_vector.py
python tests/test_wpC_recovery_smoke.py
```

### WP-BCD Verification
**Generated**: 2025-10-19 05:21:05  
**Files**: 44 | **Size**: 240KB  
**Work Packages**: B (Invariances), C (Recovery), D (Emergent metric)

**Verifies**:
- Variable-coupling hyperbolicity with local Z(Φ), Θ(Φ)
- Disformal emergent metric remains Lorentzian near REST
- No superluminal propagation (Monte Carlo verified)
- Yang-Mills extension: positivity and hyperbolicity for Z > 0

**Run**:
```bash
cd wp_bcd
python tests/test_wpB_unitarity_causality.py
python tests/test_wpC_maxwell_limit.py
python tests/test_wpC_dirac_limit.py
python tests/test_wpC_yangmills_stub.py
python tests/test_wpD_disformal_smallparams.py
```

## Key Features

### Standalone Execution
Each package can run independently without the main codebase. They have minimal dependencies and are self-contained.

### Clean Implementations
These packages contain only the essential code needed to verify specific claims, making them ideal for:
- External review
- Publication supplements
- Independent validation
- Teaching and demonstration

### Documented Results
Each package includes a status document (README or WP-*-status.md) clearly stating what was verified and how to reproduce the results.

## Usage

### For External Validation
Reviewers can run these packages independently to verify theoretical claims without needing to understand the full codebase.

### For Publication
These packages can be submitted as supplementary material with publications, providing reviewers with executable proofs.

### For Teaching
The clean, focused implementations make excellent teaching examples for specific theoretical concepts.

## Relationship to Main Codebase

The verification packages are **distillations** of work done in the main development:
- **WP-ABC** corresponds to work in v2-v4 (WP-A focus)
- **WP-AB** corresponds to v5-v7 (WP-B invariances)
- **WP-BCD** corresponds to v10-v16 (WP-D emergent metric)

They were created after the main development work to provide clean, standalone validation artifacts.

## Requirements

### Python Dependencies
- sympy (symbolic mathematics)
- numpy (numerical computations)
- pytest (optional, for test framework)

### Installation
```bash
pip install sympy numpy pytest
```

Or use the environment files provided in each package.

## Attribution

**Author**: Daniel Charboneau  
**Project**: Unified Fractal Resonance Framework - Theory of Everything

## Notes

- These packages are preserved exactly as generated
- No modifications were made during synthesis
- They represent clean validation artifacts suitable for external review
- Each package is self-contained and can be distributed independently

