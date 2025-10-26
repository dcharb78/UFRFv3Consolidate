
#!/usr/bin/env python3
# Find lines with 'σ' or 'off by' and propose projection‑law language.
# Usage:
#   python find_replace_language.py /path/to/repo > language_report.txt

import os, sys, re

PAT = re.compile(r"(off by\s+[0-9,]+σ|[0-9,]+\s*σ)", re.IGNORECASE)

def scan(root):
    for dirpath, _, files in os.walk(root):
        for fn in files:
            if fn.endswith((".md",".txt",".rst",".adoc")):
                p = os.path.join(dirpath, fn)
                try:
                    with open(p, "r", encoding="utf-8", errors="ignore") as f:
                        for i,line in enumerate(f, start=1):
                            if PAT.search(line):
                                print(f"{p}:{i}: {line.strip()}")
                                print("  → Suggest: Replace with 'intrinsic + projection (Axiom 5)' framing.")
                except Exception as e:
                    print(f"[warn] could not read {p}: {e}", file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: find_replace_language.py /path/to/repo")
        sys.exit(1)
    scan(sys.argv[1])
