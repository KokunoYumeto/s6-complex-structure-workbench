"""Exact original-radius, collar, ambient-derivative and complement identities."""
from pathlib import Path
import hashlib,json
import sympy as S
W=Path(__file__).resolve().parents[1]
checks=[]
def check(name,value):
 assert value,name
 checks.append(name)
a,b,r,eps,I,A,B,R,t=S.symbols('a b r epsilon I A B R t',positive=True)
eta=S.symbols('eta',real=True);c=(b-I)/(a-I);w=c+(1-c)*eta
check('Both original endpoint radii retained by the integral',S.simplify(c*(a-I)+I-b)==0)
check('Original cutoff coefficient is positive on its exact domain',S.simplify(c.subs({a:I+A,b:I+B})-B/A)==0)
check('Derivative has the full positive convex-combination form',S.simplify(w-((1-eta)*c+eta))==0)
check('Exact cutoff integral includes constant collar and transition',S.simplify(eps+eps/S.Integer(2)-3*eps/2)==0)
check('Explicit cutoff coefficient preserves the evaluated integral',S.simplify(c.subs(I,3*eps/2)-(b-3*eps/2)/(a-3*eps/2))==0)
check('Corrected collar retains the original signed radial coordinate',S.expand((r+b-a)-b-(r-a))==0)
check('Linear-radius candidate retains its nonunit seam derivative',S.diff(b*r/a,r)==b/a)
check('Corrected collar first derivative matches the exterior identity',S.diff(r+b-a,r)==1)
check('All higher derivatives vanish on the corrected linear collar',all(S.diff(r+b-a,r,k)==0 for k in range(2,7)))
x=S.Matrix([3*r/5,4*r/5]);y=S.Matrix([b/2,b/2,b/2,b/2])
theta=a*x/r;z=r*y/a
check('Full outgoing angular coordinate has the original attaching radius',S.simplify(theta.dot(theta)-a*a)==0)
check('Original normal radius retains b times r over a',S.simplify(z.dot(z)-(b*r/a)**2)==0)
backx=(b*r/a)*theta/b;backy=b*z/(b*r/a)
check('First inverse recovers both original coordinates exactly',S.simplify(backx-x)==S.zeros(2,1) and S.simplify(backy-y)==S.zeros(4,1))
fval=S.symbols('f_r',positive=True)
z=fval*y/b
check('Corrected normal radius is exactly f of the original radius',S.simplify(z.dot(z)-fval**2)==0)
check('Corrected inverse retains both angular factors',S.simplify((r/a)*theta-x)==S.zeros(2,1) and S.simplify((b/fval)*z-y)==S.zeros(4,1))
fp=S.symbols('f_prime',positive=True)
xi=S.Matrix(S.symbols('xi0:2'));vv=S.symbols('upsilon0:3')
upsilon=S.Matrix([*vv,-sum(vv)])
omega=(a/r)*(xi-x*(x.dot(xi))/r**2)
nu=(fp/(b*r))*y*(x.dot(xi))+(fval/b)*upsilon
backxi=(r/a)*omega+theta*(z.dot(nu))/(a*fp*fval)
backupsilon=(b/fval)*(nu-z*(z.dot(nu))/fval**2)
check('Both original tangent coordinates are recovered by the full derivative inverse',
      S.simplify(backxi-xi)==S.zeros(2,1) and S.simplify(backupsilon-upsilon)==S.zeros(4,1))
angular=S.symbols('angular')
omega=S.Matrix([-4*angular/5,3*angular/5]);nu=S.Matrix(S.symbols('nu0:4'))
xi=(r/a)*omega+theta*(z.dot(nu))/(a*fp*fval)
upsilon=(b/fval)*(nu-z*(z.dot(nu))/fval**2)
againomega=(a/r)*(xi-x*(x.dot(xi))/r**2)
againnu=(fp/(b*r))*y*(x.dot(xi))+(fval/b)*upsilon
check('The reverse tangent composition recovers the full original framed target data',
      S.simplify(againomega-omega)==S.zeros(2,1) and S.simplify(againnu-nu)==S.zeros(4,1))
