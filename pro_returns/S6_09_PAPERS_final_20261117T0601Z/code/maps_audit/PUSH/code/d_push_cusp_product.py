#!/usr/bin/env python3
"""Exact local/fan checks for C.3.17; smooth transport is proved in text."""
from pathlib import Path
import json
import sympy as sp

x, y, u, v, A, B = sp.symbols("x y u v A B")
equation = x*y-u*v
chart1 = {u:x*A, y:A*v}
chart2 = {x:u*B, v:B*y}
assert sp.expand(equation.subs(chart1, simultaneous=True)) == 0
assert sp.expand(equation.subs(chart2, simultaneous=True)) == 0
assert sp.expand((x*y).subs(chart1, simultaneous=True)-x*A*v) == 0
assert sp.expand((x*y).subs(chart2, simultaneous=True)-u*B*y) == 0

weights = {"x":0,"y":0,"u":1,"v":-1,"A":1,"B":-1}
assert weights["A"]+weights["v"] == weights["y"] == 0
assert weights["u"]+weights["B"] == weights["x"] == 0
assert weights["x"]+weights["A"] == weights["u"]
assert weights["B"]+weights["y"] == weights["v"]

# Product Tate square, subdivided along the return's (1,0)--(0,1) edge.
triangles = [((0,0),(1,0),(0,1)),((1,0),(0,1),(1,1))]
for tri in triangles:
    lifts = sp.Matrix([[p[0],p[1],1] for p in tri]).T
    assert abs(lifts.det()) == 1
    assert all(0 <= p[0] <= 1 for p in tri)
B0 = sp.Matrix([[0,1],[-1,0]])
gamma_shift = B0*sp.Matrix([1,0])
u_shift = B0*sp.Matrix([0,1])
assert gamma_shift == sp.Matrix([0,-1])
assert u_shift == sp.Matrix([1,0])
assert gamma_shift[0] == 0 and u_shift[0] == 1

# Quotient link: gamma is a direct factor; u -> u+w at a positive q-loop.
monodromy = sp.Matrix([[1,0,0],[0,1,0],[0,1,1]])
assert monodromy*sp.Matrix([1,0,0]) == sp.Matrix([1,0,0])
assert monodromy*sp.Matrix([0,1,0]) == sp.Matrix([0,1,1])
assert monodromy*sp.Matrix([0,0,1]) == sp.Matrix([0,0,1])

# E_I1 retracts to the nodal torus: H0,H1,H2 are Z,Z,Z.
E = [1,1,1]
circle = [1,1]
product = [sum(E[i]*circle[j] for i in range(3) for j in range(2)
               if i+j==k) for k in range(4)]
assert product == [1,2,2,1]

result = {
    "statement":"C.3.17",
    "status":"PASS",
    "conifold_equation":"xy=uv",
    "small_resolution_charts":["u=xA,y=Av","x=uB,v=By"],
    "quotient_projections":["(x,Av,d)->(x,Av)","(uB,y,d')->(uB,y)"],
    "weights":weights,
    "fan_triangles":triangles,
    "gamma_fan_shift":list(gamma_shift),
    "u_fan_shift":list(u_shift),
    "first_projection_periods":{"gamma":0,"u":1},
    "orbit_link_monodromy":monodromy.tolist(),
    "product_betti":product,
    "H3_generator":"[regular elliptic fibre] times [positive gamma circle]",
    "noncomputational_dependencies":[
        "Uniform proper family at bounded period-unit deformation",
        "Prescribed equivariant Ehresmann transport, unitary in fixed tubes",
        "Hopf quotient smooth submersion and identity section",
        "Extension and normalization of a positive vertical density",
    ],
    "scope":"No value of J, k, or the Theta7 monodromy is computed."
}
serialized=json.dumps(result,indent=2,default=int)
Path(__file__).with_suffix(".json").write_text(serialized+"\n")
print(serialized)
