"""Exact integral monodromy and all group-presentation comparisons. CC0-1.0."""
from pathlib import Path
from itertools import combinations
import hashlib,json
import sympy as S
from sympy.matrices.normalforms import smith_normal_form

checks=[]
def eq(name,a,b=0):
    if isinstance(a,S.MatrixBase):
        if not isinstance(b,S.MatrixBase):b=S.zeros(*a.shape)
        difference=(a-b).applyfunc(S.simplify)
        assert difference==S.zeros(*a.shape),(name,difference)
    else:
        difference=S.simplify(a-b)
        assert difference==0,(name,difference)
    checks.append(name)
def wedge(A,k):
    subsets=list(combinations(range(A.rows),k))
    return S.Matrix([[A.extract(i,j).det() for j in subsets] for i in subsets])

A1=S.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=S.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
T1=S.Matrix([[1,0,-6,2],[0,-1,1,1],[0,-1,0,1],[0,0,0,1]])
T2=S.Matrix([[1,6,0,-3],[0,0,-1,1],[0,1,0,0],[0,0,0,1]])
M0=S.Matrix([[1,0,0,0],[0,1,0,0],[0,1,1,0],[-1,0,0,1]])
T0=S.Matrix([[1,0,0,1],[0,1,-1,0],[0,0,1,0],[0,0,0,1]])
I=S.eye(4)
for j,A,T,m in [(1,A1,T1,3),(2,A2,T2,4)]:
    eq(f'dual evaluation {j}',T.T*A,I)
    eq(f'order {j}',A**m,I)
    eq(f'unimodularity {j}',A.det(),1)
    assert all(A**k!=I for k in range(1,m))
    checks.append(f'exact order {j}')
eq('whole cusp product',A1*A2*M0,I)
eq('whole dual product',T1*T2*T0,I)
eq('cusp inverse transpose',T0.T*M0,I)
eq('cusp square',(M0-I)**2)
eq('dual cusp square',(T0-I)**2)
eq('displayed T1 square',T1**2,S.Matrix([[1,6,-6,-2],[0,0,-1,1],[0,1,-1,0],[0,0,0,1]]))
eq('displayed T2 square',T2**2,S.Matrix([[1,6,-6,0],[0,-1,0,1],[0,0,-1,1],[0,0,0,1]]))
eq('displayed T2 cube',T2**3,S.Matrix([[1,0,-6,3],[0,0,1,0],[0,-1,0,1],[0,0,0,1]]))
a,b,c,d,e,f=S.symbols('a b c d e f')
eq('full cusp difference',(M0-I)*S.Matrix([a,b,c,d]),S.Matrix([0,0,b,-a]))
eq('degree-two cusp difference',(wedge(T0,2)-S.eye(6))*S.Matrix([a,b,c,d,e,f]),
   S.Matrix([-b-e+f,-f,0,0,-f,0]))
eq('degree-three cusp difference',(wedge(T0,3)-I)*S.Matrix([a,b,c,d]),S.Matrix([d,-c,0,0]))
eq('cusp invariant degree1 rank',4-(T0-I).rank(),2)
eq('cusp invariant degree2 rank',6-(wedge(T0,2)-S.eye(6)).rank(),4)
eq('cusp invariant degree3 rank',4-(wedge(T0,3)-I).rank(),2)
B2=S.Matrix([
[-2,1,1,-6,2,-8,-1,-1,1,-6,6,-3],
[-1,-1,1,-6,2,-6,1,-1,0,0,3,0],
[0,0,0,0,0,-6,0,0,0,0,6,0],
[0,0,0,0,0,1,0,0,0,0,-1,0],
[0,0,0,0,-2,1,0,0,0,0,-1,-1],
[0,0,0,0,-1,-1,0,0,0,0,1,-1]])
B3=S.Matrix([[0,0,1,2,0,-1,0,-3],
 [0,-2,1,-6,0,-1,-1,-6],[0,-1,-1,-6,0,1,-1,0],[0,0,0,0,0,0,0,0]])
eq('every degree2 relation column',B2,(wedge(T1,2)-S.eye(6)).row_join(wedge(T2,2)-S.eye(6)))
eq('every degree3 relation column',B3,(wedge(T1,3)-I).row_join(wedge(T2,3)-I))
common=[S.Matrix([1,0,0,0]),S.Matrix([0,0,6,1,0,0]),S.Matrix([1,0,0,0])]
for k,v in enumerate(common,1):
    D1=wedge(T1,k)-S.eye(len(v));D2=wedge(T2,k)-S.eye(len(v))
    eq(f'degree{k} common fixed vector',D1.col_join(D2)*v)
    eq(f'degree{k} common kernel rank',len(v)-D1.col_join(D2).rank(),1)
    relation=D1.row_join(D2)
    diag=smith_normal_form(relation,domain=S.ZZ)
    invariant=[abs(diag[i,i]) for i in range(min(diag.shape)) if diag[i,i]]
    assert invariant==[1]*(len(v)-1),(k,invariant)
    checks.append(f'degree{k} coinvariants have no torsion')
