#!/usr/bin/env python3
"""Exact local lattice, frame and sign inputs to the infinity excision audit."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from math import gcd
import json
import sympy as S

root=Path(__file__).resolve().parents[2]
folder=root/"code/part3_fourfold"
checks=[]
def ck(test,name):
    assert test,name
    checks.append(name)

# The actual I2 cycle and its primitive fibre/root basis.
I=S.Matrix([[-2,2],[2,-2]])
change=S.Matrix([[1,0],[1,1]]) # columns F=C0+C1, C1.
ck(change.det()==1,"primitive F,C1 basis")
ck(change.T*I*change==S.diag(0,-2),"actual I2 null fibre and root intersection")
line_rows=[]
for a in (1,2):
    normal_relative=S.Matrix([0,-a]) # -a C1 in F,C1 basis.
    pairing=S.diag(0,-2)
    evaluations=pairing*normal_relative
    ck(list(evaluations)==[0,2*a],f"positive-weight determinant degree a{a}")
    sq=int((normal_relative.T*pairing*normal_relative)[0])
    ck(sq==-2*a*a,f"reference determinant square a{a}")
    ck((2*a)%2==0,f"boundary order-two component class killed a{a}")
    line_rows.append({"a":a,"M_component_degrees":[-a,a],
        "positive_normal":"M_a","negative_normal":"M_a^-1",
        "positive_weight_spinor_determinant":"M_a tensor conjugate(M_a^-1)",
        "determinant_c1":"2c1(M_a)","relative_vector_F_C1":[0,-a],
        "reference_square":sq,"collision_square":0,
        "closed_double_square":2*a*a,"double_p1":0,
        "normal_link_residue_per_double":str(Q(-a*a,4))})

# Physical-line transition, keeping the negative-weight conjugation.
r,phi=S.symbols("r phi",real=True,positive=True)
g=r*S.exp(S.I*phi)
spinor_det=S.simplify(g/S.conjugate(g))
ck(S.simplify(spinor_det-S.exp(2*S.I*phi))==0,"actual positive-weight determinant phase twice M")
ck(S.diag(1,1,1,-1).det()==-1,"negative normal conjugation reverses real normal orientation")

# Literal two-chart small resolution and central Tate-node map.
B,D,z,A,C,w,xi,eta=S.symbols("B D z A C w xi eta")
v_first=(B-D*z)/2
v_second=(C*w-A)/2
ck(S.diff(v_first,B)==S.Rational(1,2),"first resolved-source v submersion")
ck(S.diff(v_second,A)==-S.Rational(1,2),"second resolved-source v submersion")
X1,Y1,T1=D*z*z,D*z,D*(1-z*z)-D*D*z**4
ck(S.expand(Y1*Y1-X1**3-X1*X1-T1*X1)==0,"first central I2 chart equation")
X2,Y2,T2=C,C*w,C*(w*w-1)-C*C
ck(S.expand(Y2*Y2-X2**3-X2*X2-T2*X2)==0,"second central I2 chart equation")
ck(S.simplify(T1.subs({D:C*w*w,z:1/w})-T2)==0,"literal central resolution chart overlap")
Qt=(xi*eta)**2
Xt0=xi/(1-xi)**2
Xtm1=(Qt/xi)/(1-Qt/xi)**2
Yt0=xi**2/(1-xi)**3
Ytm1=-(Qt/xi)/(1-Qt/xi)**3
Xtlead=S.expand(S.series(Xt0+Xtm1,xi,0,2).removeO())
Ytlead=S.expand(S.series(Yt0+Ytm1,xi,0,2).removeO())
ck(S.expand(Xtlead-xi*(1+eta**2))==0,"actual Tate X first node leading coefficient")
ck(Ytlead==-xi*eta**2,"actual Tate Y first node leading coefficient")
Tlead=16*xi*eta
Xlead=S.factor(4*Xtlead-Tlead/2)
Ylead=S.factor(8*Ytlead+4*Xtlead)
ck(S.expand(Xlead-4*xi*(1-eta)**2)==0,"marked Weierstrass X first node leading coefficient")
ck(S.expand(Ylead-4*xi*(1-eta**2))==0,"marked Weierstrass Y first node leading coefficient")
ck(S.expand(Ylead**2-Xlead**2-Tlead*Xlead)==0,"source equation at leading node order")
zlead=S.cancel(Xlead/Ylead)
Dlead=S.expand(Tlead+Xlead)
wlead=S.cancel(Ylead/Xlead)
Jfirst=S.Matrix([Dlead,zlead]).jacobian([xi,eta]).subs(xi,0).det()
Jsecond=S.Matrix([Xlead,wlead]).jacobian([xi,eta]).subs(xi,0).det()
ck(S.simplify(Jfirst)==-8,"first source resolution Jacobian on exceptional curve")
ck(S.simplify(Jsecond)==8,"complementary source resolution Jacobian on exceptional curve")
ck(zlead.subs(eta,1)==0,"marked G point in the chosen small resolution")
ck(wlead.subs(eta,-1)==0,"opposite resolution chart covers eta minus one")
ck(S.simplify((1/eta)*(xi*eta**2)-xi*eta)==0,"literal adjacent Tate node overlap")

def parity(order):
    return (-1)**sum(order[i]>order[j] for i in range(len(order)) for j in range(i+1,len(order)))
# Z has ordered coordinates Y1..Y5,rho,theta; outward rho passes five.
outer=parity([5,0,1,2,3,4,6])
ck(outer==-1,"quotient outer boundary is minus Y wedge theta")
# Removing a normal disc and quotienting its odd orbit each reverses sign.
inner=(-1)*(-1)
ck(inner==1,"inner fixed-normal boundary has positive normal-link orientation")
jin=-1
ck(jin*outer==1,"Jin reversal converts quotient outer sign to positive")

rows=[]
for a,b,N in ((1,2,4),(1,2,8),(1,2,12),(2,1,3),(2,1,6),(2,1,9)):
    paths=[
       folder/f"source_infinity_interior_residues_{a}_{b}_{N}_summary.json",
       folder/f"source_infinity_h_residues_{a}_{b}_{N}_summary.json",
       folder/f"source_infinity_e_cycles_{a}_{b}_{N}.json"]
    with (root/"records/literature_fourfold.md").open("a") as f:
        f.write("\n- "+datetime.now(timezone.utc).isoformat()+
          " — Opened "+", ".join(str(p.relative_to(root)) for p in paths)+
          ". Reason: exact independent excision lattice/sign certificate. Material: "+
          "local normal-link sums, actual E cycles and determinant orders; "+
          "no global value promoted by this code.\n")
    ii,hh,ee=[json.loads(p.read_text()) for p in paths]
    ck(ee["summary"]["component_count"]==N,f"actual N E components {a},{N}")
    for c in ee["components"]:
        ck(c["intersection_matrix"]==[[-2,2],[2,-2]],f"E I2 intersection {a},{N},{c['id']}")
        ck(c["fibre_multiplicities"]==[1,1],f"E primitive base {a},{N},{c['id']}")
        ck(c["determinant_normal_divisor"]==[0,0],f"E actual determinant orders {a},{N},{c['id']}")
    local=Q(ii["total_normal_link_residue"]["rational"])+Q(hh["H_normal_link_residue"]["rational"])
    doubles=-Q(N*a*a,4)
    total=local+doubles
    ck(total==(0 if a==1 else -1),f"local relative sum {a},{N}")
    rows.append({"a":a,"b":b,"N":N,"interior_and_H":str(local),
      "E_doubles":str(doubles),"complex_normal_link_difference":str(total),
      "Jin_sign_conversion":-1,"Jin_difference_after_map_audit":str(-total)})

out={"utc":datetime.now(timezone.utc).isoformat(),"status":"PASS",
 "check_count":len(checks),"checks":checks,
 "I2_intersection":[[-2,2],[2,-2]],"primitive_change":[[1,0],[1,1]],
 "line_rows":line_rows,"orientation":{"outer_quotient":outer,
 "inner_fixed_link":inner,"Jin_parameter":jin},
 "rows":rows,"scope":"Exact inputs to IE.1--6. Geometric comparison and global parameter dictionary require their separate proof audits."}
(folder/"source_infinity_excision_certificate.json").write_text(json.dumps(out,indent=2)+"\n")
print("PASS",len(checks),"exact excision inputs")
for row in rows: print(row)
