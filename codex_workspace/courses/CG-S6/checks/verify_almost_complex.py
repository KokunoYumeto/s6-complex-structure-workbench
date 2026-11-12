from pathlib import Path
import sympy as S
import hashlib,json
from datetime import datetime,timezone
W=Path(__file__).resolve().parents[1]
checks=[]
def check(name,condition):
 if not condition:raise AssertionError(name)
 checks.append(name)
zero=lambda v:all(S.simplify(x)==0 for x in v)
def qmul(a,b):
 a0,a1,a2,a3=a;b0,b1,b2,b3=b
 return S.Matrix([a0*b0-a1*b1-a2*b2-a3*b3,a0*b1+a1*b0+a2*b3-a3*b2,a0*b2-a1*b3+a2*b0+a3*b1,a0*b3+a1*b2-a2*b1+a3*b0])
def qc(a):return S.Matrix([a[0],-a[1],-a[2],-a[3]])
def om(x,y):
 a,b=S.Matrix(x[:4]),S.Matrix(x[4:]);c,d=S.Matrix(y[:4]),S.Matrix(y[4:])
 return qmul(a,c).col_join(S.zeros(4,1))+(-qmul(qc(d),b)).col_join(qmul(d,a)+qmul(b,qc(c)))
def bm(x,y):
 a,b=S.Matrix(x[:4]),S.Matrix(x[4:]);c,d=S.Matrix(y[:4]),S.Matrix(y[4:])
 return (qmul(a,c)-qmul(d,qc(b))).col_join(qmul(qc(a),d)+qmul(c,b))
def phi(x):return S.Matrix(x[:4]).col_join(qc(S.Matrix(x[4:])))
def cross(x,y):return S.Matrix(om(S.Matrix([0]).col_join(x),S.Matrix([0]).col_join(y))[1:])
e=[S.eye(8)[:,j] for j in range(8)]
f=[S.eye(7)[:,j] for j in range(7)]
check('Both multiplication formulas intertwine on all64 basis pairs',all(zero(phi(om(x,y))-bm(phi(x),phi(y))) for x in e for y in e))
check('Comparison is an involution on every basis vector',all(zero(phi(phi(x))-x) for x in e))
check('Comparison fixes the real unit and preserves the Euclidean metric',phi(e[0])==e[0] and S.Matrix.hstack(*[phi(x) for x in e]).T*S.Matrix.hstack(*[phi(x) for x in e])==S.eye(8))
for a,b,c in [(1,2,3),(1,4,5),(1,7,6),(2,4,6),(2,5,7),(3,4,7),(3,6,5)]:
 check('Oriented triple'+str((a,b,c)),om(e[a],e[b])==e[c] and om(e[b],e[c])==e[a] and om(e[c],e[a])==e[b])
check('All seven imaginary squares retain minus one',all(om(e[j],e[j])==-e[0] for j in range(1,8)))
check('All imaginary off-diagonal products are skew',all(om(e[j],e[k])==-om(e[k],e[j]) for j in range(1,8) for k in range(j+1,8)))
check('Universal associator identity on all343 basis triples',all(zero(S.Matrix((om(om(e[i+1],e[j+1]),e[k+1])-om(e[i+1],om(e[j+1],e[k+1])))[1:])+2*cross(f[i],cross(f[j],f[k]))-2*f[i].dot(f[k])*f[j]+2*f[i].dot(f[j])*f[k]) for i in range(7) for j in range(7) for k in range(7)))
for j in range(7):
 p=f[j];J=S.Matrix.hstack(*[cross(p,v) for v in f])
 check('Cross-square with full radial term at basis point'+str(j+1),J*J==-S.eye(7)+p*p.T)
 for uidx in range(7):
  if uidx==j:continue
  U=f[uidx];JU=cross(p,U)
  A=S.Matrix.hstack(*[cross(U,v)-cross(U,v).dot(p)*p for v in f])
  tangent=S.eye(7)-p*p.T
  N=-4*J*A*tangent;proj=tangent-U*U.T-JU*JU.T
  check('Rank4 and inverse relation at(p,U)='+str((j+1,uidx+1)),N.rank()==4 and N*N*proj==-16*proj and N.T*N==16*proj)
p=f[6];U=f[0];V=f[1]
check('Labelled Nijenhuis tensor is minus4e4',-4*cross(p,cross(U,V))==-4*f[3])
check('Labelled associator is minus2e4',om(om(e[7],e[1]),e[2])-om(e[7],om(e[1],e[2]))==-2*e[4])
Z=[(v-S.I*cross(p,v))/2 for v in f[:3]]
for a,b,c in [(1,2,0),(2,0,1),(0,1,2)]:
 N=-4*cross(p,cross(S.conjugate(Z[a]),S.conjugate(Z[b])))
 check('Complex obstruction coefficient cyclic'+str((a+1,b+1,c+1)),zero(N+4*S.I*Z[c]))
