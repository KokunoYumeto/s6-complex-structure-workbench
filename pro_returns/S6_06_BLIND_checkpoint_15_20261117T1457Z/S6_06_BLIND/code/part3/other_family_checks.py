"""Exact checks from the supplied Yang and Wang construction matrices.

No earlier-run proof, code or file is imported.  The geometric local
specialization maps are explained in notes/part3_other_families.md.
"""
from itertools import combinations
from pathlib import Path
from functools import reduce
from math import gcd, lcm
import json
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form

OUT = Path(__file__).with_suffix('.json')

def data(a):
    return [[int(v) for v in a.row(i)] for i in range(a.rows)]

def smith(a):
    d = smith_normal_form(a, domain=s.ZZ)
    return [abs(int(d[i,i])) for i in range(min(d.shape)) if d[i,i]]

def wedge(a,q):
    ix=list(combinations(range(a.rows),q))
    return s.Matrix([[a.extract(i,j).det() for j in ix] for i in ix])

def contraction(ell,q):
    src=list(combinations(range(len(ell)),q))
    dst=list(combinations(range(len(ell)),q-1))
    a=s.zeros(len(dst),len(src))
    for j,ix in enumerate(src):
        for k,b in enumerate(ix):
            a[dst.index(ix[:k]+ix[k+1:]),j] += (-1)**k*ell[b]
    return a

yang={}
for name,m,n in [('B',4,6),('C',3,6)]:
    r=s.Matrix([[-1,m,0],[1,0,n],[0,1,1]])
    yang[name]={'matrix':data(r),'determinant':int(r.det()),'smith':smith(r),
                'universal_cyclic_quotient':gcd(m,n)}

T=[s.Matrix(a) for a in [
 [[1,0,-6,-2],[0,-1,-1,1],[0,1,0,-1],[0,0,0,1]],
 [[1,0,6,3],[0,1,2,1],[0,0,1,0],[0,0,0,1]],
 [[1,0,0,0],[0,2,1,0],[0,-1,0,0],[0,0,0,1]],
 [[1,0,0,-1],[0,1,1,0],[0,0,1,0],[0,0,0,1]],
]]
assert reduce(lambda a,b:a*b,T,s.eye(4))==s.eye(4)
assert T[0]**3==s.eye(4)
ell=s.Matrix([1,-2,-4,0])
assert T[0].inv().T*ell==ell

invariant={0:s.Matrix([1]),1:s.Matrix([1,0,0,0]),
           2:s.Matrix([0,0,6,1,0,0]),3:s.Matrix([1,0,0,0]),4:s.Matrix([1])}
coinvariant={0:s.Matrix([[1]]),1:s.Matrix([[0,0,0,1]]),
             2:s.Matrix([[0,0,1,6,0,0]]),3:s.Matrix([[0,0,0,1]]),4:s.Matrix([[1]])}
specialization_weight={0:1,1:3,2:1,3:1,4:3}
wang={}
for q in range(5):
    mats=[wedge(t,q) for t in T]
    n=mats[0].rows
    differences=[a-s.eye(n) for a in mats]
    d0ambient=s.Matrix.vstack(*differences)
    rel=s.Matrix.hstack(*differences)
    assert d0ambient*invariant[q]==s.zeros(4*n,1)
    assert coinvariant[q]*rel==s.zeros(1,4*n)
    assert all(x==1 for x in smith(rel))
    assert rel.rank()==n-1
    images=[hermite_normal_form(a) for a in differences]
    d0blocks=[b.gauss_jordan_solve(a)[0] if b.cols else s.zeros(0,n)
              for a,b in zip(differences,images)]
    assert all(v.q==1 for b in d0blocks for v in b)
    d0=s.Matrix.vstack(*d0blocks)
    before=s.eye(n)
    d1blocks=[]
    for a,b in zip(mats,images):
        d1blocks.append(before*b)
        before=before*a
    d1=s.Matrix.hstack(*d1blocks)
    assert d1*d0==s.zeros(n,n)
    middle_rank=sum(b.cols for b in images)
    assert middle_rank-d1.rank()-d0.rank()==0
    assert all(x==1 for x in smith(d0ambient))
    record={
        'exterior_matrices':[data(a) for a in mats],
        'local_image_bases':[data(a) for a in images],
        'd0':data(d0),'d1':data(d1),
        'd0_rank':d0.rank(),'d1_rank':d1.rank(),
        'middle_rank':middle_rank,
        'd0_ambient_smith':smith(d0ambient),
        'coinvariant_relation_smith':smith(rel),
        'global_invariant':data(invariant[q]),
        'coinvariant_projection':data(coinvariant[q]),
        'global_specialization_index':specialization_weight[q],
        'parabolic_H1':0,
    }
    if q:
        contraction_matrix=contraction(list(ell),q)
        numerator=(coinvariant[q-1]*contraction_matrix*
                   (specialization_weight[q]*invariant[q]))[0]
        assert numerator%3==0
        record['contraction_matrix']=data(contraction_matrix)
        record['clutch_numerator']=int(numerator)
        record['leray_d2']=int(numerator/3)
    wang[q]=record

d2=[wang[q]['leray_d2'] for q in range(1,5)]
assert d2==[1,2,2,1]
# The filtered integral cochain model has one generator in each
# bidegree (0,q),(2,q), 0<=q<=4; the only differential is this d2.
# Total degree is p+q. There are no extension choices, since each
# positive total degree has at most one surviving filtration term.
cohomology={'0':'Z','1':'0','2':'0','3':'Z/2','4':'Z/2','5':'0','6':'Z'}
homology={'0':'Z','1':'0','2':'Z/2','3':'Z/2','4':'0','5':'0','6':'Z'}
H=[a.inv().T for a in T]
nonfinite=s.Matrix.hstack(*[a-s.eye(4) for a in H[1:]])
full=s.Matrix.hstack(nonfinite,ell)
finite=s.zeros(5,5);finite[:4,:4]=H[0]-s.eye(4);finite[:4,4]=-ell;finite[4,4]=3
assert smith(nonfinite)==[1,1,1] and smith(full)==[1,1,1,1]
assert smith(finite)==[1,1,1]
result={'Yang':yang,'Wang':wang,'Wang_d2':d2,
        'Wang_nonfinite_pi1_matrix':data(nonfinite),
        'Wang_full_pi1_matrix':data(full),'Wang_finite_H1_matrix':data(finite),
        'Wang_cohomology':cohomology,'Wang_homology':homology}
OUT.write_text(json.dumps(result,indent=2)+'\n')
print('Yang canonical Smith forms:',{k:v['smith'] for k,v in yang.items()})
for q,v in wang.items():
    print('Wang exterior degree',q,'local ranks',
          [len(a[0]) if a else 0 for a in v['local_image_bases']],
          'ranks(d0,d1)',(v['d0_rank'],v['d1_rank']),
          'ambient primitive Smith',v['d0_ambient_smith'])
print('Wang integral Leray differentials:',d2)
print('Wang cohomology:',cohomology)
print('Wang homology:',homology)
print('Full integer matrices:',OUT)
