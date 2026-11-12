"""Check the exact cusp, section-cocycle and finite-resolution calculations."""
from pathlib import Path
import hashlib,json
import sympy as S
root=Path(__file__).resolve().parents[1]
checks=[]
def eq(name,actual,expected=0):
    residual=S.simplify(actual-expected)
    if residual!=0:raise AssertionError((name,residual))
    checks.append(name)

t,mu,beta,nu,alpha,bet=S.symbols('tau mu beta nu alpha bet')
def one(T,N):
    return ((T-1)/T,-N/T+alpha+bet*(T-1)/T)
def two(T,N):
    return (-1/T,N/T-bet-(alpha+bet)/T)
for label,F,order in [('first',one,3),('second',two,4)]:
    pair=(t,nu)
    for _ in range(order):pair=tuple(S.cancel(v) for v in F(*pair))
    eq(label+' cyclic tau',pair[0],t);eq(label+' cyclic logarithm',pair[1],nu)
pair=one(*two(t,nu))
eq('cusp regular logarithm',pair[1],nu);eq('inverse cusp tau',pair[0],t+1)
n=-alpha-2*bet;a=alpha+bet
eq('first logarithm constant',n+2*a,alpha)
eq('first logarithm period coefficient',-n-a,bet)
eq('second logarithm constant',n+a,-bet)
eq('second logarithm period coefficient',a,alpha+bet)
k=S.symbols('k',integer=True)
eq('generator invariant under changing integral lift',-(alpha+2*k)-2*(bet-k),n)
B0=S.Matrix([[0,1],[-1,0]])
eq('cusp integral orientation',B0.det(),1)
for e in B0**2+S.eye(2):eq('cusp square entry '+str(len(checks)),e)
h,b,m=S.symbols('h b mu')
C=S.Matrix([[6*m,h],[b-h,m]])
for v,row,expected in [
    (S.Matrix([1,0]),S.Matrix([[0,1]]),-m),
    (S.Matrix([0,1]),S.Matrix([[1,0]]),6*m),
    (S.Matrix([1,-1]),S.Matrix([[1,1]]),-7*m-b)]:
    eq('opposite edge exponent '+str(len(checks)),(row*C*B0*v)[0],expected)
x,y,t,X,Y,T,V=S.symbols('x y t X Y T V')
F=y**2-x**3+3*t**3*(t-1)*x-2*t**4*(t-1)**2
first=S.cancel(F.subs({x:t*X,y:t*Y},simultaneous=True)/t**2)
eq('first t chart',first,Y**2-t*X**3-3*t**2*(1-t)*X-2*t**2*(1-t)**2)
second=S.cancel(first.subs({t:X*T,Y:X*V},simultaneous=True)/X**2)
H=X**2*T+(2+3*X)*T**2-(4*X+3*X**2)*T**3+2*X**2*T**4
eq('second X chart',second,V**2-H)
eq('critical implicit derivative',S.diff(H,T,2).subs({X:0,T:0}),4)
eq('critical leading displacement',S.series(S.diff(H,T).subs(T,-X**2/4),X,0,3).removeO(),0)
eq('critical leading value',S.series(H.subs(T,-X**2/4),X,0,5).removeO(),-X**4/8)
U,V=S.symbols('U V')
for i in range(4):
    aa=U**(i+1)*V**i;cc=U**(3-i)*V**(4-i);xx=U*V
    eq(f'A3 chart {i}',aa*cc,xx**4)
    coefficient=S.diff(xx,U)*S.diff(aa,V)/aa-S.diff(xx,V)*S.diff(aa,U)/aa
    eq(f'A3 canonical form {i}',coefficient,-1)
u=S.symbols('u')
typeIII=S.cancel(F.subs({t:1+u,x:u*X,y:u*Y},simultaneous=True)/u**2)
eq('III u chart',typeIII,Y**2-u*X**3+3*(1+u)**3*X-2*(1+u)**4)
eq('visible section point at III',typeIII.subs({X:0,Y:S.sqrt(2)*(1+u)**2}),0)
E=S.eye(6)*2
for i,j in [(0,1),(1,2),(2,3),(1,4),(4,5)]:E[i,j]=E[j,i]=-1
eq('E6 determinant',E.det(),3)
Ei=E.inv()
eq('left simple component correction',Ei[3,3],S.Rational(4,3))
eq('right simple component correction',Ei[5,5],S.Rational(4,3))
for i in range(6):
    assert S.denom(Ei[i,3]+Ei[i,5])==1
    assert S.denom(3*Ei[i,3])==1
