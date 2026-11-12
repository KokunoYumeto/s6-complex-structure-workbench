"""Exact algebra checks for the original retained-angle derivative framing."""
from pathlib import Path
import hashlib
import itertools
import json
import sympy as s

out = Path(__file__).resolve().parent
checks = []
def check(name, condition):
    assert condition, name
    checks.append({'name': name, 'pass': True})

a,b,c,d = s.symbols('a b c d', real=True)
A = s.Matrix([[a,b],[c,d]])
p = s.Rational(1,4)
N = s.Matrix([
 [s.Rational(1,2),0,-a-c,-b-d,0,0],
 [0,1,0,0,-1,-1],
 [p,0,a,b,0,0],
 [0,0,0,0,1,0],
 [p,0,c,d,0,0],
 [0,0,0,0,0,1],
])
dell = s.Matrix([[1,0,1,0,1,0]])
dphi = s.Matrix([[0,1,0,1,0,1]])
dv_minus_p_dell = s.Matrix([[-p,0,1-p,0,-p,0],[-p,0,-p,0,1-p,0]])
DP = dell.col_join(dphi).col_join(A.inv()*dv_minus_p_dell)
check('full_actual_differential_table', (DP*N-s.eye(4).row_join(s.zeros(4,2))).applyfunc(s.cancel)==s.zeros(4,6))
check('normal_first_orientation_determinant', s.expand(N.det()+A.det())==0)
Np = N*s.diag(1,1,1,1,-1,1)
check('positive_full_frame_orientation', s.expand(Np.det()-A.det())==0)
k0,k1,k2,k3 = s.symbols('k0 k1 k2 k3',positive=True)
K=s.diag(k0,k1,k2,k3)
check('literal_four_cell_dual_frame', (K*DP*N[:,:4]*K.inv()-s.eye(4)).applyfunc(s.cancel)==s.zeros(4))
z,sv,cv=s.symbols('z sv cv',nonzero=True)
Q=s.Matrix([[sv/z,-cv],[cv,sv*z]])
Qstar=s.Matrix([[sv*z,cv],[-cv,sv/z]])
check('SU2_orthogonality_before_unit_circle_relation',s.expand(Q*Qstar-(sv**2+cv**2)*s.eye(2))==s.zeros(2))
check('SU2_determinant_before_unit_circle_relation',s.expand(Q.det()-sv**2-cv**2)==0)
Kv=Q*s.Matrix([[sv,cv],[-cv,sv]])
check('periodic_contraction_start',Kv.subs({sv:0,cv:1})==s.eye(2))
check('periodic_contraction_endpoint',Kv.subs({sv:1,cv:0})==s.diag(1/z,z))
check('periodic_contraction_basepoint',s.expand(Kv.subs(z,1)-(sv**2+cv**2)*s.eye(2))==s.zeros(2))
za,zb=s.symbols('za zb',nonzero=True)
check('two_SU2_endpoints_equal_native_phase_matrix',
      s.diag(1/za,za,1)*s.diag(1/zb,1,zb)==s.diag(1/(za*zb),za,zb))
def q(v):
    x,y=v
    return (x+x*y+y)%2
vec=list(itertools.product(range(2),repeat=2))
check('all_sixteen_spin_quadratic_identities',all(
    q(((x[0]+y[0])%2,(x[1]+y[1])%2)) ==
    (q(x)+q(y)+x[0]*y[1]+x[1]*y[0])%2 for x in vec for y in vec))
check('Arf_one_and_Gauss_sum_minus_two',q((1,0))*q((0,1))==1 and sum((-1)**q(x) for x in vec)==-2)
receipt={'scope':'Exact algebra, not a replacement for topology, compactness, or spin-bordism proofs.',
         'check_count':len(checks),'checks':checks,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(out/'RETAINED_ANGLE_EXACT_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8',newline='\n')
print(json.dumps(receipt,indent=2))
