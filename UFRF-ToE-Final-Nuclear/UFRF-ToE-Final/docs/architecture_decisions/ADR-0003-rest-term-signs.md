

# ADR‑0003 (update): REST term written in manifestly gauge/Lorentz‑invariant form

We adopt the invariant scalars of electromagnetism:
\(
 I_1 \equiv F_{\mu\nu}F^{\mu\nu} = 2(B^2 - E^2), \qquad
 I_2 \equiv F_{\mu\nu}\tilde F^{\mu\nu} = -4\,\mathbf E\!\cdot\!\mathbf B.
\)

**Decision.** Use a CP–even, positive semi‑definite REST potential
\(
 V_{\text{REST}}(\Phi,F) = \mu(\Phi)\, I_1^2 + \lambda(\Phi)\, I_2^2, \quad \mu,\lambda \ge 0.
\)
It enters the Lagrangian as \(-V_{\text{REST}}\).

**Consequences.**
- Gauge invariance and Lorentz invariance are manifest (scalars built from \(F\)).
- Around backgrounds with \(I_1=I_2=0\) (vacuum, plane‑wave REST), the REST contribution is **quartic** in fields, so linearized dynamics are unmodified.
- Energy density increases away from \(I_1=I_2=0\), ensuring boundedness.
