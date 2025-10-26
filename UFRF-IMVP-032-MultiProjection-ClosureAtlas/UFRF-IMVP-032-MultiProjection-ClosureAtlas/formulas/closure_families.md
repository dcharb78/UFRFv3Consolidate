# Closure families (operational definitions)

## A) 13‑cycle / 14‑Law family (primary)
- Core rule: closures anchor at cycle hand‑offs; positions 11–12–13 seed 1–2–3.
- Implementation: identify candidates whose empirical gaps peak within ±Δ of half‑integer transitions,
  then require **non‑REST** positions (exclude {0,5,10,12} mod 13).

## B) Triangular projections
- Triangular: T_n = n(n+1)/2
- Families:
  - T_n − 1  (captures 2, 14, 20, …)
  - T_n      (captures 28, …)
  - 2·T_n    (captures 20, 28, …)
- Usage: treat as **projective shadows** of the same SU(2)×SU(2) half‑spin sampling; keep as supportive, not decisive.

## C) Multiples of 13 (sub‑magic)
- Candidates: N = 13·k, k∈ℕ
- Rationale: 13‑cycle completions; used as **enhanced stability** markers rather than full closures.

## D) SO(4)/tesseract markers
- From SU(2)×SU(2) ≅ SO(4), 4D hypercube (tesseract) counts appear:
  - vertices = 16, edges = 32, squares = 24, cubes = 8
- Treat 16 and 32 as **diagnostic**: if nuclear data show local stability near these, tag as
  “SO(4)/tesseract‑coherent” and cross‑reference half‑spin indices.

## E) REST exclusion gate
- Exclude candidates at positions {0,5,10,12} (mod 13); position 10 is REST (E=B).

## Decision recipe
1. Build the union U of families B–D (projective candidates).
2. Apply the REST exclusion and the 14‑Law boundary test to U.
3. Down‑rank anything that only clears a projective family without boundary evidence.
4. Keep final “magic” set = boundary‑supported ∩ non‑REST; keep “sub‑magic” = stable ∩ multiple‑of‑13.
