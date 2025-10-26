# PATCH GUIDE — Merge the Multi‑Projection Closure Atlas

1) Copy the `formulas/` and `validations/` folders into your repo under:
   `validations/nuclear_magic_numbers/` (recommended), or a sibling folder.

2) Add a CI step that runs:
   - `python3 validations/run_ame2020_multi_projection.py --ame_csv <your AME path>`
   - Stash the JSON report under `artifacts/` and link it from your Validation Index.

3) Documentation:
   - In your Validation Guide (nuclear section), add a “Multi‑Projection Atlas” subsection
     explaining the union‑of‑families approach and the REST/14‑Law gates.
   - Cross‑link to the SU(2)×SU(2) (SO(4)) section for the 16/32 markers.
