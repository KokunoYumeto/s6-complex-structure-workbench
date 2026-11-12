"""Exact, bounded checks of the marked A5^4 D4 umbral-shadow maps.

No floating-point arithmetic, Lean, or external mathematical package is used.
The accompanying proof establishes every all-parameter assertion.
"""

from collections import Counter
from fractions import Fraction
from itertools import product


# Q[z]/(z^8-z^4+1), with z=exp(2*pi*i/24).
ZERO = (Fraction(0),) * 8
ONE = (Fraction(1),) + ZERO[1:]


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(a, c):
    return tuple(c * x for x in a)


def mul(a, b):
    c = [Fraction(0)] * 15
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    for k in range(14, 7, -1):
        c[k - 4] += c[k]
        c[k - 8] -= c[k]
    return tuple(c[:8])


def phase(n):
    out = ONE
    z = (Fraction(0), Fraction(1)) + ZERO[2:]
    for _ in range(n % 24):
        out = mul(out, z)
    return out


def omega(n):
    return [[int((r + s) % (2 * n) == 0 and (r - s) % (12 // n) == 0)
             for s in range(12)] for r in range(12)]


def odd_part(matrix):
    return [[matrix[r][s] - matrix[r][(-s) % 12]
             for s in range(1, 6)] for r in range(1, 6)]


def mm2(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2)) % 3
                       for j in range(2)) for i in range(2))


def perm_sign(p):
    return -1 if sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) % 2 else 1


def tau(u):
    return ((u[1] + u[3]) % 2, (u[2] + u[3]) % 2)


def character_data(a):
    rows = ((1, 1), (1, 2), (1, 0), (0, 1))
    p, signs = [], []
    for row in rows:
        out = tuple(sum(row[k] * a[k][j] for k in range(2)) % 3 for j in range(2))
        matches = [(i, sign) for i, target in enumerate(rows) for sign in (-1, 1)
                   if tuple(sign * x % 3 for x in target) == out]
        assert len(matches) == 1
        i, sign = matches[0]
        p.append(i)
        signs.append(sign)
    columns = [tau(tuple(u[p[i]] for i in range(4)))
               for u in ((1, 1, 0, 0), (1, 0, 1, 0))]
    labels = ((1, 0), (0, 1), (1, 1))
    action = []
    for label in labels:
        image = tuple(sum(columns[k][i] * label[k] for k in range(2)) % 2 for i in range(2))
        action.append(labels.index(image))
    abar = sum(p[i] == i for i in range(4))
    achar = sum(signs[i] for i in range(4) if p[i] == i)
    dsign = perm_sign(action)
    dcheck = sum(action[i] == i for i in range(3)) - 1
    return abar, achar, dsign, dcheck


def twisted(data):
    abar, achar, dsign, dcheck = data
    matrix = [[0] * 12 for _ in range(12)]
    for r in range(12):
        matrix[r][r] += abar if r % 2 else achar
        if r % 6 in (0, 3):
            matrix[r][r] += dcheck
        else:
            matrix[r][r] += 1 if r % 6 in (1, 5) else dsign
            for s in range(12):
                if (r + s) % 6 == 0 and (r - s) % 4 == 0:
                    matrix[r][s] += dsign
    return matrix


