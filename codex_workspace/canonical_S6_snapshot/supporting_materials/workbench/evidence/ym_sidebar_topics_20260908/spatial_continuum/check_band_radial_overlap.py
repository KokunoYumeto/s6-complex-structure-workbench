"""Exact finite algebra checks for the band/radial correspondence.

These diagnostics do not establish the analytic weak-coupling limits,
diagonal existence, projection convergence, or continuum reconstruction.
Those statements require the retained full proof. SymPy exact algebra
only: no floating-point tests and no Lean invocation.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
checks: list[dict[str, object]] = []


def check(name: str, expression) -> None:
    if isinstance(expression, sp.MatrixBase):
        entries = list(expression)
    elif isinstance(expression, (list, tuple)):
        entries = list(expression)
    else:
        entries = [expression]
    residuals = [sp.simplify(entry) for entry in entries]
    passed = all(entry == 0 for entry in residuals)
    checks.append(
        {
            "name": name,
            "passed": passed,
            "scalar_residual_count": len(residuals),
            "nonzero_residuals": [str(x) for x in residuals if x != 0],
        }
    )
    if not passed:
        raise AssertionError(f"{name}: {residuals}")


def creation_polynomial_norm(poly, variables) -> sp.Expr:
    """Bosonic vacuum norm: monomials are orthogonal with norm alpha!."""
    result = sp.S.Zero
    for powers, coefficient in sp.Poly(sp.expand(poly), *variables).terms():
        result += sp.conjugate(coefficient) * coefficient * sp.prod(
            sp.factorial(power) for power in powers
        )
    return sp.expand(result)


def creation_polynomial_inner(left, right, variables) -> sp.Expr:
    left_terms = dict(sp.Poly(sp.expand(left), *variables).terms())
    right_terms = dict(sp.Poly(sp.expand(right), *variables).terms())
    return sp.expand(
        sum(
            sp.conjugate(coefficient)
            * right_terms.get(powers, 0)
            * sp.prod(sp.factorial(power) for power in powers)
            for powers, coefficient in left_terms.items()
        )
    )


def symmetric_matrix(prefix):
    entries = sp.symbols(f"{prefix}11 {prefix}22 {prefix}33 "
                        f"{prefix}12 {prefix}13 {prefix}23", real=True)
    x11, x22, x33, x12, x13, x23 = entries
    return sp.Matrix([[x11, x12, x13],
                      [x12, x22, x23],
                      [x13, x23, x33]])


def unpack(vector):
    return vector[0], sp.Matrix(
        [[vector[1], vector[4], vector[5]],
         [vector[4], vector[2], vector[6]],
         [vector[5], vector[6], vector[3]]]
    )


def pack(scalar, matrix):
    return sp.Matrix([scalar, matrix[0, 0], matrix[1, 1], matrix[2, 2],
                      matrix[0, 1], matrix[0, 2], matrix[1, 2]])


def operator_matrix(action):
    identity = sp.eye(7)
    columns = []
    for index in range(7):
        scalar, matrix = unpack(identity[:, index])
        out_scalar, out_matrix = action(scalar, matrix)
        columns.append(pack(out_scalar, out_matrix))
    return sp.Matrix.hstack(*columns)


def radial_compression(projector, scale):
    return operator_matrix(
        lambda scalar, matrix: (
            3 * scale * sp.trace(projector * matrix),
            scale * scalar * projector / 2
            + scale * (projector * matrix + matrix * projector),
        )
    )


def main() -> None:
    c, H, lam, a = sp.symbols("c H lambda a", real=True)
    c_gamma = 100 * sp.sqrt(2) * sp.pi
    k = sp.Rational(3, 2)
    zero3 = sp.zeros(3)
    identity3 = sp.eye(3)
    basis_projectors = [
        identity3[:, r] * identity3[:, r].T for r in range(3)
    ]

    # Exact bosonic two-creation and four-creation norms.
    creators = sp.symbols("x10 x11 x12 x20 x21 x22 x30 x31 x32",
                         real=True)
    x = sp.Matrix(3, 3, creators)
    B = symmetric_matrix("B")
    E = symmetric_matrix("E")

    def phi(matrix):
        return sum(
            matrix[i, j] * x[i, color] * x[j, color]
            for i in range(3) for j in range(3) for color in range(3)
        )

    check("two_creation_general_symmetric_metric",
          creation_polynomial_inner(phi(B), phi(E), creators)
          - 6 * sp.trace(B.T * E))
    check("diagonal_creation_raw_norm_six",
          creation_polynomial_norm(phi(basis_projectors[0]), creators) - 6)
    q_squared_coordinates = sp.symbols("z0 z1 z2", real=True)
    sigma = sp.symbols("sigma", positive=True)
    # a†² Phi0 = (sigma z²/2 - 1) Phi0 in each real coordinate.
    q = sigma * sum(z**2 for z in q_squared_coordinates) / 4
    pair_ratio = sum(sigma * z**2 / 2 - 1
                     for z in q_squared_coordinates)
    check("radial_centering_creation_sign_and_half",
          q - k - pair_ratio / 2)
    same_mode_pair = phi(basis_projectors[0])
    quartic_norm = creation_polynomial_norm(same_mode_pair**2, creators)
    check("four_creation_raw_norm_120", quartic_norm - 120)
    check("four_creation_count_with_all_color_multiplicities",
          3 * sp.factorial(4) + 3 * 4 * sp.factorial(2)**2 - 120)
    check("first_omitted_quartic_raw_norm_30_lambda_squared",
          lam**2 * quartic_norm / 4 - 30 * lam**2)

    # Frobenius metric for raw symmetric coordinates has off-diagonal
    # weight 12, since the ordered entries occur twice.
    gram = sp.diag(1, 6, 6, 6, 12, 12, 12)
    check("raw_symmetric_coordinate_metric",
          (pack(0, B).T * gram * pack(0, E))[0]
          - 6 * sp.trace(B.T * E))

    P = symmetric_matrix("P")
    C_P = radial_compression(P, c)
    check("arbitrary_real_symmetric_radial_compression_adjoint",
          gram * C_P - C_P.T * gram)
    S = symmetric_matrix("R")
    T = symmetric_matrix("Q")
    local_general = operator_matrix(
        lambda scalar, matrix: (
            3 * sp.trace(S * matrix) / (2 * a),
            scalar * S / (4 * a) + (T * matrix + matrix * T) / (2 * a),
        )
    )
    check("arbitrary_full_local_compression_adjoint",
          gram * local_general - local_general.T * gram)

    # Rational orthogonal examples retain a nontrivial exact frame.
    rotation = sp.Matrix([
        [sp.Rational(3, 5), -sp.Rational(4, 5), 0],
        [sp.Rational(4, 5), sp.Rational(3, 5), 0],
        [0, 0, 1],
    ])
    u = sp.Matrix([1, 2, 3])
    householder = identity3 - 2 * u * u.T / (u.T * u)[0]
    frames = {
        "identity": identity3,
        "rational_rotation": rotation,
        "householder": householder,
        "composed_frame": rotation * householder,
    }
    for name, frame in frames.items():
        check(f"{name}_orthogonal", frame.T * frame - identity3)
        projectors = [frame[:, r] * frame[:, r].T for r in range(3)]
        residuals = []
        for r, projector in enumerate(projectors):
            residuals.extend(projector * projector - projector)
            residuals.append(sp.trace(projector) - 1)
            for s, other in enumerate(projectors):
                residuals.append(sp.trace(projector * other) - int(r == s))
        check(f"{name}_rank_one_projectors_and_trace_orthogonality",
              residuals)
        check(f"{name}_projector_resolution_identity",
              sum(projectors, zero3) - identity3)
        check(f"{name}_creation_map_frame_covariance",
              frame.T * sum(projectors, zero3) * frame - identity3)

    # A symbolic (not just sampled) rank-one unit-sphere frame identity.
    n = sp.Matrix(sp.symbols("n1 n2 n3", real=True))
    n2 = (n.T * n)[0]
    rank_one = n * n.T
    check("symbolic_rank_one_square_retains_norm_factor",
          rank_one**2 - n2 * rank_one)
    check("symbolic_rank_one_trace_retains_norm_factor",
          sp.trace(rank_one) - n2)
    check("symbolic_rank_one_overlap_depends_only_on_unit_norm",
          6 * sp.trace((c * rank_one / 2).T
                       * (sp.sqrt(2) * sp.pi * H * identity3))
          - 3 * c * sp.sqrt(2) * sp.pi * H * n2)

    # Raw amplitudes are tested before the angular fraction.
    radial_norm = 6 * sp.trace((c * basis_projectors[0] / 2)**2)
    local_coeff = sp.sqrt(2) * sp.pi * H * identity3
    local_norm = 6 * sp.trace(local_coeff**2)
    raw_overlap = 6 * sp.trace((c * basis_projectors[0] / 2) * local_coeff)
    check("radial_raw_norm_k_c_squared", radial_norm - k * c**2)
    check("local_raw_scaled_norm_36_pi_squared_H_squared",
          local_norm - 36 * sp.pi**2 * H**2)
    check("radial_raw_norm_original_scale_30000_pi_squared",
          radial_norm.subs(c, c_gamma) - 30000 * sp.pi**2)
    check("raw_overlap_original_scale_600_pi_squared_H",
          raw_overlap.subs(c, c_gamma) - 600 * sp.pi**2 * H)
    # Cross-multiplication remains defined when H=0; the ratio 1/3
    # is asserted in the proof only when H is nonzero.
    check("angular_fraction_one_third_cross_multiplied",
          3 * raw_overlap**2 - radial_norm * local_norm)
    check("raw_sum_vector_coefficient_H_over_50",
          H * c_gamma * sum(basis_projectors, zero3) / 100 - local_coeff)
    check("sum_radial_raw_norm_90000_pi_squared",
          6 * sp.trace((c_gamma * identity3 / 2)**2) - 90000 * sp.pi**2)

    summed_radial = sum(
        [radial_compression(projector, c_gamma)
         for projector in basis_projectors], sp.zeros(7)
    )
    local_limit = operator_matrix(
        lambda scalar, matrix: (
            6 * sp.sqrt(2) * sp.pi * H * sp.trace(matrix),
            sp.sqrt(2) * sp.pi * H * (scalar * identity3 + 4 * matrix),
        )
    )
    check("full_compressed_operator_H_over_50_equality",
          H * summed_radial / 50 - local_limit)
    check("full_compressed_local_limit_adjoint",
          gram * local_limit - local_limit.T * gram)

    # Exact quadratic phase difference; the linear current cancels.
    beta, gamma, J, R = sp.symbols("beta gamma J R", real=True)
    energy = sp.symbols("A", real=True)
    phase = lambda s: energy + s * J + s**2 * R
    check("symmetric_phase_difference_retains_R",
          phase(beta) + phase(-beta) - 2 * energy - 2 * beta**2 * R)
    check("mixed_phase_second_difference",
          phase(beta + gamma) - phase(beta) - phase(gamma)
          + energy - 2 * beta * gamma * R)

    source_files = [
        ROOT / "sources" / "local_band_radial_correspondence.md",
        ROOT / "sources" / "radial_phase_square_continuation.md",
        ROOT / "sources" / "local_band_inputs" / "LOCAL_ENERGY_BAND_TRANSFER.md",
        ROOT / "sources" / "local_band_inputs" / "extensive_quantum_blocking.md",
    ]
    sources = []
    for source in source_files:
        exists = source.is_file()
        entry = {"path": source.relative_to(ROOT).as_posix(), "present": exists}
        if exists:
            data = source.read_bytes()
            entry.update({"bytes": len(data),
                          "sha256": hashlib.sha256(data).hexdigest()})
        sources.append(entry)
    payload = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "scope": (
            "Exact SymPy finite algebra diagnostics. These do not certify "
            "analytic convergence, actual vacuum/projection theorems, "
            "diagonal selection, or any continuum claim."
        ),
        "check_count": len(checks),
        "passed_count": sum(bool(item["passed"]) for item in checks),
        "scalar_residual_count": sum(
            int(item["scalar_residual_count"]) for item in checks),
        "all_passed": all(bool(item["passed"]) for item in checks),
        "checks": checks,
        "sources": sources,
    }
    output = ROOT / "BAND_RADIAL_OVERLAP_CHECKS.json"
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "check_count": payload["check_count"],
        "passed_count": payload["passed_count"],
        "scalar_residual_count": payload["scalar_residual_count"],
        "all_passed": payload["all_passed"],
        "output": output.name,
    }))


if __name__ == "__main__":
    main()
