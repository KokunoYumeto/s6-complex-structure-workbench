"""Exact finite diagnostics for the actual-vacuum relative continuation.

Run with Python and SymPy. The accompanying standalone manuscript
establishes the arbitrary-volume operator statements. This executable
checks combinatorial counts, finite spin moments, algebraic constants and
rank-two spectral comparisons. It does not prove a continuum, spectral
tightness, low-energy weight or a Yang--Mills mass-gap counterexample.
"""

from collections import Counter, defaultdict
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from pathlib import Path
import json

import sympy as s


ROOT = Path(__file__).resolve().parent
REPORT = ROOT / "RELATIVE_CONTINUATION_CHECKS.json"
PASSED = []
GROUPS = Counter()


def check(group, label, condition):
    if not bool(condition):
        raise AssertionError(f"{group}: {label}")
    PASSED.append(f"{group}: {label}")
    GROUPS[group] += 1


def same(group, label, left, right):
    # Rational cancellation avoids generic trigonometric simplification.
    check(group, label, s.cancel(left - right) == 0)


def vertex_step(n, axis):
    out = list(n)
    out[axis] += 1
    return tuple(out)


def box_data(L):
    vertices = tuple(product(range(-L, L + 1), repeat=3))
    edges = {(n, axis) for n in vertices for axis in range(3) if n[axis] < L}
    faces = {}
    incident = defaultdict(set)
    for n in vertices:
        for i in range(3):
            for j in range(i + 1, 3):
                if n[i] == L or n[j] == L:
                    continue
                name = (n, i, j)
                # Ordered physical edges of the oriented face; the last
                # two are traversed in reverse in its Wilson word.
                links = (
                    (n, i),
                    (vertex_step(n, i), j),
                    (vertex_step(n, j), i),
                    (n, j),
                )
                faces[name] = links
                for edge in links:
                    incident[edge].add(name)
    return edges, faces, incident


def check_lattice():
    group = "finite_lattice"
    for L in range(2, 7):
        edges, faces, incident = box_data(L)
        r = {edge: len(incident[edge]) for edge in edges}
        N = 6 * L * (2 * L + 1) ** 2
        M = 12 * L**2 * (2 * L + 1)
        tag = f"L={L}"
        check(group, f"{tag} complete edge count", len(edges) == N)
        check(group, f"{tag} complete face count", len(faces) == M)
        check(group, f"{tag} incidence first moment", sum(r.values()) == 4 * M)
        check(
            group, f"{tag} incidence second moment",
            sum(value**2 for value in r.values()) == 384 * L**3 + 48 * L**2 - 24 * L,
        )
        check(group, f"{tag} incidence range including boundary", min(r.values()) == 2 and max(r.values()) == 4)
        check(group, f"{tag} R2 at most 16M", sum(value**2 for value in r.values()) <= 16 * M)
        check(group, f"{tag} exact N/M", F(N, M) == 1 + F(1, 2 * L))
        check(group, f"{tag} N/M upper bound", F(N, M) <= F(5, 4))
        weighted = sum(n[1] ** 2 for n, axis in edges if axis == 0)
        check(
            group, f"{tag} original Gamma coordinate weights",
            weighted == F(2, 3) * L**2 * (L + 1) * (2 * L + 1) ** 2,
        )
        check(group, f"{tag} Gamma weight divided by M", F(weighted, M) == F((L + 1) * (2 * L + 1), 18))
        transport = sum(r[n, axis] * abs(n[1]) for n, axis in edges if axis == 0)
        check(group, f"{tag} signed-angle transport incidence sum", transport == 4 * L**3 * (4 * L + 3))
        corner = faces[((-L, -L, -L), 0, 1)]
        check(group, f"{tag} corner ordered incidences", tuple(r[edge] for edge in corner) == (2, 3, 3, 2))
        check(group, f"{tag} corner Rp=10", sum(r[edge] for edge in corner) == 10)
        check(
            group, f"{tag} opposite parallel edge is unique in full incidence set",
            all(
                len([other for other in links if other != edge and other[1] == edge[1]]) == 1
                and all(
                    set(incident[edge]) & set(incident[other]) == {face}
                    for other in links if other != edge and other[1] == edge[1]
                )
                for face, links in faces.items() for edge in links
            ),
        )


def weights(d):
    return tuple(F(2 * k - d, 2) for k in range(d + 1))


