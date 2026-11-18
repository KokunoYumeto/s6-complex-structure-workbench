#!/usr/bin/env python3
"""Exact algebraic certificate accompanying the signed plumbing audit.

Heisenberg matrices check the word using the central-commutator relation;
the geometric faces and their orientations are proved in the notes.
"""
from pathlib import Path
import json
import sympy as s

A = s.eye(3)
A[0, 1] = 1
B = s.eye(3)
B[1, 2] = 1
C = A * B * A.inv() * B.inv()
g = A.inv() * B
boundary_word = B.inv() * g * A
assert boundary_word == C.inv()
Q = s.Matrix([[0, 1], [1, 0]])
p = s.Matrix([4, -4])
p_square = (p.T * Q.inv() * p)[0]
assert p_square == -32
mu_inverse = p_square / 896
assert mu_inverse == s.Rational(-1, 28)
data = {
    'scope': 'central-word and exact intersection-pairing certificate; geometric identifications are proved in the audit notes',
    'disc_orientations': [1, -1, 1],
    'first_face_gluing': 'B: (s,t)->(s,s*t*s^-1)',
    'second_face_gluing': 'A^-1: (s,t)->(t^-1*s*t,t)',
    'outer_boundary_word': 'A^-1*B',
    'after_extending_face_maps': 'B^-1*A^-1*B*A=C^-1',
    'central_word_test_matrix': boundary_word.tolist(),
    'intersection_matrix': Q.tolist(),
    'pontryagin_evaluations_up_to_simultaneous_sign': p.tolist(),
    'relative_p1_square': int(p_square),
    'signature': 0,
    'mu_Sigma_C_inverse': str(mu_inverse),
    'mu_Sigma_C': str(-mu_inverse),
    'Hopf_transfer_comparison': 'lambda(F)=-Sigma_(F^-1); for a disc-supported class, lambda(F)=Sigma_F',
    'fixed_edge_change': 'A -> -5*A mod 28',
    'scope_limitation': 'the changed curve is a semifree fixed edge; other toric edges are not assigned a formula here',
}
Path(__file__).with_suffix('.json').write_text(json.dumps(data, indent=2, default=int) + '\n')
print('PASS: boundary word C^-1, hyperbolic intersection pairing, p1^2=-32, mu(C)=+1/28')
