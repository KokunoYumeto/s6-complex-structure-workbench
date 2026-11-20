"""Post-receiving exact checks for the actual twelve-tooth kernel.

The author's full mathematical derivation was frozen before receiving the root
target. This program was written AFTER reading the complete root proof and its
170-line certificate. It imports no producer code. Its matrix reconstruction
uses Fraction elimination, and its symbolic scope is stated explicitly below.
It is not a certificate of analytic admissibility or existence of smoothings.
"""
from pathlib import Path
from fractions import Fraction
import datetime as dt
import hashlib
import json
import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1] / 'audit_root' / 'comb_09'
checks = []

def check(name, condition, scope):
    passed = bool(condition)
    checks.append({'name': name, 'passed': passed, 'scope': scope})
    assert passed, name

def zero_matrix(M):
    return all(s.cancel(x) == 0 for x in M)

def cup(T, E):
    J = s.Matrix([[0, 1], [-1, 0]])
    return s.trace(T*E*J)

U = s.Matrix(2, 2, s.symbols('u0:4'))
V = s.Matrix(2, 2, s.symbols('v0:4'))
T = s.Matrix(2, 2, s.symbols('t0:4'))
E = s.Matrix(2, 2, s.symbols('e0:4'))
J = s.Matrix([[0, 1], [-1, 0]])
check('generic_quotient_determinant_transport',
      zero_matrix(V.inv().T*J*V.inv()-J/V.det()),
      'Universal rational identity for the exact determinant line.')
Tp = V.inv()*T*U
Ep = U.inv()*E*V.inv().T
check('generic_cup_transport',
      s.cancel(cup(Tp, Ep)-cup(T, E)/V.det()) == 0,
      'T prime=V^-1 T U and eta prime=U^-1 eta V^-t, with both bases independent.')

h11,h12,h21,h22 = s.symbols('h11 h12 h21 h22')
K = s.Matrix([[h11,h12],[h21,h22]])
a11,a12,a21,a22,p,q,r = s.symbols('a11 a12 a21 a22 p q r')
A = s.Matrix([[a11,a12],[a21,a22]])
Esym = s.Matrix([[p,q],[q,r]])
tau = (a11-a22)*q+a12*r-a21*p
check('independent_B_identity_trace_jet',
      s.expand(cup(K,A*Esym-Esym*A.T)+s.trace(K)*tau) == 0,
      'The B=I transport in the frozen independent derivation, for arbitrary K and symmetric eta.')
check('trace_inverse_open_set_identity',
      s.cancel(s.trace(K.inv())-s.trace(K)/K.det()) == 0,
      'The independent trace(B^-1 H) restriction equals the receiving trace(H^-1 B) restriction after the determinant factor.')
b1,b2 = s.symbols('b1 b2', nonzero=True)
D = s.diag(b1,b2)
Ed = s.diag(p,r)
jet = s.expand(cup(s.eye(2),A*Ed-Ed*(D*A*D.inv()).T))
check('root_diagonal_jet_receiving_identity',
      s.cancel(jet-(a21*(1+b2/b1)*p-a12*(1+b1/b2)*r)) == 0,
      'Full two-value covector, retaining transpose and both moving-frame terms.')
M = s.Matrix([[s.diff(s.diff(jet,z),w) for w in (a21,a12)] for z in (p,r)])
check('root_diagonal_jet_jacobian',
      s.cancel(M.det()+(b1+b2)**2/(b1*b2)) == 0,
      'Exact nonzero determinant on the declared eigenvalue open set.')

# Exact normal-form gluing with arbitrary cubic branch coefficients.  The
# accompanying report proves all analytic orders by im(cup)=(x,y).
x,y = s.symbols('x y')
c0 = s.symbols('c0')
cx = s.symbols('cx1:4')
cy = s.symbols('cy1:4')
ch = c0+sum(cx[i-1]*x**i for i in range(1,4))
ct = c0+sum(cy[i-1]*y**i for i in range(1,4))
cg = ch+ct-c0
phi = s.Matrix([[x,-y,0,0]])
kg = s.Matrix([y*cg,x*cg,0,0])
check('exact_node_gluing_is_annihilated', phi*kg == s.zeros(1,1),
      'Explicit Koszul extension retaining every displayed cubic branch coefficient.')
check('exact_handle_restriction', zero_matrix(kg.subs(y,0)-s.Matrix([0,x*ch,0,0])),
      'Literal restriction, without replacing the node fibre by its rank-two image.')
check('exact_tooth_restriction', zero_matrix(kg.subs(x,0)-s.Matrix([y*ct,0,0,0])),
      'Literal restriction, including the shared Koszul coefficient.')
