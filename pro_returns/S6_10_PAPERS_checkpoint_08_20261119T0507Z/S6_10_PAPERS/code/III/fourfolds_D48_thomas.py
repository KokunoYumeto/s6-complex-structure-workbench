"""Symbolic full-coefficient Pontryagin-cube localization for D.2.48.

The geometric hypotheses (the chosen class and its component restrictions)
are stated and proved in the accompanying source.  This script proves the
integer polynomial identity for arbitrary d, not by a finite cutoff.
"""
from pathlib import Path
import json
import sympy as S

ROOT=Path(__file__).resolve().parent
d=S.symbols('d',integer=True,positive=True)
j,lam=S.symbols('j lam',integer=True)
x,t,r,s=S.symbols('x t r s')
psi=-r*(r-1)/2+3*s*(s-1)
weight_difference=S.expand(psi.subs({r:0,s:j+1})-psi.subs({r:0,s:j}))
assert weight_difference==6*j
euler=S.expand((-x+t)*(-x-t))
assert euler==x*x-t*t
cube=S.expand((x+lam*t)**3)
contribution=S.cancel(cube.coeff(x,1)/(-t*t))
assert contribution==-3*lam*lam

identities=[]
for sign in (-1,1):
    total=S.simplify(S.summation((lam+sign*6*j)**2,(j,0,d-1)))
    quotient=S.expand(lam**2+sign*6*lam*(d-1)+6*(d-1)*(2*d-1))
    assert S.expand(total-d*quotient)==0
    value=-3*total
    assert S.expand(value/(3*d)+quotient)==0
    # Every coefficient is integral, so this is divisibility for all integers.
    assert all(c.q==1 for c in S.Poly(quotient,d,lam).coeffs())
    identities.append(dict(sign=sign,sum_of_squared_weights=str(total),
                           integer_quotient=str(quotient),
                           Pontryagin_cube_value=str(S.expand(value))))
    print('SIGN',sign,'sum/d =',quotient,'; P3/(3d) =',-quotient,flush=True)

# Explicit checks are supplementary; no bound is used in the proof.
checks=0
for degree in range(3,121,3):
    for origin in range(degree):
        for sign in (-1,1):
            weights=[origin+sign*6*k for k in range(degree)]
            assert (-3*sum(w*w for w in weights))%(3*degree)==0
            checks+=1
assert checks==4920
record=dict(scope=__doc__,support=str(psi),fixed_curve_weight=str(weight_difference),
            normal_euler=str(euler),single_curve_contribution=str(contribution),
            all_integer_identities=identities,bounded_supplementary_checks=checks,
            supplementary_bound='d=3,6,...,120; lambda0=0,...,d-1; both signs',
            full_target='Z/(3d) for every positive d divisible by3',
            result='Full Pontryagin-cube evaluation zero, conditional only on the proved geometric hypotheses')
(ROOT/'fourfolds_D48_thomas.json').write_text(json.dumps(record,indent=2)+'\n')
print('PASS: two universal integer identities and',checks,'supplementary exact checks')
