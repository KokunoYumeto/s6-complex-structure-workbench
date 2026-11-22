"""Postrelease 01FY certificate: Laurent exterior algebra and interpolation.

Fresh implementation with bitmask basis, separate from the prior determinant code.
"""
from fractions import Fraction
from itertools import product


def add_forms(*forms):
    out = {}
    for form in forms:
        for key, coefficient in form.items():
            out[key] = out.get(key, Fraction(0)) + coefficient
    return {key: v for key, v in out.items() if v}


def differential(powers):
    result = {}
    for i in range(len(powers)):
        if powers[i]:
            term = list(powers)
            term[i] -= 1
            result[(tuple(term), 1 << i)] = Fraction(powers[i])
    return result


def exterior(left, right):
    result = {}
    for (a, p), c in left.items():
        for (b, q), d in right.items():
            if p & q:
                continue
            swaps = sum(bool(p & (1 << i)) and bool(q & (1 << j))
                        for i in range(len(a)) for j in range(i))
            key = (tuple(x+y for x, y in zip(a, b)), p | q)
            result[key] = result.get(key, Fraction(0)) + c*d*(-1)**swaps
    return {key: v for key, v in result.items() if v}


def times_monomial(form, powers, coefficient=1):
    return {(tuple(x+y for x, y in zip(a, powers)), p): c*coefficient
            for (a, p), c in form.items()}


def log_diff(index, dimension):
    powers = [0]*dimension
    powers[index] = -1
    return {(tuple(powers), 1 << index): Fraction(1)}


# Exact same rank-one map as the old snippet, after z_old=log(w).
dq = differential((1, 1, 0))
rankone = exterior(exterior(dq, log_diff(0, 3)), log_diff(2, 3))
assert rankone == {((0, 0, -1), 7): Fraction(-1)}
old_coordinate_form = exterior(exterior(dq, log_diff(0, 3)), differential((0, 0, 1)))
assert old_coordinate_form == {((0, 0, 0), 7): Fraction(-1)}
print('d(uv) wedge du/u wedge dw/w = -(1/w) du wedge dv wedge dw')
print('z_old=log(w), w=exp(z_old): old coefficient -1 transports to -1/w')

# Rank-two toric coordinates q=XYZ.
ranktwo = exterior(exterior(differential((1, 1, 1)), log_diff(1, 3)), log_diff(2, 3))
assert ranktwo == {((0, 0, 0), 7): Fraction(1)}
toric = times_monomial(exterior(exterior(log_diff(0, 3), log_diff(1, 3)), log_diff(2, 3)), (1, 1, 1))
assert toric == ranktwo
print('d(XYZ) wedge dY/Y wedge dZ/Z = dX wedge dY wedge dZ')

# Cubic base change s=r^3, x_s=r^4 X, y_s=r^6 Y.
cubic = times_monomial(exterior(differential((3, 0, 0)), differential((4, 1, 0))), (-6, 0, -1))
assert cubic == {((0, 0, -1), 3): Fraction(3)}
assert (1+2-0) % 3 == 0
print('ds wedge dx_s/y_s = 3 dr wedge dX/Y; deck weight is 0 modulo 3')

# Logarithmic character map (z,v) -> (v,v^2/z).
dx_log = {((0, 0), 2): Fraction(1)}
dy_log = {((0, 0), 2): Fraction(2), ((0, 0), 1): Fraction(-1)}
assert exterior(dx_log, dy_log) == {((0, 0), 3): Fraction(1)}
print('dlog(v) wedge dlog(v^2/z) = dlog(z) wedge dlog(v)')

# Separate degree bound (18,3,2); 19*4*3 exact grid evaluations.
count = 0
for r, X, Y in product(range(19), range(4), range(3)):
    s, xs, ys = r**3, r**4*X, r**6*Y
    old = ys**2-xs**3+3*s**3*(s+1)*xs-s**4*(2+3*s+2*s**2)
    new = r**12*(Y**2-X**3+3*r*(r**3+1)*X-(2+3*r**3+2*r**6))
    assert old-new == 0
    count += 1
assert count == 228
print('good-reduction equation: separate degree (18,3,2), all 228 exact grid values vanish')

# Standard two-chart Cech monomial bases for O(d) on P1.
def h0_basis(d):
    return list(range(0, d+1)) if d >= 0 else []


def h1_basis(d):
    return list(range(d+1, 0)) if d <= -2 else []


assert h1_basis(1) == []
assert h0_basis(0) == [0] and h0_basis(-1) == [] and h1_basis(-1) == []
direct_images = [[0], [0, -1], [-1]]
total = [0, 0, 0, 0]
for q, degrees in enumerate(direct_images):
    for d in degrees:
        total[q] += len(h0_basis(d))
        total[q+1] += len(h1_basis(d))
assert total == [1, 1, 0, 0]
print('two-chart Cech monomial enumeration and Leray: h^q(O_Y)=', total)
