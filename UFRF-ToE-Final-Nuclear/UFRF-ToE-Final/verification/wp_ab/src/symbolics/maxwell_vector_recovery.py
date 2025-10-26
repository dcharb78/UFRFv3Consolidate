
import sympy as sp

def vector_maxwell_recovery():
    # Symbols
    kx, ky, kz, w, Z, TH = sp.symbols('kx ky kz w Z TH', real=True)
    kvec = sp.Matrix([kx, ky, kz])
    # Unknowns (complex Fourier amplitudes)
    Ex, Ey, Ez, Bx, By, Bz = sp.symbols('Ex Ey Ez Bx By Bz')
    E = sp.Matrix([Ex, Ey, Ez])
    B = sp.Matrix([Bx, By, Bz])

    # Constitutive laws from L(E,B): D = Z E + TH B ; H = Z B - TH E
    D = Z*E + TH*B
    H = Z*B - TH*E

    # Vacuum equations in Fourier domain (J=0, ρ=0):
    # Gauss: k·D = 0
    gauss = sp.simplify(kvec.dot(D))
    # Faraday: k×E + w B = 0  ->  k×E = - w B
    faraday = sp.simplify(kvec.cross(E) + w*B)
    # Ampere: k×H - w D = 0
    ampere = sp.simplify(kvec.cross(H) - w*D)

    # For Θ=0 and Z=1, combine to show wave equation -> (w^2 - |k|^2) E = 0
    Zv, THv = 1, 0
    subs = {Z:Zv, TH:THv}
    gauss0 = sp.simplify(gauss.subs(subs))
    faraday0 = sp.Matrix([sp.simplify(c.subs(subs)) for c in faraday])
    ampere0 = sp.Matrix([sp.simplify(c.subs(subs)) for c in ampere])

    # Eliminate B using Faraday: B = - (1/w) k×E (assume w ≠ 0)
    B_expr = - (1/w) * kvec.cross(E)
    amp_sub = sp.simplify((ampere0.subs({Bx:B_expr[0], By:B_expr[1], Bz:B_expr[2]})))
    # Now amp_sub should reduce to ( (k×(k×E))/w ) - w E = 0  ->  (|k|^2 - w^2) E_⊥ = 0
    # We'll compute the linear map on E and require its eigenvalues vanish on subspace orthogonal to k.
    # Build matrix M such that M*E = 0
    Ex_, Ey_, Ez_ = Ex, Ey, Ez
    M = sp.Matrix.hstack(
        sp.Matrix([sp.simplify(sp.diff(amp_sub[i], Ex_)) for i in range(3)]),
        sp.Matrix([sp.simplify(sp.diff(amp_sub[i], Ey_)) for i in range(3)]),
        sp.Matrix([sp.simplify(sp.diff(amp_sub[i], Ez_)) for i in range(3)])
    )
    # Evaluate determinant on a subspace orthogonal to k by choosing a specific k (generic) and checking dispersion.
    # Choose k along z for simplicity: k=(0,0,k)
    kv = {kx:0, ky:0, kz:sp.symbols('k', real=True)}
    Mz = sp.simplify(M.subs(kv))
    # For k along z, the physical polarizations are Ex,Ey; Ez is longitudinal (gauge). Expect (w^2 - k^2) on transverse block.
    # Extract 2x2 transverse block acting on (Ex,Ey)
    M_tt = sp.Matrix([[Mz[0,0], Mz[0,1]],[Mz[1,0], Mz[1,1]]])
    det_tt = sp.simplify(sp.factor(M_tt.det()))
    return sp.simplify(det_tt)

if __name__ == "__main__":
    det_tt = vector_maxwell_recovery()
    print({"transverse_det": str(det_tt)})
