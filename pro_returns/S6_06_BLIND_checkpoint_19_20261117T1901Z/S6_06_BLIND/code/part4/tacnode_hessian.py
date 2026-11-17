"""Exact local checks for P4R.10--11; the proof is uniform, not bounded."""
from pathlib import Path
import json
import sympy as s

out = Path(__file__).with_suffix('.json')
t, x, y, z, aa, cc = s.symbols('t x y z aa cc')
H = y**2-x**3
f = (aa*z+cc*H)**2+H**4
curve = {x:t**2,y:t**3,z:0}
q = s.hessian(f,(x,y,z)).subs(curve)
ell = s.Matrix([-3*cc*t**4,2*cc*t**3,aa])
assert s.simplify(q-2*ell*ell.T) == s.zeros(3)
u = s.Matrix([-3*t,2,0])
dh = s.Matrix([s.diff(H,v).subs(curve) for v in (x,y,z)])
assert dh == t**3*u
assert (s.Matrix([[2*t,3*t**2,0]])*u)[0] == 0

planar = 0
for m in range(2,21):
    for a in range(m,m+11):
        for c in range(0,42):
            for d in range(0,42):
                if d+2*c >= 2*a:
                    b = min(a,c)
                    assert d+2*b >= 2*a > 2*(m-1)
                    planar += 1
nonplanar = 0
for m in range(2,21):
    for a in range(0,43):
        for b in range(0,43):
            if a+b >= 2*m:
                d = a
                assert d+2*b >= 2*m > 2*(m-1)
                nonplanar += 1

# The allowed F1A3 local model has a single simple Hessian zero.
F1 = z*x**2+x*y**2
q1 = s.hessian(F1,(x,y,z)).subs({x:0,y:0})
assert q1 == s.diag(2*z,0,0)
# The two monic factors of an actual product tacnode give its normalization.
assert s.expand((x-y**2)*(x+y**2)) == x**2-y**4
result = {
    'status':'PASS',
    'proofs':['P4R.10','P4R.11'],
    'planar_bound':{'m':[2,20],'a':'m through m+10','c':[0,41],'d':[0,41],
                    'cases':planar,'assertion':'d+2 min(a,c) >= 2a > 2(m-1)'},
    'nonplanar_bound':{'m':[2,20],'a':[0,42],'b':[0,42],
                       'cases':nonplanar,'assertion':'a+2b >= 2m > 2(m-1), for a+b>=2m'},
    'cusp_parametrization':['t^2','t^3','0'],
    'cusp_conormal_generator':list(map(str,dh)),
    'primitive_plane_kernel':list(map(str,u)),
    'conormal_colength':3,
    'derivative_ramification_order':1,
    'rank_one_hessian':[[str(q[i,j]) for j in range(3)] for i in range(3)],
    'F1A3_hessian':[[str(q1[i,j]) for j in range(3)] for i in range(3)],
    'scope':'These exact checks supplement the unbounded local lattice proof; they do not replace it.'
}
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
