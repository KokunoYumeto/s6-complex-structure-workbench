"""Exact finite, intersection and blowup certificates for C.2.UN.66."""
from fractions import Fraction
from itertools import combinations_with_replacement, product
from pathlib import Path
import sympy as s

out = []
def report(value):
    out.append(str(value))

# A maximum ruled vertex has positive horizontal degrees and weights.
partitions = []
for length in (1, 2):
    for pairs in combinations_with_replacement(list(product((1, 2), repeat=2)), length):
        if sum(a*d for a, d in pairs) == 2:
            partitions.append(pairs)
assert partitions == [((1, 2),), ((2, 1),), ((1, 1), (1, 1))]
report("Maximum ruled positive partitions (weight, ruling degree): " + str(partitions))

# Exact elliptic-curve possibilities in a Hirzebruch surface.
# The genus equation forces a-1 to divide2, hence a=2 or3.
elliptic = []
for a in (2, 3):
    for n in range(0, 8):
        b = Fraction(n*a + 2 + Fraction(2, a-1), 2)
        if b.denominator == 1 and b >= n*a:
            square = -n*a*a + 2*a*b
            elliptic.append((n, a, int(b), int(square)))
assert elliptic == [(0,2,2,8),(1,2,3,8),(2,2,4,8),(1,3,3,9)]
report("Every irreducible elliptic Hirzebruch possibility (n,a,b,C^2): " + str(elliptic))
report("The genus equation and b>=na bound n<=2 for a2 and n<=1 for a3; no omitted square-zero case.")

# The Euclidean orbifold lists. Four points force all orders2.
# For three ordered orders, reciprocal sum1 bounds them by6.
euclidean = []
for length in (3,4):
    for ms in combinations_with_replacement(range(2,7), length):
        delta = Fraction(-2) + sum((1-Fraction(1,m) for m in ms), Fraction())
        if delta == 0:
            euclidean.append(ms)
assert euclidean == [(2,3,6),(2,4,4),(3,3,3),(2,2,2,2)]
for ms in euclidean:
    cover_degree = max(ms)
    ramification = sum(cover_degree-cover_degree//m for m in ms)
    assert -2*cover_degree + ramification == 0
report("Exact genus-one quotient multiplicities and Riemann-Hurwitz: " + str(euclidean))

# The constant-ratio conclusion is an exact bracket identity on a curve.
z = s.symbols("z")
b = s.Function("b")(z)
c = s.Function("c")(z)
bracket = b*s.diff(c,z)-c*s.diff(b,z)
assert s.simplify(s.diff(c/b,z)-bracket/b**2) == 0
report("PASS [b*d/dz,c*d/dz]=0 gives d(c/b)/dz=0 on the actual nonzero locus.")

# A curve blowup leaves the parent as a surface and adds the projective
# normal bundle, meeting it along the unchanged centre.
g, previous = s.symbols("g previous", integer=True)
curve_euler = 2-2*g
exceptional_euler = 2*curve_euler
new_euler = s.expand(previous + exceptional_euler - curve_euler)
assert s.expand(new_euler-previous) == -2*(g-1)
report("Exact full-support curve-blowup difference: " + str(s.expand(new_euler-previous)))

# Every sequence retains its own genus list; the result is independent
# of the order of its actual disjoint blowups.
count = 0
for length in range(0,6):
    for genera in combinations_with_replacement(range(1,6), length):
        total = 0
        for genus in genera:
            total += 2*(2-2*genus) - (2-2*genus)
        expected = -2*sum(genus-1 for genus in genera if genus >= 2)
        assert total == expected and total <= 0
        assert (total == 0) == all(genus == 1 for genus in genera)
        count += 1
report(f"PASS {count} exact retained-genus contraction records, including every multiset of up to5 centres of genera1,...,5.")

# Relative blowup maps, including the point case needed before rational
# persistence has excluded it.
x,y,w = s.symbols("x y w")
curve_map = s.Matrix([x,x*y,w])
point_map = s.Matrix([x,x*y,x*w])
assert s.factor(curve_map.jacobian([x,y,w]).det()) == x
assert s.factor(point_map.jacobian([x,y,w]).det()) == x**2
report("PASS ordinary curve/point Jacobians x and x^2, retaining canonical-order differences on surviving components.")
report("All maximum, surface-intersection, exact quotient and Euler certificates passed.")

text = "\n".join(out) + "\n"
Path(__file__).with_suffix(".out").write_text(text)
print(text, end="")
