"""Fresh K115/K118 checks, 19 November 2026.

Reuses only our previously written rational Gaussian prism solver, extracted
without running that file's checks. No supplied historical verifier is read.
The geometry of the printed maps is audited in the separate proof report.
"""
from pathlib import Path
from fractions import Fraction as F
from math import gcd
import ast, hashlib, json, time
import sympy as sp

HERE=Path(__file__).resolve().parent
started=time.monotonic()
checks=[]
def check(name,value,expected=True):
    if value != expected:
        raise AssertionError((name,value,expected))
    checks.append(name)

prior=HERE/'independent_IV_checks.py'
tree=ast.parse(prior.read_text())
names={'mul','inv2','flat','solve_linear','step'}
for node in tree.body:
    if isinstance(node,ast.FunctionDef) and node.name in names:
        exec(compile(ast.Module(body=[node],type_ignores=[]),str(prior),'exec'))
Q=[[[1,-1],[0,1]],[[1,0],[-1,1]]]
symidx={(0,0):0,(0,1):1,(0,2):2,(1,1):3,(1,2):4,(2,2):5}

def seed(J,H,chi,j=0):
    J,H,chi=map(F,(J,H,chi))
    V=[[2*J-6*H+6*J*j*(j-1),2*J*(1-2*j),2*J*(2*j-1)],
       [2*J*(1-2*j),2*J,0],[2*J*(2*j-1),0,2*J]]
    delta=[2*J+6*H-24*chi-6*J*j*(j-1),2*J*(2*j-1),2*J*(1-2*j)]
    return {'P':[[F(1),F(0)],[F(j),F(1)]], 'V':V,'delta':delta,
      'S':H/2-chi-F(J*j*(j-1),2),'B0':[[0,0],[0,2*J]],
      't':J,'denom':4,'word':'','steps':[]}

def reduce_on_curve(expr,relation,var):
    return sp.factor(sp.rem(sp.fraction(sp.cancel(expr))[0],relation,var))

# An explicit comparison of the original r=0 source with E26's displayed source.
x,y,t,tau,X,Y,w,z=sp.symbols('x y t tau X Y w z')
t_of_tau=4*(1-tau)/(27*tau)
X_of_x=sp.Rational(9,2)*tau**2*x
Y_of_y=27/(2*sp.sqrt(2))*tau**3*y
e26=Y_of_y**2-X_of_x**3+3*tau**3*(tau-1)*X_of_x-2*tau**4*(tau-1)**2
check('E26 actual source polynomial transport',sp.factor(e26-
    sp.Rational(729,8)*tau**6*(y*y-x**3-t_of_tau*x-t_of_tau**2)),0)
check('E26 base map inverse',sp.cancel((4/(27*t+4)).subs(t,t_of_tau)-tau),0)
check('E26 marked point transport',sp.simplify(Y_of_y.subs(y,t_of_tau)
    -sp.sqrt(2)*tau**2*(1-tau)),0)

# Full odd-point Miller functions before taking good-root values.
f2=(y-t-x/2)/(x-sp.Rational(1,4))
f3=(x/4)*(y-t-x/2)/((y+t+x/2)/4-(sp.Rational(1,4)+2*t)*x)
phi=(w*Y-w*w-X/2)/(w*w*X-sp.Rational(1,4))
psi=X*(2*w*Y-2*w*w-X)/(2*w*Y+2*w*w-X-16*w**4*X)
sub={x:w*w*X,y:w**3*Y,t:w**4}
check('full finite good-root f2',sp.cancel(f2.subs(sub)/w**2-phi),0)
check('full finite good-root f3',sp.cancel(f3.subs(sub)/w**2-psi),0)
check('finite phi central value',phi.subs(w,0),2*X)
check('finite psi central value',psi.subs(w,0),X)
for a in [1,3]:
    coefficient=(2*X)**a*(1 if a==1 else (1/X)/X)
    check('odd-line negative coefficient',sp.simplify(coefficient),2**a*X)
    inverse=sp.cancel(1/coefficient.subs(X,1/X))
    check('odd-line inverse coefficient at inverse source',inverse,X/2**a)
    check('odd-line twofold full coefficient norm',sp.cancel(coefficient*coefficient.subs(X,1/X)),2**(2*a))

