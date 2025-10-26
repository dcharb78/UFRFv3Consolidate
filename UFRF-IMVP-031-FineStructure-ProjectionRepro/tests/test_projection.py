
import math
from src.fs_projection.repro import project

def test_dM():
    M_obs, M_tgt = 144000.0, 144.0
    dM = math.log(M_obs/M_tgt)
    assert abs(dM - math.log(1000.0)) < 1e-12

def test_single_projection():
    # Using a small alpha*S to yield small shift
    O_star = 137.036303776
    M_obs, M_tgt = 144000.0, 144.0
    alpha, S = 0.3, -0.1
    O_obs = project(O_star, M_obs, M_tgt, alpha, S)
    # Expect O_obs slightly less than O_star for negative alpha*S
    assert O_obs < O_star
