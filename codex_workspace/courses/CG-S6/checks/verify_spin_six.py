from pathlib import Path
from datetime import datetime, timezone
import sympy as S
import hashlib,json
W=Path(__file__).resolve().parents[1];checks=[]
def check(label,value):
    assert value,label
    checks.append(label)
def zero(M):return all(S.simplify(v)==0 for v in M)
pairs=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
def exterior_derivative(A):
    M=S.zeros(6)
    for col,(i,j) in enumerate(pairs):
        for a in range(4):
            if a!=j:
                pair=tuple(sorted((a,j)));M[pairs.index(pair),col]+=A[a,i]*(1 if a<j else -1)
            if a!=i:
                pair=tuple(sorted((i,a)));M[pairs.index(pair),col]+=A[a,j]*(1 if i<a else -1)
    return M
T=S.zeros(6)
for a,b,sign in [(0,5,1),(1,4,-1),(2,3,1)]:T[a,b]=sign;T[b,a]=sign
columns=[]
for a,b,sign in [(0,5,1),(1,4,-1),(2,3,1)]:
    va=S.eye(6)[:,a];vb=sign*S.eye(6)[:,b]
    columns.extend([(va+vb)/S.sqrt(2),S.I*(va-vb)/S.sqrt(2)])
B=S.Matrix.hstack(*columns)
check('Original antilinear star squares to identity',T*T.conjugate()==S.eye(6))
check('All six displayed vectors are fixed by the antilinear star',zero(T*B.conjugate()-B))
check('The retained square-root-two basis is orthonormal',zero(B.conjugate().T*B-S.eye(6)))
gens=[]
for j in range(3):
    A=S.zeros(4);A[j,j]=S.I;A[3,3]=-S.I;gens.append(A)
for i in range(4):
    for j in range(i+1,4):
        A=S.zeros(4);A[i,j]=1;A[j,i]=-1;gens.append(A)
        A=S.zeros(4);A[i,j]=S.I;A[j,i]=S.I;gens.append(A)
real_actions=[]
for k,A in enumerate(gens):
    M=exterior_derivative(A);N=S.simplify(B.conjugate().T*M*B)
    check(f'Lie generator{k+1}: exterior square commutes with full star',zero(M*T-T*M.conjugate()))
    check(f'Lie generator{k+1}: real action is real and skew-symmetric',zero(N-N.conjugate()) and zero(N+N.T))
    real_actions.append(N)
check('The fifteen actual real actions are independent',S.Matrix.hstack(*[x.reshape(36,1) for x in real_actions]).rank()==15)
for central in [1,-1,S.I,-S.I]:
    check(f'Central scalar{central}: full exterior-square value retained',central**2==(1 if central in [1,-1] else -1))
x1,x2,x3,x4=S.symbols('x1 x2 x3 x4');xs=[x1,x2,x3,x4]
c1=sum(xs);c3=sum(xs[i]*xs[j]*xs[k] for i in range(4) for j in range(i+1,4) for k in range(j+1,4))
full=(x1+x2)*(x1+x3)*(x1+x4)
check('Entire Euler polynomial retains x1-squared times the determinant class',S.expand(full-c3-x1*x1*c1)==0)
check('Specified determinant equation gives positive c3',S.expand((full-c3).subs(x4,-x1-x2-x3))==0)
check('Without determinant trivialization the extra term is nonzero',S.expand(full-c3)!=0)
c,ss=S.symbols('c s',real=True)
for k in range(3):
    a,b,sign=[(0,5,1),(1,4,-1),(2,3,1)][k]
    diag=S.eye(6);diag[a,a]=c+S.I*ss;diag[b,b]=c-S.I*ss
    block=S.simplify((B.conjugate().T*diag*B)[2*k:2*k+2,2*k:2*k+2])
    check(f'Weight plane{k+1}: its positive real rotation retains all signs',block==S.Matrix([[c,-ss],[ss,c]]))
check('Both tangent zero derivatives have positive orientation in dimension six',(-S.eye(6)).det()==1 and S.eye(6).det()==1)
p=S.Matrix(S.symbols('p0:7',real=True));v=S.Matrix(S.symbols('v0:7',real=True));a=S.symbols('a',real=True)
norm=(p.T*p)[0];pv=(p.T*v)[0];w=v+a*p;aa=(p.T*w)[0];vv=w-aa*p
check('Stable inverse scalar keeps both sphere and tangency defects',S.expand(aa-a-pv-a*(norm-1))==0)
check('Stable inverse tangent component keeps both defects',zero(vv-v+p*pv-a*p*(1-norm)))
P=S.eye(7)-p*p.T
check('Tangent projection plus the original normal term is identity',zero(P+p*p.T-S.eye(7)))
c2=sum(xs[i]*xs[j] for i in range(4) for j in range(i+1,4))
weights=[xs[i]+xs[j] for i,j in pairs]
check('Full exterior-square degree-one character',S.expand(sum(weights)-3*c1)==0)
check('Full exterior-square degree-two character',S.expand(sum(x*x for x in weights)/2-S.Rational(3,2)*c1*c1+2*c2)==0)
check('Full exterior-square degree-three character',S.expand(sum(x**3 for x in weights)/6-c1*(c1*c1-2*c2)/2)==0)
check('Nontrivial determinant example keeps the missing ten',full.subs(dict(zip(xs,[1,2,3,4])))==60 and c3.subs(dict(zip(xs,[1,2,3,4])))==50)
re=S.Matrix(S.symbols('r0:6',real=True));im=S.Matrix(S.symbols('s0:6',real=True));xi=re+S.I*im
first=(xi+T*xi.conjugate())/2;second=(xi-T*xi.conjugate())/(2*S.I)
check('Complexification inverse has two actual star-fixed factors',zero(T*first.conjugate()-first) and zero(T*second.conjugate()-second))
check('Complexification inverse retains both halves and the i factor',zero(first+S.I*second-xi))
source=W/'src/spin-six-and-the-framing-comparison.md'
out=dict(source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),passed=len(checks),checks=checks,limitations='These exact exterior-representation, Chern/Euler-polynomial and inverse-map computations supplement the written family-index and homotopy arguments. They are not a verification of those infinite-dimensional or topological proofs, and are not independent review.')
(W/'checks/SPIN_SIX_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':len(checks),'source_sha256':out['source_sha256']}))
