"""Exact geometry, derivative-coefficient and representation diagnostics.

These checks support the complete analytic proof. They do not compute an
unknown interacting vacuum or establish a joint continuum spectral limit.
"""
from pathlib import Path
from hashlib import sha256
import itertools
import json
import sympy as s

checks = []

def zero(name, value):
    assert s.expand(value) == 0, (name, value)
    checks.append(name)

m, lt, q, y1, y2 = s.symbols('m L_T q y1 y2', real=True)
d = lt*q + 6*m*m
bmat = s.Matrix([[6*m, lt], [-q, m]])
binv_num = s.Matrix([[m, -lt], [q, 6*m]])
assert bmat*binv_num == d*s.eye(2)
checks.append('original imaginary-block inverse with all sixes')
zero('original imaginary-block determinant', bmat.det()-d)
perm = s.zeros(4)
for row,col in enumerate((2,1,3,0)):
    perm[row,col]=1
assert perm.det()==1 and perm*perm.T==s.eye(4)
checks.append('physical space/time permutation preserves orientation and metric')
u1=(m*y1-lt*y2)/d
u2=(q*y1+6*m*y2)/d
zero('original magnetic two-form',
     s.cancel(s.diff(u1,y1)*s.diff(u2,y2)-s.diff(u1,y2)*s.diff(u2,y1)-1/d))
f=2*s.pi/d**2*(m*q*y1**2/2-lt*q*y1*y2-3*m*lt*y2**2)
orig=[2*s.pi*u1*s.diff(u2,t) for t in (y1,y2)]
zero('first exact gauge derivative y1',s.cancel(orig[0]-s.diff(f,y1)))
zero('first exact gauge derivative y2',s.cancel(orig[1]-2*s.pi*y1/d-s.diff(f,y2)))
f2=-2*s.pi*y1*y2/d
zero('second exact gauge derivative y1',s.diff(f2,y1)+2*s.pi*y2/d)
zero('second exact gauge derivative y2',2*s.pi*y1/d+s.diff(f2,y2))

rotations=[]
for p in itertools.permutations(range(3)):
    for signs in itertools.product((-1,1), repeat=3):
        r=s.zeros(3)
        for i,col in enumerate(p):
            r[i,col]=signs[i]
        if r.det()==1:
            rotations.append(r)
assert len(rotations)==24
for i,j in itertools.product(range(3), repeat=2):
    zero(f'rotation first moment {i}{j}',sum(r[i,j] for r in rotations)/s.Integer(24))
for a,b,c,e in itertools.product(range(3), repeat=4):
    zero(f'rotation second moment {a}{b}{c}{e}',
         sum(r[a,b]*r[c,e] for r in rotations)/s.Integer(24)
         -s.Rational(1,3)*int(a==c)*int(b==e))

for dim in range(1,13):
    j=s.Rational(dim-1,2)
    weights=[-j+k for k in range(dim)]
    zero(f'spin {j} character quadratic coefficient',
         -2*sum(x*x for x in weights)/dim+s.Rational(2,3)*j*(j+1))
zero('original Hc frame and quartic factor',s.Rational(1,4)*s.Rational(4,3)**2-s.Rational(4,9))

ks=s.symbols('k0:3',real=True)
vm=s.Matrix(3,3,lambda i,j:s.Symbol(f'V{i}{j}'))
km=s.diag(*ks)
comm=km*(vm*km-km*vm)-(vm*km-km*vm)*km
for i,j in itertools.product(range(3),repeat=2):
    zero(f'exact magnetic channel double-commutator {i}{j}',
         comm[i,j]+(ks[i]-ks[j])**2*vm[i,j])

halfside,idx,offset=s.symbols('L index offset',integer=True,positive=True)
qm=idx**2+idx+s.Rational(1,2)
angular=(2*halfside*(2*halfside+1)*s.summation(qm**2,(idx,-halfside,halfside-1))
         +4*halfside**2*s.summation(idx**4,(idx,-halfside,halfside)))
angular_printed=halfside**2*(2*halfside+1)*(24*halfside**4+24*halfside**3
                        +8*halfside**2-4*halfside+3)/15
zero('full angular coefficient polynomial',angular-angular_printed)
error_coefficient=s.Rational(2,3)*(2*halfside*(2*halfside+1)
    *s.summation(qm**3,(idx,-halfside,halfside-1))
    +4*halfside**2*s.summation(idx**6,(idx,-halfside,halfside)))
positive_polynomial=s.Poly(s.expand((16*halfside**9-error_coefficient)
                                   .subs(halfside,offset+2)),offset)
assert all(c>0 for c in positive_polynomial.all_coeffs())
checks.append('explicit angular remainder bound for all integer L>=2')
zero('cusp coefficient leading factor',s.LC(s.Poly(angular,halfside))-s.Rational(16,5))

root=Path(__file__).resolve().parent
proof=root/'magnetic_translation_true_vacuum.md'
raw=proof.read_bytes()
receipt={'status':'PASS','check_count':len(checks),'checks':checks,
         'proof_bytes':len(raw),'proof_sha256':sha256(raw).hexdigest(),
         'scope':'Exact geometry/finite algebra only; analytic and vacuum claims proved in source.'}
(root/'MAGNETIC_GEOMETRY_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
print(json.dumps(receipt,indent=2))
