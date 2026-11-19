#!/usr/bin/env python3
"""Post-comparison exact maps from the printed complex to the preread quotient.

This uses only the statement packet and our newly written Euclidean
kernel routine. No prior producing program or exported matrices are read.
"""
from pathlib import Path
from itertools import combinations
import ast,json,re
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
P=Path(__file__).resolve().parents[2]
source=(Path(__file__).with_name('P1A4_integral_fresh.py')).read_text()
tree=ast.parse(source)
fn=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='integer_kernel')
exec(compile(ast.Module(body=[fn],type_ignores=[]),'<our fresh Euclidean kernel>','exec'))
packet=(P/'analysis/continuation_V/P1A4_statement_input_packet.md').read_text()
data=json.loads(re.search(r'```json\n(.*?)\n```',packet,re.S).group(1))
A=s.Matrix(data['M1']);B=s.Matrix(data['M2']);I=s.eye(6);M0=(A*B).inv();N=M0-I
N1=sum((A**k for k in range(5)),s.zeros(6))
N2=sum((B**k for k in range(4)),s.zeros(6))
L1=integer_kernel(N1);L2=integer_kernel(N2)
L0=integer_kernel(integer_kernel(N.T).T)
def coordinates(basis,v):
    z=basis.gauss_jordan_solve(v)[0]
    assert all(x.q==1 for x in z) and basis*z==v
    return z
C1=coordinates(L1,A-I);C2=coordinates(L2,B-I);C0=coordinates(L0,N)
assert [abs(int(smith_normal_form(C0,domain=s.ZZ)[i,i])) for i in range(3)]==[1,1,1]
D1=L1.row_join(A*L2).row_join(A*B*L0)
D0=C1.col_join(C2).col_join(C0)
assert D1.shape==(6,11) and D0.shape==(11,6)
assert D1*D0==s.zeros(6)
cycles=integer_kernel(D1);coboundary=coordinates(cycles,D0)
assert cycles.cols==6
smith=[abs(int(smith_normal_form(coboundary,domain=s.ZZ)[i,i])) for i in range(6)]
assert smith==[1,1,1,1,1,2]
K=integer_kernel(N1.col_join(N2));T=integer_kernel(A*B-I)
Z=coordinates(K,(B-I)*T)

# An integral right inverse of C0 records a primitive cusp-period preimage.
right=None
for cols in combinations(range(6),3):
    minor=C0[:,cols]
    if abs(minor.det())==1:
        right=s.zeros(6,3)
        inv=minor.inv()
        for i,col in enumerate(cols):right[col,:]=inv[i,:]
        break
assert right is not None and C0*right==s.eye(3)

# Map a three-meridian cycle (x1,x2,x0) to y=x2-(B-I)lambda,
# where x0=N*lambda. This is exactly the prereading elimination.
Y=coordinates(K,L2*cycles[4:8,:]-(B-I)*right*cycles[8:11,:])
# The inverse sends y to (-A*y,y,0).
inclusion=coordinates(L1,-A*K).col_join(coordinates(L2,K)).col_join(s.zeros(3))
X=coordinates(cycles,inclusion)
assert Y*X==s.eye(3)
H=coboundary.inv()*(s.eye(6)-X*Y)
assert all(x.q==1 for x in H) and coboundary*H==s.eye(6)-X*Y
R=Z.inv()*Y*coboundary
assert all(x.q==1 for x in R) and Z*R==Y*coboundary
def rows(M):return [[str(v) for v in row] for row in M.tolist()]
out={'status':'PASS','chronology':'Written after printed proof comparison; no prior producing code or exports read',
 'L1':rows(L1),'L2':rows(L2),'L0':rows(L0),'D1':rows(D1),'D0':rows(D0),
 'D1D0':'zero','cycle_basis':rows(cycles),'coboundary_coordinates':rows(coboundary),
 'smith_factors':smith,'cusp_period_preimage':rows(right),
 'map_to_prereading_quotient':rows(Y),'map_from_prereading_quotient':rows(X),
 'homotopy_coboundary_matrix':rows(H),'boundary_map_coordinates':rows(R),
 'identities':['Y*X=I3','I6-X*Y=coboundary*H','Y*coboundary=Z*R'],
 'conclusion':'The printed11-generator cochain quotient and the prereading3-generator quotient are explicitly isomorphic, both Z/2.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['status','chronology','smith_factors','identities','conclusion']},indent=2))
