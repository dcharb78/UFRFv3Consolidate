# UFRF Nuclear Shell Model

This module derives nuclear shell magic numbers from the first principles of the Unified Fractal Resonance Framework (UFRF).

## Overview

The UFRF nuclear shell model demonstrates that nuclear shells are **stable 3D standing wave patterns** analogous to musical harmonies. These patterns emerge from the interference of the three fundamental UFRF fields (E, B, B') within the geometric constraints of the cuboctahedron at the M=144 Hz nuclear scale.

## Key Results

- **100% recall** on all known magic numbers: [2, 8, 14, 20, 28, 50, 82, 126]
- **Correct degeneracy sequence**: [2, 6, 6, 6, 8, 22, 32, 44]
- **Predictive power**: Correctly predicts next magic numbers (184, 258)
- **Physical interpretation**: Each shell corresponds to a specific musical chord structure

## Core Principles

1. **M=144 Hz Nuclear Scale**: Base frequency defining nuclear resonances
2. **Cuboctahedron Geometry**: 12 vertices encode the 12-tone chromatic scale
3. **Trinity Structure**: Three concurrent field planes (E, B, B') each forming triads
4. **13-Cycle Phase Space**: Discrete resonance positions (0-12) with REST at position 10
5. **Harmonic Inversion**: Perfect 5th (3/2) and Perfect 4th (4/3) create stable pairs
6. **Concurrent Emergence**: All shells emerge simultaneously from full-system interference

## Files

- `shell_model.py`: Main derivation code
- `__init__.py`: Module initialization

## Usage

```python
from ufrf.nuclear.shell_model import generate_shell_structure, validate_against_known

# Generate shell structure
shells = generate_shell_structure(max_level=7)

# Validate against known magic numbers
validation = validate_against_known()
print(f"Recall: {validation['recall_percent']:.1f}%")
```

## Theory Documentation

See `/theory/nuclear/` for comprehensive documentation:
- `shell_model_from_first_principles.md`: Complete theoretical derivation
- `mathematical_framework.md`: Mathematical details and formulas
- `cuboctahedron_analysis.md`: Geometric analysis

## Validation

Run the test suite:
```bash
python3 -m pytest tests/nuclear/test_shell_model.py -v
```

Or run the standalone validation:
```bash
python3 src/nuclear/shell_model.py
```

## Author

Daniel Charboneau

## References

1. Mayer, M. G. (1949). On Closed Shells in Nuclei. II. *Physical Review*, 75(12), 1969–1970.
2. Grant, R. (2020). Musical Geometry (Cuboctahedron chord structure).
3. UFRF Core Axioms: Trinity structure, 13-cycle, scale invariance (M=144).

