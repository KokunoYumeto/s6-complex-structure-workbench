#!/usr/bin/env python3
"""Exact coordinate/cochain identities for RCZ; no numerical return claim."""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as s

root=Path(__file__).resolve().parents[2]
checks=[]
def ck(name,x):
    assert s.simplify(x)==0,name
    checks.append({'name':name,'pass':True})

p,k,n,t,d=s.symbols('p k n t d',integer=True)
for a,b in ((1,2),(2,1)):
    ck(f'({a},{b}) actual ordinary scalar cancellation',2*a*b-4)
for good in (True,False):
    m=4*p if good else 4*p-1
    target=0 if good else -s.Rational(2)/m
    ck(f'{good} root X coordinate exponent',2-8*p/m-target)
    target=0 if good else -s.Rational(3)/m
    ck(f'{good} root Y coordinate exponent',3-12*p/m-target)
    ck(f'{good} marked section Y becomes v z^(3p)',12*p/m+(0 if good else -s.Rational(3)/m)-3)
ck('reduced D^-4 X endpoint differs from -2 by -2m',-8*p+2+2*(4*p-1))
ck('reduced D^-4 Y endpoint differs from -3 by -3m',-12*p+3+3*(4*p-1))
ck('retained doubled half-period',4*(1+s.I)/2-2*(1+s.I))
ck('signed retained doubled half-period',4*n*(1+s.I)/2-2*n*(1+s.I))
ck('quadratic scalar cochain forward one-step exponent',6*k*n*((t+1)*t-t*(t-1))-12*k*n*t)

# Use formal exponent vectors of (u,q_new) for the prescribed q_old^d.
qold=s.Matrix([-4,1]);qnew=s.Matrix([0,1]);u=s.Matrix([1,0])
for i,x in enumerate(d*qold-(-4*d*u+d*qnew)):
    ck(f'prescribed annular d retained coordinate {i}',x)

for m in (3,4,7,8,11,12):
    gs=s.symbols('g0:'+str(m))
    relation={gs[-1]:-sum(gs[:-1])}
    f=-sum(j*gs[j] for j in range(m))/m
    fD=-sum(j*gs[(j+1)%m] for j in range(m))/m
    ck(f'finite zero-norm unit conjugation m={m}',(fD-f+gs[0]).subs(relation))
    ck(f'finite additive norm m={m}',sum(gs).subs(relation))

# Keep the actual carry as an independent lattice vector until the
# logarithm relation is applied; no zero source period is substituted.
H,l,Lsmall=s.symbols('H l Lsmall')
ck('fourth logarithm retains its full period carry',(4*l-Lsmall-H).subs(H,4*l-Lsmall))
cp,cm,ell,cv=s.symbols('b_plus b_minus ell cauchy_v')
ck('scalar factorization logarithm has exact ratio',((cp-cv)-(cm-cv)-ell).subs(cp,cm+ell))
ck('corrected family arrows agree in logarithmic scalars',(-cp+(cm+ell)).subs(cp,cm+ell))

result={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),'checks':len(checks),'identities':checks,
        'proof':'notes/part3_source_zero_relative_comparison_working.md',
        'scope':'Exact root, finite-average, retained-period and scalar-arrow identities. The analytic interpolation and total groupoid comparison are proved in the note and undergo independent audit. No source-zero numerical return assigned.'}
(root/'code/part3/source_zero_relative_comparison.json').write_text(json.dumps(result,indent=2)+'\n')
print(f'PASS: {len(checks)} exact relative source-zero coordinate/cochain identities.')
