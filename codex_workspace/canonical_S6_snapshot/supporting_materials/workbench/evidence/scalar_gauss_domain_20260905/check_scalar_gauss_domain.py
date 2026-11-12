"""One small exact symbolic replay; no floating point, searches, or file writes."""

from __future__ import annotations

import json
import time

import sympy as s


started = time.perf_counter()
checks: list[str] = []


def comm(a, b):
    return a * b - b * a


def tf(a):
    return a - s.trace(a) * s.eye(3) / 3


def assert_zero(name, value):
    entries = list(value) if isinstance(value, s.MatrixBase) else [value]
    reduced = [s.expand(s.radsimp(s.cancel(s.expand(entry), extension=True)))
               for entry in entries]
    if any(entry != 0 for entry in reduced):
        raise AssertionError((name, reduced))
    checks.append(name)


delta = s.sqrt(s.Rational(2, 3))
r = s.sqrt(6) / 4
q = s.Matrix([1 / (2 * s.sqrt(2)), 0, 0])
H0 = s.Matrix([[0, 0, 0], [0, -s.Rational(1, 2), 1 / (2 * s.sqrt(2))],
               [0, 1 / (2 * s.sqrt(2)), s.Rational(1, 2)]])
A0 = s.sqrt(2) * s.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
F0 = -2 * H0 + s.diag(-2, 1, 1)
assert_zero("literal force and original constants", comm(A0, comm(A0, H0)) - F0)

e, t, omega = s.symbols("e t omega", real=True)
coordinates = s.symbols("x1 y1 x2 y2 x3 y3 x4 y4", real=True)
x1, y1, x2, y2, x3, y3, x4, y4 = coordinates
v = s.Matrix([x1 + s.I * y1, x2 + s.I * y2])
w = s.Matrix([x3 + s.I * y3, x4 + s.I * y4])


def X(column):
    return s.zeros(1, 1).row_join(-column.H).col_join(column.row_join(s.zeros(2)))


H = s.Matrix([[0, 0, 0], [0, 0, r], [0, r, 0]])
F = -2 * H + s.diag(-2, 1, 1)
C = s.I * e * s.diag(1, 0, -1)
Z1, Z2 = X(v), X(w)
M, N = v * v.H + w * w.H, s.I * (v * w.H - w * v.H)
u, v0, m = M[0, 0], M[1, 1], M[0, 1]
b = s.im((v.H * w)[0]).expand(complex=True)
Q, E = s.diag(1, 2), s.diag(s.Rational(2, 3), -s.Rational(5, 6))


def inertia(Y):
    return tf(comm(H, comm(H, Y)) + q * q.H * Y + Y * q * q.H)


def K(Y):
    return -comm(Z1, comm(Z1, Y)) - comm(Z2, comm(Z2, Y))


trace_residual = s.trace(M) - e ** 2 + 2
real_m = s.re(m).expand(complex=True)
expected_H = s.Matrix([[2 - 4 * r * real_m, 0, 0],
                      [0, 2 * r * real_m - 1, r * trace_residual],
                      [0, r * trace_residual, 2 * r * real_m - 1]])
assert_zero("all nine adjoint scalar residual entries with eight real coordinates",
            comm(C, comm(C, H)) - comm(Z1, comm(Z1, H))
            - comm(Z2, comm(Z2, H)) - F - expected_H)
assert_zero("all three vector scalar residual entries with eight real coordinates",
            (C ** 2 - Z1 ** 2 - Z2 ** 2) * q + 2 * q - trace_residual * q)
gamma0 = e * t / 6 + 4 * e * (u + 2 * v0) + 8 * omega * b
G = e * t * E - 2 * e * (Q * M + M * Q) - 4 * omega * N
assert_zero("all nine full Gauss residual entries with eight real coordinates",
            t * inertia(C) + 2 * K(C) - 4 * omega * comm(Z1, Z2)
            - s.I * s.diag(gamma0, G))
assert_zero("upper Gauss entry is the negative full lower trace", gamma0 + s.trace(G))
assert_zero("two exact rank-one realization factorizations",
            (M + N - (v - s.I * w) * (v - s.I * w).H)
            .row_join(M - N - (v + s.I * w) * (v + s.I * w).H))
assert_zero("two-vector determinant sign identity", s.det(N) + s.det(M))

uu, vv, yy = s.symbols("u v0 y", real=True)
mm = delta + s.I * yy
MM = s.Matrix([[uu, mm], [s.conjugate(mm), vv]])
dd = uu * vv - delta ** 2 - yy ** 2
TT = t * E / 4 - (Q * MM + MM * Q) / 2
assert_zero("complete trace condition with nonzero imaginary off-diagonal part",
            s.trace(MM.adjugate() * TT) - (t * (4 * vv - 5 * uu) / 24 - 3 * dd))
