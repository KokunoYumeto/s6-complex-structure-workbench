"""Fresh numerical corroboration of C7.10; no transcendence conclusion.

The exact CM identities are checked separately in cm_witness_exact.py.
This script evaluates the stated original real-lattice branch with python-flint
ball arithmetic. It is not execution of the absent historical PARI program.
"""
from pathlib import Path
import hashlib
import json
import flint
from flint import acb, arb, acb_series, ctx

ctx.dps = 160
beta = acb(0, arb(19).sqrt())
tau = (1 + beta / 19) / 2
g2, g3 = tau.elliptic_invariants()
omega = (g2.real / 152).root(4)
u_scaled = acb(4 * omega**2).elliptic_inv_p(tau)
u = omega * u_scaled
area = omega**2 * tau.imag

def zeta(z):
    return (z / omega).elliptic_zeta(tau) / omega

def sigma(z):
    return omega * (z / omega).elliptic_sigma(tau)

wp_series = acb_series([u_scaled, 1], 2).elliptic_p(tau)
wp_prime = wp_series[1] / omega**3
eta1 = 2 * acb(arb(1) / 2).elliptic_zeta(tau) / omega
c = zeta(u) - eta1 * u / omega
gaussian = (-arb.pi() * u**2 / (2 * area)).exp()
a = zeta(beta * u) + beta * zeta(u) + 4 * beta * u
r2 = sigma((1 + beta) * u) / (sigma(u) * sigma(beta * u))
r2 *= (2 * beta * u**2).exp()
exact_a = -21 * beta / 703
exact_r2 = -acb(165) / 74 + 1839 * beta / 1406
eps = arb("1e-110")
checks = {
    "g2_imaginary_part_contains_zero": g2.imag.contains(0),
    "g3_matches_minus361_with_error_below_1e110": abs(g3 / omega**6 + 361).upper() < eps,
    "u_is_real_within_balls": u.imag.contains(0),
    "u_strictly_positive": u.real.lower() > 0,
    "u_below_half_real_period": u.real.upper() < omega.lower() / 2,
    "wp_prime_matches_minus3_with_error_below_1e110": abs(wp_prime + 3).upper() < eps,
    "zeta_a_error_below_1e110": abs(a - exact_a).upper() < eps,
    "sigma_r2_error_below_1e110": abs(r2 - exact_r2).upper() < eps,
    "c_displayed_digits": (c.real - arb("1.14793408195385447403276278660663356664777041472753")).abs_upper() < arb("1e-49"),
    "Gaussian_displayed_digits": (gaussian.real - arb("0.68133647525194864004469591167703191986051023921164")).abs_upper() < arb("1e-49"),
}
assert all(checks.values()), checks
result = {
    "author": "GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort; same family",
    "phase": "S6_SERIES_GRIND",
    "scope": "Fresh ball evaluation of the explicitly stated real-lattice branch; analytic corroboration of exact CM identities. No transcendence result and no original-program replay.",
    "flint_version": flint.__version__,
    "working_decimal_digits": ctx.dps,
    "parameter": "tau=(1+i/sqrt(19))/2; omega=(Re(g2(tau))/152)^(1/4)>0; u=omega*wp_tau^(-1)(4*omega^2)",
    "checks_passed": sum(checks.values()),
    "checks": checks,
    "values": {k: str(v) for k, v in {
        "tau": tau, "omega": omega, "u": u, "area": area,
        "c": c, "Gaussian": gaussian, "a": a, "r2": r2,
        "a_error": a - exact_a, "r2_error": r2 - exact_r2,
        "wp_prime_error": wp_prime + 3, "g3_error": g3 / omega**6 + 361,
    }.items()},
    "program_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
out = Path(__file__).with_suffix(".output.json")
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"checks_passed": result["checks_passed"], "output": str(out), "program_sha256": result["program_sha256"]}))
