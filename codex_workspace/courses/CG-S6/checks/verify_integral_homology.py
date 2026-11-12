"""Exact integral checks for the developing seventh CG-S6 lesson. CC0-1.0."""
from pathlib import Path
from itertools import combinations
import hashlib,json
import sympy as S
from sympy.matrices.normalforms import smith_normal_form,hermite_normal_form
checks=[]
def eq(name,a,b=0):
 if isinstance(a,S.MatrixBase):
  if not isinstance(b,S.MatrixBase):b=S.zeros(*a.shape)
  assert (a-b).applyfunc(S.simplify)==S.zeros(*a.shape),(name,a,b)
 else:assert S.simplify(a-b)==0,(name,a,b)
 checks.append(name)
def wedge(A,k):
 subs=list(combinations(range(A.rows),k))
 return S.Matrix([[A.extract(i,j).det() for j in subs] for i in subs])
def cup(a,k,b,l):
 out={s:0 for s in combinations(range(4),k+l)}
 for i,x in zip(combinations(range(4),k),a):
  for j,y in zip(combinations(range(4),l),b):
   if set(i)&set(j):continue
   sign=(-1)**sum(p>q for p in i for q in j)
   out[tuple(sorted(i+j))]+=sign*x*y
 return S.Matrix(list(out.values()))
def lattice(name,A,B):
 eq(name,hermite_normal_form(A),hermite_normal_form(B))
A=[S.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]]),
 S.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])]
T=[a.inv().T for a in A];T0=(T[0]*T[1]).inv()
g,u,w,d=[S.eye(4)[:,i] for i in range(4)]
eta=[2*u+w+3*d,u+w+2*d]
v=[S.Matrix([1,2,-4,0]),S.Matrix([-1,-3,3,0])]
q=S.Matrix([0,0,6,1,0,0]);b=S.Matrix([1,0,0,0])
c=[S.Matrix([0,-4,-2,1]),S.Matrix([0,-3,-3,1])]
for j,m in enumerate([3,4]):
 Q=S.Matrix([[1,0,0,0],[0,2,1,3] if j==0 else [0,1,1,2]])
 eq(f'finite coinvariant map {j+1}',Q*(A[j]-S.eye(4)))
 eq(f'full translation quotient {j+1}',Q*v[j],S.Matrix([1 if j==0 else -1,0]))
 eq(f'invariant eta {j+1}',T[j]*eta[j],eta[j])
 eq(f'eta twist {j+1}',(eta[j].T*v[j])[0])
 I2=cup(g,1,eta[j],1).row_join(q)
 eq(f'complete invariant2 vectors {j+1}',(wedge(T[j],2)-S.eye(6))*I2)
 eq(f'invariant2 rank {j+1}',6-(wedge(T[j],2)-S.eye(6)).rank(),2)
 a1,a2,a3,a4,a5,a6=S.symbols('a1:7')
 param=I2*S.Matrix([a2 if j==0 else a1,a4])
 sol=S.Matrix([2*a2,a2,3*a2+6*a4,a4,0,0]) if j==0 else S.Matrix([a1,a1,2*a1+6*a4,a4,0,0])
 eq(f'invariant2 integral solution {j+1}',param,sol)
 gram=S.Matrix([[cup(I2[:,i],2,I2[:,k],2)[0] for k in range(2)] for i in range(2)])
 eq(f'intersection matrix {j+1}',gram,S.Matrix([[0,3 if j==0 else 2],[3 if j==0 else 2,12]]))
 eq(f'finite middle index {j+1}',abs(gram.det())*([1,2][j]**2),m*m)
 I3=b.row_join(c[j])
 eq(f'complete invariant3 vectors {j+1}',(wedge(T[j],3)-S.eye(4))*I3)
 eq(f'invariant3 rank {j+1}',4-(wedge(T[j],3)-S.eye(4)).rank(),2)
 one=g.row_join(eta[j])
 pair=S.Matrix([[cup(one[:,i],1,I3[:,k],3)[0] for k in range(2)] for i in range(2)])
 eq(f'one-three matrix {j+1}',pair,S.Matrix([[0,1],[-3 if j==0 else -2,0]]))
 eq(f'finite degree3 index {j+1}',abs(pair.det())*m*[1,2][j],m*m)
 N=sum((T[j]**i for i in range(m)),S.zeros(4))
 lattice(f'full cyclic norm image {j+1}',N,S.Matrix.hstack(m*g,[1,2][j]*eta[j]))
N=sum((T[1]**i for i in range(4)),S.zeros(4))
assert hermite_normal_form(N)!=hermite_normal_form(N.row_join(eta[1]))
checks.append('eta2 is not a cyclic norm')
I2=cup(g,1,eta[1],1).row_join(q)
a=S.symbols('a',integer=True)
pull=I2*S.Matrix([[2,a],[0,1]])
form=S.Matrix([[cup(pull[:,i],2,pull[:,j],2)[0]/4 for j in range(2)] for i in range(2)])
eq('parity of actual order4 sublattice',form,S.Matrix([[0,1],[1,a+3]]))
eq('degree3 missing coset',cup(eta[1],1,b,3)[0],-2)
DP=S.Matrix([[1,-1,0],[1,0,-1],[0,1,-1]])
DQ=S.Matrix([[0,-1,1],[1,-1,0],[1,0,-1]])
ss=S.Matrix([[1,-1,1]])
for name,D in [('P',DP),('Q',DQ)]:
 eq('triple boundary square '+name,ss*D)
 eq('triple differences rank '+name,D.rank(),2)
 eq('diagonal kernel '+name,D*S.ones(3,1))
 diag=smith_normal_form(D,domain=S.ZZ)
 eq('primitive triple invariant factors '+name,diag.applyfunc(abs),S.diag(1,1,0))