assert_zero("parameterized trace constraint at its exact positive coupling",
            s.trace(MM.adjugate() * TT).subs(t, 72 * dd / (4 * vv - 5 * uu)))

zplus, zminus, zeta = s.symbols("zplus zminus zeta", nonzero=True)


def star_phase(matrix):
    # Exact Laurent coordinate ring of U(1)^3: conjugate(z)=1/z.
    return matrix.H.xreplace({s.conjugate(zplus): 1 / zplus,
                              s.conjugate(zminus): 1 / zminus,
                              s.conjugate(zeta): 1 / zeta})


for sigma in (1, -1):
    point_M = delta * s.Matrix([[1, 1], [1, 2]])
    point_N = sigma * delta / s.sqrt(13) * s.Matrix([[2, -1], [-1, -6]])
    factors = []
    for sign in (1, -1):
        root = s.sqrt(1 + sign * 2 * sigma / s.sqrt(13))
        col = s.sqrt(delta) * s.Matrix([root, (1 - sign * sigma / s.sqrt(13)) / root])
        assert_zero(f"rank-one factor for sigma={sigma}, sign={sign}",
                    col * col.H - point_M - sign * point_N)
        factors.append(col)
    point_v = (zplus * factors[0] + zminus * factors[1]) / 2
    point_w = s.I * (zplus * factors[0] - zminus * factors[1]) / 2
    assert_zero(f"all phases recover both Gram matrices for sigma={sigma}",
                (point_v * star_phase(point_v) + point_w * star_phase(point_w) - point_M)
                .row_join(s.I * (point_v * star_phase(point_w)
                                - point_w * star_phase(point_v)) - point_N))
    point_t = 24 * delta
    point_omega = 3 * sigma * s.sqrt(13) * e / 2
    point_b = -2 * sigma * delta / s.sqrt(13)
    assert_zero(f"full Gauss block and upper entry, both temporal signs, sigma={sigma}",
                s.diag(e * point_t / 6 + 4 * e * (delta + 4 * delta)
                       + 8 * point_omega * point_b,
                       e * point_t * E - 2 * e * (Q * point_M + point_M * Q)
                       - 4 * point_omega * point_N))
    assert_zero(f"all scalar entries at the constructed Gram data, sigma={sigma}",
                s.Matrix([[2 - 4 * r * delta, 0, 0],
                          [0, 2 * r * delta - 1, r * (3 * delta - (2 + 3 * delta) + 2)],
                          [0, r * (3 * delta - (2 + 3 * delta) + 2), 2 * r * delta - 1]]))

x, d0 = s.Rational(1, 2), 1 / (2 * s.sqrt(2))
S = s.Matrix([[d0, -(r + x)], [r + x, d0]]) / s.sqrt(2 * r * (r + x))
U = s.diag(1, S)
W = s.Matrix([[-1 / zeta, -1 / zeta], [zeta, -zeta]]) / s.sqrt(2)
V = s.diag(1, W)
assert_zero("first original unitary frame and retained determinant",
            (U.H * U - s.eye(3)).row_join(s.diag(s.det(U) - 1, 0, 0)))
assert_zero("first frame has the exact ordered literal H eigenvalues",
            U.H * H0 * U - s.diag(0, r, -r))
assert_zero("entire second-frame unit phase and determinant",
            (star_phase(V) * V - s.eye(3)).row_join(s.diag(s.det(V) - 1, 0, 0)))
assert_zero("second frame maps exact H for every retained phase",
            star_phase(V) * s.diag(0, r, -r) * V - H)
B = U * V
assert_zero("literal inverse fixes q and recovers H and F",
            (B * q - q).row_join(B * H * star_phase(B) - H0)
            .row_join(B * F * star_phase(B) - F0))

rho, tau = s.symbols("rho tau", positive=True)
rho_formula = (tau + s.sqrt(tau ** 2 + 4608 * delta ** 2)) / (96 * delta)
assert_zero("inverse formula realizes every retained positive coupling",
            (48 * delta * rho ** 2 - tau * rho - 24 * delta).subs(rho, rho_formula))

print(json.dumps({"status": "PASS", "exact_check_groups": len(checks),
                  "checks": checks, "elapsed_seconds": time.perf_counter() - started,
                  "floating_point_acceptance": False,
                  "spatial_equations_imposed": False,
                  "writes_files": False}, indent=2))
