from src.projection.projection_law_fit import demo_synthetic, fit_projection

fit = demo_synthetic(n=50, O_star=1.37, S=-0.05, rng=42)
print("Recovered O* ≈", fit["O_star"], "S ≈", fit["S"], "stderr =", fit["stderr"])
