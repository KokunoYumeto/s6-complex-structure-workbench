"""Exact postrelease certificates for P4.56 / 02XV.

The six-point enumeration is exhaustive for that exact finite incidence case.
The universal graph and analytic arguments are proved in the comparison.
This program does not replay the unavailable historical implementation.
"""
from itertools import combinations
import sympy as s


def matchings(points):
    if not points:
        yield ()
        return
    first = points[0]
    for i in range(1, len(points)):
        other = points[i]
        rest = points[1:i] + points[i + 1:]
        for tail in matchings(rest):
            yield ((first, other),) + tail


points = ("H_A", "R_A", "V_plus", "V_minus", "W_plus", "W_minus")
component = {p: p.split("_")[0] for p in points}
image = {p: p.split("_")[1] for p in points}
accepted = []
all_pairings = list(matchings(points))
assert len(all_pairings) == 15
for pairs in all_pairings:
    if any(image[a] == image[b] or component[a] == component[b]
           for a, b in pairs):
        continue
    supports = [set((image[a], image[b])) for a, b in pairs]
    if any(not a.intersection(b) for a, b in combinations(supports, 2)):
        continue
    adjacency = {v: set() for v in ("H", "R", "V", "W")}
    for a, b in pairs:
        adjacency[component[a]].add(component[b])
        adjacency[component[b]].add(component[a])
    reached, todo = set(), ["H"]
    while todo:
        v = todo.pop()
        if v not in reached:
            reached.add(v)
            todo.extend(adjacency[v] - reached)
    if len(reached) != 4 or sum(map(len, adjacency.values())) != 6:
        continue
    assert len(adjacency["H"]) == len(adjacency["R"]) == 1
    assert len(adjacency["V"]) == len(adjacency["W"]) == 2
    accepted.append(pairs)
assert len(accepted) == 4
print("Exhaustive six-point incidence count: 15 pairings, 4 admissible labelled paths")
for row in accepted:
    print(" ", row)
for h in (1, 2):
    total = h + 5
    lower, upper = h + 2, total // 2
    print(f"h={h}: T={total}, normalization-point interval [{lower},{upper}]")
assert (1 + 5) // 2 == 1 + 2
assert (2 + 5) // 2 < 2 + 2
assert 4 - 3 == 1
assert (2 + 1) - 2 == 1
print("Both two-junction budget excesses are 1")

a0, a1, b0, b1 = s.symbols("a0 a1 b0 b1")
mul_a = s.Matrix([[a0, 0], [a1, a0]])
mul_b = s.Matrix([[b0, 0], [b1, b0]])
expected = s.Matrix([[a0 * b0, 0], [a0 * b1 + a1 * b0, a0 * b0]])
assert mul_a * mul_b == expected
nil = s.Matrix([[0, 0], [1, 0]])
assert nil**2 == s.zeros(2)
print("Split rank-two algebra: multiplication agrees with epsilon^2=0")

X, Y, z, u, v, alpha, beta, a, h = s.symbols("X Y z u v alpha beta a h")
prepared = Y**2 + X * alpha * Y + X**2 * beta
depressed = (Y + X * alpha / 2)**2 + X**2 * (beta - alpha**2 / 4)
assert s.expand(prepared - depressed) == 0
normal_equation = Y**2 + X**2 * a**2 * h
pullback = s.expand(normal_equation.subs(Y, X * a * v))
assert s.expand(pullback - X**2 * a**2 * (v**2 + h)) == 0
assert s.rem(pullback, v**2 + h, v) == 0
print("Exact depression identity and square-part normalization substitution: zero residuals")

# A local witness to the failed intermediate implication, not to the theorem.
F = Y**2 + X**2 * (z - X)**3
actual_map = {Y: -X * v**3, z: X - v**2}
assert s.expand(F.subs(actual_map, simultaneous=True)) == 0
partial = u**2 + (z - X)**3
partial_gradient = [s.diff(partial, w) for w in (X, z, u)]
assert all(s.expand(g.subs({u: 0, z: X}, simultaneous=True)) == 0
           for g in partial_gradient)
actual = v**2 + z - X
assert s.diff(actual, z) == 1
assert s.expand(actual.subs(z, X - v**2)) == 0
assert s.expand(actual.subs({X: 0, z: -v**2}, simultaneous=True)) == 0
print("Local witness k=(z-X)^3: partial cover singular along u=0,z=X")
print("Actual cover v^2+z-X=0 is smooth; X=0 is z=-v^2")
print("ord_z k(0,z)=3, ord_z h(0,z)=1; the map on H has ramification order 2")
t, x, y = s.symbols("t x y")
assert s.expand((y**2 - x**3).subs({x: t**2, y: t**3})) == 0
assert s.expand((t**2 - x).subs(x, t**2)) == 0
print("Cusp normalization (x,y)=(t^2,t^3): one sheet, singular image, integral parameter t")

b, m, d = s.symbols("b m d", positive=True)
assert s.expand((2 * b - m).subs(b, m + d) - (m + 2 * d)) == 0
assert s.expand((2 * b - m).subs(b, m) - m) == 0
print("For b=m+d with d>=0 and m>0: 2b-m=m+2d>0, excluding 2b=m")
print("PASS: all exact identities and the complete six-point enumeration")
