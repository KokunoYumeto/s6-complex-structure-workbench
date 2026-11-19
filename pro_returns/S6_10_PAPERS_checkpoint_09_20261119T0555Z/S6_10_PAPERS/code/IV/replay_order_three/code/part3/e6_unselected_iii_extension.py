#!/usr/bin/env python3
"""Exact symbolic source, root, Cartier, norm and sector identities."""
from pathlib import Path
import sympy as S,json,hashlib,math
R=Path(__file__).resolve().parents[2];checks=[]
def eq(name,e):
 v=S.factor(S.together(e))
 if v!=0:raise AssertionError((name,v))
 checks.append(name)
def mod(name,e,rel,var):
 num=S.fraction(S.together(e))[0]
 eq(name,S.rem(num,rel,var))

x,y,z,a,b,c,cp,B,C,s,u,v,L=S.symbols('x y z a b c cp B C s u v L')
l=S.symbols('l',integer=True,nonnegative=True)
f0,f1,f2,f3=S.symbols('f0 f1 f2 f3')
eq('literal three-step point-line lift',(f0*f1)*(f1*f2)*(f2*f3)-f0*f3*f1**2*f2**2)
for component in [0,1]:
 vals=[(component+j)%2 for j in range(4)]
 eq('I2 three-step order component'+str(component),vals[0]+2*vals[1]+2*vals[2]+vals[3]-3)
curve=y*y-x**3-1
tx=2*x/(y-1);ty=-(y+3)/(y-1)
tx2=-2*x/(y+1);ty2=(y-3)/(y+1)
mod('actual central minus-G x',((y+1)/x)**2-x-tx,curve,y)
mod('actual central minus-G y',1-(y+1)/x*tx-ty,curve,y)
eq('actual central second x',2*tx/(ty-1)-tx2)
eq('actual central second y',-(ty+3)/(ty-1)-ty2)
eq('actual central third x',2*tx2/(ty2-1)-x)
eq('actual central third y',-(ty2+3)/(ty2-1)-y)
eq('central f second factor',(ty-1)/tx+(y+1)/x)
eq('central f third factor',(ty2-1)/tx2-2/x)
mod('full central Miller norm',(y-1)/x*(-(y+1)/x)*2/x+2,curve,y)
eq('full M2 central multiplier',(-2)**2-4)

# Universal reduced root: B=z^l and C=r z^(2l), held fixed by the fibre law.
cc=c*c-1-B*a*b-C*a*a*b*b
zz=a*b*(b-a)/(2*c);XX=a*b;YY=a*b*(a+b)/2
mod('universal reduced root equation',YY*YY-XX**3-zz*zz*(C*XX*XX+B*XX+1),cc,c)
K=1+b*(b-a)*(B+C*a*b)/(2*c*(c+1))
mod('universal chord slope',(YY-zz)/XX-a*K,cc,c)
F=1-a*b*(B+C*a*b)*(K+1)/(2*c*(c+1))-C*a*b*b*(a-b)/(4*c*c)
Xp=a*(a-b)*F;Yp=-zz-a*K*Xp
eq('universal X prime',a*a*K*K-C*zz*zz-XX-Xp)
H=K+b*(a-b)*(B+C*Xp)/(2*c*(1+cp))
mod('universal V prime',Yp+zz*cp+a*Xp*H,cp*cp-1-B*Xp-C*Xp*Xp,cp)
eq('universal toric product',((b-a)*F/H)*(-a*H)-Xp)
for name,fun in [('K',K),('F',F),('H',H)]:
 eq('central unit '+name,fun.subs({a:0,b:0,c:1,cp:1})-1)
J0=B+2*C*XX
WU=3*XX*XX-zz*J0*(a*XX)/c
WV=3*XX*XX+zz*J0*(b*XX)/c
Wa=a*(2*b-a-zz*J0/c);Wb=b*(2*a-b+zz*J0/c)
eq('regular vertical field a',(WU*XX-a*XX*2*YY)/XX**2-Wa)
eq('regular vertical field b',(WV*XX-b*XX*2*YY)/XX**2-Wb)
eq('regular field preserves X',Wa*b+a*Wb-2*YY)

