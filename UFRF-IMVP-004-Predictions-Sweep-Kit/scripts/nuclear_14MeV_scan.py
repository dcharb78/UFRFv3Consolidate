
#!/usr/bin/env python3
# Scan a CSV (A,Z,Energy_MeV) to detect a shell gap near 14.0 ± 0.25 MeV.
# Outputs a JSON summary with any detected discontinuity close to 14 MeV.
# Usage:
#   python nuclear_14MeV_scan.py input.csv artifacts/14MeV_report.json

import sys, csv, json, math

def detect_gap(energies, target=14.0, tol=0.25):
    hits = [e for e in energies if abs(e - target) <= tol]
    return {
        "target": target,
        "tolerance": tol,
        "count_hits": len(hits),
        "hits": hits[:50],
        "min_delta": min([abs(e-target) for e in hits], default=None)
    }

def main():
    if len(sys.argv) < 3:
        print("Usage: nuclear_14MeV_scan.py input.csv output.json")
        sys.exit(1)
    src, out = sys.argv[1], sys.argv[2]
    energies = []
    with open(src, newline="") as f:
        r = csv.DictReader(f)
        for row in r:
            try:
                energies.append(float(row.get("Energy_MeV", "")))
            except:
                pass
    report = detect_gap(energies)
    with open(out, "w") as fo:
        json.dump(report, fo, indent=2)
    print("[nuclear] report saved:", out)

if __name__ == "__main__":
    main()
