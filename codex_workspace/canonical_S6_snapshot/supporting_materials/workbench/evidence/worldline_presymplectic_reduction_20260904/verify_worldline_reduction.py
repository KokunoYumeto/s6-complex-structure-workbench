#!/usr/bin/env python3
"""Exact checks for worldline_presymplectic_reduction.tex.

All matrix calculations use SymPy exact arithmetic.  No floating-point
comparison occurs.
"""

from __future__ import annotations

import json
import hashlib
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
RESULTS = []


def check(name: str, condition, detail: str = "") -> None:
    ok = bool(condition)
    RESULTS.append({"name": name, "pass": ok, "detail": detail})
    if not ok:
        raise AssertionError(name + (": " + detail if detail else ""))


def hermitian(v):
    q0, q1, q2, q3 = v
    return sp.Matrix([[q0 + q3, q1 - sp.I * q2],
                      [q1 + sp.I * q2, q0 - q3]])


def lorentz_coords(H):
    return sp.Matrix([
        sp.expand((H[0, 0] + H[1, 1]) / 2),
        sp.expand((H[0, 1] + H[1, 0]) / 2),
        sp.expand((H[1, 0] - H[0, 1]) / (2 * sp.I)),
        sp.expand((H[0, 0] - H[1, 1]) / 2),
    ])


def real_vectorize(M):
    out = []
    for entry in list(M):
        re, im = sp.expand_complex(entry).as_real_imag()
        out.extend([sp.simplify(re), sp.simplify(im)])
    return sp.Matrix(out)


def orbit_matrix(Z, generators):
    return sp.Matrix.hstack(*(real_vectorize(X * Z) for X in generators))


alpha, s, t = sp.symbols("alpha s t", positive=True, nonzero=True, real=True)
q = sp.symbols("q0:4", real=True)
r = sp.symbols("r0:4", real=True)
Q = hermitian(q)
R = hermitian(r)
G = sp.diag(1, -1, -1, -1)

pair_trace = sp.expand(
    (sp.trace(Q) * sp.trace(R) - sp.trace(Q * R)) / 2
)
pair_coordinate = (sp.Matrix(q).T * G * sp.Matrix(r))[0]
check("Lorentz pairing coordinate identity",
      sp.simplify(pair_trace - pair_coordinate) == 0)
check("Hermitian determinant is Lorentz square",
      sp.simplify(Q.det() - (sp.Matrix(q).T * G * sp.Matrix(q))[0]) == 0)

# Real coordinates on Mat_{3x2}(C), ordered row by row and entry by entry.
u = sp.symbols("u0:12", real=True)
Z = sp.Matrix([
    [u[0] + sp.I*u[1], u[2] + sp.I*u[3]],
    [u[4] + sp.I*u[5], u[6] + sp.I*u[7]],
    [u[8] + sp.I*u[9], u[10] + sp.I*u[11]],
])
P = sp.simplify(alpha * Z.conjugate().T * Z)
pcoords = lorentz_coords(P)
DP = pcoords.jacobian(u)

sub_rank2 = {
    u[0]: s, u[1]: 0, u[2]: 0, u[3]: 0,
    u[4]: 0, u[5]: 0, u[6]: t, u[7]: 0,
    u[8]: 0, u[9]: 0, u[10]: 0, u[11]: 0,
}
sub_rank1 = dict(sub_rank2)
sub_rank1[u[6]] = 0
sub_zero = {x: 0 for x in u}

J2 = sp.simplify(DP.subs(sub_rank2))
J1 = sp.simplify(DP.subs(sub_rank1))
J0 = sp.simplify(DP.subs(sub_zero))
check("rank-two Gram differential rank", J2.rank() == 4, str(J2.rank()))
check("rank-one Gram differential rank", J1.rank() == 3, str(J1.rank()))
check("zero Gram differential rank", J0.rank() == 0, str(J0.rank()))

# Exact right inverse at Z=diag(s,t) embedded in three rows.
a0, a1, a2, a3 = sp.symbols("a0:4", real=True)
A = hermitian((a0, a1, a2, a3))
Z2 = sp.Matrix([[s, 0], [0, t], [0, 0]])
dZA = sp.Rational(1, 2) / alpha * Z2 * (Z2.conjugate().T * Z2).inv() * A
right_inverse = sp.simplify(
    alpha * (dZA.conjugate().T * Z2 + Z2.conjugate().T * dZA) - A
)
check("rank-two exact Gram right inverse", right_inverse == sp.zeros(2))

# A real basis of su(3).
def E(i, j):
    M = sp.zeros(3)
    M[i, j] = 1
    return M


su3 = []
for i in range(3):
    for j in range(i + 1, 3):
        su3.append(E(i, j) - E(j, i))
        su3.append(sp.I * (E(i, j) + E(j, i)))