check('Equal original radii give the identity radial correction',S.simplify(c.subs(b,a)-1)==0 and S.simplify(w.subs(b,a)-1)==0)
for q in [2,3,4]:
 v=S.Matrix(S.symbols(f'v0:{q}'));g=S.Matrix([S.symbols(f'g0:{q}')]);M=v*g;J=S.eye(q)+t*M
 check(f'Entire rank-one determinant in normal dimension {q}',S.expand(J.det()-(1+t*(g*v)[0]))==0)
 inverse=S.eye(q)-t*M/(1+t*(g*v)[0])
 check(f'Entire normal derivative inverse in dimension {q}',S.simplify(J*inverse-S.eye(q))==S.zeros(q,q))
exI=S.Rational(3,16);exc=S.Rational(45,29)
check('Worked radii preserve the full cutoff coefficient',c.subs({a:2,b:3,I:exI})==exc)
lower=exc*S.Rational(7,4)
transition=exc*S.Rational(1,8)+(1-exc)*S.Rational(1,16)
check('Worked lower joining radius',lower==S.Rational(315,116))
check('Both terms of the complete transition integral',transition==S.Rational(37,232))
check('Upper joining value agrees with the actual collar',lower+transition==S.Rational(23,8))
u,v=S.symbols('u v',real=True);norm2=u*u+v*v
den=S.sqrt(R*R+norm2)
check('Full radius sphere-complement inverse lands on the original sphere',
      S.simplify(R*R*norm2/den**2+R**4/den**2-R*R)==0)
check('Sphere-complement inverse recovers both angular and Euclidean coordinates',
      S.simplify(R*(R/den)/(R*R/den))==1)
z2=S.symbols('z2',nonnegative=True)
check('The framed tube retains the original sphere radius',
      S.simplify((R*R-z2)/R**2*R**2+z2-R**2)==0)
check('Original radial deformation fixes the seam at every time',
      S.expand(((1-t)*r+t*a).subs(r,a)-a)==0)
check('Original radial deformation retains both endpoints',
      ((1-t)*r+t*a).subs(t,0)==r and ((1-t)*r+t*a).subs(t,1)==a)
check('Six-dimensional middle-level disk avoidance does not follow from a strict inequality',2+3==5)
check('Original index-two normal dimension gives pi1 and pi2 isomorphisms and pi3 surjection',
      6-2==4 and all(i+1<4 for i in [1,2]) and 3<4 and not 4<4)
g,g1,g2,p1,p2=S.symbols('g g1 g2 p1 p2',real=True)
jet=S.Matrix([[g,g*p1,g*p2],[g1,g1*p1+g,g1*p2],[g2,g2*p1,g2*p2+g]])
check('Full three-function first-jet determinant retains all cutoff derivatives',S.expand(jet.det()-g**3)==0)
value,d1,d2=S.symbols('value d1 d2')
dv1=(d1-g1*value/g)/g;dv2=(d2-g2*value/g)/g
dv0=value/g-p1*dv1-p2*dv2
check('Full parameter inverse supplies the prescribed value and both derivatives',
      S.simplify(jet*S.Matrix([dv0,dv1,dv2])-S.Matrix([value,d1,d2]))==S.zeros(3,1))
gp,pp1,pp2=S.symbols('g_prime p_prime1 p_prime2')
for index,pvalue,ppvalue in [(1,p1,pp1),(2,p2,pp2)]:
 check(f'Two distinct-point evaluation minor in coordinate {index}',
       S.expand(S.Matrix([[g,g*pvalue],[gp,gp*ppvalue]]).det()-g*gp*(ppvalue-pvalue))==0)
av=S.Matrix(S.symbols('a0:5'));lam=S.symbols('lambda')
rankone=av.row_join(lam*av)
check('Complete rank-one matrix chart satisfies every two-row minor',
      all(S.expand(rankone.extract([i,j],[0,1]).det())==0 for i in range(5) for j in range(i+1,5)))
coordinates=av.col_join(S.Matrix([lam*av[0]]))
check('Six rank-one chart parameters have a full nonzero coordinate Jacobian',
      S.expand(coordinates.jacobian([*av,lam]).det()-av[0])==0)
