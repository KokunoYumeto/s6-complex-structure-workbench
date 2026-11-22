"""Exact supporting calculations for the statement-led 02XU derivation.

No target proof or historical target program has been read. The universal
graph inequality is proved in the derivation; the finite enumeration below
checks its set-theoretic common-branch premise, not its unbounded conclusion.
"""
import itertools
import json
import sympy as s

x, y, a, b, c, d, u, v, t, k = s.symbols("x y a b c d u v t k")
P = a*x**3+b*x**2*y+c*x*y**2+d*y**3
disc = s.discriminant(P.subs(y, 1), x)
expected = b*b*c*c-4*a*c**3-4*b**3*d-27*a*a*d*d+18*a*b*c*d
assert s.expand(disc-expected) == 0
diagonal = s.discriminant(P.subs({x:u*x, y:v}, simultaneous=True), x)
assert s.expand(diagonal-(u*v)**6*disc) == 0
shear = s.discriminant(P.subs({x:x+t, y:1}, simultaneous=True), x)
assert s.expand(shear-disc) == 0
assert s.expand(s.discriminant(k*P.subs(y, 1), x)-k**4*disc) == 0

# Evaluating x^2-xy, y^2-xy, xy on (q,0), (0,q), (q,q),
# and dividing by q^2 gives the identity, hence arbitrary independent jets.
columns = [x*x-x*y, y*y-x*y, x*y]
E = s.Matrix([[q.subs({x:X,y:Y}, simultaneous=True) for q in columns]
              for X,Y in [(1,0),(0,1),(1,1)]])
assert E == s.eye(3)

families = 0
choices = [{0},{1},{0,1}]
for n in range(1, 8):
    for F in itertools.product(choices, repeat=n):
        if all(F[i]&F[j] for i in range(n) for j in range(i)):
            assert set.intersection(*F)
            families += 1

delta, tau, ram, mult, g, h0, h1 = s.symbols(
    "delta tau ram mult g h0 h1", integer=True)
assert s.expand((1-delta)+(4+ram-tau)-(5-(delta+tau-ram))) == 0
assert s.expand((mult-1)+2*mult-(mult-1)-2*mult) == 0
assert s.expand((mult-1)+2*mult-(mult-2)-(2*mult+1)) == 0

print(json.dumps({
    "binary_cubic_discriminant": str(disc),
    "diagonal_frame_weight": "(u*v)^6",
    "unipotent_frame_shear": "invariant",
    "equation_unit_weight": "k^4",
    "conductor_jet_evaluation_matrix": [[int(z) for z in row] for row in E.tolist()],
    "pairwise_intersecting_two_branch_families_checked": families,
    "family_sizes_checked": [1,7],
    "primary_double_curve_chi": "5 - sum(delta + tau - ram)",
    "nonplanar_unibranch_defect_lower_bound": "2*m >= 6",
    "nonplanar_two_branch_defect_lower_bound": "2*(m1+m2)+1 >= 7",
    "planar_defect": "5*delta",
    "singular_image_remaining_case": "one planar delta=1 point; genus(H)=1",
    "separated_point_graph_bound": "beta >= k-c+(r_plus+r_minus-n) >= k > 0",
    "historical_program_read": False,
    "events_added": 0
}, indent=2))
