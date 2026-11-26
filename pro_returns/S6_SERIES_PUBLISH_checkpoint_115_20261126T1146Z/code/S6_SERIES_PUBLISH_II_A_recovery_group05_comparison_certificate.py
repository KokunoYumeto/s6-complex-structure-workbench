"""Postrelease comparison computations for WN--WQ; no new blind credit."""
from itertools import product, permutations

def det(a):
    n=len(a);ans=0
    for p in permutations(range(n)):
        v=1
        for i,j in enumerate(p):v*=a[i][j]
        ans+=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))*v
    return ans

for a,b,c,d in product(range(3),repeat=4):
    M=[[1,0,1,0],[0,1,0,1],[a,b,c,d],[b,-a,d,-c]]
    assert det(M)==-((c-a)**2+(d-b)**2)
print('Lifted-arc graph-plane determinant: 81 exact grid values, separate degree <=2, det=-|c_l-c_k|^2.')

def egcd(a,b):
    if b==0:return a,1,0
    d,u,v=egcd(b,a%b)
    return d,v,u-(a//b)*v
for b,c in product(range(1,9),repeat=2):
    d,p,q=egcd(b,c)
    B,C=b//d,c//d
    assert B*p+C*q==1
    M=[[B,C],[q,-p]]
    inv=[[p,C],[q,-B]]
    assert [[sum(M[i][k]*inv[k][j] for k in range(2)) for j in range(2)] for i in range(2)]==[[1,0],[0,1]]
    pairings=[[-2*B*C for j in range(d)] for i in range(d)]
    assert sum(map(sum,pairings))==-2*b*c
print('64 coprime exponent matrices have the displayed integral inverse; all lifted-arc pairings sum to -2bc.')

for a,n in product(range(2,7),range(1,13)):
    size=a*n
    def coordinates(v):
        q=[v[i*n+n-1] for i in range(a)]
        differences=[[v[i*n+j]-v[i*n+j+1] for j in range(n-1)] for i in range(a)]
        return q,differences
    def reconstruct(q,differences):
        return [q[i]+sum(differences[i][j:]) for i in range(a) for j in range(n)]
    for k in range(size):
        v=[int(j==k) for j in range(size)]
        assert reconstruct(*coordinates(v))==v
    for k in range(a-1):
        q=[int(i==k)-int(i==k+1) for i in range(a)]
        coefficients=[sum(q[:i+1]) for i in range(a-1)]
        assert coefficients==[int(i==k) for i in range(a-1)]
        assert sum(q)==0
    parent={'infty_y':'infty_x','zero_y':'infty_x'}
    for i in range(a):
        for j in range(1,n):
            parent[(i,j)]='zero_y' if j==1 else (i,j-1)
    assert len(parent)==2+a*(n-1)
    for v in parent:
        for _ in range(n+2):
            if v=='infty_x':break
            v=parent[v]
        assert v=='infty_x'
print('60 blowup-boundary cases: explicit integer coordinate inverse and root-basis inverse; every boundary vertex has a parent path to infinity_x.')

def mixed_member(i,j):return i%2==0 or (i>=3 and j>=2)
for i,j in product(range(17),repeat=2):
    assert (mixed_member(i,j) and mixed_member(i+1,j))==(i>=2 and j>=2)
print('Mixed-example conductor via normalization module {1,u}: exponent pairs 0..16 give exactly u^2 v^2.')

def mpow(e,k):return tuple(k*x for x in e)
def mmul(e,f):return tuple(x+y for x,y in zip(e,f))
for a,n in product(range(2,10),range(1,7)):
    x,y,z=(n,1),(a,0),(0,a)
    assert all((e[0]-n*e[1])%a==0 for e in [x,y,z])
    assert mpow(x,a)==mmul(mpow(y,n),z)
def a1(e):
    u,v,w=e;q,r=divmod(v,2)
    return u+q,r,w+q
for a,n,x,y,z in [(2,3,(1,1,0),(1,0,0),(0,0,1)),(4,2,(0,1,0),(0,0,1),(2,0,0))]:
    assert a1(mpow(x,a))==a1(mmul(z,mpow(y,n)))
print('General mu_a normalization monomials are invariant and satisfy the hypersurface equation; both A1 normalization maps satisfy it after reducing V^2=UW.')
print('Postrelease computations complete; geometric and integral maps are proved in the comparison supplement.')

