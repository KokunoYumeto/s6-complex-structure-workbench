"""Exact local checks supplementing the written Morse realization and cancellation."""
from pathlib import Path
import hashlib,json
import sympy as S
W=Path(__file__).resolve().parents[1]
checks=[]
def ck(name,ok):
 assert bool(ok),name
 checks.append(name)
def zero(v):return all(S.simplify(x)==0 for x in v)
delta,beta,r,s=S.symbols('delta beta r s',positive=True)
c=S.symbols('c',real=True)
for n,k in [(6,2),(6,3),(6,4),(7,2),(7,3),(7,4),(7,5)]:
 q=n-k
 u=S.Matrix(S.symbols('u0:'+str(k),real=True));v=S.Matrix(S.symbols('v0:'+str(q),real=True))
 aa=S.symbols('a0:'+str(k),positive=True);bb=S.symbols('b0:'+str(q),positive=True)
 B=beta*v.dot(v)/s**2;A=(delta+B)*u.dot(u)/r**2
 E=S.Matrix([u[j]/r*S.sqrt((delta+B)/aa[j]) for j in range(k)]+[v[j]/s*S.sqrt(beta/bb[j]) for j in range(q)])
 coords=S.Matrix.vstack(u,v)
 f=c-A+B
 X=S.Matrix.vstack(-(delta+2*B)/(delta+B)*u,v)
 ck(f'Full original quadratic identity n={n} k={k}',S.simplify(c-sum(aa[j]*E[j]**2 for j in range(k))+sum(bb[j]*E[k+j]**2 for j in range(q))-f)==0)
 pushed=E.jacobian(coords)*X
 for j in range(n):ck(f'Full field transport n={n} k={k} coordinate={j}',S.simplify(pushed[j]-(-E[j] if j<k else E[j]))==0)
 ck(f'Actual positive function derivative n={n} k={k}',S.simplify((S.Matrix([f]).jacobian(coords)*X)[0]-2*(A+B))==0)
 origin={x:0 for x in coords}
 H=S.hessian(f,coords).subs(origin)
 ck(f'Entire original-parameter Hessian n={n} k={k}',H==S.diag(*([-2*delta/r**2]*k+[2*beta/s**2]*q)))
 expected_det=(-2*delta/r**2)**k*(2*beta/s**2)**q
 ck(f'Hessian determinant with every scale n={n} k={k}',S.simplify(H.det()-expected_det)==0)
 invv=S.Matrix([s*S.sqrt(bb[j]/beta)*E[k+j] for j in range(q)])
 ck(f'Full positive coordinate inverse n={n} k={k}',zero(invv-v))
 invu=S.Matrix([r*S.sqrt(aa[j]/(delta+sum(bb[h]*E[k+h]**2 for h in range(q))))*E[j] for j in range(k)])
 ck(f'Full negative coordinate inverse n={n} k={k}',zero(invu-u))
B,sigma,tau=S.symbols('B sigma tau',real=True)
tauof=-(2*sigma/r+sigma**2/r**2)*(delta+B)
ck('Original seam transverse derivative',S.simplify(S.diff(tauof,sigma)+2*(1+sigma/r)*(delta+B)/r)==0)
ck('Original seam full positive-block derivative',S.diff(tauof,B)==-(2*sigma/r+sigma**2/r**2))
inv=r*(S.sqrt(1-tau/(delta+B))-1)
ck('Seam inverse retains the full square root',S.simplify(tauof.subs(sigma,inv)-tau)==0)
sigmadot=-(r+sigma)*(delta+2*B)/(delta+B)
ck('Seam field retains radial and positive terms',S.simplify(S.diff(tauof,sigma)*sigmadot+S.diff(tauof,B)*2*B-2*(delta+2*B-tauof))==0)
a,T,L,rho,etap,eta,ell=S.symbols('a T L rho etap eta ell',real=True)
for d in [5,6]:
 dl=S.Matrix(1,d,S.symbols('dl0:'+str(d)))
 J=S.eye(d+1);J[d,:d]=rho/L*dl;J[d,d]=(ell-a)/L
 invJ=S.eye(d+1);invJ[d,:d]=-rho/(ell-a)*dl;invJ[d,d]=L/(ell-a)
 ck(f'Variable roof full inverse in level dimension {d}',zero(J*invJ-S.eye(d+1)))
 ck(f'Variable roof determinant in level dimension {d}',S.simplify(J.det()-(ell-a)/L)==0)
 dT=S.Matrix(1,d,S.symbols('dT0:'+str(d)))
 K=S.eye(d+1);K[d,:d]=eta*dT;K[d,d]=1+T*etap
 invK=S.eye(d+1);invK[d,:d]=-eta/(1+T*etap)*dT;invK[d,d]=1/(1+T*etap)
 ck(f'Full collar absorption inverse in level dimension {d}',zero(K*invK-S.eye(d+1)))
 ck(f'Full collar absorption determinant in level dimension {d}',S.simplify(K.det()-(1+T*etap))==0)
 # A transverse level gives an n-dimensional sum after adjoining the actual flow line.
 for p in [2,3]:
  q=d-p
  E=S.eye(d+1)
  flow=E[:,d]+sum((S.Integer(j+1)*E[:,j] for j in range(d)),S.zeros(d+1,1))
  tangents=S.Matrix.hstack(*[E[:,j] for j in range(p)],flow,*[E[:,j] for j in range(p,d)])
  ck(f'Full trajectory tangent rank d={d} p={p} q={q}',tangents.rank()==d+1)
  ck(f'Full trajectory tangent determinant d={d} p={p} q={q}',tangents.det()==(-1)**q)