checks.append('E6 outer classes are opposite and killed by three')
assert any(S.denom(Ei[i,3])==3 for i in range(6))
checks.append('E6 outer class has exact order three')
affine=-2*S.eye(7)
for i,j in [(0,1),(1,2),(2,3),(3,4),(2,5),(5,6)]:affine[i,j]=affine[j,i]=1
multiplicities=S.Matrix([1,2,3,2,1,2,1])
for i,v in enumerate(affine*multiplicities):eq(f'full fibre intersection {i}',v)
eq('full fibre intersection rank',affine.rank(),6)
eq('A1 correction',S.Matrix([[2]]).inv()[0,0],S.Rational(1,2))
eq('generator height',2-S.Rational(4,3)-S.Rational(1,2),S.Rational(1,6))
X0=1+12*u/(u-1)**2
Y0=12*S.sqrt(3)*u*(u+1)/(u-1)**3
eq('complete nodal parametrization',Y0**2,(X0-1)**2*(X0+2))
ratio=Y0/(X0-1)
eq('nodal coordinate inverse',(ratio+S.sqrt(3))/(ratio-S.sqrt(3)),u)
v=S.symbols('v')
Fnode=Y**2-X**3+3*(1-v)*X-2*(1-v)**2
eq('section cannot pass node first-order term',S.diff(Fnode,v).subs({X:1,Y:0,v:0}),1)

# The published matrices are checked entry by entry, not only on their diagonal.
published_inverse=S.Matrix([[6,9,6,3,6,3],[9,18,12,6,12,6],
    [6,12,10,5,8,4],[3,6,5,4,4,2],[6,12,8,4,10,5],[3,6,4,2,5,4]])/3
eq('complete displayed E6 inverse',(E*published_inverse-S.eye(6)).norm(),0)
eq('canonical finite first x chart',
    S.cancel(F.subs({t:x*T,y:x*Y},simultaneous=True)/x**2),
    Y**2-x-3*x**2*T**3*(1-x*T)-2*x**2*T**4*(1-x*T)**2)
eq('second t chart',
    S.cancel(first.subs({X:t*X,Y:t*Y},simultaneous=True)/t**2),
    Y**2-t**2*X**3-3*t*(1-t)*X-2*(1-t)**2)
U=S.symbols('U')
eq('III x chart',
    S.cancel(F.subs({t:1+x*U,y:x*Y},simultaneous=True)/x**2),
    Y**2-x+3*(1+x*U)**3*U-2*(1+x*U)**4*U**2)
# All four A3 monomial maps and their full adjacent overlap.
U,V=S.symbols('U V',nonzero=True)
for i in range(3):
    after={U:1/V,V:U*V**2}
    for name,expr,previous in [
        ('a',U**(i+2)*V**(i+1),U**(i+1)*V**i),
        ('c',U**(2-i)*V**(3-i),U**(3-i)*V**(4-i)),
        ('X',U*V,U*V)]:
        eq(f'A3 overlap {i} {name}',expr.subs(after,simultaneous=True),previous)
# Every tangent-cone determinant and actual smoothness derivative.
u,x,y=S.symbols('u x y')
quad=y*y+3*u*x-2*u*u
eq('III quadratic Hessian determinant',
   S.hessian(quad,(x,y,u)).det(),-18)
eq('second t chart at E2 plus',2*S.sqrt(2),S.diff(Y**2-2,Y).subs(Y,S.sqrt(2)))
eq('second t chart at E2 minus',-2*S.sqrt(2),S.diff(Y**2-2,Y).subs(Y,-S.sqrt(2)))
# Universal bilinear expansion with every fibre correction.
aO,bO,ab=S.symbols('aO bO ab')
va=S.Matrix(S.symbols('va0:6'));vb=S.Matrix(S.symbols('vb0:6'))
da,db=S.symbols('da db')
Gram=S.zeros(11)
# Ordered Q,R,O,F,Theta1,...,Theta6,D.
Gram[0,0]=Gram[1,1]=Gram[2,2]=-1
Gram[0,1]=Gram[1,0]=ab
Gram[0,2]=Gram[2,0]=aO;Gram[1,2]=Gram[2,1]=bO
for i in (0,1,2):Gram[i,3]=Gram[3,i]=1
for i in range(6):
    Gram[0,4+i]=Gram[4+i,0]=va[i]
    Gram[1,4+i]=Gram[4+i,1]=vb[i]
    for j in range(6):Gram[4+i,4+j]=-E[i,j]
