#!/usr/bin/env python3
"""Post-comparison recomputation of the complete historical 127-lattice scope.

The alternative evaluator polarizes the quotient-cell cubic by seven integer
function evaluations. It then compares this with restriction to one surface.
No historical implementation or data file is read.
"""
from itertools import combinations_with_replacement
from datetime import datetime,timezone

rays=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
def det(u,v): return u[0]*v[1]-u[1]*v[0]
for r in range(6):
    assert det(rays[r],rays[(r+1)%6])==1
    assert tuple(rays[(r-1)%6][j]+rays[(r+1)%6][j] for j in range(2))==rays[r]
print('UTC:',datetime.now(timezone.utc).isoformat())
count=tests=0
for a in range(1,13):
    for d in range(1,12//a+1):
        for b in range(a):
            vertices=[(x,y) for y in range(d) for x in range(a)]
            D=a*d
            def red(x,y):
                q,r=divmod(y,d)
                return a*r+(x-b*q)%a
            adjacent=[[red(x+dx,y+dy) for dx,dy in rays] for x,y in vertices]
            edges=[(i,adjacent[i][r]) for i in range(D) for r in range(3)]
            triangles=[]
            for i,(x,y) in enumerate(vertices):
                triangles.extend([(i,red(x+1,y),red(x,y+1)),
                    (red(x+1,y+1),red(x+1,y),red(x,y+1))])
            def C(z):
                return (6*sum(t**3 for t in z)
                    -3*sum(z[i]*z[j]*(z[i]+z[j]) for i,j in edges)
                    +6*sum(z[i]*z[j]*z[k] for i,j,k in triangles))
            def value(indices):
                z=[0]*D
                for i in indices:z[i]+=1
                return C(z)
            for i,j,k in combinations_with_replacement(range(D),3):
                numerator=(value((i,j,k))-value((i,j))-value((i,k))
                    -value((j,k))+value((i,))+value((j,))+value((k,)))
                assert numerator%6==0
                v=[int(neighbor==j)-int(i==j) for neighbor in adjacent[i]]
                w=[int(neighbor==k)-int(i==k) for neighbor in adjacent[i]]
                intersection=sum(-v[r]*w[r]+v[r]*w[(r+1)%6]
                                 +v[(r+1)%6]*w[r] for r in range(6))
                assert numerator//6==intersection
                tests+=1
            count+=1
assert count==127
print('All127 Hermite forms of index at most12; polarized basis triples:',tests)
print('Every seven-evaluation numerator is divisible by6 and gives the exact surface product.')
print('Six primitive adjacent determinants and all six ray relations verified.')
print('No historical target program or data was imported; all comparisons pass.')
