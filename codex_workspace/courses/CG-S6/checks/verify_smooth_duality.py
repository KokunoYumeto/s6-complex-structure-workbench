"""Exact finite tests of the written phase, adjoint and perturbation identities."""
from pathlib import Path
from itertools import combinations
import sympy as S
import hashlib,json
W=Path(__file__).resolve().parents[1];checks=[]
def check(name,condition):
 if not condition:raise AssertionError(name)
 checks.append(name)
def zero(m):return all(S.simplify(x)==0 for x in m)
def sign_join(I,J):return (-1)**sum(i>j for i in I for j in J)
def basis(n,q):return list(combinations(range(n),q)) if 0<=q<=n else []
def wedge(n,q,a):
 left=basis(n,q+1);right=basis(n,q);M=S.zeros(len(left),len(right))
 for j,I in enumerate(right):
  for k in range(n):
   if k in I:continue
   J=tuple(sorted((k,)+I));M[left.index(J),j]+=a[k]*sign_join((k,),I)
 return M
def smat(n,q):
 left=basis(n,n-q);right=basis(n,q);M=S.zeros(len(left),len(right));phase=(-1)**(n*(n-1)//2)*S.I**(-n)
 for j,I in enumerate(right):
  J=tuple(k for k in range(n) if k not in I);M[left.index(J),j]=phase*sign_join(I,J)
 return M
for n in range(1,7):
 phase=(-1)**(n*(n-1)//2)*S.I**(-n)
 check(f'Dimension{n}: exact volume phase',S.simplify(phase*(-1)**(n*(n-1)//2)*S.I**n)==1)
 a=S.Matrix([(k+1+S.I*(2*k+1))/S.sqrt(2) for k in range(n)])
 for q in range(n+1):
  Sq=smat(n,q)
  check(f'Dimension{n} degree{q}: antiunitary frame matrix',zero(Sq.conjugate().T*Sq-S.eye(Sq.cols)))
  if q>0:
   dstar=-S.I*wedge(n,q-1,a).conjugate().T
   # An antilinear map takes frequency xi to -xi; preserve that sign.
   lhs=-S.I*wedge(n,n-q,a)*Sq
   rhs=(-1)**q*smat(n,q-1)*dstar.conjugate()
   check(f'Dimension{n} degree{q}: dual differential sign with reversed frequency',zero(lhs-rhs))
  if q<n:
   lhs=S.I*wedge(n,n-q-1,a).conjugate().T*Sq
   rhs=(-1)**(q+1)*smat(n,q+1)*(S.I*wedge(n,q,a)).conjugate()
   check(f'Dimension{n} degree{q}: dual adjoint sign with reversed frequency',zero(lhs-rhs))
a,c,d,e,f=S.symbols('a c d e f')
diff=S.zeros(4);diff[3,1]=1
h=S.zeros(4);h[1,3]=1
i=S.Matrix([[1,0],[0,0],[0,1],[0,0]]);p=i.T
delta=S.zeros(4);delta[2:4,0:2]=a*S.Matrix([[c,d],[e,f]])
T=S.simplify((S.eye(4)+delta*h).inv()*delta)
D=S.simplify(p*T*i);ip=i-h*T*i;pp=p-p*T*h;hp=h-h*T*h
check('Original contraction identity retains harmonic projection',zero(diff*h+h*diff-S.eye(4)+i*p))
check('Full perturbed two-term differential squares to zero',zero((diff+delta)**2))
check('Both resolvent expressions preserve matrix order',zero(T-delta*(S.eye(4)+h*delta).inv()))
check('Exact central perturbation identity',zero(diff*T+T*diff+T*i*p*T))
check('Effective differential includes the full Schur denominator',S.simplify(D[1,0]-(a*c-a*a*d*e/(1+a*f)))==0)
check('Effective differential squares to zero',zero(D**2))
check('Perturbed inclusion is a chain map',zero((diff+delta)*ip-ip*D))
check('Perturbed projection is a chain map',zero(pp*(diff+delta)-D*pp))
check('Perturbed maps retain the exact retraction',zero(pp*ip-S.eye(2)))
check('Full perturbed homotopy identity',zero((diff+delta)*hp+hp*(diff+delta)-S.eye(4)+ip*pp))
check('Perturbed contraction retains its square-zero side condition',zero(hp**2))
check('Original-source right resolvent product equals delta, not identity',zero(T*(S.eye(4)+h*delta)-delta))
source=W/'src/smooth-duality-and-finite-twist-complexes.md'
out=dict(source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),passed=len(checks),checks=checks,limitations='Exact phase and symbol signs in dimensions1–6 and an arbitrary two-by-two perturbed differential. These checks supplement the full written functional-analytic proof; they do not certify estimates or replace independent review.')
(W/'checks/SMOOTH_DUALITY_CHECKS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':len(checks),'source_sha256':out['source_sha256']}))