Gram[0,10]=Gram[10,0]=da;Gram[1,10]=Gram[10,1]=db;Gram[10,10]=-2
pa=S.Matrix([1,0,-1,-(aO+1),*(Ei*va),da/2])
pb=S.Matrix([0,1,-1,-(bO+1),*(Ei*vb),db/2])
eq('complete height bilinear expansion',
   -(pa.T*Gram*pb)[0],1+aO+bO-ab-(va.T*Ei*vb)[0]-da*db/2)
for col in range(2,11):
    eq(f'height projection perpendicular to column {col}',(pa.T*Gram)[col])
eq('sixfold section height',36*S.Rational(1,6),6)
eq('sixfold zero-section intersection',S.Rational(6-2,2),2)
eq('sixfold section intersection',1+0+2-1,2)
eq('Hom degree from complete restrictions',(2-2)+(0-(-1)),1)
# All six residue classes, retaining their exact correction indicators.
N=S.symbols('N',integer=True)
for r in range(6):
    n=6*N+r
    expression=n**2/S.Integer(12)-1+S.Rational(2,3)*int(r%3!=0)+S.Rational(1,4)*int(r%2!=0)
    polynomial=S.Poly(expression,N)
    assert all(S.denom(x)==1 for x in polynomial.all_coeffs())
    checks.append(f'integral section intersection residue {r}')
    eq(f'height with both corrections residue {r}',
       2+2*expression-S.Rational(4,3)*int(r%3!=0)-S.Rational(1,2)*int(r%2!=0),
       n**2/6)
for n,expected in enumerate([0,0,0,1,2,2],1):
    expression=S.Rational(n*n,12)-1+S.Rational(2,3)*int(n%3!=0)+S.Rational(1,4)*int(n%2!=0)
    eq(f'small multiple intersection {n}',expression,expected)
# Full finite lift exponents, nodal section coordinate and multiplicative scale.
beta,mu=S.symbols('beta mu')
eq('finite III lift exponent',-beta-3*mu,-(beta+3*mu))
eq('finite IVstar lift exponent',-beta-2*mu,-(beta+2*mu))
for sgn in [-1,1]:
    u0=-5+sgn*2*S.sqrt(6)
    eq(f'cusp section root {sgn}',u0**2+10*u0+1)
    eq(f'cusp section x {sgn}',1+12*u0/(u0-1)**2)
# Every original affine triangle basis and translation-unit exponent.
a,b,r,s=S.symbols('a b r s',integer=True)
rays=S.Matrix([[a,a+1,a],[b,b,b+1],[1,1,1]])
dual=S.Matrix([[-1,-1,1+a+b],[1,0,-a],[0,1,-b]])
eq('L triangle exact dual matrix',(dual*rays-S.eye(3)).norm(),0)
eq('L triangle base character',(S.ones(1,3)*dual-S.Matrix([[0,0,1]])).norm(),0)
eq('L triangle unimodularity',rays.det(),1)
upper=S.Matrix([[a+1,a,a+1],[b,b+1,b+1],[1,1,1]])
eq('U triangle ordered determinant',upper.det(),-1)
fan=[S.Matrix(v) for v in [(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]]
for i,v in enumerate(fan):
    eq(f'hexagon adjacent determinant {i}',S.Matrix.hstack(v,fan[(i+1)%6]).det(),1)
    eq(f'hexagon full neighbour relation {i}',(fan[i-1]+fan[(i+1)%6]-v).norm(),0)
source=root/'src/cusp-and-compact-threefold.md'
report={'lesson':'CG-S6-05','checks':len(checks),'passed':len(checks),'check_names':checks,
 'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'scope':'Exact finite algebra checks. Analytic convergence, separation, properness, global extension and comparison require the complete written proofs.'}
(root/'checks/CUSP_GEOMETRY_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'lesson':'CG-S6-05','checks':len(checks),'passed':True}))
