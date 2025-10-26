
#!/usr/bin/env python3
import math, json, argparse, random, statistics, os

def sample_alpha():
    # sample technique components in [0,1] with mild bias near bands seen in docs
    aE = random.uniform(0.05, 0.7)
    aB = random.uniform(0.05, 0.7)
    return (aE, aB, math.sqrt(aE*aE + aB*aB))

def run_mc(n, Ostar, dM, S, eps_sigma=1e-6, seed=12345):
    random.seed(seed)
    obs = []
    alphas = []
    for _ in range(n):
        aE,aB,atot = sample_alpha()
        lnO = math.log(Ostar) + dM*atot*S + random.gauss(0.0, eps_sigma)
        O = math.exp(lnO)
        obs.append(O)
        alphas.append(atot)
    return obs, alphas

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=2000)
    ap.add_argument("--Ostar", type=float, default=1.0)
    ap.add_argument("--dM", type=float, default=6.907, help="~ln(1000) for 144k vs 144")
    ap.add_argument("--S", type=float, default=-0.10)
    args = ap.parse_args()

    obs, alphas = run_mc(args.n, args.Ostar, args.dM, args.S)
    mu = statistics.mean(obs); sd = statistics.pstdev(obs)
    print(f"n={args.n}  mean(O)={mu:.9f}  std={sd:.3e}")
    print(f"alpha_total: mean={statistics.mean(alphas):.3f}, min={min(alphas):.3f}, max={max(alphas):.3f}")
    os.makedirs("artifacts", exist_ok=True)
    with open("artifacts/projection_mc.json","w") as f:
        json.dump({"mean_O":mu,"std_O":sd,"alphas_stats":{"mean":statistics.mean(alphas),"min":min(alphas),"max":max(alphas)}}, f, indent=2)
    print("Saved artifacts/projection_mc.json")

if __name__ == "__main__":
    main()
