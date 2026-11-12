"""Exact finite checks for the actual relative Morse construction draft."""
from pathlib import Path
import json,hashlib
import sympy as S
W=Path(__file__).resolve().parents[1];checks=[]
def check(name,v):
 assert v,name
 checks.append(name)
def eq(a,b):return S.simplify(a-b)==0
g=S.symbols('g',positive=True);p=S.Matrix(S.symbols('p0:6'));dg=S.Matrix(S.symbols('g0:6'))
jet=S.zeros(7);jet[0,0]=g
for j in range(6):jet[0,j+1]=g*p[j]
for i in range(6):
 jet[i+1,0]=dg[i]
 for j in range(6):jet[i+1,j+1]=dg[i]*p[j]+g*int(i==j)
col=S.eye(7)
for j in range(6):col[0,j+1]=-p[j]
reduced=jet*col
check('Six-dimensional augmented jet keeps the constant parameter',reduced[0,1:7]==S.zeros(1,6) and reduced[1:7,1:7]==g*S.eye(6))
check('Exact determinant of the complete six-dimensional local jet',reduced.det()==g**7 and col.det()==1)
a,b,c,pd,qd,rd=S.symbols('a b c delta_a delta_b delta_c')
AA=S.Matrix([[a,b],[b,c]]);DD=S.Matrix([[pd,qd],[qd,rd]])
KK=-AA.inv()*DD/2
check('Full noncommuting symmetric congruence velocity',S.simplify(KK.T*AA+DD+AA*KK)==S.zeros(2))
example=AA.subs({a:2,b:1,c:-3});de=DD.subs({pd:1,qd:2,rd:3})
check('The comparison does not assume commutation',example*de-de*example!=S.zeros(2))
s,alpha,delta=S.symbols('s alpha delta',positive=True)
M=S.sqrt(alpha/(alpha+s*delta))
check('Scalar exact matrix flow including the half coefficient',eq(S.diff(M,s),-delta*M/(2*(alpha+s*delta))))
check('Scalar full congruence conserves the original coefficient',eq(M*M*(alpha+s*delta),alpha))
x=S.Matrix(S.symbols('x0:6'));lam=S.symbols('lambda0:6')
f=sum(lam[i]*x[i]**2/2 for i in range(6))
check('All six original eigenvalues remain in the full Hessian',S.hessian(f,x)==S.diag(*lam))
A,B,D=S.symbols('A B D',positive=True);rad=S.sqrt(D*D+4*A*B)
sm=2*A/(D+rad);sp=(D+rad)/(2*B)
check('Lower exponential coordinate solves the exact level equation',eq(-A/sm+B*sm,-D))
check('Upper exponential coordinate solves the exact level equation',eq(-A/sp+B*sp,D))
check('Lower formula includes the B equals zero domain',eq(sm.subs(B,0),A/D))
check('Upper formula includes the A equals zero domain',eq(sp.subs(A,0),D/B))
for root,name in [(sm,'lower'),(sp,'upper')]:
 check(name+' exact positive level derivative denominator',eq(A/root+B*root,rad))
 check(name+' complete A derivative of the hit time',eq(S.diff(root,A)/(2*root),1/(2*root*rad)))
 check(name+' complete B derivative of the hit time',eq(S.diff(root,B)/(2*root),-root/(2*rad)))
da,db,ss=S.symbols('dA dB exponential_time',nonzero=True)
dt=(da/ss-ss*db)/(2*(A/ss+B*ss))
check('Every time-derivative contribution cancels in the target tangent map',eq(-da/ss+ss*db+2*(A/ss+B*ss)*dt,0))
tt=S.symbols('t',real=True)
for k in range(7):
 determinant=S.exp(-tt)**k*S.exp(tt)**(6-k)
 check('Original six-dimensional flow determinant at index '+str(k),eq(determinant,S.exp((6-2*k)*tt)))
Av=S.Integer(3);Bv=S.Rational(9,20);Dv=S.Rational(4,5)
rm=sm.subs({A:Av,B:Bv,D:Dv});rp=sp.subs({A:Av,B:Bv,D:Dv})
check('Diagram lower and upper levels retain every sample coefficient',eq(-Av/rm+Bv*rm,-Dv) and eq(-Av/rp+Bv*rp,Dv))

