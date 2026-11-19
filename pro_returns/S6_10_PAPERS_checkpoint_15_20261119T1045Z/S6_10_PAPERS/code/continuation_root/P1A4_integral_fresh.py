#!/usr/bin/env python3
"""P1A.4: independently derived commutant and parabolic lattice quotient.

Only the clean statement/construction packet is read. No target proof or
previous producing computation is imported.
"""
from pathlib import Path
from itertools import combinations
import json,re
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

P=Path(__file__).resolve().parents[2]
packet=(P/'analysis/continuation_V/P1A4_statement_input_packet.md').read_text()
data=json.loads(re.search(r'```json\n(.*?)\n```',packet,re.S).group(1))
A=s.Matrix(data['M1']);B=s.Matrix(data['M2']);I=s.eye(6)
assert A**5==I and B**4==I

def integer_kernel(mat):
    """Primitive integer kernel by explicit unimodular row Euclidean steps."""
    H=mat.T.copy();T=s.eye(H.rows);row=0
    for col in range(H.cols):
        hits=[i for i in range(row,H.rows) if H[i,col]]
        if not hits:continue
        i=hits[0];H.row_swap(row,i);T.row_swap(row,i)
        for i in range(row+1,H.rows):
            while H[i,col]:
                quotient=H[row,col]//H[i,col]
                H[row,:]=H[row,:]-quotient*H[i,:]
                T[row,:]=T[row,:]-quotient*T[i,:]
                H.row_swap(row,i);T.row_swap(row,i)
        if H[row,col]<0:
            H[row,:]=-H[row,:];T[row,:]=-T[row,:]
        row+=1
        if row==H.rows:break
    assert H==T*mat.T and abs(T.det())==1
    assert all(H[i,j]==0 for i in range(row,H.rows) for j in range(H.cols))
    K=T[row:,:].T
    assert mat*K==s.zeros(mat.rows,K.cols)
    assert K.cols==mat.cols-mat.rank()
    return K

# Direct linear equations for all36 entries of a commuting endomorphism.
variables=s.symbols('x:36');X=s.Matrix(6,6,variables)
equations=list(X*A-A*X)+list(X*B-B*X)
comm,_=s.linear_eq_to_matrix(equations,variables)
null=comm.nullspace()
assert len(null)==1
C=s.Matrix(6,6,list(null[0]));assert C==C[0,0]*I and C[0,0]!=0

# Alternating bilinear forms are cohomology classes; no invariant form survives.
pairs=list(combinations(range(6),2));u=s.symbols('u:15');J=s.zeros(6)
for x,(i,j) in zip(u,pairs):J[i,j]=x;J[j,i]=-x
inv,_=s.linear_eq_to_matrix(list(A.T*J*A-J)+list(B.T*J*B-J),u)
assert inv.rank()==15

N1=sum((A**k for k in range(5)),s.zeros(6))
N2=sum((B**k for k in range(4)),s.zeros(6))
K=integer_kernel(N1.col_join(N2))
T=integer_kernel(A*B-I)
image=(B-I)*T
# Every image vector is in the cocycle kernel, by the defining equations.
assert N1*image==s.zeros(6,image.cols) and N2*image==s.zeros(6,image.cols)
Z=K.gauss_jordan_solve(image)[0]
assert all(v.q==1 for v in Z) and K*Z==image
D=smith_normal_form(Z,domain=s.ZZ)
smith=[abs(int(D[i,i])) for i in range(min(D.shape))]
assert K.cols==T.cols==3 and smith==[1,1,2]
assert integer_kernel((A-I).col_join(B-I)).cols==0

# Finite affine root actions obstruct the linear part -I.
ell=s.Matrix([data['ell']]);v1=s.Matrix(data['v1']);v2=s.Matrix(data['v2'])
assert ell*A==ell and ell*B==ell
obstructions=[s.Rational(2*int((ell*v1)[0]),5),s.Rational(2*int((ell*v2)[0]),4)]
assert all(q.q!=1 for q in obstructions)

def rows(M):return [[str(v) for v in row] for row in M.tolist()]
out={
 'status':'PASS','target_proof_and_producing_code_read':False,
 'method':'Explicit unimodular Euclidean kernel bases, direct36-variable commutator equations, and15-variable alternating-form equations',
 'rational_commutant_dimension':len(null),'commutant_basis':rows(C),
 'alternating_invariant_dimension':15-inv.rank(),
 'cocycle_kernel_basis_K':rows(K),'cusp_invariant_basis_T':rows(T),
 'coboundary_coordinate_matrix':rows(Z),'smith_factors':smith,
 'global_invariant_lattice_rank':0,
 'minus_identity_affine_obstructions':[str(x) for x in obstructions],
 'parabolic_quotient':'Z/2',
 'scope':'The exact group-cohomology presentation and analytic translation stalks are justified separately in the prereading derivation.'
}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
