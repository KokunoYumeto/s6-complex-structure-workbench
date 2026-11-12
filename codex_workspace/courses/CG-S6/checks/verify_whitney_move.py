"""Finite exact checks supplementing the complete supported-move proof."""
from pathlib import Path
import hashlib,json
import sympy as S
W=Path(__file__).resolve().parents[1]
checks=[]
def check(name,condition):
 assert condition,name
 checks.append(name)
def equal(a,b):return S.simplify(a-b)==0
x,y,z1,z2,z3,t=S.symbols('x y z1 z2 z3 t',real=True)
R,d,b,h=S.symbols('R d b h',positive=True)
chi=S.Function('chi');phi=R**2-x**2
u=4*phi/d+2;mu=chi(u);delta=mu*(phi+d)
L=(y+2*d)/d;H=(phi+d-y)/d
eta=chi(L)*chi(H);Z=2-2*(z1*z1+z2*z2+z3*z3)/b**2;zeta=chi(Z)
cp=lambda q:S.Subs(S.Derivative(chi(S.Symbol('v')),S.Symbol('v')),S.Symbol('v'),q)
check('Full x cutoff derivative retains both terms',equal(S.diff(delta,x),-2*x*(chi(u)+4*(phi+d)*cp(u)/d)))
check('Both y-window x factors retained',equal(S.diff(eta,x),-2*x*chi(L)*cp(H)/d))
check('Both signed y-window derivative terms retained',equal(S.diff(eta,y),(cp(L)*chi(H)-chi(L)*cp(H))/d))
for z in [z1,z2,z3]:
 check('Original normal radius and derivative in '+str(z),equal(S.diff(zeta,z),-4*z*cp(Z)/b**2))
v=delta*eta*zeta
check('Complete x derivative of the field',equal(S.diff(v,x),S.diff(delta,x)*eta*zeta+delta*S.diff(eta,x)*zeta))
check('Complete y derivative of the field',equal(S.diff(v,y),delta*S.diff(eta,y)*zeta))
check('Entire sheet displacement retains the cutoff convex combination',equal(phi-delta,(1-mu)*phi-mu*d))
q=(1-t)*(R**2-x*x)-t*d;star=R**2/(R**2+d)
check('Pair meeting time is exact',equal(q.subs({x:0,t:star}),0))
check('Both root squares solve the retained equation',equal(q.subs(x*x,R**2-t*d/(1-t)),0))
A=S.Matrix([1,S.diff(q,x),0,0,0]);AZ=S.Matrix([0,0,1,0,0])
BX=S.Matrix([1,0,0,0,0]);BZ2=S.Matrix([0,0,0,1,0]);BZ3=S.Matrix([0,0,0,0,1])
check('Full five-vector intersection determinant has the original sign',equal(S.Matrix.hstack(A,AZ,BX,BZ2,BZ3).det(),-2*(1-t)*x))
check('The second spatial tangency derivative is nonzero with full d',equal(S.diff(q,x,2).subs(t,star),-2*d/(R**2+d)))
check('The time tangency derivative retains R squared plus d',equal(S.diff(q,t).subs(x,0),-(R**2+d)))
check('Horizontal support enlargement retains the exact denominator',equal(S.sqrt(R**2+d/2)-R,d/(2*(S.sqrt(R**2+d/2)+R))))
j,ax,a1,a2,a3=S.symbols('J a_x a_1 a_2 a_3',nonzero=True)
M=S.eye(5);M[1,:]=S.Matrix([[ax,j,a1,a2,a3]])
Mi=S.eye(5);Mi[1,:]=S.Matrix([[-ax/j,1/j,-a1/j,-a2/j,-a3/j]])
check('Full ambient Jacobian determinant',M.det()==j)
check('Both full ambient inverse products',M*Mi==S.eye(5) and Mi*M==S.eye(5))
r,s,eps,k=S.symbols('r s epsilon kappa',real=True)
for sign,name in [(-1,'left'),(1,'right')]:
 X=sign*R-sign*2*R*(r+s);Y=4*R**2*r*(1-r)
 base=S.Matrix([X,Y]).jacobian([r,s])
 check(name+' corner base determinant',equal(base.det(),sign*8*R**3*(1-2*r)))
 check(name+' complete corner-to-parabola difference',equal(R**2-X**2-Y,4*R**2*s*(1-2*r-s)))
 full=S.Matrix([X,Y,z1,z2,z3]).jacobian([r,z1,s,z2,z3])
 check(name+' full chart retains coordinate-order transposition',equal(full.det(),-base.det()))
check('Top radial normal product',equal(2*x*x+phi-R**2/2,x*x+R**2/2))
check('Both left rounded normal coefficients retained',
 S.Matrix([-4*R**2*(1-2*r)*2*eps*k,2*R*2*eps*(2*k-1)])==
 4*R*eps*(k*S.Matrix([-2*R*(1-2*r),1])+(1-k)*S.Matrix([0,-1])))