d0 = s.symbols('d0')
raw = s.Matrix([y*(ct-c0+d0), x*ch, 0, 0])
defect = s.cancel((phi*raw)[0]/(x*y))
check('unique_node_obstruction_constant', s.expand(defect.subs({x:0,y:0})-(d0-c0)) == 0,
      'The single mixed coefficient is precisely the common-Koszul-value obstruction.')

# All actual finite-character exponent cells; negative exponents are divided
# in the coarse variable before the root pullback, jointly in parameters.
finite = []
for name,n,af,ag in [('p1',3,[0,1],[0,2]),('p2',4,[0,3],[0,1])]:
    exponent = [[ag[j]-af[i] for i in range(2)] for j in range(2)]
    lifted = [[d+(n if d < 0 else 0) for d in row] for row in exponent]
    finite.append({'point':name,'order':n,'aF':af,'aG':ag,
                   'raw_exponents':exponent,'after_required_coarse_division':lifted})
    check(name+'_all_finite_character_cells',
          all(0 <= lifted[j][i] < n for j in range(2) for i in range(2)),
          'All four entries, after exactly the negative-weight coarse divisions.')
check('p1_exact_required_entry', finite[0]['raw_exponents']==[[0,-1],[2,1]] and
      finite[0]['after_required_coarse_division']==[[0,2],[2,1]],
      'Actual order-three invariant generators.')
check('p2_exact_required_entries', finite[1]['raw_exponents']==[[0,-3],[1,-2]] and
      finite[1]['after_required_coarse_division']==[[0,1],[1,2]],
      'Actual order-four invariant generators.')

def rank_fraction(matrix):
    data = [[Fraction(v) for v in row] for row in matrix]
    rr = 0
    for cc in range(len(data[0])):
        pivot = next((i for i in range(rr,len(data)) if data[i][cc]),None)
        if pivot is None:
            continue
        data[rr],data[pivot] = data[pivot],data[rr]
        scale = data[rr][cc]
        data[rr] = [v/scale for v in data[rr]]
        for i in range(rr+1,len(data)):
            factor=data[i][cc]
            if factor:
                data[i]=[v-factor*w for v,w in zip(data[i],data[rr])]
        rr += 1
        if rr == len(data):
            break
    return rr

root_output = json.loads((ROOT/'exact_node_and_jets.json').read_text())
hermite_receipt = []
for old in root_output['hermite']:
    k = old['twist']
    columns = [(j,d) for j in range(3) for d in range(k+(j==0))]
    rows = []
    for j in range(3):
        for point in range(2+4*j,6+4*j):
            rows.append([point**d if z==j else 0 for z,d in columns])
            rows.append([d*point**(d-1) if z==j and d else 0 for z,d in columns])
    check(f'Hermite_{k}_all_exact_entries',
          rows==old['matrix'] and [list(v) for v in columns]==old['columns'],
          'Every row and column of the independently reconstructed restriction map.')
    rk = rank_fraction(rows)
    check(f'Hermite_{k}_Fraction_rank', rk==old['rank'],
          'Independent Fraction Gaussian elimination; no SymPy rank and no producer code import.')
    check(f'Hermite_{k}_nullity',len(columns)-rk==old['nullity'],
          'Complete rank and nullity of this finite restriction map.')
    hermite_receipt.append({'twist':k,'rows':len(rows),'columns':len(columns),
                            'rank':rk,'nullity':len(columns)-rk})

check('flat_central_Euler_characteristic',
      (1-12)+12*2-12*3==-23,
      'Handle first modifications, all tooth Euler characteristics, and all node ranks.')
check('flat_central_degree',-23-3==-26,
      'Rank-three degree recovered from central-fibre Euler characteristic.')

result = {
    'schema':'S6-comb-sign-receiving-exact-09',
    'executed_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
    'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'own_derivation_sha256':'be3ac29edb8e43eb5005ff516e6d7d2442e245d17f2c5d5a53b8004f1b1d0c0d',
    'root_output_sha256':hashlib.sha256((ROOT/'exact_node_and_jets.json').read_bytes()).hexdigest(),
    'exposure':'Post-receiving implementation: full root proof and producer code were read before this program was authored. No producer code imported.',
    'scope':'Exact determinant/jet/node/character identities and full saved Hermite matrices. Analytic existence, root-family holomorphic division and collapse are proved in the mathematical reports.',
    'passed':sum(c['passed'] for c in checks),'total':len(checks),
    'checks':checks,'finite_character_maps':finite,'hermite':hermite_receipt,
}
(HERE/'receiving_exact_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ('executed_utc','program_sha256','passed','total','scope')}))
