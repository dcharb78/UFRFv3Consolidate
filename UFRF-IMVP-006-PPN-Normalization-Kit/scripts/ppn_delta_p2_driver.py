
#!/usr/bin/env python3
# Compute (γ−1) and (β−1) from Δp² law with a/b = 1/φ² and optional normalization.
# Checks against documented Cassini/LLR bounds.
# Usage:
#   python ppn_delta_p2_driver.py --delta_p 1e-4 --kappa 1.0 --B0_sq_over_U none

import math, argparse, json, sys

PHI = (1+5**0.5)/2

def compute_params(delta_p, kappa=1.0, a_over_b=None):
    if a_over_b is None:
        a_over_b = 1.0/(PHI**2)
    b = 1.0
    a = a_over_b * b
    gamma_minus_1 =  b*kappa*(delta_p**2)
    beta_minus_1  = -(a*kappa/2.0)*(delta_p**2)
    return gamma_minus_1, beta_minus_1, a_over_b

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--delta_p", type=float, required=True)
    ap.add_argument("--kappa", type=float, default=1.0)
    ap.add_argument("--B0_sq_over_U", type=str, default="none",
                    help="none or numeric; multiplies kappa if numeric")
    args = ap.parse_args()

    kappa = args.kappa
    if args.B0_sq_over_U.lower() != "none":
        try:
            v = float(args.B0_sq_over_U)
            kappa = kappa * v
        except:
            print("Invalid B0_sq_over_U; using kappa as is.", file=sys.stderr)

    g1, b1, ratio = compute_params(args.delta_p, kappa=kappa)
    # Bounds documented in the project README
    cassini_bound = 2.4e-7  # |γ−1|
    llr_bound     = 1.2e-7  # |β−1|

    report = {
        "delta_p": args.delta_p,
        "kappa": kappa,
        "a_over_b": ratio,
        "gamma_minus_1": g1,
        "beta_minus_1": b1,
        "passes": {
            "gamma": abs(g1) < cassini_bound,
            "beta":  abs(b1) < llr_bound
        },
        "bounds": {"gamma": cassini_bound, "beta": llr_bound}
    }
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
