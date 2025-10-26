
#!/usr/bin/env python3
# Utilities for domain‑wise reporting and simple meta‑analytic combination.
from math import log
from typing import List, Tuple

def fisher_method(pvals: List[float]) -> float:
    # Combined p using Fisher's method (with explicit caveats!)
    # Requires scipy for chi2 CDF; report domain‑wise if scipy not available.
    try:
        from scipy.stats import chi2
    except Exception:
        raise RuntimeError("scipy not available; report domain‑wise instead.")
    X = -2.0*sum(log(p) for p in pvals if p>0)
    df = 2*len(pvals)
    return 1.0 - chi2.cdf(X, df)

def report_domainwise(domains: List[Tuple[str,float]]):
    return [{"domain": d, "p": p} for d,p in domains]
