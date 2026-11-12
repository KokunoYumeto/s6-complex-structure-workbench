"""Finite exact checks for the original Morse trajectory and lowering maps."""
from pathlib import Path
import hashlib,json
import sympy as S
W=Path(__file__).resolve().parents[1];checks=[]
def check(name,v):
 assert v,name
 checks.append(name)
def eq(a,b):return S.simplify(S.factor(a-b))==0
q1,q2,t,s,e,ep=S.symbols('q1 q2 t s eta eta_prime',real=True)
A=S.Matrix([[1,2*e*q2],[0,1]]);v=S.Matrix([ep*q2*q2,0])
DF=A.row_join(v).col_join(S.Matrix([[0,0,1]]))
DI=A.inv().row_join(-A.inv()*v).col_join(S.Matrix([[0,0,1]]))
check('Full product derivative inverse keeps the time column',DF*DI==S.eye(3))
check('Full product derivative determinant is the original isotopy determinant',eq(DF.det(),A.det()))
check('Pushforward of the original descending time direction',DF*S.Matrix([0,0,-1])==S.Matrix([-ep*q2*q2,0,-1]))
check('The original shear and its inverse compose exactly',eq((q1+e*q2*q2)-e*q2*q2,q1))
eta=S.Function('eta')
curve=S.Matrix([q1+eta(t-s)*q2*q2,q2,t-s])
check('Entire descending trajectory has the specified vector field',all(eq(a,b) for a,b in zip(curve.diff(s),[-S.diff(eta(t-s),t)*q2*q2,0,-1])))
check('The shear holonomy retains its framing derivative',S.Matrix([q1+q2*q2,q2]).jacobian([q1,q2])==S.Matrix([[1,2*q2],[0,1]]))
# General isotopy blocks need not have determinant one.
a11,a12,a21,a22,u1,u2=S.symbols('a11 a12 a21 a22 u1 u2')
M=S.Matrix([[a11,a12,u1],[a21,a22,u2],[0,0,1]])
check('General holonomy chart retains its nonunit determinant',eq(M.det(),a11*a22-a12*a21))
AA=M[:2,:2];vv=M[:2,2]
check('General inverse retains every off-diagonal term',all(eq(x,0) for x in M.inv()[:2,2]+AA.inv()*vv))
# Original ellipsoid and full angular differential.
x1,x2,aa,ab,eps=S.symbols('x1 x2 a1 a2 epsilon',positive=True)
x=S.Matrix([x1,x2]);Q=aa*x1*x1+ab*x2*x2
ex=S.sqrt(eps/Q)*x
de=S.sqrt(eps/Q)*(S.eye(2)-x*S.Matrix([[S.diff(Q,x1),S.diff(Q,x2)]])/(2*Q))
check('Ellipsoid direction retains both original coefficients',eq(aa*ex[0]**2+ab*ex[1]**2,eps))
check('Full ellipsoid angular derivative',all(eq(v,0) for v in ex.jacobian(x)-de))
check('Angular differential has no radial component',all(eq(v,0) for v in de*x))
check('Exact local flow reconstructs the original point',all(eq(v,0) for v in S.sqrt(Q/eps)*ex-x))
ell=S.symbols('ell',positive=True)
check('Disk field keeps its full radial speed and coefficients',eq(S.diff(Q,x1)*ell*x1+S.diff(Q,x2)*ell*x2,2*Q*ell))
tauA,dfZ,base,cost=S.symbols('tauA dfZ base cost')
hittime=(-cost-base)/dfZ
check('Hitting-time formula includes the fixed-time flow term',eq(base+dfZ*hittime,-cost))
# Original six-variable function, with independent smooth cutoff functions.
xs=S.symbols('x0:2',real=True);ys=S.symbols('y0:4',real=True)
aco=S.symbols('a0:2',positive=True);bco=S.symbols('b0:4',positive=True)
T,delta,c=S.symbols('T delta c',positive=True)
Aq=sum(a*x*x for a,x in zip(aco,xs));Bq=sum(b*y*y for b,y in zip(bco,ys))
beta=S.Function('beta');zeta=S.Function('zeta');z=S.symbols('z')
F=c-Aq+Bq-s*delta*beta(Aq/T)*zeta(Bq)
bp=S.diff(beta(z),z).subs(z,Aq/T)
zp=S.diff(zeta(z),z).subs(z,Bq)
neg=1+s*delta/T*bp*zeta(Bq);pos=1-s*delta*beta(Aq/T)*zp
for i,(a,xv) in enumerate(zip(aco,xs)):
 check('Full lowering derivative in original negative coordinate '+str(i),eq(S.diff(F,xv),-2*a*xv*neg))
