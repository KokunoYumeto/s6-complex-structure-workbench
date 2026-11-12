"""Exact finite algebra behind the original-coordinate cusp framing proof."""
from pathlib import Path
import hashlib
import json
import sympy as s

ell, lam = s.symbols('ell lam', real=True)
r11, r12, r21, r22 = s.symbols('r11 r12 r21 r22', real=True)
B0 = s.Matrix([[0, 1], [-1, 0]])
R = s.Matrix([[r11, r12], [r21, r22]])
u0 = s.Matrix([s.Rational(-1,4), s.Rational(1,4)])
A = ell*B0 + lam*R
J = s.Matrix([[s.Rational(1,2), -A[0,0]-A[1,0], -A[0,1]-A[1,1]],
              [s.Rational(1,4), A[0,0], A[0,1]],
              [s.Rational(1,4), A[1,0], A[1,1]]])
assert B0*u0 == s.Matrix([s.Rational(1,4),s.Rational(1,4)])
assert s.expand(J.det()-A.det()) == 0
assert J.subs(lam,0).det() == ell**2
assert s.simplify(J*J.inv()) == s.eye(3)
beta = s.Matrix([s.Rational(1,2),s.Rational(1,4),s.Rational(1,4)])
assert J[:,0] == beta and sum(beta) == 1
payload = {'status':'PASS', 'u0':[str(x) for x in u0],
           'B0_u0':[str(x) for x in B0*u0],
           'determinant':str(s.expand(J.det())),
           'endpoint_determinant':str(J.subs(lam,0).det()),
           'checks':['original matrix times chosen quotient lift',
                     'full Jacobian determinant equals det(ell B0+lambda R)',
                     'endpoint determinant ell^2', 'symbolic full inverse',
                     'three positive barycentric exponents sum to one'],
           'scope':'Finite algebra only; the geometric fibre identification and framed nullbordism require the complete proof.'}
encoded = (json.dumps(payload,indent=2)+'\n').encode()
(Path(__file__).parent/'JACOBIAN_CHECK.json').write_bytes(encoded)
print(json.dumps({'status':'PASS','payload_sha256':hashlib.sha256(encoded).hexdigest(),
                  'determinant':payload['determinant']}))