def check_spin_moments():
    group = "exact_spin_moments"
    for d in range(25):
        values = weights(d)
        lam = F(d * (d + 2), 4)
        moments = {power: sum(value**power for value in values) / len(values) for power in (1, 2, 3, 4)}
        check(group, f"q={F(d,2)} first moment", moments[1] == 0)
        check(group, f"q={F(d,2)} second moment", moments[2] == lam / 3)
        check(group, f"q={F(d,2)} third moment", moments[3] == 0)
        check(group, f"q={F(d,2)} fourth moment", moments[4] == lam * (3 * lam - 1) / 15)

    # Each tuple is (twice-spin values, original signed n2 coordinates).
    blocks = (
        ((0,), (0,)), ((1,), (-3,)), ((2,), (2,)), ((3,), (-1,)),
        ((1, 1), (-2, 3)), ((2, 3), (0, -3)), ((4, 1), (2, 1)),
        ((1, 2, 3), (-2, 0, 3)), ((2, 2, 2), (-3, 1, 2)),
        ((0, 3, 4), (5, -1, 2)), ((3, 4, 1), (-1, -2, -3)),
        ((1, 1, 1, 1), (-3, -1, 1, 3)),
    )
    for index, (ds, coordinates) in enumerate(blocks):
        samples = tuple(product(*(weights(d) for d in ds)))
        ys = tuple(2 * sum(n * m for n, m in zip(coordinates, sample)) for sample in samples)
        m2 = sum(value**2 for value in ys) / len(ys)
        m4 = sum(value**4 for value in ys) / len(ys)
        lambdas = tuple(F(d * (d + 2), 4) for d in ds)
        gamma = sum(n**2 * lam for n, lam in zip(coordinates, lambdas))
        deficit = sum(F(32, 15) * n**4 * lam**2 + F(16, 15) * n**4 * lam for n, lam in zip(coordinates, lambdas))
        check(group, f"joint block {index} second moment", m2 == F(4, 3) * gamma)
        check(group, f"joint block {index} complete fourth moment", m4 == F(16, 3) * gamma**2 - deficit)
        check(group, f"joint block {index} nonnegative fourth-moment deficit", deficit >= 0)
        check(group, f"joint block {index} all-block fourth-moment coefficient", m4 / 24 <= F(2, 9) * gamma**2)

    group = "symbolic_moment_identities"
    d, k = s.symbols("d k", integer=True, nonnegative=True)
    lam = d * (d + 2) / 4
    for power, expected in ((2, lam / 3), (4, lam * (3 * lam - 1) / 15)):
        actual = s.summation((k - d / 2) ** power, (k, 0, d)) / (d + 1)
        same(group, f"unrestricted twice-spin polynomial moment {power}", actual, expected)
    a, b, wa, wb = s.symbols("a b wa wb")
    fourth = 16 * (wa**2 * a * (3 * a - 1) / 15 + wb**2 * b * (3 * b - 1) / 15 + 6 * wa * wb * a * b / 9)
    bound_minus_deficit = s.Rational(16, 3) * (wa * a + wb * b) ** 2 - s.Rational(32, 15) * (wa**2 * a**2 + wb**2 * b**2) - s.Rational(16, 15) * (wa**2 * a + wb**2 * b)
    same(group, "complete two-edge fourth-moment polynomial", fourth, bound_minus_deficit)
    check(group, "Taylor fourth moment coefficient", F(16, 3) / 24 == F(2, 9))
    check(group, "relative remainder coefficient", F(2, 9) / F(2, 3) == F(1, 3))


def check_electric_constants():
    group = "electric_moment_constants"
    check(group, "sqrt(3) rational majorant", F(3) <= F(7, 4) ** 2)
    check(group, "(5/4)^(1/4) rational majorant", F(5, 4) <= F(17, 16) ** 4)
    check(group, "Ar rational majorant", 8 * F(7, 4) * F(17, 16) == F(119, 8))
    ratio = F(119, 8) + (6 + F(119, 8)) / 240
    check(group, "minimum full box M2", 12 * 2**2 * 5 == 240)
    check(group, "improved B2 coefficient before rounding", ratio == F(28727, 1920))
    check(group, "improved B2 coefficient at most 15", ratio < 15)
    check(group, "strict improvement margin", 15 - ratio == F(73, 1920))
    check(group, "earlier 35 coefficient radical comparison", 16 * 10 < 13**2)
    check(group, "corrected raw norm coefficient 384", F(4, 3) * 4 * 2 * 36 == 384)
    check(group, "corrected raw norm power minus ten", -20 + 4 + 6 == -10)
    L = s.symbols("L", integer=True, positive=True)
    N = 6 * L * (2 * L + 1) ** 2
    M = 12 * L**2 * (2 * L + 1)
    same(group, "exact symbolic finite-box ratio", N / M, 1 + 1 / (2 * L))
    same(group, "variance lower-bound denominator coefficient", s.Rational(3, 4) * (L + 1) * (2 * L + 1) / 18, (L + 1) * (2 * L + 1) / 24)


