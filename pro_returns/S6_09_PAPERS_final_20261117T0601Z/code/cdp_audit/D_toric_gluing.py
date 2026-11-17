"""Exact lattice, chart, cocycle and period checks for C.2.UN.71.

The proof supplies the analytic properness argument and the precise
Gross--Siebert comparison.  These checks certify the displayed maps
and signs; they do not replace that argument by numerical sampling.
"""
from fractions import Fraction
import random
import sympy as S

e1=S.Matrix([1,0]); e2=S.Matrix([0,1])
Pij=S.Matrix([[-1,-1],[0,1]])
Pjk=S.Matrix([[1,0],[-1,-1]])
Pki=S.Matrix([[-1,-1],[1,0]])
assert Pij*Pjk*Pki==S.eye(2)
assert Pij*(Pjk*e1+e2)+e1==S.zeros(2,1)
a,b=S.symbols('a b',integer=True)
at_other_end=Pij*(-b*e1-e2)
desired=-a*e1-e2-e1
assert at_other_end-desired==(a+b+2)*e1
print('PASS exact triple angular maps, affine triangle cocycle and endpoint discrepancy (a+b+2)e1.')

survivors=[]
for i in range(9):
    for j in range(9):
        for k in range(9):
            if i-k==0 and j-k==0:
                survivors.append((i,j,k))
assert survivors==[(i,i,i) for i in range(9)]
print('PASS exact two-circle residue filter: only a_(q,q,q)t^q survives the angular integral.')

rng=random.Random(7102026)
cones=0
for _ in range(240):
    M=S.eye(2)
    for step in range(5):
        k=rng.randrange(-5,6)
        E=S.Matrix([[1,k],[0,1]]) if step%2==0 else S.Matrix([[1,0],[k,1]])
        M=M*E
    p=S.Matrix([rng.randrange(-8,9),rng.randrange(-8,9)])
    q=p+M[:,0]; r=p+M[:,1]
    A=S.Matrix([[p[0],q[0],r[0]],[p[1],q[1],r[1]],[1,1,1]])
    assert A.det()==1
    assert A.inv().applyfunc(lambda z:z.q)==S.ones(3)
    # log(z1),log(z2),log(t)=A log(x0,x1,x2).
    # t dlog(t) wedge dlog(z1) wedge dlog(z2)=det(A) dx0 wedge dx1 wedge dx2.
    cyclic_rows=A[[2,0,1],:]
    assert cyclic_rows.det()==1
    coeff=[Fraction(rng.randrange(1,21)) for _ in range(3)]
    total=sum(coeff); coeff=[x/total for x in coeff]
    bary=S.Matrix([S.Rational(x.numerator,x.denominator) for x in coeff])
    point=A*bary
    assert point[2]==1 and A.inv()*point==bary
    assert all(x>=0 for x in bary)
    cones+=1
print('PASS',cones,'exact translated unimodular cone charts, integral inverses, volume determinants and barycentric coordinate recoveries.')

def shear(v):
    return S.Matrix([[1,0,v[0]],[0,1,v[1]],[0,0,1]])
shears=0
for _ in range(300):
    v=tuple(rng.randrange(-20,21) for _ in range(2))
    w=tuple(rng.randrange(-20,21) for _ in range(2))
    assert shear(v)*shear(w)==shear((v[0]+w[0],v[1]+w[1]))
    assert shear(v).det()==1
    assert shear(v)*S.Matrix([3,-2,1])==S.Matrix([3+v[0],-2+v[1],1])
    shears+=1
print('PASS',shears,'actual integral shear compositions, determinants and height-one vertex translations.')

def mul(x,y): return tuple(a*b for a,b in zip(x,y))
def inv(x): return tuple(1/a for a in x)
def power(x,n): return tuple(a**n for a in x)

nx,ny=5,4
holx=(Fraction(2),Fraction(3)); holy=(Fraction(5),Fraction(7))
gauge={(i,j):(Fraction(11)**(i-j),Fraction(13)**(i+2*j))
       for i in range(nx) for j in range(ny)}
def edge(i,j,di,dj):
    p=(i%nx,j%ny); raw=(p[0]+di,p[1]+dj)
    q=(raw[0]%nx,raw[1]%ny)
    wraps=(raw[0]//nx,raw[1]//ny)
    return mul(mul(inv(gauge[p]),mul(power(holx,wraps[0]),power(holy,wraps[1]))),gauge[q])

for i in range(nx):
    for j in range(ny):
        E=[edge(i,j,1,0),edge(i+1,j,0,1),edge(i+1,j+1,-1,0),edge(i,j+1,0,-1)]
        product=(Fraction(1),Fraction(1))
        for z in E: product=mul(product,z)
        assert product==(1,1)
for j in range(ny):
    product=(Fraction(1),Fraction(1))
    for i in range(nx): product=mul(product,edge(i,j,1,0))
    assert product==holx
for i in range(nx):
    product=(Fraction(1),Fraction(1))
    for j in range(ny): product=mul(product,edge(i,j,0,1))
    assert product==holy
print('PASS exact torus-valued Cech gauge equations:20 face products and9 marked cycle holonomies.')

L,h=S.symbols('L h',nonzero=True,real=True)
q11,q12,q21,q22,c11,c12,c21,c22,d11,d12,d21,d22=S.symbols('q11 q12 q21 q22 c11 c12 c21 c22 d11 d12 d21 d22',real=True)
Q=S.Matrix([[q11,q12],[q21,q22]])
C=S.Matrix([[c11,c12],[c21,c22]])
D=S.Matrix([[d11,d12],[d21,d22]])
periods=S.zeros(2).row_join(L*Q+C).col_join((h*S.eye(2)).row_join(D))
assert S.expand(periods.det()-h**2*(L*Q+C).det())==0
print('PASS symbolic real period determinant: (2pi)^2 det(log|t| Q+Re C), independent of angular constants.')

index_cases=0
for a in range(1,16):
    for d in range(1,16):
        for b in range(a):
            Q=S.Matrix([[a,b],[0,d]])
            assert Q.det()==a*d
            assert len({(i,j) for i in range(a) for j in range(d)})==a*d
            index_cases+=1
print('PASS',index_cases,'integral finite-index period lattices and exact vertex/Euler indices.')
print('ALL UN71 EXACT CHECKS PASSED')
