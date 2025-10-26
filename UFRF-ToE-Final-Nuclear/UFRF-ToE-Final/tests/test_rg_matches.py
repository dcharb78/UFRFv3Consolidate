import math
from src.symbolics.rg_flows import beta_qed_one_loop
def test_qed_beta_coefficient():
    # Check numeric coefficient 2/(3π) within tolerance
    alpha = 1/137.0
    n = 1
    num = beta_qed_one_loop(alpha, n)
    expected = 2.0*n/(3.0*math.pi)*alpha*alpha
    assert abs(num - expected) < 1e-15
