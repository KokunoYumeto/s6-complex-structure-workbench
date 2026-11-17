"""Exact normalization checks for C.3.14; no actual monodromy value computed."""
from fractions import Fraction
import json
from pathlib import Path
import sympy as s

phi, beta, x, p, t = s.symbols('phi beta x p t')
k = 6*phi + beta
pontryagin_pairing = 4*beta
J = s.expand((pontryagin_pairing - 4*k)/24)
assert J == -phi
index = s.expand((1+x*t**2+x**2*t**4/2+x**3*t**6/6)
                 * (1-p*t**4/24)).coeff(t,6)
assert s.expand(index - (x**3/s.Integer(6)-p*x/s.Integer(24))) == 0
milnor = Fraction(6**2-4,896)
assert milnor == Fraction(1,28)
matrix=s.Matrix([[6,1],[0,4]])
assert matrix.det()==24
record={
    'wall_map_rows_k_p1x': [list(matrix.row(i)) for i in range(2)],
    'wall_knot_phi_to_J': str(J),
    'spin_dirac_degree_six': str(index),
    'milnor_S_2_minus1_EK': str(milnor),
    'actual_J_psi': 'UNCOMPUTED',
    'wall_davis_orientation_sign': 'UNRESOLVED',
    'actual_sixfold_monodromy': 'UNCOMPUTED; equals signed J_psi modulo28',
}
record['wall_map_rows_k_p1x']=[[int(v) for v in row] for row in record['wall_map_rows_k_p1x']]
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
print('PASS: exact normalization identities only; no substituted monodromy value.')
