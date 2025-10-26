# Getting Started with UFRF

## 1. Read the Axioms

Start with `../AXIOMS.md` - understand the 5 first principles.

## 2. Follow the Theory

Read in this order:
1. `theory/foundations/trinity_structure.md`
2. `theory/foundations/13_cycle.md`
3. `theory/foundations/REST_equilibrium.md`
4. `theory/foundations/projection_law.md`
5. `theory/foundations/golden_ratio.md`

## 3. Run a Validation

```bash
cd validations/nuclear_magic_numbers
python3 validation.py
```

You should see 100% recall on all 11 known magic numbers.

## 4. Explore the Code

```python
from src.topology.triple_series import compute_triple_series
S = compute_triple_series(a=1, b=2, c=3, max_order=20)
print(f"Triple series S = {S:.6f}")  # Should be ~0.0016
```

## 5. Deep Dive

Choose a topic:
- **Nuclear physics**: `theory/physics/nuclear_structure.md`
- **Gravity**: `theory/physics/emergent_gravity.md`
- **Quantum**: `theory/physics/quantum_emergence.md`
- **RG flows**: `theory/physics/rg_flows.md`

---
*Start simple, build understanding systematically.*
