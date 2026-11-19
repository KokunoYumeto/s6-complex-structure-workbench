#!/usr/bin/env python3
"""Exact determinant square for the labelled equivariant cusp plumbing."""
from pathlib import Path
import datetime
import json
import sympy as S

ROOT = Path(__file__).resolve().parents[2]
checks = []


def check(name, value):
    if isinstance(value, bool):
        passed = value
    elif isinstance(value, S.MatrixBase):
        passed = all(S.simplify(x) == 0 for x in value)
    else:
        passed = S.simplify(value) == 0
    assert passed, name
    checks.append({'name': name, 'pass': True})


b, bb, alpha, alphab, kappa = S.symbols('b bb alpha alphab kappa', nonzero=True)
normal = S.diag(bb/alphab, kappa*alpha*b)
check('positive_weight_complex_normal_determinant', normal.det()-kappa*alpha*b*bb/alphab)
A, C, U, V, Ab, Vb = S.symbols('A C U V Ab Vb', nonzero=True)
Gplus, Gminus = S.diag(Ab, C), S.diag(Vb, U)
new_transition = Gminus*normal*Gplus.inv()
check('full_derivative_determinant_square',
      new_transition.det()-(Vb*U)*kappa*alpha*b*bb/(alphab*Ab*C))

aw, cw, uw, vw, kw, alw, etw = S.symbols('aw cw uw vw kw alw etw', integer=True)
det_winding = -vw+uw+kw+2*alw+aw-cw
check('endpoint_relations_leave_exact_obstruction',
      det_winding.subs({uw:-aw, vw:etw-cw})-(kw+2*alw-etw))
check('actual_obstruction_is_minus_six',
      (kw+2*alw-etw).subs({kw:-6, alw:0, etw:0})+6)

matrix = S.Matrix([[1, 0, 1, 0], [0, 1, 0, 1], [1, -1, 1, -1]])
rhs = S.Matrix([0, 0, 6])
check('third_coefficient_row_is_first_minus_second',
      matrix[2,:]-matrix[0,:]+matrix[1,:])
check('coefficient_rank_two', matrix.rank() == 2)
check('actual_augmented_rank_three', matrix.row_join(rhs).rank() == 3)
check('integer_system_has_no_solution',
      S.linsolve((matrix, rhs), (aw,cw,uw,vw)) == S.EmptySet)

# The determinant argument is independent of off-diagonal normal entries:
g11,g12,g21,g22,n11,n12,n21,n22 = S.symbols('g11 g12 g21 g22 n11 n12 n21 n22')
G=S.Matrix([[g11,g12],[g21,g22]])
N=S.Matrix([[n11,n12],[n21,n22]])
check('general_two_by_two_determinant_multiplicativity',
      (G*N).det()-G.det()*N.det())

report = {
    'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'status':'PASS','checks_count':len(checks),'checks':checks,
    'actual_windings':{'kappa':-6,'alpha':0,'eta':0},
    'endpoint_equations':['aw+uw=0','cw+vw=wind(eta)'],
    'determinant_equation':'-vw+uw+wind(kappa)+2wind(alpha)+aw-cw=0',
    'remaining_obstruction':-6,
    'coefficient_matrix':str(matrix),'actual_rhs':str(rhs),
    'scope':'No periodic smooth physical-delta-equivariant product of this labelled three-curve plumbing with its two labelled vertices and positive complex curve orientations.',
    'not_claimed':['An obstruction to separate single-star products','A value of either nonfixed relative return','An impossibility of other all-fan methods'],
    'proof':'notes/part3_source_cusp_product_obstruction_working.md',
}
(ROOT/'code/part3/source_cusp_product_obstruction.json').write_text(json.dumps(report,indent=2)+'\n')
print(f'PASS {len(checks)} exact determinant/winding checks; obstruction -6 to the specified labelled equivariant product.')
