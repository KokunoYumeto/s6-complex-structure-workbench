"""Fresh root certificate for the proposed comb proof.

Written after root's derivation freeze. No producer program or saved output is
imported. Symbolic identities and exact finite Hermite ranks only; this program
does not certify admissibility, analytic smoothing, or the root-family lift.
"""
from pathlib import Path
import datetime as dt
import hashlib
import json
import sympy as s

OUT = Path(__file__).resolve().parent
checks = []

def check(name, value, detail=None):
    ok = bool(value)
    checks.append(dict(name=name, passed=ok, detail=detail))
    assert ok, name

def mat_zero(M):
    return all(s.cancel(v) == 0 for v in M)

def pairing(T, eta):
    return sum(T[1, i]*eta[i, 0]-T[0, i]*eta[i, 1]
               for i in range(2))

y = s.symbols('y')
a,b,c,d = s.symbols('a b c d')
e,f,g,h = s.symbols('e f g h')
r0,r1,r2,r3 = s.symbols('r0 r1 r2 r3')
A = s.Matrix([[a,b],[c,d]])
B = s.Matrix([[e,f],[g,h]])
eta = s.Matrix([[r0,r1],[r2,r3]])
I = s.eye(2)
P = I+y*A
C = I+y*B*A*B.inv()
S = P.col_join(y*B)
q = (-y*B).row_join(C)
check('quotient_annihilates_conic_columns', mat_zero(q*S))
check('quotient_times_conic_derivative_equals_B', mat_zero(q*S.diff(y)-B))
check('quotient_frame_C_is_BPBinverse', mat_zero(C-B*P*B.inv()))
check('determinant_frame_transition', s.cancel(C.det()-P.det()) == 0)
Z = y*B*P.inv()
check('graph_quotient_transition', mat_zero(C*(-Z).row_join(I)-q))
check('graph_tautological_transition', mat_zero(I.col_join(Z)*P-S))
T = Z.diff(y)
check('actual_derivative_frame_transition', mat_zero(T-C.inv()*B*P.inv()))
eta_graph = P*eta*C.inv().T
check('determinant_valued_pairing_transition',
      s.cancel(pairing(T,eta_graph)-pairing(B,eta)/C.det()) == 0)
eta_prime = eta_graph.diff(y).subs(y,0)
check('actual_tensor_first_jet', mat_zero(eta_prime-(A*eta-eta*(B*A*B.inv()).T)))

# The pairing's nondegeneracy, with declared row/column ordering.
Tvars = s.Matrix([[a,b],[c,d]])
row = s.Matrix([[s.diff(pairing(Tvars,eta),v) for v in (r0,r1,r2,r3)]])
check('row_G_column_F_cup_row', row == s.Matrix([[c,-a,d,-b]]))
pair_matrix = s.Matrix([[s.diff(row[0,j],v) for v in (a,b,c,d)]
                       for j in range(4)])
check('pairing_perfect_integrally', abs(pair_matrix.det()) == 1)

# Retain arbitrary mixed graph and tensor jets, rather than setting them zero.
x = s.symbols('x')
Hs=s.symbols('H0:4'); Bs=s.symbols('B0:4')
Rs=s.symbols('R0:4'); Us=s.symbols('U0:4'); Vs=s.symbols('V0:4')
Es=s.symbols('E0:4'); Exs=s.symbols('Ex0:4'); Eys=s.symbols('Ey0:4')
H=s.Matrix(2,2,Hs); BB=s.Matrix(2,2,Bs)
R=s.Matrix(2,2,Rs); U=s.Matrix(2,2,Us); V=s.Matrix(2,2,Vs)
E=s.Matrix(2,2,Es); Ex=s.Matrix(2,2,Exs); Ey=s.Matrix(2,2,Eys)
Z2=x*H+y*BB+x*x*U+y*y*V+x*y*R
Theta=x*Z2.diff(x)-y*Z2.diff(y)
check('mixed_graph_coefficient_cancels',
      mat_zero(Theta.diff(x).diff(y).subs({x:0,y:0})))
mixed=s.expand(pairing(Theta,E+x*Ex+y*Ey)).coeff(x,1).coeff(y,1)
check('flat_kernel_mixed_coefficient',
      s.expand(mixed-(pairing(H,Ey)-pairing(BB,Ex))) == 0)
check('handle_value_coefficient',
      s.expand(pairing(Theta,E+x*Ex+y*Ey)).coeff(x,1).coeff(y,0)
      == pairing(H,E))
check('tooth_value_coefficient',
      s.expand(pairing(Theta,E+x*Ex+y*Ey)).coeff(x,0).coeff(y,1)
      == -pairing(BB,E))

