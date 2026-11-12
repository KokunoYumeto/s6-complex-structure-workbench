"""Bounded exact finite crosswalk checks, with no external-task writes.

Only standard-library integer/fraction arithmetic. No imports from the ES task.
"""
from fractions import Fraction as F
from itertools import permutations, product
from math import gcd, isqrt

def prime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
def factor(n):
    answer=[]
    d=2
    while d*d<=n:
        e=0
        while n%d==0:
            n//=d; e+=1
        if e: answer.append((d,e))
        d+=1
    if n>1: answer.append((n,1))
    return answer
def shell_counts(p,R):
    a=(p+R)//4
    assert (p+R)%4==0 and gcd(R,p*a)==1 and p>a and prime(p)
    counts={}
    fac=factor(a)
    for exps in product(*(range(-e,e+1) for _,e in fac)):
        value=1
        for (q,_),exponent in zip(fac,exps): value=value*pow(q,exponent,R)%R
        counts[value]=counts.get(value,0)+1
    c1=counts.get((-1)%R,0)
    cp=counts.get((-pow(p,-1,R))%R,0)
    return a,fac,c1,cp,c1+2*cp

V=[r for r in range(840) if r%24==1 and gcd(r,840)==1]
def beta(r): return tuple(0 if pow(r,(p-1)//2,p)==1 else 1 for p in (5,7))
fibres={b:[r for r in V if beta(r)==b] for b in product((0,1),repeat=2)}
assert len(V)==24 and all(len(v)==6 for v in fibres.values())
assert sorted(pow(289,j,840) for j in range(6))==fibres[(0,0)]
print('PASS: exact V840, Legendre quotient and cyclic principal fibre')

H2=[((0,0,0,0),(0,0)),((1,1,1,1),(0,0)),
    ((1,1,0,0),(1,0)),((0,0,1,1),(1,0)),
    ((1,0,1,0),(0,1)),((0,1,0,1),(0,1)),
    ((1,0,0,1),(1,1)),((0,1,1,0),(1,1))]
H3={tuple((a+b,a+2*b,a,b)[i]%3 for i in range(4)) for a,b in product(range(3),repeat=2)}
glue={(tuple((3*u[i]+2*z[i])%6 for i in range(4)),y) for u,y in H2 for z in H3}
assert len(glue)==72
minima={}
for x,y in glue:
    q=sum(F(5*k*k,6) for k in x)+int(any(y))
    assert q.denominator==1 and q.numerator%2==0
    minimum=sum(F(k*(6-k),6) for k in x)+int(any(y))
    minima[minimum]=minima.get(minimum,0)+1
assert set(minima)=={0,4,6} and minima[0]==1 and 6**4*4==72**2
print('PASS: index-72 isotropic glue; norm minima multiplicities',minima)

I=tuple(tuple(F(i==j) for j in range(4)) for i in range(4))
R=tuple(tuple(F(-1 if i==j==0 else i==j) for j in range(4)) for i in range(4))
H=tuple(tuple(F(v,2) for v in row) for row in ((1,1,1,1),(1,1,-1,-1),(1,-1,1,-1),(1,-1,-1,1)))
c=(F(-1,2),F(1,2),F(1,2),F(1,2))
assert H==tuple(tuple(I[i][j]-2*c[i]*c[j] for j in range(4)) for i in range(4))
def mv(A,v):return tuple(sum(A[i][j]*v[j] for j in range(4)) for i in range(4))
roots=set()
for i in range(4):
    for j in range(i+1,4):
        for a,b in product((-1,1),repeat=2):
            v=[F(0)]*4; v[i]=a; v[j]=b; roots.add(tuple(v))
for A in (R,H): assert {mv(A,v) for v in roots}==roots
Vweights={tuple(F(sign if i==j else 0) for i in range(4)) for j in range(4) for sign in (-1,1)}
Splus={tuple(F(v,2) for v in signs) for signs in product((-1,1),repeat=4) if signs[0]*signs[1]*signs[2]*signs[3]==1}
Sminus={tuple(F(v,2) for v in signs) for signs in product((-1,1),repeat=4) if signs[0]*signs[1]*signs[2]*signs[3]==-1}
assert {mv(R,v) for v in Splus}==Sminus
assert {mv(H,v) for v in Vweights}==Splus
assert {mv(H,v) for v in Sminus}==Sminus
print('PASS: ES Hadamard equals F4 short-root reflection; exact triality weight-set maps')

GL2=[((a,b),(c,d)) for a,b,c,d in product((0,1),repeat=4) if (a*d-b*c)%2]
def gy(A,y):return tuple(sum(A[i][j]*y[j] for j in range(2))%2 for i in range(2))
R2=((1,1),(0,1)); H2mat=((0,1),(1,0)); I2=((1,0),(0,1))
stabilizer=[]
for signs in product((1,-1),repeat=4):
    for perm in permutations(range(4)):
        for A in GL2:
            image={(tuple(signs[i]*x[perm[i]]%6 for i in range(4)),gy(A,y)) for x,y in glue}
            if image==glue: stabilizer.append((signs,perm,A))
assert len(stabilizer)==48
assert all(sum(A==G for _,_,A in stabilizer)==8 for G in GL2)
for name,G in (('R',R2),('H',H2mat)):
    assert {(x,gy(G,y)) for x,y in glue}!=glue
    chosen=next((signs,perm) for signs,perm,A in stabilizer if A==G)
    print(f'PASS: {name} requires A5 transport; one exact (signs, zero-based permutation) lift is {chosen}')
print('PASS: glue stabilizer has order 48; projection to D4 triality has eight lifts per element')

# The two displayed lifts preserve the ternary and binary generator spaces
# directly, and are involutions whose product has order three.
def transform(A,x):
    if A=='R': return (x[1],x[0],x[2],-x[3])
    return (x[0],x[2],x[1],-x[3])
za=(1,1,1,0); zb=(1,2,0,1)
assert tuple(v%3 for v in transform('R',za))==za
assert tuple(v%3 for v in transform('R',zb))==tuple(2*v%3 for v in zb)
assert tuple(v%3 for v in transform('H',za))==za
assert tuple(v%3 for v in transform('H',zb))==tuple((2*za[i]+2*zb[i])%3 for i in range(4))
for x in product(range(3),repeat=4):
    assert transform('R',transform('R',x))==x
    assert transform('H',transform('H',x))==x
    y=x
    for _ in range(3): y=transform('R',transform('H',y))
    assert y==x
print('PASS: exact S3 lift generators preserve the ternary code and Coxeter relations')

p1,p2,Rsh=2521,3361,3
assert p1%840==p2%840==1
d1=shell_counts(p1,Rsh);d2=shell_counts(p2,Rsh)
assert d1==(631,[(631,1)],0,0,0)
assert d2==(841,[(29,2)],2,2,6)
print('PASS: actual shell counts do not descend modulo 840:',p1,d1,p2,d2)
a,b,cc=841,974690,28266010
assert F(4,p2)==F(1,a)+F(1,b)+F(1,cc)
print('PASS: explicit R=3 ES certificate for 3361; no such shell certificate for 2521')
print('ALL CROSSWALK CHECKS PASSED')
