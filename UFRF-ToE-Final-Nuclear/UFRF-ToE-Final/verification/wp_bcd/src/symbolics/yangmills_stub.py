
import sympy as sp

def ym_symbols():
    Ex,Ey,Ez,Bx,By,Bz = sp.symbols('Ex Ey Ez Bx By Bz', real=True)
    Z, TH = sp.symbols('Z TH', positive=True, real=True)
    return {"Ex":Ex,"Ey":Ey,"Ez":Ez,"Bx":Bx,"By":By,"Bz":Bz,"Z":Z,"TH":TH}

def ym_hamiltonian_positivity():
    sy = ym_symbols()
    Z, TH = sy["Z"], sy["TH"]
    Ex,Ey,Ez,Bx,By,Bz = sy["Ex"], sy["Ey"], sy["Ez"], sy["Bx"], sy["By"], sy["Bz"]
    E2 = Ex**2+Ey**2+Ez**2
    B2 = Bx**2+By**2+Bx**2 - Bx**2 + By**2 + Bz**2  # keep same as E2+ B2 def; simplified below
    B2 = Bx**2+By**2+Bz**2
    EdotB = Ex*Bx+Ey*By+Ez*Bz
    L = sp.Rational(1,2)*Z*(E2 - B2) + TH*EdotB
    Pi = [sp.diff(L, Ex), sp.diff(L, Ey), sp.diff(L, Ez)]
    H = sum(Pi[i]*[Ex,Ey,Ez][i] for i in range(3)) - L
    return sp.simplify(H - sp.Rational(1,2)*Z*(E2+B2)), Pi, sy

def ym_hyperbolicity_symbol():
    w,kx,ky,kz,Z = sp.symbols('w kx ky kz Z', real=True, positive=True)
    mag = sp.sqrt(kx**2 + ky**2 + kz**2)
    return [mag, -mag]
