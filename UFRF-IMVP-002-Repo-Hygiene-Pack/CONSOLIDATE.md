
# CONSOLIDATE: Repo Hygiene Pack

**Adds:**
- Missing `__init__.py` markers so `src/` is importable as a package
- `derivation.md` placeholders for `nuclear`, `beta`, `ppn` validations

**How to merge**
1) `bash scripts/apply_repo_hygiene.sh /path/to/your/repo`
2) Inspect new files; if a target file already exists in your repo, the script
   leaves it intact (`cp -n`). Fill each `derivation.md` with a short summary and
   pointers to code/figures.

**Why**
Your package review lists these as "expected but missing", and one incomplete
function. Package markers + derivation notes reduce friction for replication.
