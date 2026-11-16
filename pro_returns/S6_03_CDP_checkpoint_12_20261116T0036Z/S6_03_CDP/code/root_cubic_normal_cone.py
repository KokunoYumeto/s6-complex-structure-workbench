"""Exact local and global budgets for the cubic normal-cone obstruction.

Plane curve ADE forms with total delta at most four.  The suspension is
z^3 = r(x,y).  Geometric genus is the lower-monomial count; the rational
first Betti number of its link counts plane monodromy eigenvalues zeta_3
and zeta_3^2.  All weights and comparisons use Fraction.
"""
from fractions import Fraction as F
from itertools import product

rows=[]
for n in range(1,9):
    rows.append((f'A{n}',F(1,2),F(1,n+1),[(0,j) for j in range(n)],(n+1)//2,2 if n%2 else 1))
for n in range(4,8):
    rows.append((f'D{n}',F(n-2,2*(n-1)),F(1,n-1),[(0,j) for j in range(n-1)]+[(1,0)],(n+2)//2,3 if n%2==0 else 2))
rows += [
    ('E6',F(1,3),F(1,4),list(product(range(2),range(3))),3,1),
    ('E7',F(1,3),F(2,9),[(0,j) for j in range(5)]+[(1,0),(1,1)],4,2),
    ('E8',F(1,3),F(1,5),list(product(range(2),range(4))),4,1),
]
res=[]
print('type; weights (x,y,z); delta; branches; mu; pg(suspension); b1(link); lower monomials')
for name,wx,wy,basis,delta,branches in rows:
    wz=F(1,3)
    mu=len(basis)
    assert mu==2*delta-branches+1,(name,mu,delta,branches)
    lower=[]
    for i,j,k in product(range(12),repeat=3):
        if (i+1)*wx+(j+1)*wy+(k+1)*wz <= 1:
            lower.append((i,j,k))
    pg=len(lower)
    eig=[(i+1)*wx+(j+1)*wy for i,j in basis]
    b1=sum(a-int(a) in (F(1,3),F(2,3)) for a in eig)
    assert pg<=1 and (pg==0 or delta>=3)
    assert b1<=2 and (b1==0 or delta>=3)
    res.append(dict(name=name,delta=delta,branches=branches,pg=pg,b1=b1))
    print(f'{name}; ({wx},{wy},{wz}); {delta}; {branches}; {mu}; {pg}; {b1}; {lower}')

collections=[]
def walk(start,used,items):
    collections.append(items)
    for i in range(start,len(res)):
        r=res[i]
        if used+r['delta']<=4:
            walk(i,used+r['delta'],items+[r])
walk(0,0,[])
minimum=100
for items in collections:
    delta=sum(r['delta'] for r in items)
    genus=4-delta
    p=sum(r['pg'] for r in items)
    link=sum(r['b1'] for r in items)
    nu=sum(r['branches']-1 for r in items)
    assert p<=1 and link<=2
    b_boundary=2*genus+nu+link
    e_open=3*(2+2*genus+nu)
    rank_lower=e_open-1-b_boundary
    assert rank_lower>=3+4*genus+2*nu
    minimum=min(minimum,rank_lower)
print(f'Checked {len(collections)} singularity collections with total delta <=4.')
print('For every collection: sum pg <=1, sum b1(link)<=2.')
print('b1(U)=2q(X)<=2; intersection rank lower bound >=3+4g+2*sum(branches-1)>0.')
print('Minimum certified intersection-rank lower bound:',minimum)
print('PASS')
