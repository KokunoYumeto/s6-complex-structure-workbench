#!/usr/bin/env python3
"""Exact boundary algebra and characteristic arithmetic for C.3.18.

The global Lefschetz-map, determinant-line and smooth framing arguments
are proved in the accompanying text; this is their algebraic audit.
"""
from pathlib import Path
import json
import sympy as sp

S,A,z,q,eps=sp.symbols("S A z q eps")
z1=S**3*A*z**3
z2=S**4*z**4
F=sp.expand((1-eps)*z2**3-z1**4)
F=sp.expand(F.subs(A**4,1-q))
assert sp.expand(F-(q-eps)*S**12*z**12)==0
on_K=sp.expand(F.subs(q,0))
assert on_K == -eps*S**12*z**12
argument_degree=sp.Poly(on_K,z).degree()
assert argument_degree==12
assert argument_degree%2==0

relative_c1_square=0
relative_c2=argument_degree
relative_p1=relative_c1_square-2*relative_c2
assert relative_p1==-24

# At the zero-unit cusp, real complex-fibre coordinates are
# (Re zeta1, Im zeta1, Re zeta2, Im zeta2).
T=sp.symbols("T",positive=True)
gamma=sp.Matrix([0,0,0,-T])
u=sp.Matrix([0,T,0,0])
w=sp.Matrix([1,0,0,0])
delta=sp.Matrix([0,0,1,0])
ordered=sp.Matrix.hstack(delta,gamma,u,w)
assert sp.simplify(ordered.det())==T**2
# Complex elliptic orientation is w,u.  Boundary orientation is
# cyclically equivalent to w,u,gamma, hence gamma,w,u.
swap=sp.Matrix([[1,0,0],[0,0,1],[0,1,0]])
assert swap.det()==-1

result={
    "statement":"C.3.18",
    "status":"PASS",
    "page_polynomial":"(1-epsilon) z2^3-z1^4",
    "exact_collar_identity":str(F),
    "critical_knot_restriction":str(on_K),
    "positive_intersection_count":argument_degree,
    "normal_plane_rotation_winding":-argument_degree,
    "stable_SO5_loop_class_mod2":argument_degree%2,
    "relative_c1_square":relative_c1_square,
    "relative_c2":relative_c2,
    "relative_p1_Lefschetz_orientation":relative_p1,
    "positive_boundary_basis":["gamma","w","u"],
    "transgression_in_gamma_u_w_orientation":-relative_p1,
    "delta_gamma_u_w_real_complex_orientation_determinant":str(ordered.det()),
    "noncomputational_dependencies":[
        "C.3.13 exterior affine torus bundle",
        "C.3.17 exact marked product and identity section",
        "Positive nodal local model and smooth page pullback",
        "Relative determinant-line evaluation across nodal fibres",
        "Outward-vector relative Euler theorem",
        "Exact boundary stable-frame comparison",
    ],
    "scope":"No conversion to cap p1x, cubic k, J, or Theta7 is made."
}
serialized=json.dumps(result,indent=2,default=int)
Path(__file__).with_suffix(".json").write_text(serialized+"\n")
print(serialized)
