"""Exact, tiny rational checks for the original period-shear calculation."""
from fractions import Fraction as F
import json

A1 = [[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]]
A2 = [[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]]
I = [[int(i == j) for j in range(4)] for i in range(4)]
E = [[int(i == 3 and j == 0) for j in range(4)] for i in range(4)]

def mm(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]

def mv(a,v):
    return [sum(x*y for x,y in zip(row,v)) for row in a]

def add(a,b):
    return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]

def scale(c,a):
    return [[c*x for x in row] for row in a]

def norm(a,m):
    n=[[0]*4 for _ in range(4)]
    p=I
    for _ in range(m):
        n=add(n,p)
        p=mm(p,a)
    assert p == I
    return n

N1,N2=norm(A1,3),norm(A2,4)
assert mm(A1,E)==mm(E,A1)==E
assert mm(A2,E)==mm(E,A2)==E
r1=[0,-F(1,3),-F(1,3),0]
r2=[0,F(1,4),F(1,4),0]
l1=[0,0,-1,0]
l2=[0,F(1,2),0,0]
d1=[0,0,-1,F(1,3)]
d2=[0,F(1,2),0,-F(1,4)]
assert mv(add(I,scale(-1,A1)),r1)==d1
assert mv(add(I,scale(-1,A2)),r2)==d2
assert mv(N1,l1)==[0,0,0,-1]
assert mv(N2,l2)==[0,0,0,1]
product_cocycle=[x+y for x,y in zip(l1,mv(A1,l2))]
assert product_cocycle==[0,0,-F(3,2),F(1,2)]

# The simultaneous rational centralizer, computed by elimination on 16 unknowns.
equations=[]
for a in (A1,A2):
    for i in range(4):
        for j in range(4):
            row=[F(0)]*16
            for k in range(4):
                row[4*i+k]+=a[k][j]
                row[4*k+j]-=a[i][k]
            equations.append(row)
pivots=[]
r=0
for c in range(16):
    hit=next((i for i in range(r,len(equations)) if equations[i][c]),None)
    if hit is None:
        continue
    equations[r],equations[hit]=equations[hit],equations[r]
    den=equations[r][c]
    equations[r]=[v/den for v in equations[r]]
    for i in range(len(equations)):
        if i!=r and equations[i][c]:
            q=equations[i][c]
            equations[i]=[x-q*y for x,y in zip(equations[i],equations[r])]
    pivots.append(c)
    r+=1
free=[c for c in range(16) if c not in pivots]
basis=[]
for c in free:
    v=[F(0)]*16
    v[c]=1
    for i,p in enumerate(pivots):
        v[p]=-equations[i][c]
    basis.append([v[4*i:4*i+4] for i in range(4)])

assert len(basis)==2
assert basis==[E,I]

print(json.dumps({
    'N1':N1,'N2':N2,
    'r1_per_n':r1,'r2_per_n':r2,
    'l1_per_n':l1,'l2_per_n':l2,
    'l1_plus_A1_l2_per_n':product_cocycle,
    'centralizer_dimension':len(basis),'centralizer_basis':basis,
    'status':'all exact checks passed'
},default=str,indent=2))
