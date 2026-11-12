"""Small exact algebra checks for wilson_finite_lattice.tex.

This verifies finite matrix identities and one product-rule identity. It does
not compute a Yang--Mills vacuum, any continuum limit, or any spectral gap.
Run: python check_wilson_exact.py
"""

import sympy as s


def su_basis(n):
    out = []
    for i in range(n):
        for j in range(i + 1, n):
            a, b = s.zeros(n), s.zeros(n)
            a[i, j], a[j, i] = s.Rational(1, 2), -s.Rational(1, 2)
            b[i, j] = b[j, i] = s.I / 2
            out.extend((a, b))
    for k in range(1, n):
        d = [1] * k + [-k] + [0] * (n - k - 1)
        out.append(s.I * s.diag(*d) / s.sqrt(2 * k * (k + 1)))
    return out


def zero(x):
    assert s.simplify(x) == 0, x


def matrix_zero(a):
    for x in a:
        zero(x)


checks = 0
for n in (2, 3, 4):
    basis = su_basis(n)
    assert len(basis) == n * n - 1
    for a, ta in enumerate(basis):
        matrix_zero(ta.H + ta)
        zero(s.trace(ta))
        for b, tb in enumerate(basis):
            zero(-2 * s.trace(ta * tb) - int(a == b))
            zero(-s.trace((2 * ta) * (2 * tb)) / 2 - int(a == b))
            checks += 2
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    lhs = sum(ta[i, j] * ta[k, l] for ta in basis)
                    rhs = -(s.Integer(i == l) * int(j == k)
                            - s.Rational(1, n) * int(i == j) * int(k == l)) / 2
                    zero(lhs - rhs)
                    checks += 1
    casimir = sum((ta * ta for ta in basis), s.zeros(n))
    matrix_zero(casimir + s.Rational(n * n - 1, 2 * n) * s.eye(n))
    checks += n * n

n = 3
basis = su_basis(n)
u = s.Matrix([[s.Rational(3, 5), s.Rational(4, 5), 0],
              [-s.Rational(4, 5), s.Rational(3, 5), 0], [0, 0, 1]])
r = s.Matrix([[1, 0, 0], [0, s.Rational(5, 13), 12 * s.I / 13],
              [0, 12 * s.I / 13, s.Rational(5, 13)]])
v = s.diag(s.I, -s.I, 1)
for m in (u, r, v):
    matrix_zero(m.H * m - s.eye(n))
    zero(m.det() - 1)

ap, am = u * r, v * u.H
wp, wm = s.trace(ap), s.trace(am)
dp = [s.trace(ta * u * r) for ta in basis]
dm = [-s.trace(u.H * ta * v) for ta in basis]
for ta, d in zip(basis, dm):
    zero(d + s.trace(ta * am))
    checks += 1
for a, w, ds in ((ap, wp, dp), (am, wm, dm)):
    zero(sum(d * s.conjugate(d) for d in ds)
         - (n * n - w * s.conjugate(w)) / (2 * n))
    zero(sum(d * d for d in ds)
         + (s.trace(a * a) - w * w / n) / 2)
    zero(sum(s.re(d) ** 2 for d in ds)
         - (n - s.re(s.trace(a * a)) - 2 * s.im(w) ** 2 / n) / 4)
    checks += 3

zero(sum(x * s.conjugate(y) for x, y in zip(dp, dm))
     + (s.trace(ap * am.H) - wp * s.conjugate(wm) / n) / 2)
zero(sum(x * y for x, y in zip(dp, dm))
     - (s.trace(ap * am) - wp * wm / n) / 2)
checks += 2

# A word with two occurrences of the same physical edge, with opposite signs.
a1, a2 = u * r * u.H * v, v * u * r * u.H
ds = [s.trace(ta * u * r * u.H * v - u * r * u.H * ta * v)
      for ta in basis]
for ta, d in zip(basis, ds):
    zero(d - s.trace(ta * a1) + s.trace(ta * a2))
    # Setting v=I makes the trace of u*r*u^-1 independent of u.
    zero(s.trace(ta * u * r * u.H - u * r * u.H * ta))
    checks += 2
rhs = 0
for eps, a in ((1, a1), (-1, a2)):
    for eta, b in ((1, a1), (-1, a2)):
        rhs += eps * eta * (s.trace(a * b.H)
                            - s.trace(a) * s.conjugate(s.trace(b)) / n) / 2
zero(sum(d * s.conjugate(d) for d in ds) - rhs)
checks += 1

# Exact local ground-state product rule in one coordinate, arbitrary functions.
x = s.symbols('x', real=True)
kappa = s.symbols('kappa', positive=True)
psi, f, g = (s.Function(z)(x) for z in ('psi', 'f', 'g'))
potential_minus_ground = kappa * s.diff(psi, x, 2) / psi
shifted_h = -kappa * s.diff(psi * g, x, 2) + potential_minus_ground * psi * g
identity = (psi * f * shifted_h
            - kappa * psi**2 * s.diff(f, x) * s.diff(g, x)
            + kappa * s.diff(psi**2 * f * s.diff(g, x), x))
zero(identity)
checks += 1

print(f'PASS: {checks} exact scalar assertions, plus exact matrix entries.')
print('Checked SU(2), SU(3), SU(4) Fierz normalization and Casimir; metric factor 4;')
print('oriented SU(3) loop contractions, repeated-edge terms, real trace, product rule.')
print('No interacting vacuum or continuum spectrum was computed.')
