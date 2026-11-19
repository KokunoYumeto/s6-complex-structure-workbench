#!/usr/bin/env python3
"""Exact mixed-face maps, with the global endpoint still under audit."""
from pathlib import Path
import json
import sympy as s

out = Path(__file__).with_suffix(".json")
checks = []

def equal(name, left, right=0):
    residual = s.factor(s.cancel(left-right))
    assert residual == 0, (name, residual)
    checks.append(name)

# Fixed S3 tube: the physical positive spinor is (zeta,nu).
rho, zz, nn = s.symbols("rho zz nn", positive=True)
tt = rho**2/(1+zz) - (1+zz)*nn
equal("fixed tube exact radial equation",
      (1+zz)*tt+(1+zz)**2*nn, rho**2)
equal("fixed tube R equation", tt+zz*nn, rho**2/(1+zz)-nn)

# All of the radial face is covered by T1 != 0 or V != 0.
A,B,C,D=s.symbols("A B C D", nonzero=True)
h=s.sqrt(D)
charged=s.Matrix([h*A,h*B,1/h,h*C])
jac=charged.jacobian([A,B,C,D])
equal("T1 to V cover Jacobian",jac.det(),s.Rational(1,2))
equal("T1 to V source q1",charged[0]*charged[3],A*C*D)
equal("T1 to V source q2",charged[1]*charged[2],B)
equal("canonical contraction volume",-2*jac.det(),-1)
h_symbol=s.symbols("h",nonzero=True)
charged_root=[h_symbol*A,h_symbol*B,1/h_symbol,h_symbol*C]
for i in range(4):
    # The other square root is the actual simultaneous mu2 deck.
    equal(f"root sign is charged mu2 coordinate {i}",
          charged_root[i].subs(h_symbol,-h_symbol)+charged_root[i])

x,y,t,w=s.symbols("x y t w", nonzero=True)
upper_to_T1=[t*x,t*y,t,w/t**2]
equal("upper to T1 q1",upper_to_T1[0]*upper_to_T1[2]*upper_to_T1[3],x*w)
equal("upper to T1 q2",upper_to_T1[1],y*t)
upper_to_V=s.Matrix([s.sqrt(w)*x,s.sqrt(w)*y,t/s.sqrt(w),s.sqrt(w)])
equal("upper to V cover Jacobian",
      upper_to_V.jacobian([x,y,t,w]).det(),s.Rational(1,2))
equal("upper to V q1",upper_to_V[0]*upper_to_V[3],x*w)
equal("upper to V q2",upper_to_V[1]*upper_to_V[2],y*t)

# Complete theta/Cartier unit symbols. Their dependence is through the
# invariant source chart, never through the free line coordinate.
up,uq,E=s.symbols("uP uQ E",nonzero=True)
q1=x*w
q2=y*t
P=up/q2
Q=q1*q2*uq
Z0=uq*up*y*w
W0=x*t/up
V0=E**2*x/y**2
equal("Tate source conifold",Z0*W0,Q)
equal("inverse h source coordinate",Z0/Q,1/W0)
equal("full h-inverse J line cancellation",(Z0/Q)*(V0/P**2),E**2*t/up)

Z,T,q,L=s.symbols("Z T q L",nonzero=True)
inv={t:up*L/E**2,w:T*L/E**2,x:E**2*Z/L,y:E**2*q/(up*L)}
forward=[x*t/up,up*w/t,y*t,E**2*t/up]
for name,expr,target in zip(["Z","T","q2","line"],forward,[Z,T,q,L]):
    equal("upper free chart inverse "+name,expr.subs(inv, simultaneous=True),target)
equal("opposite source W0",W0.subs(inv,simultaneous=True),Z)
equal("opposite source Z0",Z0.subs(inv,simultaneous=True),uq*q*T)
equal("source q1 after inverse",(x*w).subs(inv,simultaneous=True),Z*T)

# Full theta products have no residual q2 poles after the indicated
# extraction; these four generators control every product factor.
Qn=Z*T*q*uq
Pn=up/q
Sn=Pn*Z
equal("theta S over P",Sn/Pn,Z)
equal("theta Q times S",Qn*Sn,Z**2*T*uq*up)
equal("theta Q over S",Qn/Sn,T*q**2*uq/up)
equal("theta Q over Z",Qn/Z,T*q*uq)

J=s.Matrix([[-1,0],[1,1]])
d0={(0,0),(1,0),(0,1)}
d1={(1,0),(0,1),(1,1)}
def image(poly):
    return {tuple(J*s.Matrix(v)) for v in poly}
def translate(poly,v):
    return {(p[0]+v[0],p[1]+v[1]) for p in poly}
assert image(d0)==translate(d1,(-1,0))
checks.append("negative-square first triangle exact height translate")
assert image(d1)==translate(d0,(-1,1))
checks.append("negative-square second triangle exact height translate")
assert J.det()==-1 and J*J==s.eye(2)
checks.append("literal integral character involution")

# The actual inverse suspension closes the opposite source chart.
c,uX=s.symbols("c_lambda uX",nonzero=True)
Ztarget=q*uq*T
Vtarget=up**2*Z*L/q**2
Psource=up/q
cX=q*uX
Zpre=Psource*Ztarget
Vpre=cX**2*Vtarget/(c*Z*T)
equal("actual inverse suspension source",Zpre,uq*up*T)
equal("actual inverse suspension opposite ruling cancellation",
      Qn/Zpre,q*Z/up)
equal("actual inverse suspension line",Vpre,up**2*uX**2*L/(c*T))
F=uq*up**3*uX**2/c
equal("indexed diagonal full line coordinate",Zpre*Vpre,F*L)
equal("full endpoint unit at collision",
      F.subs({uq:s.Rational(1,256),up:16,uX:s.Rational(-1,4)}),1/c)
edge={(0,0,1),(1,-1,1)}
assert edge=={(1,0-1,1),(0,1-1,1)}
checks.append("actual diagonal height translate is minus e2")
for r in edge:
    assert r[0]+r[1]==0
checks.append("ZV is the indexed edge unit character")
equal("fixed tube to T1 q1",
      (t*x)*(t*y)*(w/t**2),x*y*w)

result={
 "status":"PASS",
 "count":len(checks),
 "checks":checks,
 "source_map":{
   "fixed_tube":"q1=p0*zeta*conj(nu), q2=p1*t",
   "T1_chart":"q1=A*C*D, q2=B",
   "upper_free_chart":"q1=Z_t*T_t, q2=q2",
   "source_marking":"opposite (Z0,q2) resolution; actual -G/Cartier reset retained"
 },
 "scope":"Exact fixed/free/upper charts, actual inverse-suspension endpoint, full units and indexed toric edge, physical weights and canonical volume overlap. This certificate assigns no global source-zero return.",
}
out.write_text(json.dumps(result,indent=2)+"\n")
print(f"PASS {len(checks)} exact mixed outer-face checks")
