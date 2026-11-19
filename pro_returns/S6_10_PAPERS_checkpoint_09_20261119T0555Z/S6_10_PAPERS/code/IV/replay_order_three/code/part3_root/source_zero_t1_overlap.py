"""Exact T1/V chart overlap of the actual reduced a=2 Cox quotient.

All identities use the full source products. No source-zero return is
assigned by this local certificate.
"""
from datetime import datetime, timezone
from pathlib import Path
import json
import sympy as s

root = Path(__file__).resolve().parents[2]
A, B, C, h, zeta = s.symbols('A B C h zeta', nonzero=True)
checks = []


def check(name, left, right):
    assert s.simplify(left - right) == 0, name
    checks.append(name)


# D=h^2 on the actual two-sheeted cover of the overlap D != 0.
# Target order is (S0,S1,T1,z), with V=1.
target = s.Matrix([h*A, h*B, 1/h, h*C])
S0, S1, T1, z = target
check('q1 is preserved literally', S0*z, A*C*h**2)
check('q2 is preserved literally', S1*T1, B)
check('cross source product S0*T1', S0*T1, A)
check('cross source product S1*T0', S1*z, B*C*h**2)
check('conifold determinant', (S0*z)*(S1*T1)-(S0*T1)*(S1*z), 0)

# Chain rule d/dD=(1/(2h))*d/dh; no chosen positive square root.
jac = target.jacobian([A, B, C, h])
jac[:, 3] = jac[:, 3]/(2*h)
check('full complex determinant in A,B,C,D', jac.det(), s.Rational(1, 2))
check('contracted canonical volumes', -2*jac.det(), -1)

# Inverse is read on the V=1 cover; the deck signs cancel.
inverse = s.Matrix([S0*T1, S1*T1, z*T1, T1**-2])
for label, left, right in zip(('A','B','C','D'), inverse, [A,B,C,h**2]):
    check('inverse '+label, left, right)
for i in range(4):
    check('actual root deck coordinate '+str(i), target[i].subs(h,-h), -target[i])
check('root deck determinant', (-s.eye(4)).det(), 1)

# Physical phase exp(i phi)=zeta^2. D has weight -1,
# C has weight +1, so h lifts with half weight -1/2.
phase = {C:zeta**2*C, h:zeta**-1*h}
for i, weight in enumerate((-1,-1,1,1)):
    check('physical half-weight '+str(i),
          target[i].subs(phase, simultaneous=True), zeta**weight*target[i])
check('physical complex determinant', zeta**(-1-1+1+1), 1)

# The same ambient radial defining function in the two gauges.
aa, bb, cc, hh = s.symbols('aa bb cc hh', nonnegative=True)
Hprime = aa+bb+cc
Hcharged = hh*Hprime
check('full radial equation', Hcharged/hh+Hcharged**2,
      Hprime+Hprime**2*hh**2)

out = {
    'utc': datetime.now(timezone.utc).isoformat(),
    'status':'PASS', 'checks':len(checks), 'identities':checks,
    'source_chart':'T1=1; (A,B,C,D); D != 0 on overlap',
    'target_chart':'V=1; (S0,S1,T1,z) modulo simultaneous mu2',
    'map':'h^2=D; (hA,hB,h^-1,hC)',
    'inverse':'(S0*T1,S1*T1,z*T1,T1^-2)',
    'volume':'(-2 dS0 dS1 dT1 dz) pulls back to -dA dB dC dD',
    'scope':'Exact local overlap, physical equivariance and full source products. The global period/reset attachment and source-zero return remain separate obligations.'
}
(root/'code/part3_root/source_zero_t1_overlap.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
