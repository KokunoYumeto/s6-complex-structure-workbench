"""Exact logarithmic-origin comparison for the positive OS47 r-loop.

The local characters are Z=exp(2*pi*i*zeta1), V=exp(2*pi*i*zeta2).
Scalar lambda=r**4, and the positive deck has ordinary translation -s*delta.
"""
from pathlib import Path
import json
import sympy as sp

s, v, theta, Gamma, C = sp.symbols('s v theta Gamma C')
delta = sp.Matrix([0, 1])
gamma = sp.Matrix([Gamma, C+s+4*v])
ordinary = sp.Matrix([-Gamma*s/4, -C*s/4-s*s/8-s*v])
cusp = sp.Matrix([Gamma*v, C*v+2*v*v-2*v])
F = sp.simplify(cusp-ordinary)

def change(expr, var, amount):
    return sp.simplify(expr.subs(var,var+amount)-expr)

checks = {
    'ordinary_parameter_deck': change(ordinary,v,1)+s*delta,
    'cusp_parameter_deck': change(cusp,v,1)-gamma+s*delta,
    'ordinary_Q_deck': change(ordinary,s,4)+gamma+2*delta,
    'cusp_Q_deck': change(cusp,s,4),
    'angular_clutch': change(F,v,theta)-theta*gamma-2*theta*(theta-1)*delta,
    'Q_angular_gauge': change(change(F,v,theta),s,4)-4*theta*delta,
}
assert all(all(sp.expand(x)==0 for x in vec) for vec in checks.values())
assert sp.simplify(2*theta*(theta-1)).subs(theta,0)==0
assert sp.simplify(2*theta*(theta-1)).subs(theta,1)==0
data = {
    'character': 'V=exp(2*pi*i*zeta2)',
    'scalar': 'lambda=r**4',
    'positive_deck': '(v,zeta)->(v+1,zeta-s*delta)',
    'inverse_closing_multiplier': 'h(t)=t-t_c',
    'gamma': [str(x) for x in gamma],
    'ordinary_origin': [str(x) for x in ordinary],
    'cusp_origin': [str(x) for x in cusp],
    'difference': [str(sp.expand(x)) for x in F],
    'angular_difference': [str(sp.expand(x)) for x in change(F,v,theta)],
    'gamma_coefficient': 1,
    'Q_deck_gauge_winding': 4,
    'checks': {name:[str(x) for x in value] for name,value in checks.items()},
}
Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
for key,value in data.items():
    print(f'{key}: {value}')
