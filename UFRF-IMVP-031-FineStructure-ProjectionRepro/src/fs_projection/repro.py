
import json, argparse, math, os, sys, time
from typing import List, Tuple

def parse_tech(arg: str) -> Tuple[str, float, float]:
    # "name:alpha:S"
    parts = arg.split(":")
    if len(parts) != 3:
        raise ValueError(f"Bad --tech '{arg}', expected name:alpha:S")
    name = parts[0]
    alpha = float(parts[1])
    S = float(parts[2])
    return name, alpha, S

def project(O_star: float, M_obs: float, M_tgt: float, alpha: float, S: float) -> float:
    d_M = math.log(M_obs / M_tgt)
    return math.exp(math.log(O_star) + d_M * alpha * S)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--M_obs", type=float, default=144000.0)
    ap.add_argument("--M_tgt", type=float, default=144.0)
    ap.add_argument("--O_star", type=float, default=137.036303776)
    ap.add_argument("--alpha", type=float, default=None, help="single-tech alpha")
    ap.add_argument("--S", type=float, default=None, help="single-tech S")
    ap.add_argument("--tech", nargs="*", default=[], help='Multiple techniques as "name:alpha:S"')
    ap.add_argument("--target", type=float, default=137.035999084, help="reference observed value for delta")
    ap.add_argument("--out", default="artifacts/fs_projection_results.json")
    args = ap.parse_args()

    results = {
        "M_obs": args.M_obs,
        "M_tgt": args.M_tgt,
        "d_M": math.log(args.M_obs/args.M_tgt),
        "O_star": args.O_star,
        "target": args.target,
        "techniques": []
    }

    tech_list = []
    if args.tech:
        for t in args.tech:
            tech_list.append(parse_tech(t))
    elif args.alpha is not None and args.S is not None:
        tech_list.append(("single", args.alpha, args.S))
    else:
        # sensible defaults
        tech_list = [
            ("optical", 0.30, -0.10),
            ("electronic", 0.50, -0.06),
            ("xray", 0.70, -0.04),
            ("grav", 0.90, -0.02),
        ]

    for name, alpha, S in tech_list:
        O_obs = project(args.O_star, args.M_obs, args.M_tgt, alpha, S)
        results["techniques"].append({
            "name": name,
            "alpha": alpha,
            "S": S,
            "O_obs": O_obs,
            "delta_vs_target": O_obs - args.target
        })

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Wrote {args.out}")
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
