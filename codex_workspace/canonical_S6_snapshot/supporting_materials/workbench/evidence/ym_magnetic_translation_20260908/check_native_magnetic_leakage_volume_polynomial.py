"""Exact polynomial algebra plus independent open-edge incidence enumeration.

No interpolation, external packages, file writes, Lean, or spectral simulation.
The previous checker supplies the unchanged original box construction.
"""

from collections import defaultdict
from fractions import Fraction as F

from check_native_magnetic_physical_band_transport import box


class Polynomial:
    def __init__(self, *coefficients):
        values = [F(x) for x in coefficients] or [F(0)]
        while len(values) > 1 and values[-1] == 0:
            values.pop()
        self.coefficients = tuple(values)

    @staticmethod
    def of(value):
        return value if isinstance(value, Polynomial) else Polynomial(value)

    def __add__(self, other):
        other = self.of(other)
        a, b = self.coefficients, other.coefficients
        return Polynomial(*(sum((seq[i] for seq in (a, b) if i < len(seq)), F(0))
                            for i in range(max(len(a), len(b)))))

    __radd__ = __add__

    def __neg__(self):
        return Polynomial(*(-x for x in self.coefficients))

    def __sub__(self, other):
        return self + -self.of(other)

    def __rsub__(self, other):
        return self.of(other) + -self

    def __mul__(self, other):
        other = self.of(other)
        values = [F(0)] * (len(self.coefficients) + len(other.coefficients) - 1)
        for i, a in enumerate(self.coefficients):
            for j, b in enumerate(other.coefficients):
                values[i + j] += a * b
        return Polynomial(*values)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        return Polynomial(*(x / F(scalar) for x in self.coefficients))

    def __pow__(self, exponent):
        assert isinstance(exponent, int) and exponent >= 0
        result = Polynomial(1)
        for _ in range(exponent):
            result *= self
        return result

    def __eq__(self, other):
        return self.coefficients == self.of(other).coefficients

    def evaluate(self, value):
        result = F(0)
        for a in reversed(self.coefficients):
            result = result * value + a
        return result


X = Polynomial(0, 1)
S0 = 2 * X
S1 = -X
S2 = (2 * X ** 3 + X) / 3
S3 = -X ** 3
S4 = (6 * X ** 5 + 10 * X ** 3 - X) / 15
F4 = S4 + X ** 4
I4 = F4 - 2 * X ** 4
I2 = (2 * X ** 3 - 3 * X ** 2 + X) / 3
I0 = 2 * X - 1
SUM_R2 = S4 + 2 * S3 + 2 * S2 + S1 + S0 / 4


def classification_polynomials(c, d):
    c, d = F(c), F(d)
    t = c + d
    return {
        (1, "coplanar12"): 2 * X * (2 * X + 1) *
            (t ** 2 * I4 + t * c * I2 + c ** 2 * I0 / 4),
        (1, "coplanar13"): 2 * X * (2 * X - 1) * t ** 2 * F4,
        (1, "hinged"): 16 * X ** 2 *
            (t ** 2 * S4 + t * c * S3 + (t * c / 2 + c ** 2 / 4) * S2
             + c ** 2 * S1 / 4 + c ** 2 * S0 / 16),
        (2, "coplanar12"): c ** 2 * (2 * X - 1) * (2 * X + 1) * SUM_R2,
        (2, "coplanar23"): Polynomial(0),
        (2, "hinged"): 4 * X ** 2 * c ** 2 * SUM_R2,
        (3, "coplanar13"): 2 * X * (2 * X - 1) * c ** 2 * F4,
        (3, "coplanar23"): Polynomial(0),
        (3, "hinged"): 2 * X ** 2 * c ** 2 * (2 * F4 - 2 * X ** 4),
    }


def expanded_pair_polynomial(c, d):
    c, d = F(c), F(d)
    return Polynomial(
        0,
        -3 * c ** 2 / 5,
        4 * c ** 2 / 5 + 2 * c * d / 3,
        2 * c ** 2 - 6 * c * d / 5 - 8 * d ** 2 / 5,
        -4 * c ** 2 - 8 * c * d / 3,
        48 * c ** 2 / 5 + 16 * c * d + 12 * d ** 2,
        16 * c ** 2 / 5,
        16 * c ** 2 + 96 * c * d / 5 + 48 * d ** 2 / 5,
    )


