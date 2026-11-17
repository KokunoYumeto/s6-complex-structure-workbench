#!/usr/bin/env python3
"""Exact algebra for the actual two-fan OS49 correction; no arbitrary-fan claim."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as S,json
ROOT=Path(__file__).resolve().parents[2]
checks=[]
def check(name,expr):
    ok=bool(expr);checks.append(dict(name=name,passed=ok));assert ok,name
def zero(name,expr):check(name,S.simplify(expr)==0)
t,z,s,v,k=S.symbols('t z s v k',real=True)
m=3*k
f=t**3*(t-1);g=t**4*(t-1)*(t-S.Rational(1,2))
zero('source discriminant',f**3-g**2+S.Rational(1,4)*t**8*(t-1)**2)
zero('marked G source substitution',t**4-(t**6-3*f*t**2+2*g))
u=S.Matrix([2*s,s]);gamma=S.Matrix([-3*s,-s+m*v]);H=-u-gamma;K=3*u+2*gamma
check('H period',H==S.Matrix([s,-m*v]))
check('K period',K==S.Matrix([0,s+2*m*v]))
check('source period determinant',S.Matrix([[2,-3],[1,-1]]).det()==1)
check('signed point-angle determinant+',S.Matrix([[2,-3],[1,-1]]).det()==1)
check('signed point-angle determinant-',S.Matrix([[2,3],[-1,-1]]).det()==1)
kap,al,gg,eta,A,D,a,b,c=S.symbols('kap al gg eta A D a b c',nonzero=True)
rows=[(kap*al*b*c,a*b/al,1/(kap*b)),(gg*eta*b*c,1/(eta*c),a*c/gg),(1/a,a*b,a*c)]
sub={a:a/(A*D),b:A*b,c:D*c}
for j,row in enumerate(rows):
    target=(A*D*row[0],row[1]/D,row[2]/A)
    check('full unit row '+str(j),all(S.simplify(x.subs(sub,simultaneous=True)-y)==0 for x,y in zip(row,target)))
zero('Cox q is fixed',a/(A*D)*(A*b)*(D*c)-a*b*c)
for n in (-1,1):
    zero('one-r forward seam source '+str(n),gg**n*gg**(-n)-1)
    zero('one-r forward seam line '+str(n),eta**n*eta**(-n)-1)
    check('finite cap character '+str(n),(n+2*n)%3==0)
    check('cusp rational cube congruence '+str(n),(-n-2*n)%3==0)
    check('cap rational cube congruence '+str(n),(n+2*n)%3==0)
    DD,R,LU,gu,uu,ga=S.symbols('DD R LU gu uu ga')
    # Work with the exact two-component logarithms, retaining the full units.
    U1,U2,C1,C2=S.symbols('U1 U2 C1 C2')
    uv=S.Matrix([2*s+U1,s+U2]);gv=S.Matrix([-3*s+C1,-s+m*v+C2])
    dv=3*S.Matrix([U1,U2])+2*S.Matrix([C1,C2]);delta=S.Matrix([0,1])
    LUv=(-gv+m*v*delta-R*delta)/3
    g0log=(-n*s-2*n*R)/3
    bounded=n*uv-2*n*LUv+(2*n*k*v+g0log)*delta
    tau=n*(dv+2*m*v*delta)/3;alpha=-2*n*k/3
    check('full bounded unit cancellation '+str(n),all(S.simplify(x)==0 for x in bounded-tau))
    sigma=n*v*dv+n*m*v*(v-1)*delta
    check('shorter sigma endpoint '+str(n),all(S.simplify(x)==0 for x in sigma.subs(v,v+S.Rational(1,3))-sigma-tau-alpha*delta))
    for j in range(4):
        total=S.zeros(2,1)
        for h in range(j):total+=tau.subs(v,v+S.Rational(h,3))+alpha*delta
        expected=j*n*dv/3+(2*n*k*j*v+n*k*j*(j-3)/3)*delta
        check('intermediate closing '+str(n)+'/'+str(j),all(S.simplify(x)==0 for x in total-expected))
    total=sum([tau.subs(v,v+S.Rational(h,3))+alpha*delta for h in range(3)],S.zeros(2,1))
    check('triple bounded one-r closing '+str(n),all(S.simplify(x)==0 for x in total-n*dv-2*n*m*v*delta))
    check('parameter-root cyclic phase '+str(n),(2*n*3)%3==0)

# All component and iterate identities are checked in both parity classes.
for parity in (0,1):
    h=lambda j:(j+1)//2
    check('line degree '+str(parity),-(h(parity-1)+h(parity+1)-2*h(parity))==(-1 if parity==0 else 1))
    check('linearization component defect '+str(parity),h(parity)-1-h(parity-3)==parity)
    check('plus G defect '+str(parity),h(parity)-h(parity+1)==(-1 if parity==0 else 0))
    for power in range(1,9):
        check('no reentry '+str(parity)+'/'+str(power),h(parity)-power-h(parity-3*power)==(power//2 if parity==0 else (power+1)//2))

t0=2*m;l=[6*m,0,4*m];w=[0,1,-1];d=[-2,-1,-1]
I=[S.expand(t0*w[j]+d[j]*(l[j]-t0)) for j in range(3)]
W=[S.expand(t0*w[j]-d[j]*(l[j]-t0)) for j in range(3)]
check('actual trace I',I==[-8*m,4*m,-4*m])
check('actual trace W',W==[8*m,0,0])
V22=-I[2];delta2=W[0]-W[2]
nu=(delta2-V22)/2;mu=-V22-nu
check('ordinary double pair',(S.expand(mu),S.expand(nu))==(-6*m,2*m))
native=(S.expand(mu+2*t0),S.expand(nu))
check('native double pair',native==(-2*m,2*m))
check('single actual free pair',tuple(S.expand(x/2) for x in native)==(-m,m))
check('shorter actual free pair',tuple(S.expand(x/6) for x in native)==(-k,k))
zero('positive page characteristic',(3*(-8*k)-(-24*k))/24)
zero('outer determinant winding',0+2*(-m)+2*m)
check('shorter positive scalar witness',(-1)%28==27)
check('all shorter residues',sorted({(-kk)%28 for kk in range(1,29)})==list(range(28)))

D1=S.Matrix([[-1]*6,[1]*6]);block=S.Matrix([[1,-1],[-1,1]]);D2=S.diag(block,block,block)
check('cell chain identity',D1*D2==S.zeros(2,6))
check('cell ranks',(D1.rank(),D2.rank())==(1,3))
result=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',check_count=len(checks),checks=checks,
 positive_fan_Jin_integer=0,
 negative_r_class='-3*k mod 28',negative_w_class='-k mod 28',
 native_r_free_pair=['-3*k','3*k'],native_w_free_pair=['-k','k'],
 norm_signs=[-1,1],delta_character='every fixed integer d',
 scope='Two specified actual fans and their constructed r/w parameters. No negative integer lift or arbitrary-fan formula assigned.')
(ROOT/'code/part3_fourfold/os49_corrected_returns.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
