"""Exact finite diagnostics for the phase-square and radial Gamma formulas.

These symbolic identities check coefficients, signs, polynomial moments, and
scalar generating functions. They do not certify nonlinear operator convergence,
weighted tail bounds, a local continuum construction, or a mass-gap conclusion.
"""

from collections import Counter
from pathlib import Path
import hashlib
import json

import sympy as sp


ROOT = Path(__file__).resolve().parent
checks = []
groups = Counter()


def same(group, name, actual, expected=0):
    difference = sp.cancel(sp.expand(actual - expected))
    if difference != 0:
        difference = sp.simplify(difference)
    if difference != 0:
        raise AssertionError((group, name, difference))
    checks.append(f"{group}: {name}")
    groups[group] += 1


# General variable-coefficient divergence form, including its full potential.
x = sp.symbols("x", real=True)
kappa = sp.symbols("kappa", positive=True)
beta = sp.symbols("beta", real=True)
p, Q, V, f = (sp.Function(name)(x) for name in ("p", "Q", "V", "f"))
phase = sp.exp(sp.I * beta * Q)


def A1(h):
    return -kappa * sp.diff(p * sp.diff(h, x), x) + V * h


def C1(h):
    return sp.expand(A1(Q * h) - Q * A1(h))


J1 = -sp.I * kappa * (
    2 * p * sp.diff(Q, x) * sp.diff(f, x)
    + sp.diff(p * sp.diff(Q, x), x) * f
)
R1 = kappa * p * sp.diff(Q, x) ** 2
conjugated1 = sp.expand(A1(phase * f) / phase)
same("divergence_1d", "full conjugation with variable p and V",
     conjugated1, A1(f) + beta * J1 + beta**2 * R1 * f)
same("divergence_1d", "first commutator including p derivative",
     sp.I * C1(f), J1)
same("divergence_1d", "double commutator sign and factor",
     Q * C1(f) - C1(Q * f), 2 * R1 * f)
same("divergence_1d", "current commutator",
     sp.I * (C1(Q * f) - Q * C1(f)), -2 * sp.I * R1 * f)
same("divergence_1d", "symmetric phase second difference",
     conjugated1 + conjugated1.subs(beta, -beta) - 2 * A1(f),
     2 * beta**2 * R1 * f)
same("divergence_1d", "third nested coordinate commutator",
     Q * (2 * R1 * f) - 2 * R1 * (Q * f))

# A symmetric two-coordinate coefficient matrix with unrestricted cross term.
y = sp.symbols("y", real=True)
coords = (x, y)
p11, p12, p22 = (sp.Function(name)(x, y)
                 for name in ("p11", "p12", "p22"))
P = sp.Matrix([[p11, p12], [p12, p22]])
Q2, V2, f2 = (sp.Function(name)(x, y) for name in ("Q2", "V2", "f2"))


def A2(h):
    return (-kappa * sum(
        sp.diff(P[a, b] * sp.diff(h, coords[b]), coords[a])
        for a in range(2) for b in range(2)) + V2 * h)


def C2(h):
    return sp.expand(A2(Q2 * h) - Q2 * A2(h))


gradient = sp.Matrix([sp.diff(Q2, coordinate) for coordinate in coords])
R2 = kappa * (gradient.T * P * gradient)[0]
same("divergence_2d", "all cross coefficients retained", R2,
     kappa * (p11 * sp.diff(Q2, x)**2
              + 2 * p12 * sp.diff(Q2, x) * sp.diff(Q2, y)
              + p22 * sp.diff(Q2, y)**2))
phase2 = sp.exp(sp.I * beta * Q2)
same("divergence_2d", "full variable matrix conjugation",
     sp.expand(A2(phase2 * f2) / phase2),
     A2(f2) + sp.I * beta * C2(f2) + beta**2 * R2 * f2)
same("divergence_2d", "matrix double commutator",
     Q2 * C2(f2) - C2(Q2 * f2), 2 * R2 * f2)

# The radial Laguerre generator in the original Gamma probability measure.
q = sp.symbols("q", positive=True)
k = sp.symbols("k", positive=True)
radial_f = sp.Function("radial_f")(q)


def N(h):
    return -q * sp.diff(h, q, 2) - (k - q) * sp.diff(h, q)


rho = q**(k - 1) * sp.exp(-q) / sp.gamma(k)
same("radial", "Gamma divergence-form generator",
     -sp.diff(q * rho * sp.diff(radial_f, q), q) / rho, N(radial_f))
same("radial", "vacuum eigenvector", N(sp.Integer(1)))
same("radial", "centered first Laguerre eigenvector", N(q - k), q - k)
same("radial", "full exponential action",
     sp.expand(N(sp.exp(sp.I * beta * q)) / sp.exp(sp.I * beta * q)),
     beta**2 * q + sp.I * beta * (q - k))
commutator = sp.expand(N(q * radial_f) - q * N(radial_f))
same("radial", "coordinate commutator",
     commutator, -2 * q * sp.diff(radial_f, q) + (q - k) * radial_f)
