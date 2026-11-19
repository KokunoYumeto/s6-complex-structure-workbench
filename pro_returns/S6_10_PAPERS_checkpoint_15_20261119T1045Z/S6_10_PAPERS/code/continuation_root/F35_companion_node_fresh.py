#!/usr/bin/env python3
"""Exact companion and nodal data checks, written from statement-only inputs."""
from pathlib import Path
import sympy as s,json
t,x,lam=s.symbols('t x lambda')
Cf=s.Matrix([[0,0,0,-1],[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]])
Cg=s.Matrix([[0,0,0,-1],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
f=t**4+t**3+t**2+t+1;g=t**4+1
assert Cf.charpoly(t).as_expr()==f and Cg.charpoly(t).as_expr()==g
assert (Cf-Cg).rank()==1
e1=s.eye(4)[:,0];d=(Cf-Cg)[:,3]
Bc=s.Matrix.hstack(*[Cf**k*d for k in range(4)])
assert Bc.det()==1 and Bc.inv()*Cf*Bc==Cf
adjcol=(t*s.eye(4)-Cf).adjugate()*e1
assert adjcol==s.Matrix([t**3+t**2+t+1,t**2+t+1,t+1,1])
w=s.Matrix([[-1,0,0,1]])
assert s.expand((w*adjcol)[0])==g-f
assert Bc.inv()*Cg*Bc==Cf-e1*w
p=x**5+lam**3*x+lam**4
disc=s.factor(s.discriminant(p,x))
assert s.expand(disc-lam**15*(256+3125*lam))==0
a=-s.Rational(256,3125);r=s.Rational(64,625)
assert p.subs({x:r,lam:a})==0 and s.diff(p,x).subs({x:r,lam:a})==0
assert s.diff(p,x,2).subs({x:r,lam:a})!=0
q=s.div(p.subs(lam,a),(x-r)**2,x)
assert q[1]==0 and s.discriminant(q[0],x)!=0
assert s.diff(disc,lam).subs(lam,a)!=0
out={'status':'PASS','written_before_target_proof_and_old_producing_code':True,
 'companion_model_basis':str(Bc),'basis_determinant':str(Bc.det()),
 'rank_one_covector':str(w),'adjugate_column':str(adjcol),
 'curve_discriminant':str(disc),'nodal_cubic':str(s.factor(q[0])),
 'normalization_cubic_discriminant':str(s.factor(s.discriminant(q[0],x))),
 'scope':'Exact rational companion and supplied nodal algebra; the explicit normalization/annulus/primitive-cycle argument is in the prereading proof.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
