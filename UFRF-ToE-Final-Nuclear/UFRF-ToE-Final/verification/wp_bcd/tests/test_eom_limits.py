
# tests/test_eom_limits.py
import json, math
from pathlib import Path

def test_variable_couplings_eom():
    import importlib.util, sys
    p = Path(__file__).resolve().parents[1] / "src" / "symbolics" / "variable_couplings_eom.py"
    spec = importlib.util.spec_from_file_location("variable_couplings_eom", p.as_posix())
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    out = mod.derive_em_eom_variable_couplings()
    assert out["target_all_zero"] is True, "EL eqn did not reduce to ∂μ(ZF^{μν}+ΘF~^{μν})=J^ν"
    assert out["bianchi_identity"] == "0"

def test_linearized_dispersion_lightlike():
    import importlib.util, sympy as sp
    from pathlib import Path
    p = Path(__file__).resolve().parents[1] / "src" / "symbolics" / "linearize_limits.py"
    spec = importlib.util.spec_from_file_location("linearize_limits", p.as_posix())
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    k2 = sp.simplify(mod.plane_wave_dispersion())
    # The light cone condition is k2 == 0 for propagation; we check it's exactly (ω^2 - |k|^2)
    w, kx, ky, kz = sp.symbols('w kx ky kz', real=True)
    assert sp.simplify(k2 - (w**2 - (kx**2 + ky**2 + kz**2))) == 0

def test_dirac_det_identity():
    import importlib.util, sympy as sp
    from pathlib import Path
    p = Path(__file__).resolve().parents[1] / "src" / "symbolics" / "dirac_free_check.py"
    spec = importlib.util.spec_from_file_location("dirac_free_check", p.as_posix())
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    residual = mod.dirac_det_identity()
    assert residual == 0
