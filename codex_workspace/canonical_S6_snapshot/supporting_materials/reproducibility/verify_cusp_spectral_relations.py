#!/usr/bin/env python3
"""Exact verifier for the cusp-period spectral identities.

Every check is an explicit symbolic equality.  No Python ``assert`` is used,
so ``python -O`` does not disable the verification.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp


def zero_matrix(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in matrix)


def main() -> int:
    a, u, c, v, d, w, r, s, h, x, y = sp.symbols(
        "a u c v d w r s h x y", real=True
    )
    D = 6 * u**2 - w * v
    P = sp.Matrix(
        [
            [6 * a, c, 1, 0],
            [6 * u, v, 0, 0],
            [d, a, 0, 1],
            [w, u, 0, 0],
        ]
    )
    proposed_inverse_transpose = sp.Matrix(
        [
            [0, 0, 1, 0],
            [u / D, -w / D, (-6 * a * u + c * w) / D, (a * w - d * u) / D],
            [0, 0, 0, 1],
            [-v / D, 6 * u / D, (6 * a * v - 6 * c * u) / D, (-6 * a * u + d * v) / D],
        ]
    )

    k_restricted = sp.Matrix([r, s, 0, 0])
    q_restricted = proposed_inverse_transpose * k_restricted
    q_expected = sp.Matrix([0, (u * r - w * s) / D, 0, (-v * r + 6 * u * s) / D])
    q1 = proposed_inverse_transpose * sp.Matrix([1, 0, 0, 0])
    q2 = proposed_inverse_transpose * sp.Matrix([0, 1, 0, 0])

    koide_substitution = {v: h + y, u: x / sp.sqrt(6), w: h - y}
    koide_form = h**2 - x**2 - y**2

    checks: list[dict[str, object]] = []

    def record(name: str, passed: bool, expression: object, expected: object) -> None:
        checks.append(
            {
                "name": name,
                "passed": bool(passed),
                "expression": str(expression),
                "expected": str(expected),
            }
        )

    det_p = sp.factor(P.det())
    record("period_matrix_determinant", sp.simplify(det_p + D) == 0, det_p, -D)

    inverse_residual = sp.simplify(P.T * proposed_inverse_transpose - sp.eye(4))
    record(
        "full_inverse_transpose",
        zero_matrix(inverse_residual),
        inverse_residual.tolist(),
        sp.zeros(4).tolist(),
    )

    restricted_residual = sp.simplify(q_restricted - q_expected)
    record(
        "restricted_dual_lattice_map",
        zero_matrix(restricted_residual),
        restricted_residual.tolist(),
        sp.zeros(4, 1).tolist(),
    )

    q1_norm = sp.factor((q1.T * q1)[0])
    q2_norm = sp.factor((q2.T * q2)[0])
    q12_inner = sp.factor((q1.T * q2)[0])
    record(
        "first_coordinate_dual_norm",
        sp.simplify(q1_norm - (u**2 + v**2) / D**2) == 0,
        q1_norm,
        (u**2 + v**2) / D**2,
    )
    record(
        "second_coordinate_dual_norm",
        sp.simplify(q2_norm - (w**2 + 36 * u**2) / D**2) == 0,
        q2_norm,
        (w**2 + 36 * u**2) / D**2,
    )
    record(
        "coordinate_dual_inner_product",
        sp.simplify(q12_inner + u * (w + 6 * v) / D**2) == 0,
        q12_inner,
        -u * (w + 6 * v) / D**2,
    )

    wedge_coefficient = sp.factor(q1[1] * q2[3] - q1[3] * q2[1])
    record(
        "theta1_wedge_theta2",
        sp.simplify(wedge_coefficient - 1 / D) == 0,
        wedge_coefficient,
        1 / D,
    )

    koide_determinant = sp.simplify(det_p.subs(koide_substitution))
    record(
        "koide_ambient_discriminant",
        sp.simplify(koide_determinant - koide_form) == 0,
        koide_determinant,
        koide_form,
    )

    N = sp.symbols("N", integer=True, positive=True)
    finite_factor = 4 * N**2 * sp.sin(sp.pi / N) ** 2
    finite_first = sp.simplify(finite_factor * q1_norm)
    finite_second = sp.simplify(finite_factor * q2_norm)
    record(
        "finite_first_coordinate_eigenvalue",
        sp.simplify(finite_first - finite_factor * (u**2 + v**2) / D**2) == 0,
        finite_first,
        finite_factor * (u**2 + v**2) / D**2,
    )
    record(
        "finite_second_coordinate_eigenvalue",
        sp.simplify(finite_second - finite_factor * (w**2 + 36 * u**2) / D**2) == 0,
        finite_second,
        finite_factor * (w**2 + 36 * u**2) / D**2,
    )

    eps, H, B, M = sp.symbols("eps H B M", real=True)
    cusp_values = {
        v: 1 / eps + H,
        u: M,
        w: -1 / eps + B - H,
    }
    cusp_D = sp.expand(D.subs(cusp_values))
    expected_cusp_D = 1 / eps**2 + (2 * H - B) / eps + 6 * M**2 + H * (H - B)
    record(
        "radial_cusp_volume_expansion",
        sp.simplify(cusp_D - expected_cusp_D) == 0,
        cusp_D,
        expected_cusp_D,
    )
    q1_scaled = sp.simplify(q1_norm.subs(cusp_values) / eps**2)
    q2_scaled = sp.simplify(q2_norm.subs(cusp_values) / eps**2)
    q1_first_correction = sp.simplify(sp.limit((q1_scaled - 1) / eps, eps, 0))
    q2_first_correction = sp.simplify(sp.limit((q2_scaled - 1) / eps, eps, 0))
    record(
        "first_dual_mode_first_correction",
        sp.simplify(q1_first_correction - 2 * (B - H)) == 0,
        q1_first_correction,
        2 * (B - H),
    )
    record(
        "second_dual_mode_first_correction",
        sp.simplify(q2_first_correction + 2 * H) == 0,
        q2_first_correction,
        -2 * H,
    )

    failed = [entry["name"] for entry in checks if not entry["passed"]]
    result = {
        "schema": "s6-cusp-spectral-exact-checks-v1",
        "method": "SymPy exact symbolic identities; checks remain active under python -O",
        "formula_scope": [
            "real period matrix and full inverse transpose",
            "dual coordinate covectors and their Euclidean pairings",
            "integral coframe wedge coefficient",
            "ambient Koide/discriminant change of variables",
            "finite forward-difference coordinate eigenvalues",
            "positive radial cusp volume and first spectral corrections",
        ],
        "check_count": len(checks),
        "passed_count": len(checks) - len(failed),
        "failed_count": len(failed),
        "failed_checks": failed,
        "checks": checks,
    }
    output_path = Path(__file__).with_name("cusp_spectral_relations_results.json")
    output_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("check_count", "passed_count", "failed_count", "failed_checks")}, indent=2))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
