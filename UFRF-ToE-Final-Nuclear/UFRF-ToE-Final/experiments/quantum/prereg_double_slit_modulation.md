
# Prereg: Double-Slit Phase/Amplitude Modulation from UFRF Projection (v0)

**Hypothesis (UFRF):**
Fringe visibility and phase in a double-slit experiment show (a) enhancement with
REST gating (E≈B in beam/prep optics), and (b) small log-periodic modulation with
frequency ω = 2π/ln(13/12) in **log-scaled** control parameters (intensity, path-length,
wavelength tuning), independent of beam species (electrons/photons).

**Design:**
- Manipulate pre-slit field balance to approach REST (polarization/electronics)
- Vary a control parameter µ across decades (e.g., source current) and replot vs ln µ
- Fit amplitude/phase residuals to A cos(ω ln µ + φ) with ω fixed = 2π/ln(13/12)

**Metrics:**
- Primary: Bayes factor > 10 for model with fixed ω vs no-ripple
- Secondary: Increased visibility as I₁, I₂ → 0 (REST)

**Blinding/Hashes:**
- Freeze ω, priors on amplitude A ≤ 0.05
- Commit seed/config hashes in validation kit
