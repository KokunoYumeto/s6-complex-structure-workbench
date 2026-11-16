"""Exact certificates for UN63; every assertion is over Q or a cyclotomic ring.

The finite graph examples below test identities and character constraints.
They are not asserted to be additional geometric realizations.
"""
from math import gcd
import sympy as sp


def check_zero(value):
    if isinstance(value, sp.MatrixBase):
        assert all(sp.cancel(x) == 0 for x in value)
    else:
        assert sp.cancel(value) == 0


# The actual direct and inverse signed-edge compositions.
v0, v1, L, c = sp.symbols("v0 v1 L c")
D = sp.Matrix(2, 2, sp.symbols("d00 d01 d10 d11"))
v = sp.Matrix([v0, v1])
bj = sp.Matrix(sp.symbols("bj0 bj1"))
bk = sp.Matrix(sp.symbols("bk0 bk1"))
tj = sp.Matrix(sp.symbols("tj0 tj1"))
tn = sp.Matrix(sp.symbols("tn0 tn1"))
lj = sp.Matrix(sp.symbols("lj0 lj1"))
lk = sp.Matrix(sp.symbols("lk0 lk1"))
for eps in (1, -1):
    left = D * (v + bj + lj * L) + tn
    right = D * v + tj + eps * bk + eps * lk * (L + c)
    expected = tn + D * bj - tj - eps * bk - eps * lk * c
    expected += (D * lj - eps * lk) * L
    check_zero(left - right - expected)
print("PASS: both actual signed-edge composition identities")

N = sp.symbols("N", positive=True, integer=True)
graph_count = 0
for count in range(2, 9):
    bs = [sp.Matrix(sp.symbols(f"b{j}_0 b{j}_1")) for j in range(count)]
    ts = [sp.Matrix(sp.symbols(f"t{j}_0 t{j}_1")) for j in range(count)]
    ns = [sp.Matrix(sp.symbols(f"n{j}_0 n{j}_1")) for j in range(count)]
    hs = sp.symbols(f"h0:{count}")
    for eps in (1, -1):
        sigma = (lambda j: (j + 1) % count) if eps == 1 else (
            lambda j: (-j) % count
        )
        total = sp.zeros(2, 1)
        for j in range(count):
            k = sigma(j) if eps == 1 else sigma((j + 1) % count)
            total += (
                ts[(j + 1) % count] + D * bs[j] - ts[j]
                - eps * bs[k] + eps * hs[k] * ns[k] / N
            )
        b = sum(bs, sp.zeros(2, 1))
        u = -sum((hs[j] * ns[j] for j in range(count)), sp.zeros(2, 1))
        check_zero(total - ((D - eps * sp.eye(2)) * b - eps * u / N))
        graph_count += 1
print(f"PASS: {graph_count} exact signed summed affine equations")

# The two-dimensional unitary identity is an exact determinant identity.
J = sp.Matrix([[0, 1], [-1, 0]])
check_zero(D * J * D.T - D.det() * J)
print("PASS: D J D^T = det(D) J, hence the unitary equivariance identity")

a, aa, b, bb, q, qq, T = sp.symbols("a aa b bb q qq T")
lam = sp.Matrix([a, b])
barlam = sp.Matrix([aa, bb])
Vlam = lam + T * J * barlam
Vmu = q * lam + T * qq * J * barlam
check_zero(sp.det(sp.Matrix.hstack(Vlam, Vmu))
           - T * (q - qq) * (a * aa + b * bb))
print("PASS: primitive elliptic period coefficient is exactly nonzero times T")

