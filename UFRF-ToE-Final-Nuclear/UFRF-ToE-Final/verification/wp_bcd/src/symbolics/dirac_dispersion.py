
import sympy as sp

def gamma_matrices():
    # Pauli
    I2 = sp.eye(2)
    sx = sp.Matrix([[0,1],[1,0]])
    sy = sp.Matrix([[0,-sp.I],[sp.I,0]])
    sz = sp.Matrix([[1,0],[0,-1]])
    # Dirac representation, signature (−,+,+,+): {γμ,γν}=2ημν
    g0 = sp.Matrix([[1,0,0,0],
                    [0,1,0,0],
                    [0,0,-1,0],
                    [0,0,0,-1]])
    zero = sp.zeros(2)
    g1 = sp.Matrix.hstack(sp.zeros(2),  sx, ) .col_join( sp.Matrix.hstack(-sx, sp.zeros(2)) )
    g2 = sp.Matrix.hstack(sp.zeros(2),  sy, ) .col_join( sp.Matrix.hstack(-sy, sp.zeros(2)) )
    g3 = sp.Matrix.hstack(sp.zeros(2),  sz, ) .col_join( sp.Matrix.hstack(-sz, sp.zeros(2)) )
    return g0, g1, g2, g3

def dirac_determinant(w, kx, ky, kz, m):
    g0,g1,g2,g3 = gamma_matrices()
    # Operator D = γ^0 w - γ^1 kx - γ^2 ky - γ^3 kz - m I
    D = g0*w - g1*kx - g2*ky - g3*kz - m*sp.eye(4)
    return sp.factor(D.det())

if __name__ == "__main__":
    w,kx,ky,kz,m = sp.symbols('w kx ky kz m', real=True)
    det = dirac_determinant(w,kx,ky,kz,m)
    print({"det": str(det)})
