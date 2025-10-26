#!/usr/bin/env bash
set -euo pipefail
echo "Running UFRF-ToE validation tests..."
python -V
python tests/test_wpB_variable_coupling.py
python tests/test_wpD_disformal_smallparams.py
python tests/test_wpC_yangmills_stub.py
python tests/test_wpC_maxwell_limit.py
python tests/test_wpC_dirac_limit.py
echo "All tests passed."
