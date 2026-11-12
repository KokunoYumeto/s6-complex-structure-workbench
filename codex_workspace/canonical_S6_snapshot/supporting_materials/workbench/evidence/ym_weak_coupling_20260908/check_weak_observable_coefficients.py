"""Exact finite diagnostics for the full radial-observable coefficient proof.

The analytic convergence proofs are in weak_coupling_state_observable_limit.md.
These tests do not certify actual nonlinear eigenvectors or continuum existence.
Requires SymPy; no heavy computation and no filesystem writes.
"""
import json
import sympy as s


def run():
    q = s.symbols("q", real=True)
    k = s.Rational(3, 2)
    polynomials = [s.assoc_laguerre(n, k - 1, q).expand() for n in range(7)]

    def gamma_moment(polynomial):
        return s.expand(sum(
            coefficient * s.rf(k, power[0])
            for power, coefficient in s.Poly(s.expand(polynomial), q).terms()
        ))

    count = 0
    for n, polynomial in enumerate(polynomials):
        assert s.expand(q * s.diff(polynomial, q, 2)
                        + (k - q) * s.diff(polynomial, q) + n * polynomial) == 0
        count += 1
        for m, other in enumerate(polynomials):
            expected = s.rf(k, n) / s.factorial(n) if n == m else 0
            assert gamma_moment(polynomial * other) == expected
            count += 1
        # Divide out the common (1-i)^(-k) factor in the Gamma integral.
        actual = sum(coefficient * s.rf(k, power[0]) / (1 - s.I) ** power[0]
                     for power, coefficient in s.Poly(polynomial, q).terms())
        expected = s.rf(k, n) / s.factorial(n) * (-s.I) ** n / (1 - s.I) ** n
        assert s.simplify(s.expand_complex(actual - expected)) == 0
        count += 1

    z = s.symbols("z")
    generating_function = (2 - z) ** (-k)
    for n in range(7):
        actual = s.diff(generating_function, z, n).subs(z, 0) / s.factorial(n)
        expected = s.rf(k, n) / s.factorial(n) / 2 ** (n + k)
        assert s.simplify(actual - expected) == 0
        count += 1
    assert s.simplify(s.Rational(3, 2) / 2 ** s.Rational(5, 2)
                      - 3 / (8 * s.sqrt(2))) == 0
    count += 1
    return {
        "status": "PASS", "exact_checks": count,
        "scope": ["Laguerre radial differential equation for n=0..6",
                  "Gamma orthogonality for n,m=0..6",
                  "complex overlap at beta=1 for n=0..6",
                  "spectral generating coefficients for n=0..6",
                  "first raw positive mass 3/(8 sqrt(2))"],
        "not_certified_by_finite_tests": ["analytic convergence of actual states",
                                          "interacting continuum existence"]}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
