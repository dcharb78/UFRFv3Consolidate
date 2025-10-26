# UFRF API Reference

## Core Modules

### projection_law.py

```python
class ProjectionLaw:
    def __init__(self, M_obs, M_source):
        """Initialize with observer and source scales"""
    
    def observe(self, O_star, alpha, S, epsilon=1e-6):
        """Calculate observed value from source value"""
        return O_obs
```

### manifold.py

```python
class UFRFManifold:
    def compute_euler_characteristic(self):
        """Compute χ(M) for 3-manifold"""
    
    def compute_hopf_invariant(self):
        """Compute Hopf linking number"""
```

### triple_series.py

```python
def compute_triple_series(a, b, c, max_order=20):
    """Compute S_{a,b,c} triple series"""
    return S
```

## Validation Scripts

All in `validations/` directory with complete documentation.

---
*See source code for full API details.*
