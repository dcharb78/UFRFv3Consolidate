from src.numerics.lattice_rest_solver import find_rest_window
def test_rest_minimum_on_E_equals_B():
    out = find_rest_window(E_range=(-1,1), B_range=(-1,1), steps=41)
    assert abs(out['min_E'] - out['min_B']) < 1e-12
