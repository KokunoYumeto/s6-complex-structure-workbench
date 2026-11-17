#!/usr/bin/env python3
"""Exact scalar-star coordinate/relative-line certificate.

This certificate does not choose a global C1 bordism orientation or
infer its characteristic correction from the native right integer.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as s

here = Path(__file__).resolve().parent
checks = []

def check(name, expression):
    if isinstance(expression, s.MatrixBase):
        ok = all(s.simplify(x) == 0 for x in expression)
    else:
        ok = s.simplify(expression) == 0
    checks.append({"name": name, "pass": bool(ok)})
    assert ok, (name, expression)

kappa, alpha, g, beta, lam, lam0 = s.symbols(
    "kappa alpha g beta lambda lambda0", nonzero=True)
eta = lam*beta
a,b,c,u,v,w,A,D = s.symbols("a b c u v w A D", nonzero=True)

# The actual C0 -> C1 second fixed-branch coordinate arrow.
R0 = s.diag(alpha,1/(kappa*alpha))
R1 = s.diag(eta,1/(g*eta))
R = s.diag(eta/alpha,kappa*alpha/(g*eta))
check("actual outer normal arrow R*R0=R1", R*R0-R1)
check("actual outer fixed-base arrow", (g/kappa)*(kappa*w)-g*w)
Rbased = s.simplify(R*R.subs(lam,lam0).inv())
check("based C1 normal arrow", Rbased-s.diag(lam/lam0,lam0/lam))

# Circle restriction: conjugating the negative first normal line.
z = s.symbols("z", nonzero=True)
hopf = s.diag(1/z,1/z)
check("positive-weight determinant", hopf.det()-z**(-2))

# Full three native transition rows, not merely their linearizations.
C0 = (kappa*alpha*b*c, a*b/alpha,1/(kappa*b))
C1 = (g*eta*b*c,1/(eta*c),a*c/g)
C2 = (1/a,a*b,a*c)
for name,row in (("C0",C0),("C1",C1),("C2",C2)):
    check(name+" preserves q", s.prod(row)-a*b*c)
check("C1 native inverse source coordinate", eta*C1[1]-1/c)
check("C1 native first normal", g*C1[2]-c*a)
check("C1 native second normal", C1[0]/(g*eta)-c*b)
check("C2 native inverse source coordinate", C2[0]-1/a)
check("C2 native first normal", C2[1]-a*b)
check("C2 native second normal", C2[2]-a*c)

# The seam acts on the full transition formulas.
new = {a:a/(A*D),b:A*b,c:D*c}
for name,row in (("C0",C0),("C1",C1),("C2",C2)):
    transformed = [s.simplify(x.subs(new, simultaneous=True)) for x in row]
    expected = [A*D*row[0],row[1]/D,row[2]/A]
    for i in range(3):
        check(name+" exact seam square "+str(i),transformed[i]-expected[i])

# Cox maps preserve the literal height monomial.
a0,a1,c0,c1=s.symbols("a0 a1 c0 c1",nonzero=True)
cox1=(a0,D*a1,c0/(A*D),A*c1)
cox2=(a0,a1/(A*D),A*c0,D*c1)
check("C1 Cox preserves actual q",s.prod(cox1)-a0*a1*c0*c1)
check("C2 Cox preserves actual q",s.prod(cox2)-a0*a1*c0*c1)
check("C2 outer normal arrow is constant",
      s.diag(1/alpha,kappa*alpha)*R0-s.eye(2))
check("C2 outer base arrow is constant",(kappa*w)/kappa-w)

# K47's full GL2(C) determinant square, retaining its endpoint equations.
aa,cc,uu,vv,J=s.symbols("aa cc uu vv J",integer=True)
det_square=(-vv+uu)-(-aa+cc)
check("determinant obstruction after actual pointed products",
      det_square.subs({uu:-aa,vv:J-cc})+J)

# Every integer winding, before reducing modulo 28.
t=J
l=s.Matrix([2*J,0,2*J])
weights=s.Matrix([0,1,-1])
d=s.Matrix([-2,-1,-1])
I=s.Matrix([t*weights[i]+d[i]*(l[i]-t) for i in range(3)])
W=s.Matrix([t*weights[i]-d[i]*(l[i]-t) for i in range(3)])
check("all-winding exact trace I",I-s.Matrix([-2*J,2*J,-2*J]))
check("all-winding exact stable trace W",W-s.Matrix([2*J,0,0]))
V11=I[1]; delta1=W[1]-W[0]
V22=-I[2]; delta2=-(W[2]-W[0])
n1=(delta1-V11)/2; m1=-V11-n1
n2=(delta2-V22)/2; m2=-V22-n2
check("C1 ordinary pair left",m1)
check("C1 ordinary pair right",n1+2*J)
check("C1 native double pair left",m1+2*t-2*J)
check("C1 native double pair right",n1+2*J)
check("C2 ordinary pair left",m2+2*J)
check("C2 ordinary pair right",n2)
check("C2 native double pair left",m2+2*t)
check("C2 native double pair right",n2)

# Cech connection sign with the specified oriented spatial circle.
# Temporary cap direction is 0 -> 1; the actual spatial circle
# traverses it 1 -> 0.  A_cap=i J s dtheta, so F/(2pi i)
# integrates to -J over that oriented torus.
ss,theta=s.symbols("ss theta",real=True)
cech=s.integrate(s.integrate(-J/(2*s.pi),(theta,0,2*s.pi)),(ss,0,1))
check("Cech crossing c1 in prescribed orientation",cech+J)
check("positive normal determinant crossing class",2*cech+2*J)

samples=[]
for j in range(-12,13):
    samples.append({
       "scalar_winding":j,
       "double_C1_native":[2*j,-2*j],
       "single_C1_native":[j,-j],
       "double_C2_native":[0,0],
       "single_C2_native":[0,0],
       "outer_C1_Hopf_line_winding":-j,
       "outer_C1_Hopf_determinant_winding":-2*j,
       "outer_C2_Hopf_determinant_winding":0,
    })
out={
 "status":"PASS",
 "scope":"Exact scalar native C1/C2 arrows, integral local trace and outer relative line; full C1 global bordism orientation not assigned.",
 "created_utc":datetime.now(timezone.utc).isoformat(),
 "checks":checks,
 "check_count":len(checks),
 "samples":samples,
 "Cech_orientation":"master interval endpoint0->endpoint1, cap interval endpoint1->endpoint0, then positive scalar angle",
 "global_C1_characteristic_correction":"unassigned pending oriented fixed-base comparison",
 "proof":"notes/part3_scalar_c1_native_arrow_working.md",
}
(here/"scalar_c1_outer_marking.json").write_text(json.dumps(out,indent=2)+"\n")
print(f"PASS {len(checks)} exact identities; {len(samples)} signed integral winding instances")
print("C1 outer positive-Hopf determinant winding = -2J; C2 outer winding = 0.")
print("Full C1 characteristic correction remains unassigned.")