# Original handle embedding and its complete transverse derivative.
delta,beta,r,s=S.symbols('delta beta r s',positive=True)
u0,u1,v0,v1=S.symbols('u0 u1 v0 v1',real=True)
aa0,aa1,bb0,bb1=S.symbols('a0 a1 b0 b1',positive=True)
uu=S.Matrix([u0,u1]);vv=S.Matrix([v0,v1]);coords=[u0,u1,v0,v1]
Bv=beta*(v0*v0+v1*v1)/s**2
xx=S.Matrix([u0/r*S.sqrt((delta+Bv)/aa0),u1/r*S.sqrt((delta+Bv)/aa1)])
yy=S.Matrix([v0/s*S.sqrt(beta/bb0),v1/s*S.sqrt(beta/bb1)])
AA=aa0*xx[0]**2+aa1*xx[1]**2;BB=bb0*yy[0]**2+bb1*yy[1]**2
check('Original handle preserves all A contributions',eq(AA,(delta+Bv)*(u0*u0+u1*u1)/r**2))
check('Original handle preserves all B contributions',eq(BB,Bv))
for i in range(2):
 check('Handle inverse recovers u '+str(i),eq(r*S.sqrt([aa0,aa1][i]/(delta+BB))*xx[i],uu[i]))
 check('Handle inverse recovers v '+str(i),eq(s*S.sqrt([bb0,bb1][i]/beta)*yy[i],vv[i]))
jac=xx.col_join(yy).jacobian(coords)
for i in range(2):
 for j in range(2):
  check('Thick tube x derivative '+str(i)+','+str(j),eq(jac[i,j+2],xx[i]*S.diff(Bv,vv[j])/(2*(delta+Bv))))
check('Core y framing has every original scale factor',jac[2:4,2:4]==S.diag(S.sqrt(beta/bb0)/s,S.sqrt(beta/bb1)/s))
check('Handle Jacobian keeps all original radius and eigenvalue factors',eq(jac.det(),(delta+Bv)*beta/(r*r*s*s*S.sqrt(aa0*aa1*bb0*bb1))))
df=(-AA+BB).diff(v0)
check('The complete thick-tube derivative is tangent on the attaching face',eq(df,(1-(u0*u0+u1*u1)/r**2)*S.diff(Bv,v0)))
check('Discarding the x derivative gives the wrong tangent map',not eq(S.diff(BB,v0),df))
# Empty blocks as well as every index in both dimensions.
for n in [6,7]:
 for k in range(n+1):
  q=n-k
  av=[S.Integer(2*i+3) for i in range(k)]
  bv=[S.Integer(3*j+5) for j in range(q)]
  rval=S.Rational(17,5);sval=S.Rational(19,7);dv=S.Rational(23,11);bvscale=S.Rational(29,13)
  us=[rval/S.Integer(3*n+i+1) for i in range(k)]
  vs=[sval/S.Integer(4*n+j+1) for j in range(q)]
  vvB=bvscale*sum(z*z for z in vs)/sval**2
  xs=[us[i]/rval*S.sqrt((dv+vvB)/av[i]) for i in range(k)]
  ys=[vs[j]/sval*S.sqrt(bvscale/bv[j]) for j in range(q)]
  Aval=sum(av[i]*xs[i]**2 for i in range(k));Bval=sum(bv[j]*ys[j]**2 for j in range(q))
  check('Full six/seven dimensional handle index '+str((n,k)),eq(Aval,(dv+vvB)*sum(z*z for z in us)/rval**2) and eq(Bval,vvB) and eq(dv-Aval+Bval,(dv+vvB)*(1-sum(z*z for z in us)/rval**2)))
U,V,delta,beta=S.symbols('U V delta beta',real=True)
radial=S.Matrix([delta+beta+V-U,beta+V])
check('Exact corner coordinates retain their orientation factor',radial.jacobian([U,V]).det()==-1)
check('Exact corner coordinates recover U and V',eq(delta-radial[0]+radial[1],U) and eq(radial[1]-beta,V))
AA,BB,kap=S.symbols('A B kappa')
check('Full outward conormal field pairing',eq((1-kap)*2*(AA+BB)+kap*2*BB,2*((1-kap)*AA+BB)))
T,eta,ep,Tq=S.symbols('T eta eta_prime dT')
cm=S.Matrix([[1,0],[eta*Tq,1+T*ep]])
check('Collar absorption Jacobian including tangential time change',eq(cm.det(),1+T*ep))
check('Collar absorption inverse keeps the tangential time change',S.simplify(cm.inv()*S.Matrix([1,0])-S.Matrix([1,-eta*Tq/(1+T*ep)]))==S.zeros(2,1))
rr,dd,Bv,sg=S.symbols('r delta B sigma',positive=True)
seam=-((rr+sg)/rr)**2*(dd+Bv)+Bv
check('Exact transverse seam derivative retains radius and B',eq(S.diff(seam,sg),-2*(1+sg/rr)*(dd+Bv)/rr))