# Local Koszul generator retains a common branch coefficient.
M=s.Matrix([[x,y,0,0]])
G=s.Matrix([[-y,0,0],[x,0,0],[0,1,0],[0,0,1]])
check('node_free_generators_annihilated', M*G == s.zeros(1,3))
check('handle_negative_modification', G.subs(y,0) ==
      s.Matrix([[0,0,0],[x,0,0],[0,1,0],[0,0,1]]))
check('tooth_negative_modification', G.subs(x,0) ==
      s.Matrix([[-y,0,0],[0,0,0],[0,1,0],[0,0,1]]))

# Diagonal transport by the actual invertible H; H=I only after that map.
beta1,beta2,u,v,p,qv,rv,sv=s.symbols('beta1 beta2 u v p q r ss', nonzero=True)
BD=s.diag(beta1,beta2)
AD=s.Matrix([[p,qv],[rv,sv]])
ED=s.diag(u,v)
check('diagonal_value_pairing_H',pairing(I,ED)==0)
check('diagonal_value_pairing_B',pairing(BD,ED)==0)
psi=s.factor(pairing(I,AD*ED-ED*(BD*AD*BD.inv()).T))
expected=rv*(1+beta2/beta1)*u-qv*(1+beta1/beta2)*v
check('full_second_jet_covector',s.cancel(psi-expected)==0)
coeff=s.Matrix([[s.diff(s.diff(psi,z),w) for w in (rv,qv)]
                for z in (u,v)])
expected_det=-(beta1+beta2)**2/(beta1*beta2)
check('second_jet_surjective_on_declared_open',
      s.cancel(coeff.det()-expected_det)==0)
check('scalar_A_parameter_has_zero_jet',
      pairing(I,p*I*ED-ED*(BD*(p*I)*BD.inv()).T)==0)

# Three literal products defining the split-coordinate witness.
t=s.symbols('t')
node_groups=[list(range(2,6)),list(range(6,10)),list(range(10,14))]
products=[s.prod((t-n)**2 for n in group) for group in node_groups]
for j,poly in enumerate(products):
    check(f'component_{j}_product_degree_eight',s.degree(poly,t)==8)
    for n in node_groups[j]:
        check(f'component_{j}_double_root_{n}',
              poly.subs(t,n)==0 and s.diff(poly,t).subs(t,n)==0)

def hermite(k):
    degs=[k,k-1,k-1]
    columns=[(component,power) for component,deg in enumerate(degs)
             for power in range(deg+1)]
    rows=[]
    for component,group in enumerate(node_groups):
        for n in group:
            for derivative in (False,True):
                rows.append([
                    (0 if j != component else
                     (power*n**(power-1) if power else 0)
                     if derivative else n**power)
                    for j,power in columns])
    return columns,s.Matrix(rows)

hermite_data=[]
for k,expected_dim,expected_rank,expected_nullity in [(7,22,22,0),(8,25,24,1),(9,28,24,4)]:
    columns,Herm=hermite(k)
    rank=Herm.rank()
    check(f'Hermite_twist_{k}_shape',Herm.shape==(24,expected_dim))
    check(f'Hermite_twist_{k}_rank',rank==expected_rank)
    check(f'Hermite_twist_{k}_nullity',Herm.cols-rank==expected_nullity)
    hermite_data.append(dict(twist=k,columns=columns,
                             matrix=[[int(v) for v in row] for row in Herm.tolist()],
                             rank=rank,nullity=Herm.cols-rank))

# Check the unique twist-eight section through the exact restriction matrix.
columns,Herm=hermite(8)
vector=s.Matrix([s.expand(products[j]).coeff(t,power) if j==0 else 0
                 for j,power in columns])
check('twist_eight_literal_section_in_kernel',Herm*vector==s.zeros(24,1))
check('twist_eight_literal_section_nonzero',vector!=s.zeros(Herm.cols,1))
check('total_degree_of_twelve_modifications',-2-12*2==-26)
check('Euler_characteristic_twist_eight',-26+3*8+3==1)
check('Hodge_11_for_m12_h0zero',4*12+1==49)
check('Hodge_12_for_m12_h0zero',4*12==48)

result=dict(
    schema='S6-series-grind-exact-comb-node-and-jets-09',
    executed_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
    program_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    derivation_freeze_sha256='4a3cfbc0e5548c28e7246034bd3822241c4a03482b160fc838e67629e733a9d7',
    scope='Fresh exact symbolic identities and finite Hermite matrices only; no analytic/root-lift certification.',
    checks=checks,passed=sum(x['passed'] for x in checks),total=len(checks),
    jet_covector=str(psi),jet_jacobian_determinant=str(s.factor(coeff.det())),
    node_groups=node_groups,coordinate_products=[str(s.expand(v)) for v in products],
    hermite=hermite_data)
(OUT/'exact_node_and_jets.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['executed_utc','program_sha256','passed','total','scope']}))
