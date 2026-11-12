"""Exact cylinder, prism, telescope-height and coordinate-recovery identities."""
from pathlib import Path
from collections import defaultdict
import hashlib,json
import sympy as S
W=Path(__file__).resolve().parents[1]
checks=[]
def check(name,value):
 assert value,name
 checks.append(name)
def add(out,key,value):
 out[key]+=value
 if not out[key]:del out[key]
def boundary(face):
 return [(face[:i]+face[i+1:],(-1)**i) for i in range(len(face))] if len(face)>1 else []
def prism(face):
 return [(tuple((v,0) for v in face[:i+1])+tuple((v,1) for v in face[i:]),(-1)**i) for i in range(len(face))]
for m in range(0,9):
 sigma=tuple(range(m+1));diff=defaultdict(int)
 for face,a in prism(sigma):
  for term,b in boundary(face):add(diff,term,a*b)
 for face,a in boundary(sigma):
  for term,b in prism(face):add(diff,term,a*b)
 add(diff,tuple((v,1) for v in sigma),-1)
 add(diff,tuple((v,0) for v in sigma),1)
 check(f'Entire signed prism identity in dimension {m}',not diff)
t,r,u,R,tau,rho=S.symbols('t r u R tau rho',real=True)
lam0=2/(2-t);lam1=1/r
time0=S.simplify(2+lam0*(t-2));time1=S.simplify(2+lam1*(t-2))
check('Cylinder bottom branch time is exactly zero',time0==0)
check('Cylinder side branch radius is exactly one',S.simplify(lam1*r)==1)
check('Cylinder switching values agree',S.simplify(lam0-lam1.subs(r,1-t/2))==0)
check('Cylinder nonnegative side time retains threshold',S.simplify(time1-(2*r+t-2)/r)==0)
check('Cylinder side time upper bound retains original factor',S.simplify(time1-t-(2-t)*(r-1)/r)==0)
check('Cylinder bottom is fixed',lam0.subs(t,0)==1)
check('Cylinder side is fixed',lam1.subs(r,1)==1 and time1.subs(r,1)==t)
samples=[S.Rational(i,16) for i in range(17)]
check('Exact rational cylinder domain and face values',all(
  (0<=2+min(2/(2-tt),1/rr if rr else S.oo)*(tt-2)<=tt and
   0<=min(2/(2-tt),1/rr if rr else S.oo)*rr<=1 and
   (2+min(2/(2-tt),1/rr if rr else S.oo)*(tt-2)==0 or min(2/(2-tt),1/rr if rr else S.oo)*rr==1))
  for tt in samples for rr in samples))
height=(1-tau)*t+tau*rho
check('Telescope homotopy starts at original height',height.subs(tau,0)==t)
check('Telescope homotopy ends at section height',height.subs(tau,1)==rho)
check('Telescope section is fixed throughout',S.expand(height.subs(t,rho)-rho)==0)
j,a,b=S.symbols('j a b',nonnegative=True)
check('Allowed telescope heights remain above the actual first stage',S.expand(height.subs({t:j+a,rho:j+b})-j-((1-tau)*a+tau*b))==0)
n=S.Symbol('n',integer=True)
check('Nested grid surrounding-layer bound retains both scales',S.simplify(2**(-n)-2**(-n-1)-2**(-n-1))==0)
inside=(1-tau)*u+tau*R
check('Original removed-disk radius is unchanged at the final retraction',inside.subs(tau,1)==R)
check('Punctured annulus inner-bound margin stays positive',S.expand(inside-R/2-((1-tau)*(u-R/2)+tau*R/2))==0)
check('Punctured annulus map agrees with the identity at its outer seam',S.expand(inside.subs(u,R)-R)==0)
check('Punctured annulus map starts at its original radius',inside.subs(tau,0)==u)
for dim in [1,2,4,6]:
 p=S.symbols('phi',nonzero=True)
 x=S.Matrix(S.symbols(f'x0:{dim}'))
 d=S.Matrix([S.symbols(f'd0:{dim}')])
 derivative=d.col_join(x*d+p*S.eye(dim))
 inverse=(-x/p).row_join(S.eye(dim)/p)
 check(f'Positive coordinate block recovers every original tangent coordinate, dimension {dim}',S.simplify(inverse*derivative)==S.eye(dim))
for dim in [2,4,6,7]:
 reflection=S.diag(-1,*([1]*(dim-1)))
 check(f'Original one-coordinate reflection determinant, dimension {dim}',reflection.det()==-1)
source=W/'src/cw-models-and-the-first-hurewicz-map.md'
result=dict(source=source.name,source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),passed=len(checks),checks=checks,scope='Formal prism coefficients, both exact cylinder branches, telescope height identities, original punctured-disk radii, coordinate-block derivative inverses and reflection signs. Finite checks supplement the full topological proofs.',independent_review=False)
(W/'checks/CW_HUREWICZ_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(passed=len(checks),source_sha256=result['source_sha256'])))