# Complete worked examples, including the nonzero terms that a shortened derivative loses.
check('Exercise 5.1 original negative-coordinate contribution',eq(-22*S.Rational(52,99)*S.Rational(21,260),-S.Rational(14,15)))
check('Exercise 5.1 original positive-coordinate contribution',eq(6*S.sqrt(S.Rational(7,3))/5*S.sqrt(S.Rational(7,3))/3,S.Rational(14,15)))
check('Exercise 5.1 full A and B retain the original lower level',eq(-S.Rational(52,9)+S.Rational(7,9),-5))
P,Q,R,et,ww=S.symbols('P Q R eta w',real=True)
GG=S.Matrix([[P,Q],[Q,R]]);JJ=S.Matrix([[1,0],[-et/4,ww]])
expected=S.Matrix([[P-et*Q/2+et*et*R/16,ww*(Q-et*R/4)],[ww*(Q-et*R/4),ww*ww*R]])
check('Exercise 5.2 complete original pullback metric',S.simplify(JJ.T*GG*JJ-expected)==S.zeros(2))
check('Exercise 5.2 full metric determinant',eq(expected.det(),ww**2*(P*R-Q**2)))
check('Exercise 5.2 inverse tangential derivative',JJ.inv()*S.Matrix([1,0])==S.Matrix([1,et/(4*ww)]))
z=S.symbols('z',real=True)
ch=S.exp(-1/z)/(S.exp(-1/z)+S.exp(-1/(1-z)))
check('Symmetric smooth step exact central value and derivative',eq(ch.subs(z,S.Rational(1,2)),S.Rational(1,2)) and eq(S.diff(ch,z).subs(z,S.Rational(1,2)),2))

source=W/'src/relative-morse-functions-and-original-handles.md'
# Bind domain checks to the exercise's actual constants, not an isolated matrix.
import re
source_text=source.read_text(encoding='utf-8')
exercise=source_text.split('### Exercise 5.2.',1)[1].split('**Solution.**',1)[0]
domain_match=re.search(r'z\\in\((-?\d+),(-?\d+)\)',exercise)
values=re.search(r'a=(-?\d+),\\qquad b=(-?\d+),\\qquad f\(q\(z\)\)=(-?\d+)\+z/(\d+),\\qquad\s*T\(z\)=(\d+)-z/(\d+)',exercise)
check('Exercise 5.2 actual interval and equation (5.7) are parsed',domain_match is not None and values is not None and r'\tag{5.7}' in exercise)
zlo,zhi=map(S.Integer,domain_match.groups())
lower,upper,offset,denominator,time_offset,time_denominator=map(S.Integer,values.groups())
fv=offset+z/denominator;travel=time_offset-z/time_denominator
check('Exercise 5.2 affine range uses a nonempty interval and positive slope',zlo<zhi and denominator>0)
flo,fhi=fv.subs(z,zlo),fv.subs(z,zhi)
# Since the domain is open and the slope positive, flo < f < fhi everywhere.
check('Exercise 5.2 full interval lies above the original lower boundary',lower<=flo)
check('Exercise 5.2 full interval lies below the upper boundary',fhi<upper)
check('Exercise 5.2 actual travel time equals b minus f',eq(travel,upper-fv))
check('Exercise 5.2 actual travel time has a positive full-interval lower bound',time_denominator>0 and travel.subs(z,zhi)>0)
check('Exercise 5.2 actual tangential travel-time derivative is retained',eq(S.diff(travel,z),-S.Rational(1,4)))
check('Exercise 5.2 negative-half witness belongs to the stated geometric range',zlo<-S.Rational(1,2)<zhi and lower<=fv.subs(z,-S.Rational(1,2))<upper)

result=dict(geometric_domain_checks=8,geometric_domain_scope='Exercise 5.2 exact affine range, lower and upper boundary, travel time and tangential derivative; not a global Morse-theory proof certificate.',source=source.name,source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),passed=len(checks),checks=checks,independent_review=False,publication=False,scope='Relative first-jet parameter map, full symmetric congruence without a commutativity assumption, all original Hessian eigenvalues, exact lower/upper hit times including exceptional-domain limits, complete tangent-map contributions and all six-dimensional index determinants. Exact handle embedding, thick-tube differential, both extreme indices, corner orientation and outward conormal, collar absorption with every travel-time derivative, original transverse seam and both complete worked exercises. The original handle decomposition and its index arrangement are proved in their included chapters; low-index removal and full reduction remain.')
(W/'checks/RELATIVE_MORSE_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(passed=len(checks),source_sha256=result['source_sha256'])))
