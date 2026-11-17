"""Exact algebra supporting C.3.12, not a numerical continuity proof."""
import json
from pathlib import Path
import sympy as s

A = 5 + 2*s.sqrt(6)
B = s.Matrix([[0, 1], [-1, 0]])
r = s.symbols('r', real=True)
checks = {
    'A_minimal_polynomial': s.simplify(A*A - 10*A + 1) == 0,
    'A_inverse': s.simplify(1/A - (5 - 2*s.sqrt(6))) == 0,
    'cusp_sin_squared': s.simplify((A + 2 + 1/A)/4) == 3,
    'raw_gamma_limit': B.inv()*s.Matrix([0, r]) == s.Matrix([-r, 0]),
    'u_fan_translation': B*s.Matrix([0, 1]) == s.Matrix([1, 0]),
    'gamma_fan_translation': B*s.Matrix([1, 0]) == s.Matrix([0, -1]),
    'edge_base_exponents': s.simplify(r + (1-r)) == 1,
}
assert all(checks.values()), checks
result = {
    'status': 'PASS',
    'checks': checks,
    'nonunit_modulus': str(A),
    'scope': ('Finite exact checks only. Universal central-fibre collapse '
              'is proved by the limiting-leaf argument in C.3.12.'),
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
