"""Exact checks for logarithmic multiplicities, weighted rings, and cyclic cusps."""
from fractions import Fraction
from math import gcd
from sympy import Matrix, zeros, symbols, sqrt, simplify
import json
from pathlib import Path

OUT=Path(__file__).resolve().parents[1]/'outputs'
rows=[]
for k in range(1,6):
    for l in range(1,6):
        m1,m2=3*k,4*l
        if m1*m2>60 or gcd(m1,m2)!=1:
            continue
        d=4*l+3*k-k*l
        hs=[]
        for n in range(13):
            # Independent exact descriptions: floor-divisor and monomial count.
            deg=n+((-n*(k-1))//m1)+((-n*(3*l-1))//m2)
            h1=max(deg+1,0)
            h2=sum(1 for a in range(max(d*n,0)//m2+1)
                   if d*n-m2*a>=0 and (d*n-m2*a)%m1==0)
            assert h1==h2,(k,l,n,h1,h2)
            hs.append(h1)
        row={'k':k,'l':l,'multiplicities':[m1,m2],
             'K_coefficients':[k-1,3*l-1], 'minus_K_weight':d,
             'ring_variable_weights':[m2,m1],'anti_plurigenera_n_0_to_12':hs}
        rows.append(row)
        print(json.dumps(row))
print('All weighted-section counts agree with the divisor-floor formula exactly.')

for n in (1,5,7,11):
    b1=zeros(n,3*n)
    b2=zeros(3*n,2*n)
    for i in range(n):
        j=(i+1)%n
        for offset in (0,2*n):
            b1[j,offset+i]+=1
            b1[i,offset+i]-=1
        # Two triangles in each square, including the vertical loop.
        b2[i,2*i]+=1; b2[n+j,2*i]+=1; b2[2*n+i,2*i]-=1
        b2[2*n+i,2*i+1]+=1; b2[i,2*i+1]-=1; b2[n+i,2*i+1]-=1
    assert b1*b2==zeros(n,2*n)
    ranks=(b1.rank(),b2.rank())
    betti=(n-ranks[0],3*n-ranks[0]-ranks[1],2*n-ranks[1])
    assert betti==(1,2,1)
    print('Cusp cover',n,'cells',(n,3*n,2*n),'boundary ranks',ranks,'O-cohomology',betti)

t=symbols('t')
A=-3*t**3*(t-1); B=2*t**4*(t-1)**2
xP=0; yP=sqrt(2)*t**2*(t-1)
lam=A/(2*yP)
x2=simplify(lam**2-2*xP)
y2=simplify(-yP+lam*(xP-x2))
print('2P x=',x2,'y=',y2)
tstar=Fraction(32,5)
assert simplify(y2.subs(t,tstar))==0
assert simplify(yP.subs(t,tstar))!=0
assert simplify((4*A**3+27*B**2).subs(t,tstar))!=0
assert simplify((y2**2-x2**3-A*x2-B))==0
print('P has exact order four at t=32/5: checked regularity, P not order 2, 2P order 2.')
(OUT/'b_families.json').write_text(json.dumps(rows,indent=2)+'\n')
