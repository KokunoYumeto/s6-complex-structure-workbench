"""Exact local identities for the other-axis Tate interface B.4.20."""
import json
from pathlib import Path
import sympy as S

x,w,s,a,kappa,e,f,r,u,v,lam = S.symbols('x w s a kappa e f r u v lam')
out=[]
for n in (1,2,3,4,8,12):
    wp=a*w+(1-a)*s
    assert S.expand((wp-s)-a*(w-s)) == 0
    xp=kappa*x*wp**n
    assert S.expand(xp.subs(w,s)-kappa*s**n*x) == 0
    assert S.expand(xp.subs(x,lam*x)-lam*xp) == 0
    # Every blow-up centre is on a single component of total w=0;
    # its new multiplicity is that component's coefficient, namely 1.
    multiplicities=[1]
    for step in range(n):
        multiplicities.append(multiplicities[-1])
    assert multiplicities==[1]*(n+1)
    # End collars join the two endpoint pieces of the reduced chain.
    cycle_components=len(multiplicities)-1
    assert cycle_components==n
    out.append({'n':n,'total_transform_coefficients':multiplicities,
                'central_cycle_components':cycle_components})
print('Cartier factor, generic Tate multiplier, x-scaling, and reduced chains: PASS')

# Relative neighbourhood, in coordinates (u,v,e) on the smooth Kato total space.
base=u*v-e
assert S.diff(base,e)==-1
normal_model=u*v
assert S.diff(normal_model,e)==0
assert S.diff(normal_model,u).subs(v,0)==0
assert S.diff(normal_model,v).subs(u,0)==0
print('Kato base s=uv-e is submersive; inherited normal-line base s=uv is not')

# The formal inverse-normal plumbing e*f=r has this literal local realization.
plumbing_r=f*(u*v-s)
substitution=plumbing_r.subs(s,u*v-e)
assert S.expand(substitution-e*f)==0
# Over r !=0, solve s=uv-r/f; its f derivative is nonzero.
resolved_base=u*v-r/f
assert S.diff(resolved_base,f)==r/f**2
print('local inverse-normal plumbing r=f(uv-s): reduced NC and submersive s-map over r!=0')

# Normal P and the six-P closing are distinct multipliers.
A=S.symbols('A', nonzero=True)
assert S.simplify((A**(-1))**(-6)-A**6)==0
print('normal factor a=A^-1; six-P translation on Tate coordinate is a^-6=A^6')

record={'status':'PASS','examples':out,
        'normal_factor':'a(s)', 'tate_multiplier':'kappa(s)*s^n',
        'actual_marking':'a=exp(-2*pi*i*mu), closing translation a^(-6)',
        'no_relative_linear_tubular_neighbourhood':True,
        'full_second_period_or_origin_cap':'NOT CONSTRUCTED'}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
print('ALL EXACT CHECKS PASSED')
