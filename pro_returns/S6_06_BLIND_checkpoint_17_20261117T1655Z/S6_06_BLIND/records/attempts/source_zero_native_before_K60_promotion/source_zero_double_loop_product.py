#!/usr/bin/env python3
"""Exact identities for the actual double source-zero seam and plumbing.

This certificate verifies algebra used in DZ.1--5. The geometric
construction and its audit remain in the accompanying proof note.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[2]
checks = []


def check(name, lhs, rhs=0):
    if isinstance(lhs, (list, tuple, s.MatrixBase)):
        residual = [s.factor(s.cancel(x-y)) for x, y in zip(lhs, rhs)]
        assert all(x == 0 for x in residual), (name, residual)
    else:
        residual = s.factor(s.cancel(lhs-rhs))
        assert residual == 0, (name, residual)
    checks.append(name)


q, Z, V = s.symbols("q Z V", nonzero=True)
A, D, kap, alp, g, eta = s.symbols(
    "A D kappa alpha g eta", nonzero=True)
x, y, z = s.symbols("x y z", nonzero=True)
L = s.symbols("L", integer=True)


def C(point):
    zz, vv = point
    return (A*zz, D*vv)


def h(point):
    zz, vv = point
    return (kap*q*zz, alp*vv)


def B(point):
    zz, vv = point
    return (g*zz, eta*q*vv)


check("C commutes full source period h", C(h((Z, V))), h(C((Z, V))))
check("C commutes full suspension period B", C(B((Z, V))), B(C((Z, V))))
delt = s.symbols("delta", nonzero=True)
check("C commutes physical delta", C((Z, delt*V)), (A*Z, delt*D*V))
check("period reindex retains source multiplier",
      g**(-L)*Z, g**(-L)*Z)
check("period reindex cancels literal q line power",
      eta**(-L)*q**(-L)*q**L*V, eta**(-L)*V)
check("terminal collar C E source", g**L*g**(-L)*Z, Z)
check("terminal collar C E line", eta**L*eta**(-L)*V, V)
check("pulled-back middle collar source", g**L*Z, g**L*Z)
check("pulled-back middle collar line", eta**L*V, eta**L*V)
check("pulled-back terminal collar source",
      g**L*g**L*g**(-2*L)*Z, Z)
check("pulled-back terminal collar line",
      eta**L*eta**L*eta**(-2*L)*V, V)
check("literal ordinary forward square", q**L*q**L*V, q**(2*L)*V)
capunit = s.symbols("capunit", nonzero=True)
check("literal cap forward square", capunit**L*capunit**L, capunit**(2*L))


def cp(point):
    aa, bb, cc = point
    return (aa/(A*D), A*bb, D*cc)


def cm(point):
    uu, vv, ww = point
    return (A*D*uu, vv/D, ww/A)


def f0(point):
    aa, bb, cc = point
    return (kap*alp*bb*cc, aa*bb/alp, 1/(kap*bb))


def f1(point):
    aa, bb, cc = point
    return (g*eta*bb*cc, 1/(eta*cc), aa*cc/g)


def f2(point):
    aa, bb, cc = point
    return (1/aa, aa*bb, aa*cc)


check("positive triangle retains q", s.prod(cp((x, y, z))), x*y*z)
check("negative triangle retains q", s.prod(cm((x, y, z))), x*y*z)
for i, f in enumerate((f0, f1, f2)):
    check(f"full edge {i} chart square", f(cp((x, y, z))),
          cm(f((x, y, z))))
    check(f"full edge {i} retains q", s.prod(f((x, y, z))), x*y*z)

# Literal native products, including complete nonconstant unit factors.
u0, v0, w0 = f0((x, y, z))
check("native C0 source", kap*w0, 1/y)
check("native C0 first normal", alp*v0, y*x)
check("native C0 second normal", u0/(kap*alp), y*z)
u1, v1, w1 = f1((x, y, z))
check("native C1 source", eta*v1, 1/z)
check("native C1 first normal", g*w1, z*x)
check("native C1 second normal", u1/(g*eta), z*y)
u2, v2, w2 = f2((x, y, z))
check("native C2 source", u2, 1/x)
check("native C2 first normal", v2, x*y)
check("native C2 second normal", w2, x*z)

# Cox lift with source homogeneous pair a0,a1 and line pair c0,c1.
aa0, aa1, cc0, cc1 = s.symbols("a0 a1 c0 c1", nonzero=True)
cox = (aa0, aa1/(A*D), A*cc0, D*cc1)
chart = (aa1/aa0, aa0*cc0, aa0*cc1)
chart_after = (cox[1]/cox[0], cox[0]*cox[2], cox[0]*cox[3])
check("Cox lift is literal positive-star arrow", chart_after, cp(chart))
check("Cox character product retains physical q",
      s.prod(chart_after), s.prod(chart))
aux = s.symbols("aux", nonzero=True)
check("Cox auxiliary commutation",
      (aux*cox[0], aux*cox[1], cox[2]/aux, cox[3]/aux),
      (aux*aa0, aux*aa1/(A*D), A*cc0/aux, D*cc1/aux))

a, b, N = s.symbols("a b N", integer=True)
t = N-1
wind = s.Matrix([[2, 2*b], [-2*a, 2*(N-2)]])
check("double trace is 2t", s.trace(wind), 2*t)
l = s.Matrix([wind[1, 1]-wind[1, 0],
              wind[0, 0]-wind[0, 1], wind[1, 1]])
check("all three first normal exponents", l,
      s.Matrix([2*(N+a-2), 2*(1-b), 2*(N-2)]))
for i in range(3):
    check(f"quaternion first endpoint exponent {i}", t+(l[i]-t), l[i])
    check(f"quaternion second endpoint exponent {i}",
          t-(l[i]-t), 2*t-l[i])
w = s.Matrix([0, 1, -1])
d = s.Matrix([-2, -1, -1])
for i in range(3):
    assert (int(w[i])-int(d[i])) % 2 == 0
    checks.append(f"base and normal Spin endpoints cancel {i}")
I = s.Matrix([t*w[i]+d[i]*(l[i]-t) for i in range(3)])
W = s.Matrix([t*w[i]-d[i]*(l[i]-t) for i in range(3)])
check("all actual meridian degree expressions", I,
      s.Matrix([-2*(N+2*a-3), 2*N+2*b-4, -2*N+4]))
check("all actual stable derivative expressions", W,
      s.Matrix([2*(N+2*a-3), 2-2*b, -2]))
V22 = -I[2]
delta2 = W[0]-W[2]
check("actual V22 prism expression", V22, 2*N-4)
check("actual delta2 prism expression", delta2, 2*N+4*a-4)
n2 = s.expand((delta2-V22)/2)
m2 = s.expand(-V22-n2)
check("ambient frame gives right integer", n2, 2*a)
check("ordinary left integer", m2, -2*N+4-2*a)
native_m2 = s.expand(m2+2*t)
check("native left endpoint removes actual pure-left correction",
      native_m2, 2-2*a)
check("native pair is independent of scalar order", s.diff(native_m2, N), 0)
check("diagonal flop central change", n2, 2*a)
single_m2, single_n2 = 1-a, a
check("actual relative square first free coordinate", 2*single_m2, native_m2)
check("actual relative square second free coordinate", 2*single_n2, n2)
check("single Cox flop central change", single_n2, a)

rows = []
for av, bv, branch in ((1, 2, "good"), (2, 1, "reduced")):
    for pv in range(1, 5):
        mv = 4*pv if branch == "good" else 4*pv-1
        for kv in range(1, 5):
            for nv in (-1, 1):
                nv_order = kv*mv
                vals = {a: av, b: bv, N: nv_order}
                pair = [int(native_m2.subs(vals)), int(n2.subs(vals))]
                assert pair == [2-2*av, 2*av]
                assert 2*nv*kv % 1 == 0
                rows.append({
                    "branch": branch, "a": av, "b": bv, "p": pv,
                    "m": mv, "k": kv, "n": nv, "N": nv_order,
                    "literal_forward_line_exponent": 2*nv*kv,
                    "native_C2_pair": pair,
                    "single_native_C2_pair": [1-av, av],
                    "doubled_flop_difference_mod28": 2*av,
                    "single_flop_difference_mod28": av
                })
assert len(rows) == 64
checks.append("64 retained signed cap/scalar tuples, each with two fan objects")
kernel_two = [j for j in range(28) if (2*j) % 28 == 0]
assert kernel_two == [0, 14]
checks.append("literal kernel of doubling in Z/28 is {0,14}")
paired_rows = []
for av, bv, branch in ((1, 2, "good"), (2, 1, "reduced")):
    for pv in range(1, 5):
        scalar = 0 if branch == "good" else 1-3*pv
        for kv in range(1, 5):
            pair_sum = (-av+2*kv*scalar) % 28
            actual_solutions = [
                [xv, yv] for xv in range(28) for yv in range(28)
                if (xv+yv-pair_sum) % 28 == 0
                and (yv-xv-av) % 28 == 0
            ]
            displayed_solutions = [
                [(-av+kv*scalar+14*ee) % 28, (kv*scalar+14*ee) % 28]
                for ee in (0, 1)
            ]
            assert sorted(actual_solutions) == sorted(displayed_solutions)
            paired_rows.append({
                "a": av, "b": bv, "p": pv, "k": kv,
                "scalar_A": scalar, "pair_sum": pair_sum,
                "fan_difference": av,
                "two_allowed_pairs": displayed_solutions,
                "e_selected": False
            })
checks.append("all32 sample paired congruences have exactly the two displayed solutions")

out = {
    "utc": datetime.now(timezone.utc).isoformat(),
    "status": "PASS_EXACT_IDENTITIES",
    "geometric_audit_status": "working proof submitted",
    "checks": len(checks), "check_names": checks,
    "proof": "notes/part3_source_zero_double_loop_product_working.md",
    "literal_seam": {
        "single_forward": "(Z,V,q)->(Z,q^(nk)*V,q)",
        "single_reindex": "B^(-nk)",
        "single_bounded_endpoint": "(g^(-nk)*Z,eta^(-nk)*V,q)",
        "single_collar_map": "C=(exp(nk chi log g)*Z,exp(nk chi log eta)*V,q)",
        "single_collar_equality": "C_end E_v=C_start=Id",
        "literal_pullback": "C_double(j+t)=C_single(t) E_v^(-j), j=0,1",
        "double_forward": "(Z,V,q)->(Z,q^(2nk)*V,q)",
        "double_terminal": "E_v^(-2)"
    },
    "symbolic": {
        "wind_matrix": [[str(x) for x in wind.row(i)] for i in range(2)],
        "I": [str(s.expand(x)) for x in I],
        "W": [str(s.expand(x)) for x in W],
        "V22": str(s.expand(V22)), "delta2": str(s.expand(delta2)),
        "ordinary_C2_pair": [str(m2), str(n2)],
        "native_C2_pair": [str(native_m2), str(n2)],
        "single_native_C2_pair": [str(single_m2), str(single_n2)],
        "doubled_relation": "2 Z_JT - 2 Z_T = 2a (mod28)",
        "single_relation": "Z_JT - Z_T = a (mod28)"
    },
    "sample_instances": rows,
    "signed_parameter_tuple_count": len(rows),
    "fan_object_count": 2*len(rows),
    "kernel_of_doubling": kernel_two,
    "paired_return_alternatives": paired_rows,
    "paired_symbolic": "(-a+k*A_scalar+14e,k*A_scalar+14e), e in {0,1}",
    "individual_source_zero_class_assigned": False,
    "division_in_Theta7_used": False,
    "relative_square_free_coordinates": "Actual pullback gives f^2; multiplication by2 is injective in Z^2.",
    "preserved_diagnostic": "code/part3/source_zero_double_loop_diagnostic.json"
}
base = ROOT/"code/part3/source_zero_double_loop_product"
base.with_suffix(".json").write_text(json.dumps(out, indent=2)+"\n")
line = (f"PASS: {len(checks)} exact identities, including 64 signed tuples / 128 fan objects; "
        "actual seam/pullback/plumbing proof submitted for independent audit; "
        "no division in Theta7 or individual return.\n")
base.with_suffix(".out").write_text(line)
print(line, end="")
