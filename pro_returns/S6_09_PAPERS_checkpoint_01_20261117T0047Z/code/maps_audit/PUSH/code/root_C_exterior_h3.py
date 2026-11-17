#!/usr/bin/env python3
"""Exact exterior-power calculations for a possible global framing route.

This computes lattice maps only.  It does not identify a cap invariant or
silently replace the integral homology of a bielliptic quotient by invariants.
"""
import itertools
import json
from pathlib import Path
import sympy as sp

root = Path(__file__).resolve().parents[1]
A1 = sp.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2 = sp.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
A0 = (A1*A2).inv()
basis = list(itertools.combinations(range(4), 3))

def wedge3(A):
    return sp.Matrix([[A.extract(I,J).det() for J in basis] for I in basis])

norms=[]
for A,n in [(A1,3),(A2,4)]:
    B=wedge3(A)
    assert B**n == sp.eye(4)
    norms.append(sum((B**i for i in range(n)),sp.zeros(4)))
stack=norms[0].col_join(norms[1])
row=lambda M:[[str(v) for v in M.row(i)] for i in range(M.rows)]
result={
    'basis':['gamma_u_w','gamma_u_delta','gamma_w_delta','u_w_delta'],
    'A0':row(A0),
    'norm_A1_wedge3':row(norms[0]),
    'norm_A2_wedge3':row(norms[1]),
    'joint_rank':stack.rank(),
    'joint_kernel':[row(v) for v in stack.nullspace()],
    'gamma_u_w_images':[row(N[:,0]) for N in norms],
    'scope':'Exact rational transfer diagnostics only. No actual J or Theta7 value.'
}
(root/'code/root_C_exterior_h3.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
