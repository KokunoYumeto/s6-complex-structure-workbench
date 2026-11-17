#!/usr/bin/env python3
"""Exact chart and quaternion checks for the P3K.46 cap morphism."""
from pathlib import Path
import datetime
import json
import sympy as S

ROOT = Path(__file__).resolve().parents[2]
checks = []


def check(name, expression):
    if isinstance(expression, (list, tuple, S.MatrixBase)):
        passed = all(S.simplify(x) == 0 for x in expression)
    elif expression in (True, False):
        passed = bool(expression)
    else:
        passed = S.simplify(expression) == 0
    assert passed, name
    checks.append({"name": name, "pass": True})


z, c0, c1, alpha, kappa = S.symbols("z c0 c1 alpha kappa", nonzero=True)
q = z*c0*c1
Z_half, V_half = kappa*q/z, c1
Z_target, V_target = Z_half/(kappa*q), V_half/alpha
check("actual_source_period_cancels_kappa", Z_target-1/z)
check("target_line_unit_retained", V_target-c1/alpha)
d0, d1 = q/V_target, V_target/Z_target
check("reflected_first_normal_coordinate", d0-alpha*z*c0)
check("reflected_second_normal_coordinate", d1-z*c1/alpha)
check("physical_height_preserved", Z_target*d0*d1-q)
check("second_chart_tangent", 1/Z_target-z)
check("second_chart_first_normal", Z_target*d0-alpha*c0)
check("second_chart_second_normal", Z_target*d1-c1/alpha)

a0, a1, b0, b1, tau = S.symbols("a0 a1 b0 b1 tau", nonzero=True)
check("homogeneous_source_coordinate_swap", a0/a1-1/(a1/a0))
check("homogeneous_first_normal_matches", a1*tau*b0-tau*(a1/a0)*(a0*b0))
check("homogeneous_second_normal_matches", a1*b1/tau-(a1/a0)*(a0*b1)/tau)


def qm(p, v):
    w, x, y, zq = p
    a, b, c, d = v
    return S.Matrix([w*a-x*b-y*c-zq*d,
                     w*b+x*a+y*d-zq*c,
                     w*c-x*d+y*a+zq*b,
                     w*d+x*c-y*b+zq*a])


def qc(p):
    return S.Matrix([p[0], -p[1], -p[2], -p[3]])


i = S.Matrix([0, 1, 0, 0])
j = S.Matrix([0, 0, 1, 0])
r, d = qm(j, i), -i
ur, ui, vr, vi = S.symbols("ur ui vr vi", real=True)
u = S.Matrix([ur, ui, vr, -vi])  # u=a0+j*a1, with right complex coefficients.
check("literal_Cox_source_swap_rud", qm(qm(r, u), d)-S.Matrix([vr, vi, ur, -ui]))
check("r_is_unit", qm(r, qc(r))-S.Matrix([1, 0, 0, 0]))
check("d_is_unit", qm(d, qc(d))-S.Matrix([1, 0, 0, 0]))

br, bi, cr, ci, tr, ti = S.symbols("br bi cr ci tr ti", real=True)
v = S.Matrix([br, bi, cr, ci])  # v=b0+j*conj(b1).
tq = S.Matrix([tr, ti, 0, 0])
# b0 -> tau*b0, b1 -> conjugate(tau)*b1, where |tau|=1.
v_target = S.Matrix([tr*br-ti*bi, tr*bi+ti*br,
                     tr*cr+ti*ci, tr*ci-ti*cr])
check("opposite_normal_gauge_is_physical_right_scalar", qm(v, tq)-v_target)
norm_u = sum(x*x for x in u)
h = qm(qm(u, i), qc(u))/norm_u
Q = qm(u, v)
check("unit_h_square_minus_one", qm(h, h)+S.Matrix([1, 0, 0, 0]))
check("boundary_middle_exponential_identity", qm(-h, Q)-qm(qm(u, d), v))
check("full_Cox_product_arrow", qm(qm(qm(r, -h), Q), tq)-qm(qm(qm(r, u), d), v_target))

sr, si = S.symbols("sr si", real=True)
physical = S.Matrix([sr, si, 0, 0])
check("physical_circle_commutes_with_tau", qm(tq, physical)-qm(physical, tq))
check("physical_equivariance_of_full_arrow",
      qm(qm(qm(qm(r, -h), Q), physical), tq)
      - qm(qm(qm(qm(r, -h), Q), tq), physical))

y1, y2, y3, e0, e1 = S.symbols("y1 y2 y3 e0 e1", real=True)
y = S.Matrix([0, y1, y2, y3])
ey = S.Matrix([e0, e1*y1, e1*y2, e1*y3])
norm_e = e0**2+e1**2*(y1**2+y2**2+y3**2)
check("cap_exponential_inverse_scalar", qm(ey, qc(ey))-S.Matrix([norm_e, 0, 0, 0]))
check("cap_base_rotation_inverse", qm(qm(qc(r), qm(qm(r, y), qc(r))), r)-y)
# With e0=cos(pi|y|/2), e1=-sin(pi|y|/2)/|y|, norm_e=1,
# and ey is the smooth exponential at y=0. Its explicit inverse is qc(ey).
check("cap_fibre_inverse_before_unit_relations",
      qm(qm(qm(qc(ey), qc(r)), qm(qm(qm(r, ey), Q), tq)), qc(tq))
      - norm_e*(tr**2+ti**2)*Q)

k, ell = S.Integer(6), S.Integer(0)
A = (4*k-ell)/24
check("reflected_Jin_index", A-1)
check("fixed_edge_relative_m", 6*A-k)
check("fixed_edge_relative_n", -6*A+6)

report = {
    "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "status": "PASS", "checks_count": len(checks), "checks": checks,
    "statement": "P3K.46", "proof": "notes/part3_source_cusp_reflected_pair_working.md",
    "chart_arrow": "(z,c0,c1)->(1/z,alpha*z*c0,alpha^-1*z*c1)",
    "cap_arrow": "(y,qH,rho)->(r*y*r^-1,r*exp(-pi*y/2)*qH*tau(rho),-rho), r=j*i",
    "characteristic_pair": [6, 0],
    "relative_fixed_edge_coordinates": [0, -6, 1],
    "not_assigned": ["C2 relative integers", "arbitrary-fan return formula"],
}
(ROOT/"code/part3/source_cusp_reflected_pair.json").write_text(json.dumps(report, indent=2)+"\n")
print(f"PASS {len(checks)} exact reflected-chart, actual-cap and characteristic identities.")
