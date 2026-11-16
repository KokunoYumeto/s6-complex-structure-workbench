"""Exact chart, adjunction and Euler certificates for C.2.UN.72.

The arithmetic records below verify the identities for actual allowed
blowups. They do not assert that arbitrary proposed curve centres exist.
"""
from itertools import combinations_with_replacement
import sympy as s

x, u, v, w, t, g = s.symbols("x u v w t g")
print("C.2.UN.72: ordinary charts and exact reconstruction identities")
point = s.Matrix([x, x*u, x*v])
curve = s.Matrix([x, w, x*v])
assert s.det(point.jacobian([x, u, v])) == x**2
assert s.det(curve.jacobian([x, w, v])) == x
assert point[2] == curve[2] == x*v
print("Point chart (x,xu,xv): Jacobian x^2; fibre x*v.")
print("Curve chart (x,w,xv): Jacobian x; fibre x*v.")

# At a new component: the order increment and the actual section normal.
point_increment, point_section_square = 2, 1
curve_increment, curve_section_square = 1, 2 - 2*g
assert -point_increment*point_section_square == -2
assert s.expand(-curve_increment*curve_section_square) == 2*g - 2
assert -point_increment - 1 == -3
assert -curve_increment - 1 == -2
print("Actual edge adjunction: plane line (-2)*1=-2; ruled section gives 2g-2.")

checked, zeros = 0, []
for length in range(6):
    for genera in combinations_with_replacement(range(1, 6), length):
        for points in range(8):
            via_blowups = 2*points + sum(2 - 2*h for h in genera)
            via_edges = 2*points - 2*sum(h - 1 for h in genera if h >= 2)
            assert via_blowups == via_edges
            assert (via_blowups == 0) == (points == sum(h - 1 for h in genera))
            assert via_blowups % 2 == 0
            checked += 1
            if via_blowups == 0:
                zeros.append((points, genera))
print("Exact point/genus reconstruction records:", checked)
print("Zero-balance records among those:", len(zeros))
for example in [(0, (1, 1)), (1, (2,)), (2, (3,)), (3, (2, 3))]:
    assert example in zeros
    print("Zero Euler certificate: points=%s, curve genera=%s" % example)

# Direct SNC Euler identities, with the triple contribution retained until
# the no-triple premise is imposed.
sum_ev, sum_ec, triples = s.symbols("sum_ev sum_ec triples")
nearby = sum_ev - 2*sum_ec + 3*triples
support = sum_ev - sum_ec + triples
assert s.expand(support - nearby) == sum_ec - 2*triples
all_elliptic_no_triples = support.subs(sum_ev, 2*sum_ec - 3*triples).subs(
    {sum_ec: 0, triples: 0})
assert all_elliptic_no_triples == 0
print("Nearby-stratum comparison: e(S)-e(F)=sum e(C)-2t; elliptic/no-triple gives 0.")
print("Every certificate PASS.")