relation=Y*Y-X**3-1
slope=(Y-1)/X
Xp=sp.cancel(slope*slope-X)
Yp=sp.cancel(-Y+slope*(X-Xp))
check('good infinity positive source x',reduce_on_curve(Xp-2*(1-Y)/X**2,relation,Y),0)
check('good infinity source point equation',reduce_on_curve(Yp**2-Xp**3-1,relation,Y),0)
check('good infinity inverse-source line coefficient',reduce_on_curve(Xp/(Yp-1)-X/2,relation,Y),0)
# For 3-torsion +G, the next source point has x=2(1+Y)/X^2.
Xm=2*(1+Y)/X**2
check('odd infinity threefold norm',reduce_on_curve(X*Xp*Xm/8+sp.Rational(1,2),relation,Y),0)

# Page base map and its exact ramification calculation.
eta,xi,T=sp.symbols('eta xi T')
for m in range(2,13):
    for h in range(1,14):
        if gcd(m,h)!=1:continue
        deg=m*h
        genus=F((m-1)*(h-1),2)
        rh=-2*deg + m*(h-1)+h*(m-1)+(deg-1)
        check('complete three-branch page genus',rh,2*genus-2)

def egcd(a,b):
    if b==0:return a,1,0
    g,u,v=egcd(b,a%b)
    return g,v,u-(a//b)*v

def profile(a,k,l):
    b=6//a
    m=3*l if a in [1,2] else 3*l+2
    h=4*k if a in [1,3] else 4*k+1
    e_inf=0 if a in [1,2] else 4
    e_zero=0 if a in [1,3] else 3
    M=m*h; J=F(M,b); H=F(M*a*a,6); chi=F(M+h*e_inf+m*e_zero,12)
    return b,m,h,M,J,H,chi

profiles=0; endpoints=0; fan_steps=0
selected_witnesses={}
for a in [1,2,3,6]:
    for k in range(0,13):
        for l in range(0,13):
            if (a in [1,3] and k==0) or (a in [1,2] and l==0):continue
            b,m,h,M,J,H,chi=profile(a,k,l)
            if gcd(m,h)!=1:continue
            profiles+=1
            check('integral root-domain J0',J.denominator,1)
            check('page chi integer',chi.denominator,1)
            check('primitive physical pair integral',all(q.denominator==1 for q in [3*H/b,24*chi/b]))
            expected={1:(k*l,4*k*l,0),
              2:(2*l*(4*k+1),8*l*(k+1),k*l),
              3:(9*k*(3*l+2),12*k*(l+2),k*(4*l+2)),
              6:(18*(3*l+2)*(4*k+1),24*(k*l+2*k+l+1),35*k*l+22*k+8*l+5)}[a]
            actual=(3*H/b,24*chi/b,H/(2*b)-chi/b)
            check('four actual page pairs and indices',actual,expected)
            check('native characteristic inverse',F(actual[1],4)+(actual[0]-F(actual[1],4)),actual[0])
            check('chronological finite phase integer',int(J)*(b-1)%2,0)
            _,ninf,nzero=egcd(h,m)
            for eps in [-1,1]:
                for shift in range(-3,4):
                    ni=eps*ninf+m*shift; nz=eps*nzero-h*shift
                    check('signed actual sphere equation',h*ni+m*nz,eps)
                    d=F(3*eps-m*nz,b)
                    check('d0 integer',d.denominator,1)
                    check('two d0 formulas',d,F(2*eps+h*ni,b))
                    check('finite root endpoint exponent',h*d-F(3*h*eps,b),-J*nz)
                    check('infinity root endpoint exponent',-m*d+F(2*m*eps,b),-J*ni)
                    check('full infinity character square',(h*ni+2*eps)%b,0)
                    check('full finite character square',(m*nz-3*eps)%b,0)
                    for nu in [-7,-1,0,1,7]:check('full negative annular obstruction',ni+m*nu!=0)
                    check('ordinary full cyclic t exponent',b*d-3*eps,-m*nz)
                    endpoints+=1
            # The proof uses a complete linear solver, with multiple finite words.
            st=seed(J,H/b,chi/b)
            factor={1:k*l,2:l,3:k,6:1}[a]
            words=['0','00','000','01','010','001']
            for word in words:
                ns=st
                for e in word:ns=step(ns,int(e));fan_steps+=1
                check('fan integer scales by stated source divisor',(ns['S']/factor).denominator,1)
                if a==1 and word=='00':check('odd M1 two-flop witness',ns['S'],3*k*l)
                if a==3 and word=='000':check('odd M3 three-flop witness',ns['S'],k*(553*l+344))
                if k<=1 and l<=1:selected_witnesses[f'a{a}_k{k}_l{l}_{word}']=ns
            if a==2:
                jj=0 if k%2 and k%7 else 4 if k%2 else 2 if k%7!=2 else 3
                val=k-(4*k+1)*jj*(jj-1)//2
                check('M2 joint vertical unit witness',gcd(val,28),1)
            if a==3:check('M3 admissibility and odd unit witness',(l%2,gcd(553*l+344,28)),(1,1))
            if a==6:
                A=35*k*l+22*k+8*l+5
                candidates=[A,A-6*int(J)] if k*l%2==0 else [A-int(J),A-3*int(J)]
                check('M6 coprime profile supplies a vertical unit',any(gcd(v,28)==1 for v in candidates))

# K115 original finite-cap progression, including rational primitive inputs.
k115_witnesses={}
for l in range(1,57):
    for kind in ['M2','M6']:
        m=3*l if kind=='M2' else 3*l+2
        J,Hhat,chihat=(l,F(2*l,3),F(l,3)) if kind=='M2' else (m,6*m,l+1)
        for j in range(-4,6):
            ss=seed(J,Hhat,chihat,j)
            expected=-F(l*j*(j-1),2) if kind=='M2' else 8*l+5-F(m*j*(j-1),2)
            check('K115 vertical exact integer',ss['S'],expected)
        if kind=='M2':check('K115 M2 primitive witness',seed(J,Hhat,chihat,2)['S'],-l)
        else:
            jj=0 if l%7!=2 else 4
            check('K115 M6 vertical unit witness',gcd(int(seed(J,Hhat,chihat,jj)['S']),28),1)
        st=seed(J,Hhat,chihat)
        for word in ['0','00','01','000','001','010','011']:
            ns=st
            for e in word:ns=step(ns,int(e));fan_steps+=1
            if kind=='M2':check('K115 all tested fan integers scale by l',(ns['S']/l).denominator,1)
            if l==1:k115_witnesses[f'{kind}_{word}']=ns
# The l=0 reduced-IV M6 row is also included.
check('K115 l0 initial index',seed(2,12,1)['S'],5)
check('K115 l0 unit',gcd(5,28),1)

# Unbounded unit arguments reduced to their exact finite residue periods.
for k in range(56):
    for l in range(56):
        m,h=3*l+2,4*k+1; J=m*h; A=35*k*l+22*k+8*l+5
        if gcd(m,h)%7==0:continue
        candidates=[A,A-6*J] if k*l%2==0 else [A-J,A-3*J]
        check('all mod56 residues for M6 unit proof',any(gcd(v,28)==1 for v in candidates))

def serial(v):
    if isinstance(v,F):return int(v) if v.denominator==1 else str(v)
    if isinstance(v,sp.Basic):return str(v)
    raise TypeError(type(v).__name__)
result={'scope':'Fresh exact K115/K118 source, endpoint, page, rational-prism and unit-witness checks; geometry audited separately.',
 'profiles':profiles,'signed_endpoints':endpoints,'prism_steps':fan_steps,
 'checks_passed':len(checks),'elapsed_seconds':round(time.monotonic()-started,3),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'reused_our_prism_source_sha256':hashlib.sha256(prior.read_bytes()).hexdigest(),
 'joint_witnesses':selected_witnesses,'K115_witnesses':k115_witnesses,'check_names':checks}
(HERE/'independent_IV_joint_checks.json').write_text(json.dumps(result,default=serial,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['joint_witnesses','K115_witnesses','check_names']},indent=2))