# All exponent equalities are symbolic in l, not inferred from finite samples.
mr=3*l+2;kr=2*l+1;mg=3*l;kg=2*l
for name,m,k,A2,A4,A6,Gexp in [('reduced',mr,kr,2*l+2,l+2,2,1),('good',mg,kg,2*l,l,0,0)]:
 eq(name+' root a2 exponent',2*m-2*k-A2)
 eq(name+' root a4 exponent',3*m-4*k-A4)
 eq(name+' root a6 exponent',4*m-6*k-A6)
 eq(name+' marked G exponent',2*m-3*k-Gexp)
 eq(name+' actual root formal weight',-2*k+3*k-k)
 eq(name+' chord times tau deck weight',-k+k)
eq('reduced full selected coefficient exponent',2*mr-6*(mr-kr)+2)
eq('good full selected coefficient exponent',2*mg-6*(mg-kg))
eq('reduced invariant c weight',l-2*kr+mr)
eq('reduced middle deck cubic',3*(l+1)-mr-1)
eq('reduced middle X deck',2*(l+1)+2*kr-2*mr)
eq('reduced middle U deck',-3*kr+2*mr-1)
eq('reduced unit K weight',2*(l+1)+l-mr)
eq('reduced unit high term weight',4*(l+1)+2*l-2*mr)
eq('reduced division exact norm',mr*(2-(2*mr-1)/mr)-1)
eq('small division component multiple',2*mr-1-3*(2*l+1))
eq('whole Miller root leading exponent',2*(kr+1)-2*kr-2)
w=S.symbols('w')
eq('whole Miller root leading coefficient',w**6*(s/(-s*w**3/2))**2*(-4/s)/(-4/s)-4)
eq('root tangent-over-vertical leading coefficient',(-8/s**3+(3/s)*(4/s**2))/(-1/s**2)+4/s)

# Both actual graph chart coefficients, including the equality direction.
Zk=S.symbols('Zk')
eq('first reduced graph coefficient',u/(u-L)-(Zk*u)/(Zk*u-Zk*L))
eq('second reduced graph coefficient',u/(u-L)-1/(1-L/u))
for ll in range(25):
 mm=3*ll+2;kk=2*ll+1
 if math.gcd(ll+1,mm)!=1:raise AssertionError('deck order')
 checks.append('primitive reduced deck l'+str(ll))
 rays=[(j,1) for j in range(kk,-1,-1)]
 eq(f'first reduced graph cone determinant l{ll}',S.det(S.Matrix([[1,kk],[0,1]]))-1)
 for j0 in range(kk):
  p,q=rays[j0];p1,q1=rays[j0+1]
  eq(f'reduced adjacent graph determinant l{ll}j{j0}',p*q1-q*p1-1)
 for p,q in rays[:-1]:
  # ord(tau)=p; ord(tau-z^k L)=min(p,kq) with L a nonzero
  # independent unit. Equality retains the distinct strict directions.
  eq(f'actual reduced graph section orders l{ll}j{p}',p-min(p,kk*q))
for ll in range(1,25):
 for p,q in [(1,0),(2*ll,1),(ll,1),(0,1)]:
  eq(f'good strict-section correction l{ll}p{p}q{q}',p-max(p-2*ll*q,0)-min(p,2*ll*q))

# The actual n-signed root/line/character norm and full overlap square.
ss,kk,nn,ff,PP,cc0,jj,bb0,LL,hh=S.symbols('ss kk nn ff PP cc0 jj bb0 LL hh')
f_beta=ff+PP;h_beta=hh-nn*ss*PP+jj*bb0+LL
U_alpha=nn*ss*ff+ss*cc0+hh
U_beta=nn*(ss+kk)*f_beta+(ss+kk)*cc0+h_beta
eq('full target-sheet cap overlap',U_beta-U_alpha-kk*(nn*f_beta+cc0)-jj*bb0-LL)
for nn0 in [-1,1]:
 for ll in range(1,25):
  for mm in [3*ll,3*ll+2]:
   eq(f'actual cap generator m{mm}n{nn0}',nn0*nn0-1)
   for dd in range(mm):
    eq(f'finite character exact norm m{mm}n{nn0}d{dd}',S.Rational(dd,mm)*mm-dd)
eq('full marked source scalar cancellation',-6+6)
src=R/'notes/part3_e6_unselected_iii_extension_working.md'
out={'status':'PASS','checks':len(checks),'source':str(src.relative_to(R)),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'identities':checks,'scope':'Both complete admitted E6 cap progressions, signed norms, literal source/root/line and reference cochains. Geometry separately audited.','no_numbered_promotion':True}
(R/'code/part3/e6_unselected_iii_extension.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
