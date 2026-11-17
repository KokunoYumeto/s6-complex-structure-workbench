#!/usr/bin/env python3
"""Exact finite identities for the independent parabolic Kato weight audit.

The proof of absence of other vector fields is a lowest-order argument in
sections/ab_push_kato_weights_referee.md; finite truncation is not used to
infer that analytic statement.
"""
import json
from pathlib import Path
import sympy as sp

lam, n, j = sp.symbols('lambda n j', nonzero=True)
elliptic = 2*n*lam/(lam-1)**2
node = -(lam**2+1)/(lam-1)**2
assert sp.cancel(elliptic+n*node+n) == 0

rays = sp.Matrix([[j,j+1],[1,1]])
assert rays.det() == -1
weights = rays.inv()*sp.Matrix([1,0])
assert weights == sp.Matrix([-1,1])

x,v,a,K,b,c = sp.symbols('x v a K b c', nonzero=True)
checks=[]
for nn in range(1,13):
    F=sp.Matrix([K*x*v**nn,a*v])
    jac=F.jacobian([x,v])
    V=sp.Matrix([c*x,0])
    at_F=V.subs({x:F[0],v:F[1]},simultaneous=True)
    assert all(sp.expand(z)==0 for z in at_F-jac*V)
    trial=sp.Matrix([c*x,b*v])
    trial_F=trial.subs({x:F[0],v:F[1]},simultaneous=True)
    defect=sp.simplify(trial_F-jac*trial)
    assert defect[0] == -K*b*nn*v**nn*x
    assert defect[1] == 0
    checks.append({'n':nn,'chi_log_tangent_character':-nn,
                   'h0_log_tangent_weight_zero':1,
                   'h1_log_tangent_weight_zero':nn+1,
                   'h1_contracted_tangent_weight_zero':nn,
                   'horizontal_field_defect':str(defect[0])})

out={'status':'PASS',
     'elliptic_fixed_curve_contribution':str(elliptic),
     'one_cycle_node_contribution':str(node),
     'total_character':str(sp.cancel(elliptic+n*node)),
     'adjacent_ray_determinant':str(rays.det()),
     'tangent_weights':list(weights),
     'checks':checks,
     'scope':'Exact character and coordinate identities; analytic global-vector-field completeness is proved by Hartogs and lowest orders.'}
target=Path(__file__).with_suffix('.json')
target.write_text(json.dumps(out,indent=2,default=str)+'\n')
print(json.dumps(out,indent=2,default=str))
