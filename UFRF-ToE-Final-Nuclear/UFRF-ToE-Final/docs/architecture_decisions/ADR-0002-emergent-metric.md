# ADR‑0002: Algebraic disformal emergent metric g_{μν}[F,Φ]

## Status
Accepted

## Context
To study gravity as emergent geometry without introducing higher‑derivative pathologies, we adopt an algebraic, disformal ansatz for the effective metric built from EM invariants and Φ.

## Decision
Use
```
g_{μν} = η_{μν} + a(Φ) η_{μν} I₁ + b(Φ) F_{μ}{}^{α} F_{να} + c(Φ) ∂_μΦ ∂_νΦ,
```
with small `a,b,c` in weak‑field regimes, and REST‑compatible potentials ensuring hyperbolicity.

## Consequences
- Minkowski is recovered at `a=b=c=0` (unit test included).
- Principal symbol matches Maxwell around vacuum (quartic REST terms enter at higher order).
- PPN/grav‑wave speed checks can proceed via linearization about small backgrounds.
