"""Exact additional check of the conjugation convention in the integrated V.

This program verifies the cohomology matrix, its unique normalization, and
the parameter sign. It does not numerically recompute X or period solutions.
"""
from pathlib import Path
import json
import sympy as s

A=s.Matrix([[1,0,0,1,-1,1],[0,1,-1,-1,1,0],[0,1,0,-1,0,0],
            [0,2,-1,-1,0,1],[0,2,0,-1,0,0],[0,1,1,-1,0,0]])
B=s.Matrix([[1,0,0,0,0,0],[0,0,-1,0,1,0],[0,0,-1,0,0,1],
            [0,0,-1,0,0,0],[0,1,-1,0,0,0],[0,0,-1,1,0,0]])
K=s.Matrix([[1,2,-1,-1,2,-1],[0,0,0,0,-1,1],[0,0,-1,0,0,1],
            [0,0,0,-1,0,1],[0,-1,0,0,0,1],[0,0,0,0,0,1]])
e=s.eye(6)[:,0]
assert K*K==s.eye(6)
assert K*e==e
assert K*A==A.inv()*K
assert K*B==B.inv()*K
v=s.symbols('v0:36')
T=s.Matrix(6,6,v)
equations=list(T*A-A.inv()*T)+list(T*B-B.inv()*T)
coeff,rhs=s.linear_eq_to_matrix(equations,v)
assert coeff.rank()==35
assert coeff.nullspace()[0].reshape(6,6)==K
normalized,normalized_rhs=s.linear_eq_to_matrix(equations+list(T*e-e),v)
assert normalized.rank()==36
assert list(s.linsolve((normalized,normalized_rhs),v))[0]==tuple(K)

# A symbolic check includes a genuinely non-imaginary parameter, so it
# detects the difference between -conjugate(xi) and conjugate(xi).
x,y,k=s.symbols('x y k',real=True)
xi=x+s.I*y
eta=-s.conjugate(xi)
assert s.im(eta)==y
assert s.simplify(s.conjugate(s.I*k*eta)-s.I*k*xi)==0
assert s.simplify(s.conjugate(s.I*k*s.conjugate(xi))+s.I*k*xi)==0
data={
 'cohomology_K':K.tolist(),
 'K_square_identity':True,
 'K_fixes_e0':True,
 'K_A_equals_A_inverse_K':True,
 'K_B_equals_B_inverse_K':True,
 'anti_intertwiner_solution_dimension':36-coeff.rank(),
 'normalization_rank':normalized.rank(),
 'parameter_map':'xi -> -conjugate(xi)',
 'parameter_imaginary_part_preserved':True,
 'scope':'Exact cohomology conjugation identities and parameter sign; X identification uses the based rational-connection proof in the companion TeX.'
}
out=Path(__file__).resolve().parent.parent/'S6_SERIES_PUBLISH_V_conjugation_exact.json'
out.write_text(json.dumps(data,default=str,indent=2)+'\n')
print(json.dumps(data,default=str,indent=2))
