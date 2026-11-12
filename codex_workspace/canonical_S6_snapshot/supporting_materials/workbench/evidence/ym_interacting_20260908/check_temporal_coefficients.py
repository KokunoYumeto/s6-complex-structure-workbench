"""Exact finite algebra checks for temporal_transfer.tex; no numerical limit."""
import sympy as s


def zero(value):
    assert s.simplify(value) == 0, value


def matrix_zero(value):
    for entry in value:
        zero(entry)


checks = 0
a, eps, g2, b, x = s.symbols('a eps g2 b x', positive=True)
bt = a / (2 * g2 * eps)
bs = eps / (2 * g2 * a)
zero(bt * (a * eps)**2 / (a**3 * eps) - 1 / (2 * g2))
zero(bs * a**4 / (a**3 * eps) - 1 / (2 * g2))
zero(bs / eps - 1 / (2 * g2 * a))
zero((2 * g2 / a) / 4 - g2 / (2 * a))
checks += 4


def bessel_polynomial(d, cutoff):
    return sum(b**(2 * r + d) / (s.factorial(r) * s.factorial(r + d))
               for r in range(cutoff + 1))


for d in range(1, 10):
    # Exact formal coefficients, no use of floating point or Bessel asymptotics.
    recurrence = (bessel_polynomial(d - 1, 10)
                  - bessel_polynomial(d + 1, 10)
                  - s.Integer(d) * bessel_polynomial(d, 10) / b)
    for power in range(d - 1, d + 18):
        zero(s.expand(recurrence).coeff(b, power))
        checks += 1
    character = s.chebyshevu(d - 1, x)
    zero(character.subs(x, 1) - d)
    zero(s.diff(character, x).subs(x, 1) / d - s.Rational(d*d - 1, 3))
    casimir = s.Rational(d*d - 1, 4)
    first_coefficient = s.Rational(d*d - 1, 3) * s.Rational(3, 4)
    zero(first_coefficient - casimir)
    zero((casimir / bt) / eps - 2 * g2 * casimir / a)
    checks += 4

# The two exact leading moment ratios arising from the gamma integrals.
zero(s.gamma(s.Rational(5, 2)) / (2 * s.gamma(s.Rational(3, 2)))
     - s.Rational(3, 4))
zero(s.gamma(s.Rational(7, 2)) / (4 * s.gamma(s.Rational(3, 2)))
     - s.Rational(15, 16))
checks += 2

# Metric convention and its unaltered kinetic coefficient.
sigma = [s.Matrix([[0, 1], [1, 0]]),
         s.Matrix([[0, -s.I], [s.I, 0]]),
         s.diag(1, -1)]
basis = [s.I * q / 2 for q in sigma]
for i, ta in enumerate(basis):
    for j, tb in enumerate(basis):
        zero(-2 * s.trace(ta * tb) - int(i == j))
        zero(-s.trace((2 * ta) * (2 * tb)) / 2 - int(i == j))
        checks += 2
matrix_zero(sum((ta * ta for ta in basis), s.zeros(2))
            + s.Rational(3, 4) * s.eye(2))


def q0(c, d):
    return s.Matrix([[c, d], [-d, c]])


def q1(c, d):
    return s.Matrix([[c, s.I * d], [s.I * d, c]])


u = q0(s.Rational(3, 5), s.Rational(4, 5))
up = q1(s.Rational(5, 13), s.Rational(12, 13))
vs = s.diag(s.I, -s.I)
vt = q0(s.Rational(8, 17), s.Rational(15, 17))
h0s, h0t, h1s, h1t = up, vt, u, vs
for value in (u, up, vs, vt):
    matrix_zero(value.H * value - s.eye(2))
    zero(value.det() - 1)
    checks += 1

plaquette = u * vt * up.H * vs.H
transformed_future = vs * up * vt.H
matrix_zero(plaquette.H - transformed_future * u.H)
zero(s.re(s.trace(plaquette))
     - s.re(s.trace(transformed_future * u.H)))
checks += 1

# Original inverse-transport gauge law h_source^-1 U h_target at both times.
u_h = h0s.H * u * h0t
up_h = h1s.H * up * h1t
vs_h = h0s.H * vs * h1s
vt_h = h0t.H * vt * h1t
p_h = u_h * vt_h * up_h.H * vs_h.H
matrix_zero(p_h - h0s.H * plaquette * h0s)
# Dictionary alpha_g=beta_h with g=h^-1.
gs, gt = h0s.H, h0t.H
matrix_zero(gs * u * gt.H - u_h)

# Symmetric endpoint magnetic weights produce one complete interior slice.
v0, v1, v2 = s.symbols('v0 v1 v2', real=True)
zero(eps * (v0 + v1) / 2 + eps * (v1 + v2) / 2
     - eps * (v0 / 2 + v1 + v2 / 2))
checks += 1

print(f'PASS: {checks} exact scalar assertions, plus exact matrix-entry checks.')
print('Checked anisotropic action coefficients, spin multiplier coefficients,')
print('SU(2) metrics/Casimir, temporal plaquette ordering, gauge dictionary,')
print('and symmetric magnetic endpoint weights. No numerical vacuum was used.')
