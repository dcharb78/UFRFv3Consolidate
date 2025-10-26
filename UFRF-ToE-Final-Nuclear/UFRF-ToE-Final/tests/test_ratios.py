from src.common.ratios import sqrt_phi
def test_sqrt_phi_value():
    val = sqrt_phi()
    assert abs(val - 1.2720196495) < 1e-9
