
# CONSOLIDATE: PPN Alignment Pack

**Where these files go**
- `docs/PPN-DeltaP2-PhiRatio.md` → `docs/` (new subsection under Mathematical Framework)
- `docs/Discoveries-PPN-Mapping-Note.md` → `discoveries/ppn_from_orbital_period.md` (replace toy mapping)
- `docs/AXIOMS-Projection-Footnote.md` → fold into `AXIOMS.md` (Axiom 5 example box)

**How to merge**
1) `bash scripts/apply_patch_ppn.sh /path/to/your/repo`
2) Open `validations/ppn_parameters/ppn_complete_derivation.py` and add the optional
   `B0sq_over_U` toggle (default None). Ensure the final PPN coefficients do **not**
   depend on `U` (only on `Δp²`). Keep `a/b = 1/φ²`.
3) Commit with message:
   `feat(ppn): add Δp² law + 1/φ² ratio; clarify orbital→phase mapping; projection footnote`

**Sanity checks**
- Re-run the PPN script and verify |γ−1| and |β−1| match prior artifacts.
- Record the ratio |β−1|/|γ−1| and confirm ~1/φ².
