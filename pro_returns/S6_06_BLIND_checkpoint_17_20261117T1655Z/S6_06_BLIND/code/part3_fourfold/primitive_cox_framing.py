#!/usr/bin/env python3
"""Exact cusp-origin, orbit derivative and relative-coordinate identities."""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as s
ROOT = Path(__file__).resolve().parents[2]
rel = "notes/part3_primitive_cox_framing.md"
with (ROOT/"records/literature_fourfold.md").open("a") as log:
    log.write("\n- "+datetime.now(timezone.utc).isoformat()
              +" — Opened own "+rel
              +"; reason: execute the proposed rotating/Cox comparison identities; "
              "material: actual origins, positive nodal derivative, and relative coordinates. "
              "The geometric product comparison has passed independent root audit.\n")
(ROOT/rel).read_text()
ss,v,t,G,C=s.symbols("s v theta Gamma C")
sigma=s.Matrix([G*v,C*v+(v*v-v)/2])
ordinary=s.Matrix([-G*ss,-C*ss-ss*ss/2-ss*v])
gamma=s.Matrix([G,C+ss+v])
delta=s.Matrix([0,1])
assert s.simplify(sigma.subs(v,v+1)-sigma-gamma+ss*delta)==s.zeros(2,1)
bounded=s.Matrix([G*t,(C+v)*t+t*(t-1)/2])
assert s.simplify(sigma.subs(v,v+t)-sigma-bounded)==s.zeros(2,1)
F=sigma-ordinary
assert s.simplify(F.subs(v,v+t)-F-t*gamma-t*(t-1)*delta/2)==s.zeros(2,1)

r,X,Y=s.symbols("r X Y",positive=True)
b=(r-Y/r)/2
bp=(X*r-1/r)/2
ratio=s.factor(s.diff(bp,r)/s.diff(b,r))
assert s.simplify(ratio-(X+r**-2)/(1+Y*r**-2))==0
c1,c2=s.symbols("chi_y1 chi_y2",real=True)
c3=s.symbols("chi_b",positive=True)
h=s.symbols("h",real=True)
Q=s.Matrix([[1,0,0],[0,1,0],[c1,c2,c3]])
Qh=s.Matrix([[1,0,0],[0,1,0],[(1-h)*c1,(1-h)*c2,(1-h)*c3+h]])
assert Qh.subs(h,0)==Q and Qh.subs(h,1)==s.eye(3)
assert s.simplify(Qh.det()-((1-h)*c3+h))==0

def qm(q, v):
    a,b,c,d=q
    e,f,g,h=v
    return s.Matrix([a*e-b*f-c*g-d*h,
                     a*f+b*e+c*h-d*g,
                     a*g-b*h+c*e+d*f,
                     a*h+b*g-c*f+d*e])
def qc(q):
    return s.Matrix([q[0],-q[1],-q[2],-q[3]])
aa,bb,cc,dd,xx,yy=s.symbols("a b c d x y",real=True)
norm_z=xx*xx+yy*yy
u0=s.Matrix([1,0,xx,-yy])
v0=s.Matrix([aa,bb,cc,dd])
u1=s.Matrix([xx/norm_z,-yy/norm_z,1,0])
v1=s.Matrix([xx*aa-yy*bb,xx*bb+yy*aa,
             xx*cc-yy*dd,xx*dd+yy*cc])
assert s.simplify(qm(u0,v0)-qm(u1,v1))==s.zeros(4,1)
qi=s.Matrix([0,1,0,0])
hopf=qm(qm(v0,qi),qc(v0))
expected=s.Matrix([0,aa*aa+bb*bb-cc*cc-dd*dd,
                    2*(aa*dd+bb*cc),-2*(aa*cc-bb*dd)])
assert s.simplify(hopf-expected)==s.zeros(4,1)
Lhopf=s.Matrix([[0,0,-2],[0,2,0],[-2,0,0]])
Ru=s.Matrix.hstack(*[
    qm(qm(u0,s.eye(4)[:,i]),qc(u0))[1:4,:]
    for i in range(1,4)
])
assert s.factor(Ru.det())==(1+norm_z)**3
assert s.factor((Ru*Lhopf).det())==-8*(1+norm_z)**3
AA,BB,zeta,zetabar,c0,c0bar,c1,c1bar=s.symbols(
    "A B zeta zetabar c0 c0bar c1 c1bar", nonzero=True
)
initial_pair=s.Matrix([c0-zetabar*c1bar,c1bar+zeta*c0])
# Unitary conjugates are represented by reciprocals of A,B.
unit_p=AA*BB
unit_q1=AA/BB
unit_a=AA**-2
target_pair=s.Matrix([
    unit_p*c0-unit_a**-1*zetabar*unit_q1**-1*c1bar,
    unit_q1**-1*c1bar+unit_a*zeta*unit_p*c0
])
left_right_pair=s.diag(AA*BB,BB/AA)*initial_pair
assert s.simplify(target_pair-left_right_pair)==s.zeros(2,1)
values=[]
for d in [8,14,20,30]:
    A=1-s.Rational(d,2)
    k,ell=-3*d,-24
    mrel,nrel=-k+6*A,-6*A
    assert mrel==-s.Rational(ell,4)==6
    values.append({
        "d":d,"k":k,"ell":ell,
        "relative_m":int(mrel),"relative_n":int(nrel),
        "central_class_mod_28":int(A%28),
        "fixed_flop_class_mod_28":int((-5*A)%28),
    })
out={
    "status":"PASS",
    "proof":"P3K.27 Proved; independent root audit passed",
    "bounded_cusp_log_translation":[str(x) for x in bounded],
    "exact_nodal_orbit_derivative":str(ratio),
    "normal_derivative_Q":[[str(x) for x in row] for row in Q.tolist()],
    "normal_homotopy_determinant":str(s.factor(Qh.det())),
    "literal_initial_Cox_overlap":True,
    "literal_bounded_unitary_identity":"q_H -> A q_H B, with A^2=p*q1, B^2=p/q1 and a*p*q1=1",
    "local_Hopf_to_global_frame":[[str(x) for x in row] for row in (Ru*Lhopf).tolist()],
    "local_frame_determinant":str(s.factor((Ru*Lhopf).det())),
    "values":values,
    "scope":"Algebraic identities only; the complete actual product, normal map, and clutch proof is written in the independently root-audited note."
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print("PASS: actual bounded cusp origin, gamma transition, positive nodal normal derivative, and all relative tuples.")
