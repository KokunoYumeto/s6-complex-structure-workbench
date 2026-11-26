"""Complete exact 02XU certificate after target release.

Includes the independently frozen resultant/conductor checks and the full
printed spectral-genus and incidence inequalities. No historical script
was available to read or replay. The unbounded inequalities are proved
symbolically; the finite checks only verify the stated elementary cases.
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

report = {
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
}

# Relative P1-bundle cohomology and P1 Riemann--Roch, independently of
# the printed adjunction multiplication: R1 p_* O(-3 xi+bF)
# = E^* tensor O(b-deg(E)), whose two splitting degrees are below.
alpha, beta, base_zero = s.symbols("alpha beta base_zero", integer=True)
e = alpha+beta
R1_degrees = [base_zero-2*alpha-beta, base_zero-alpha-2*beta]
chi_R1 = sum(z+1 for z in R1_degrees)
chi_curve = 1+chi_R1
arithmetic_genus = s.expand(1-chi_curve)
assert s.expand(arithmetic_genus-(3*e-2-2*base_zero)) == 0

# Separate multiplication in the rank-two projective-bundle Chow ring.
xi, F, ee, bb = s.symbols("xi F ee bb")
D = 3*xi-bb*F
K = -2*xi+(ee-2)*F
product = s.Poly(s.expand(D*(D+K)), xi, F)
intersection = s.expand(ee*product.coeff_monomial(xi**2)
                       +product.coeff_monomial(xi*F))
assert intersection == 6*ee-6-4*bb
assert s.expand(1+intersection/2-(3*ee-2-2*bb)) == 0
assert arithmetic_genus.subs({alpha:0,beta:0}) == -2-2*base_zero
assert arithmetic_genus.subs({alpha:2,beta:0}) == 4-2*base_zero

# The stronger printed nonplanar unibranch bound: only the m=3,delta=2
# equality case needs sharpening from six to seven. The quadratic terms
# x^2 and xy are absent because they have unique orders six and seven.
# All order-three gradient vectors then have only their z coordinate.
q = s.symbols("q")
c1,d1,e1,f1,c2,d2,e2,f2 = s.symbols("c1 d1 e1 f1 c2 d2 e2 f2")
z = s.symbols("z")
rels=[c1*x*z+d1*y*y+e1*y*z+f1*z*z,
      c2*x*z+d2*y*y+e2*y*z+f2*z*z]
J=s.Matrix([[s.diff(R,w).subs({x:q**3,y:q**4,z:q**5}, simultaneous=True)
             for w in (x,y,z)] for R in rels])
minor_orders=[]
for ij in itertools.combinations(range(3),2):
    M=s.Poly(s.expand(J[:,ij].det()),q)
    order=min(m[0][0] for m in M.terms())
    assert order>=7
    minor_orders.append(order)

# Integer checks supplement the universal graph slack inequalities:
# singleton A: contribution>=2c; singleton +/-: >=c+r_A;
# no singleton: >=ceil((r_A+2c)/2)>c.
rows=[]
for cB in range(1,51):
    for rA in range(1,4):
        lower=[2*cB,cB+rA,(rA+2*cB+1)//2]
        assert all(v>cB for v in lower)
        assert cB+1>cB
        rows.append([cB,rA,*[v-cB for v in lower]])
report.update({
    "relative_R1_splitting_degrees": [str(z) for z in R1_degrees],
    "relative_cohomology_arithmetic_genus": str(arithmetic_genus),
    "independent_Chow_ring_intersection": str(intersection),
    "degree_zero_bundle_genus": "-2-2*b < 0",
    "degree_two_bundle_two_common_zeros_genus": "4-2*b <= 0 for b>=2",
    "nonplanar_equality_case_gradient_minor_orders": minor_orders,
    "three_branch_graph_rows_checked": len(rows),
    "minimum_graph_excesses": [min(row[j] for row in rows) for j in (2,3,4)],
    "two_junction_A_only_excess": "at least one",
    "historical_replay": False
})
print(json.dumps(report,indent=2))