theta,rr=S.symbols('theta rho_radius',real=True)
f,fr,ft=S.symbols('f f_r f_theta')
er=S.Matrix([S.cos(theta),S.sin(theta)]);eth=S.Matrix([-S.sin(theta),S.cos(theta)])
check('Polar derivative keeps angular term in its full columns',equal(S.Matrix.hstack(fr*er,ft*er+f*eth).det(),fr*f))
a,ss=S.symbols('a sigma',positive=True);aa=1-ss+ss*a
check('Normal-scale isotopy velocity at the current point',equal(S.diff(aa*t,ss),(a-1)*(aa*t)/aa))
p1,p2=S.symbols('p1 p2')
Am=S.Matrix(2,3,S.symbols('A0:6'))
Bq=S.Matrix([z1*z1+z1*z2+z3*z3,z1*z3+z2*z2])
Cq=S.Matrix([z1*z2,z2*z3,z1*z1+z3*z3])
g=S.Matrix([p1,p2])+Am*S.Matrix([z1,z2,z3])+Bq
gz=S.Matrix([z1,z2,z3])+Cq
gs=g.subs({z1:ss*z1,z2:ss*z2,z3:ss*z3},simultaneous=True)
gzs=gz.subs({z1:ss*z1,z2:ss*z2,z3:ss*z3},simultaneous=True)/ss
full=S.Matrix.vstack(gs,gzs)
J0=full.jacobian([p1,p2,z1,z2,z3]).subs({z1:0,z2:0,z3:0})
expect=S.eye(5);expect[:2,2:5]=ss*Am
check('Full dilation conjugate retains every tangential shear column',J0==expect and J0.det()==1)
check('Normal quadratic remainders have the exact dilation factor',
 S.simplify(gzs-S.Matrix([z1,z2,z3])-ss*Cq)==S.zeros(3,1))
ha=S.Function('h_A')(s,z1);k2=S.Function('k_2')(s,z1);k3=S.Function('k_3')(s,z1)
shear=S.Matrix([s,r+ha,z1,z2+k2,z3+k3])
check('A graph shear has full determinant one',shear.jacobian([s,r,z1,z2,z3]).det()==1)
check('A graph inverse retains all coefficients',
 shear.subs({r:r-ha,z2:z2-k2,z3:z3-k3},simultaneous=True)==S.Matrix([s,r,z1,z2,z3]))
hb=S.Function('h_B')(s,z2,z3);k1=S.Function('k_1')(s,z2,z3)
shearb=S.Matrix([s,r+hb,z1+k1,z2,z3])
check('B graph shear retains both normal parameters',shearb.jacobian([s,r,z1,z2,z3]).det()==1)
check('B graph inverse retains both base and normal shifts',
 shearb.subs({r:r-hb,z1:z1-k1},simultaneous=True)==S.Matrix([s,r,z1,z2,z3]))
collar=S.eye(6);collar[:5,:5]=M;collar[:5,5]=S.Matrix(S.symbols('c0:5'))
check('Full collar derivative includes its off-diagonal column',collar.det()==j)
check('Exercise exact meeting time',star.subs({R:2,d:S.Rational(3,5)})==S.Rational(20,23))
check('Exercise retained squared intersection radius',(R**2-t*d/(1-t)).subs({R:2,d:S.Rational(3,5),t:S.Rational(1,2)})==S.Rational(17,5))
check('Exercise both exact tangency derivatives',
 S.diff(q,x,2).subs({R:2,d:S.Rational(3,5),t:S.Rational(20,23)})==-S.Rational(6,23) and
 S.diff(q,t).subs({R:2,d:S.Rational(3,5),x:0})==-S.Rational(23,5))
aval=2+S.cos(theta)/2;angle=theta+t*S.sin(theta)
den=aval.subs(theta,angle);residual=(aval*t+t*t*S.cos(theta))/den
check('Exercise residual uses the actual image angle',equal(residual*den,aval*t+t*t*S.cos(theta)))
check('Exercise residual identity normal derivative',equal(S.diff(residual,t).subs(t,0),1))
Tri=S.Matrix([[2,p1,p2],[0,3,p1+p2],[0,0,5]])
zz=S.Matrix([z1,z2,z3]);out=Tri*zz
check('Nonorthogonal frame determinant and full Gram form',
 Tri.det()==30 and equal(out.dot(out),(2*z1+p1*z2+p2*z3)**2+(3*z2+(p1+p2)*z3)**2+25*z3*z3))
vv=S.Matrix(S.symbols('v1:3'));ww=S.Matrix(S.symbols('w1:4'))
mapall=S.Matrix.vstack(S.Matrix([p1,p2]),out)
fullvariation=mapall.jacobian([p1,p2,z1,z2,z3])*S.Matrix.vstack(vv,ww)
expected=S.Matrix.vstack(vv,(S.diff(Tri,p1)*vv[0]+S.diff(Tri,p2)*vv[1])*zz+Tri*ww)
check('Full frame-coordinate differential retains the base variation',S.simplify(fullvariation-expected)==S.zeros(5,1))
source=W/'src/whitney-move-with-controlled-support.md'
report=dict(source=source.name,source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),passed=len(checks),checks=checks,independent_review=False,scope='Finite exact cutoff derivatives, intersection signs and tangency, full derivative inverses, both corner charts, polar and dilation comparisons, sheet shears, original nonorthogonal frame and collar derivatives. These checks supplement the complete written geometric proof; they do not prove the remaining original handle arrangement or smooth sphere-group calculation.')
(W/'checks/WHITNEY_MOVE_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(passed=len(checks),source_sha256=report['source_sha256'])))
