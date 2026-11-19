"""Recompute the parabolic lattice complex by new Smith-basis linear algebra.

Only the marked input matrices are reused as mathematical data. No old program,
basis, chain differential, or output matrix is imported. Independent exact Smith
decompositions produce primitive kernels and the integral quotient.
"""
from pathlib import Path
import json
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from sympy.matrices.normalforms import hermite_normal_form,smith_normal_form

BASE=Path('/workspace/scratch/ae06852560d6')
inp=BASE/'materials/S6_08_PAPERS_2_returns_code/returns/S6_04_MAPS_MANIFOLDS/records/fourfolds_marked_survivor_input.json'
d=json.loads(inp.read_text());M1,M2=map(s.Matrix,d['matrices']);I=s.eye(6);M0=(M1*M2).inv();N=M0-I
def smith_with_bases(A):
    D,U,V=smith_normal_decomp(DomainMatrix.from_Matrix(A).convert_to(s.ZZ))
    D,U,V=map(lambda a:a.to_Matrix(),(D,U,V))
    assert U*A*V==D and abs(U.det())==1 and abs(V.det())==1
    return D,U,V
def kernel(A):
    D,U,V=smith_with_bases(A)
    rank=sum(D[i,i]!=0 for i in range(min(D.shape)))
    K=V[:,rank:]
    assert A*K==s.zeros(A.rows,K.cols)
    return K
def coord(L,A):
    R=L.gauss_jordan_solve(A)[0]
    assert all(a.q==1 for a in R) and L*R==A
    return R
L1=kernel(sum((M1**j for j in range(5)),s.zeros(6)))
L2=kernel(sum((M2**j for j in range(4)),s.zeros(6)))
L0=hermite_normal_form(N)
D1=L1.row_join(M1*L2).row_join(M1*M2*L0)
D0=coord(L1,M1-I).col_join(coord(L2,M2-I)).col_join(coord(L0,M0-I))
assert D1.shape==(6,11) and D0.shape==(11,6) and D1*D0==s.zeros(6)
K=kernel(D1);R=coord(K,D0);F=smith_normal_form(R,domain=s.ZZ)
diag=[abs(int(F[i,i])) for i in range(min(F.shape)) if F[i,i]]
H1={'free_rank':K.cols-len(diag),'torsion':[x for x in diag if x>1],'smith':diag}
assert H1['free_rank']==0 and H1['torsion']==[2]

tau=s.Matrix([0,1,1,1,1,1])/2
assert all(v.q==1 for M in [M1,M2,M0] for v in M*tau-tau)
# Exact integer solution to N*lambda=N*tau, obtained from Smith basis.
D,U,V=smith_with_bases(N);rhs=U*N*tau
z=s.zeros(6,1)
for i in range(3):z[i]=rhs[i]/D[i,i]
assert all(v.q==1 for v in z)
lam=V*z;assert N*lam==N*tau and all(v.q==1 for v in lam)
bounded=tau-lam;assert N*bounded==s.zeros(6,1)
S=s.Matrix(d['cusp_marking']);canonical=I.copy()
canonical[:3,3:]=s.eye(3)
assert abs(S.det())==1 and S.inv()*M0*S==canonical

def mat(A):return [[str(A[i,j]) for j in range(A.cols)] for i in range(A.rows)]
out={'method':'new primitive kernels via unimodular Smith decompositions; exact parabolic cocycle quotient',
     'L1':mat(L1),'L2':mat(L2),'L0':mat(L0),'D1':mat(D1),'D0':mat(D0),
     'kernel_D1':mat(K),'D0_in_kernel_coordinates':mat(R),'H1':H1,
     'half_period':mat(tau),'integer_period_to_subtract':mat(lam),'bounded_half_period':mat(bounded),
     'marking_determinant':int(S.det()),'cusp_normal_form':mat(canonical)}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
print(json.dumps({'status':'passed','H1':H1,'D1_shape':D1.shape,'D0_shape':D0.shape,
  'bounded_half_period':mat(bounded)},indent=2))