def check_corrected_cusp():
    group = "corrected_cusp_constants"
    j, x, q, C = s.symbols("j x q C", positive=True)
    # x=xi^(1/4), q=exp(8*pi*xi). Keeping q formal makes every
    # cancellation below an exact rational identity; q^4=1/alpha.
    xi = x**4
    L = j**2
    a = 1 / (100 * j)
    M = 12 * j**4 * (2 * j**2 + 1)
    T = 2 * C + j**4 * q
    Dlower = (T - C) ** 2
    sigma_lower = xi * q**-4 * (L + 1) * (2 * L + 1) / (24 * (6 + 64 * xi))
    B2 = 15 * x**7 * M**2
    # theta/pi=2 a^2 / D. This expression bounds eta/pi^2.
    theta_over_pi = 2 * a**2 / Dlower
    eta_over_pi2 = theta_over_pi**2 * L**4 * B2 / (3 * sigma_lower)
    sharp_count = s.Rational(69120, 10**8) * x**3 * (6 + 64 * xi) * j**-4 * (2 * j**2 + 1) / (j**2 + 1)
    retained_C_factor = (j**4 * q / (C + j**4 * q)) ** 4
    same(group, "exact-count corrected cusp relative coefficient", eta_over_pi2, sharp_count * retained_C_factor)
    check(group, "C-dependent denominator excess has nonnegative coefficients", all(coef >= 0 for coef in s.Poly((C + j**4 * q) ** 4 - (j**4 * q) ** 4, C, j, q).coeffs()))
    same(group, "finite-count ratio is below two", 2 - (2 * j**2 + 1) / (j**2 + 1), 1 / (j**2 + 1))
    check(group, "uniform sharpened coefficient", 2 * 69120 == 138240)

    # Independent conservative route preserves the previous displayed
    # coefficient: D >= T^2/4 >= j^8 q^2/4, M <= 36j^6,
    # (L+1)(2L+1) >= 2j^4.
    conservative_D = j**8 * q**2 / 4
    conservative_sigma = xi * q**-4 * 2 * j**4 / (24 * (6 + 64 * xi))
    conservative = (2 * a**2 / conservative_D) ** 2 * j**8 * 15 * x**7 * (36 * j**6) ** 2 / (3 * conservative_sigma)
    expected = s.Rational(4976640, 10**8) * x**3 * (6 + 64 * xi) * j**-4
    same(group, "independent conservative coefficient 4976640", conservative, expected)
    check(group, "conservative versus uniform sharpened coefficient", F(4976640, 138240) == 36)
    same(group, "M majorant factorization", 36 * j**6 - M, 12 * j**4 * (j - 1) * (j + 1))
    same(group, "Gamma denominator majorant factorization", (j**2 + 1) * (2 * j**2 + 1) - 2 * j**4, 3 * j**2 + 1)
    same(group, "cover systole scale inequality polynomial", j**4 - j, j * (j - 1) * (j**2 + j + 1))
    same(group, "retained base-change logarithmic exponent", j * (-2 * T / j), -2 * T)
    same(group, "pullback volume retains cover degree", j**2 * Dlower, j**2 * (C + j**4 * q) ** 2)

    group = "explicit_coupling_paths"
    # j=t^2 and kappa*=h^2 keep the stated fractional powers exact.
    t, h = s.symbols("t h", positive=True)
    fixed_x = 10 * t / h
    actual = fixed_x**3 * (6 + 64 * fixed_x**4) * t**-8
    target = 6000 * h**-3 * t**-5 + 640000000 * h**-7 * t**-1
    same(group, "fixed-kappa two exact path coefficients", actual, target)
    gj2 = h**2 / (200 * t**2)
    aj = 1 / (100 * t**2)
    same(group, "fixed-kappa physical electric coefficient", 2 * gj2 / aj, h**2)
    same(group, "fixed-kappa xi with all factors", 1 / (4 * gj2**2), 10000 * t**4 / h**4)
    same(group, "fixed-kappa physical magnetic coefficient", 1 / (2 * gj2 * aj), 10000 * t**4 / h**2)
    z = s.symbols("z", positive=True)  # z=sqrt(log j)
    log_x = z / s.sqrt(2)
    log_polynomial = log_x**3 * (6 + 64 * log_x**4)
    same(group, "logarithmic trajectory exact polynomial", log_polynomial, z**3 * (6 + 16 * z**4) / (2 * s.sqrt(2)))
    same(group, "logarithmic xi", 1 / (4 * (1 / z**2) ** 2), z**4 / 4)
    # exp(4z^2) >= (4z^2)^4/4! proves the stated vanishing bound;
    # this checks its exact coefficients, not a finite approximation.
    log_majorant = log_polynomial * s.factorial(4) / (4 * z**2) ** 4
    same(group, "logarithmic factorial majorant coefficients", log_majorant, 9 / (32 * s.sqrt(2) * z**5) + 3 / (4 * s.sqrt(2) * z))


