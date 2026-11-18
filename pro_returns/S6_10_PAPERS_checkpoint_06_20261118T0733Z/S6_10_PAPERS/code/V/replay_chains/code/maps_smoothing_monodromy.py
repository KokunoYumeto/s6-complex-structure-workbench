"""Exact rational parabolic cohomology for the separated rank-one cusps.

The four local monodromies are A1,A2,Cw,Cd with product one.  A central
parameter shear S=I-2E acts on the constructible local systems.  This
script computes its induced action on H1(P1,j_* exterior^q V), using
parabolic cocycles, rather than inferring an action from dimensions.
The passage from these groups to a particular family's total H3 is a
separate geometric assertion and is not built into the computation.
"""
from pathlib import Path
from itertools import combinations
import json
import sympy as s

A1=s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
E=s.zeros(4); E[3,0]=1
Cw=s.eye(4); Cw[2,1]=1
Cd=s.eye(4)-E
assert A1*A2*Cw*Cd==s.eye(4)
S=s.eye(4)-2*E
assert all(S*A==A*S for A in [A1,A2,Cw,Cd])

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

data={}
for q in range(5):
    # Use cohomology, so the original homology matrices are inverse transposed.
    mats=[exterior(A.inv().T,q) for A in [A1,A2,Cw,Cd]]
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
    data[q]={
        'rank_local_system':rank,
        'ranks_local_monodromy_minus_identity':sizes,
        'dim_global_invariants':invariants.cols,
        'dim_parabolic_H1':len(complement),
        'parameter_action_on_parabolic_H1':[[str(x) for x in row] for row in answer.tolist()],
        'parameter_action_on_global_invariants':[[str(x) for x in row] for row in coords(invariants,T*invariants).tolist()],
    }
    if q==2:
        assert len(complement)==2
        assert answer==s.eye(2)
        reps=s.Matrix.hstack(*complement)
        differences=(block-s.eye(block.rows))*reps
        coboundary,parameters=D0.gauss_jordan_solve(differences)
        coboundary=coboundary.subs({z:0 for z in parameters})
        assert D0*coboundary==differences
        actual=s.diag(*images)*reps
        data[q]['cohomology_exterior_basis']=['g_u','g_w','g_d','u_w','u_d','w_d']
        data[q]['parabolic_cocycle_representatives_by_meridian']=[
            [[str(x) for x in row] for row in actual[6*i:6*(i+1),:].tolist()]
            for i in range(4)]
        data[q]['parameter_difference_is_coboundary_of']=[
            [str(x) for x in row] for row in coboundary.tolist()]

out=json.dumps(data,indent=2)+'\n'
print(out,end='')
Path(__file__).with_suffix('.out.json').write_text(out)