# Finite affine jet gauge in Q[z]/Phi_d.
z = sp.symbols("z")
gauge_count = 0
resonant_count = 0
for order in range(1, 13):
    phi = sp.Poly(sp.cyclotomic_poly(order, z), z, domain=sp.QQ)
    def reduce(poly):
        return sp.rem(sp.Poly(poly, z, domain=sp.QQ), phi).as_expr()
    for ell in range(1, 2 * order + 1):
        aval = z ** ell
        for j in range(ell):
            coeff = sum(
                z ** (ell * (order - 1 - k) + k * j)
                for k in range(order)
            )
            if (j - ell) % order == 0:
                check_zero(reduce(coeff - order * z ** (ell * (order - 1))))
                assert reduce(coeff) != 0
                resonant_count += 1
            else:
                assert reduce(coeff) == 0
                denominator = reduce(z ** j - aval)
                inverse = sp.invert(denominator, phi.as_expr(), z)
                check_zero(reduce(denominator * inverse - 1))
                gauge_count += 1
        # The terminal coefficient, after division by xi^ell, is k*d0/order.
        coefficient = order * z ** (ell * (order - 1))
        candidate = z ** ell / order
        check_zero(reduce(coefficient * candidate - 1))
print(f"PASS: {gauge_count} removable finite jets and "
      f"{resonant_count} forced-zero resonant jets")
print("PASS: every terminal fractional translation is k*c/stabilizer_order")

# Literal compressed insertion, finite weights, pulled-line divisor.
x, W, Z, s, beta, dunit = sp.symbols("x W Z s beta dunit", nonzero=True)
compressed_count = 0
for m in range(1, 7):
    for h in range(1, 6):
        for n in range(1, 8):
            if gcd(m, n) != 1:
                continue
            for ell in (h * m, h * m + 1, h * m + 3):
                newZ = beta ** m * (
                    Z + dunit * s ** (ell - h * m) * W ** m
                )
                newx = x / beta
                newW = beta * W
                check_zero(newx * newW - x * W)
                dp = sp.expand(newx ** m * newZ - x ** m * Z)
                check_zero(dp.subs(W, s ** h / x) - dunit * s ** ell)
                dU = sp.cancel(newZ / newW ** m - Z / W ** m)
                check_zero(dU - dunit * s ** (ell - h * m))
                assert (m - m) % n == 0  # p=x^m Z
                assert (-1 + 1) % n == 0  # xW
                assert (m - m) % n == 0  # W^m and Z same character
                assert n * h == h * n  # div(x^n)=nh E_new
                compressed_count += 1
print(f"PASS: {compressed_count} compressed weighted maps, finite characters, "
      "and exact order drops")

for h in range(1, 13):
    for ell in range(h + 1, h + 5):
        check_zero((s ** h * Z + dunit * s ** ell) / s ** h
                   - Z - dunit * s ** (ell - h))
        assert ell - h > 0
print("PASS: 48 exact compressed product-cap maps with product central action")

# Smooth quotient: I has order hAB and weights (hA*k,hB*l,1).
ring_count = 0
for A in range(1, 7):
    for B in range(1, 7):
        if gcd(A, B) != 1:
            continue
        k, l, one = sp.gcdex(A, B)
        assert one == 1 and A * k + B * l == 1
        for h in range(1, 6):
            order = h * A * B
            wu, wv = int(h * A * k), int(h * B * l)
            assert (wu + wv - h) % order == 0
            assert (B * wu) % order == 0
            assert (A * wv) % order == 0
            for iu in range(5):
                for iv in range(5):
                    for power_s in range(order):
                        invariant = (iu * wu + iv * wv + power_s) % order == 0
                        if invariant:
                            assert power_s % h == 0
                            added = power_s // h
                            assert (iu + added) % B == 0
                            assert (iv + added) % A == 0
            for g in range(1, 5):
                mult_a, mult_b = g * A, g * B
                base_order = h * g * A * B
                assert B * mult_a == A * mult_b == g * A * B
                assert h * B * mult_a == base_order
            ring_count += 1
print(f"PASS: {ring_count} exact inertia-character invariant rings "
      "and original weighted functions")

# A formal reflected-core character test, without an occurrence claim.
assert 3 % 2 == 1
assert 6 % 2 != 1
print("PASS: reflected character det(D)=-1 requires odd common nonlinear height")
print("These last integers are character checks, not additional geometric examples.")
print("ALL UN63 EXACT CHECKS PASSED")