same("radial", "coordinate double commutator",
     q * commutator
     - (N(q * q * radial_f) - q * N(q * radial_f)),
     2 * q * radial_f)
same("radial", "phase conjugation on arbitrary smooth test",
     sp.expand(N(sp.exp(sp.I * beta * q) * radial_f)
               / sp.exp(sp.I * beta * q)),
     N(radial_f) + sp.I * beta * commutator + beta**2 * q * radial_f)
for degree in range(2, 7):
    laguerre = sp.assoc_laguerre(degree, k - 1, q)
    same("radial", f"Laguerre polynomial eigenvalue degree {degree}",
         N(laguerre), degree * laguerre)

# Exact integrations at all three original colors, k = 3/2.
k3 = sp.Rational(3, 2)
moments = {}
for degree in range(9):
    moments[degree] = sp.integrate(q**degree * rho.subs(k, k3), (q, 0, sp.oo))
    same("gamma", f"raw moment degree {degree}",
         moments[degree], sp.rf(k3, degree))
same("gamma", "centered first moment", moments[1] - k3 * moments[0])
same("gamma", "raw centered variance",
     moments[2] - 2 * k3 * moments[1] + k3**2 * moments[0], k3)
same("gamma", "positive centered fourth moment",
     sum(sp.binomial(4, n) * (-k3)**(4 - n) * moments[n]
         for n in range(5)), 3 * k3**2 + 6 * k3)

# Heat ansatz: verify both coefficient ODEs and initial values separately.
u = sp.symbols("u", nonnegative=True)
decay = sp.exp(-u)
D = 1 - sp.I * beta * (1 - decay)
z = sp.I * beta * decay / D
prefactor = D**(-k)
same("heat", "exponent Riccati equation", sp.diff(z, u), z**2 - z)
same("heat", "prefactor logarithmic derivative",
     -k * sp.diff(D, u) / D, k * z)
same("heat", "initial exponent", z.subs(u, 0), sp.I * beta)
same("heat", "initial prefactor", prefactor.subs(u, 0), 1)
same("heat", "entire differential residual",
     -k * sp.diff(D, u) / D + sp.diff(z, u) * q
     - (q * (z**2 - z) + k * z))
same("heat", "denominator squared modulus",
     sp.expand(D * sp.conjugate(D)), 1 + beta**2 * (1 - decay)**2)
same("heat", "exponent real part",
     (z + sp.conjugate(z)) / 2,
     -beta**2 * decay * (1 - decay)
     / (1 + beta**2 * (1 - decay)**2))

# The carrier calculation uses epsilon = 1/sqrt(j) and a fixed symbolic
# c_j value C. These are scalar Taylor coefficients, not operator limits.
eps = sp.symbols("eps", positive=True)
b0, alpha = sp.symbols("b0 alpha", real=True)
C, t = sp.symbols("C t", positive=True)
carrier = b0 / eps
carrier_beta = carrier + alpha
d = sp.symbols("d", real=True)
demodulated = sp.I * carrier_beta * (1 - d) / (1 - sp.I * carrier_beta * d) \
    - sp.I * carrier
same("carrier", "exact demodulated numerator", demodulated,
     (sp.I * alpha - sp.I * carrier_beta * d - carrier * carrier_beta * d)
     / (1 - sp.I * carrier_beta * d))
d_series = sp.series(1 - sp.exp(-t * C * eps**2), eps, 0, 5).removeO()
same("carrier", "time Taylor coefficient", d_series,
     t * C * eps**2 - t**2 * C**2 * eps**4 / 2)
same("carrier", "vanishing phase denominator perturbation",
     sp.series(carrier_beta * d_series, eps, 0, 1).removeO(), 0)
same("carrier", "retained quadratic carrier phase",
     sp.series(carrier * carrier_beta * d_series, eps, 0, 1).removeO(),
     C * b0**2 * t)
same("carrier", "demodulated exponential coefficient",
     sp.series(demodulated.subs(d, d_series), eps, 0, 1).removeO(),
     sp.I * alpha - C * b0**2 * t)
same("carrier", "unbounded first-energy scalar coefficient",
     sp.expand(carrier_beta**2 * C * eps**2),
     C * (b0**2 + 2 * b0 * alpha * eps + alpha**2 * eps**2))
same("carrier", "exact zero-time demodulation",
     demodulated.subs(d, 0), sp.I * alpha)
sigma, a, z1, z2, z3 = sp.symbols("sigma a z1 z2 z3", positive=True)
mode_q = sigma * (z1**2 + z2**2 + z3**2) / 4
same("carrier", "three-color electric square coefficient",
     2 / a * sum(sp.diff(mode_q, v)**2 for v in (z1, z2, z3)),
     (2 * sigma / a) * mode_q)
same("carrier", "symmetric phase-square rescaling",
     (2 * carrier**2 * sp.Symbol("R")) / (2 * b0**2),
     sp.Symbol("R") / eps**2)