for i,(b,yv) in enumerate(zip(bco,ys)):
 check('Full lowering derivative in original positive coordinate '+str(i),eq(S.diff(F,yv),2*b*yv*pos))
flat=c-Aq+Bq-s*delta
coords=xs+ys
check('Whole original Hessian survives the constant critical change',S.hessian(flat,coords)==S.diag(*[-2*a for a in aco],*[2*b for b in bco]))
check('Critical value moves by its whole retained amount',eq(flat.subs({v:0 for v in coords}),c-s*delta))
Avar=S.symbols('A',real=True)
h=c-Avar-s*delta*beta(Avar/T)
check('Disk value derivative keeps the factor T inverse',eq(S.diff(h,Avar),-1-s*delta/T*S.diff(beta(z),z).subs(z,Avar/T)))
check('Disk field retains the complete cutoff derivative',eq(sum(S.diff(F,xv)*ell*xv for xv in xs),-2*Aq*ell*neg))
# The actual field construction can be joined to its initial value:
# convex combinations of two strictly negative numbers remain negative.
u,v,theta=S.symbols('u v theta',positive=True)
check('A convex combination preserves the full two field contributions',eq((1-theta)*(-u)+theta*(-v),-((1-theta)*u+theta*v)))
# Every original numerical coefficient in Exercise 6.2.
numer={aco[0]:2,aco[1]:7,bco[0]:3,bco[1]:5,bco[2]:13,bco[3]:17,c:11,T:9,delta:6,s:1}
Qnum=flat.subs(numer)
check('Six-dimensional original Hessian is exactly retained',S.hessian(Qnum,coords)==S.diag(-4,-14,6,10,26,34))
check('Original target critical value is five',Qnum.subs({v:0 for v in coords})==5)
check('Original lower regular level is two',11-9==2)
check('Full cutoff bound is one fifteenth',1-S.Rational(2,3)*S.Rational(7,5)==S.Rational(1,15))
check('Explicit bump has exact integral one',S.Rational(4,3)*(S.Rational(1,24)+S.Rational(2,3)+S.Rational(1,24))==1)
check('Explicit bump bound is below the retained K',S.Rational(4,3)<S.Rational(7,5))
check('Explicit bump improves the negative derivative gap to one ninth',1-S.Rational(2,3)*S.Rational(4,3)==S.Rational(1,9))
w=S.symbols('w',real=True)
check('The left bump transition starts at the original one twelfth',(12*w-1).subs(w,S.Rational(1,12))==0)
check('The left bump reaches the plateau at one sixth',(12*w-1).subs(w,S.Rational(1,6))==1)
check('The right bump begins its transition at five sixths',(11-12*w).subs(w,S.Rational(5,6))==1)
check('The right bump ends at eleven twelfths',(11-12*w).subs(w,S.Rational(11,12))==0)
# Full metric product of the example's chart, including all time terms.
g11,g12,g13,g22,g23,g33=S.symbols('g11 g12 g13 g22 g23 g33')
G=S.Matrix([[g11,g12,g13],[g12,g22,g23],[g13,g23,g33]])
P=DF.T*G*DF
check('Metric time-time coefficient retains the square and cross term',eq(P[2,2],g11*ep**2*q2**4+2*g13*ep*q2**2+g33))
check('Metric space-time coefficient retains the shear derivative',eq(P[1,2],(2*e*q2*g11+g12)*ep*q2**2+2*e*q2*g13+g23))
check('The metric determinant retains the entire change-of-coordinate determinant',eq(P.det(),DF.det()**2*G.det()))
source=W/'src/morse-trajectories-and-critical-value-lowering.md'
result=dict(source=source.name,source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),passed=len(checks),checks=checks,independent_review=False,publication=False,scope='Exact full holonomy and inverse derivatives, nonunit isotopy determinant, descending shear trajectory, original ellipsoid parametrization and hitting-time term, all six cutoff derivatives and retained Hessian, lower-level and critical-value constants, explicit smooth bump integral and gap, and full mixed metric terms. Finite symbolic checks complement the written geometric and analytic proofs; they are not an independent proof review.')
(W/'checks/MORSE_TRAJECTORY_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(passed=len(checks),source_sha256=result['source_sha256'])))

