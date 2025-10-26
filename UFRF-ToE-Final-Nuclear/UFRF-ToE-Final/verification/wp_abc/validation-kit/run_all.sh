#!/usr/bin/env bash
set -euo pipefail
python - <<'PY'
import sys,pytest; sys.exit(pytest.main(['-q']))
PY
