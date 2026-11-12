"""Independent exact certificate replay with standard-library arithmetic only.

Reads the supplied JSON data, never imports or executes the supplied checkers.
Reconstructs the witness residuals from the FULL eight-dimensional Gauss
matrix, using no seven-dimensional Schur-adjugate coefficient recursion.
One process, no child processes, 55-second watchdog.
"""
import ast
from fractions import Fraction
import json
import os
from pathlib import Path
import threading
import time

START = time.monotonic()
WATCHDOG = threading.Timer(55.0, lambda: os._exit(124))
WATCHDOG.daemon = True
WATCHDOG.start()
ROOT = Path(__file__).resolve().parents[1] / "finite_coupling_root_20260905"
EXACT = json.loads((ROOT / "PAIR_BEZOUT_CERTIFICATE.json").read_text())
MOD = json.loads((ROOT / "PAIR_MODULAR_CERTIFICATE.json").read_text())
P = 101

# Exact arithmetic in Q[s]/(s^2-6); all numerators and denominators retained.
class Quadratic:
    def __init__(self, a=0, b=0):
        self.a = Fraction(a)
        self.b = Fraction(b)

    def __add__(self, other):
        return Quadratic(self.a + other.a, self.b + other.b)

    def __neg__(self):
        return Quadratic(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        return Quadratic(self.a * other.a + 6 * self.b * other.b,
                         self.a * other.b + self.b * other.a)

    def __truediv__(self, other):
        denominator = other.a**2 - 6 * other.b**2
        assert denominator != 0
        return self * Quadratic(other.a / denominator, -other.b / denominator)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def mod(self):
        def rational(f):
            assert f.denominator % P != 0
            return f.numerator * pow(f.denominator, -1, P) % P
        return (rational(self.a) + 39 * rational(self.b)) % P


def parse_coefficient(text):
    def visit(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, int):
            return Quadratic(node.value)
        if isinstance(node, ast.Call):
            assert isinstance(node.func, ast.Name) and node.func.id == "sqrt"
            assert len(node.args) == 1 and node.args[0].value == 6
            return Quadratic(0, 1)
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return -visit(node.operand)
        if isinstance(node, ast.BinOp):
            left, right = visit(node.left), visit(node.right)
            if isinstance(node.op, ast.Add):
                return left + right
            if isinstance(node.op, ast.Sub):
                return left - right
            if isinstance(node.op, ast.Mult):
                return left * right
            if isinstance(node.op, ast.Div):
                return left / right
        raise AssertionError(ast.dump(node))
    return visit(ast.parse(text, mode="eval").body)


def convolution(left, right, zero):
    result = [zero for _ in range(len(left) + len(right) - 1)]
    for j, a in enumerate(left):
        for k, b in enumerate(right):
            result[j + k] = result[j + k] + a * b
    return result


assert 39 * 39 % P == 6
mc = MOD["coefficients_descending"]
mf, mg, ma, mb = (mc[k] for k in ("P_H11", "P_H22", "A", "B"))
integer_identity = [(a + b) % P for a, b in zip(
    convolution(ma, mf, 0), convolution(mb, mg, 0))]
assert integer_identity == [0] * 23 + [1]
print("PASS: independent ordinary-integer modular convolution: 23 zeros then 1", flush=True)

f, g, a, b = ([parse_coefficient(v) for v in EXACT[key]] for key in (
    "original_left_coefficients_descending",
    "original_right_coefficients_descending",
    "bezout_A_coefficients_descending",
    "bezout_B_coefficients_descending"))
assert [v.mod() for v in f] == mf
assert [v.mod() for v in g] == mg
assert len(f) == len(g) == 13 and len(a) <= 12 and len(b) <= 12
assert mf[0] and mg[0]
rational_identity = [x + y for x, y in zip(
    convolution(a, f, Quadratic()), convolution(b, g, Quadratic()))]
assert rational_identity == [Quadratic()] * 23 + [Quadratic(1)]
assert [parse_coefficient(v) for v in EXACT["gcd_coefficients_descending"]] == [Quadratic(1)]
print("PASS: exact Q(sqrt6) Bezout convolution and all original coefficient reductions", flush=True)

# Retained witness constants and one exact nonzero bracket entry, over Q[i].
def exact_product(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def exact_dot(a, b):
    terms = [exact_product(x, y) for x, y in zip(a, b)]
    return tuple(sum(term[k] for term in terms) for k in (0, 1))


left21 = exact_dot([(1, 1), (0, Fraction(1, 2)), (2, -1)],
                   [(0, -2), (2, 3), (1, -1)])
right21 = exact_dot([(2, 3), (0, Fraction(3, 2)), (-1, 2)],
                    [(0, 1), (1, 1), (-1, 2)])
assert tuple(x - y for x, y in zip(left21, right21)) == (9, Fraction(-7, 2))
assert Fraction(3, 4) * (7 + 15) + 3 * (5 + 5) == Fraction(93, 2)
assert Fraction(1, 4) + Fraction(8 + 19, 8) == Fraction(29, 8)
print("PASS: exact witness bracket entry 9-(7/2)i, eta=93/2, alpha=29/8", flush=True)

# Complex matrices are pairs in F101[i]/(i^2+1). Conjugation sends (a,b)
# to (a,-b), so no invalid identification of complex conjugation occurs.
Z = (0, 0)
ONE = (1, 0)
IMAG = (0, 1)


def cadd(a, b):
    return ((a[0] + b[0]) % P, (a[1] + b[1]) % P)


def cneg(a):
    return (-a[0] % P, -a[1] % P)


def cmul(a, b):
    return ((a[0] * b[0] - a[1] * b[1]) % P,
            (a[0] * b[1] + a[1] * b[0]) % P)


def cconj(a):
    return (a[0], -a[1] % P)


def cscale(k, a):
    return (k * a[0] % P, k * a[1] % P)


def zero_matrix():
    return [[Z for _ in range(3)] for _ in range(3)]


def madd(a, b):
    return [[cadd(a[j][k], b[j][k]) for k in range(3)] for j in range(3)]


def mscale(k, a):
    return [[cscale(k, e) for e in row] for row in a]


def mmul(a, b):
    result = zero_matrix()
    for j in range(3):
        for k in range(3):
            for ell in range(3):
                result[j][k] = cadd(result[j][k], cmul(a[j][ell], b[ell][k]))
    return result


def comm(a, b):
    return madd(mmul(a, b), mscale(-1, mmul(b, a)))


def trace(a):
    result = Z
    for j in range(3):
        result = cadd(result, a[j][j])
    return result


def ip(a, b):
    result = cneg(trace(mmul(a, b)))
    assert result[1] == 0
    return result[0]


def su(a, h, v1, v2, z):
    return [[(0, a % P), cneg(cconj(v1)), cneg(cconj(v2))],
            [v1, (0, (h - a) * pow(2, -1, P) % P), z],
            [v2, cneg(cconj(z)), (0, -(h + a) * pow(2, -1, P) % P)]]


def coords(a):
    return [a[0][0][1], (a[0][0][1] + 2 * a[1][1][1]) % P,
            *a[1][0], *a[2][0], *a[1][2]]


def lift(a):
    return su(a[0], a[1], (a[2], a[3]), (a[4], a[5]), (a[6], a[7]))


def diag(a):
    result = zero_matrix()
    for j, entry in enumerate(a):
        result[j][j] = entry
    return result


r = 39 * pow(4, -1, P) % P
H = diag([(0, 0), (r, 0), (-r % P, 0)])
J = diag([(0, 0), (0, r), (0, -r % P)])
F = diag([(-2 % P, 0), ((1 - 2 * r) % P, 0), ((1 + 2 * r) % P, 0)])
QQ = diag([(pow(8, -1, P), 0), Z, Z])
Z1 = su(1, 2, (1, 1), (-1 % P, 2), (2, -1 % P))
Z2 = su(-2, 1, (2, 3), (1, -1 % P), (-1 % P, 2))


def inertia(a):
    result = madd(comm(H, comm(H, a)), madd(mmul(QQ, a), mmul(a, QQ)))
    correction = cscale(-pow(3, -1, P), trace(result))
    return madd(result, diag([correction] * 3))


def kop(a):
    return mscale(-1, madd(comm(Z1, comm(Z1, a)), comm(Z2, comm(Z2, a))))


basis = [lift([int(j == k) for j in range(8)]) for k in range(8)]
Icols = [coords(inertia(e)) for e in basis]
Kcols = [coords(kop(e)) for e in basis]
I8 = [[Icols[k][j] for k in range(8)] for j in range(8)]
K8 = [[Kcols[k][j] for k in range(8)] for j in range(8)]
Bc = coords(comm(Z1, Z2))
eta = ip(J, kop(J))
jnorm = ip(J, J)
assert eta == 93 * pow(2, -1, P) % P
assert jnorm == 3 * pow(4, -1, P) % P
alpha = 29 * pow(8, -1, P) % P
force = madd(F, madd(comm(Z1, comm(Z1, H)), comm(Z2, comm(Z2, H))))


def determinant_and_solve(matrix, rhs):
    a = [row[:] + [value] for row, value in zip(matrix, rhs)]
    determinant = 1
    for j in range(8):
        pivot = next((k for k in range(j, 8) if a[k][j] % P), None)
        if pivot is None:
            return 0, None
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            determinant = -determinant % P
        pv = a[j][j] % P
        determinant = determinant * pv % P
        inv = pow(pv, -1, P)
        a[j] = [value * inv % P for value in a[j]]
        for k in range(8):
            if k == j:
                continue
            factor = a[k][j]
            a[k] = [(x - factor * y) % P for x, y in zip(a[k], a[j])]
    return determinant, [a[j][8] for j in range(8)]


def evaluate(coefficients, t):
    result = 0
    for coefficient in coefficients:
        result = (result * t + coefficient) % P
    return result


checked = []
singular = []
for tv in range(P):
    L = [[(tv * I8[j][k] + 2 * K8[j][k]) % P for k in range(8)] for j in range(8)]
    detL, Tc = determinant_and_solve(L, [4 * value % P for value in Bc])
    if not detL:
        singular.append(tv)
        continue
    # Exact block determinant identity det(L)=(2 eta/<J,J>) D7.
    D = detL * jnorm * pow(2 * eta, -1, P) % P
    N = mscale(D, lift(Tc))
    first_col_norm = 0
    for row in N:
        entry = cmul(cconj(row[0]), row[0])
        assert entry[1] == 0
        first_col_norm = (first_col_norm + entry[0]) % P
    Q = first_col_norm * pow(8, -1, P) % P
    PH = madd(mscale(alpha, comm(N, comm(N, H))), mscale(-Q, force))
    assert PH[0][0] == (evaluate(mf, tv), 0), (tv, PH[0][0])
    assert PH[1][1] == (evaluate(mg, tv), 0), (tv, PH[1][1])
    checked.append(tv)

assert len(checked) >= 13
print(f"PASS: full 8D Gauss reconstruction agrees with both original degree-12 entries at {len(checked)} F101 points; singular t={singular}", flush=True)

# Reconstruct the fixed 24 by 24 Sylvester map directly, without a resultant.
S = [[0 for _ in range(24)] for _ in range(24)]
for k in range(12):
    for j, coefficient in enumerate(reversed(mf)):
        S[k + j][k] = coefficient
    for j, coefficient in enumerate(reversed(mg)):
        S[k + j][12 + k] = coefficient
detS = 1
for j in range(24):
    pivot = next((k for k in range(j, 24) if S[k][j]), None)
    assert pivot is not None
    if pivot != j:
        S[j], S[pivot] = S[pivot], S[j]
        detS = -detS % P
    pv = S[j][j]
    detS = detS * pv % P
    inv = pow(pv, -1, P)
    for k in range(j + 1, 24):
        factor = S[k][j] * inv % P
        S[k] = [(x - factor * y) % P for x, y in zip(S[k], S[j])]
assert detS != 0
cleared_det = detS * pow(eta, 16 * 24, P) % P
assert cleared_det != 0
print(f"PASS: fixed Sylvester determinant={detS}, eta^16-cleared determinant={cleared_det} in F101", flush=True)
WATCHDOG.cancel()
print(f"ALL INDEPENDENT PROJECTION CERTIFICATE CHECKS PASSED in {time.monotonic() - START:.3f}s", flush=True)
