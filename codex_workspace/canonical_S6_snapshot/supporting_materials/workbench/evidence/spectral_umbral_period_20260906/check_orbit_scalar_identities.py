"""Exact polynomial checks for the orbit certificate; Python standard library only."""
from fractions import Fraction
from itertools import permutations


class P:
    def __init__(self, value=0):
        self.c = ({e: Fraction(v) for e, v in value.items() if v}
                  if isinstance(value, dict) else
                  ({(0, 0, 0, 0): Fraction(value)} if value else {}))

    def __add__(self, other):
        other = other if isinstance(other, P) else P(other)
        result = dict(self.c)
        for e, v in other.c.items():
            result[e] = result.get(e, Fraction(0)) + v
        return P(result)

    __radd__ = __add__

    def __neg__(self):
        return P({e: -v for e, v in self.c.items()})

    def __sub__(self, other):
        return self + (-other if isinstance(other, P) else -P(other))

    def __rsub__(self, other):
        return P(other) - self

    def __mul__(self, other):
        other = other if isinstance(other, P) else P(other)
        result = {}
        for e, v in self.c.items():
            for f, w in other.c.items():
                k = tuple(x + y for x, y in zip(e, f))
                result[k] = result.get(k, Fraction(0)) + v * w
        return P(result)

    __rmul__ = __mul__

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        result = P(1)
        for _ in range(n):
            result *= self
        return result

    def __truediv__(self, scalar):
        return self * Fraction(1, scalar)


def product(items):
    result = P(1)
    for item in items:
        result *= item
    return result


def determinant(matrix):
    result = P()
    for perm in permutations(range(len(matrix))):
        inversions = sum(perm[i] > perm[j] for i in range(len(perm))
                         for j in range(i + 1, len(perm)))
        result += (-1) ** inversions * product(
            matrix[i][perm[i]] for i in range(len(perm)))
    return result


def zero(name, polynomial):
    assert polynomial.c == {}, (name, polynomial.c)
    print("PASS:", name)


a, b, c, mu = [P({tuple(int(i == j) for i in range(4)): 1}) for j in range(4)]
vandermonde = (a - b) * (a - c) * (b - c)
invariant_jacobian = [[1, 1, 1], [2 * a, 2 * b, 2 * c], [b * c, a * c, a * b]]
zero("invariant Jacobian is -2 times the descending Vandermonde",
     determinant(invariant_jacobian) + 2 * vandermonde)
ys = [a, b, -a - b]
s = sum(x ** 2 for x in ys)
d = product(ys)
discriminant = product((ys[i] - ys[j]) ** 2 for i in range(3) for j in range(i + 1, 3))
zero("trace-four is one half trace-two squared", sum(x ** 4 for x in ys) - s ** 2 / 2)
zero("trace-three is three times determinant", sum(x ** 3 for x in ys) - 3 * d)
zero("discriminant is s^3/2 - 27 d^2", discriminant - s ** 3 / 2 + 27 * d ** 2)
zero("normal Gram determinant is discriminant/3",
     s ** 3 / 6 - 9 * d ** 2 - discriminant / 3)
zero("mean-retaining determinant formula",
     product(mu + x for x in ys) - (mu ** 3 - mu * s / 2 + d))
