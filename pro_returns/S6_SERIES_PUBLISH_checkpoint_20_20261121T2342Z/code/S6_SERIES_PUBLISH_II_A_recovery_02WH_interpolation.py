"""Postrelease recovery: exact interpolation, exterior forms and cell counts.

Polynomial degree bounds are proved in the accompanying recovery addendum.
No symbolic gcd, substitution/expansion, Jacobian determinant, or matrix rank is used.
"""
from fractions import Fraction as Q
from itertools import product
from collections import defaultdict


# Each cleared residual has degree at most 12, so thirteen integer values certify it.
for t in range(13):
    d_new, dp_new = 4 + 27*t**12, 324*t**11
    d_print, dp_print = t**12 - 4, 12*t**11
    assert 12*d_new - t*dp_new - 48 == 0
    assert 12*d_print - t*dp_print + 48 == 0
assert (4, -4) == (4 + 27*0**12, 0**12 - 4)
print('two degree-12 Bezout identities: 13 exact integer evaluations each')
print('a common root with the derivative contradicts the nonzero constants 4 or -4')

# In each independent coordinate the following three residuals have degree <=2.
for a, u, x in product(range(3), repeat=3):
    y, v = -a*u, -a*x
    r, h = x-u, y-v
    assert x*y-u*v == 0
    assert h-a*r == 0
    assert x*y+a*u*x == 0
for b, y, v in product(range(3), repeat=3):
    u, x = -b*y, -b*v
    r, h = x-u, y-v
    assert x*y-u*v == 0
    assert r-b*h == 0
    assert x*y+b*y*v == 0
print('both small-resolution charts: 3 residuals, separate degree <=2, 27 grid points each')

# After the displayed denominators are cleared, separate degrees are <=1.
# Distinct nonzero coordinates 1,2 may be used for the inverse parameter.
for a, u, x in product((Q(1), Q(2)), (Q(0), Q(1)), (Q(0), Q(1))):
    b, y, v = 1/a, -a*u, -a*x
    assert a*b-1 == 0
    assert a*(-b*y-u) == 0
    assert a*(-b*v-x) == 0
for b, y, v in product((Q(1), Q(2)), (Q(0), Q(1)), (Q(0), Q(1))):
    a, u, x = 1/b, -b*y, -b*v
    assert a*b-1 == 0
    assert b*(-a*u-y) == 0
    assert b*(-a*x-v) == 0
print('overlap inverses: separate degree <=1 after clearing denominators, 8 grid points each')

# Laurent exterior algebra in s,X,Y. A term is (monomial exponent, wedge-index tuple).
def monomial_derivative(exponent):
    answer = {}
    for j, power in enumerate(exponent):
        if power:
            shifted = list(exponent)
            shifted[j] -= 1
            answer[(tuple(shifted), (j,))] = Q(power)
    return answer


def wedge(left, right):
    out = defaultdict(Q)
    for (m, a), c in left.items():
        for (n, b), d in right.items():
            if set(a) & set(b):
                continue
            inversions = sum(i > j for i in a for j in b)
            exponent = tuple(i+j for i, j in zip(m, n))
            indices = tuple(sorted(a+b))
            out[(exponent, indices)] += c*d*(-1)**inversions
    return {k: v for k, v in out.items() if v}


def multiply_monomial(form, exponent, coefficient):
    return {(tuple(i+j for i, j in zip(m, exponent)), a): coefficient*c
            for (m, a), c in form.items()}


dt = monomial_derivative((-1, 0, 0))
dx = monomial_derivative((-2, 1, 0))
canonical = multiply_monomial(wedge(dt, dx), (3, 0, -1), Q(1, 2))
assert canonical == {((-1, 0, -1), (0, 1)): Q(-1, 2)}
print('Laurent exterior product: dt wedge dx/(2y) = -ds wedge dX/(2sY)')


def tensor_counts(a, b):
    result = [0] * (len(a)+len(b)-1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            result[i+j] += u*v
    return result


def euler(cells):
    return sum((-1)**k*n for k, n in enumerate(cells))


nodal = [1, 1, 1]  # S^2 wedge S^1, from identifying two points in P^1.
node_product = tensor_counts(nodal, nodal)
relative = list(node_product)
relative[0] -= 1
p1 = [1, 0, 1]
resolved = [a+(p1[k] if k < len(p1) else 0) for k, a in enumerate(relative)]
torus = [1]
for _ in range(4):
    torus = tensor_counts(torus, [1, 1])
punctured_base = [1, 11]
assert node_product == [1, 2, 3, 2, 1]
assert relative == [0, 2, 3, 2, 1]
assert resolved == [1, 2, 4, 2, 1]
assert torus == [1, 4, 6, 4, 1]
assert euler(relative) == 0 and euler(resolved) == 2
total = 12*euler(resolved) + euler(tensor_counts(punctured_base, torus))
assert total == 24
print('CW counts nodal/product/relative/resolved', nodal, node_product, relative, resolved)
print('CW counts torus and punctured base', torus, punctured_base)
print('resolved fibre Euler', euler(resolved), 'total Euler/Chern number', total)
