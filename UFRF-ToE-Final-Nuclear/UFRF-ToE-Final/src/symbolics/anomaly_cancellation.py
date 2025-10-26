from fractions import Fraction
Ncolor = 3
Y = {"Q_L": Fraction(1,6),"u_Rc": -Fraction(2,3),"d_Rc": Fraction(1,3),"L_L": -Fraction(1,2),"e_Rc": Fraction(1,1)}
def u1_cubic():
    s = 2*Ncolor * Y["Q_L"]**3
    s += Ncolor * Y["u_Rc"]**3
    s += Ncolor * Y["d_Rc"]**3
    s += 2 * Y["L_L"]**3
    s += Y["e_Rc"]**3
    return s
def su2_su2_u1(): return Ncolor*Y["Q_L"] + Y["L_L"]
def su3_su3_u1(): return 2*Y["Q_L"] + Y["u_Rc"] + Y["d_Rc"]
def grav_grav_u1():
    s = 2*Ncolor * Y["Q_L"] + Ncolor*Y["u_Rc"] + Ncolor*Y["d_Rc"] + 2*Y["L_L"] + Y["e_Rc"]
    return s
if __name__=='__main__':
    print({"U(1)^3": float(u1_cubic()), "SU(2)^2-U(1)": float(su2_su2_u1()), "SU(3)^2-U(1)": float(su3_su3_u1()), "grav^2-U(1)": float(grav_grav_u1())})
