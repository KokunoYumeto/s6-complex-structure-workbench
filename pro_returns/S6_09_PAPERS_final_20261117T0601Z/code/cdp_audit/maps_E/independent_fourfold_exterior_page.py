"""Independent exact six-dimensional exterior-matrix check of MAPS E1.4.

This complements, and does not replace, the original fourfolds_checks.py.
The transgression ranks are proof inputs; only their diagonal consequence is
checked here.  Cusp specialization and the extra degree-four stalk are also
separate geometric inputs, explicitly recorded in the output.
"""
import json
from itertools import combinations
from pathlib import Path
from sympy import Matrix, diag, eye

out = Path(__file__).resolve().parent
A1 = Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2 = Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
A0 = Matrix([[1,0,0,0],[0,1,0,0],[0,1,1,0],[-1,0,0,1]])
C1 = Matrix([[-1,-1],[1,0]])
C2 = Matrix([[0,1],[-1,0]])
C0 = Matrix([[1,1],[0,1]])
homology = [diag(A0,C0), diag(A1,C1), diag(A2,C2)]
assert A1*A2*A0 == eye(4)
assert C1*C2*C0 == eye(2)
assert homology[1]**3 == eye(6)
assert homology[2]**4 == eye(6)
cohomology = [a.inv().T for a in homology]

def exterior(a,q):
    basis = list(combinations(range(a.rows),q))
    if q == 0:
        return eye(1)
    return Matrix([[a.extract(i,j).det() for j in basis] for i in basis])

rows = []
for q in range(7):
    mats = [exterior(a,q) for a in cohomology]
    dim = mats[0].rows
    differences = [a-eye(dim) for a in mats]
    invariants = [dim-a.rank() for a in differences]
    h0 = dim-Matrix.vstack(*differences).rank()
    h2 = dim-Matrix.hstack(*differences).rank()
    euler = -dim+sum(invariants)
    h1 = h0+h2-euler
    rows.append({'q':q, 'rank':dim, 'local_invariants_p0_p1_p2':invariants,
                 'global_invariants':h0, 'global_coinvariants':h2,
                 'euler_j_star':euler, 'h1':h1,
                 'cohomology_exterior_matrices':[a.tolist() for a in mats]})

E0 = [r['global_invariants']+(r['q']==4) for r in rows]
E1 = [r['h1'] for r in rows]
E2 = [r['global_coinvariants'] for r in rows]
assert E0 == [1,1,2,3,3,1,1]
assert E1 == [0,1,0,1,0,1,0]
assert E2 == [1,1,2,3,2,1,1]
assert rows[2]['local_invariants_p0_p1_p2'][0] == 9
ranks = [0,1,1,2,2,1,1,0]
betti=[]
for n in range(9):
    value = E0[n]-ranks[n] if n<=6 else 0
    value += E1[n-1] if 1<=n<=7 else 0
    value += E2[n-2]-ranks[n-1] if 2<=n<=8 else 0
    betti.append(value)
assert betti == [1,0,2,1,2,1,2,0,1]
assert sum((-1)**i*v for i,v in enumerate(betti)) == 6
record={'method':'Exact rational minors for every exterior power, followed by kernel/image ranks over Q',
        'geometric_inputs_not_proved_by_program':['E1.3 integral cusp specialization and unique degree-four kernel', 'E1.4 six transgression ranks from actual sphere pullback, the zero-section class and Poincare duality'],
        'rows':rows, 'actual_E2_page':[E0,E1,E2],
        'supplied_transgression_ranks':ranks[1:7], 'resulting_betti_numbers':betti}
(out/'independent_fourfold_exterior_page.json').write_text(json.dumps(record,default=int,indent=2)+'\n')
print('Six-dimensional cohomology exterior matrices: all seven degrees checked exactly.')
print('E2 H0:',E0)
print('E2 H1:',E1)
print('E2 H2:',E2)
print('Conditional on the independently read geometric transgressions:',betti)
