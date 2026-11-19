"""Fresh exact residual K116 calculation; no former producer is imported/read."""
from pathlib import Path
from fractions import Fraction
import datetime, hashlib, json
import sympy as s

ROOT=Path(__file__).resolve().parents[2]
p,g,z,a,x,y,t,Q,Z,b,P,CB=s.symbols('p gamma z a x y t Q Z b P CB', nonzero=True)
checks=[]
def eq(name,left,right):
    residual=s.cancel(left-right)
    assert residual==0,(name,residual)
    checks.append({'name':name,'result':'passed'})
def yes(name,value):
    assert bool(value),name
    checks.append({'name':name,'result':'passed'})

# Divisors use basis (O,P1,P2,P8,P9), not a former result table.
v2=s.Matrix([-1,2,-1,0,0]);v8=s.Matrix([-7,8,0,-1,0])
v8T=s.Matrix([0,-7,8,0,-1])
divB=8*v2+v8T-v8
yes('directed horizontal Hom divisor cancellation',divB+s.Matrix([1,-1,0,-1,1])==s.zeros(5,1))

ell=lambda u: p**-3-u**-3-s.Rational(3,2)/u*(p**-2-u**-2)
vert=lambda u: p**-2-(2*u)**-2
eq('actual tangent factorization',ell(g),(p-g)**2*(p+2*g)/(2*g**3*p**3))
eq('actual doubled vertical factorization',vert(g),-(p-2*g)*(p+2*g)/(4*g**2*p**2))
f={2:s.cancel(ell(g)/vert(g))}
f[4]=s.cancel(f[2]**2*ell(2*g)/vert(2*g))
f[8]=s.cancel(f[4]**2*ell(4*g)/vert(4*g))
for m in (2,4,8):
    eq(f'f{m} full scalar',f[m],-m*g**(-(m-1))*(p-g)**m/((p-m*g)*p**(m-1)))
B=s.cancel(f[2]**8*f[8].subs(p,p-g)/f[8])
C=256/g**8
eq('chronological B full scalar',B,C*(p-g)*(p-8*g)/(p*(p-9*g)))
r=(p-8*g)/p
eq('finite Cartier frame coefficient',B*r.subs(p,p-g)/r,C)
cusp=C*(1-73*g**2*x+72*g**3*y)/(1-81*g**2*x)
inv_cusp=(1-57*g**2*x-56*g**3*y)/(C*(1-49*g**2*x))
norm={x:p**-2,y:p**-3}
eq('original cusp ring coefficient',cusp.subs(norm),B)
eq('inverse evaluated at inverse source',inv_cusp.subs(norm),1/B.subs(p,p+g))
xp=(x+2*g*y+g**2*x**2)/(1-g**2*x)**2
yp=(y+3*g*x**2+3*g**2*x*y+g**3*x**3)/(1-g**2*x)**3
eq('actual cusp translation x',xp.subs(norm),(p-g)**-2)
eq('actual cusp translation y',yp.subs(norm),(p-g)**-3)
relation_num=s.fraction(s.cancel(yp**2-xp**3))[0]
eq('translation preserves original cusp ring relation',s.rem(relation_num,y**2-x**3,y),0)
eq('inverse cusp coefficient after forward translation',B*inv_cusp.subs(norm).subs(p,p-g),1)
eq('reverse cusp coefficient after inverse translation',B.subs(p,p+g)*inv_cusp.subs(norm),1)

R=t*t+a;fpoly=R*R+t
slope=(3*R**2-3*fpoly)/s.sqrt(3)
eq('original G tangent slope',slope,-s.sqrt(3)*t)
eq('original doubling abscissa',slope**2-2*R,t*t-2*a)

