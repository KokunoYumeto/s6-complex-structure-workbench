"""Exact local-system algebra for the fixed-circle surgery, B.6.16.

The four local monodromies are A1,A2,C1,C2 with product one.  A central
parameter shear S=I-2E acts on the constructible local systems.  This
script computes its induced action on H1(P1,j_* exterior^q V), using
parabolic cocycles, rather than inferring an action from dimensions.
The smooth geometric realization is proved separately in B.6.16.
The computation does not determine the extension between its two H3
Leray grades, hence does not evaluate its integral shear.
"""
from pathlib import Path
from itertools import combinations
import json
import sympy as s

A1=s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
E=s.zeros(4); E[3,0]=1
C1=s.eye(4); C1[2,1]=1; C1[2,0]=-1
C2=s.eye(4); C2[2,0]=1; C2[3,0]=-1
assert A1*A2*C1*C2==s.eye(4)
S=s.eye(4)-2*E
assert all(S*A==A*S for A in [A1,A2,C1,C2])
g,u,w,d=[s.eye(4)[:,i] for i in range(4)]
a1,a2,b1,b2=w,w-d,u,g+u
B=s.Matrix.hstack(a1,a2,b1,b2)
assert abs(B.det())==1
assert (C1-s.eye(4))*b1==a1
assert (C1-s.eye(4))*b2==s.zeros(4,1)
assert (C2-s.eye(4))*b2==a2
assert (C2-s.eye(4))*b1==s.zeros(4,1)
assert (S-s.eye(4))*b2==-2*a1+2*a2
assert (S-s.eye(4))*b1==s.zeros(4,1)

def exterior(A,q):
    inds=list(combinations(range(A.rows),q))
    return s.Matrix([[A.extract(i,j).det() for j in inds] for i in inds])

def columns(A):
    return s.Matrix.hstack(*A.columnspace()) if A.rank() else s.zeros(A.rows,0)

def kernel(A):
    return s.Matrix.hstack(*A.nullspace()) if len(A.nullspace()) else s.zeros(A.cols,0)

def coords(B,A):
    if B.cols==0:
        assert A==s.zeros(B.rows,A.cols)
        return s.zeros(0,A.cols)
    ans=B.gauss_jordan_solve(A)[0]
    assert not any(x.free_symbols for x in ans)
    assert B*ans==A
    return ans

data={'basis_columns_a1_a2_b1_b2':B.tolist(),
      'local_matrices':[A.tolist() for A in [A1,A2,C1,C2]],
      'parameter_matrix':S.tolist(),
      'critical_elliptic_return_matrices':[[[1,2],[0,1]],[[1,0],[0,1]]],
      'degrees':{}}
for q in range(5):
    # Use cohomology, so the original homology matrices are inverse transposed.
    mats=[exterior(A.inv().T,q) for A in [A1,A2,C1,C2]]
    T=exterior(S.inv().T,q)
    rank=mats[0].rows
    images=[columns(A-s.eye(rank)) for A in mats]
    sizes=[B.cols for B in images]
    pieces=[]; prefix=s.eye(rank)
    for A,B in zip(mats,images):
        pieces.append(prefix*B); prefix=prefix*A
    assert prefix==s.eye(rank)
    D1=s.Matrix.hstack(*pieces)
    D0=s.Matrix.vstack(*[coords(B,A-s.eye(rank)) for A,B in zip(mats,images)])
    assert D1*D0==s.zeros(rank,rank)
    K=kernel(D1); I=columns(D0)
    basis=I
    complement=[]
    for v in K.columnspace():
        if basis.row_join(v).rank()>basis.cols:
            basis=basis.row_join(v); complement.append(v)
    assert basis.cols==K.cols
    block=s.diag(*[coords(B,T*B) for B in images])
    restriction=coords(basis,block*basis)
    answer=restriction[I.cols:,I.cols:]
    assert restriction[I.cols:,:I.cols]==s.zeros(len(complement),I.cols)
    invariants=kernel(s.Matrix.vstack(*[A-s.eye(rank) for A in mats]))
    coin_image=columns(s.Matrix.hstack(*[A-s.eye(rank) for A in mats]))
    coin_basis=coin_image
    for v in s.eye(rank).columnspace():
        if coin_basis.row_join(v).rank()>coin_basis.cols:
            coin_basis=coin_basis.row_join(v)
    coin_action=coords(coin_basis,T*coin_basis)[coin_image.cols:,coin_image.cols:]
    assert coin_action==s.eye(rank-coin_image.cols)
    data['degrees'][q]={
        'rank_local_system':rank,
        'ranks_local_monodromy_minus_identity':sizes,
        'dim_global_invariants':invariants.cols,
        'dim_global_coinvariants':rank-coin_image.cols,
        'parameter_action_on_global_coinvariants':coin_action.tolist(),
        'dim_parabolic_H1':len(complement),
        'parameter_action_on_parabolic_H1':[[str(x) for x in row] for row in answer.tolist()],
        'parameter_action_on_global_invariants':[[str(x) for x in row] for row in coords(invariants,T*invariants).tolist()],
    }
    if q==2 and complement:
        reps=s.Matrix.hstack(*complement)
        actual=s.diag(*images)*reps
        data['degrees'][q]['cohomology_exterior_basis']=['g_u','g_w','g_d','u_w','u_d','w_d']
        data['degrees'][q]['parabolic_cocycle_representatives_by_meridian']=[
            [[str(x) for x in row] for row in actual[6*i:6*(i+1),:].tolist()]
            for i in range(4)]

out=json.dumps(data,indent=2,default=str)+'\n'
print(out,end='')
Path(__file__).with_suffix('.out.json').write_text(out)
