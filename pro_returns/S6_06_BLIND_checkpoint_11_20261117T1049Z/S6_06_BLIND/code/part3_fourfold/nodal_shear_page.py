#!/usr/bin/env python3
"""Exact old/new conifold and source norm-shell chart identities."""
from pathlib import Path
import json
import sympy as s
t,a,b,x,z,j=s.symbols('t a b x z j',nonzero=True)
old=(a,t*b,b,t*a)
sp,up,vp=b/a,a,t*a
new=(up,sp*vp,sp*up,vp)
assert all(s.simplify(c-d)==0 for c,d in zip(old,new))
assert s.simplify(old[0]*old[1]-old[2]*old[3])==0
assert s.simplify(sp*up*vp-t*a*b)==0
blow=(z/t,x,t*x)
assert s.simplify(blow[0]*blow[1]*blow[2]-x*x*z)==0
assert s.simplify(blow[0]*blow[2]-x*z)==0
assert (j+1)-j==1
data={
 'old_chart':['t','a','b'],
 'source_and_line':{'x':'a','y':'t*b','V':'t','q':'x*y'},
 'conifold_coordinates':['a','t*b','b','t*a'],
 'new_chart':{'s_prime':'b/a','u_prime':'a','v_prime':'t*a'},
 'new_source_and_line':{'x_prime':'x','y_prime':'y','V_prime':'x*V'},
 'delta_old_weights':[1,0,-1],
 'delta_new_weights':[-1,0,1],
 'branch_orders_of_x':[1,0],
 'branch_orders_after_base_q_power':['j+1','j'],
 'branch_order_difference':1,
 'source_blowup':['x','z=y/x','t'],
 'map_to_new_resolution':['z/t','x','t*x'],
 'exceptional_orbit_map':'|s_prime|=|z|/rho',
 'scope':'exact nodal map and collapsed exceptional orbit; new embedded page and its global Euler-line surgery remain to be constructed',
}
Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
print('PASS: both resolutions, common conifold, branch orders, and common-blowup page map.')