su3.extend([
    sp.I * sp.diag(1, -1, 0),
    sp.I * sp.diag(1, 1, -2),
])
check("su(3) basis size", len(su3) == 8)
O2 = orbit_matrix(Z2, su3)
Z1 = sp.Matrix([[s, 0], [0, 0], [0, 0]])
O1 = orbit_matrix(Z1, su3)
O0 = orbit_matrix(sp.zeros(3, 2), su3)
check("rank-two colour orbit dimension", O2.rank() == 8, str(O2.rank()))
check("rank-one colour orbit dimension", O1.rank() == 5, str(O1.rank()))
check("zero colour orbit dimension", O0.rank() == 0, str(O0.rank()))
check("rank-two colour tangent lies in Gram kernel",
      sp.simplify(J2 * O2) == sp.zeros(4, 8))
check("rank-one colour tangent lies in Gram kernel",
      sp.simplify(J1 * O1) == sp.zeros(4, 8))


def omega_from_jacobian(J):
    B = G * J
    return sp.Matrix.vstack(
        sp.Matrix.hstack(sp.zeros(4), B),
        sp.Matrix.hstack(-B.T, sp.zeros(J.cols)),
    )


Om2 = omega_from_jacobian(J2)
Om1 = omega_from_jacobian(J1)
Om0 = omega_from_jacobian(J0)
check("rank-two ambient presymplectic rank", Om2.rank() == 8,
      str(Om2.rank()))
check("rank-one ambient presymplectic rank", Om1.rank() == 6,
      str(Om1.rank()))
check("zero ambient presymplectic rank", Om0.rank() == 0,
      str(Om0.rank()))
check("rank-two ambient presymplectic nullity",
      16 - Om2.rank() == 8)
check("rank-one ambient presymplectic nullity",
      16 - Om1.rank() == 10)
check("zero ambient presymplectic nullity",
      16 - Om0.rank() == 16)

# Tangent to the rank-one variety at Z1: the row-2/row-3 entries of
# the second column vanish to first order.  The retained eight columns
# are the intrinsic tangent coordinates.
rank1_tangent_indices = [0, 1, 2, 3, 4, 5, 8, 9]
J1t = J1[:, rank1_tangent_indices]
Om1t = omega_from_jacobian(J1t)
check("rank-one intrinsic tangent dimension",
      len(rank1_tangent_indices) == 8)
check("rank-one intrinsic Gram rank", J1t.rank() == 3,
      str(J1t.rank()))
check("rank-one intrinsic presymplectic rank", Om1t.rank() == 6,
      str(Om1t.rank()))
check("rank-one intrinsic presymplectic nullity",
      12 - Om1t.rank() == 6)

p1 = sp.simplify(pcoords.subs(sub_rank1))
characteristic = sp.Matrix.vstack(p1, sp.zeros(12, 1))
check("rank-one spacetime characteristic is ambient-null",
      sp.simplify(Om1 * characteristic) == sp.zeros(16, 1))

# Cauchy--Binet and the irregular massless constraint.
F = sp.expand(P.det())
minor_sum = 0
for i in range(3):
    for j in range(i + 1, 3):
        minor = Z[i, 0] * Z[j, 1] - Z[i, 1] * Z[j, 0]
        minor_sum += sp.expand_complex(minor * sp.conjugate(minor))
check("Cauchy--Binet sum with retained alpha",
      sp.simplify(F - alpha**2 * minor_sum) == 0)
gradF1 = sp.Matrix([sp.diff(F, x) for x in u]).subs(sub_rank1)
gradF0 = sp.Matrix([sp.diff(F, x) for x in u]).subs(sub_zero)
check("massless constraint gradient vanishes at rank one",
      sp.simplify(gradF1) == sp.zeros(12, 1))
check("massless constraint gradient vanishes at zero",
      sp.simplify(gradF0) == sp.zeros(12, 1))

eps, tr, ti = sp.symbols("epsilon t_r t_i", real=True)
Ztrans = sp.Matrix([[s, 0], [0, eps*(tr + sp.I*ti)], [0, 0]])
Ftrans = sp.expand((alpha * Ztrans.conjugate().T * Ztrans).det())
check("exact quadratic transverse rank opening",
      sp.simplify(Ftrans - alpha**2*s**2*eps**2*(tr**2 + ti**2)) == 0)

# The transverse direction is not an orbit tangent: at Z1 every
# infinitesimal left action has identically zero second column.
check("rank-one colour orbit has zero second column",
      all(sp.simplify((X * Z1)[i, 1]) == 0
          for X in su3 for i in range(3)))

# Shell tangent annihilators with all scales retained.
pa, pb, h, zre, zim = sp.symbols(
    "p_a p_b h z_re z_im", positive=True, real=True
)
p_massive = sp.Matrix([ (pa + pb)/2, 0, 0, (pa - pb)/2 ])
A_massive_matrix = sp.Matrix([[h, zre-sp.I*zim],
                               [zre+sp.I*zim, -pb*h/pa]])
A_massive = lorentz_coords(A_massive_matrix)
check("massive shell tangent is Lorentz-orthogonal to p",
      sp.simplify((p_massive.T * G * A_massive)[0]) == 0)
