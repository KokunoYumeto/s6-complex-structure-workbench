"""Post-exposure KZ auxiliary block identities, from literal marked matrices.

No historical KZ program or output is read. These are exact identities;
the complete all-order and geometric arguments are in the comparison.
"""
from pathlib import Path
from fractions import Fraction
from itertools import combinations


def mul(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]


def ident(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]


def minus(a,b):
    return [[x-y for x,y in zip(row,other)] for row,other in zip(a,b)]


def rank(a):
    a=[list(map(Fraction,row)) for row in a]
    r=0
    for j in range(len(a[0])):
        p=next((i for i in range(r,len(a)) if a[i][j]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]
        v=a[r][j]
        a[r]=[x/v for x in a[r]]
        for i in range(len(a)):
            if i!=r:
                v=a[i][j]
                a[i]=[x-v*y for x,y in zip(a[i],a[r])]
        r+=1
    return r


cases=[
    (1,[[-1,-3,0,4],[0,-1,0,4],[-1,-2,1,3],[0,0,0,1]],
     [[2,0,-1,0],[0,1,0,2],[1,0,0,0],[0,0,0,1]],
     [[0,0,1,0],[0,1,0,-2],[-1,0,2,0],[0,0,0,1]]),
    (4,[[-1,-3,0,1],[0,-1,0,1],[-4,-8,1,3],[0,0,0,1]],
     [[1,0,0,0],[0,0,0,1],[2,0,1,0],[0,-1,0,2]],
     [[1,0,0,0],[0,2,0,-1],[-2,0,1,0],[0,1,0,0]])
]
for a,t,h,hi in cases:
    assert mul(h,hi)==mul(hi,h)==ident(4)
    b=mul(mul(hi,t),h)
    n=minus(mul(t,t),ident(4))
    assert mul(t,n)==[[-x for x in row] for row in n]
    z=[[0]*4 for _ in range(4)];z[0][1]=3
    assert mul(mul(hi,n),h)==z
    assert b[1]==[0,-1,0,0]
    assert [[b[i][j] for j in (2,3)] for i in (2,3)]==ident(2)
    assert b[2][0]==b[3][0]==0
    pp=list(combinations(range(4),2))
    w=[[t[i][k]*t[j][l]-t[i][l]*t[j][k] for k,l in pp] for i,j in pp]
    assert 4-rank(minus(t,ident(4)))==2
    assert 6-rank(minus(w,ident(6)))==2
    print('SECTION_PAIR',a,4//a)
    print('H_inverse_T_H',b)
    print('H_inverse_N_H',z)
    print('PASS T N=-N; primitive Smith factor3; dual sign-1; transverse identity; f=g=2')

print('PASS exact auxiliary identities for all eight initial markers via the two section pairs.')
