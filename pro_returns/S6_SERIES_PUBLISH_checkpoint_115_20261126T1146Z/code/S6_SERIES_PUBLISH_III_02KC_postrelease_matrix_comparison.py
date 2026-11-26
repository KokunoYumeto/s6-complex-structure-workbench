#!/usr/bin/env python3
"""Exact post-release comparison of the printed B with the fixed fresh D.

The input B is the exact authorized KB matrix used by the 02KC proof.
This is a replay inside one targeted comparison, not an original program
association and not an additional independent check.
"""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import sympy as S

t = S.symbols('t', nonzero=True)
started = datetime.now(timezone.utc).isoformat()
D = S.Matrix([[1,-t,-1/t],[-1,1,1/t],[-1,t,1/t],[-1,t,1]])
B = S.Matrix([[-1,-1,-1,-1],[1,1,1,t],[-t,-t,-1,-t]])
J = S.diag(1,-1,-1,-1)
P = S.Matrix([[1,0,0,0],[0,0,0,1],[0,1,0,0],[0,0,1,0]])
U = S.diag(-1,-t,1)
row = S.Matrix([[1,0,0],[1,1,0],[-t,0,1]])
column = S.Matrix([[-1,-1,-1,-1],[0,0,0,1],[0,0,1,0],[0,1,0,0]])
normal = S.Matrix([[1,0,0,0],[0,t-1,0,0],[0,0,t-1,0]])

def zero(M):
    return all(S.cancel(x)==0 for x in M)

def shown(M):
    return [[str(S.factor(x)) for x in row] for row in M.tolist()]

assert zero(B-U*D.subs(t,1/t).T*J*P)
assert zero(D-J*P*B.subs(t,1/t).T*U.subs(t,1/t).inv().T)
assert P.inv()==P.T and J.inv()==J
assert U.det()==t and row.det()==1
assert column.det() in [1,-1]
assert zero(row*B*column-normal)
assert zero(B-row.inv()*normal*column.inv())
assert zero(B*S.Matrix([-1,1,0,0]))
assert B.subs(t,1).rank()==1

report={
 'scope':'Post-release exact comparison of the printed B(t) and the fixed fresh D(t); no original KC program/result is identified by the released proof or the exact inventory metadata.',
 'started_utc':started,
 'finished_utc':datetime.now(timezone.utc).isoformat(),
 'sympy_version':S.__version__,
 'fresh_homological_D':shown(D),
 'printed_cohomological_B':shown(B),
 'intersection_pairing_J':shown(J),
 'component_basis_P':shown(P),
 'component_basis_inverse':shown(P.inv()),
 'edge_basis_U':shown(U),
 'edge_basis_inverse':shown(U.inv()),
 'exact_relation':'B(t)=U(t)*D(t^-1)^T*J*P',
 'relation_and_inverse_verified':True,
 'row_operation':shown(row),
 'row_operation_inverse':shown(row.inv()),
 'column_operation':shown(column),
 'column_operation_inverse':shown(column.inv()),
 'normal_matrix':shown(normal),
 'normal_form_and_inverse_verified':True,
 'nontrivial_character_kernel_generator':[-1,1,0,0],
 'rank_at_t_one':1,
 'conclusion':'For every nonzero t != 1 the printed B has rank 3, kernel dimension 1 and cokernel 0; the fresh D has rank 3, kernel 0 and cokernel dimension 1 through the displayed exact duality and basis maps.',
 'additional_check_credit':0,
}
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output',type=Path)
args=parser.parse_args()
body=json.dumps(report,indent=2)+'\n'
if args.output is not None:
    args.output.write_text(body)
print(body,end='')
