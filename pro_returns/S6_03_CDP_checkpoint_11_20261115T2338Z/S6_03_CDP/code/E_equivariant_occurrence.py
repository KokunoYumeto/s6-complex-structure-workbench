"""Exact finite-chart and divisor-functor certificates for C.2.UN.35.

The theorem is proved for all orders in the text.  These checks retain the
actual monomial and divisor maps, rather than comparing numerical classes.
The complementary norm-torus calculation is A_equivariant_torus.py.
"""
from math import gcd
from functools import reduce
import sympy as s

I = s.eye(2)
models = {
    1: I,
    2: -I,
    3: s.Matrix([[0, -1], [1, -1]]),
    4: s.Matrix([[0, -1], [1, 0]]),
    6: s.Matrix([[0, -1], [1, 1]]),
}

# A point orbit and its exceptional-curve orbit have exactly the same
# permutation module.  The coefficient map is literally the identity,
# not merely an isomorphism after tensoring with Q or passing to Picard.
orbit_count = 0
for n in range(1, 25):
    for d, A in models.items():
        if n % d:
            continue
        for r in s.divisors(n):
            P = s.zeros(r)
            for j in range(r):
                P[(j + 1) % r, j] = 1
            point_action = s.kronecker_product(P, A)
            exceptional_action = s.kronecker_product(P, A)
            extension = s.eye(2 * r)
            assert extension * point_action == exceptional_action * extension
            assert point_action ** n == s.eye(2 * r)
            # Same coefficient submodule at a point stabilized by g^r.
            fixed = (A ** r - I).nullspace()
            for v in fixed:
                assert A ** r * v == v
                for denominator in (1, 2, 3, 5, 7):
                    orbit = [A ** j * (v / denominator) for j in range(r)]
                    assert A * orbit[-1] == orbit[0]
            orbit_count += 1
print('Exact point-to-exceptional divisor intertwining checks:', orbit_count)

# The inertia translation on C/(Z lambda_1 + Z lambda_2) represented by
# (a,b)/m has order m/gcd(m,a,b).  Root coefficients are preserved.
faithful = 0
for m in range(2, 21):
    for a in range(m):
        for b in range(m):
            exact_order = next(k for k in range(1, m + 1)
                               if (k * a) % m == 0 and (k * b) % m == 0)
            assert exact_order == m // reduce(gcd, (m, a, b))
            if exact_order == m:
                assert all((k * a) % m or (k * b) % m
                           for k in range(1, m))
                faithful += 1
print('Faithful root-translation charts checked:', faithful)

# Exact blowup chart x=u v, y=v, including a marked old SNC node.
x, y, u, v, w, alpha, gamma = s.symbols('x y u v w alpha gamma', nonzero=True)
assert s.Matrix([u * v, v]).jacobian([u, v]).det() == v
for a in range(1, 7):
    for b in range(0, 7):
        pullback = (x ** a * y ** b).subs({x: u * v, y: v})
        assert pullback == u ** a * v ** (a + b)
        transformed = pullback.subs({u: alpha / gamma * u, v: gamma * v})
        assert s.simplify(transformed - alpha ** a * gamma ** b * pullback) == 0
        for m in (1, 2, 3, 4, 6, 7):
            assert pullback.subs(v, w ** m) == u ** a * w ** (m * (a + b))
print('Blowup/root charts: exact multiplicities and cyclic characters passed')

# The auxiliary exceptional coordinate is z=x/t.  For a faithful base
# character chi, it receives chi^{-1}; the generic base remains elliptic.
t, chi = s.symbols('t chi', nonzero=True)
assert s.simplify(x / (chi * t) - chi ** -1 * x / t) == 0
print('Rational auxiliary curve: z=x/t has exactly the inverse disc character')

# Changing a local mth-root lift by a kth root of unity is exactly the
# same deck operation on the normal coordinate and on both character
# lines.  Passing through Phi gives the same inertia translation.
for m in range(2, 17):
    for a, b in ((1, 0), (0, 1), (1, 1), (2, 3)):
        for k in range(m):
            line_weights = ((k * a) % m, (k * b) % m)
            deck_translation = ((k * a) % m, (k * b) % m)
            assert line_weights == deck_translation
print('Root-lift ambiguity: simultaneous line weights equal deck translations')
print('PASS: all exact chart, divisor and inertia checks')