check('Complex obstruction determinant retains64i',S.simplify((-4*S.I)**3-64*S.I)==0)
xi=S.symbols('x0:3',real=True);eta=S.symbols('y0:3',real=True)
a=[(S.I*xi[j]-eta[j])/2 for j in range(3)]
rows=[]
for j,k in [(0,1),(0,2),(1,2)]:
 row=[0]*3;row[k]=a[j];row[j]=-a[k];rows.append(row)
rows.append([-S.conjugate(x) for x in a])
symbol=S.Matrix(rows)
check('First-order elliptic symbol has exact norm factor1/4',zero(symbol.conjugate().T*symbol-S.eye(3)*sum(x*x for x in xi+eta)/4))
z,zb,eps=S.symbols('z zb eps')
H=z+eps*z*zb;Hbar=zb+eps*z*zb
E=-S.diff(H,zb)/S.diff(Hbar,zb)
jac=S.diff(H,z)*S.diff(Hbar,zb)-S.diff(H,zb)*S.diff(Hbar,z)
Psi=S.diff(E,z)*S.diff(Hbar,zb)/jac-S.diff(E,zb)*S.diff(Hbar,z)/jac
check('Original gauge formula has negative first variation',S.simplify(S.diff(Psi,eps).subs(eps,0))==-1)
check('The quadratic local test retains both denominators',S.simplify(Psi+eps/((1+eps*z)*(1+eps*(z+zb))))==0)
for k in range(1,101):
 total=sum(S.Rational(k-j+1,(j+1)**2*(k-j+2)**2) for j in range(1,k+1))
 assert total<=S.Rational(8*(k+1),(k+2)**2)
check('First100 exact factorial-convolution inequalities',True)
check('Original octonion complex orientation is negative outward orientation',S.Matrix.hstack(f[0],-f[5],f[1],f[4],f[2],f[3],p).det()==-1)
check('Algebra comparison reverses the imaginary orientation',S.Matrix.hstack(*[phi(x) for x in e]).det()==-1)
r=S.symbols('r',positive=True)
check('Original tautological curvature has Chern number minus one',S.integrate(-2*r/(1+r*r)**2,(r,0,S.oo))==-1)
check('Factorial tangent obstruction leaves n1,n2,n3 before the parity test',[n for n in range(1,10) if S.Integer(2)%S.factorial(n-1)==0]==[1,2,3])
check('Conjugate-summand parity excludes n2',1+(-1)**2==2 and 1+(-1)**3==0)
a0=S.Matrix([[1,2],[0,1]]);a1=S.Matrix([[0,1],[1,0]]);a2=S.Matrix([[2,0],[1,3]])
zero2=S.zeros(2);I2=S.eye(2)
mu=S.BlockMatrix([[a0,a1,a2],[-z*I2,I2,zero2],[zero2,-z*I2,I2]]).as_explicit()
expected=S.diag(a0+a1*z+a2*z*z,I2,I2)
for j in [2,1]:
 Aj=mu[:2,2*j:2*j+2]
 left=S.eye(6);left[:2,2*j:2*j+2]=-Aj
 mu=S.simplify(left*mu)
 right=S.eye(6);right[2*j:2*j+2,2*(j-1):2*j]=z*I2
 mu=S.simplify(mu*right)
check('Polynomial clutching elimination preserves noncommuting coefficient order',zero(mu-expected))
theta=S.symbols('theta',real=True)
rotation=S.BlockMatrix([[S.cos(theta)*I2,-S.sin(theta)*I2],[S.sin(theta)*I2,S.cos(theta)*I2]]).as_explicit()
g=a0;h=a2
path=S.diag(g,I2)*rotation*S.diag(I2,h)*rotation.T
check('Based loop product homotopy has the exact two endpoints',path.subs(theta,0)==S.diag(g,h) and path.subs(theta,S.pi/2)==S.diag(g*h,I2))
u1,u2=S.symbols('u1 u2')
check('Tensor line retains rank and both intermediate Chern terms',S.expand((1-u1)*(1-u2))==1-u1-u2+u1*u2)
source=W/'src/almost-complex-structures-and-integrability.md'
out=dict(source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),checks=checks,passed=len(checks),limits='Exact finite algebra checks and100 rational inequalities supplement the complete written arguments. They are not a test of convergence or a substitute for the analytic estimates.')
(W/'checks/ALMOST_COMPLEX_CHECKS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':len(checks),'source_sha256':out['source_sha256']}))
