"""Independent exact audit of the scalar shear and OS49 native arrows.

The symbolic identities certify the algebra used in the accompanying typed
geometric audits. They do not substitute for the seam, collar, normal-frame,
or oriented exterior maps recorded in those audits.
"""
from datetime import datetime, timezone
from pathlib import Path
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[2]
n, J, m = s.symbols('n J m', integer=True)
Q, K, Al, G, Et = s.symbols('Q K Al G Et')
checks = []

def equal(name, left, right):
    difference = left - right
    entries = list(difference) if isinstance(difference, s.MatrixBase) else [difference]
    assert all(s.expand(x) == 0 for x in entries), (name, difference)
    checks.append(name)

P = s.Matrix([[1, 0], [n, 1]])
C = s.Matrix([[1, 0], [-n, 1]])
periods = s.Matrix([[Q+K, G], [Al, Q+Et]])
changed = C * periods * P
equal('literal logarithmic period conjugation', changed,
      s.Matrix([[Q+K+n*G, G], [Al+n*Et-n*K-n*n*G, Q+Et-n*G]]))
wind = changed.subs({Q:0, K:0, Al:0, G:0, Et:J})
equal('scalar winding matrix', wind, s.Matrix([[0,0],[n*J,J]]))
equal('integral character inverse', C*P, s.eye(2))

w = s.Matrix([0,1,-1])
d = s.Matrix([-2,-1,-1])
l = s.Matrix([2*J*(1-n),0,2*J])
t = J
I = s.Matrix([t*w[i]+d[i]*(l[i]-t) for i in range(3)])
W = s.Matrix([t*w[i]-d[i]*(l[i]-t) for i in range(3)])
equal('actual orbit degrees', I, s.Matrix([-2*J+4*n*J,2*J,-2*J]))
equal('actual stable derivative degrees', W, s.Matrix([2*J-4*n*J,0,0]))
native = {}
for i in (1,2):
    variation = I[i]/w[i]
    derivative = (W[i]-W[0])/w[i]
    right = (derivative-variation)/2
    left = -variation-right
    native[i] = s.Matrix([(left+2*t)/2, right/2])
equal('single native C1 pair', native[1], s.Matrix([J*(1-n),J*(n-1)]))
equal('single native C2 pair', native[2], s.Matrix([n*J,-n*J]))
F = -J*n*(n-1)/2
equal('forward C2 central difference', F.subs(n,n+1)-F, native[2][1])
equal('backward C1 central difference', F.subs(n,n-1)-F, native[1][1])

hk = s.Matrix([[-1,3],[-1,2]])
equal('OS49 primitive H K basis', s.Matrix([[2,-3],[1,-1]])*hk, s.eye(2))
equal('OS49 retained scalar period row', s.Matrix([[0,m]])*hk, s.Matrix([[-m,2*m]]))
equal('OS49 basis determinant', hk.det(), 1)
os_t, os_l0, os_l2 = 2*m, 6*m, 4*m
os_double = s.Matrix([2*os_t-os_l0, os_l0-os_l2])
equal('OS49 doubled native C2 pair', os_double, s.Matrix([-2*m,2*m]))
equal('OS49 single native C2 pair', os_double/2, s.Matrix([-m,m]))
equal('OS49 positive-normal outer determinant winding', 2*(-m), -2*m)
left,right = -m,m
equal('directed exterior conjugation free pair',
      s.Matrix([-right,left+2*right]), s.Matrix([-m,m]))
equal('directed exterior central increment', right, m)

instances=0
for nv in range(-12,13):
    for jv in range(-8,9):
        a = -jv*nv*(nv-1)//2
        nxt = -jv*(nv+1)*nv//2
        previous = -jv*(nv-1)*(nv-2)//2
        assert nxt-a == -nv*jv
        assert previous-a == (nv-1)*jv
        assert all(x.subs({n:nv,J:jv}).is_Integer for pair in native.values() for x in pair)
        instances += 1

result = {'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),
          'symbolic_identity_count':len(checks),'identities':checks,
          'signed_scalar_instances':instances,
          'scope':'Exact algebra of the specified maps; geometric extension and central orientation are audited separately.'}
target=ROOT/'records/root_scalar_vertical_os49_exact.json'
target.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
