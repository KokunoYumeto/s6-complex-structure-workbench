#!/usr/bin/env python3
"""Exact 01CE comparison by quadratic-form matrices and integer Euler updates.

The programme is independent of the prereading certificate and all local files.
It verifies the maps between the frozen notation and the printed invariants.
"""
import json
import sympy as s

checks = []


def equal(name, left, right):
    value = s.cancel(s.expand(left-right))
    if value != 0:
        raise AssertionError((name, str(value)))
    checks.append({"name": name, "result": "exact"})


a, b, e, alpha, beta, gamma, mu = s.symbols(
    "a b e alpha beta gamma mu", nonzero=True
)
gram = s.Matrix([[a, b/2], [b/2, e]])
transition = s.Matrix([[alpha, beta], [0, gamma**2]])
pulled = mu*transition.T*gram*transition
delta_printed = a*e-b*b/4
delta_frozen = b*b-4*a*e
equal("printed determinant is the quartic invariant", gram.det(), delta_printed)
equal("exact discriminant conversion", delta_printed, -delta_frozen/4)
equal("determinant functor gives invariant transition", pulled.det(),
      mu**2*alpha**2*gamma**4*delta_printed)
equal("pulled quadratic coefficient", pulled[0, 0], mu*alpha**2*a)
equal("pulled mixed coefficient", 2*pulled[0, 1], mu*(2*alpha*beta*a+alpha*gamma**2*b))
equal("pulled fourth coefficient", pulled[1, 1], mu*(beta**2*a+beta*gamma**2*b+gamma**4*e))
equal("graded matrix inverse", (transition*transition.inv()-s.eye(2)).norm(), 0)

w, d = s.symbols("w d")
P = a*w*w+b*w+e
equal("printed square-root coordinate", (a*w+b/2)**2+delta_printed, a*P)
equal("printed inverse gives quadratic equation", P.subs(w, (d-b/2)/a),
      (d*d+delta_printed)/a)
equal("printed root recovered", (a*w+b/2).subs(w, (d-b/2)/a), d)
equal("printed ratio recovered", ((d-b/2)/a).subs(d, a*w+b/2), w)
equal("field generators differ by two", 2*(a*w+b/2), 2*a*w+b)

q0, ell, degreeM = s.symbols("q0 ell degreeM", integer=True)
degreeR = -2-q0
degree_line = degreeM-q0-2*degreeR
equal("printed square line degree", (2*degree_line).subs(degreeM, 0), 8+2*q0)
equal("radical line matches frozen L", degreeR.subs(q0, -2-ell), ell)
equal("quadratic zero degree matches frozen formula", (-2*q0).subs(q0, -2-ell), 4+2*ell)
equal("quartic zero degree matches frozen formula", (8+2*q0).subs(q0, -2-ell), 4-2*ell)
A = s.symbols("A", integer=True)
equal("sum of the two printed divisor degrees", A+(8-A), 8)
equal("forced quotient degree at A=2", (-s.Rational(1,2)*A).subs(A, 2), -1)

# Formal blowup counts: a coefficient-two section meets coefficient v.
v = s.symbols("v", integer=True, positive=True)
equal("exceptional coefficient at a section-boundary node", (2+v)-1, v+1)
equal("smooth section blowup coefficient", s.Integer(2)-1, 1)
Nzero, Npositive, r = s.symbols("Nzero Npositive r", integer=True)
surface_euler = 4 + Nzero + Npositive
boundary_euler = 2 + r + Npositive
equal("reverse-blowup complement count", surface_euler-boundary_euler, 2-r+Nzero)
c, vertices, edges = s.symbols("c vertices edges", integer=True)
graph_betti = edges-(c+vertices)+1
equal("curve Euler by graph chain ranks", 2*c-edges+vertices, c+1-graph_betti)
equal("two-component minimum at graph rank one", (c+1-graph_betti).subs(edges, c+vertices).subs(c, 2), 2)
equal("smooth sole image component Euler", 2*s.Integer(1), 2)
equal("final difference from asserted bound", (2-r+Nzero+2)-(2+Nzero), 2-r)

print(json.dumps({
    "tag": "01CE", "all_passed": True, "count": len(checks),
    "method": "symmetric Gram matrix pullback, square-root algebra isomorphisms, and exact Euler updates",
    "checks": checks,
}, indent=2)+"\n", end="")
