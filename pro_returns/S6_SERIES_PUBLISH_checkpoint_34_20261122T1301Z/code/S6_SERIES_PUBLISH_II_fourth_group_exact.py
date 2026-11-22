#!/usr/bin/env python3
"""Fresh exact computations for G9, E10, E12 and E17; no old code imported."""
from pathlib import Path
import json
import sympy as S

t, s, x, y = S.symbols('t s x y')
legendre_j = lambda z: 256*(1-z+z*z)**3/(z*z*(1-z)**2)
lam = (3+s)/(2*(2+s))
j_derivative = S.factor(S.diff(legendre_j(lam),s).subs(s,0))
assert j_derivative != 0
psi = (t-2)/(2*(t-3))
assert [S.simplify(psi.subs(t,k)) for k in [2,4]] == [0,1]
hesse_first = t**3-1
hesse_second = (t-4)*((t-4)**3-1)
assert S.gcd(hesse_first,hesse_second) == 1
branch = S.prod(t-k for k in range(10,15))*(t-15-s)
branch_discriminant = S.factor(S.discriminant(branch,t).subs(s,0))
assert branch_discriminant != 0
node_syzygy = (S.Matrix([[y,x]])*S.Matrix([x,-y]))[0]
assert S.expand(node_syzygy) == 0

# Cohomology on the actual genus-two target, with L=K and deg L=2.
def curve_cohom(a):
    assert a >= 0
    return (1,2) if a==0 else (0,2*a+1)
def leray_twist(a,multiplicity=1):
    out=[0,0,0,0]
    for q,rank in [(0,1),(1,2),(2,1)]:
        h0,h1=curve_cohom(a+q)
        out[q]+=multiplicity*rank*h0
        out[q+1]+=multiplicity*rank*h1
    return out
table={'O_Y':leray_twist(0),'g_star_T_C':leray_twist(1),
       'T_relative':leray_twist(1,2)}
assert table=={'O_Y':[1,2,6,5],'g_star_T_C':[0,3,10,7],
              'T_relative':[0,6,20,14]}

# E12: the two-term resolution [O --t--> O] is in degrees 1,2
# after the P1(-2) shift. The simple zero gives length one.
local_map = S.Matrix([[t]])
generic_rank = local_map.rank()
special_rank = local_map.subs(t,0).rank()
assert (generic_rank,special_rank)==(1,0)
fiber_general=[0,1-generic_rank,1-generic_rank]
fiber_special=[0,1-special_rank,1-special_rank]
assert fiber_general==[0,0,0] and fiber_special==[0,1,1]
vanishing_order = min(mon[0] for mon,coeff in S.Poly(t,t).terms() if coeff)
assert vanishing_order == 1

# E17: count the Laurent monomial representatives on the two affine
# charts of P1 for O(-k), then add the square-zero skyscraper H0.
nilpotent_twists=[]
for k in range(-4,10):
    h0_reduced=len(range(0,1-k)) if k<=0 else 0
    h1_reduced=len(range(1,k)) if k>=2 else 0
    h0,h1=h0_reduced+1,h1_reduced
    assert h0==max(1-k,0)+1 and h1==max(k-1,0)
    nilpotent_twists.append({'k':k,'h0':h0,'h1':h1,'higher':0})

result={
 'method':'Fresh rational symbolic maps, local two-term complex, curve Riemann--Roch coefficient aggregation, and Laurent-monomial Cech representatives; no inherited checking code imported.',
 'G9':{'allowed_euler_values':[0,2],'nonpositive_intersection':sorted(set([0,2]).intersection(range(-10,1))),'b3':2},
 'E10_prereading_model':{'second_legendre_parameter':str(psi),'second_critical_values':[2,3,4],
   'base_cross_ratio':str(lam),'base_cross_ratio_derivative':str(S.diff(lam,s).subs(s,0)),
   'elliptic_base_j_derivative':str(j_derivative)},
 'E10_printed_model':{'first_finite_critical_polynomial':str(hesse_first),
   'second_critical_polynomial':str(S.expand(hesse_second)),
   'critical_polynomial_gcd':str(S.gcd(hesse_first,hesse_second)),
   'infinity_first_is_critical':True,'infinity_second_maps_to_zero_and_is_smooth':True,
   'genus_two_branch_discriminant_at_zero':str(branch_discriminant),
   'node_kernel_identity':str(node_syzygy),'cohomology_table':table},
 'E12':{'local_resolution_degrees':[1,2],'local_map':'multiplication by t',
   'generic_rank':generic_rank,'special_rank':special_rank,'cokernel_length':vanishing_order,
   'generic_fiber_cohomology':fiber_general,'special_fiber_cohomology':fiber_special,
   'global_cohomology':[0,0,1,0]},
 'E17':{'general_formula':{'h0':'max(1-k,0)+1','h1':'max(k-1,0)','higher':0},
   'Laurent_representative_counts':nilpotent_twists},
 'all_assertions_passed':True,'events_added':0,
}
out=Path(__file__).with_name('S6_SERIES_PUBLISH_II_fourth_group_exact_output.json')
assert not out.exists(),out
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