# A nonconstant second-order collar germ tests the dilation, including its normal speed.
z,h,w=S.symbols('z h w',real=True);eps=S.symbols('eps',positive=True)
base=z+h*(1+z**2)+h*h*z
height=(2+z*z)*h+(3+z)*h*h+h**3
gs=S.Matrix([base.subs(h,eps*w),height.subs(h,eps*w)/eps])
g0=S.Matrix([S.limit(x,eps,0) for x in gs])
ck('Dilation limit retains varying transverse speed',zero(g0-S.Matrix([z,(2+z*z)*w])))
ck('Whole collar germ recovered at parameter one',gs.subs(eps,1)==S.Matrix([base.subs(h,w),height.subs(h,w)]))
ck('Full boundary derivative includes tangential shear',gs.jacobian([z,w]).subs(w,0)==S.Matrix([[1,eps*(1+z*z)],[0,2+z*z]]))
# Worked example retains zero coordinates and their nonzero coefficients.
uu=S.Matrix([0,1]);vv=S.Matrix([S.Rational(3,5),S.Rational(4,5),0,0])
B1=3*vv.dot(vv)/9;A1=(2+B1)*uu.dot(uu)/4
ck('Exercise roof values and original unequal widths',(6-2,6-5,6+7+1)==(4,1,14))
ck('Exercise exact function',B1==S.Rational(1,3) and A1==S.Rational(7,12) and 6-A1+B1==S.Rational(23,4))
xx=S.Matrix([0,S.sqrt(S.Rational(7,33))/2])
yy=S.Matrix([S.Rational(1,5),S.Rational(4,15)*S.sqrt(S.Rational(3,13)),0,0])
ck('Exercise negative quadratic sum',(xx.T*S.diag(2,11)*xx)[0]==A1)
ck('Exercise all four positive contributions',(yy.T*S.diag(3,13,17,19)*yy)[0]==B1)
ck('Exercise original field coefficient',(2+2*B1)/(2+B1)==S.Rational(8,7))
ck('Exercise exact derivative',2*(A1+B1)==S.Rational(11,6))
D3=S.Matrix([[1,0]]);D4=S.Matrix([[0],[1]])
ck('Exercise relative chain identity',D3*D4==S.zeros(1,1))
ck('Exercise integer kernel and image',D3.nullspace()==[D4] and D3*S.Matrix([1,0])==S.ones(1,1))
ck('Exercise original signed counts',sum([1,1,-1])==D3[0,0] and sum([1,-1])==D3[0,1])
src=W/'src/realizing-framed-handles-and-middle-cancellation.md'
result=dict(passed=len(checks),checks=checks,source=src.name,source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),scope='Finite full-coordinate function, field, Hessian, seam, collar, transversality and exercise identities. These checks do not certify the global smooth or homotopy arguments.')
(W/'checks/MIDDLE_REALIZATION_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(passed=len(checks),source_sha256=result['source_sha256'])))
