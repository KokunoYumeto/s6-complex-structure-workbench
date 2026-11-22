#!/usr/bin/env python3
"""Exact symbolic certificate for the independently derived 01CE argument.

This checks identities and finite consequences of the proved geometric bounds;
the geometry, convergence and topological maps are proved in the derivation.
No target proof or local file is read.  Requires SymPy.
"""
import json
import sympy as s

checks = []


def equal(name, left, right):
    residual = s.cancel(s.expand(left - right))
    if residual != 0:
        raise AssertionError((name, str(residual)))
    checks.append({"name": name, "result": "exact"})


def true(name, proposition):
    if not proposition:
        raise AssertionError(name)
    checks.append({"name": name, "result": "exact"})


A, B, C, alpha, beta, gamma, mu = s.symbols(
    "A B C alpha beta gamma mu", nonzero=True
)
x, y, w, d = s.symbols("x y w d")
quartic = A*x*x + B*x*y*y + C*y**4
x_old = alpha*x + beta*y*y
y_old = gamma*y
transformed = s.Poly(s.expand(mu*quartic.subs(
    {x: x_old, y: y_old}, simultaneous=True)), x, y)
An = mu*alpha**2*A
Bn = mu*(alpha*gamma**2*B + 2*alpha*beta*A)
Cn = mu*(gamma**4*C + beta*gamma**2*B + beta**2*A)
equal("quadratic coefficient transition", transformed.coeff_monomial(x**2), An)
equal("mixed coefficient transition", transformed.coeff_monomial(x*y**2), Bn)
equal("fourth coefficient transition", transformed.coeff_monomial(y**4), Cn)
Delta = B**2 - 4*A*C
equal("intrinsic discriminant transition", Bn**2 - 4*An*Cn,
      mu**2*alpha**2*gamma**4*Delta)
x_inv = (x-beta*y*y/gamma**2)/alpha
y_inv = y/gamma
equal("graded inverse x after forward",
      x_inv.subs({x: x_old, y: y_old}, simultaneous=True), x)
equal("graded inverse y after forward",
      y_inv.subs({x: x_old, y: y_old}, simultaneous=True), y)
equal("graded forward x after inverse",
      x_old.subs({x: x_inv, y: y_inv}, simultaneous=True), x)
equal("graded forward y after inverse",
      y_old.subs({x: x_inv, y: y_inv}, simultaneous=True), y)

# A second computation of the discriminant: determinant of the Sylvester map.
P = A*w*w + B*w + C
sylvester = s.Matrix([[A, B, C], [2*A, B, 0], [0, 2*A, B]])
equal("Sylvester determinant for P and its derivative", sylvester.det(), -A*Delta)
equal("resultant from elimination", s.resultant(P, s.diff(P, w), w), -A*Delta)
w_from_d = (d-B)/(2*A)
equal("quadratic field equation after inverse root map",
      P.subs(w, w_from_d), (d*d-Delta)/(4*A))
equal("root coordinate recovered", (2*A*w+B).subs(w, w_from_d), d)
equal("quadratic coordinate recovered", w_from_d.subs(d, 2*A*w+B), w)
equal("root chart transition",
      2*A*(alpha*w+beta)/gamma**2+B,
      (2*An*w+Bn)/(mu*alpha*gamma**2))

ell, degM = s.symbols("ell degM", integer=True)
degL = ell
degQ = -2-ell
degree_A = degM-2*degQ
degree_Delta = 2*degM-2*degQ-4*degL
equal("degree of A", degree_A.subs(degM, 0), 4+2*ell)
equal("degree of discriminant", degree_Delta.subs(degM, 0), 4-2*ell)
equal("ell=-1 degrees", (degree_A+degree_Delta).subs({degM: 0, ell: -1}), 8)
equal("ell=-2 leaves no quadratic zero", degree_A.subs({degM: 0, ell: -2}), 0)
# The derivation proves -2 <= ell <= -1 and that A has at least two zeros.
admissible = [k for k in (-2, -1) if 4+2*k >= 2 and 4-2*k >= 6]
true("complete finite integer consequence", admissible == [-1])
branch_orders = [(i, 6-i) for i in range(1, 6)
                 if i % 2 == 1 and (6-i) % 2 == 1 and i >= 3 and 6-i >= 3]
true("two branch orders exhaust degree six", branch_orders == [(3, 3)])

t, a1, b1, c0, c1 = s.symbols("t a1 b1 c0 c1")
jet_delta = (b1*t)**2 - 4*(a1*t)*(c0+c1*t)
equal("simple discriminant derivative", s.diff(jet_delta, t).subs(t, 0), -4*a1*c0)
equal("square term has no linear coefficient", s.diff((b1*t)**2, t).subs(t, 0), 0)

X, Y, T, scale = s.symbols("X Y T scale", nonzero=True)
bx, by, bt = s.symbols("bx by bt")
F0 = X**2*T + Y**4
dilation = {X: scale**3*X, Y: scale**2*Y, T: scale**2*T}
equal("weight-eight principal part", F0.subs(dilation, simultaneous=True), scale**8*F0)
remainder = X*Y**2*(bx*X+by*Y+bt*T)
equal("positive order of scaled first remainder",
      remainder.subs(dilation, simultaneous=True)/scale**8,
      scale**2*bx*X**2*Y**2 + scale*by*X*Y**3 + scale*bt*X*T*Y**2)
equal("Hirzebruch coordinate map", Y**4-X**2*(-T), F0)
for variable, weight in ((X, 3), (Y, 2), (T, 2)):
    equal("weighted dilation inverse " + str(variable),
          (variable/scale**weight).subs(dilation, simultaneous=True), variable)
equal("complex Jacobian of dilation",
      s.Matrix([dilation[X], dilation[Y], dilation[T]]).jacobian([X, Y, T]).det(),
      scale**7)

# Formal ramified chart for each odd order k=2n+1, with the unit root carried.
z, unitroot = s.symbols("z unitroot", nonzero=True)
n = s.symbols("n", integer=True, nonnegative=True)
ramified_t = z**2
ramified_d = z**(2*n+1)*unitroot
equal("ramified quadratic equation", ramified_d**2,
      ramified_t**(2*n+1)*unitroot**2)
equal("odd-order normalization inverse", ramified_d/(ramified_t**n*unitroot), z)

r, N0, Nplus = s.symbols("r N0 Nplus", integer=True)
eZ = 4+N0+Nplus
eD = 2+r+Nplus
equal("blowup complement Euler number", eZ-eD, 2-r+N0)
c, singular, branches = s.symbols("c singular branches", integer=True)
graph_rank = branches-c-singular+1
equal("normalization pushout Euler number", 2*c-(branches-singular), c+1-graph_rank)
equal("final Euler bound at r=2", (2-r+N0+2).subs(r, 2), 2+N0)

print(json.dumps({
    "tag": "01CE",
    "method": "weighted substitution, Sylvester elimination, root-field inverse maps, symbolic degree and Euler identities",
    "all_passed": True,
    "count": len(checks),
    "checks": checks,
}, indent=2) + "\n", end="")
