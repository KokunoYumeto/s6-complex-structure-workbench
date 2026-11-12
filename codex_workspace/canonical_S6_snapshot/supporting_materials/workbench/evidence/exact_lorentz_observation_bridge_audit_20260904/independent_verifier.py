#!/usr/bin/env python3
"""Independent exact checks for the 2026-09-04 Lorentz-bridge intake.

This program is independent of the verifier shipped in the ZIP.  It does not
import or execute packet code.  All identities are checked over exact SymPy
expressions; barred variables are algebraically independent stand-ins for
complex conjugates where appropriate.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
OUT = HERE / "independent_verification.json"


def zero_scalar(expr: sp.Expr) -> bool:
    return sp.factor(sp.together(sp.expand(expr))) == 0


def zero_matrix(matrix: sp.Matrix) -> bool:
    return all(zero_scalar(entry) for entry in matrix)


def main() -> None:
    checks: dict[str, dict[str, object]] = {}

    def check(name: str, condition: bool, detail: str) -> None:
        checks[name] = {"passed": bool(condition), "detail": detail}
        if not condition:
            raise AssertionError(f"{name}: {detail}")

    P = sp.Matrix([[1, -1, 0], [0, 1, -1]])
    u = sp.Matrix([1, 1, 1])
    C = P * P.T
    R = P.T * C.inv()
    Pi = u * u.T / 3
    X = R.row_join(u)
    Xinv = P.col_join(u.T / 3)

    check("fixed_C", C == sp.Matrix([[2, -1], [-1, 2]]), "C=P P^*")
    check(
        "fixed_R",
        R
        == sp.Rational(1, 3)
        * sp.Matrix([[2, 1], [-1, 1], [-1, -2]]),
        "R=P^* C^{-1}",
    )
    check("right_inverse", P * R == sp.eye(2), "P R=I_2")
    check("orthogonal_projector", R * P == sp.eye(3) - Pi, "R P=I_3-u u^*/3")
    check("kernel_vector", P * u == sp.zeros(2, 1), "P u=0")
    check("orthogonal_columns", u.T * R == sp.zeros(1, 2), "u^* R=0")
    check("adapted_determinant", X.det() == 1, "det X=1")
    check("adapted_inverse_left", Xinv * X == sp.eye(3), "X^{-1}X=I_3")
    check("adapted_inverse_right", X * Xinv == sp.eye(3), "XX^{-1}=I_3")

    g11, g12, g21, g22 = sp.symbols("g11 g12 g21 g22")
    z1, z2, zb1, zb2, lam = sp.symbols("z1 z2 zb1 zb2 lam")
    G = sp.Matrix([[g11, g12], [g21, g22]])
    z = sp.Matrix([z1, z2])
    zs = sp.Matrix([[zb1, zb2]])
    M = G.row_join(z).col_join(zs.row_join(sp.Matrix([[lam]])))
    H = X * M * X.T
    check("recover_G", zero_matrix(P * H * P.T - G), "P H P^*=G")
    check("recover_z", zero_matrix(P * H * u / 3 - z), "P H u/3=z")
    check("recover_lambda", zero_scalar((u.T * H * u)[0] / 9 - lam), "u^* H u/9=lambda")
    block_det = lam * G.det() - (zs * G.adjugate() * z)[0]
    check("block_determinant", zero_scalar(H.det() - block_det), "det H=lambda detG-z^*adj(G)z")

    J = R * G * R.T
    e2_J = (sp.trace(J) ** 2 - sp.trace(J * J)) / 2
    check("e2_pullback", zero_scalar(e2_J - G.det() / 3), "e_2(j_P(G))=detG/3")
    eps = sp.symbols("eps")
    check(
        "transverse_determinant",
        zero_scalar((u * u.T + eps * J).det() - eps**2 * G.det()),
        "det(uu^*+epsilon j_P(G))=epsilon^2 detG",
    )

    a, b, c, d = sp.symbols("a b c d")
    g = sp.Matrix([[a, b], [c, d]])
    Dg = sp.eye(3)
    Dg[:2, :2] = g
    T = R * g * P + Pi
    check("spin_embedding_formula", zero_matrix(T - X * Dg * Xinv), "T_P(g)=X(g+1)X^{-1}")
    check("spin_embedding_determinant", zero_scalar(T.det() - g.det()), "det T_P(g)=det g")
    check("spin_intertwiner_P", zero_matrix(P * T - g * P), "P T_P(g)=gP")
    check("spin_fixed_u", zero_matrix(T * u - u), "T_P(g)u=u")
    check("spin_intertwiner_R", zero_matrix(T * R - R * g), "T_P(g)R=Rg")
    check(
        "central_spin_sign",
        zero_matrix((-sp.eye(2)) * z + z),
        "-I_2 fixes G under congruence and sends z to -z",
    )

    x11, x12, x21, x22, x31, x32 = sp.symbols("x11 x12 x21 x22 x31 x32")
    y11, y12, y21, y22, y31, y32 = sp.symbols("y11 y12 y21 y22 y31 y32")
    f1, f2, f3, fb1, fb2, fb3 = sp.symbols("f1 f2 f3 fb1 fb2 fb3")
    Z = sp.Matrix([[x11, x12], [x21, x22], [x31, x32]])
    Zs = sp.Matrix([[y11, y21, y31], [y12, y22, y32]])
    phi = sp.Matrix([f1, f2, f3])
    phis = sp.Matrix([[fb1, fb2, fb3]])
    gram2 = Zs * Z
    cb = sp.Integer(0)
    for i, j in ((0, 1), (0, 2), (1, 2)):
        cb += Zs.extract([0, 1], [i, j]).det() * Z.extract([i, j], [0, 1]).det()
    check("cauchy_binet_3x2", zero_scalar(gram2.det() - cb), "det(Z^*Z)=sum of squared minors")
    B = Z.row_join(phi)
    Bs = Zs.col_join(phis)
    gram3 = Bs * B
    G3 = gram3[:2, :2]
    z3 = gram3[:2, 2]
    z3s = gram3[2, :2]
    lam3 = gram3[2, 2]
    check(
        "full_gram_phase",
        zero_scalar(Bs.det() * B.det() - (lam3 * G3.det() - (z3s * G3.adjugate() * z3)[0])),
        "|det B|^2=lambda detG-z^*adj(G)z",
    )

    alpha, omega2, lambda0, w2 = sp.symbols("alpha omega2 lambda0 w2", positive=True)
    mu2 = omega2 / (lambda0 - w2)
    check(
        "constrained_mass_formula",
        zero_scalar(alpha**2 * mu2 - alpha**2 * omega2 / (lambda0 - w2)),
        "det p=alpha^2|omega_0|^2/(lambda_0-||w||^2)",
    )
    check(
        "sharp_endpoint_difference",
        zero_scalar(
            alpha**2 * omega2 / (lambda0 - w2)
            - alpha**2 * omega2 / lambda0
            - alpha**2 * omega2 * w2 / (lambda0 * (lambda0 - w2))
        ),
        "mass minus endpoint is nonnegative for 0<=||w||^2<lambda_0",
    )

    # Differential of p(A,w)=alpha*mu(w)*exp(A) at A=0 and w=(r,0).
    # Hermitian coordinates are ordered (p0,p1,p2,p3).  The three A
    # directions are the Pauli directions; the fourth row is the real radial
    # w direction.  Three sphere-tangent w directions have zero derivative.
    r, mu, dmu = sp.symbols("r mu dmu", positive=True)
    J_interior = sp.diag(alpha * dmu, alpha * mu, alpha * mu, alpha * mu)
    J_threshold = sp.Matrix(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [alpha * mu, 0, 0, 0, 0, 0, 0],
            [0, alpha * mu, 0, 0, 0, 0, 0],
            [0, 0, alpha * mu, 0, 0, 0, 0],
        ]
    )
    check("interior_momentum_rank", J_interior.det() != 0, "rank Dp=4 when w is nonzero")
    check("threshold_momentum_rank", J_threshold.rank() == 3, "rank Dp=3 at w=0")
    check("threshold_kernel_dimension", 7 - J_threshold.rank() == 4, "ker Dp has four w directions at w=0")

    lorentz_metric = sp.diag(1, -1, -1, -1)
    check("lorentz_pairing_nondegenerate", lorentz_metric.det() == -1, "the polarized determinant pairing is nondegenerate")
    check(
        "fixed_phase_sequence",
        zero_scalar(sp.symbols("R", positive=True) ** 2 * (alpha**2 * omega2 / sp.symbols("R", positive=True) ** 2) - alpha**2 * omega2),
        "with fixed determinant phase and lambda=R^2, mass is alpha^2|omega|^2/R^2",
    )

    passed = sum(1 for value in checks.values() if value["passed"])
    result = {
        "arithmetic": "exact symbolic",
        "sympy_version": sp.__version__,
        "passed": passed,
        "failed": len(checks) - passed,
        "checks": checks,
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in ("passed", "failed", "sympy_version")}, indent=2))


if __name__ == "__main__":
    main()