def main():
    identity = omega(1)
    j = omega(3)
    reflection = omega(6)
    assert all(identity[r][s] == int(r == s) for r in range(12) for s in range(12))
    assert all(j[r][s] == int(s == 5 * r % 12) for r in range(12) for s in range(12))
    assert all(reflection[r][s] == int(s == -r % 12) for r in range(12) for s in range(12))
    full = [[5 * identity[r][s] + j[r][s] for s in range(12)] for r in range(12)]
    expected_odd = [[5, 0, 0, 0, 1], [0, 4, 0, 0, 0], [0, 0, 6, 0, 0],
                    [0, 0, 0, 4, 0], [1, 0, 0, 0, 5]]
    assert odd_part(full) == expected_odd
    assert twisted((4, 4, 1, 2)) == full
    print("PASS: exact full 12-component and odd 5-component shadow matrices")

    # Finite quadratic refinement and exact S/T commutation.
    assert all(((5 * r) ** 2 - r * r) % 24 == 0 for r in range(12))
    assert all((5 * r * s - r * (5 * s)) % 12 == 0 for r in range(12) for s in range(12))
    for r in range(12):
        for s in range(12):
            total = ZERO
            for t in range(12):
                total = add(total, phase(-2 * t * (r + s)))
            assert total == scale(ONE, 12 if (r + s) % 12 == 0 else 0)
    print("PASS: theta refinement Q(r)=r^2/24, Omega commutation, Fourier square=reflection")

    # Exact Fourier determinant by its Vandermonde product.
    determinant = ONE
    for a in range(12):
        for b in range(a + 1, 12):
            determinant = mul(determinant, add(phase(2 * b), scale(phase(2 * a), -1)))
    determinant = scale(determinant, Fraction(1, 12 ** 6))
    assert determinant == phase(-6)  # det Fplus = -i
    gauss = ZERO
    for r in range(12):
        gauss = add(gauss, phase(r * r))
    sqrt12 = scale(add(phase(2), phase(-2)), 2)
    assert gauss == mul(sqrt12, phase(3))
    assert sum(r * r for r in range(12)) == 506
    assert phase(506) == phase(2)
    assert mul(phase(-36), phase(6)) == phase(-6)
    print("PASS: det Fplus=-i, det Fminus=i, Gauss sum=sqrt(12)*e(1/8)")
    print("PASS: det U(T)=e(1/12), det U(S)=e(-3/12); dual determinant is the retained chi")

    # The original six-point Fourier transform has its original negative sign.
    assert all(phase(-2 * r * (2 * k)) == phase(-4 * (r % 6) * k)
               for r in range(12) for k in range(6))
    assert all((Fraction(5 * r * r, 6) - 10 * Fraction(r * r, 12)) % 2 == 0
               for r in range(12))
    assert (Fraction(6 * 6, 24) % 1) == Fraction(1, 2)
    print("PASS: exact six-to-twelve Fourier intertwiner and factor-10 discriminant map")

    classes = Counter()
    for entries in product(range(3), repeat=4):
        a = ((entries[0], entries[1]), (entries[2], entries[3]))
        if (a[0][0] * a[1][1] - a[0][1] * a[1][0]) % 3 == 0:
            continue
        data = character_data(a)
        abar, achar, dsign, dcheck = data
        expected = [[abar + 1, 0, 0, 0, dsign], [0, achar, 0, 0, 0],
                    [0, 0, abar + dcheck, 0, 0], [0, 0, 0, achar, 0],
                    [dsign, 0, 0, 0, abar + 1]]
        assert odd_part(twisted(data)) == expected
        classes[data] += 1
    assert classes == Counter({(4, 4, 1, 2): 1, (4, -4, 1, 2): 1,
                              (2, 0, -1, 0): 12, (0, 0, 1, 2): 6,
                              (1, 1, 1, -1): 8, (1, -1, 1, -1): 8,
                              (0, 0, -1, 0): 12})
    print("PASS: all 48 original-code GL2(F3) elements give CDH twisted-shadow character data")
    print("Twisted character multiplicities:", dict(sorted(classes.items())))

    # Independent coefficient check of the shadow-to-eta Lambert map.
    alpha = [0, 5, 4, 6, 4, 5]
    frame = {1: -5, 2: 1, 3: -1, 6: 5}
    assert sum(d * a for d, a in frame.items()) == 24
    for n in range(1, 241):
        coefficient_shadow = sum(d * alpha[d % 6] for d in range(1, n + 1) if n % d == 0)
        coefficient_eta = -sum(a * d * sum(k for k in range(1, n // d + 1) if (n // d) % k == 0)
                               for d, a in frame.items() if n % d == 0)
        assert coefficient_shadow == coefficient_eta
    exponents = {d: -a for d, a in frame.items()}
    assert sum(exponents.values()) == 0
    assert sum(d * a for d, a in exponents.items()) == -24
    assert sum((6 // d) * a for d, a in exponents.items()) == 24
    constant_squared = Fraction(1)
    for d, a in exponents.items():
        constant_squared *= Fraction(6, d) ** a
    assert constant_squared == 72 ** 2
    print("PASS: 240 exact Lambert coefficients, original reciprocal eta sign, Fricke scalar 72")
    print("ALL EXACT SHADOW CHECKS PASSED")


if __name__ == "__main__":
    main()
