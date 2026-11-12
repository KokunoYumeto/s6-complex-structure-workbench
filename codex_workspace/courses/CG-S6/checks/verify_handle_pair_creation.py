"""Finite exact derivative and framing checks; the geometric proofs remain in the chapter."""
from pathlib import Path
import sympy as S
import hashlib,json
W=Path(__file__).resolve().parents[1];checks=[]
def ck(n,v):
 assert v,n
 checks.append(n)
def eq(a,b):return S.simplify(a-b)==0
u,s,L=S.symbols('u s L',positive=True)
delta=4*S.exp(-1/(1-u*u))
g=8*u/(1-u*u)**2*S.exp(-1/(1-u*u))
ck('Full derivative of the original bump gives h prime equal to one minus g',eq(S.diff(u+delta,u),1-g))
ck('The exact logarithmic derivative retains both denominator factors',eq(S.diff(g,u)/g,(1-3*u**4)/(u*(1-u*u)**2)))
ck('The unique maximum coordinate is the exact fourth root',eq(1-3*(3**(-S.Rational(1,4)))**4,0))
ck('The displayed value of g at one half is exact',eq(g.subs(u,S.Rational(1,2)),S.Rational(64,9)*S.exp(-S.Rational(4,3))))
ck('The actual explicit cutoff has integral one',eq(S.Rational(4,3)*(S.Rational(1,24)+S.Rational(2,3)+S.Rational(1,24)),1))
ck('The retained derivative gap is one fifth',eq(1-S.Rational(3,5)*S.Rational(4,3),S.Rational(1,5)))
ck('The entire support lies above the original lower level by one sixtieth',eq(S.Rational(1,5)*(1-S.Rational(11,12)),S.Rational(1,60)))
y=S.symbols('y1:3',real=True);z=S.symbols('z1:4',real=True)
aa=S.symbols('a1:3',positive=True);bb=S.symbols('b1:4',positive=True)
A=sum(a*v*v for a,v in zip(aa,y));B=sum(b*v*v for b,v in zip(bb,z))
h=S.Function('h');d=S.Function('delta');R=S.Function('R');be=S.Function('beta');et=S.Function('eta')
v=A/R(u)**2;F=h(u)-A+B-(1-s)*d(u)*be(v)*et(B)
q=S.symbols('q');bep=S.diff(be(q),q).subs(q,v);etp=S.diff(et(q),q).subs(q,B)
for i,(a,x) in enumerate(zip(aa,y)):
 ck('Full negative-coordinate derivative '+str(i),eq(S.diff(F,x),-2*a*x*(1+(1-s)*d(u)/R(u)**2*bep*et(B))))
for j,(b,x) in enumerate(zip(bb,z)):
 ck('Full positive-coordinate derivative '+str(j),eq(S.diff(F,x),2*b*x*(1-(1-s)*d(u)*be(v)*etp)))
want=S.diff(h(u),u)-(1-s)*S.diff(d(u),u)*be(v)*et(B)+2*(1-s)*d(u)*S.diff(R(u),u)/R(u)*v*bep*et(B)
ck('Complete variable-radius u derivative at every birth parameter',eq(S.diff(F,u),want))
Av,Bv,da,a=S.symbols('A B delta a',positive=True)
u0=a+Av-Bv;gam=1+da/Av
ck('The original level parametrization retains the bump contribution',eq(u0+da-gam*Av+Bv,a))
ck('The inverse radial factors multiply to one on the level',eq(gam*(Av/(Av+da)),1))
Au,Bu,du,dd=S.symbols('dA dB du ddelta')
gamfun=1+d(a+Av-Bv)/Av
ck('The full gamma derivative in the original A variable',eq(S.diff(gamfun,Av),S.Subs(S.Derivative(d(u),u),u,u0)/Av-d(u0)/Av**2))
ck('The full gamma derivative in the original B variable',eq(S.diff(gamfun,Bv),-S.Subs(S.Derivative(d(u),u),u,u0)/Av))
hm,um,eps,tt=S.symbols('hm um epsilon t',positive=True)
scale=S.sqrt((um-a)/(hm-a))
ck('The incoming attaching ellipsoid keeps its exact level radius',eq(scale**2*(hm-a),um-a))
T0=S.log((hm-a)/eps)/2
ck('The full unstable hitting time retains the initial epsilon',eq(eps*S.exp(2*T0),hm-a))
hf=S.Function('h')
lograd=S.log((u-a)/(hf(u)-a))/2
ck('The derivative of the lower radial factor retains h prime before evaluation',eq(S.diff(lograd,u),1/(2*(u-a))-S.diff(hf(u),u)/(2*(hf(u)-a))))
ck('The exact radial derivative at the lower critical point has the retained denominator',eq(S.diff(lograd,u).subs(S.diff(hf(u),u),0),1/(2*(u-a))))
for i,x in enumerate(y):
 ck('The original outward radial vector differentiates its ellipsoid to one coordinate '+str(i),eq(S.diff(A,x)*x/(2*Av),aa[i]*x*x/Av))