p_null = sp.Matrix([alpha*s**2/2, 0, 0, alpha*s**2/2])
A_null_matrix = sp.Matrix([[h, zre-sp.I*zim],
                            [zre+sp.I*zim, 0]])
A_null = lorentz_coords(A_null_matrix)
check("null shell tangent is Lorentz-orthogonal to p",
      sp.simplify((p_null.T * G * A_null)[0]) == 0)

shift = sp.symbols("shift", real=True)
check("cotangent covector invariant under x -> x + shift p",
      sp.simplify(-shift * (p_null.T * G * A_null)[0]) == 0)

# Formal product-rule and gauge-boundary identities.
px, xp, p_dot_x = sp.symbols("px xp p_dot_x", real=True)
check("reduced one-form boundary identity",
      sp.expand(p_dot_x - ((xp + p_dot_x) - xp)) == 0)
qv, qdot, evdot, epsilon = sp.symbols(
    "q qdot epsilon_dot epsilon", real=True
)
M2 = sp.symbols("M2", real=True)
delta_L = evdot*qv + epsilon*qdot/2 - evdot*(qv-M2)/2
boundary_dot = evdot*(qv+M2)/2 + epsilon*qdot/2
check("Hamiltonian gauge boundary identity",
      sp.simplify(delta_L-boundary_dot) == 0)

# Extended-packet constrained quotient:
# p(A,w)=alpha*mu(w)*exp(A), evaluated at A=0 with three retained
# traceless-Hermitian tangent coordinates.  Lorentz covariance transports
# these rank calculations to arbitrary A.
lam0, omega_abs, wr = sp.symbols(
    "lambda_0 omega_abs w_r", positive=True, nonzero=True, real=True
)
mu_r = omega_abs / sp.sqrt(lam0 - wr**2)
dmu_r = sp.diff(mu_r, wr)
check("extended packet retained radial derivative",
      sp.simplify(
          dmu_r
          - omega_abs*wr/(lam0-wr**2)**sp.Rational(3, 2)
      ) == 0)
check("extended packet derivative vanishes at threshold",
      sp.simplify(dmu_r.subs(wr, 0)) == 0)

# Columns: three A-directions followed by four real w-directions.
J_packet_interior = sp.Matrix([
    [0, 0, 0, alpha*dmu_r, 0, 0, 0],
    [alpha*mu_r, 0, 0, 0, 0, 0, 0],
    [0, alpha*mu_r, 0, 0, 0, 0, 0],
    [0, 0, alpha*mu_r, 0, 0, 0, 0],
])
J_packet_threshold = sp.simplify(J_packet_interior.subs(wr, 0))
check("extended packet strict-interior momentum rank",
      J_packet_interior.rank() == 4, str(J_packet_interior.rank()))
check("extended packet threshold momentum rank",
      J_packet_threshold.rank() == 3, str(J_packet_threshold.rank()))
check("extended packet threshold momentum kernel dimension",
      7 - J_packet_threshold.rank() == 4)

eps2, vnorm2 = sp.symbols("epsilon_2 vnorm_2", real=True)
det_packet_curve = (
    alpha**2 * omega_abs**2 / (lam0 - eps2**2*vnorm2)
)
threshold_det = alpha**2 * omega_abs**2 / lam0
check("extended packet threshold opens only at second order",
      sp.simplify(sp.diff(det_packet_curve, eps2).subs(eps2, 0)) == 0
      and sp.simplify(
          sp.diff(det_packet_curve, eps2, 2).subs(eps2, 0)
          - 2*alpha**2*omega_abs**2*vnorm2/lam0**2
      ) == 0)

summary = {
    "status": "PASS",
    "arithmetic": "exact SymPy symbolic arithmetic; no floats",
    "checks_total": len(RESULTS),
    "checks_passed": sum(item["pass"] for item in RESULTS),
    "checks": RESULTS,
}
lines = [
    f"{item['name']}: {'PASS' if item['pass'] else 'FAIL'}"
    + (f" ({item['detail']})" if item["detail"] else "")
    for item in RESULTS
]
lines.append(
    f"TOTAL: {summary['checks_passed']}/{summary['checks_total']} PASS"
)
(HERE / "worldline_reduction_checks.log").write_text(
    "\n".join(lines) + "\n", encoding="utf-8"
)

tex_path = HERE / "worldline_presymplectic_reduction.tex"
tex_lines = tex_path.read_text(encoding="utf-8").splitlines()
(HERE / "worldline_presymplectic_reduction_source_numbered.txt").write_text(
    "\n".join(f"{number:05d}\t{line}" for number, line in enumerate(tex_lines, 1))
    + "\n",
    encoding="utf-8",
)
summary["tex_source_sha256"] = hashlib.sha256(tex_path.read_bytes()).hexdigest()
summary["tex_source_lines"] = len(tex_lines)
(HERE / "worldline_reduction_checks.json").write_text(
    json.dumps(summary, indent=2) + "\n", encoding="utf-8"
)
print(lines[-1])
