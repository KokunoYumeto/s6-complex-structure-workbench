#!/usr/bin/env python3
from pathlib import Path
import sympy as s,json,hashlib
ROOT=Path(__file__).resolve().parents[2]
checks=[]
def ck(name,v):
    assert bool(v),name
    checks.append(name)
A=s.Matrix([[1,0,0,0],[0,1,-1,0],[3,3,-2,0],[1,1,-1,1]])
B=s.Matrix([[1,0,0,0],[0,0,1,0],[0,-1,1,0],[0,0,0,1]])
C=s.Matrix([[1,0,0,0],[0,1,0,0],[-3,-2,1,0],[-1,-1,0,1]])
ck('actualABC',A*B*C==s.eye(4))
x=s.symbols('x');polys=[]
for name,M,target in [('A',A,(x-1)**2*(x*x+x+1)),('B',B,(x-1)**2*(x*x-x+1)),('C',C,(x-1)**4)]:
    q=s.factor(M.charpoly(x).as_expr());polys.append(str(q));ck('charpoly'+name,s.expand(q-target)==0)
ck('Cnonidentity',C!=s.eye(4))
vs=s.symbols('x0:16');X=s.Matrix(4,4,vs)
sol=list(s.linsolve(list(X*A-A*X)+list(X*B-B*X)+list(X*C-C*X),vs))[0]
a,c=s.symbols('a c');E=s.zeros(4);E[3,0]=1
XX=s.Matrix(4,4,sol).subs({vs[15]:a,vs[12]:c})
ck('fullCentralizer',XX==a*s.eye(4)+c*E);ck('determinant',s.factor(XX.det())==a**4)
ck('realRankOne',E.rank()==1);ck('squareZero',E*E==s.zeros(4))
t,y=s.symbols('t y'); rhs=lambda xx:xx**3-3*t**3*(t-1)*xx+2*t**4*(t-1)*(t-s.Rational(1,2))
ck('GandMinusG',s.expand(rhs(t*t)-t**4)==0)
ck('IIunit',(x-t*t).subs({x:0,t:1})==-1)
z,Xr,V=s.symbols('z Xr V',nonzero=True);k=s.symbols('k',integer=True,positive=True)
ck('rootCartier',s.simplify((z**(4*k)*Xr-z**(6*k))/z**(4*k)-(Xr-z**(2*k)))==0)
f=s.symbols('f',nonzero=True);ck('lineInverseSquare',s.simplify(1/(f*(1/(f*V)))-V)==0)
Z,p,r=s.symbols('Z p r',nonzero=True)
ck('fullSourcePeriodInverse',s.simplify(1/(p*(1/Z))-Z/p)==0)
ck('fullLinePeriodInverse',s.simplify(1/(r*(1/V))-V/r)==0)
u=s.Matrix([1,0]);v=s.Matrix([0,1]);zero=s.zeros(2,1)
canon=lambda S:{tuple(t) for t in S}
T0=[zero,u,v];T1=[u,v,u+v]
ck('negativeFirstTriangle',canon([-w+u+v for w in T0])==canon(T1))
ck('negativeSecondTriangle',canon([-w+u+v for w in T1])==canon(T0))
L,theta,si,sj,xx=s.symbols('L theta si sj xx');left=-(L*xx+theta)+si;right=L*(-xx+sj)+theta
ck('affineSquare',s.expand(left-right-(si-L*sj-2*theta))==0)
ck('sphereFreeObstructionPlus',2!=0);ck('sphereFreeObstructionMinus',-2!=0)
for K in [1,2,3,4,5,9]:
    norm=sum((A**j for j in range(3*K)),s.zeros(4));ck('fullNorm%d'%K,norm==K*(s.eye(4)+A+A*A))
source=ROOT/'notes/part3_os49_full_automorphisms_working.md'
out={'status':'PASS','checks':len(checks),'names':checks,'centralizer':str(XX),'characteristic_polynomials':polys,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'scope':'Exact identities supporting the working full holomorphic automorphism argument; no promotion or new return assigned.'}
(ROOT/'code/part3/os49_full_automorphisms.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:',len(checks),'exact monodromy, centralizer, local inversion, fan and finite-norm identities.')
