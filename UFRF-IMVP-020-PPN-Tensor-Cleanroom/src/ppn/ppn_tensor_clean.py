#!/usr/bin/env python3
import math, argparse

def near_rest_I1(dp, K=2.0*math.pi/13.0, B0=1.0):
    """Near-REST scalar invariant proxy I1 ~ -4 * B0^2 * K^2 * dp^2."""
    return -4.0*(B0*B0)*(K*K)*(dp*dp)

def ppn_from_ansatz(U, dp, A=1.0, B=1.0, B0=1.0, phi=(1.0+5**0.5)/2.0):
    """
    Minimal mapping:
      g00 = -1 + 2U + A*I1
      gij = δij * (1 + 2*γ*U + B*I1)
    Expose effective linearized shifts (γ−1), (β−1) by comparing coefficients of U.
    """
    I1 = near_rest_I1(dp, B0=B0)
    gamma_minus_1_eff = (B*I1) / (2.0*U*phi) if U != 0 else 0.0
    beta_minus_1_eff  = -(A*I1) / (2.0*U*(phi**3)) if U != 0 else 0.0
    return gamma_minus_1_eff, beta_minus_1_eff, I1

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--U", type=float, default=1e-8, help="dimensionless Newtonian potential at the experiment")
    ap.add_argument("--dp", type=float, default=0.10, help="distance from REST (dimensionless)")
    ap.add_argument("--A", type=float, default=1.0, help="coefficient A in g00 ansatz")
    ap.add_argument("--B", type=float, default=1.0, help="coefficient B in gij ansatz")
    ap.add_argument("--B0", type=float, default=1.0, help="baseline B amplitude for I1")
    args = ap.parse_args()
    g1, b1, I1 = ppn_from_ansatz(args.U, args.dp, A=args.A, B=args.B, B0=args.B0)
    print(f"Near-REST invariant I1 ≈ {I1:.3e}")
    print(f"(γ−1)_eff ≈ {g1:.3e}")
    print(f"(β−1)_eff ≈ {b1:.3e}")
    # Nominal reference windows (edit per docs)
    cassini = 2.4e-7
    llr     = 1.2e-7
    warn = []
    if abs(g1) > cassini: warn.append("γ bound (Cassini)")
    if abs(b1) > llr:     warn.append("β bound (LLR)")
    if warn: print("[CAUTION] Exceeds: " + ", ".join(warn))
    else:    print("Within Cassini/LLR windows (per current placeholders).")
    print(f"|I1|/U ≈ {abs(I1)/max(args.U,1e-300):.3e}  (small-perturbation check)")

if __name__ == "__main__":
    main()
