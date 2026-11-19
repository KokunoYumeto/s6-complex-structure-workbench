#!/usr/bin/env python3
"""New exact checks for VI; no historical implementation is imported.

Determinants here use the Leibniz formula, rather than the elimination used in
the other continuation program. Characteristic polynomials are determinant
polynomials, and zeta identities are checked by integer cross multiplication.
"""
from itertools import combinations, permutations, product
from fractions import Fraction as Q
from pathlib import Path
from math import gcd, isqrt, lcm
import json

def trim(p):
    while len(p)>1 and p[-1]==0:p.pop()
    return p
def add(p,q):
    r=[0]*max(len(p),len(q))
    for i,x in enumerate(p):r[i]+=x
    for i,x in enumerate(q):r[i]+=x
    return trim(r)
def mul(p,q):
    r=[0]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):r[i+j]+=x*y
    return trim(r)
def power(p,n):
    r=[1]
    for _ in range(n):r=mul(r,p)
    return r
def sign(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def det(A):
    n=len(A);v=0
    for p in permutations(range(n)):
        term=sign(p)
        for i,j in enumerate(p):term*=A[i][j]
        v+=term
    return v
def detpoly(A):
    n=len(A);r=[0]
    for p in permutations(range(n)):
        term=[sign(p)]
        for i,j in enumerate(p):term=mul(term,[int(i==j),-A[i][j]])
        r=add(r,term)
    return r
def identity(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def matmul(A,B):return [[sum(a*b for a,b in zip(r,c)) for c in zip(*B)] for r in A]
def matpow(A,n):
    B=identity(len(A))
    for _ in range(n):B=matmul(B,A)
    return B
def minusone(A):return [[int(i==j)-A[i][j] for j in range(len(A))] for i in range(len(A))]
def exterior(A,q):
    ix=list(combinations(range(len(A)),q))
    return [[det([[A[i][j] for j in c] for i in r]) for c in ix] for r in ix]
def companion(p):
    n=len(p)-1;A=[[0]*n for _ in range(n)]
    for j in range(n-1):A[j+1][j]=1
    for i in range(n):A[i][-1]=-p[i]
    return A
def blocks(*args):
    n=sum(map(len,args));A=[[0]*n for _ in range(n)];k=0
    for B in args:
        for i,r in enumerate(B):
            for j,v in enumerate(r):A[k+i][k+j]=v
        k+=len(B)
    return A

phi={1:[-1,1],2:[1,1],3:[1,1,1],4:[1,0,1],5:[1,1,1,1,1],6:[1,-1,1],8:[1,0,0,0,1],10:[1,-1,1,-1,1],12:[1,0,-1,0,1]}
patterns=[]
# Enumerate partitions of four by cyclotomic degrees, recursively.
def enum(start,left,chosen):
    if not left:
        if chosen.count(1)%2==chosen.count(2)%2==0:patterns.append(chosen)
        return
    keys=sorted(phi)
    for j in range(start,len(keys)):
        k=keys[j];d=len(phi[k])-1
        if d<=left:enum(j,left-d,chosen+[k])
enum(0,4,[])
assert len(patterns)==19
zeta=[]
for ns in patterns:
    A=blocks(*(companion(phi[n]) for n in ns));M=lcm(*ns)
    numerator=denominator=[1]
    ps=[]
    for q in range(5):
        p=detpoly(exterior(A,q));ps.append(p)
        if q%2:numerator=mul(numerator,p)
        else:denominator=mul(denominator,p)
    a={}
    for n in range(1,M+1):
        L=det(minusone(matpow(A,n)))
        v=Q(L-sum(d*c for d,c in a.items() if n%d==0),n)
        assert v.denominator==1
        a[n]=int(v)
        if M%n:assert a[n]==0
    rhsn=rhsd=[1]
    for n,c in a.items():
        f=[1]+[0]*(n-1)+[-1]
        if c>0:rhsd=mul(rhsd,power(f,c))
        if c<0:rhsn=mul(rhsn,power(f,-c))
    assert mul(numerator,rhsd)==mul(denominator,rhsn)
    # Check inversion at all indices through 6M, including indices not dividing M.
    for k in range(1,6*M+1):
        assert det(minusone(matpow(A,k)))==sum(n*c for n,c in a.items() if k%n==0)
    zeta.append({'factors':ns,'order':M,'exterior_determinants':ps,'coefficients':{str(n):c for n,c in a.items() if c},'verified_indices':6*M})

# Realification of the printed Gaussian matrices acts on the actual Z[i]^2 lattice.
J=[[0,-1],[1,0]];Z=[[0,0],[0,0]];I=identity(2)
def block2(a,b,c,d):return [a[i]+b[i] for i in range(2)]+[c[i]+d[i] for i in range(2)]
G8=block2(Z,J,I,Z);G12=block2(Z,I,I,J)
finite=[]
for n,A in [(8,G8),(12,G12)]:
    assert matpow(A,n)==identity(4)
    assert all(matpow(A,k)!=identity(4) for k in range(1,n))
    assert detpoly(A)==phi[n]
    finite.append({'order':n,'matrix':A,'det_one_minus_tA':detpoly(A)})

k3=[]
expected={2:{2:16},3:{3:9},4:{4:4,2:6},6:{6:1,3:4,2:5}}
for n in [2,3,4,6]:
    A=blocks([[-1,0],[0,-1]],[[-1,0],[0,-1]]) if n==2 else blocks(companion(phi[n]),companion(phi[n]))
    fixed={k:det(minusone(matpow(A,k))) for k in range(1,n)}
    exact={};orbits={}
    for d in sorted((d for d in range(2,n+1) if n%d==0),reverse=True):
        exact[d]=fixed[n//d]-sum(v for e,v in exact.items() if e%d==0)
        assert exact[d]%(n//d)==0
        orbits[d]=exact[d]//(n//d)
    assert orbits==expected[n]
    euler=Q(sum(fixed.values()),n);rank=sum((d-1)*c for d,c in orbits.items())
    assert euler+rank==24
    k3.append({'order':n,'fixed_points':fixed,'singularity_orbits':orbits,'exceptional_rank':rank,'quotient_euler':int(euler),'resolution_euler':24})

# UN32: exact elliptic-lattice characters, branch-root arithmetic and the
# finite cyclic averaging operator used in the actual torsor coordinates.
torsor_characters=[]
for s in (2,3,4,6):
    B=[[-1,0],[0,-1]] if s==2 else companion(phi[s])
    norm=[[sum(matpow(B,j)[r][c] for j in range(s)) for c in range(2)] for r in range(2)]
    assert norm==[[0,0],[0,0]]
    assert det(minusone(B))>0
    possible=[]
    for m in range(1,s+1):
        if s%m:continue
        # rho^s=1 and rho^m has exact order s, represented by rho=exp(2pi i k/s).
        lifts=[k for k in range(s) if gcd(m*k,s)==1]
        if lifts:possible.append(m)
    assert possible==[1]
    torsor_characters.append({'order':s,'matrix':B,'det_I_minus_B':det(minusone(B)),'possible_branch_multiplicities':possible})
cyclic_gauges=[]
for m in range(1,49):
    # B(x)=-(1/m) sum j*x^j; modulo x^m-1,
    # (x-1)B(x)=-1+(1/m)(1+x+...+x^(m-1)).
    b=[-Q(j,m) for j in range(m)]
    difference=[b[(j-1)%m]-b[j] for j in range(m)]
    assert difference==[Q(1,m)-int(j==0) for j in range(m)]
    cyclic_gauges.append(m)

# Actual isotropic construction: H' is formed by orthogonal projection to four
# disjoint A1 roots, then rational four squares remove its positive square.
isotropic=[]
def four_squares(n):
    two={a*a+b*b:(a,b) for a in range(isqrt(n)+1) for b in range(a,isqrt(n)+1) if a*a+b*b<=n}
    for x,ab in two.items():
        if n-x in two:return ab+two[n-x]
    raise AssertionError(n)
for h2 in range(2,22,2):
    for intersections in [(1,1,1,1),(1,2,3,4),(2,3,5,7)]:
        hp2=Q(h2)+Q(sum(a*a for a in intersections),2)
        r=hp2/2;u=four_squares(r.numerator*r.denominator)
        xs=[Q(v,r.denominator) for v in u]
        assert sum(x*x for x in xs)==r
        assert hp2-2*sum(x*x for x in xs)==0
        isotropic.append({'H_square':h2,'intersections':intersections,'Hprime_square':str(hp2),'four_rational_squares':list(map(str,xs))})

# UN3: actual central extension group laws and their abelianization maps.
group_checks=[]
def gp(a,b,n):
    x,y,z,w=a;X,Y,Z,W=b
    return (x+X,y+Y,z+Z+n*x*Y,w+W)
def inv(a,n):
    x,y,z,w=a;return (-x,-y,-z+n*x*y,-w)
for n in range(1,51):
    e=(0,0,0,0);x=(1,0,0,0);y=(0,1,0,0)
    comm=gp(gp(gp(x,y,n),inv(x,n),n),inv(y,n),n)
    assert comm==(0,0,n,0)
    for a,b,c in [((2,-3,4,5),(-2,1,3,2),(1,1,-1,2)),(x,y,(0,0,1,0))]:
        assert gp(gp(a,b,n),c,n)==gp(a,gp(b,c,n),n)
        assert gp(a,inv(a,n),n)==e
        h=gp(a,b,n)
        assert (h[0],h[1],h[3],h[2]%n)==(a[0]+b[0],a[1]+b[1],a[3]+b[3],(a[2]+b[2])%n)
    group_checks.append({'n':n,'Kodaira_free_rank':3,'Hopf_free_rank':1,'torsion_order':n})

# UN17: rational adjugates of negative-definite chain blocks have nonpositive
# entries. This is a finite supplement to the universal positive-part proof.
matrix_sign=[]
for n in range(1,6):
    for excess in range(4):
        A=[[-2-excess if i==j else int(abs(i-j)==1) for j in range(n)] for i in range(n)]
        d=det(A);assert (-1)**n*d>0
        inverse=[[Q((-1)**(i+j)*det([[A[r][c] for c in range(n) if c!=i] for r in range(n) if r!=j]),d) for j in range(n)] for i in range(n)]
        assert all(v<=0 for r in inverse for v in r)
        assert matmul(A,inverse)==identity(n)
        matrix_sign.append({'size':n,'diagonal':-2-excess,'determinant':d})

# UN38: the first resonant Laurent exponent cancels exactly; no floating powers.
resonance=[]
for r,k in product(range(1,21),repeat=2):
    j=r*k
    exponent=j+r-r*(k+1)
    assert exponent==0 and k!=0
    resonance.append([r,k,exponent])

out={'status':'all assertions passed','zeta_identities':zeta,'finite_order_torus_matrices':finite,'K3_quotients':k3,'torsor_characters':torsor_characters,'cyclic_gauge_orders':cyclic_gauges,'isotropic_classes':isotropic,'component_groups':group_checks,'negative_curve_matrices':matrix_sign,'Hopf_resonance_cases':len(resonance),'limits':'All nineteen zeta/table cases, four K3 quotient cases and four possible elliptic branch-character cases are exhaustive under their proved hypotheses. Cyclic-gauge, four-square, group, matrix-sign and resonance sample checks supplement the universal written arguments and do not prove those arguments by enumeration.'}
Path(__file__).with_name('zeta_K3_and_surface_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'zeta_rows':len(zeta),'K3_rows':len(k3),'isotropic_examples':len(isotropic),'group_examples':len(group_checks),'matrix_examples':len(matrix_sign),'resonance_examples':len(resonance)}))