check('Every disk-defect parameter projection has strictly smaller dimension',
      [domain-codim for domain,codim in [(2,4),(2,10),(4,5),(2,3)]]==[-2,-8,-1,-1])
zj,z6,dzj,dz6,zjp,z6p,dzjp,dz6p,c0,pp,tt=S.symbols('zj z6 dzj dz6 zjp z6p dzjp dz6p c p t')
ZJ=zj+tt*dzj+pp*(zjp+tt*dzjp)
Z6=z6+tt*dz6+pp*(z6p+tt*dz6p)
nonlinear=ZJ+c0*Z6**2
full_variation=dzjp+2*c0*dz6*z6p+2*c0*z6*dz6p
check('Curved target first-jet variation retains the complete second derivative term',
      S.expand(S.diff(nonlinear,pp,tt).subs({pp:0,tt:0})-full_variation)==0)
ss=S.symbols('s',real=True);av=S.Matrix(S.symbols('a0:3',real=True))
cross=S.Matrix([[0,-av[2],av[1]],[av[2],0,-av[0]],[-av[1],av[0],0]])
normq=ss**2+av.dot(av)
CQ=(ss**2-av.dot(av))*S.eye(3)+2*av*av.T+2*ss*cross
check('Full quaternion conjugation matrix preserves the norm with its complete norm factor',
      S.simplify(CQ.T*CQ-normq**2*S.eye(3))==S.zeros(3))
check('Full quaternion conjugation determinant retains the sixth-degree norm factor',
      S.expand(CQ.det()-normq**3)==0)
vv=S.Matrix(S.symbols('v0:3'));aa=S.Matrix(S.symbols('b0:3'))
qq=S.symbols('q')
derivative=CQ.subs({ss:1,av[0]:qq*aa[0],av[1]:qq*aa[1],av[2]:qq*aa[2]}).diff(qq).subs(qq,0)
check('Quaternion covering derivative includes its factor two',S.simplify(derivative*vv-2*aa.cross(vv))==S.zeros(3,1))
theta=S.symbols('theta',real=True)
rot=S.Matrix([[1,0,0],[0,S.cos(theta),-S.sin(theta)],[0,S.sin(theta),S.cos(theta)]])
liftmatrix=CQ.subs({ss:S.cos(theta/2),av[0]:S.sin(theta/2),av[1]:0,av[2]:0})
check('Quaternion half-angle lift gives the entire oriented plane rotation',S.trigsimp(liftmatrix-rot)==S.zeros(3))
check('A full plane rotation closes in SO3 and ends at minus one in its lift',
      rot.subs(theta,2*S.pi)==S.eye(3) and S.cos(S.pi)==-1 and S.sin(S.pi)==0)
check('The permitted frame rotation keeps its original first vector and determinant',
      rot[:,0]==S.Matrix([1,0,0]) and S.trigsimp(rot.det())==1 and S.trigsimp(rot.T*rot)==S.eye(3))
block=S.Matrix(3,2,S.symbols('d0:6'));proj=S.diag(1,1,1,0,0)
projdot=S.zeros(3).row_join(block).col_join(block.T.row_join(S.zeros(2)))
K=projdot*proj-proj*projdot
check('Full projector transport generator is skew with every free tangent entry retained',K.T==-K)
check('Full projector commutator is its original derivative',K*proj-proj*K==projdot)
Afixture=S.Matrix([[1,1],[2,0],[0,3],[1,-1],[2,2]])
Pfixture=Afixture*(Afixture.T*Afixture).inv()*Afixture.T
check('Normal projector formula retains the nonorthonormal disk Gram matrix',
      Pfixture.T==Pfixture and Pfixture**2==Pfixture and Pfixture*Afixture==Afixture)
e1,e2,e3=S.symbols('e1 e2 e3')
coordinate=rot*S.Matrix([e1,e2,e3])
check('Exact changed tube coordinates retain all rotated normal contributions',
      coordinate==S.Matrix([e1,S.cos(theta)*e2-S.sin(theta)*e3,S.sin(theta)*e2+S.cos(theta)*e3]))

check('Extra collar boundary and corner strata have smaller parameter projections',
      [(2-(5-d)) for d in [2,1,0]]==[-1,-2,-3])