def check_coefficient_algebra():
    assert SUM_R2 == X * (4 * X ** 4 + 1) / 10
    # A homogeneous quadratic in (c,d) is determined by these three
    # evaluations. Each assertion compares the entire L polynomial.
    for c, d in [(1, 0), (0, 1), (1, 1), (3, 7)]:
        actual = sum(classification_polynomials(c, d).values(), Polynomial(0))
        assert actual == expanded_pair_polynomial(c, d)
    mass = (2 * X * (2 * X + 1) * SUM_R2 + 4 * X ** 2 * F4) / 4
    assert mass == Polynomial(0, 0, F(1, 20), F(1, 30), 0, F(2, 3), F(6, 5), F(4, 5))
    h11 = expanded_pair_polynomial(1, 1)
    h37 = expanded_pair_polynomial(3, 7)
    assert h11 == Polynomial(0, -F(3, 5), F(22, 15), -F(4, 5), -F(20, 3),
                            F(188, 5), F(16, 5), F(224, 5))
    assert h37 == Polynomial(0, -F(27, 5), F(106, 5), -F(428, 5), -92,
                            F(5052, 5), F(144, 5), F(5088, 5))
    leakage = F(4, 225) * mass + h11 / 81 + h37 / 24843
    assert leakage == Polynomial(0, -1917900, 4992787, -3201942, -21634000,
                                 129973560, 15594888, 153001392) / 251535375
    C = F(12750116, 16769025)
    B = F(54848, 51597)
    assert C == F(4, 225) + F(56, 81) + F(424, 8281)
    P5 = Polynomial(19179, 45698, 95770, 216340, -24724, 2139072)
    P4 = Polynomial(114513, 43430, -95770, 1566220, 3233332)
    assert C * mass - leakage == 4 * X * P5 / 10061415
    assert mass.coefficients[0] == 0
    mass_over_X = Polynomial(*mass.coefficients[1:])
    assert leakage - C * mass + B * mass_over_X == 4 * X * P4 / 10061415
    # Leading-ratio and first-correction identities also follow directly
    # from the top two coefficients of the exact polynomials.
    assert leakage.coefficients[7] / mass.coefficients[7] == C
    assert ((leakage.coefficients[6] - C * mass.coefficients[6]) /
            mass.coefficients[7]) == -B
    assert F(4, 9) * F(1, 4) ** 4 == F(1, 576)
    assert F(16, 576) == F(1, 36)
    return mass, leakage


def direct_check(L, mass, leakage):
    faces, w, a, adjacent = box(L)
    a4 = {p: int(4 * ap) for p, ap in a.items()}
    assert all(F(a4[p], 4) == a[p] for p in faces)
    exact_mass = F(sum(ap ** 2 for ap in a4.values()), 16)
    assert exact_mass == mass.evaluate(L)
    count_by_type = defaultdict(int)
    sums = {(1, 1): defaultdict(int), (3, 7): defaultdict(int)}
    for p, q, e in adjacent:
        i = e[1] + 1
        if p[1:] == q[1:]:
            kind = "coplanar" + "".join(str(j + 1) for j in p[1:])
        else:
            kind = "hinged"
        key = (i, kind)
        count_by_type[key] += 1
        for (c, d), totals in sums.items():
            # The original a values have denominator 4; this integer
            # expression evaluates the original squared sum exactly.
            totals[key] += (c * (a4[p] + a4[q]) + 4 * d * w[e]) ** 2
    for i in range(1, 4):
        assert sum(n for (j, _), n in count_by_type.items() if i == j) == 48 * L ** 3 - 4 * L
        assert count_by_type[i, "hinged"] == 32 * L ** 3
    assert sum(count_by_type.values()) == 144 * L ** 3 - 12 * L
    values = {}
    for (c, d), totals in sums.items():
        for key, poly in classification_polynomials(c, d).items():
            assert F(totals[key], 16) == poly.evaluate(L), (L, c, d, key)
        values[c, d] = F(sum(totals.values()), 16)
        assert values[c, d] == expanded_pair_polynomial(c, d).evaluate(L)
    exact_leakage = F(4, 225) * exact_mass + values[1, 1] / 81 + values[3, 7] / 24843
    assert exact_leakage == leakage.evaluate(L)
    ratio = exact_leakage / exact_mass
    C, B = F(12750116, 16769025), F(54848, 51597)
    assert 0 < ratio < C
    assert 0 < ratio - C + B / L <= F(24787475, 10061415 * L ** 2)
    print(f"L={L}: pairs={len(adjacent)}; A_L={exact_mass}; R_L={exact_leakage}; R_L/A_L={ratio}")


if __name__ == "__main__":
    mass_polynomial, leakage_polynomial = check_coefficient_algebra()
    print("PASS: complete polynomial coefficient algebra, exact ratio identities, and amplitude factors.")
    for L in range(2, 9):
        direct_check(L, mass_polynomial, leakage_polynomial)
    print("PASS: every coplanar/hinged edge-direction class and open boundary, L=2,...,8; no interpolation.")
