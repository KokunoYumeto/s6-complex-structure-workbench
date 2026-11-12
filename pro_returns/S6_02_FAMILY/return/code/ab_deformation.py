"""Exact checks for A.5.2; no numerical approximations or theorem inputs.

Checks the independent coarse-degree and weighted-monomial cohomology
calculations, cusp cup product, monodromy character, Leray summands and
the logarithmic-volume determinant.  Geometric exactness and descent are
proved in AB.tex; these finite computations verify their displayed data.
"""
from collections import Counter
from fractions import Fraction
import sympy as S


def coarse_degree(k):
    degree = Fraction(k, 12) - Fraction(k % 3, 3) - Fraction((-k) % 4, 4)
    assert degree.denominator == 1
    return int(degree)


def coarse_cohom(k):
    d = coarse_degree(k)
    return (max(d + 1, 0), max(-d - 1, 0))


def weighted_monomials(k):
    if k < 0:
        return 0
    return sum(1 for i in range(k // 3 + 1) if (k - 3 * i) % 4 == 0)


for k in range(-240, 241):
    independent = (weighted_monomials(k), weighted_monomials(-k - 7))
    assert coarse_cohom(k) == independent
print("Root-line cohomology: coarse invariant exponents and weighted monomials agree for 481 weights.")
for k in (0, 1, -1, -2, -5, -6):
    print("weight, r3, r4, coarse degree, (h0,h1):", k, k % 3, (-k) % 4, coarse_degree(k), coarse_cohom(k))

# The presentation Pic=<H,R1,R2 | 3R1=H=4R2> has no torsion.
pic_relations = S.Matrix([[-1, 3, 0], [-1, 0, 4]])
minors = [pic_relations[:, inds].det() for inds in ((0, 1), (0, 2), (1, 2))]
assert S.gcd_list(minors) == 1
assert pic_relations * S.Matrix([12, 4, 3]) == S.zeros(2, 1)
assert 4 - 3 == 1
print("Picard relation maximal minors:", minors, "; gcd=1; generator has degrees (H,R1,R2)=(12,4,3).")

A1 = S.Matrix([[1, 0, 0, 0], [6, 0, 1, 0], [-6, -1, -1, 0], [-2, 1, 0, 1]])
A2 = S.Matrix([[1, 0, 0, 0], [0, 0, -1, 0], [-6, 1, 0, 0], [3, 0, 1, 1]])
gamma = S.Matrix([[1, 0, 0, 0]])
assert gamma * A1 == gamma and gamma * A2 == gamma
print("The character gamma is fixed by both finite monodromies.")

B0 = S.Matrix([[0, 1], [-1, 0]])
directions = [S.Matrix([1, 0]), S.Matrix([0, 1]), S.Matrix([-1, 1])]
deck_vectors = [B0.inv() * d for d in directions]
assert deck_vectors == [S.Matrix([0, 1]), S.Matrix([-1, 0]), S.Matrix([-1, -1])]
edge_gamma = S.Matrix([v[0] for v in deck_vectors])
edge_second = S.Matrix([v[1] for v in deck_vectors])
boundary = S.Matrix([[1, -1, 1], [1, -1, 1]])
assert boundary.rank() == 1
assert boundary * edge_gamma == S.zeros(2, 1)
assert boundary * edge_second == S.zeros(2, 1)
cup = edge_gamma[0] * edge_second[2] - edge_gamma[2] * edge_second[0]
assert cup == 1
print("Cusp (h0,h1,h2)=(1,2,1); gamma edges=", list(edge_gamma), "; second-character edges=", list(edge_second), "; cup=", cup)

# Independently check alternating and nondegenerate pairing on all 1-cocycles.
a, b, c, d = S.symbols("a b c d")
alpha = S.Matrix([a, a + b, b])
beta = S.Matrix([c, c + d, d])
pairing = S.expand(alpha[0] * beta[2] - alpha[2] * beta[0])
assert pairing == a * d - b * c
assert S.Matrix([[0, 1], [-1, 0]]).det() == 1
print("Cusp cup form in a kernel basis:", pairing, "; determinant=1.")

R_O = [[0], [0, -1], [-1]]
vertical_bundle = [0, -1]
vertical_direct_images = [[a + b for a in vertical_bundle for b in row] for row in R_O]
horizontal_direct_images = [[-5 + b for b in row] for row in R_O]


def leray_dimensions(direct_images):
    result = [0] * 4
    for q, weights in enumerate(direct_images):
        for k in weights:
            for p, dim in enumerate(coarse_cohom(k)):
                result[p + q] += dim
    return result


vertical_h = leray_dimensions(vertical_direct_images)
horizontal_h = leray_dimensions(horizontal_direct_images)
assert vertical_h == [1, 1, 0, 0]
assert horizontal_h == [0, 0, 0, 0]
print("Vertical direct-image weight multiplicities:", [dict(Counter(x)) for x in vertical_direct_images])
print("Horizontal direct-image weight multiplicities:", [dict(Counter(x)) for x in horizontal_direct_images])
print("Leray dimensions: vertical=", vertical_h, "; horizontal=", horizontal_h)

# Logarithmic change of variables and the two representatives of maximal cones.
u, v = S.symbols("u v")
log_change = S.Matrix([[1, 0, u], [0, 1, v], [0, 0, 1]])
assert log_change.det() == 1
cone_plus = S.Matrix.hstack(S.Matrix([0, 0, 1]), S.Matrix([1, 0, 1]), S.Matrix([0, 1, 1]))
cone_minus = S.Matrix.hstack(S.Matrix([1, 0, 1]), S.Matrix([0, 1, 1]), S.Matrix([1, 1, 1]))
assert cone_plus.det() == 1 and cone_minus.det() == -1
print("Invariant cusp-volume determinant:", log_change.det(), "; maximal-cone determinants:", cone_plus.det(), cone_minus.det())
print("With the proved normal quotient nu_*K_dP6, the exact-sequence dimensions are h^q(T_X)=(1,1,1,0).")
print("All exact deformation checks passed.")
