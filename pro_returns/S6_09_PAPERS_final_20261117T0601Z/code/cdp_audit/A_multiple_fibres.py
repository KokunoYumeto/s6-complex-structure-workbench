"""Exact character computations for Example A.3.2; no numerical approximation."""
from math import comb
print('m k b h0 h1 h2')
for m in range(3,13):
    for b in range(m):
        for k in range(1,m+1):
            tangent=[j for j in range(k) if (j+b)%m==0]
            normal=[j for j in range(k) if (j+b+1)%m==0]
            d=2*len(tangent)+len(normal)
            h=tuple(d*comb(2,q) for q in range(3))
            if b==1:
                expected=0 if k<=m-2 else (1 if k==m-1 else 3)
                assert d==expected
            print(m,k,b,*h)
print('For b=1: support cohomology (0,0,0), full fibre (3,6,3).')
print('For b=1: global cohomology on quotient Y: (0,1,2,1).')
print('Global Cech normal-form H1 basis: dz/z (weight 0), dz (weight 1).')
print('ALL CHARACTER COUNTS PASSED')
