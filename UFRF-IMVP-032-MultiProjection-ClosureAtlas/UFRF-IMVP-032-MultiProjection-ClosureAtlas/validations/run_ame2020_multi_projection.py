#!/usr/bin/env python3
\"\"\"
Extend AME-2020 nuclear gap analysis with multi-projection families.
This is a scaffold: point it to your AME CSV (Z,N, A, Energy or Gap columns).
Outputs a JSON report tagging each nucleus with:
- pos13 class (A % 13)
- family hits (T_n-1, T_n, 2*T_n, 13k_submagic, tesseract markers)
- REST exclusion flag (pos13 in {0,5,10,12})
- heuristic ranking (boundary-supported vs projective-only)
\"\"\"
import argparse, csv, json, math, os
from formulas.projective_filters import families_for_N

REST_EXCLUDE = {0,5,10,12}

def classify_A(A: int):
    fam = families_for_N(A)
    pos13 = A % 13
    return {
        "A": A,
        "families": fam,
        "pos13": pos13,
        "rest_excluded": pos13 in REST_EXCLUDE
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ame_csv", required=True, help="Path to AME-2020 (min: columns A, Gap)")
    ap.add_argument("--out", default="artifacts/ame2020_multi_projection_report.json")
    args = ap.parse_args()

    rows = []
    with open(args.ame_csv) as f:
        r = csv.DictReader(f)
        for row in r:
            A_val = row.get("A") or row.get("MassNumber") or row.get("A_number")
            try:
                A = int(A_val)
            except Exception:
                continue
            rec = classify_A(A)
            gap = row.get("Gap") or row.get("Separation") or ""
            rec["gap"] = gap
            rows.append(rec)

    report = {"count": len(rows), "rows": rows}
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as w:
        json.dump(report, w, indent=2)
    print(f"[OK] Wrote {args.out} with {len(rows)} rows.")

if __name__ == "__main__":
    main()
