#!/usr/bin/env python3
import math, json, os

def phases_13():
    return [2.0*math.pi*n/13.0 for n in range(13)]

def enumerate_halfspins():
    thetas = phases_13()
    out = []
    idx = 0
    for n in range(13):
        theta = thetas[n]
        for half in [0, 0.5]:
            out.append({"index": idx+1, "n": n, "half": half, "angle_rad": theta + half*math.pi})
            idx += 1
    return out

def main():
    data = enumerate_halfspins()
    os.makedirs("artifacts", exist_ok=True)
    with open("artifacts/su2xsu2_26.json","w") as f:
        json.dump(data, f, indent=2)
    print("Wrote artifacts/su2xsu2_26.json with 26 entries.")

if __name__ == "__main__":
    main()
