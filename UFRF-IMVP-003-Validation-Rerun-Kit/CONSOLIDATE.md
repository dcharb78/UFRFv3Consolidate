
# CONSOLIDATE: Validation Re‑run Kit

**How to use**
1) Create/activate an environment:
   ```bash
   conda env create -f templates/environment.yml
   conda activate ufrf-validation
   ```
2) From this pack’s root, run:
   ```bash
   bash scripts/run_all_validations.sh /path/to/your/repo
   ```
3) The script tees outputs into `./artifacts/*.log`. Copy any JSON/plots produced
   by the validation scripts into `./artifacts/` as well and update
   `templates/artifact_manifest.json` with filenames & checksums.

**Goal**
Freeze runnable evidence for the three headline validations (nuclear, β‑function, PPN).
