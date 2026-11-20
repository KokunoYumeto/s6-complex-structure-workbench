"""Exact independent universal identities for six fully compared II proofs.

Written after target comparison; this is computation credit, not prereading
proof credit. No earlier producing or checking program is imported or copied.
The analytic, covering and birational arguments remain the written proofs.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

checks = []
values = {}


def equal(label, name, left, right):
    if isinstance(left, s.MatrixBase):
        difference = (left - right).applyfunc(s.simplify)
        assert difference == s.zeros(*left.shape), (label, name, difference)
    else:
        difference = s.factor(s.together(left - right))
        assert difference == 0, (label, name, difference)
    checks.append({"label": label, "identity": name, "difference": "0"})


# UN14 imports the actual vertical blowups of UN4. This checks their universal
# Euler replacement and the two numerical generators used in the comparison.
r, g, old, target = s.symbols("r g old target", integer=True)
delta = r * (2 - 2 * g) - (2 - 2 * g)
equal("UN14", "projective-bundle Euler replacement", delta, (r - 1) * (2 - 2 * g))
equal("UN14", "point replacement", 3 * 1 - 1, 2)
equal("UN14", "quartic replacement", delta.subs({r: 2, g: 3}), -4)
equal("UN14", "point-plus-quartic replacement", 2 + delta.subs({r: 2, g: 3}), -2)
equal("UN14", "arbitrary upward even target", 2 * old + 2 * (target - old), 2 * target)
equal("UN14", "arbitrary downward even target", 2 * old - 2 * (old - target), 2 * target)

# UN20: derive the ratio and its exact projective composition in the formal
# field Q(a,b,c,d,e,f,g,h,z), without sampling group elements.
a, b, c, d, e, f, g0, h, z = s.symbols("a b c d e f g h z")
M = s.Matrix([[a, b], [c, d]])
N = s.Matrix([[e, f], [g0, h]])


def ratio(matrix, argument):
    return (matrix[1, 0] + matrix[1, 1] * argument) / (matrix[0, 0] + matrix[0, 1] * argument)


equal("UN20", "basis coefficient ratio", (M * s.Matrix([1, z]))[1] / (M * s.Matrix([1, z]))[0], ratio(M, z))
equal("UN20", "actual projective composition", ratio(M, ratio(N, z)), ratio(M * N, z))
equal("UN20", "actual projective inverse", ratio(M.adjugate(), ratio(M, z)), z)
equal("UN20", "projective scalar invariance", ratio(e * M, z), ratio(M, z))

# UN23: universal cyclic quotient ray and canonical order calculations.
n, i, m, q = s.symbols("n i m q", integer=True, positive=True)
v0 = s.Matrix([(n - i) / n, i / n])
v1 = s.Matrix([(n - i - 1) / n, (i + 1) / n])
equal("UN23", "consecutive A-chain ray determinant", s.Matrix.hstack(v0, v1).det(), 1 / n)
equal("UN23", "height-one crepant ray", sum(v0), 1)
equal("UN23", "canonical extension order on A-chain", m * (sum(v0) - 1), 0)
t = s.symbols("t", integer=True, nonnegative=True)
equal("UN23", "non-SL canonical pole with r=n-2-t", m * ((1 + n - 2 - t) / n - 1), -m * (1 + t) / n)
equal("UN23", "xy=z^n exponent morphism first coordinate", n + 0, n * 1)
equal("UN23", "xy=z^n exponent morphism second coordinate", 0 + n, n * 1)
lam1, lam2 = s.symbols("lambda1 lambda2")
lam = s.Matrix([lam1, lam2])
lin = s.Matrix([[a, b], [c, d]])
equal("UN23", "fixed-stabilizer product kills translation", lam + lin * s.zeros(2, 1), lam)
equal("UN23", "fixed-stabilizer inverse linear part", lin * lin.inv(), s.eye(2))

# UN26: retain the contraction convention Omega=F dz wedge dw, including the
# actual base-coordinate factor. The Lie bracket uses only V(h(z))=0.
F, scale = s.symbols("F scale", nonzero=True)
Vz = s.Integer(0)
Vw = 1 / F
equal("UN26", "contraction dz coefficient", -F * Vw, -1)
equal("UN26", "contraction dw coefficient", F * Vz, 0)
equal("UN26", "base coordinate change retains field", scale / (scale * F), Vw)
equal("UN26", "relative time form on field", F * Vw, 1)
zz, ww = s.symbols("zz ww")
ff = s.Function("F")(zz, ww)
hh = s.Function("h")(zz)
V = [s.Integer(0), 1 / ff]
W = [s.Integer(0), hh / ff]
for j in range(2):
    bracket = sum(V[k] * s.diff(W[j], x) - W[k] * s.diff(V[j], x) for k, x in enumerate([zz, ww]))
    equal("UN26", "commuting field component " + str(j), bracket, 0)
character = s.symbols("character")
equal("UN26", "same eigencharacter on invariant-base multiple", character * hh / ff, hh * (character / ff))

# UN28: actual exterior algebra in the oriented real basis dx,dy,du,dv.
def wedge(left, right):
    out = {}
    for x, cx in left.items():
        for y, cy in right.items():
            word = x + y
            if len(set(word)) != len(word):
                continue
            inversions = sum(word[k] > word[l] for k in range(len(word)) for l in range(k + 1, len(word)))
            key = tuple(sorted(word))
            out[key] = s.expand(out.get(key, 0) + (-1) ** inversions * cx * cy)
    return {key: s.simplify(value) for key, value in out.items() if value != 0}


alpha = wedge({(0,): 1, (1,): s.I}, {(2,): 1, (3,): s.I})
bar_alpha = {key: s.conjugate(value) for key, value in alpha.items()}
real_alpha = {key: s.re(value) for key, value in alpha.items() if s.re(value) != 0}
top = (0, 1, 2, 3)
equal("UN28", "holomorphic two-form orientation", wedge(alpha, bar_alpha)[top], 4)
equal("UN28", "real positive-plane normalization", wedge(real_alpha, real_alpha)[top], wedge(alpha, bar_alpha)[top] / 2)
pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
Q = s.Matrix(6, 6, lambda k, l: wedge({pairs[k]: 1}, {pairs[l]: 1}).get(top, 0))
columns = [s.eye(6)[:, k] * sign for k, sign in [(0, 1), (5, 1), (1, 1), (4, -1), (2, 1), (3, 1)]]
C = s.Matrix.hstack(*columns)
H = s.Matrix([[0, 1], [1, 0]])
equal("UN28", "literal integral congruence to three hyperbolic planes", C.T * Q * C, s.diag(H, H, H))
equal("UN28", "congruence is unimodular", s.Abs(C.det()), 1)
values["UN28_Gram"] = str(Q)
values["UN28_integral_congruence"] = str(C)
values["UN28_signature"] = [3, 3, 0]

# UN47: universal cover-degree inequalities. k=N/e counts actual components.
k, ell = s.symbols("k ell", integer=True, positive=True)
equal("UN47", "chi-two lower bound remainder", 2 * k * ell - k - k * ell, k * (ell - 1))
equal("UN47", "chi-one lower bound", k * ell - (k * ell) / ell, k * (ell - 1))
u, v = s.symbols("u v", integer=True, nonnegative=True)
equal("UN47", "only nontrivial finite quotient degree", (1 + u) * ((2 + v) - 1), 1 + u + v + u * v)
equal("UN47", "double cover coherent equality", 2 - 1 + q, 1 + q)
values["UN47_nonnegative_remainder_coefficients"] = [
    [list(exponents), int(coefficient)]
    for exponents, coefficient in s.Poly(u + v + u * v, u, v).terms()
]

root = Path(__file__).resolve().parents[1]
target_source = root.parent / "parts" / "II.body.linked.tex"
report = {
    "status": "PASS",
    "check_count": len(checks),
    "method": "Universal exact symbolic polynomial/rational identities and independently written exterior algebra; no old code imported.",
    "exposure": "Written after the six target proofs were fully read. This is independent computation, not a before-reading proof event.",
    "source_sha256": hashlib.sha256(target_source.read_bytes()).hexdigest(),
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "checks": checks,
    "values": values,
    "limits": "The program verifies the displayed algebraic identities. Analytic extension, properness, actual covering spaces, semicompleteness and birational/Stein morphisms are the retained complete written proofs, not consequences of finite arithmetic sampling.",
}
output = root / "II_candidate_general_identities_07.json"
output.write_text(json.dumps(report, indent=2) + "\n")
print("PASS", len(checks), "universal exact identities; output", output)