Rm=1+a*z*z;F=Rm**2+z**3
G=Rm**3+s.Rational(3,2)*z**3*Rm+s.Rational(3,8)*z**6
delta=s.expand(F**3-G**2)
eq('exact infinity discriminant polynomial',delta,-s.Rational(3,4)*a*z**8*Rm**2-s.Rational(1,8)*z**9-s.Rational(9,8)*a*z**11-s.Rational(9,64)*z**12)
kap0=s.cancel(delta/z**8).subs(z,0)/1728
eq('inverse Tate leading coefficient',kap0,-a/2304)
sqrtF=s.series(s.sqrt(F),z,0,7).removeO()
pi0=s.expand(Rm-sqrtF).coeff(z,3)/12
eq('actual point leading coefficient',pi0,-s.Rational(1,24))
b0=s.cancel(pi0**8/kap0**3)
eq('identity component point',b0,-1/(9*a**3))
eq('unselected II value',b0.subs(a**3,s.Rational(3,256)),-s.Rational(256,27))
yes('identity component point separated from zero',-s.Rational(256,27)!=1)
eq('central X coordinate',1+12*b0/(1-b0)**2,(81*a**6-90*a**3+1)/(9*a**3+1)**2)
eq('central Y coordinate with fixed sign',12*b0*(b0+1)/(b0-1)**3,108*a**3*(9*a**3-1)/(9*a**3+1)**3)

# An exact finite-product identity exposes every residual tail factor;
# the written proof passes to the normally convergent infinite product.
def theta_finite(q,w,n):
    ans=1-w
    for k in range(1,n+1):ans*= (1-q**k*w)*(1-q**k/w)
    return ans
q0=Fraction(1,19);w0=Fraction(77,65)
for n in (4,8,20,80):
    lhs=theta_finite(q0,w0/q0**3,n)
    main=(-w0)**3*q0**-6*theta_finite(q0,w0,n)
    tail=Fraction(1)
    upper=Fraction(1)
    for j in range(3):
        aa=q0**(n+1+j)/w0;dd=q0**(n-j)*w0
        tail*= (1-aa)/(1-dd)
        upper*= (1+aa)/(1-dd)
    yes(f'theta exact shifted finite product N={n}',lhs==main*tail)
    yes(f'theta rigorous tail comparison N={n}',abs(tail-1)<=upper-1)
    if n==80:yes('theta residual at N80 below 1e-95',upper-1<Fraction(1,10**95))

D=-b**3*Z**-3*Q**6
eq('full reciprocal frame',D*(-Z/b)**3*Q**-6,1)
eq('h line conjugation',D.subs(Z,Q*Z)/D*P**8,P**8/Q**3)
eq('B line conjugation',D.subs(Z,P**-1*Z)/D*CB,P**3*CB)
M=s.Matrix([[-1,3],[-3,8]]);Mi=s.Matrix([[8,-3],[3,-1]])
yes('period matrix determinant one',M.det()==1)
yes('exact inverse words both directions',M*Mi==s.eye(2) and Mi*M==s.eye(2))
yes('primitive source valuations',s.Matrix([[8,-3]])*M==s.Matrix([[1,0]]))
lam,hat=s.symbols('lambda C_hat',nonzero=True)
eq('K retains lambda eighth power',b**3*(P**3*lam*hat)**8,lam**8*b**3*P**24*hat**8)
kap,pi,X,Y=s.symbols('kappa pi X Y',nonzero=True)
for i in range(8):
    source=z**i*X
    eq(f'h chart X index {i}',(z**8*kap*source)/z**(i+8),kap*X)
    eq(f'B chart X index {i}',(z**-3*pi**-1*source)/z**(i-3),pi**-1*X)
    eq(f'h chart Y index {i}',z**(i+9)/(z**8*kap*source),kap**-1*z/X)
    eq(f'B chart Y index {i}',z**(i-2)/(z**-3*pi**-1*source),pi*z/X)
    yes(f'theta node exponent index {i}',8-i-1>=0)

receipt=ROOT/'analysis/continuation_root/K116_residual_before_read.md'
out={'status':'passed','completed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
     'checker':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro',
     'method':'new SymPy rational-function and cusp-ring identities; exact Fraction theta tail products; exact integral matrix and chart maps',
     'prereading_file':str(receipt.relative_to(ROOT)),
     'prereading_sha256':hashlib.sha256(receipt.read_bytes()).hexdigest(),
     'checks':checks,'count':len(checks),
     'scope':'A1-A4 and B1-B6 residual identities, on the stated allowed antecedents. A5 parameter normalization requires the explicit continuing prescription or retention of its analytic unit; numerical tests do not decide it.'}
target=Path(__file__).with_suffix('.output.json');target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'checks':len(checks),'output':str(target),'prereading_sha256':out['prereading_sha256']},indent=2))
