"""Primitive H2 cohomology lattice and cubic for one marked OS45 example.

Input: OS45/default, P=2G,Q=8G, weights(2,0,0,0,0), e=1;
all multiplicative Mumford caps. The computation reconstructs the exact
cusp complement H1 before finding its mod2 meridian character. It then
extends all16-component triple products to the primitive index2 lattice.
"""
from pathlib import Path
from itertools import product
import json
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form
import manifolds_general_initial as G
from manifolds_rankone_families import decomp
from manifolds_weighted_profiles import group
import fourfolds_D2_component_ring as C
ROOT=Path(__file__).resolve().parents[1]
X=G.compute(45,'default',2,8,[2,0,0,0,0],e=1)
assert X['homology'][1]==dict(free=0,torsion=[])
assert X['fundamental_group']['vertical_quotient']==dict(free=0,torsion=[])
assert X['homology'][2]==dict(free=15,torsion=[8])
assert X['homology'][3]==dict(free=0,torsion=[8])
A=list(map(s.Matrix,X['fundamental_group']['conjugation_matrices']))
count=len(A);nrow=4+count-1
cols=[(B-s.eye(4))[:,j].col_join(s.zeros(count-1,1)) for B in A for j in range(4)]
def base(i):return s.eye(count-1)[:,i] if i<count-1 else -s.ones(count-1,1)
power=s.Matrix([0,0,0,-1])
cols.append((-power).col_join(base(0)))
for cap in X['local'][1:]:
    idx=1+cap['site'];F=s.Matrix(cap['pi1_kernel'])
    cols.extend(v.col_join(s.zeros(count-1,1)) for v in F.columnspace())
    cols.append(s.zeros(4,1).col_join(base(idx)))
M=s.Matrix.hstack(*cols)
D,U,V,rank=decomp(M)
assert abs(U.det())==abs(V.det())==1 and U*M*V==D
assert group(M)==dict(free=1,torsion=[2])
tors=[i for i in range(rank) if abs(D[i,i])>1]
assert len(tors)==1 and D[tors[0],tors[0]] in (-2,2)
chi=U[tors[0],:]
assert [int(x)%2 for x in chi]==[0,0,1,0]+[0]*(count-1)
free=U[rank,:]
if (free*s.zeros(4,1).col_join(base(1)))[0]<0:free=-free
vertices=list(product(range(8),range(2)))
meridians=[]
for r,t in vertices:
    mer=s.Matrix([r,0,t,0]).col_join(base(1))
    assert (free*mer)[0]==1
    assert (chi*mer)[0]%2==t
    meridians.append(dict(vertex=[r,t],free=1,torsion=t))

form=C.run(8,0,2)
T=[[[0 for k in range(16)] for j in range(16)] for i in range(16)]
from itertools import permutations
for row in form['symmetric_integral_trilinear']:
    for idx in set(permutations(row['indices'])):T[idx[0]][idx[1]][idx[2]]=row['intersection']
# Verify the closed geometric formula, independently of its later basis change.
for i,j,k in product(range(16),repeat=3):
    values=[i,j,k];distinct=set(values)
    if len(distinct)==1: expected=6
    elif len(distinct)==2:
        ii=next(v for v in distinct if values.count(v)==2)
        jj=next(v for v in distinct if values.count(v)==1)
        r,ss=vertices[ii];rr,tt=vertices[jj]
        expected=-2 if r==rr else (-1 if (rr-r)%8 in (1,7) else 0)
    else:
        columns={vertices[v][0] for v in distinct}
        expected=int(len(columns)==2 and ((max(columns)-min(columns))%8 in (1,7)))
    assert T[i][j][k]==expected

