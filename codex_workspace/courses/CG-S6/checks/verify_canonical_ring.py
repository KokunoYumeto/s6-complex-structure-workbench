"""Exact character, divisor, graded-basis and pencil checks for CG-S6-08. CC0-1.0."""
from pathlib import Path
import hashlib,json
import sympy as S

checks=[]
def eq(name,a,b=0):
    if isinstance(a,S.MatrixBase):
        assert (a-b).applyfunc(S.simplify)==S.zeros(*a.shape),(name,a,b)
    else:
        assert S.simplify(a-b)==0,(name,a,b)
    checks.append(name)

tau=S.symbols('tau',nonzero=True)
eq('original first determinant',(tau-1)/tau-1,-1/tau)
eq('original second determinant',-(-1/tau),1/tau)
rho=(1+S.sqrt(3)*S.I)/2
eq('order-three fixed determinant',-1/rho,rho-1)
eq('order-four fixed determinant',1/S.I,-S.I)
for m,a in [(3,2),(4,1)]:
    k=m-1-a
    assert 0<=k<m
    assert [(n+1+a)%m==0 for n in range(5*m)]==[n%m==k for n in range(5*m)]
    checks.append(f'full five-block canonical character powers m{m}')
    eq(f'ramification exponent m{m}',k-(m-1),-a)
eq('finite divisor coefficient first',3-1-2,0)
eq('finite divisor coefficient second',4-1-1,2)
# Coefficient vectors in the original divisor basis (p0,p1,p2).
p0=S.Matrix([1,0,0]);p2=S.Matrix([0,0,1])
eq('specified rational-function divisor',p0-2*p2-(p0-p2),-p2)
eq('canonical coefficient at actual multiple fibre',-4+2,-2)
eq('inverse canonical square is full fibre',-2*(-2),4)
t,w=S.symbols('t w',nonzero=True)
eq('original h at infinity',1/(1/w-1),w/(1-w))
eq('original base differential at infinity',(-1/w**2)/(1/w-1)**2,-1/(1-w)**2)
floor_table=[-3,-2,-2,-2,-2,-1,-1,-1,-1,0,0,0,0,1,1,1,1,2,2]
assert [k//4 for k in range(-9,10)]==floor_table
checks.append('all negative and positive exercise floor values')
for k in range(-41,42):
    bound=-(k//4)
    assert 4*bound+k>=0 and 4*(bound-1)+k<0
checks.append('exact integer order-bound endpoints in both signs')
A,B,x=S.symbols('A B x',nonzero=True)
for r in range(9):
    basis=S.Matrix([[S.expand((A*x+B)**j).coeff(x,i) for j in range(r+1)] for i in range(r+1)])
    eq(f'full graded basis determinant r{r}',basis.det(),A**(r*(r+1)//2))
for m in range(25):
    basis=[(m-2*j,j) for j in range(m//2+1)]
    assert all(a+2*b==m and a>=0 for a,b in basis)
    assert len(basis)==m//2+1
checks.append('all graded monomial weights through degree24')
z=S.symbols('z')
series=S.series(1/((1-z)*(1-z**2)),z,0,25).removeO()
assert [series.coeff(z,m) for m in range(25)]==[m//2+1 for m in range(25)]
checks.append('Hilbert series versus exact degree counts through24')
M=S.Matrix([[1,-1],[B,A-B]])
Minv=S.Matrix([[A-B,1],[-B,1]])
eq('coordinate matrix determinant',M.det(),A)
eq('coordinate inverse left with scalar',Minv*M,A*S.eye(2))
eq('coordinate inverse right with scalar',M*Minv,A*S.eye(2))
c,a,b,U,V=S.symbols('c a b U V',nonzero=True)
forward={U:c*U,V:a*V+b*U**2}
inverse={U:U/c,V:V/a-b*U**2/(a*c**2)}
for label,first,second in [('left',forward,inverse),('right',inverse,forward)]:
    for variable in [U,V]:
        eq(f'graded automorphism {label} {variable}',first[variable].subs(second,simultaneous=True),variable)
lam,mu=S.symbols('lambda mu')
tstar=1-mu*A/(lam+mu*B)
eq('exact degree-two member zero',((lam+mu*B)*(t-1)+mu*A).subs(t,tstar),0)
eq('cusp member after full coefficient cancellation',(lam+mu*B+mu*A/(t-1)).subs(lam,-mu*B),mu*A/(t-1))
eq('order-three member condition',(lam+mu*B)*(0-1)+mu*A,mu*A-lam-mu*B)

root=Path(__file__).resolve().parents[1]
source=root/'src/canonical-divisor-and-intrinsic-fibration.md'
out=dict(source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),passed=len(checks),checks=checks,
    limitations='Exact checks of the written character, divisor and algebra formulas; author self-check, not independent proof certification.')
(root/'checks/CANONICAL_RING_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':len(checks),'source_sha256':out['source_sha256']}))
