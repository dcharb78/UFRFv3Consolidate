
# Dirac Local U(1) Invariance — Short Proof Note (WP‑B)

We consider the minimally coupled Dirac Lagrangian (flat spacetime):
\[\mathcal{L}_D = \bar\psi ( i \gamma^\mu D_\mu - m ) \psi,\qquad D_\mu = \partial_\mu + i q A_\mu.\]

Under a local U(1) transformation with smooth real function \(\chi(x)\):
\[\psi \to e^{-i q \chi(x)} \psi,\quad \bar\psi \to \bar\psi\, e^{+i q \chi(x)},\quad A_\mu \to A_\mu + \partial_\mu \chi.\]

Compute the variation to first order in \(\chi\):
\[\delta\psi = -i q \chi\,\psi,\quad \delta\bar\psi = + i q \chi\,\bar\psi,\quad \delta A_\mu = \partial_\mu \chi.\]

Then
\[\delta \mathcal{L}_D
= \delta\bar\psi (i\gamma^\mu D_\mu - m)\psi
+ \bar\psi i\gamma^\mu \delta(D_\mu \psi)
- \bar\psi\, m\, \delta\psi.\]

Using \( \delta(D_\mu \psi) = -i q (\partial_\mu \chi)\psi - i q \chi D_\mu \psi\) and the relations above, all terms proportional
to \(\chi\) cancel pairwise, and the remaining terms combine into a **total divergence**:
\[\delta \mathcal{L}_D = \partial_\mu \big( \chi\, q\, \bar\psi \gamma^\mu \psi \big) \equiv \partial_\mu(\chi\, J^\mu).\]

Therefore the action \(\int d^4x\, \mathcal{L}_D\) is invariant (boundary term), with Noether current \(J^\mu = q\,\bar\psi\gamma^\mu\psi\).
This current is exactly the source that appears in the Maxwell equation derived from the UFRF action in the Maxwell limit.
