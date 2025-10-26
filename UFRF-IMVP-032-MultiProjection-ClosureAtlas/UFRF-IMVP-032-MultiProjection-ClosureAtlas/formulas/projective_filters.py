#!/usr/bin/env python3
import argparse, csv, json, math, sys
from typing import List, Dict, Any

def is_triangular(n: int) -> bool:
    # n = k(k+1)/2 ⇒ 8n+1 is perfect square
    x = 8*n + 1
    r = int(math.isqrt(x))
    return r*r == x

def nearest_triangular(n: int):
    # returns (k, T_k) minimizing |T_k - n|
    # k approx floor((sqrt(8n+1)-1)/2)
    k = int((math.sqrt(8*n+1) - 1)/2)
    candidates = [max(1,k-1), k, k+1]
    best = None
    for kk in candidates:
        Tk = kk*(kk+1)//2
        if best is None or abs(Tk-n) < abs(best[1]-n):
            best = (kk, Tk)
    return best  # (k, T_k)

def families_for_N(N: int) -> List[str]:
    fam = []
    pos13 = N % 13

    # Triangular families
    if is_triangular(N+1):
        fam.append("T_n_minus_1")
    if is_triangular(N):
        fam.append("T_n")
    if N % 2 == 0 and is_triangular(N//2):
        fam.append("2*T_n")

    # Multiples of 13
    if N % 13 == 0:
        fam.append("13k_submagic")

    # SO(4)/tesseract markers
    tesseract_counts = {8:"tesseract_3D_cubes",16:"tesseract_vertices",
                        24:"tesseract_squares",32:"tesseract_edges"}
    if N in tesseract_counts:
        fam.append(tesseract_counts[N])

    # Position class (for reporting)
    fam.append(f"pos13={pos13}")
    return fam

def scan_csv(path: str) -> Dict[str, Any]:
    rows = []
    with open(path) as f:
        r = csv.DictReader(f)
        for row in r:
            try:
                N = int(row["N"])
            except Exception:
                continue
            fam = families_for_N(N)
            row["families"] = ";".join(fam)
            rows.append(row)
    return {"rows": rows}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scan", type=str, help="CSV with column N")
    ap.add_argument("--out", type=str, default="scan_report.json")
    args = ap.parse_args()
    if args.scan:
        report = scan_csv(args.scan)
        with open(args.out, "w") as w:
            json.dump(report, w, indent=2)
        print(f"Wrote {args.out} with {len(report['rows'])} rows.")
    else:
        print("Nothing to do. Use --scan <csv>.")

if __name__ == "__main__":
    main()