# Component classes in the primitive basis (x0,...,x13,y).
image=s.zeros(15,16)
for i in range(14):image[i,i]=1
for i in range(0,14,2):image[i,14]=-1
image[14,14]=-2
for i in range(1,14,2):image[i,15]=-1
image[14,15]=2
assert image*s.ones(16,1)==s.zeros(15,1)
assert group(image)==dict(free=0,torsion=[2])
assert image*s.Matrix([i%2 for i in range(16)])==2*s.eye(15)[:,14]
# Rational representatives in the component lattice.
Q=s.zeros(16,15)
for i in range(14):Q[i,i]=1
for i in range(1,16,2):Q[i,14]=s.Rational(1,2)
assert image*Q==s.eye(15)
S=[[[s.Integer(0) for k in range(15)] for j in range(15)] for i in range(15)]
for i,j,k in product(range(15),repeat=3):
    qi=[(a,Q[a,i]) for a in range(16) if Q[a,i]]
    qj=[(a,Q[a,j]) for a in range(16) if Q[a,j]]
    qk=[(a,Q[a,k]) for a in range(16) if Q[a,k]]
    S[i][j][k]=sum(x*y*z*T[a][b][c] for a,x in qi for b,y in qj for c,z in qk)
    assert S[i][j][k].q==1
for i,j,k in product(range(15),repeat=3):
    assert S[i][j][k]==S[j][i][k]==S[k][j][i]
for i,j in product(range(14),repeat=2):
    r,ss=vertices[i];rr,tt=vertices[j]
    expected=(-1)**ss*((tt==ss and (rr-r)%8 in (1,7))-2*(i==j))
    assert S[14][i][j]==expected
    assert S[14][14][i]==0
assert S[14][14][14]==0
for i,j,k in product(range(16),repeat=3):
    ci=[(a,image[a,i]) for a in range(15) if image[a,i]]
    cj=[(a,image[a,j]) for a in range(15) if image[a,j]]
    ck=[(a,image[a,k]) for a in range(15) if image[a,k]]
    value=sum(x*y*z*S[a][b][c] for a,x in ci for b,y in cj for c,z in ck)
    assert value==T[i][j][k]
# Toric Picard classes in cyclic ray order.
curves=[s.Matrix(v) for v in [(0,1,0,0),(1,-1,-1,0),(0,0,1,0),
                             (1,0,-1,-1),(0,0,0,1),(1,-1,0,-1)]]
Pic=s.diag(1,-1,-1,-1);f=s.Matrix([1,-1,0,0])
assert sum((curves[i] for i in [1,2,4,5]),s.zeros(4,1))==2*f
assert (f.T*Pic*f)[0]==0
assert [(f.T*Pic*c)[0] for c in curves]==[1,0,0,1,0,0]
sparse=[dict(indices=[i,j,k],intersection=int(S[i][j][k])) for i in range(15) for j in range(i,15) for k in range(j,15) if S[i][j][k]]
result=dict(status='PASS',input=dict(entry=45,profile='default',a=2,b=8,weights=[2,0,0,0,0],e=1),
            complement_H1=group(M),complement_presentation=M.tolist(),
            complement_smith=D.tolist(),complement_left=U.tolist(),
            torsion_character=list(map(int,chi)),free_character=list(map(int,free)),
            component_meridians=meridians,vertices=vertices,
            component_classes_in_primitive_basis=image.tolist(),component_index=2,
            primitive_basis=['x'+str(i) for i in range(14)]+['y'],
            y_equals_half_odd_sum=True,y_restriction_even=[1,-1,0,0],
            y_restriction_odd=[-1,1,0,0],
            primitive_trilinear=sparse,component_form=form,
            p1_on_primitive_free_basis=[0]*15,
            scope='Exact primitive free lattice/cubic and free characteristic pairings; no complete torsion mu or refined-P claim.')
(ROOT/'records/fourfolds_OS45_primitive_cubic.json').write_text(json.dumps(result,indent=2,default=int)+'\n')
print('PASS: complement H1=Z+Z2; all16 meridians; exact component index2.')
print('PASS: all3375 primitive triples integral/symmetric; all4096 component triples recovered.')
print('PASS: y restriction±(H-E1), y²x_i=y³=0; nonzero sorted primitive triples',len(sparse))
