#!/usr/bin/env python3
"""Fresh integral lattice/affine construction from the clean F2.13 packet.

No old proof, lattice/vector choices or producing code has been read.
The finite search constructs explicit invariant overlattices; subsequent
identities will certify the chosen lattices independently of enumeration.
"""
from pathlib import Path
from itertools import product
from functools import reduce
from math import gcd,lcm
import re,json
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form,smith_normal_form

packet=Path('analysis/continuation_V/F2_13_nonvacuity_statement_packet.md').read_text()
models=[json.loads(x) for x in re.findall(r'```json\n(.*?)\n```',packet,re.S)]

def span(vectors):
    piv={}
    for x in vectors:
        while x:
            i=x.bit_length()-1
            if i in piv:x^=piv[i]
            else:
                piv[i]=x
                break
    for i in sorted(piv):
        for j in sorted(piv):
            if j>i and (piv[j]>>i)&1:piv[j]^=piv[i]
    return tuple(piv[i] for i in sorted(piv,reverse=True))
def contains(W,x):return span(W+(x,))==W
def act(M,x):
    return sum((sum(int(M[i,j])*((x>>j)&1) for j in range(6))%2)<<i for i in range(6))
def stable_closure(Ms,W):
    W=span(tuple(W))
    while True:
        new=span(W+tuple(act(M,x) for M in Ms for x in W))
        if new==W:return W
        W=new
def primitive_vector(v):
    d=lcm(*(int(x.q) for x in v));z=[int(d*x) for x in v]
    g=reduce(gcd,z);z=[x//g for x in z]
    if next(x for x in z if x)!=abs(next(x for x in z if x)):z=[-x for x in z]
    return s.Matrix(z)
def integral_fixed(M,ell,value):
    D=(M-s.eye(6)).col_join(ell);rhs=s.zeros(7,1);rhs[6]=value
    R,piv=D.row_join(rhs).rref()
    if 6 in piv:return None
    free=[j for j in range(6) if j not in piv]
    denominator=lcm(*(int(x.q) for x in R))
    if denominator**len(free)>100000:return None
    for values in product(range(denominator),repeat=len(free)):
        ans=s.zeros(6,1)
        for j,x in zip(free,values):ans[j]=x
        for i,j in enumerate(piv):ans[j]=R[i,6]-sum(R[i,f]*ans[f] for f in free)
        if all(x.q==1 for x in ans):return ans
    return None

out=[]
for case,model in zip(('A','B'),models):
    A=s.Matrix(model['A']);B=s.Matrix(model['B']);I=s.eye(6)
    start=stable_closure((A,B),(1,));todo=[start];seen={start};found=[]
    while todo:
        W=todo.pop(0)
        columns=[s.Matrix([((x>>i)&1) for i in range(6)]) for x in W]
        H=hermite_normal_form((2*I).row_join(s.Matrix.hstack(*columns)))
        L=H/2;At=L.inv()*A*L;Bt=L.inv()*B*L
        assert all(x.q==1 for M in (At,Bt) for x in M)
        K=Bt*At-I;smith=smith_normal_form(K,domain=s.ZZ)
        diag=[abs(int(smith[i,i])) for i in range(6) if smith[i,i]]
        J=(At.T-I).row_join(Bt.T-I);sj=smith_normal_form(J,domain=s.ZZ)
        dj=[abs(int(sj[i,i])) for i in range(6) if sj[i,i]]
        fixed=(At-I).col_join(Bt-I).nullspace()
        if diag==[1,1,1] and dj==[1,1,1,1,1] and len(fixed)==1:
            ell=primitive_vector(fixed[0]).T
            v1=integral_fixed(At.T,ell,1);v2=integral_fixed(Bt.T,ell,-1)
            if v1 is not None and v2 is not None:
                found.append({'case':case,'mod2_subspace':W,'L':L.tolist(),'A':At.tolist(),'B':Bt.tolist(),'ell':list(ell),'v1':list(v1),'v2':list(v2),'cusp_smith':diag,'coinvariant_smith':dj,'index':str(1/L.det())})
                break
        for x in range(1,64):
            if contains(W,x):continue
            new=stable_closure((A,B),W+(x,))
            if new not in seen:seen.add(new);todo.append(new)
    print(case,'invariant subspaces seen',len(seen),'found',len(found),flush=True)
    if found:out.extend(found)
    else:out.append({'case':case,'status':'not found in invariant half-overlattices containing e0'})

def cv(x):
    if isinstance(x,s.Rational):return str(x)
    raise TypeError(type(x))
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2,default=cv)+'\n')
print(json.dumps(out,indent=2,default=cv))
