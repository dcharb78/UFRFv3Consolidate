#!/usr/bin/env python3
import os, sys, pathlib

DEFAULT_INIT_DIRS = [
    'src', 'src/core', 'src/topology', 'src/analysis',
    'src/analysis/higher_traces', 'src/analysis/quasi_arithmetic'
]

DERIVATION_FILES = [
    ('validations/nuclear_magic_numbers', 'derivation.md'),
    ('validations/beta_function', 'derivation.md'),
    ('validations/ppn_parameters', 'derivation.md')
]

INIT_CONTENT = """# Package marker created by UFRF-IMVP-043
"""

DERIVATION_TEMPLATE = """# Derivation (Scaffold)

This file documents the step-by-step derivation, assumptions, and intermediate identities
so independent reviewers can reproduce the result without the main text.
"""

def ensure_init(path):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
    init_file = os.path.join(path, '__init__.py')
    if not os.path.exists(init_file):
        with open(init_file, 'w', encoding='utf-8') as w:
            w.write(INIT_CONTENT)
        print('[ADD] ', init_file)

def ensure_derivation(root, subdir, fname):
    d = os.path.join(root, subdir)
    if os.path.isdir(d):
        f = os.path.join(d, fname)
        if not os.path.exists(f):
            os.makedirs(d, exist_ok=True)
            with open(f, 'w', encoding='utf-8') as w:
                w.write(DERIVATION_TEMPLATE)
            print('[ADD] ', f)

def main():
    repo_root = sys.argv[1] if len(sys.argv)>1 else '.'
    for d in DEFAULT_INIT_DIRS:
        ensure_init(os.path.join(repo_root, d))
    for sub, fn in DERIVATION_FILES:
        ensure_derivation(repo_root, sub, fn)
    print('[OK] Patch complete.')

if __name__ == '__main__':
    main()
