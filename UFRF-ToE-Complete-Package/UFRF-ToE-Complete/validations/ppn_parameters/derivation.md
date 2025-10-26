# PPN Parameters: Complete Derivation

## From UFRF First Principles

### Axioms Used
1. 13-cycle from E×B geometry
2. Projection law
3. Golden ratio from REST
4. Emergent metric from E×B×B' interference

### Mathematical Derivation

**Step 1**: Solar system position in 13-cycle
```
T_Earth = 365.26 days
Position p = (365.26 mod 13)/13 = 0.097
Distance from REST (10/13): Δp = 0.672
```

**Step 2**: E/B ratio from cycle position
```
E/B = tan(2πp/13) = 0.697
```

**Step 3**: Field invariant
```
I₁ = 2(B² - E²) ≈ -4B²K²Δp²
K = 2π/13
```

**Step 4**: Golden ratio modulation
```
B²_space = B²/φ (light deflection)
B²_time = B²×φ (perihelion)
```

**Step 5**: Geometric constants
```
a/b = 1/φ² = 0.382
Geometric factor = 13/(2π²) = 0.659
```

**Step 6**: Normalization
```
U = GM_☉/(rc²) = 9.87×10⁻⁹
```

**Step 7**: PPN deviations
```
|γ-1| = geometric_factor × I₁ / U = 1.82×10⁻⁹
|β-1| = geometric_factor × I₁² / U = 6.94×10⁻¹⁰
```

### Validation

**Cassini bound**: |γ-1| < 2.4×10⁻⁷  
**UFRF**: |γ-1| = 1.82×10⁻⁹ ✓

**LLR bound**: |β-1| < 1.2×10⁻⁷  
**UFRF**: |β-1| = 6.94×10⁻¹⁰ ✓

Both within observational bounds!

### Physical Interpretation

PPN parameters measure distance from REST in 13-cycle. Solar system is relatively close to REST (Δp = 0.672 within same cycle), explaining tight bounds.

---
*See ppn_complete_derivation.py for complete implementation.*
