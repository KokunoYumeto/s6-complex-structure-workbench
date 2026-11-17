"""Independent exact matrix checks for the primitive reduced-III cap notes.

The chart, line-norm, fundamental-group and boundary-cycle proofs remain in
notes/part3_iii_star_reduced_cap.md.  These checks certify their displayed
integral matrices, without supplying the outstanding parameter/page comparison.
"""
from pathlib import Path
import itertools
import json
import sympy as S
from sympy.matrices.normalforms import smith_normal_form

ROOT = Path(__file__).resolve().parents[2]

def matrix(a):
    return [[str(x) for x in row] for row in a.tolist()]

def smith(a):
    return [int(abs(x)) for x in smith_normal_form(a, domain=S.ZZ).diagonal()]

C = 2*S.eye(7)
for i,j in ((0,1),(1,2),(2,3),(3,4),(4,5),(2,6)):
    C[i,j] = C[j,i] = -1
R = C.inv()[:,5]
Q = S.zeros(10)
Q[0,0] = Q[9,9] = -1
Q[0,1] = Q[1,0] = Q[1,9] = Q[9,1] = 1
Q[2:9,2:9] = -C
Q[7,9] = Q[9,7] = 1
F = S.eye(10)[:,1]
M = S.Matrix([-2,-1,*list(2*R),2])
assert Q.det() == -1
assert (M.T*Q*M)[0] == -2
assert (M.T*Q*F)[0] == 0
assert M[9] == 2 and all(x.q == 1 for x in M)
assert (M.T*Q[:,2:9]) == S.zeros(1,7)
assert C.det() == 2

T = S.Matrix([[1,-1],[0,1]])
assert (T-S.eye(2))*S.Matrix([0,1]) == S.Matrix([-1,0])
assert smith(T-S.eye(2)) == [1,0]
J = S.Matrix([[0,1,-1],[-1,0,0],[0,0,1]])
pairs = list(itertools.combinations(range(3),2))
J2 = S.Matrix([[J.extract(I,K).det() for K in pairs] for I in pairs])
z = S.Matrix([-1,1,2])
functional = S.Matrix([[2,-1,-1]])
assert (J-S.eye(3))*z == S.zeros(3,1)
assert functional*(J2-S.eye(3)) == S.zeros(1,3)
assert smith(J-S.eye(3)) == [1,1,0]
assert smith(J2-S.eye(3)) == [1,1,0]
assert functional[0] == 2

m, kappa = S.symbols('m kappa', integer=True)
D1 = S.Matrix([[0,1],[1,-m]])
D2 = S.Matrix([[0,-1],[-1,-kappa]])
P = S.Matrix([[1,-kappa],[0,1]])
assert D1.det() == D2.det() == -1
assert P.det() == 1
assert D2*P == S.Matrix([[0,-1],[-1,0]])
record = {
    'status':'PASS',
    'scope':'Independent exact displayed-matrix audit; no new return index assigned.',
    'E7_cartan':matrix(C),
    'E7_correction':matrix(R),
    'source_gram':matrix(Q),
    'source_gram_determinant':str(Q.det()),
    'actual_line_class_M':matrix(M),
    'line_square':str((M.T*Q*M)[0]),
    'exterior_translation':matrix(T),
    'boundary_J':matrix(J),
    'boundary_wedge2_J':matrix(J2),
    'primitive_invariant':matrix(z),
    'primitive_coinvariant_functional':matrix(functional),
    'D1':matrix(D1),
    'D2_before_boundary_basis_change':matrix(D2),
    'boundary_basis_change':matrix(P),
    'D2_after_boundary_basis_change':matrix(D2*P),
    'degree_one_and_two_determinants':['-1','-1'],
}
target = Path(__file__).with_suffix('.json')
target.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
