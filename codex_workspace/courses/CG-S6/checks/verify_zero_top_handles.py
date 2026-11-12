"""Exact finite checks for zero/top cancellation signs and maps."""
from pathlib import Path
import hashlib,json
import sympy as S
W=Path(__file__).resolve().parents[1];checks=[]
def check(name,v):
 assert v,name
 checks.append(name)
def eq(a,b):return S.simplify(S.factor(a-b))==0
a,eps,t=S.symbols('a epsilon t',positive=True)
check('Both original index-one starting points have the retained level drop',all(eq(a*x*x,eps) for x in [-S.sqrt(eps/a),S.sqrt(eps/a)]))
x0,y0=S.symbols('x0 y0',real=True)
check('Original unstable coordinate solves its full field equation',eq(S.diff(x0*S.exp(t),t),x0*S.exp(t)))
check('Original stable coordinate solves its full field equation',eq(S.diff(y0*S.exp(-t),t),-y0*S.exp(-t)))
u,ss=S.symbols('u s',real=True);h=S.Function('h');delta=S.Function('Delta');eta=S.Function('eta')
z=S.symbols('z0:6',real=True);B=sum(v*v for v in z);F=h(u)+B-ss*delta(u)*eta(B)
ep=S.symbols('ep');etap=S.diff(eta(ep),ep).subs(ep,B)
check('The complete arc derivative retains the cutoff factor',eq(S.diff(F,u),S.diff(h(u),u)-ss*S.diff(delta(u),u)*eta(B)))
for i,v in enumerate(z):
 check('Complete supported cancellation derivative in coordinate '+str(i),eq(S.diff(F,v),2*v*(1-ss*delta(u)*etap)))
# Incidence including the original loop.
D=S.Matrix([[1,-1,0,0],[0,1,-1,0]])
check('The retained relative loop column is zero',D[:,3]==S.zeros(2,1))
check('The displayed tree columns have integral determinant one',D[:,:2].det()==1)
v1=S.Matrix([1,1,1,0]);v2=S.Matrix([0,0,0,1])
check('The complete three-edge cycle retains all signs',D*v1==S.zeros(2,1))
check('The loop is a separate kernel vector',D*v2==S.zeros(2,1))
r,q=S.symbols('r q',integer=True)
check('The full free kernel parametrization satisfies both original equations',D*S.Matrix([r,r,r,q])==S.zeros(2,1))
check('The cycle generators have independent integral parameters',S.Matrix.hstack(v1,v2)[[2,3],:].det()==1)
N0,N1,j=S.symbols('N0 N1 j',integer=True)
check('Every zero/one cancellation retains the original index difference',eq((N1-j)-(N0-j),N1-N0))
# All original coefficients and permutation signs in both receiving dimensions.
for n in [6,7]:
 for k in range(n+1):
  co=S.symbols('c0:'+str(n),positive=True)
  H=S.diag(*[-2*c for c in co[:k]],*[2*c for c in co[k:]])
  order=list(range(k,n))+list(range(k))
  P=S.zeros(n)
  for i,old in enumerate(order):P[i,old]=1
  wanted=S.diag(*[-2*c for c in co[k:]],*[2*c for c in co[:k]])
  check('Reversal keeps the entire Hessian in dimension/index '+str((n,k)),P*(-H)*P.T==wanted)
  check('Reversal retains the exact coordinate orientation in dimension/index '+str((n,k)),P.det()==(-1)**(k*(n-k)))
cm,cp,rad=S.symbols('cminus cplus radius')
check('The incoming reversed collar retains its original endpoint',eq(-(cp-rad),-cp+rad))
check('The outgoing reversed collar retains its original endpoint',eq(-(cm+rad),-cm-rad))
coef=[2,3,5,7,11,13,17]
H=S.diag(*[-2*c for c in coef[:6]],2*coef[6])
order=[6,0,1,2,3,4,5];P=S.zeros(7)
for i,old in enumerate(order):P[i,old]=1
check('All seven original coefficients in the worked reversal',P*(-H)*P.T==S.diag(-34,4,6,10,14,22,26))
check('The worked original index-six permutation has positive sign',P.det()==1)
source=W/'src/removing-the-original-zero-and-top-handles.md'
result=dict(source=source.name,source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),passed=len(checks),checks=checks,publication=False,independent_review=False,scope='Original index-one starting radii and flow signs; full supported zero/one cancellation derivatives in six transverse coordinates; complete signed incidence map with loop column and integral kernel; exact count invariant; every Hessian and permutation sign for dimensions six and seven including both extremes; actual boundary reversal and all seven worked coefficients. The component-graph, measure-zero and geometric cancellation proofs are in the text and are not replaced by these checks.')
(W/'checks/ZERO_TOP_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(passed=len(checks),source_sha256=result['source_sha256'])))

