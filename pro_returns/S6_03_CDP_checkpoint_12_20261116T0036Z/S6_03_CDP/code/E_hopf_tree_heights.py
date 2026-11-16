#!/usr/bin/env python3
"""Exact canonical height and normal-root comparisons; no occurrence inference."""
from sympy import Rational, symbols, simplify, solve, expand

# A unicyclic graph with branched trees, unequal normal orders and three
# nonlinear leaves of equal total height. These are equation checks only.
cycle = [(0, 1, 1), (1, 2, 1), (2, 0, 1)]
tree = [(0, 3, 2), (3, 4, 3), (3, 5, 1), (5, 6, 2),
        (1, 7, 5), (2, 8, 4)]
edges = cycle + tree
n = 9
nonlinear = {4, 6, 7}
height = [0, 0, 0, 2, 5, 3, 5, 5, 4]
h = symbols("h0:" + str(n))
eqs = [h[j] for j in range(3)]
theta = {}
for v in range(3, n):
    incident = [(a, b, m) for a, b, m in edges if v in (a, b)]
    if v in nonlinear:
        a, b, m = incident[0]
        w = b if a == v else a
        eqs.append(h[v] - h[w] - m)
    else:
        eqs.append(sum((h[b if a == v else a] - h[v]) / m
                       for a, b, m in incident) - (len(incident) - 2))
solution = solve(eqs, h, dict=True)
assert len(solution) == 1
assert [solution[0][v] for v in h] == height
for v in range(n):
    if v in nonlinear:
        continue
    orders = []
    for a, b, m in edges:
        if v in (a, b):
            w = b if a == v else a
            d = Rational(height[w] - height[v], m)
            assert d.q == 1
            orders.append(d - 1)
    assert sum(orders) == -2
    theta[v] = orders
R = height[next(iter(nonlinear))]
assert all(height[v] == R for v in nonlinear)
assert all(height[v] < R for v in range(n) if v not in nonlinear)
print("ABSTRACT CANONICAL EQUATION CHECK (not an existence assertion)")
print("weighted edges =", edges)
print("unique canonical heights =", height)
print("base differential orders by elliptic vertex =", theta)
print("nonlinear leaves =", sorted(nonlinear), "; common period order =", R)
print("all elliptic vertex heights are strictly smaller")

# The mismatch is detected by the same single-period comparison.
changed = height[:]
changed[7] += 1
assert len({changed[v] for v in nonlinear}) > 1
print("changing one nonlinear height is incompatible with one nonzero period")

# Exact root congruence: no unmarked multiple can have order zero.
for m in range(2, 41):
    assert (-m + 1) % m != 0
print("unmarked root congruence checked for m=2,...,40")

# Gauge identity for arbitrary values around a finite orbit whose sum is zero.
# This formal cyclic calculation avoids unnecessary algebraic-root simplification.
gauges = 0
for m in range(2, 21):
    A = list(symbols("a0:" + str(m - 1)))
    A.append(-sum(A))
    b0 = -sum(j*A[j] for j in range(m))/m
    b1 = -sum(j*A[(j + 1) % m] for j in range(m))/m
    assert expand(b1 - b0 + A[0]) == 0
    gauges += 1
print("constant-inertia gauge identities passed =", gauges)

# Actual collar equality, with no replacement of an integral cover degree.
x, y, t, c = symbols("x y t c", nonzero=True)
for m in range(1, 21):
    assert simplify((t/x)**m - t**m/x**m) == 0
print("collar map y=t/x sends x^m=c to y^m=t^m/c, m=1,...,20")
print("ALL CHECKS PASSED")
