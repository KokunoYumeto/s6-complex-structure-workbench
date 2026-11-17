#!/usr/bin/env python3
"""Signed one-turn origin comparison for the order-one smooth log cap."""
from pathlib import Path
import json
import sympy as sp

s,v,theta,Gamma,C=sp.symbols('s v theta Gamma C')
delta=sp.Matrix([0,1])
gamma=sp.Matrix([Gamma,C+s+v])
ordinary=sp.Matrix([-Gamma*s,-C*s-s*s/2-s*v])
cusp=sp.Matrix([Gamma*v,C*v+(v*v-v)/2])
F=sp.simplify(cusp-ordinary)
def change(expr,var,amount):return sp.simplify(expr.subs(var,var+amount)-expr)
checks={
 'ordinary_parameter_deck':change(ordinary,v,1)+s*delta,
 'cusp_parameter_deck':change(cusp,v,1)-gamma+s*delta,
 'ordinary_double_cusp_deck':change(ordinary,s,2)+2*gamma+2*delta,
 'cusp_double_cusp_deck':change(cusp,s,2),
 'angular_clutch':change(F,v,theta)-theta*gamma-theta*(theta-1)*delta/2,
 'double_cusp_angular_gauge':change(change(F,v,theta),s,2)-2*theta*delta}
assert all(all(sp.expand(x)==0 for x in vec) for vec in checks.values())
data={
 'scalar_parameter':'lambda=exp(2*pi*i*v), with no parameter cover',
 'smooth_log_site':'t=0',
 'cusp_site':'any simple root t_c of 48t^4+8t^3+96t^2+72t+57',
 'global_closing_function':'h(t)=(t-t_c)/t',
 'local_cusp_coordinate':'q=h(t), s=log(q)/(2*pi*i)',
 'ordinary_positive_parameter_deck':'zeta -> zeta-s*delta',
 'smooth_log_gluing':'zeta_out=zeta_in+log(t)/(2*pi*i)*gamma(t,v)',
 'cusp_cover_for_origins_only':'q=Q^2; no proper descended corner is asserted or used',
 'gamma':[str(x) for x in gamma],
 'ordinary_origin':[str(x) for x in ordinary],
 'cusp_origin':[str(x) for x in cusp],
 'difference':[str(sp.expand(x)) for x in F],
 'one_step_cusp_deck_of_ordinary':[str(x) for x in change(ordinary,s,1)],
 'angular_difference':[str(sp.expand(x)) for x in change(F,v,theta)],
 'gamma_turns_per_positive_lambda_loop':1,
 'double_cusp_deck_line_gauge_winding':2,
 'checks':{name:[str(x) for x in value] for name,value in checks.items()}}
path=Path(__file__).with_suffix('.json')
path.write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
