"""Check cap boundary coefficients and the retained integral covering pairings."""
from pathlib import Path
from collections import defaultdict
from itertools import combinations
import hashlib,json
import sympy as S
W=Path(__file__).resolve().parents[1]
checks=[]
def check(name,condition):
 assert condition,name
 checks.append(name)
def add(target,key,value):
 target[key]+=value
 if not target[key]:del target[key]
def boundary(face):
 return [(face[:i]+face[i+1:],(-1)**i) for i in range(len(face))] if len(face)>1 else []
for m in range(1,9):
 for r in range(m+1):
  sigma=tuple(range(m+1));diff=defaultdict(int)
  # Formal key (face evaluated by a, output chain face).
  aface=sigma[m-r:];front=sigma[:m-r+1]
  for face,sign in boundary(front):add(diff,(aface,face),sign)
  if m-1>=r:
   for face,sign in boundary(sigma):
    add(diff,(face[m-1-r:],face[:m-r]),-sign)
  if m>=r+1:
   tail=sigma[m-r-1:];front=sigma[:m-r]
   for aface,sign in boundary(tail):
    add(diff,(aface,front),-(-1)**(m-r)*sign)
  check(f'Entire simplex cap boundary identity m={m}, r={r}',not diff)
def wedge(a,b):
 out=defaultdict(int)
 for I,x in a.items():
  for J,y in b.items():
   if set(I)&set(J):continue
   sign=(-1)**sum(i>j for i in I for j in J)
   add(out,tuple(sorted(I+J)),S.expand(sign*x*y))
 return dict(out)
gamma={(0,):1}
eta=[{(1,):2,(2,):1,(3,):3},{(1,):1,(2,):1,(3,):2}]
b={(0,1,2):1}
cs=[{(1,2,3):1,(0,1,3):-4,(0,2,3):-2},{(1,2,3):1,(0,1,3):-3,(0,2,3):-3}]
vol=(0,1,2,3)
for j,m in enumerate([3,4]):
 D=S.Matrix([[wedge(v,w).get(vol,0) for w in [b,cs[j]]] for v in [gamma,eta[j]]])
 check(f'Original invariant pairing at order {m}',D==S.Matrix([[0,1],[-[3,2][j],0]]))
 P1=S.diag(m,1);P3=S.diag([1,2][j],1)
 upstairs=P1.T*D*P3
 check(f'Actual covering factor and full degree-three lattice at order {m}',upstairs==m*S.Matrix([[0,1],[-1,0]]))
 check(f'Integral downstairs unimodularity at order {m}',(upstairs/m).det()==1)
 check(f'Original degree-three image index at order {m}',P3.det()==[1,2][j])
 for a in [gamma,eta[j]]:
  for c in [b,cs[j]]:
   check(f'Ordered degree-one/three sign {m}:{len(checks)}',wedge(a,c)=={key:-value for key,value in wedge(c,a).items()})
 r,s=S.symbols('r s',integer=True)
 ev=S.diag(m,1)*D*S.Matrix([r,s])
 check(f'Full variable evaluation at order {m}',ev==S.Matrix([m*s,-[3,2][j]*r]))
 # Divisibility is proved symbolically in the text; samples are supplemental.
 check(f'All sampled integer rows obey the proved divisibility criterion {m}',all(all(int(x)%m==0 for x in (ev.subs({r:a,s:c})))==(j==0 or a%2==0) for a in range(-9,10) for c in range(-9,10)))
T=S.Matrix([[0,0,4,8],[-2,-4,0,-6]])
check('Exercise 5.2 complete ordered evaluation table',S.Matrix([[0,4],[-2,0]])*S.Matrix([[1,2,0,3],[0,0,1,2]])==T)
check('Exercise 5.2 necessary and sufficient descent columns',[all(int(x)%4==0 for x in T[:,i]) for i in range(4)]==[False,True,True,False])
check('Exercise 5.2 both actual downstairs columns',T[:,1:3]/4==S.Matrix([[0,1],[-1,0]]))
source=W/'src/integral-duality-and-the-specialization-lattices.md'
result=dict(source=source.name,source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),passed=len(checks),checks=checks,scope='Formal cap identity through simplex dimension eight; full exact original exterior pairings, degree factors and exercise columns. These finite checks do not replace the written general proofs.',independent_review=False)
(W/'checks/INTEGRAL_DUALITY_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(passed=len(checks),source_sha256=result['source_sha256'])))
