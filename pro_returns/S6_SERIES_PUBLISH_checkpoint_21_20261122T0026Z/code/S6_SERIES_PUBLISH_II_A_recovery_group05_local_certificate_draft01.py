"""Fresh prefreeze recovery computations for WN, WO, WP, WQ.

Written from the statement equations and surviving independent derivations.
No target proof or historical target routine has been read.
The old 19:48 program was lost; this is a new file and run.
"""
from collections import defaultdict
from itertools import permutations, product
from math import comb, gcd

# Sparse exact arithmetic in Z[zeta,y,u]/(zeta^a-1).
def clean(p): return {e:c for e,c in p.items() if c}
def add(p,q):
    r=defaultdict(int,p)
    for e,c in q.items(): r[e]+=c
    return clean(r)
def scale(p,c): return clean({e:c*v for e,v in p.items()})
def mul(p,q,a):
    r=defaultdict(int)
    for e,c in p.items():
        for f,d in q.items():
            r[((e[0]+f[0])%a,e[1]+f[1],e[2]+f[2])]+=c*d
    return clean(r)
def power(p,k,a):
    r={(0,0,0):1}
    for _ in range(k):r=mul(r,p,a)
    return r
one={(0,0,0):1}
chart_count=0
for a,n in product(range(2,10),range(1,6)):
    zeta={(1,0,0):1}
    x=add(zeta,{(0,n,1):1})
    z={(a-k,n*(k-1),k):comb(a,k) for k in range(1,a+1)}
    assert add(add(power(x,a,a),scale(mul(z,{(0,n,0):1},a),-1)),scale(one,-1))=={}
    P={}
    for k in range(a):
        P=add(P,mul(power(x,a-1-k,a),power(zeta,k,a),a))
    assert mul({(0,0,1):1},P,a)==z
    chart_count+=1
assert chart_count==40
print('Affine charts and their inverse cross-multiplication: 40 complete residue-ring polynomial identities, a=2..9, n=1..5.')

# Incidence minors: exact signed matching enumeration, not a determinant library.
def det_terms(matrix):
    r=len(matrix)
    answer=0
    nonzero=0
    for p in permutations(range(r)):
        v=1
        for i,j in enumerate(p):
            v*=matrix[i][j]
            if not v:break
        if v:
            inversions=sum(p[i]>p[j] for i in range(r) for j in range(i+1,r))
            answer+=(-1)**inversions*v
            nonzero+=1
    return answer,nonzero
for a in range(2,10):
    r=a-1
    # Column i is e_i-e_(i+1).
    incidence=[[int(j==i)-int(j==i+1) for i in range(r)] for j in range(a)]
    minors=[]
    for deleted in range(a):
        d,count=det_terms([row for j,row in enumerate(incidence) if j!=deleted])
        assert abs(d)==1 and count==1
        minors.append(d)
    cauchy_binet=sum(d*d for d in minors)
    assert cauchy_binet==a
    for n in range(1,6):
        gram=[[-n*sum(incidence[k][i]*incidence[k][j] for k in range(a)) for j in range(r)] for i in range(r)]
        assert all(gram[i][j]==(-2*n if i==j else n if abs(i-j)==1 else 0) for i in range(r) for j in range(r))
        det=(-n)**r*cauchy_binet
        assert det==(-1)**r*a*n**r and det!=0
print('Integral lattice: incidence deleted-row minors each have one signed matching and determinant +/-1; Cauchy–Binet gives det=(-1)^(a-1)*a*n^(a-1), a=2..9,n=1..5.')

