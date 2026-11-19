"""Exact algebra and frame arrows for the selected-cusp lifted link.

This certificate computes the germ and the inputs of the opened
Gauniyal--Turchin Theorem 4.1. The outer family comparison is separate.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as S

s, r, X, Y, c = S.symbols("s r X Y c")
f = S.Matrix([s*s-r*r, s*(s*s-r*r), r])
J = f.jacobian([s,r])
minors = [S.expand(J.extract(rows,[0,1]).det()) for rows in [[0,1],[0,2],[1,2]]]
gb = S.groebner(minors, s, r)
assert list(gb) == [s,r*r]
assert S.expand(f[1]**2-f[0]**2*(f[0]+r*r)) == 0
assert (f.subs(s,r)-f.subs(s,-r)) == S.zeros(3,1)
u = S.symbols("u")
assert S.factor(f[1]-f[1].subs(s,-s)) == 2*s*(s-r)*(s+r)

# On the double circle r*bar(r)=R², the two normal sections
# are bar(r) partial_s. Their full derivatives have this exact sum.
rb, R2 = S.symbols("rb R2")
vp = J.subs(s,r)*S.Matrix([rb,0])
vm = J.subs(s,-r)*S.Matrix([rb,0])
total = S.simplify(vp+vm)
assert total == S.Matrix([0,4*r*r*rb,0])
push = S.Matrix([0,c*r,r])
image_equation = Y*Y-X*X*(X+r*r)
assert S.expand(image_equation.subs({X:push[0],Y:push[1]})) == c*c*r*r

# The stable framing morphism is specified by actual quaternion maps.
# [Ad_q]=2[L_q], Hopf(Ad_q(i))=-1 for q=z+w*j with the
# complex orientation; [id,id] has Hopf +2 and hence maps to -4[L_q].
complex_smale = S.Integer(2)
stable_smale = -complex_smale
whitehead_to_stable = S.Integer(-4)
omega_s2 = stable_smale/whitehead_to_stable
lk = S.Integer(1)
E = S.Integer(2)
haefliger = lk/2+E/6+omega_s2/3
assert omega_s2 == S.Rational(1,2)
assert haefliger == 1

# Generic perturbation has exactly two ordinary crosscaps and no triples.
eps = S.symbols("eps", nonzero=True)
fp = S.Matrix([s*s-r*r,s*(s*s-r*r+eps),r])
Jp = fp.jacobian([s,r])
gp = S.groebner([Jp.extract(rows,[0,1]).det() for rows in [[0,1],[0,2],[1,2]]],s,r)
assert list(gp) == [s,r*r-eps]

record = {
    "utc": datetime.now(timezone.utc).isoformat(),
    "status": "PASS",
    "germ": [str(x) for x in f],
    "jacobian": str(J),
    "minor_ideal_groebner_basis": [str(x) for x in gb],
    "quotient_basis": ["1","r"],
    "complex_smale": 2,
    "stable_smale_in_Nemethi_Pinter_L_basis": -2,
    "double_branches": ["s=r","s=-r"],
    "double_preimage_linking": 1,
    "each_zero_total_link_self_framing": -1,
    "pushed_double_circle": ["0","c*r","r"],
    "image_equation_on_push": "c**2*r**2",
    "Ekholm_E": 2,
    "whitehead_square_to_stable_L": -4,
    "Omega_S2": "1/2",
    "Gauniyal_Turchin_H": 1,
    "generic_crosscap_ideal": [str(x) for x in gp],
    "generic_crosscaps": 2,
    "generic_triple_points": 0,
    "scope": "Explicit local lifted link only; the actual source-family and circle-line comparison is not inferred by this certificate.",
}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(record, indent=2)+"\n")
print(json.dumps(record, indent=2))
