
#!/usr/bin/env python3
# Detects an anomaly near 28 K in a (T, value) CSV.
# Usage:
#   python materials_28K_scan.py input.csv artifacts/28K_report.json
# Columns required: T_K, value

import sys, csv, json

def detect_anomaly(T, V, center=28.0, window=2.0):
    deriv = [(V[i+1]-V[i])/(T[i+1]-T[i]) for i in range(len(T)-1) if T[i+1] != T[i]]
    midT  = [(T[i+1]+T[i])/2 for i in range(len(T)-1) if T[i+1] != T[i]]
    idxs = [i for i,t in enumerate(midT) if abs(t-center) <= window]
    window_vals = [abs(deriv[i]) for i in idxs]
    if not window_vals:
        return {"has_anomaly": False, "center": center, "window": window, "score": 0}
    score = sum(window_vals)/len(window_vals)
    return {"has_anomaly": True, "center": center, "window": window, "score": score}

def main():
    if len(sys.argv) < 3:
        print("Usage: materials_28K_scan.py input.csv output.json")
        sys.exit(1)
    src, out = sys.argv[1], sys.argv[2]
    T, V = [], []
    with open(src, newline="") as f:
        r = csv.DictReader(f)
        for row in r:
            try:
                T.append(float(row["T_K"])); V.append(float(row["value"]))
            except:
                pass
    report = detect_anomaly(T, V)
    with open(out, "w") as fo:
        json.dump(report, fo, indent=2)
    print("[materials] report saved:", out)

if __name__ == "__main__":
    main()
