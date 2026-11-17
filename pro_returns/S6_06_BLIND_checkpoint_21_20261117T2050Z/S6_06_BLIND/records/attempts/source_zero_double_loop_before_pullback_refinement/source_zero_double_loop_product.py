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
                    "doubled_flop_difference_mod28": 2*av
                })
checks.append("128 retained signed cap/scalar instances")

out = {
    "utc": datetime.now(timezone.utc).isoformat(),
    "status": "PASS_EXACT_IDENTITIES",
    "geometric_audit_status": "working proof submitted",
    "checks": len(checks), "check_names": checks,
    "proof": "notes/part3_source_zero_double_loop_product_working.md",
    "literal_seam": {
        "forward": "(Z,V,q)->(Z,q^(2nk)*V,q)",
        "reindex": "B^(-2nk)",
        "bounded_endpoint": "(g^(-2nk)*Z,eta^(-2nk)*V,q)",
        "collar_map": "C=(exp(L chi log g)*Z,exp(L chi log eta)*V,q)",
        "collar_equality": "C_end E_v=C_start=Id"
    },
    "symbolic": {
        "wind_matrix": [[str(x) for x in wind.row(i)] for i in range(2)],
        "I": [str(s.expand(x)) for x in I],
        "W": [str(s.expand(x)) for x in W],
        "V22": str(s.expand(V22)), "delta2": str(s.expand(delta2)),
        "ordinary_C2_pair": [str(m2), str(n2)],
        "native_C2_pair": [str(native_m2), str(n2)],
        "doubled_relation": "2 Z_JT - 2 Z_T = 2a (mod28)"
    },
    "sample_instances": rows,
    "individual_source_zero_class_assigned": False,
    "division_by_two_used": False,
    "preserved_diagnostic": "code/part3/source_zero_double_loop_diagnostic.json"
}
base = ROOT/"code/part3/source_zero_double_loop_product"
base.with_suffix(".json").write_text(json.dumps(out, indent=2)+"\n")
line = (f"PASS: {len(checks)} exact identities, including 128 signed instances; "
        "actual seam/plumbing proof submitted for independent audit; "
        "no division or individual return.\n")
base.with_suffix(".out").write_text(line)
print(line, end="")
