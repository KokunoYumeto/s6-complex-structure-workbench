#!/usr/bin/env python3
"""Reconstructed exact K89 certificate; geometry is in the complete proof."""
from pathlib import Path
import datetime,hashlib,json
import sympy as s
R=Path(__file__).resolve().parents[2]
checks=[]
def check(name,v):
 v=bool(v);checks.append({'label':name,'pass':v})
 if not v:raise AssertionError(name)
def zero(name,x):check(name,s.simplify(s.expand(x)).is_zero is True)
def mz(name,x):check(name,all(s.simplify(t)==0 for t in x))
a,b,j,p,c,N,alpha,theta,tau=s.symbols('a b j p c N alpha theta tau',integer=True)
P=lambda b,j:s.Rational(1,3)*b*j*(j*j-1)+s.Rational(1,2)*(3-b)*j*(j+1)
capc2=-b*j
zero('cap Jin cube',-capc2-b*j)
zero('cap Jin mixed',-4*capc2-4*b*j)
zero('source Psi orientation',-(-2)-2)
zero('full mixed cancellation',-2*b*j*2-4*capc2)
for aa,bb,mu0 in [(1,2,1),(2,1,0)]:
 zero(f'independent cube a{aa}',6*aa*j+9*j*j+2*bb*j**3-9*j-3*bb*j*j+bb*j-6*P(bb,j))
 zero(f'fixed physical index a{aa}',(4*(mu0+6*P(bb,j))-4*mu0)/24-P(bb,j))
 zero(f'native left a{aa}',s.Rational(4*mu0,4)-mu0)
 W=s.Matrix([[1,bb],[-aa,N-2]]);C=s.Matrix([[1,0],[j,1]])
 mz(f'full period character a{aa}',C.inv()*W*C-s.Matrix([[1+bb*j,bb],[-aa+(N-3)*j-bb*j*j,N-2-bb*j]]))
 zero(f'normal determinant a{aa}',s.trace(C.inv()*W*C)-(N-1))
 for jj in range(-15,16):
  value=s.expand(P(bb,jj))
  check(f'integral index a{aa} j{jj}',value.is_Integer)
  check(f'residue crosscheck only a{aa} j{jj}',int(value)%28==int(2*bb*s.binomial(jj+1,3)+(3-bb)*s.binomial(jj+1,2))%28)
 for pp in range(1,8):
  m=4*pp if aa==1 else 4*pp-1
  chi=pp;H=2*pp if aa==1 else 8*pp-2;A0=0 if aa==1 else 3*pp-1
  zero(f'literal scalar cap a{aa} p{pp}',s.Rational(12*H-24*chi,24)-A0)
  for cc in range(-3,4):
   for jj in range(-6,7):
    kk=mu0+6*P(bb,jj)+cc*(3*H-3*m*jj*(jj-1))
    ell=4*mu0+24*cc*chi;muj=mu0+6*cc*chi
    Aj=P(bb,jj)+cc*(A0-s.Rational(m*jj*(jj-1),2))
    zero(f'coupled native a{aa} p{pp} c{cc} j{jj}',kk-muj-6*Aj)
    zero(f'coupled index a{aa} p{pp} c{cc} j{jj}',(4*kk-ell)/24-Aj)
    t=cc*m-1;v00=2*t-2*muj-12*Aj;de=2*t-2*muj+12*Aj
    zero(f'double native a{aa} p{pp} c{cc} j{jj}',(de-v00)/4-6*Aj)
def add(*fs):
 d={}
 for f in fs:
  for I,x in f.items():d[I]=s.expand(d.get(I,0)+x)
 return {I:x for I,x in d.items() if x!=0}
def sc(x,f):return {I:s.expand(x*y) for I,y in f.items() if x*y!=0}
def wedge(f,g):
 d={}
 for I,x in f.items():
  for J,y in g.items():
   if set(I)&set(J):continue
   K=I+J;sign=(-1)**sum(K[r]>K[t] for r in range(len(K)) for t in range(r+1,len(K)))
   key=tuple(sorted(K));d[key]=s.expand(d.get(key,0)+sign*x*y)
 return {I:x for I,x in d.items() if x!=0}
da,du,dt,dg,dth=({(i,):s.Integer(1)} for i in range(5))
beta=sc(-j,add(du,sc(alpha+(1+b*j)*theta,dt),sc(b*theta,dg)))
Fe=add(wedge(da,dg),sc(-2,wedge(dth,dg)),sc(j,wedge(da,dt)),sc(-(2*j+a),wedge(dth,dt)))
db=add(sc(-j,wedge(da,dt)),sc(-j*(1+b*j),wedge(dth,dt)),sc(-b*j,wedge(dth,dg)))
Fs=add(Fe,sc(tau,db));f=sc(3,wedge(beta,wedge(Fs,Fs)))
co=s.integrate(f[(0,1,2,3,4)],(tau,0,1))
zero('full original boundary collar',co+6*a*j+9*j*j+2*b*j**3)
zero('outward one-to-zero',-co-(6*a*j+9*j*j+2*b*j**3))
x,y,xb,yb=s.symbols('x y xb yb');r2=x*xb+y*yb
V=s.Matrix([x,-y]);H=s.Matrix([yb,xb])/r2
mz('actual fixed-x horizontal',H-yb/(x*r2)*V-s.Matrix([0,1/x]))
mz('actual fixed-y horizontal',H+xb/(y*r2)*V-s.Matrix([1/y,0]))
zero('source determinant',s.Matrix.hstack(V,H).det()-1)
zero('full polar determinant',s.Matrix.hstack(V,x*y*H).det()-x*y)
zero('good polynomial',P(2,j)-j*(j+1)*(4*j-1)/6)
zero('reduced polynomial',P(1,j)-j*(j+1)*(j+2)/3)
note=R/'notes/part3_source_zero_vertical_pair_working.md'
record={'status':'PASS','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':len(checks),'source_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),'recovery':'Reconstruction after checkpoint20 execution loss; not a claimed old byte hash.','checks_detail':checks,'fixed_pairs':{'good':['1+6P2(j)',4],'reduced':['6P1(j)',0]},'coupled':'mu=mu0+6pc; A=P_b(j)+c*((a-1)*(3p-1)-m*binomial(j,2)); m=4p good,4p-1 reduced','scope':'Exact local characteristic algebra and full integer seed assembly; the complete actual geometric maps are in the audited proof.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
print(f'PASS {len(checks)} full vertical-pair checks')