eq('degree2 quotient full primitive functional',S.Matrix([[0,0,1,6,0,0]])*B2,S.zeros(1,12))
eq('degree3 quotient full functional',S.Matrix([[0,0,0,1]])*B3,S.zeros(1,8))
v1=S.Matrix([1,2,-4,0]);v2=S.Matrix([-1,-3,3,0]);gamma=S.Matrix([[1,0,0,0]])
for j,A,v,sign in [(1,A1,v1,1),(2,A2,v2,-1)]:
    eq(f'full fixed translation {j}',A*v,v)
    eq(f'finite translation sign {j}',(gamma*v)[0],sign)
    eq(f'primitive invariant covector {j}',gamma*A,gamma)
    eq(f'affine power translation {j}',sum((A**k*v for k in range([3,4][j-1])),S.zeros(4,1)),
       [3,4][j-1]*v)
eq('forced normal-closure generator',A1[:,2]+I[:,2],I[:,1])
eq('cusp conjugation keeps exact positive sign',(I-M0)*I[:,0],I[:,3])
E=S.Matrix([[0,-1,-1,0],[1,-1,0,0],[0,0,1,0],[0,0,0,1]])
L=S.Matrix([[0,1,0,0],[-1,0,-1,0],[0,0,1,0],[0,0,0,1]])
CE=S.Matrix([[1,1,0,1],[0,1,0,0],[0,-1,1,0],[0,0,0,1]])
F=S.Matrix([[-1,1,-1,2],[-1,0,-1,1],[1,1,2,-1],[0,0,0,1]])
P=S.Matrix([[0,0,0,1],[1,-2,0,2],[1,1,1,-4],[-1,1,0,0]])
Pinv=S.Matrix([[2,-1,0,-2],[2,-1,0,-1],[0,2,1,3],[1,0,0,0]])
delta=S.Matrix([-2,-1,3,0]);psi=S.Matrix([[0,0,0,1]])
eq('source complete common basis',CE*L*CE.inv(),F)
eq('dictionary both inverse products',P*Pinv,I);eq('dictionary reverse inverse',Pinv*P,I)
eq('dictionary orientation determinant',P.det(),-1)
eq('first reversed meridian',A1*P,P*E.inv())
eq('second reversed meridian',A2*P,P*F.inv())
eq('actual ordered cusp comparison',M0*P,P*F*E)
eq('circle class with its sign',P*delta,I[:,3])
eq('quotient covector',gamma*P,psi)
NE=(E*F).inv()
eq('cusp conjugation after inverse orientation',F*E,E.inv()*NE.inv()*E)
eq('source full cusp image matrix',NE-I,S.Matrix([[1,1,1,0],[0,0,0,-1],[-1,-1,-1,1],[0,0,0,0]]))
eq('first primitive cusp comparison',P*E.inv()*(I[:,0]-I[:,2]),-I[:,2])
eq('second primitive cusp comparison',P*E.inv()*(I[:,2]-I[:,1]),I[:,3]-2*I[:,2])
f4=CE[:,3]
eq('first full finite vector in source marking',Pinv*v1,I[:,3])
eq('second full finite vector in source marking',Pinv*v2,-f4-delta)
eq('source signed sphere parameter',(12*psi*(-I[:,3]/3+(f4+delta)/4))[0],-1)
l0,l1,l2=S.symbols('l0 l1 l2',integer=True)
k=4*l0-l1-l2;p=12*l0-4*l1-3*l2
eq('terminal product relation',k+(l0-k),l0)
eq('terminal first power residual',3*k-l1,p)
eq('terminal second power residual',4*(l0-k)-l2,-p)
eq('original terminal parameter',p.subs({l0:0,l1:1,l2:-1}),-1)
eq('original terminal generator power',k.subs({l0:0,l1:1,l2:-1}),0)
for residue in [1,5]:
    n=S.symbols('n',integer=True);value=6*n+residue
    r1=1 if residue==1 else -1;r2=S.cancel((value-4*r1)/3)
    eq(f'full family parameter residue {residue}',4*r1+3*r2,value)
    assert all(coef.q==1 for coef in S.Poly(r2,n).all_coeffs())
    assert int(r2.subs(n,0))%2==1
    checks.append(f'free affine parity residue {residue}')
# Wedge pairing: retain the two cross terms and both original coefficients.
q=S.Matrix([0,0,6,1,0,0])
pairing=S.zeros(6)
for i,(a,b) in enumerate(combinations(range(4),2)):
    for j,(c,d) in enumerate(combinations(range(4),2)):
        order=[a,b,c,d]
        if len(set(order))==4:
            inversions=sum(order[k]>order[l] for k in range(4) for l in range(k+1,4))
            pairing[i,j]=(-1)**inversions
eq('full invariant self-intersection',(q.T*pairing*q)[0],12)
eq('full invariant coinvariant image',(S.Matrix([[0,0,1,6,0,0]])*q)[0],12)

root=Path(__file__).resolve().parents[1]
source=root/'src/integral-monodromy-and-fundamental-group.md'
report={'lesson':'CG-S6-06','checks':len(checks),'passed':len(checks),'check_names':checks,
 'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'scope':'Exact integral matrix, exterior-power and presentation checks. The based path, chart covering and gluing arguments are the written proofs.'}
(root/'checks/MONODROMY_GROUP_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'lesson':'CG-S6-06','checks':len(checks),'passed':True}))
