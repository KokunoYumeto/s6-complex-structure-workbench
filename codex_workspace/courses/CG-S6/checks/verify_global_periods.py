"""Exact algebra for lesson 4. The analytic arguments are in its source. CC0."""
from pathlib import Path
import hashlib,json
import sympy as S

checks=[]
def eq(name, actual, expected=0):
    residual=S.simplify(actual-expected)
    if residual != 0:
        raise AssertionError((name,residual))
    checks.append(name)

t,m,b=S.symbols('tau mu beta',nonzero=True)
def one(x):
    t,m,b=x
    return ((t-1)/t,(1-m)/t,b+2-6*(1-m)**2/t)
def two(x):
    t,m,b=x
    return (-1/t,1+m/t,b-3-6*m**2/t)
for name,F,order in [('order-three',one,3),('order-four',two,4)]:
    x=(t,m,b)
    for _ in range(order):x=tuple(S.cancel(v) for v in F(x))
    for label,a,e in zip(['tau','mu','beta'],x,(t,m,b)):
        eq(name+' '+label,a,e)
for label,a,e in zip(['tau','mu','beta'],one(two((t,m,b))),(t+1,m,b-1)):
    eq('inverse cusp '+label,a,e)
Pi=S.Matrix([[6*m,t,1,0],[b,m,0,1]])
As=[
    S.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]]),
    S.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])]
Rs=[S.Matrix([[-1/t,0],[(1-m)/t,1]]),S.Matrix([[1/t,0],[-m/t,1]])]
for j,(A,R,F) in enumerate(zip(As,Rs,[one,two]),1):
    transformed=Pi.subs(dict(zip((t,m,b),F((t,m,b)))),simultaneous=True)
    for k,e in enumerate(R*Pi-transformed*A):eq(f'covariance {j} entry {k}',e)
    eq(f'integral determinant {j}',A.det(),1)
tr,mr,br,T,U,V=S.symbols('tr mr br T U V',real=True)
real=S.Matrix([[6*mr,tr,1,0],[6*U,T,0,0],[br,mr,0,1],[V,U,0,0]])
eq('ordered real determinant',real.det(),T*V-6*U**2)
p,r,k=S.symbols('p r k',integer=True)
P=S.eye(2)+k*S.Matrix([[-p*r,p*p],[-r*r,p*r]])
S1=S.Matrix([[1,-1],[1,0]])
eq('parabolic determinant',P.det(),1)
eq('parabolic trace',(S1.inv()*P.inv()).trace(),1+k*(p*p-p*r+r*r))
eq('norm contraction exponent',2*S.pi*V-12*S.pi*U**2/T,2*S.pi*(V-6*U**2/T))
t=S.symbols('t')
A=-3*t**3*(t-1);B=2*t**4*(t-1)**2
c4=-48*A;c6=-864*B;disc=-16*(4*A**3+27*B**2)
eq('cubic discriminant',disc,1728*t**8*(t-1)**3)
eq('cubic j',c4**3/disc,1728*t)
eq('cubic c4',c4,144*t**3*(t-1))
eq('cubic c6',c6,-1728*t**4*(t-1)**2)
eq('explicit section',(S.sqrt(2)*t**2*(t-1))**2,B)
v=S.symbols('v',nonzero=True)
eq('infinite A',v**4*A.subs(t,1/v),-3*(1-v))
eq('infinite B',v**6*B.subs(t,1/v),2*(1-v)**2)
eq('infinite discriminant',v**12*disc.subs(t,1/v),1728*v*(1-v)**3)
X,U=S.symbols('X U')
w=(X**2-U**2*X)/(3+2*S.sqrt(2)*U)
Y=U*X+S.sqrt(2)*w
eq('rational parametrization',Y**2-X**3+3*w*X-2*w**2)
eq('parameter recovered',(Y-S.sqrt(2)*w)/X,U)
h=S.symbols('h')
eq('node equation',(h+1)**3-3*(h+1)+2,h**2*(h+3))
g2,g3=S.symbols('g2 g3',nonzero=True)
f2=-S.Rational(2,3)*t*(t-1)*g2/g3
relation={g2**3:27*t*g3**2/(t-1)}
eq('fourth scale',(f2**2*g2).subs(relation),12*t**3*(t-1))
eq('sixth scale',(f2**3*g3).subs(relation),-8*t**4*(t-1)**2)
E4,E6=S.symbols('E4 E6')
eq('modular discriminant constants',
   (4*S.pi**4*E4/3)**3-27*(8*S.pi**6*E6/27)**2,
   (2*S.pi)**12*(E4**3-E6**2)/1728)
root=Path(__file__).resolve().parents[1]
report={'lesson':'CG-S6-04','checks':len(checks),'passed':len(checks),'check_names':checks,
        'source_sha256':hashlib.sha256((root/'src/global-periods-and-line-bundle-quotients.md').read_bytes()).hexdigest(),
        'scope':'Exact algebra only; covering, gluing, convergence and quotient arguments require the written proofs.'}
(root/'checks/GLOBAL_PERIOD_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'lesson':'CG-S6-04','checks':len(checks),'passed':True}))
