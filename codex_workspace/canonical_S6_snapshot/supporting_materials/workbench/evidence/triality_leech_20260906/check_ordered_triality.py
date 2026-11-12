"""Exact independent Cayley--Dickson checks for STAGED.tex (no packages)."""
from fractions import Fraction as F
from itertools import product
import json

Z = (0,) * 8
E = [tuple(int(i == j) for i in range(8)) for j in range(8)]

def add(a, b): return tuple(x + y for x, y in zip(a, b))
def neg(a): return tuple(-x for x in a)
def scale(a, r): return tuple(r * x for x in a)
def conj(a): return (a[0],) + tuple(-x for x in a[1:])
def dot(a, b): return sum(x*y for x, y in zip(a, b))
def qm(a, b):
    w,x,y,z = a; t,u,v,s = b
    return (w*t-x*u-y*v-z*s, w*u+x*t+y*s-z*v,
            w*v-x*s+y*t+z*u, w*s+x*v-y*u+z*t)
def qc(a): return (a[0], -a[1], -a[2], -a[3])
def mul(x,y):
    a,b=x[:4],x[4:]; c,d=y[:4],y[4:]
    return add(qm(a,c), neg(qm(qc(d),b))) + add(qm(d,a),qm(b,qc(c)))
def mu(a,b): return conj(mul(a,b))
def tau(a,b,c): return mul(mul(a,b),c)[0]
def C(a,bc):
    b,c=bc
    return neg(mu(c,a)),mu(a,b)
def pairadd(u,v): return add(u[0],v[0]),add(u[1],v[1])
def pairscale(u,r): return scale(u[0],r),scale(u[1],r)

def matrix(diag=(0,0,0),q=(Z,Z,Z)):
    a,b,c=map(lambda r:scale(E[0],r),diag)
    x,y,z=q
    return [[a,z,conj(y)],[conj(z),b,x],[y,conj(x),c]]
def mm(a,b):
    return [[tuple(sum(mul(a[i][k],b[k][j])[r] for k in range(3))
                   for r in range(8)) for j in range(3)] for i in range(3)]
def jordan(a,b):
    ab,ba=mm(a,b),mm(b,a)
    return [[scale(add(ab[i][j],ba[i][j]),F(1,2)) for j in range(3)] for i in range(3)]
def tr(a): return sum(a[i][i][0] for i in range(3))
def det_trace(a):
    a2=jordan(a,a); a3=jordan(a,a2)
    return tr(a3)/3-tr(a2)*tr(a)/2+tr(a)**3/F(6)
def peirce(i,a):
    q=[Z,Z,Z]; q[i]=a
    return matrix(q=q)
def mscale(a,r): return [[scale(x,r) for x in row] for row in a]
def msum(a,b): return [[add(a[i][j],b[i][j]) for j in range(3)] for i in range(3)]

counts={}
for i,a,b in product(range(3),E,E):
    assert jordan(peirce(i,a),peirce((i+1)%3,b)) == mscale(peirce((i+2)%3,mu(a,b)),F(1,2))
counts['cyclic_peirce_products']=3*8**2
for a,b,c in product(E,E,E):
    assert tau(a,b,c)==tau(b,c,a)==tau(c,a,b)==dot(mu(a,b),c)
    assert tr(jordan(jordan(peirce(0,a),peirce(1,b)),peirce(2,c)))==tau(a,b,c)
counts['tensor_basis_triples']=8**3
SB=[(b,Z) for b in E]+[(Z,c) for c in E]
for a,b,s in product(E,E,SB):
    assert pairadd(C(a,C(b,s)),C(b,C(a,s))) == pairscale(s,-2*dot(a,b))
counts['clifford_basis_checks']=8**2*16
vol=[]
for s in SB:
    out=s
    for a in reversed(E): out=C(a,out)
    if out==s: vol.append(1)
    elif out==pairscale(s,-1): vol.append(-1)
    else: raise AssertionError('Volume is not scalar on a coordinate basis vector')
counts['volume_eigenvalues_V2_then_V3']=vol

sample=[tuple(((j+3)*(r+1)**2+2*r*j)%11-5 for r in range(8)) for j in range(12)]
for n in range(12):
    a,b,c=sample[n],sample[(n+3)%12],sample[(n+7)%12]
    assert dot(mu(a,b),mu(a,b))==dot(a,a)*dot(b,b)
    assert mu(mu(a,b),a)==scale(b,dot(a,a))
    assert mu(b,mu(a,b))==scale(a,dot(b,b))
    xi=(n-3,2*n+1,5-n)
    x=matrix(xi,(a,b,c))
    expected=xi[0]*xi[1]*xi[2]-sum(xi[i]*dot(q,q) for i,q in enumerate((a,b,c)))+2*tau(a,b,c)
    assert det_trace(x)==expected
    p=[peirce(i,q) for i,q in enumerate((a,b,c))]
    mixed=det_trace(msum(msum(p[0],p[1]),p[2]))
    mixed-=sum(det_trace(msum(p[i],p[j])) for i,j in ((0,1),(0,2),(1,2)))
    mixed+=sum(det_trace(y) for y in p)
    assert mixed==2*tau(a,b,c)
    assert mixed/F(6)==F(1,3)*tau(a,b,c)
counts['dense_integer_samples']=12
print(json.dumps({'status':'PASS','checks':counts},indent=2))
