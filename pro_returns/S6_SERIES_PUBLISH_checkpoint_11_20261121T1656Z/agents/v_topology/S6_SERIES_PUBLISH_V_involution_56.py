#!/usr/bin/env python3
"""Independent complete binary-similarity enumeration of the 56 cusp pairs."""
from itertools import product
from math import gcd,lcm
import json
from datetime import datetime,timezone
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp


def mat_from_code(code,n):return tuple((code>>(n*i))&((1<<n)-1) for i in range(n))
def code_from_mat(M,n):return sum(row<<(n*i) for i,row in enumerate(M))
def product2(A,B,n):
    cols=[sum(((B[i]>>j)&1)<<i for i in range(n)) for j in range(n)]
    return tuple(sum(((row&cols[j]).bit_count()%2)<<j for j in range(n)) for row in A)
def inverse2(A,n):
    aug=[A[i]|(1<<(n+i)) for i in range(n)]
    for j in range(n):
        p=next((i for i in range(j,n) if (aug[i]>>j)&1),None)
        if p is None:return None
        aug[j],aug[p]=aug[p],aug[j]
        for i in range(n):
            if i!=j and ((aug[i]>>j)&1):aug[i]^=aug[j]
    return tuple(row>>n for row in aug)
def plain(M,n):return [[(M[i]>>j)&1 for j in range(n)] for i in range(n)]

classes={0:[{'representative':[],'orbit_size':1}]}
group_counts={0:1}
for n in range(1,4):
    group=[]
    for code in range(1<<(n*n)):
        g=mat_from_code(code,n);gi=inverse2(g,n)
        if gi is not None:group.append((g,gi))
    unseen=set(range(1<<(n*n)));cl=[]
    while unseen:
        code=min(unseen);M=mat_from_code(code,n)
        orbit={code_from_mat(product2(product2(g,M,n),gi,n),n) for g,gi in group}
        assert code==min(orbit) and orbit<=unseen
        unseen-=orbit
        cl.append({'representative':plain(M,n),'orbit_size':len(orbit)})
    classes[n]=cl;group_counts[n]=len(group)
assert [len(classes[n]) for n in range(4)]==[1,2,6,14]
assert [group_counts[n] for n in range(4)]==[1,1,6,168]

J=sp.Matrix([[0,1],[1,0]])
N=sp.zeros(3).row_join(sp.eye(3)).col_join(sp.zeros(3,6));M0=sp.eye(6)+N
allreps=[];typecounts=[]

def primitive_fixed(M):
    w=(M-sp.eye(6)).nullspace()[0]
    den=lcm(*[x.q for x in w]);ww=[int(den*x) for x in w]
    g=gcd(*ww)
    return sp.Matrix([x//g for x in ww])

def free_power_check(M,u,j):
    R=M**j-sp.eye(6);shift=sp.Rational(j,4)*u
    d,s,t=smith_normal_decomp(DomainMatrix.from_Matrix(R).convert_to(sp.ZZ))
    d,s,t=(m.to_Matrix() for m in (d,s,t))
    assert d==s*R*t
    r=sum(d[i,i]!=0 for i in range(6))
    coords=s*shift
    # The integer matrix R maps the torus onto the coordinates with
    # nonzero Smith factors; its zero rows require integral shift.
    return any(coords[i].q!=1 for i in range(r,6))

for r in (0,1):
    for p in range(4-2*r):
        q=3-2*r-p
        Aparts=([sp.eye(p)] if p else [])+([-sp.eye(q)] if q else [])+([J]*r)
        A=sp.diag(*Aparts)
        count=0
        for cp,cq in product(classes[p],classes[q]):
            B=sp.zeros(3)
            if p:B[:p,:p]=sp.Matrix(cp['representative'])
            if q:B[p:p+q,p:p+q]=sp.Matrix(cq['representative'])
            assert A*A==sp.eye(3) and A*B==B*A
            M1=A.row_join(B).col_join(sp.zeros(3).row_join(-A))
            M2=A.row_join(B-A).col_join(sp.zeros(3).row_join(-A))
            assert M1*M1==M2*M2==sp.eye(6)
            assert M1!=sp.eye(6) and M2!=sp.eye(6)
            assert (M1*M2).inv()==M0
            u1,u2=primitive_fixed(M1),primitive_fixed(M2)
            assert all(free_power_check(M,u,j) for M,u in [(M1,u1),(M2,u2)] for j in (1,2,3))
            allreps.append({'class_id':len(allreps)+1,'type_p_q_r':[p,q,r],'A':A.tolist(),'B':B.tolist(),'M1':M1.tolist(),'M2':M2.tolist(),'primitive_fixed_vectors':[list(u1),list(u2)],'affine_order_four_all_nonidentity_powers_free':True})
            count+=1
        typecounts.append({'type_p_q_r':[p,q,r],'classes':count})
assert len(allreps)==56
print(json.dumps({'computed_utc':datetime.now(timezone.utc).isoformat(),'binary_similarity_class_counts':{n:len(classes[n]) for n in range(4)},'binary_general_linear_group_orders':group_counts,'binary_similarity_classes':classes,'involution_type_counts':typecounts,'total_classes':56,'normal_form_matrices_and_free_lifts':allreps,'all_cusp_products_verified':True,'all_affine_power_freeness_tests_passed':True},indent=2,default=int))
