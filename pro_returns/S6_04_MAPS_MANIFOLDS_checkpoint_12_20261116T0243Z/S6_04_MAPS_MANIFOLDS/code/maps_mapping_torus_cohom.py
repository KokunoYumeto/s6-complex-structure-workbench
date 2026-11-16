"""Exploratory rational local-system algebra for the smoothing mapping torus.

The regular five-dimensional fibre is the nilmanifold with bracket
[k,g]=-2d. Base monodromies include the exact finite affine defects.
This is an algebraic computation, not by itself a computation of the
global constructible direct images at the singular fibres.
"""
from pathlib import Path
from itertools import combinations
import json
import sympy as s

A1=s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
E=s.zeros(4);E[3,0]=1
Cw=s.eye(4);Cw[2,1]=1
Cd=s.eye(4)-E
S=s.eye(4)-2*E
g=s.eye(4)[:,0]
v1=s.Matrix([1,2,-4,0]);v2=s.Matrix([-1,-3,3,0])
d1=(S-s.eye(4))*v1/3-s.Rational(1,6)*(s.eye(4)-A1)*g
d2=(S-s.eye(4))*v2/4-s.Rational(1,6)*(s.eye(4)-A2)*g
assert list(d1)==[0,1,-1,-1] and list(d2)==[0,0,-1,1]
assert d1+A1*d2==s.zeros(4,1)

def lift(A,defect):
    return A.row_join(-defect).col_join(s.Matrix([[0,0,0,0,1]]))

mon=[lift(A1,d1),lift(A2,d2),lift(Cw,s.zeros(4,1)),lift(Cd,s.zeros(4,1))]
assert mon[0]*mon[1]*mon[2]*mon[3]==s.eye(5)
inds={q:list(combinations(range(5),q)) for q in range(6)}

def wedge_sign(seq):
    if len(set(seq))<len(seq): return None,0
    sign=(-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
    return tuple(sorted(seq)),sign

def diff(q):
    ans=s.zeros(len(inds.get(q+1,[])),len(inds[q]))
    if q==5:return ans
    for col,seq in enumerate(inds[q]):
        if 3 not in seq:continue
        i=seq.index(3)
        target,sign=wedge_sign(seq[:i]+(4,0)+seq[i+1:])
        if sign:ans[inds[q+1].index(target),col]=2*(-1)**i*sign
    return ans

def columns(M):
    return s.Matrix.hstack(*M.columnspace()) if M.rank() else s.zeros(M.rows,0)

def kernel(M):
    return s.Matrix.hstack(*M.nullspace()) if len(M.nullspace()) else s.zeros(M.cols,0)

def coords(B,A):
    if B.cols==0:
        assert A==s.zeros(B.rows,A.cols);return s.zeros(0,A.cols)
    ans=B.gauss_jordan_solve(A)[0]
    assert not any(t.free_symbols for t in ans)
    assert B*ans==A
    return ans

def exterior(A,q):
    return s.Matrix([[A.extract(i,j).det() for j in inds[q]] for i in inds[q]])

def quotient(K,I):
    basis=columns(I);image_rank=basis.cols
    reps=[]
    for v in K.columnspace():
        if basis.row_join(v).rank()>basis.cols:
            basis=basis.row_join(v);reps.append(v)
    return basis,image_rank,(s.Matrix.hstack(*reps) if reps else s.zeros(K.rows,0))

cohom={}
data={'finite_defects':[list(d1),list(d2)],'degrees':{}}
for q in range(6):
    D=diff(q); prev=diff(q-1) if q else s.zeros(1,0)
    if q:assert D*prev==s.zeros(D.rows,prev.cols)
    K=kernel(D);base,imrank,reps=quotient(K,prev)
    actions=[]
    for A in mon:
        T=exterior(A.inv().T,q)
        assert D*T==exterior(A.inv().T,q+1)*D if q<5 else True
        block=coords(base,T*base)
        assert block[imrank:,:imrank]==s.zeros(reps.cols,imrank)
        actions.append(block[imrank:,imrank:])
    cohom[q]=(reps,actions)
    images=[columns(A-s.eye(reps.cols)) for A in actions]
    prefix=s.eye(reps.cols);blocks=[]
    for A,B in zip(actions,images):blocks.append(prefix*B);prefix=prefix*A
    assert prefix==s.eye(reps.cols)
    rel=s.Matrix.hstack(*blocks)
    cob=s.Matrix.vstack(*[coords(B,A-s.eye(reps.cols)) for A,B in zip(actions,images)])
    assert rel*cob==s.zeros(reps.cols,reps.cols)
    invariant=kernel(s.Matrix.vstack(*[A-s.eye(reps.cols) for A in actions]))
    data['degrees'][q]={
        'betti_regular_nil_fibre':reps.cols,
        'local_action_ranks':[B.cols for B in images],
        'global_invariants':invariant.cols,
        'parabolic_H1':rel.cols-rel.rank()-cob.rank(),
        'invariant_forms':[[str(t) for t in row] for row in (reps*invariant).tolist()],
        'exterior_basis':[','.join('guwdk'[i] for i in seq) for seq in inds[q]],
    }
    if q==2:
        missing=inds[q].index((3,4))
        data['degrees'][q]['global_invariant_delta_k_coefficients']=[str(t) for t in (reps*invariant)[missing,:]]
        coin_image=columns(s.Matrix.hstack(*[A-s.eye(reps.cols) for A in actions]))
        checks={}
        for pair in [(0,1),(0,2)]:
            form=s.zeros(len(inds[q]),1);form[inds[q].index(pair),0]=1
            vec=coords(base,form)[imrank:,:]
            checks[','.join('guwdk'[i] for i in pair)]=coin_image.row_join(vec).rank()==coin_image.cols
        data['degrees'][q]['gamma_u_gamma_w_vanish_in_global_coinvariants']=checks
    if q==3:
        ix_s=inds[q].index((1,2,4))
        ix_inf=inds[q].index((0,3,4))
        data['degrees'][q]['critical_trace_evaluations']={
            'new_zero_u_w_k':[str(t) for t in (reps*invariant)[ix_s,:]],
            'infinity_g_d_k':[str(t) for t in (reps*invariant)[ix_inf,:]]}

out=json.dumps(data,indent=2,default=str)+'\n'
print(out,end='')
Path(__file__).with_suffix('.out.json').write_text(out)
