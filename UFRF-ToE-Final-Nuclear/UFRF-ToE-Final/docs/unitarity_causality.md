
# Unitarity & Causality (Draft, WP‑B)

**Scope.** Linearized analysis around (i) Minkowski vacuum and (ii) REST‑balanced states (I₁≈0), for the candidate UFRF action with soft REST terms.

## 1) Hamiltonian positivity (no ghosts)

Consider
\[\mathcal L = -\tfrac14 Z(\Phi) F_{\mu\nu}F^{\mu\nu} - \tfrac14 \Theta(\Phi) F_{\mu\nu}\tilde F^{\mu\nu} + \tfrac12(\partial\Phi)^2 - V_{13}(\Phi) - \mu(\Phi) (E^2-B^2)^2 - \nu(\Phi)\, \mathbf E\!\cdot\!\mathbf B + \ldots\]

Sufficient conditions in the small‑fluctuation regime:
- \(Z(\Phi_0) > 0\) (positive Maxwell kinetic term);
- \(|\Theta'(\Phi_0)|\) small (CP‑odd mixing bounded; acts as a total derivative for constant \(\Theta\));
- \(\mu(\Phi_0) \ge 0\) to penalize \(|E^2-B^2|\);
- quadratic expansion of \(V_{13}\) at a minimum: \(V_{13}''(\Phi_0) > 0\).

Under these, the quadratic Hamiltonian density is bounded below.

## 2) Characteristics & hyperbolicity

With the emergent disformal ansatz
\[ g_{\mu\nu} = \eta_{\mu\nu} + a(\Phi)\,\eta_{\mu\nu} I_1 + b(\Phi)\, F_\mu{}^{\alpha}F_{\nu\alpha} + c(\Phi)\,\partial_\mu\Phi\,\partial_\nu\Phi,\]
the principal symbol of the EM sector is governed by \(g^{\mu\nu}k_\mu k_\nu\). In REST‑like backgrounds (\(I_1\!\approx\!0\), \(\partial\Phi\) small), taking \(|a|,|b|,|c|\ll1\) yields luminal cones up to \(\mathcal O(a,b,c)\) with no superluminality. See `src/numerics/emergent_metric_solver.py` and the principal‑symbol check in the artifacts JSON.

**Result (current sandbox):** for a null wavevector \(k_\mu=(-\omega,0,0,k)\) with \(\omega=k\), \(g^{\mu\nu}k_\mu k_\nu = 0\) numerically to machine precision for small \((a,b)\).

## 3) Gauge symmetry & constraints

Gauge invariance under \(A_\mu\!\to\!A_\mu+\partial_\mu\chi\) holds for \(Z(\Phi),V_{13}\) and REST quartic terms; a spacetime‑dependent \(\Theta(\Phi)\) preserves gauge but can break CP. Dirac–Bergmann analysis proceeds as in Maxwell: two first‑class constraints remove unphysical polarizations; the scalar \(\Phi\) adds one healthy dof if \(+\tfrac12(\partial\Phi)^2\).

## 4) REST windows and √φ gain

At position 10 of the 13‑cycle (E≈B), the theory predicts an impedance‑matched transfer window with \(\sqrt\varphi\) enhancement; we linearize around \(I_1=0\) for well‑posedness and treat the window as a small‑parameter domain in which dissipationless mode‑conversion occurs. (See cited UFRF docs in `docs/ADR-0001` cross‑refs.)
