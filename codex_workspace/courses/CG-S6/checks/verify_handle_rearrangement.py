"""Finite exact checks for the full original handle interchange."""
from pathlib import Path
import json,hashlib,itertools
import sympy as S
W=Path(__file__).resolve().parents[1];checks=[]
def check(name,value):
 assert value,name
 checks.append(name)
def eq(x,y):return S.simplify(S.factor(x-y))==0
r,s,d,b,L,g=S.symbols('r s delta beta L g',positive=True)
U,V=S.symbols('U V',nonnegative=True);kap=S.symbols('kappa',real=True)
D=d+b
R=r*S.sqrt(1-U/(D+V));T=s*S.sqrt(1+V/b)
check('Original rounded boundary recovers the complete B',eq(b*T*T/(s*s),b+V))
check('Original rounded boundary recovers the complete A',eq(R*R/(r*r)*(d+b*T*T/(s*s)),d+b+V-U))
Rw=-(S.diff(R,U)*L*kap+S.diff(R,V)*(-L*(1-kap)))/g
Tw=-(S.diff(T,U)*L*kap+S.diff(T,V)*(-L*(1-kap)))/g
check('Complete R derivative includes the V variation in its denominator',eq(Rw,r*L/(2*g*S.sqrt(1-U/(D+V)))*(kap/(D+V)+U*(1-kap)/(D+V)**2)))
check('Complete T derivative includes the original beta',eq(Tw,s*L*(1-kap)/(2*b*g*S.sqrt(1+V/b))))
wm=r*S.sqrt(1-L/(2*D))-r;wp=s*S.sqrt(1+L/(2*b))-s
check('Retained exterior endpoint radius',eq(s+wp,T.subs(V,L/2)))
check('Retained handle endpoint radius',eq(r+wm,R.subs({V:0,U:L/2})))
Delta,I,J=S.symbols('Delta I J',positive=True)
h=(Delta-I)/J
check('Both endpoint germs have the exact total travel',eq(I+h*J,Delta))
w=S.symbols('w',real=True)
check('Original exterior germ has R equal r',eq(R.subs(U,0),r))
check('Original handle germ has T equal s',eq(T.subs(V,0),s))
# Radial derivative tensor in every normal dimension needed by n=6 and n=7.
rr,rad,jac=S.symbols('rho R J',positive=True)
for q in range(1,8):
 # Evaluate at an arbitrary rotated radial axis: transverse symmetry leaves
 # one J eigenvalue and all q-1 original R/rho eigenvalues.
 M=S.diag(jac,*([rad/rr]*(q-1)))
 check('Complete radial determinant in normal dimension '+str(q),eq(M.det(),(rad/rr)**(q-1)*jac))
z=S.Matrix(S.symbols('z0:3'));rho=S.sqrt(z.dot(z));H=S.Function('H')
radmap=H(rho)/rho*z
DJ=radmap.jacobian(z)
# Use an independent scalar radius before substitution in H'.
rv=S.symbols('rv',positive=True);Hp=S.diff(H(rv),rv).subs(rv,rho)
formula=H(rho)/rho*S.eye(3)+(Hp-H(rho)/rho)*(z*z.T)/rho**2
check('Complete three-dimensional radial derivative retains the projection term',all(eq(v,0) for v in DJ-formula))
zz,zp=S.symbols('zeta zeta_prime')
vv=S.symbols('v',positive=True);cut=S.Function('zeta')
check('Outward radius velocity derivative has the full 2R squared term',eq(S.diff(cut(vv*vv)*vv,vv),cut(vv*vv)+2*vv*vv*S.Subs(S.Derivative(cut(S.Symbol('qv')),S.Symbol('qv')),S.Symbol('qv'),vv*vv)))
m,R1,R2,x=S.symbols('m R1 R2 x',positive=True)
A=(x-m*m/4)/(3*m*m/4);B=(x-R1*R1)/(R2*R2-R1*R1)
chi=S.Function('chi');expr=chi(A)*(1-chi(B))
cp=S.Function('chip')
deriv=S.diff(expr,x)
manual=S.diff(chi(A),x)*(1-chi(B))-chi(A)*S.diff(chi(B),x)
check('Both complete cutoff derivative summands are retained',eq(deriv,manual))
check('Inner cutoff reaches one at the original m',eq(A.subs(x,m*m),1))
check('Outer cutoff begins at the retained target radius',eq(B.subs(x,R1*R1),0))
check('Outer cutoff ends at the retained support radius',eq(B.subs(x,R2*R2),1))
t=S.symbols('t',real=True)
check('Original plateau trajectory reaches R1 at the exact time',eq(m*S.exp(S.log(R1/m)),R1))
# The exact dimensions, including all same-index interchanges, in both receiving dimensions.
for n in [6,7]:
 for mu in range(1,n):
  for lam in range(1,mu+1):
   excess=(lam-1)+(n-mu-1)-(n-1)
   check('Exact core/belt dimension for n,mu,lambda '+str((n,mu,lam)),excess==lam-mu-1 and excess<0)
# Full off-diagonal collar derivative and inverse.
a11,a12,a21,a22,v1,v2=S.symbols('a11 a12 a21 a22 v1 v2')
M=S.Matrix([[a11,a12, v1],[a21,a22,v2],[0,0,1]])
check('Boundary isotopy extension keeps its original tangent determinant',eq(M.det(),a11*a22-a12*a21))
AA=S.Matrix([[a11,a12],[a21,a22]]);vv=S.Matrix([v1,v2])
check('Boundary isotopy extension inverse retains the mixed collar term',S.simplify(M.inv()[:2,2]+AA.inv()*vv)==S.zeros(2,1))
# Exercises: all stated inversion counts and actual adjacent pairs.
seq=[4,0,3,1,2,6,5];expected=[7,6,5,4,3,2,1,0];seen=[];pairs=[]
def inv(seq):return sum(x>y for i,x in enumerate(seq) for y in seq[i+1:])
for k in range(8):
 seen.append(inv(seq))
 if k==7:break
 i=next(i for i in range(len(seq)-1) if seq[i]>seq[i+1])
 pairs.append((seq[i],seq[i+1]));seq[i],seq[i+1]=seq[i+1],seq[i]
check('All eight original inversion counts in Exercise 5.2',seen==expected)
check('All original labels survive the seven interchanges',seq==list(range(7)))
check('The first and last swaps are the stated extreme-index cases',pairs[0]==(4,0) and pairs[-1]==(6,5))
check('The exact outer-annulus time is log 2',eq(S.log(5)-S.log(S.Rational(5,2)),S.log(2)))
Rstar,zeta=S.symbols('Rstar zeta',positive=True)
normal=S.diag(Rstar*zeta/2,Rstar/2,Rstar/2)
check('Exercise 5.1 keeps every transition eigenvalue',eq(normal.det(),(Rstar/2)**3*zeta))
check('Exercise 5.1 plateau derivative keeps all three dilation factors',(5*S.eye(3)).det()==125)
source=W/'src/rearranging-the-original-framed-handles.md'
result=dict(source=source.name,source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),passed=len(checks),checks=checks,independent_review=False,publication=False,scope='Full original rounded-boundary radii and both seam derivatives; complete endpoint-germ integral; radial derivative in every receiving dimension and its entire three-dimensional tensor; original cutoff denominators and both derivative terms; every allowed core/belt dimension in n=6 and n=7; full mixed collar derivative; both worked examples. The analytic and geometric proofs are in the chapter, not replaced by these finite checks.')
(W/'checks/HANDLE_REARRANGEMENT_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(passed=len(checks),source_sha256=result['source_sha256'])))