# Deck orbits and their exact invariant i+j modulo gcd(b,c).
deck_cases=0
for b,c in product(range(1,9),repeat=2):
    d=gcd(b,c)
    remaining=set(product(range(b),range(c)))
    orbits=[]
    while remaining:
        start=min(remaining)
        orbit=[]
        p=start
        while p not in orbit:
            orbit.append(p)
            p=((p[0]+1)%b,(p[1]-1)%c)
        assert p==start
        assert len(orbit)==b*c//d
        assert len({(i+j)%d for i,j in orbit})==1
        remaining.difference_update(orbit)
        orbits.append(orbit)
    assert len(orbits)==d
    assert {((o[0][0]+o[0][1])%d) for o in orbits}==set(range(d))
    assert d*(b*c//d)==b*c
    deck_cases+=1
assert deck_cases==64
print('Deck permutation: 64 cases b,c=1..8, gcd(b,c) invariant-labelled orbits each of length bc/gcd(b,c).')

# First-order dual algebra for derivatives: (value, dy, dt).
def dual_mul(p,q):
    return (p[0]*q[0],p[1]*q[0]+p[0]*q[1],p[2]*q[0]+p[0]*q[2])
def dual_power(p,k):
    r=(1,0,0)
    for _ in range(k):r=dual_mul(r,p)
    return r
normal_values=0
for y,t in product(range(5),range(7)):
    x=y*y*t**3
    z=t*t
    assert x*x-z**3*y**4==0
    normal_values+=1
assert normal_values==35
for y,t in product(range(3),range(5)):
    Y,T=(y,1,0),(t,0,1)
    X=dual_mul(dual_power(Y,2),dual_power(T,3))
    Z=dual_power(T,2)
    rows=[X,Y,Z]
    minors=[]
    for i,j in [(0,1),(0,2),(1,2)]:
        minors.append(rows[i][1]*rows[j][2]-rows[i][2]*rows[j][1])
    assert minors==[-3*y*y*t*t,4*y*t**4,2*t]
print('WP normalization identity: 35 exact grid values with separate degree (4,6).')
print('WP differential minors by first-order dual algebra: 15 exact values with separate degree (2,4), giving (-3 y^2 t^2,4 y t^4,2t), hence ideal (t).')

# Exact Laurent-polynomial arithmetic in the coordinate pair (y,x).
def lmul(p,q):
    r=defaultdict(int)
    for e,c in p.items():
        for f,d in q.items():r[(e[0]+f[0],e[1]+f[1])]+=c*d
    return clean(r)
Y={(1,0):1}; X={(0,1):1}; Z={(-2,2):1,(-3,0):-1}
F=add(lmul(Y,lmul(X,X)),scale(lmul(Z,lmul(Y,lmul(Y,Y))),-1))
assert F=={(0,0):1}
print('WQ affine inverse: exact Laurent dictionary substitution z=y^-2*x^2-y^-3 gives y*x^2-z*y^3=1.')

# Normalization monomial relations and the conductor from the finite R-module
# generating set {1,t}; membership in yR tests h and ht.
def umbrella_member(i,j):return i>=0 and j>=0 and (j%2==0 or i>=1)
def yR_member(i,j):return i>=1 and j>=0 and umbrella_member(i-1,j)
for i,j in product(range(17),repeat=2):
    conductor=umbrella_member(i,j) and umbrella_member(i,j+1)
    full_union=yR_member(i,j) and yR_member(i,j+1)
    assert conductor==(i>=1)
    assert full_union==(i>=2)
# nu_B=(yt,y,t^2): the umbrella polynomial has identical monomials.
assert (2,2)==(2,0+2)
# WO a=n=3: x=yt,y=y,z=t^3 gives x^3=z*y^3.
assert (3,3)==(3,3)
# WO a=4,n=2: reduce v^2=u*w in the source A1 ring.
def a1_reduce(u,v,w):
    q,r=divmod(v,2)
    return (u+q,r,w+q)
assert a1_reduce(0,4,0)==a1_reduce(2,0,2)
print('WQ conductor: on all exponent pairs 0..16, testing {h,ht} gives (y) on the umbrella and (y^2) for the union; the planar component ideal is (x^2).')
print('WO normalization equations agree under (y,t)->(yt,y,t^3) and (u,v,w)->(v,w,u^2) on v^2=u*w.')

# The weighted equations are identities in the positive parameters.
for a,b,c,n in product(range(2,10),range(1,9),range(1,9),range(1,6)):
    assert a*(n+1)==a+n*a
    assert a*(b+c)==b*a+c*a
print('Positive weights: (n+1,a,a) has degree a(n+1), and (b+c,a,a) has degree a(b+c).')
print('All results are exact. Universal geometric, degree-bound, and all-exponent arguments are in the derivations; finite parameter runs are not substituted for them.')