def check_rank_two():
    group = "rank_two_spectral_comparison"
    t, r = s.symbols("t r", real=True)
    c = (1 - t**2) / (1 + t**2)
    v = 2 * t / (1 + t**2)
    uvec = s.Matrix([1, 0])
    wvec = s.Matrix([c, v])
    D = uvec * uvec.T - wvec * wvec.T
    same(group, "unit direction rational parameter", c**2 + v**2, 1)
    same(group, "difference of rank-one projectors has zero trace", s.trace(D), 0)
    same(group, "rank-two determinant", D.det(), -v**2)
    for i in range(2):
        for k in range(2):
            same(group, f"rank-two squared matrix entry {i},{k}", (D * D)[i, k], v**2 if i == k else 0)
    same(group, "exact relative vector error controls angular error", (r - c) ** 2 + v**2 - v**2, (r - c) ** 2)
    same(group, "relative error decomposition from original vectors", ((r * uvec - wvec).T * (r * uvec - wvec))[0] - v**2, (r - c) ** 2)
    for tv in (F(1, 3), F(1, 2), F(1), F(2)):
        cv = (1 - tv**2) / (1 + tv**2)
        sv = 2 * tv / (1 + tv**2)
        Dv = s.Matrix([[1 - cv**2, -cv * sv], [-cv * sv, -sv**2]])
        for pv in (F(-3), F(-1), F(0), F(1, 2), F(1), F(2)):
            av = (1 - pv**2) / (1 + pv**2)
            bv = 2 * pv / (1 + pv**2)
            direction = s.Matrix([av, bv])
            P = direction * direction.T
            check(group, f"exact projection discrepancy t={tv},p={pv}", abs(s.trace(Dv * P)) <= abs(sv))
    complex_w = s.Matrix([s.Rational(3, 5), 4 * s.I / 5])
    complex_D = uvec * uvec.T - complex_w * complex_w.conjugate().T
    check(group, "complex rank-two self-adjoint difference", complex_D == complex_D.conjugate().T)
    check(group, "complex rank-two angular square", complex_D**2 == s.Rational(16, 25) * s.eye(2))


def report(status, error=None):
    source_paths = (
        Path(__file__),
        ROOT / "spatial_continuum.md",
    )
    value = {
        "status": status,
        "exact_assertions": len(PASSED),
        "groups": dict(GROUPS),
        "scope": "Exact finite lattice enumeration, complete finite spin-weight moments, symbolic coefficient identities and rank-two spectral diagnostics. General operator and limit arguments are proved in the standalone manuscript.",
        "not_established_by_this_script": [
            "arbitrary-volume operator inequalities from finite sampling",
            "existence of an interacting continuum",
            "low-energy spectral tightness or nonzero limiting spectral weight",
            "a Yang--Mills mass-gap counterexample",
        ],
        "audited_relative_coefficients_without_pi_squared": {
            "exact_count": "69120/10^8 times (2j^2+1)/(j^2+1)",
            "uniform_sharpened": "138240/10^8",
            "previous_conservative": "4976640/10^8",
            "common_factor": "xi^(3/4)(6+64xi)j^(-4)",
        },
        "utc": datetime.now(timezone.utc).isoformat(),
        "source_sha256": {
            str(path.relative_to(ROOT)): sha256(path.read_bytes()).hexdigest()
            for path in source_paths
        },
        "passed_assertions": PASSED,
    }
    if error is not None:
        value["error"] = str(error)
    REPORT.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    return value


def main():
    try:
        check_lattice()
        check_spin_moments()
        check_electric_constants()
        check_corrected_cusp()
        check_rank_two()
    except Exception as error:
        report("failed", error)
        raise
    result = report("passed")
    print(json.dumps({key: result[key] for key in ("status", "exact_assertions", "groups", "scope")}, indent=2))


if __name__ == "__main__":
    main()
