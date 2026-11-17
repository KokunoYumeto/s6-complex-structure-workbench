#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime,timezone
import sympy as s,json
n,J,t,a,theta=s.symbols('n J t alpha_q theta')
def add(*ds):
 out={}
 for d in ds:
  for k,v in d.items():out[k]=s.simplify(out.get(k,0)+v)
 return {k:v for k,v in out.items() if v!=0}
def mul(c,d):return {k:s.simplify(c*v) for k,v in d.items() if s.simplify(c*v)!=0}
def wedge(p,q):
 out={}
 for I,A in p.items():
  for K,B in q.items():
   if set(I)&set(K):continue
   sign=(-1)**sum(i>k for i in I for k in K)
   L=tuple(sorted(I+K));out[L]=out.get(L,0)+sign*A*B
 return {k:s.simplify(v) for k,v in out.items() if s.simplify(v)!=0}
e=[{(i,):s.Integer(1)} for i in range(5)]
da,du,dv,dg,dt=e
F0=wedge(da,dg)
beta=add(mul(-n,du),mul(-n*(a-6*theta),dv))
dbeta=add(mul(-n,wedge(da,dv)),mul(6*n,wedge(dt,dv)))
Fext=add(F0,mul(n,wedge(da,dv)))
checks=[]
def ck(name,x,y):assert x==y,(name,x,y);checks.append(name)
ck('source actual curvature square',wedge(Fext,Fext),{})
ck('source seam curvature square',wedge(dbeta,dbeta),{})
ck('source full boundary curvature',add(Fext,dbeta),add(F0,mul(6*n,wedge(dt,dv))))
Ft=add(Fext,mul(t,dbeta)); form=mul(3,wedge(beta,wedge(Ft,Ft)))
out={k:s.integrate(v,(t,0,1)) for k,v in form.items()}
ck('source fifth-form coefficient',out,{tuple(range(5)):18*n*n})
beta2=add(mul(-n,du),mul(-n*a,dv)); dbeta2=mul(-n,wedge(da,dv))
Fs=add(wedge(add(da,mul(J,dt)),dg),mul(n,wedge(add(da,mul(J,dt)),dv)))
ck('scalar exterior curvature square',wedge(Fs,Fs),{})
ck('scalar seam curvature square',wedge(dbeta2,dbeta2),{})
Fst=add(Fs,mul(t,dbeta2));form2=mul(3,wedge(beta2,wedge(Fst,Fst)))
out2={k:s.integrate(v,(t,0,1)) for k,v in form2.items()}
ck('scalar fifth-form coefficient',out2,{tuple(range(5)):3*J*n*n})
report={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS-algebra-only','checks':checks,'source_boundary_coefficient':'18*n^2','scalar_boundary_coefficient':'3*J*n^2','orientation':'dalpha_q du dv dgamma_B dtheta','scope':'No global gluing sign or integer characteristic pair inferred.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
print('PASS',len(checks),'exact exterior-form identities; integer-index refinement remains unpromoted.')
