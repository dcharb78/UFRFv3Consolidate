
# validation-kit/run_all.py
# Minimal test runner to avoid external deps; imports and calls tests.
import importlib.util, sys, types, traceback
from pathlib import Path

TESTS_DIR = Path(__file__).resolve().parents[1] / "tests"

def run():
    failures = 0
    for test_file in sorted(TESTS_DIR.glob("test_*.py")):
        name = test_file.stem
        spec = importlib.util.spec_from_file_location(name, test_file.as_posix())
        mod = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(mod)
            for attr in dir(mod):
                if attr.startswith("test_") and callable(getattr(mod, attr)):
                    try:
                        getattr(mod, attr)()
                        print(f"[PASS] {name}::{attr}")
                    except AssertionError as e:
                        failures += 1
                        print(f"[FAIL] {name}::{attr} — {e}")
                    except Exception as e:
                        failures += 1
                        print(f"[ERROR] {name}::{attr} — {e}")
                        traceback.print_exc()
        except Exception as e:
            failures += 1
            print(f"[ERROR] Could not import {name}: {e}")
    print(f"\nSummary: {('ALL PASS' if failures==0 else str(failures)+' failure(s)')}")
    return failures

if __name__ == "__main__":
    import sys
    sys.exit(run())
