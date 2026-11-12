"""Exact finite diagnostics for weak_coupling_electric_graph_limit.md.

No simulation, eigenvalue truncation, file writes or continuum certification.
Requires SymPy. Original raw masses and all physical prefactors are retained.
"""
import json
import sympy as s


def run():
    checks = 0
    fixtures = [
        (s.diag(1, 4), s.Matrix([[2, 1], [1, 3]])),
        (s.diag(1, 4, 9), s.Matrix([[1, -2, 3], [-2, 0, 1], [3, 1, -1]])),
        (s.diag(4, 9, 16), s.Matrix([[1, 2, 0], [2, 4, 0], [0, 0, 0]])),
    ]
    for Sigma, A in fixtures:
        n = Sigma.rows
        root_sigma = s.diag(*[s.sqrt(Sigma[i, i]) for i in range(n)])
        J = root_sigma * A * root_sigma
        covariance = 2 * Sigma.inv()
        Q = Sigma * A * Sigma
        # Three independent colors: quadratic-form variance is 3*2*tr((Q Cov)^2).
        direct_raw_norm = s.Rational(6, 256) * s.trace((Q * covariance)**2)
        formula_raw_norm = s.Rational(3, 32) * s.trace(J**2)
        assert direct_raw_norm == formula_raw_norm
        checks += 1
        direct_energy_times_a = s.Rational(6, 64) * s.trace(Q**2 * covariance)
        formula_energy_times_a = s.Rational(3, 16) * s.trace(Sigma * J**2)
        assert direct_energy_times_a == formula_energy_times_a
        checks += 1
        weights = [(s.Rational(3, 32)*J[i, i]**2, 2*Sigma[i, i])
                   for i in range(n)]
        weights += [(s.Rational(3, 16)*J[i, j]**2, Sigma[i, i]+Sigma[j, j])
                    for i in range(n) for j in range(i+1, n)]
        assert sum(weight for weight, energy in weights) == formula_raw_norm
        assert sum(weight*energy for weight, energy in weights) == formula_energy_times_a
        assert all(weight >= 0 for weight, energy in weights)
        checks += 3

    for L in range(2, 13):
        raw_sum = (2*L)*(2*L+1)*sum(k*k for k in range(-L, L+1))
        formula = s.Rational(2, 3)*L**2*(L+1)*(2*L+1)**2
        r = 4*L**2*(4*L+3)
        lower = formula**2 / (2*r*(2*L+1)**2)
        expected = s.Rational(L**2*(L+1)**2*(2*L+1)**2, 18*(4*L+3))
        assert raw_sum == formula
        assert lower == expected
        assert lower >= s.Rational(L**5, 27)
        checks += 3

    tau, g, a = s.symbols("tau g a", positive=True)
    kappa, b = 2*g**2/a, 1/(2*g**2*a)
    for k in range(1, 9):
        assert s.cancel(4*kappa*k*k/b/g**4) == 16*k*k
        checks += 1
    B2 = tau**2 + 16
    B3 = s.expand(tau*B2 + 16*4*tau)
    assert B3 == tau**3 + 80*tau
    checks += 1
    return {"status": "PASS", "exact_checks": checks,
            "scope": "Original potential-moment constants, signed Gaussian raw norm/energy mode-pair identities, native weight sum and explicit trace lower bound",
            "not_a_certificate_of": ["analytic graph convergence", "uniform joint limit", "interacting continuum"]}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