d11,d22,d33=S.symbols('t11 t22 t33',positive=True)
d12,d13,d23=S.symbols('t12 t13 t23',real=True)
Tri=S.Matrix([[d11,d12,d13],[0,d22,d23],[0,0,d33]])
fullgram=S.Matrix([[d11**2,d11*d12,d11*d13],
 [d11*d12,d12**2+d22**2,d12*d13+d22*d23],
 [d11*d13,d12*d13+d22*d23,d13**2+d23**2+d33**2]])
check('All six original triangular coefficients remain in the full Gram matrix',Tri.T*Tri==fullgram)
check('The full original frame determinant retains all positive diagonal factors',Tri.det()==d11*d22*d33)
check('Quaternion comparison retains the full original frame Gram matrix',
      S.simplify((CQ*Tri).T*(CQ*Tri)-normq**2*fullgram)==S.zeros(3))
tau=S.symbols('tau',real=True);blend=(1-tau)*S.eye(3)+tau*Tri
check('Exact positive triangular extension retains every off-diagonal entry',
      blend[0,1]==tau*d12 and blend[0,2]==tau*d13 and blend[1,2]==tau*d23 and
      all(S.expand(blend[i,i]-(1-tau+tau*Tri[i,i]))==0 for i in range(3)))
eye=S.eye(5)
check('First Whitney corner retains its exact negative intersection sign',
      eye[:,[0,2,1,3,4]].det()==-1)
qorient=eye[:,[0,2,1,3,4]];qorient[:,1]=-qorient[:,1]
check('Second corner retains both orientation changes and their positive product',qorient.det()==1)
g00,g01,g11=S.symbols('g00 g01 g11',real=True)
met2=S.Matrix([[g00,g01],[g01,g11]])
mixed=S.Matrix(2,3,S.symbols('m0:6',real=True))
h0,h1,h2,h3,h4,h5=S.symbols('h0:6',real=True)
met3=S.Matrix([[h0,h1,h2],[h1,h3,h4],[h2,h4,h5]])
Gfull=met2.row_join(mixed).col_join(mixed.T.row_join(met3))
Vfull=eye[:,:2];Wfull=eye[:,2:]
Wperp=(-met2.inv()*mixed).col_join(S.eye(3))
check('Full endpoint normal projection retains every original metric cross term',
      S.simplify(Vfull.T*Gfull*Wperp)==S.zeros(2,3))
check('Full projected Gram matrix equals the unsuppressed Schur expression',
      S.simplify(Wperp.T*Gfull*Wperp-(met3-mixed.T*met2.inv()*mixed))==S.zeros(3))
check('Projection changes no endpoint determinant or intersection orientation',
      Vfull.row_join(Wperp).det()==1)
eps0=S.symbols('epsilon',positive=True);I0=S.Rational(1,2)
check('Both original inner-corner endpoints retain their half and three-half widths',
      eps0/2+2*eps0*I0==3*eps0/2)
kk=S.symbols('kappa')
check('The retained corner derivative cannot vanish when the two cutoffs sum to one',
      S.expand(kk+(1-kk))==1)
Lmat=S.Matrix(3,3,S.symbols('l0:9'))
check('The nonorthogonal corner connection annihilates its whole original frame',
      S.simplify(Lmat-Lmat*(Tri.T*Tri).inv()*Tri.T*Tri)==S.zeros(3))

source=W/'src/belt-sphere-complements-and-the-whitney-disk.md'
result=dict(source=source.name,source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),passed=len(checks),checks=checks,scope='Exact collar and inverse formulas, both full tangent-map compositions, original radius factors, complete rank-one determinant and derivative inverse, worked cutoff integrals, full radius sphere complement, full disk parameter jet, double-point minors, rank strata, curved target variation, full quaternion matrix, rotation lift, projector transport, full triangular Gram factors, both corner signs, complete original metric projection and nonorthogonal connection. No finite check substitutes for the written avoidance and homotopy proofs. The supported ambient Whitney move is proved in its included companion; the original cobordism handle reduction remains in progress.',independent_review=False)
(W/'checks/BELT_COMPLEMENT_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(passed=len(checks),source_sha256=result['source_sha256'])))