ck('The complete outward radial vector differentiates A to one on its sphere',eq(sum(S.diff(A,x)*x for x in y)/(2*A),1))
tau,hp=S.symbols('tau hp',positive=True)
Fb=h(u)-A+B
X=[-tau*S.diff(h(u),u),*y,*[-x for x in z]]
coords=[u,*y,*z]
ck('The complete model descent identity retains all five transverse coefficients',eq(sum(S.diff(Fb,x)*v for x,v in zip(coords,X)),-tau*S.diff(h(u),u)**2-2*A-2*B))
for idx,x in enumerate(y):
 ck('Unstable model coordinate flow '+str(idx),eq(S.diff(S.exp(tt)*x,tt),S.exp(tt)*x))
for idx,x in enumerate(z):
 ck('Stable model coordinate flow '+str(idx),eq(S.diff(S.exp(-tt)*x,tt),-S.exp(-tt)*x))
ex=(u+delta)-2*y[0]**2-7*y[1]**2+3*z[0]**2+5*z[1]**2+13*z[2]**2
H=S.hessian(ex,coords)
ck('All six original Hessian coefficients in the worked pair',all(eq(x,0) for x in H-S.diag(S.diff(u+delta,u,2),-4,-14,6,10,26)))
for k in [2,3,4,5]:
 n=k+2;order=list(range(1,k+1))+[0]+list(range(k+1,n));P=S.zeros(n)
 for i,j in enumerate(order):P[i,j]=1
 ck('Exact lower Morse coordinate permutation sign for k '+str(k),P.det()==(-1)**k)
lam=S.symbols('lambda',positive=True)
D=S.diag(2,3,5,7,11,13);H0=S.diag(-17,-4,-14,6,10,26)
Hactual=D.inv().T*(lam*H0)*D.inv()
ck('The complete original-coordinate Hessian congruence retains lambda',D.T*Hactual*D==lam*H0)
# Exact noncommuting matrix identity for the variable-time level projection.
M=S.Matrix([[1,2,0],[0,1,3],[0,0,1]]);vx=S.Matrix([2,1,1]);alpha=S.Matrix([[0,0,1]])
vp=M*vx;bet=alpha*M.inv();DP=M-vp*alpha
ck('The model variable-time derivative annihilates the horizontal field',DP*vx==S.zeros(3,1))
ck('The model variable-time derivative has tangent image',bet*DP==S.zeros(1,3))
ck('Without the time term the horizontal field has a nonzero level derivative',bet*M*vx==S.ones(1,1))
source=W/'src/creating-an-original-cancelling-handle-pair.md'
result=dict(source=source.name,source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),passed=len(checks),checks=checks,publication=False,independent_review=False,scope='Exact bump derivatives and critical-point equation; all supported derivatives with birth parameter, radius and five transverse coefficients; cutoff and level-gap constants; full level parametrization and its radial derivative; original attaching ellipsoid, hitting time and frame; Hessian congruence and coordinate orientation signs; noncommuting variable-time projection identities. Completeness, compact support, implantation, transversality and framed disk proofs are supplied by the text, not certified by these finite checks.')
(W/'checks/HANDLE_PAIR_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(passed=len(checks),source_sha256=result['source_sha256'])))

