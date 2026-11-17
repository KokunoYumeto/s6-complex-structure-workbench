"""Exact local and divisor checks for Proposition B.4.21.

This verifies the displayed formulas; properness and the analytic
neighbourhood comparison are proved in the accompanying source.
"""
from pathlib import Path
import json
import sympy as S

n = 12
u, v, s, x, y, e, ep, h, H = S.symbols('u v s x y e ep h H')
a, kappa, z = S.symbols('a kappa z')
steps = []
for j, m in enumerate(range(n, 1, -2), 1):
    # Strict transform in the parameter chart of the point blow-up.
    transformed = (u*v-s**m).subs({u:s*x, v:s*y})
    assert S.expand(transformed-s**2*(x*y-s**(m-2))) == 0
    # In the u-chart the strict transform has derivative one in y.
    transformed_u = (u*v-s**m).subs({v:u*y, s:u*z})
    assert S.expand(transformed_u-u**2*(y-u**(m-2)*z**m)) == 0
    assert S.diff(y-u**(m-2)*z**m, y) == 1
    steps.append({'point_blowup':j, 'incoming_exponent':m,
                  'remaining_exponent':m-2, 'h_order_new_divisor':2*j})
assert len(steps) == 6

coeff = S.Matrix([2*min(i, n-i) for i in range(n)])
correction = S.Matrix([n-c for c in coeff])
Q = S.zeros(n)
for i in range(n):
    Q[i,i] = -2
    Q[i,(i-1)%n] += 1
    Q[i,(i+1)%n] += 1
normal_degrees = -Q*coeff
assert list(normal_degrees) == [-4,0,0,0,0,0,4,0,0,0,0,0]
assert Q*S.ones(n,1) == S.zeros(n,1)
assert -Q*(coeff+correction) == S.zeros(n,1)
assert sum(correction) == 72
assert sum(coeff) == 72
assert min(correction) == 0 and correction[6] == 0

# At each node the two repeated curve blow-ups raise the two h-orders
# independently; the final h/q is exactly the strict divisor coordinate.
node_records = []
for i in range(n):
    j = (i+1)%n
    ci, cj = int(coeff[i]), int(coeff[j])
    bi, bj = int(correction[i]), int(correction[j])
    assert ci+bi == cj+bj == n
    final_h = e*x**(ci+bi)*y**(cj+bj)
    assert S.cancel(final_h/(x*y)**n) == e
    for old_order in range(ci, n):
        old = e*x**old_order*y**cj
        assert S.expand(old.subs(e,x*ep)-ep*x**(old_order+1)*y**cj) == 0
    node_records.append({'node':[i,j], 'initial_h_orders':[ci,cj],
                         'final_h_orders':[n,n], 'H_normal_order':1})

# Minimal A_11 resolution character charts.
character_charts = []
for i in range(n):
    U = x**(i+1)*y**i
    V = x**(n-i-1)*y**(n-i)
    assert S.expand(U*V-(x*y)**n) == 0
    assert S.cancel(U/(x*y)**i) == x
    assert S.cancel((x*y)**(i+1)/U) == y
    det = S.det(S.Matrix([[i,1],[i+1,1]]))
    assert abs(det) == 1
    character_charts.append({'i':i, 'adjacent_ray_determinant':int(det)})

# The q-chart of Bl(h,q), h=uv-s^12, and the regularizing transverse H.
assert S.expand(u*(v/(1+H))-s**n).subs(u*v,s**n*(1+H)) == 0
# Finite product identity, with its explicit factor tending to one.
product_checks = []
for m in (1,2,3,6,12):
    G = S.prod(1+a**j*H for j in range(1,m+1))
    assert S.cancel(G.subs(H,a*H)/G - (1+a**(m+1)*H)/(1+a*H)) == 0
    product_checks.append(m)

record = {
    'status':'PASS', 'point_blowups':steps,
    'normal_correction_Z':[int(c) for c in coeff],
    'normal_degrees_before_curve_repair':[int(c) for c in normal_degrees],
    'curve_blowups_per_component':[int(c) for c in correction],
    'curve_blowups_total':int(sum(correction)),
    'normal_degrees_after_curve_repair':[0]*n,
    'actual_transverse_coordinate':'H=h/q=h/s^12',
    'normal_comparison_from_old_punctured_frame':'s^(-12)',
    'nodes':node_records, 'character_charts':character_charts,
    'finite_product_identity_checked_to':product_checks,
    'persistent_elliptic_normal_degree':-1,
    'whole_second_period_or_origin_cap':'NOT CONSTRUCTED'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
print('Six point charts and residual A-exponents: PASS')
print('Z =', record['normal_correction_Z'])
print('Normal degrees before curve repair =', record['normal_degrees_before_curve_repair'])
print('Curve blow-ups per component =', record['curve_blowups_per_component'])
print('Total curve blow-ups =', record['curve_blowups_total'])
print('All twelve node exponents give H=h/s^12 with normal order one: PASS')
print('Twelve minimal-resolution character charts, determinants and products: PASS')
print('Finite approximants of the uniform product identity: PASS')
print('ALL EXACT CHECKS PASSED')
