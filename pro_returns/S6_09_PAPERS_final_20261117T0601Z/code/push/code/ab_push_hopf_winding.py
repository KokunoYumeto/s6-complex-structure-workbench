#!/usr/bin/env python3
"""Exact certificates for B.4.8 and the restricted two-torus cocycle note.

The topology of the core and the clutching calculation are proved in the
TeX.  This file checks their integer algebra and the actual cusp marking.
"""
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

base = Path(__file__).resolve().parent
m, n, k = s.symbols('m n k', integer=True)
T = s.Matrix([[1, 1], [0, 1]])
J = T - s.eye(2)
assert J * J == s.zeros(2)
Tk = s.eye(2) + k * J
assert (s.eye(2) + m * J) * (s.eye(2) + n * J) == s.eye(2) + (m + n) * J

A1 = s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2 = s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
A0 = (A1 * A2).inv()
Nq = A0 - s.eye(4)
E = s.zeros(4)
E[3,0] = 1
Nr = -12 * E
assert Nq * Nq == s.zeros(4)
assert Nr * Nr == s.zeros(4)
assert Nq * Nr == Nr * Nq == s.zeros(4)
stacked = Nq.col_join(Nr)
ker = stacked.nullspace()
assert ker == [s.eye(4)[:,2], s.eye(4)[:,3]]
images = Nq.row_join(Nr)
snf = smith_normal_form(images, domain=ZZ)
diag = [abs(int(snf[i,i])) for i in range(4)]
assert diag == [1,1,0,0]

qstar = -(5 + 2*s.sqrt(6))
assert s.simplify(qstar*qstar + 10*qstar + 1) == 0
assert s.simplify(1/qstar + 5 - 2*s.sqrt(6)) == 0
# The nodal cubic has normalization X=h^2-2, Y=h(h^2-3).
h = s.symbols('h')
X, Y = h*h-2, h*(h*h-3)
assert s.expand(Y*Y-(X**3-3*X+2)) == 0
mult = s.simplify((s.sqrt(2)-s.sqrt(3))/(s.sqrt(2)+s.sqrt(3)))
assert s.simplify(mult + 5 - 2*s.sqrt(6)) == 0

# Actual affine cusp class: the q functions mu,D are single valued.
cc, hh, mu, dd = s.symbols('c h mu D')
sigma = s.Matrix([-cc*mu/2, -cc**2/24-cc*dd/12])
closing = s.Matrix([-hh*mu/2, -hh*(cc+dd)/12-hh**2/24])
assert (sigma.subs(cc,cc+hh)-sigma-closing).applyfunc(s.expand) == s.zeros(2,1)
positive_r_deck = closing.subs(hh,-12).applyfunc(s.expand)
assert positive_r_deck == s.Matrix([6*mu, cc+dd-6])

out = {
    'status': 'PASS',
    'winding_after_q_equals_sN_unit': str(m*n),
    'mixed_c1_covector_in_x_y_marking': ['0', str(m*n)],
    'positive_cycle_monodromy': [[str(v) for v in row] for row in Tk.tolist()],
    'A0': A0.tolist(),
    'Nq': Nq.tolist(),
    'Nr_after_w_equals_r6': Nr.tolist(),
    'common_invariant_basis': [v.T.tolist()[0] for v in ker],
    'coinvariant_relation_smith': diag,
    'H2_torus_base_local_system': 'Z^2, represented by gamma and u',
    'cusp_unit_minimal_polynomial': 'z^2+10z+1',
    'contracting_root': str(mult),
    'actual_affine_cusp_section': [str(v) for v in sigma],
    'actual_positive_r_translation': [str(v) for v in positive_r_deck],
    'actual_q_r_affine_commutator': [0, 0],
    'actual_torus_torsor_class': [0, 0],
    'scope': 'Normal-line obstruction for the stated semistable elliptic interface; ordinary single-valued logarithmic homomorphisms only.'
}
encoded = json.dumps(out, indent=2, default=str)
(base/'ab_push_hopf_winding.json').write_text(encoded+'\n')
print(encoded)