# Laplace moments imply the complete complex insertion formula by analytic
# substitution into a positive-real-part parameter. No branch simplification
# of unrestricted complex powers is used here.
zeta = sp.symbols("zeta", positive=True)
for degree in range(6):
    value = sp.integrate(q**(degree + k3 - 1) * sp.exp(-zeta * q)
                         / sp.gamma(k3), (q, 0, sp.oo))
    same("insertion", f"exact Laplace moment degree {degree}",
         value, sp.rf(k3, degree) / zeta**(k3 + degree))
time_left, time_right = sp.symbols("time_left time_right", nonnegative=True)
delta = sp.symbols("delta", real=True)
left_coefficient = sp.I * alpha - C * b0**2 * time_left
right_coefficient = sp.I * delta - C * b0**2 * time_right
same("insertion", "complex Gram denominator sign",
     1 - sp.conjugate(left_coefficient) - right_coefficient,
     1 + C * b0**2 * (time_left + time_right) + sp.I * (alpha - delta))
same("insertion", "origin modulation derivative",
     sp.diff(sp.exp(sp.I * alpha * q) - (1 - sp.I * alpha)**(-k), alpha)
     .subs(alpha, 0) / sp.I, q - k)
same("insertion", "raw centered observable vacuum mass",
     C**2 * (moments[2] - 2 * k3 * moments[1] + k3**2), k3 * C**2)

# Poisson--Gamma mixing: finite exact integrals and factorial-moment algebra.
j, c_j, c_gamma = sp.symbols("j c_j c_gamma", positive=True)
for degree in range(6):
    mixed = (j**degree / sp.factorial(degree)
             * sp.integrate(q**(degree + k3 - 1) * sp.exp(-(j + 1) * q)
                            / sp.gamma(k3), (q, 0, sp.oo)))
    same("poisson_gamma", f"exact mixed mass at n={degree}",
         mixed, sp.rf(k3, degree) * j**degree
         / (sp.factorial(degree) * (j + 1)**(degree + k3)))
zpgf = sp.symbols("zpgf", real=True)
pgf = (1 + j * (1 - zpgf))**(-k)
same("poisson_gamma", "full probability mass", pgf.subs(zpgf, 1), 1)
same("poisson_gamma", "removed vacuum mass", pgf.subs(zpgf, 0), (j + 1)**(-k))
same("poisson_gamma", "first factorial moment",
     sp.diff(pgf, zpgf).subs(zpgf, 1), j * k)
same("poisson_gamma", "second factorial moment",
     sp.diff(pgf, zpgf, 2).subs(zpgf, 1), j**2 * k * (k + 1))
# Direct conditional expansion uses E[N|q]=jq and E[N^2|q]=jq+j^2q^2.
conditional_error = ((c_j / j)**2 * (j * q + j**2 * q**2)
                     - 2 * (c_j / j) * c_gamma * q * (j * q)
                     + c_gamma**2 * q**2)
same("poisson_gamma", "conditional squared coupling error",
     conditional_error, c_j**2 * q / j + (c_j - c_gamma)**2 * q**2)
averaged_error = sp.Poly(sp.expand(conditional_error), q)
averaged_error = sum(coefficient * sp.rf(k, power[0])
                     for power, coefficient in averaged_error.terms())
same("poisson_gamma", "complete mean-square coupling error",
     averaged_error, k * c_j**2 / j + k * (k + 1) * (c_j - c_gamma)**2)
same("poisson_gamma", "all-three-color coupling constants",
     averaged_error.subs(k, k3),
     sp.Rational(3, 2) * c_j**2 / j
     + sp.Rational(15, 4) * (c_j - c_gamma)**2)
physical_c = 100 * sp.sqrt(2) * sp.pi
angle = sp.pi / (4 * j**2 + 2)
linear_cj = 400 * sp.sqrt(2) * j**2 * angle
same("physical_scale", "retained linear sine comparison deficit",
     physical_c - linear_cj, physical_c / (2 * j**2 + 1))
same("physical_scale", "physical Gamma scale from original lambda",
     j * (2 * sp.sqrt(8) * sp.sin(angle) / (1 / (100 * j))),
     400 * sp.sqrt(2) * j**2 * sp.sin(angle))

sources = [Path(__file__).name, "sources/radial_phase_square_continuation.md"]
report = {
    "status": "passed",
    "exact_assertions": len(checks),
    "groups": dict(groups),
    "scope": (
        "Finite exact divergence-form conjugation and commutator identities, "
        "radial Laguerre polynomial identities, Gamma integrals, scalar heat "
        "coefficient equations, carrier Taylor coefficients, complex insertion "
        "signs, and Poisson-Gamma coupling algebra."
    ),
    "not_established_by_script": [
        "nonlinear fixed-box or regulator-uniform operator convergence",
        "weighted actual-vacuum tail estimates",
        "a spatial local interacting continuum",
        "a Yang-Mills mass-gap conclusion",
    ],
    "source_sha256": {
        name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
        for name in sources
    },
    "passed_assertions": checks,
}
(ROOT / "PHASE_SQUARE_CONTINUATION_CHECKS.json").write_text(
    json.dumps(report, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps({key: report[key] for key in
                  ("status", "exact_assertions", "groups", "source_sha256")},
                 indent=2))
