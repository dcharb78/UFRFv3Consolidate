
#!/usr/bin/env python3
import math, argparse

def compute(dp, U, a=1.0, b=1.0, K=2.0*math.pi/13.0, B0=1.0, phi=(1.0+5**0.5)/2.0):
    # Using the algebraic structure provided in the sketch: I1 ~ -4 B0^2 K^2 dp^2 near REST
    # and gamma-1 ~ -2 b B^2 K^2 dp^2 / U (with optional 1/phi factor), beta-1 ~ +2 a B^2 K^2 dp^2 / U (with optional 1/phi^3).
    B2 = B0*B0
    fac = 2.0 * B2 * K*K * (dp*dp) / max(U, 1e-300)  # protect div-by-zero
    gamma_minus_1 = -(fac * b) / phi                   # adopt the 1/phi modulation
    beta_minus_1  =  (fac * a) / (phi*phi*phi)         # adopt the 1/phi^3 modulation
    return gamma_minus_1, beta_minus_1

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dp", type=float, default=0.10, help="distance from REST in cycle units")
    ap.add_argument("--U", type=float, default=1e-8, help="dimensionless Newtonian potential")
    ap.add_argument("--a", type=float, default=1.0, help="geometric coefficient a")
    ap.add_argument("--b", type=float, default=1.0, help="geometric coefficient b")
    ap.add_argument("--B0", type=float, default=1.0, help="baseline B amplitude")
    args = ap.parse_args()

    g1, b1 = compute(args.dp, args.U, a=args.a, b=args.b, B0=args.B0)
    print(f"(γ−1) ≈ {g1:.3e}")
    print(f"(β−1) ≈ {b1:.3e}")
    # Compare against doc bounds (Cassini & LLR; using values cited in your README/cross‑validation docs)
    cassini_bound = 2.4e-7   # |gamma-1| < 2.4e-7
    llr_bound     = 1.2e-7   # |beta-1|  < 1.2e-7
    warn = []
    if abs(g1) > cassini_bound: warn.append("γ bound (Cassini)")
    if abs(b1) > llr_bound:     warn.append("β bound (LLR)")
    if warn:
        print("[CAUTION] Exceeds: " + ", ".join(warn))
    else:
        print("Within cited bounds (per package docs).")

if __name__ == "__main__":
    main()