globalD=S.Matrix([[1,-1,1],[1,-1,1]])
eq('global endpoint difference rank',globalD.rank(),1)
diag=smith_normal_form(globalD,domain=S.ZZ)
eq('global endpoint primitive image',diag,S.Matrix([[1,0,0],[0,0,0]]))
intersection=S.Matrix([[0,1,0,0],[1,-1,-1,0],[0,0,1,0],[1,0,-1,-1],[0,0,0,1],[1,-1,0,-1]])
diff=intersection[:3,:]-intersection[3:,:]
eq('every opposite-curve intersection difference',diff,S.Matrix([[-1,1,1,1],[1,-1,-1,-1],[-1,1,1,1]]))
eq('primitive normalization degree2 image',hermite_normal_form(diff),S.Matrix([1,-1,1]))
eq('cusp Euler characteristic',1-2+4-2+1,2)
for k,rank in enumerate([1,2,4,2,1]):
 size=len(list(combinations(range(4),k)))
 eq(f'cusp invariant rank{k}',size-(wedge(T0,k)-S.eye(size)).rank(),rank)
image1=S.Matrix.hstack(2*g+u+w,2*g-u)
lattice('parabolic V full image',T[0]-S.eye(4),image1)
lattice('parabolic cusp V full image',T0-S.eye(4),S.Matrix.hstack(g,u))
eq('parabolic V denominator',(T[0]-S.eye(4))*eta[1],-2*g+u)
gu,gw,gd,uw,ud,wd=[S.eye(6)[:,i] for i in range(6)]
lattice('parabolic exterior2 full image',wedge(T[0],2)-S.eye(6),S.Matrix.hstack(gu,gw,2*ud+wd,uw+ud-wd-6*gd))
lattice('parabolic cusp exterior2 full image',wedge(T0,2)-S.eye(6),S.Matrix.hstack(gu,gw+ud))
eq('parabolic exterior2 denominator',(wedge(T[0],2)-S.eye(6))*cup(g,1,eta[1],1),gu)
eq('global invariant product',cup(12*g,1,2*q,2),12*2*b)
eq('original q coefficient quotient',(S.Matrix([[0,0,1,6,0,0]])*q)[0],12)
eq('delta degree3 product sign',cup(d,1,2*b,3)[0],-2)
eq('q gamma-delta product sign',cup(2*q,2,gd,2)[0],2)
eq('full finite discrepancy',12*(g.T*v[0])[0]/3+12*(g.T*v[1])[0]/4,1)
r,s=S.symbols('r s')
assert S.solve([s-(2-r),-2*r+2*s],[r,s])=={r:1,s:1}
checks.append('both higher integral transgressions')
P=S.Matrix([[0,0,0,1],[1,-2,0,2],[1,1,1,-4],[-1,1,0,0]])
xi=S.Matrix([3,1,0,-2,0,-2]);psi=S.Matrix([0,0,0,1])
k=S.Matrix([1,-1,0,0]);nu=S.Matrix([1])
eq('source marking gamma',P.T*g,psi)
eq('source marking delta',P.T*d,-k)
eq('source marking complete q',wedge(P.T,2)*q,xi)
eq('source marking gamma delta',wedge(P.T,2)*gd,cup(k,1,psi,1))
eq('source marking complete degree3',wedge(P.T,3)*b,cup(xi,2,psi,1))
eq('source marking volume orientation',wedge(P.T,4)*S.Matrix([1]),-nu)
eq('source first transgression orientation',12*(psi.T*(-P.inv()*v[0]/3-P.inv()*v[1]/4))[0],-1)
eq('source middle transgression orientation',-P.T*d,k)
eq('source third transgression orientation',-wedge(P.T,2)*gd,-cup(k,1,psi,1))
eq('exercise exact order4 pulled-back pairing',S.Matrix([[2,0],[1,1]])*S.Matrix([[0,2],[2,12]])*S.Matrix([[2,1],[0,1]])/4,S.Matrix([[0,1],[1,4]]))
eq('normalization degree0 integral kernel',globalD*S.Matrix([[1,-1],[1,0],[0,1]]))
eq('normalization degree2 quotient kernel',S.Matrix([[1,1,0],[0,1,1]])*S.Matrix([1,-1,1]))
rp,sp=S.symbols('rp sp')
assert S.solve([sp+2+rp,-2*rp+2*sp],[rp,sp])=={rp:-1,sp:-1}
checks.append('all orientation-reversed transgression coefficients')
eq('actual connected-sum Euler counterexample',1+1-2+1+1,2)
W=Path(__file__).resolve().parents[1];source=W/'src/integral-homology-and-sphere-recognition.md'
out=dict(source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),passed=len(checks),checks=checks,
 limitations='Finite algebra checks supplement the written integral proof; they do not independently certify the topology or the smooth-recognition argument.')
(W/'checks/INTEGRAL_HOMOLOGY_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':len(checks),'source_sha256':out['source_sha256']}))
