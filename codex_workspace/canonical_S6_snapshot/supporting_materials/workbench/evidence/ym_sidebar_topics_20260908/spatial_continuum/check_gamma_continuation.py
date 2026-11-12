"""Exact finite diagnostics for the actual electric graph and pair spectrum.

The complete operator, state, measure and limit proofs are in the manuscript
and its retained source proofs. This script does not assert continuum
existence, a uniform small-coupling remainder, or a mass-gap counterexample.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib, json
import sympy as s

ROOT=Path(__file__).resolve().parent
checks=[]
groups=Counter()

def check(group,name,condition):
    if not bool(condition): raise AssertionError((group,name))
    checks.append(group+': '+name);groups[group]+=1

def same(group,name,a,b):
    check(group,name,s.cancel(a-b)==0)

for L in range(2,9):
    N=6*L*(2*L+1)**2
    M=12*L**2*(2*L+1)
    rank=16*L**3+12*L**2
    A=0;S=0;incidence=0
    for n in product(range(-L,L+1),repeat=3):
        for axis in range(3):
            if n[axis]==L:continue
            r=sum(1 if n[k] in (-L,L) else 2 for k in range(3) if k!=axis)
            incidence+=r
            if axis==0:
                S+=n[1]**2;A+=r*n[1]**2
    exactA=F(4,3)*L**2*(2*L+1)*(4*L**2+2*L+1)
    check('lattice',f'L={L} retained incidence sum',incidence==4*M)
    check('lattice',f'L={L} exact transverse rank',rank==N-(2*L+1)**3+1)
    check('lattice',f'L={L} full original weighted incidence',A==exactA)
    check('lattice',f'L={L} exact coordinate weight sum',S==F(2,3)*L**2*(L+1)*(2*L+1)**2)
    check('lattice',f'L={L} rank upper bound',rank<=22*L**3)
    check('lattice',f'L={L} weighted incidence lower bound',A>=F(32,3)*L**5)
    check('lattice',f'L={L} covariance trace lower constant',F(A*A,12*rank)>=F(128,297)*L**7)
    for K in range(0,2*L+1):
        count=sum(max(0,sum(t>0 for t in triple)-1) for triple in product(range(K+1),repeat=3))
        check('rank_count',f'L={L},K={K} complete multiplicity',count==3*K*K+2*K**3)

L=s.symbols('L',positive=True)
exactA=s.Rational(4,3)*L**2*(2*L+1)*(4*L**2+2*L+1)
same('symbolic','weighted incidence summation',
     2*L*((2*L+1)*s.Rational(2,3)*L*(2*L**2+1)+4*L*L*(L+1)*(2*L+1)/3),exactA)
same('symbolic','rank majorant factor',22*L**3-(16*L**3+12*L**2),6*L**2*(L-2))
check('constants','trace lower bound',F(32,3)**2/(12*22)==F(128,297))
check('constants','raw covariance lower bound',F(3,32)*F(128,297)==F(4,99))
check('constants','raw covariance upper bound',F(3,32)*12*22==F(99,4))
check('constants','probability reciprocal',1/F(128,297)==F(297,128))
check('constants','diagonal color-pair norm coefficient',F(1,8)**2*6==F(3,32))
check('constants','off-diagonal color-pair norm coefficient',F(1,4)**2*3==F(3,16))
check('constants','whole covariance state factor',F(3,16)==2*F(3,32))

# Direct exact Gaussian integration for every entry of a symmetric
# two-spatial-mode kinetic matrix, including all three original colors.
u,v=s.symbols('u v',positive=True)
d11,d12,d22=s.symbols('d11 d12 d22',real=True)
xs=s.symbols('x0:6',real=True)
variances=[2/u,2/v]*3
poly=0
for c in range(3):
    x,y=xs[2*c:2*c+2]
    poly-=s.Rational(1,16)*(u*u*d11*x*x+2*u*v*d12*x*y+v*v*d22*y*y-2*(u*d11+v*d22))
def mean_polynomial(p):
    ans=0
    for powers,coef in s.Poly(s.expand(p),*xs).terms():
        moment=coef
        for power,var in zip(powers,variances):
            if power%2:moment=0;break
            if power:moment*=s.factorial2(power-1)*var**(power//2)
        ans+=moment
    return s.expand(ans)
same('gaussian','all-color centered mean',mean_polynomial(poly),0)
expected=s.Rational(3,32)*(u*u*d11*d11+2*u*v*d12*d12+v*v*d22*d22)
same('gaussian','all-color raw covariance exact norm',mean_polynomial(poly*poly),expected)
same('gaussian','full diagonal/off-diagonal mass sum',
     s.Rational(3,32)*(u*u*d11*d11+v*v*d22*d22)+s.Rational(3,16)*u*v*d12*d12,expected)

# Exact scaled potential moment recursion, including the original
# kappa=2g^2/a and b=1/(2g^2 a) coefficients.
a,g,E,eps=s.symbols('a g E eps',positive=True)
k=s.symbols('k',integer=True,positive=True)
mk,mprev=s.symbols('mk mprev')
kappa=2*g*g/a;b=1/(2*g*g*a)
rhs=(E*g**(2*k)*mk+4*kappa*k*k*g**(2*k-2)*mprev)/(b*g**(2*k+2))
same('moments','original coefficient recursion',rhs,2*a*E*mk+16*k*k*mprev)
same('moments','explicit energy factor',2*a*(3*s.sqrt(7)/a),6*s.sqrt(7))
B0=1;B1=4*eps
B2=4*eps*B1+16*B0
B3=4*eps*B2+64*B1
same('moments','explicit second moment constant',B2,16*eps**2+16)
same('moments','explicit third moment constant',B3,64*eps**3+320*eps)

j,x,q,C=s.symbols('j x q C',positive=True)
xi=x**4
factor=x**3*(6+64*x**4)
Ll=j*j;Ml=12*j**4*(2*j*j+1)
# Formally q=exp(8*pi xi), x=xi^(1/4); theta/pi is bounded as written.
angle_squared_without_pi2=4/(10**8*j**20*q**4*factor)
lower_sigma=xi*q**-4*(Ll+1)*(2*Ll+1)/(24*(6+64*xi))
Btwo=15*x**7*Ml**2
eta_without_pi2=angle_squared_without_pi2*Ll**4*Btwo/(3*lower_sigma)
same('cusp','full coupling factor cancels in relative error',eta_without_pi2,
     s.Rational(69120,10**8)*j**-4*(2*j*j+1)/(j*j+1))
same('cusp','raw norm coupling factor retained',x**3/factor,1/(6+64*x**4))
same('cusp','selected-dyadic physical scalar coefficient',
     2*(50*j*q**2)*Ml,100*j*q**2*Ml)
same('rates','finite-energy lower-rank power',j**-2*j**-6*j**2,j**-6)
same('rates','finite-energy upper-rank power',j**-2*j**-6*j**3,j**-5)

report={'status':'passed','exact_assertions':len(checks),'groups':dict(groups),
 'scope':'Finite exact incidence/rank counts, Gaussian pair-state integration, raw amplitudes, coefficient recursions and cusp cancellations. General operator and limit proofs are in the complete manuscript and retained companion sources.',
 'not_established_by_script':['an interacting four-dimensional continuum','a uniform-volume error for the small-g graph limit','nonzero limiting native low-energy weight','a Yang-Mills mass-gap counterexample'],
 'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in [Path(__file__).name,'spatial_continuum.md']},
 'passed_assertions':checks}
(ROOT/'GAMMA_CONTINUATION_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:report[k] for k in ['status','exact_assertions','groups','scope']},indent=2))
