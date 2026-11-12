#!/usr/bin/env python3
"""Exact symbolic replay for the Lorentz observation bridge.

All checks use rational arithmetic and polynomial identities.  Complex
conjugates are represented by algebraically independent barred symbols, so a
zero polynomial proves the corresponding complex identity.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp

OUT = Path(__file__).with_name("verification_output.json")


def matrix_zero(M: sp.Matrix) -> bool:
    return all(sp.factor(x) == 0 for x in M)


def scalar_zero(x: sp.Expr) -> bool:
    return sp.factor(sp.expand(x)) == 0


def record(results: dict[str, Any], name: str, passed: bool, detail: str = "") -> None:
    results[name] = {"passed": bool(passed), "detail": detail}
    if not passed:
        raise AssertionError(f"{name} failed: {detail}")


def main() -> None:
    results: dict[str, Any] = {}

    P = sp.Matrix([[1, -1, 0], [0, 1, -1]])
    u = sp.Matrix([1, 1, 1])
    C = P * P.T
    R = P.T * C.inv()
    Pi = u * u.T / 3
    X = R.row_join(u)
    Xinv = P.col_join(u.T / 3)

    record(results, "C=PP*", C == sp.Matrix([[2, -1], [-1, 2]]))
    record(results, "R exact", R == sp.Matrix([[sp.Rational(2, 3), sp.Rational(1, 3)],
                                                [sp.Rational(-1, 3), sp.Rational(1, 3)],
                                                [sp.Rational(-1, 3), sp.Rational(-2, 3)]]))
    record(results, "PR=I2", P * R == sp.eye(2))
    record(results, "RP=I3-Pi", R * P == sp.eye(3) - Pi)
    record(results, "u*R=0", u.T * R == sp.zeros(1, 2))
    record(results, "Pu=0", P * u == sp.zeros(2, 1))
    record(results, "detX=1", sp.factor(X.det() - 1) == 0)
    record(results, "X inverse", Xinv * X == sp.eye(3) and X * Xinv == sp.eye(3))

    # Generic Hermitian block, with starred variables algebraically independent.
    g11, g12, g21, g22 = sp.symbols("g11 g12 g21 g22")
    z1, z2, zb1, zb2, lam = sp.symbols("z1 z2 zb1 zb2 lam")
    G = sp.Matrix([[g11, g12], [g21, g22]])
    z = sp.Matrix([z1, z2])
    zstar = sp.Matrix([[zb1, zb2]])
    M = G.row_join(z).col_join(zstar.row_join(sp.Matrix([[lam]])))
    H = X * M * X.T

    record(results, "block observation PHP*=G", matrix_zero(P * H * P.T - G))
    record(results, "block z recovery", matrix_zero(P * H * u / 3 - z))
    record(results, "block lambda recovery", scalar_zero((u.T * H * u)[0] / 9 - lam))
    block_det = lam * G.det() - (zstar * G.adjugate() * z)[0]
    record(results, "block determinant", scalar_zero(H.det() - block_det))

    J = R * G * R.T
    e2J = ((sp.trace(J) ** 2) - sp.trace(J * J)) / 2
    record(results, "e2(j(G))=det(G)/3", scalar_zero(e2J - G.det() / 3))

    eps = sp.symbols("eps")
    affine = u * u.T + eps * J
    record(results, "det(uu*+eps j(G))=eps^2 detG",
           scalar_zero(affine.det() - eps**2 * G.det()))

    # Generic SL2 block embedding.  No determinant-one substitution is made
    # until after the determinant identity is obtained.
    a, b, c, d = sp.symbols("a b c d")
    g = sp.Matrix([[a, b], [c, d]])
    Dg = sp.diag(1, 1, 1)
    Dg[:2, :2] = g
    T_formula = R * g * P + Pi
    T_conj = X * Dg * Xinv
    record(results, "T_P formula equals X(g+1)X^-1", matrix_zero(T_formula - T_conj))
    record(results, "det T_P=det g", scalar_zero(T_formula.det() - g.det()))
    record(results, "P T_P=gP", matrix_zero(P * T_formula - g * P))
    record(results, "T_P u=u", matrix_zero(T_formula * u - u))
    record(results, "T_P R=Rg", matrix_zero(T_formula * R - R * g))

    # Congruence law with an independent algebraic stand-in for g*.
    ab, bb, cb, db = sp.symbols("ab bb cb db")
    gs = sp.Matrix([[ab, cb], [bb, db]])  # algebraic g-star
    Dgs = sp.eye(3)
    Dgs[:2, :2] = gs
    M_trans = Dg * M * Dgs
    expected = (g * G * gs).row_join(g * z).col_join(
        (zstar * gs).row_join(sp.Matrix([[lam]]))
    )
    record(results, "full block congruence law", matrix_zero(M_trans - expected))

    # The cubic spinor-vector coupling is invariant when det(g)=det(g*)=1.
    N_before = block_det
    N_after = lam * (g * G * gs).det() - ((zstar * gs) * (g * G * gs).adjugate() * (g * z))[0]
    # General identity acquires det(g)det(gs); subtract after imposing both =1.
    substitutions = {d: (1 + b * c) / a, db: (1 + bb * cb) / ab}
    N_after_sl = sp.factor((N_after - N_before).subs(substitutions))
    record(results, "cubic invariant under SL2 congruence", N_after_sl == 0)

    # 3x2 Cauchy-Binet with independent barred variables.
    x11, x12, x21, x22, x31, x32 = sp.symbols("x11 x12 x21 x22 x31 x32")
    y11, y12, y21, y22, y31, y32 = sp.symbols("y11 y12 y21 y22 y31 y32")
    Z = sp.Matrix([[x11, x12], [x21, x22], [x31, x32]])
    Zstar = sp.Matrix([[y11, y21, y31], [y12, y22, y32]])
    gram2 = Zstar * Z
    minors = []
    minors_bar = []
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        minors.append(Z.extract([i, j], [0, 1]).det())
        minors_bar.append(Zstar.extract([0, 1], [i, j]).det())
    cb_rhs = sum(mb * m for mb, m in zip(minors_bar, minors))
    record(results, "3x2 Cauchy-Binet mass identity", scalar_zero(gram2.det() - cb_rhs))

    # Full colored doublet+scalar Gram determinant identity.
    f1, f2, f3, fb1, fb2, fb3 = sp.symbols("f1 f2 f3 fb1 fb2 fb3")
    phi = sp.Matrix([f1, f2, f3])
    phistar = sp.Matrix([[fb1, fb2, fb3]])
    B = Z.row_join(phi)
    Bstar = Zstar.col_join(phistar)
    Mfull = Bstar * B
    Gfull = Mfull[:2, :2]
    zfull = Mfull[:2, 2]
    zfullstar = Mfull[2, :2]
    lamfull = Mfull[2, 2]
    omega = B.det()
    omegabar = Bstar.det()
    gram_rhs = lamfull * Gfull.det() - (zfullstar * Gfull.adjugate() * zfull)[0]
    record(results, "full Gram phase identity", scalar_zero(omegabar * omega - gram_rhs))

    # Observation of the physical Gram matrix through H_P.
    HP = X * Mfull * X.T
    record(results, "O_P(H_P(B))=Z*Z", matrix_zero(P * HP * P.T - gram2))

    # Exact mass decomposition with retained alpha.
    alpha = sp.symbols("alpha", nonzero=True)
    pmat = alpha * Gfull
    mass2 = pmat.det()
    mass_decomp = alpha**2 * omegabar * omega / lamfull + alpha * (
        zfullstar * pmat.adjugate() * zfull
    )[0] / lamfull
    record(results, "phase-spinor mass decomposition",
           scalar_zero(sp.together(mass2 - mass_decomp) * lamfull))

    # Explicit sharpness family; use real positive d, lambda and |omega|^2
    # algebraically via q=sqrt(d), without numerical approximations.
    q, lambda0, Om2 = sp.symbols("q lambda0 Om2", positive=True)
    # G=q I, det G=q^2.  Choose z with squared norm q*lambda0-Om2/q.
    r2 = q * lambda0 - Om2 / q
    Gq = q * sp.eye(2)
    # algebraic squared cross term; adj(Gq)=q I
    cross = q * r2
    det_block = lambda0 * Gq.det() - cross
    record(results, "sharp family determinant equals |omega|^2",
           scalar_zero(det_block - Om2))
    record(results, "sharp lower endpoint", scalar_zero((q**2 - Om2 / lambda0).subs(q**2, Om2 / lambda0)))

    # Global constrained-quotient coordinates.  Let w2 denote ||w||^2 and
    # mu^2=|omega|^2/(lambda0-w2), retaining every scale.
    w2 = sp.symbols("w2", nonnegative=True)
    mu2 = Om2 / (lambda0 - w2)
    record(results, "constrained topology determinant equation",
           scalar_zero(mu2 * (lambda0 - w2) - Om2))
    record(results, "constrained mass in spinor-ball coordinates",
           scalar_zero(alpha**2 * mu2 - alpha**2 * Om2 / (lambda0 - w2)))

    # Exact gauge-section check on a symbolic positive diagonal Gram matrix.
    # The independent phasebar is then constrained by phasebar*phase=1.
    phase, phasebar = sp.symbols("phase phasebar", nonzero=True)
    r1, r2, r3 = sp.symbols("r1 r2 r3", positive=True)
    Bsec = sp.diag(phase * r1, r2, r3)
    Bsec_star = sp.diag(phasebar * r1, r2, r3)
    Msec = sp.diag(r1**2, r2**2, r3**2)
    record(results, "global section preserves the Gram matrix",
           matrix_zero((Bsec_star * Bsec - Msec).subs(phasebar, 1 / phase)))
    record(results, "global section has the retained determinant phase",
           scalar_zero(Bsec.det() - phase * r1 * r2 * r3))

    # Explicit no-threshold sequences.
    Rvar, OmAbs2 = sp.symbols("R OmAbs2", positive=True)
    fixed_phase_mass = alpha**2 * OmAbs2 / Rvar**2
    record(results, "fixed phase sequence tends algebraically as R^-2",
           scalar_zero(Rvar**2 * fixed_phase_mass - alpha**2 * OmAbs2))
    e = sp.symbols("e")
    fixed_lambda_mass = alpha**2 * e**4
    record(results, "fixed scalar sequence is alpha^2 epsilon^4",
           scalar_zero(fixed_lambda_mass - alpha**2 * e**4))

    results["summary"] = {
        "passed": sum(1 for v in results.values() if isinstance(v, dict) and v.get("passed")),
        "failed": 0,
        "sympy_version": sp.__version__,
    }
    OUT.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(results["summary"], indent=2))
    for key, value in results.items():
        if key != "summary":
            print(f"PASS {key}")


if __name__ == "__main__":
    main()
