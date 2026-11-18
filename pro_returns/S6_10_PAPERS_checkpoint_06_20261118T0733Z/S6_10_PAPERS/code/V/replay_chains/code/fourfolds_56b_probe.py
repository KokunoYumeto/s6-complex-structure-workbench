"""Exact first integral probe of the geometric (5,6) quotient.

The finite extension equations are solved over Z by Smith reduction.
Only the printed finite combinations are tested for a primitive cusp;
failure of that sample would not be an impossibility proof.
"""
from sympy import Matrix, eye, zeros, symbols, Poly, ZZ, factor
from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from itertools import combinations, product

def snf(R):
    return tuple(T.to_Matrix() for T in smith_normal_decomp(
        DomainMatrix.from_Matrix(R).convert_to(ZZ)))
def kernel(R):
    D,U,V=snf(R)
    K=V[:,R.rank():]
    assert R*K==zeros(R.rows,K.cols)
    return K
def factors(R):
    D=smith_normal_form(R,domain=ZZ)
    return [abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
def ext(T,q):
    inds=list(combinations(range(T.rows),q))
    return Matrix([[T.extract(i,j).det() for j in inds] for i in inds])
def companion(poly):
    p=Poly(poly,t);n=p.degree();T=zeros(n)
    for i in range(n-1):T[i+1,i]=1
    for i in range(n):T[i,n-1]=-p.nth(i)
    return T

t=symbols('t')
F=companion(t**4+t**3+t**2+t+1)
G=companion(t**4+t**2+1)
assert F**10==eye(4) and G**12==eye(4)
assert (F.inv()*G-eye(4)).rank()==1
assert (F.inv()*G-eye(4))**2==zeros(4)
WA,WB=ext(F.inv(),2),ext(G,2)
om=kernel(Matrix.vstack(WA-eye(6),WB-eye(6)))
assert om.cols==1
D,U,V=snf(om)
assert abs(D[0,0])==1
Q=U.inv();Q[:,0]*=D[0,0]
assert Q[:,0]==om[:,0] and abs(Q.det())==1
AA=Q.inv()*WA*Q;BB=Q.inv()*WB*Q
A0=AA[1:,1:];B0=BB[1:,1:]
assert A0**5==eye(5) and B0**6==eye(5)
assert factor(A0.charpoly(t).as_expr())==(t-1)*(t**4+t**3+t**2+t+1)
assert factor(B0.charpoly(t).as_expr())==(t-1)*(t+1)**2*(t*t-t+1)
print('source companions',F,G)
print('omega',om,'quotient marking',Q)
print('rank-five quotient',A0,B0)
assert Matrix.vstack(A0-eye(5),B0-eye(5)).rank()==5
assert Matrix.hstack(A0-eye(5),B0-eye(5)).rank()==5
print('rank-five stacked Smith',factors(Matrix.vstack(A0-eye(5),B0-eye(5))))
print('rank-five horizontal Smith',factors(Matrix.hstack(A0-eye(5),B0-eye(5))))
normA=sum((A0**i for i in range(5)),zeros(5))
normB=sum((B0**i for i in range(6)),zeros(5))
N0=A0*B0-eye(5)
cols=[]
for i in range(10):
    a=zeros(1,5);b=zeros(1,5)
    if i<5:a[0,i]=1
    else:b[0,i-5]=1
    cols.append(Matrix(list(a*normA)+list(b*normB)+list((a*B0+b)*N0)))
equations=Matrix.hstack(*cols)
K=kernel(equations)
assert K.cols==6
print('integral finite/square-zero extension kernel',K)

def matrices(w):
    A=eye(6);B=eye(6)
    A[1:,1:]=A0;B[1:,1:]=B0
    A[0,1:]=w[:5,0].T;B[0,1:]=w[5:,0].T
    return A,B

chosen=None;tested=0
# First test the actual six integral basis columns; then the 3^6 cube.
samples=[K[:,i] for i in range(6)]
samples += [K*Matrix(c) for c in product([-1,0,1],repeat=6)]
for w in samples:
    tested+=1
    A,B=matrices(w);N=A*B-eye(6)
    assert A**5==eye(6) and B**6==eye(6) and N*N==zeros(6)
    if N.rank()==3 and factors(N)==[1,1,1]:
        chosen=(A,B);break
print('tested extension vectors',tested,'of bounded sample',len(samples))
if chosen is None:
    print('No primitive cusp in this finite sample; no impossibility asserted.')
    raise SystemExit
A,B=chosen
print('primitive rank-six extension A=',A,'B=',B)
M1,M2=A.T,B.T;M0=(M1*M2).inv();N=M0-eye(6)
ell=Matrix([[1,0,0,0,0,0]])
twists=[]
for M,m in [(M1,5),(M2,6)]:
    V=kernel(M-eye(6));row=ell*V
    D,U,R=snf(row)
    print('finite invariant lattice',m,V,'ell image gcd',D[0,0])
    if abs(D[0,0])==1:
        v=V*R[:,0]*D[0,0]*U[0,0]
        assert ell*v==Matrix([1]) and M*v==v
        twists.append(v)
        print('ell-one invariant vector',m,list(v))
L=hermite_normal_form(Matrix.hstack(N,M1*N,M2*N))
print('cusp normal closure initial Hermite basis',L)
for q in range(7):
    C,D,E=ext(A,q),ext(B,q),ext(A*B,q);n=C.rows
    a=n-Matrix.vstack(C-eye(n),D-eye(n)).rank()
    b=n-Matrix.hstack(C-eye(n),D-eye(n)).rank()
    local=[n-(T-eye(n)).rank() for T in [C,D,E]]
    h=a+b+n-sum(local)
    print('q',q,'inv,parabolic,coinv',a,h,b,'local',local,
          'coinvariant Smith',factors(Matrix.hstack(C-eye(n),D-eye(n))))
print('All printed extension checks exact; integral total homology is not yet asserted.')

for M,m in [(M1,5),(M2,6)]:
    D=M[1:,1:]
    for q in range(1,5):
        E=ext(D.T,q)
        print('cap vertical degree',q,'multiplicity',m,'Smith',factors(E-eye(E.rows)))
for q in (1,2,3,4):
    C,D=ext(A,q),ext(B,q);n=C.rows
    print('global degree',q,'coboundary Smith',factors(Matrix.vstack(C-eye(n),D-eye(n))))

for (M,m),u,C in zip([(M1,5),(M2,6)],twists,[A,B]):
    D=M[1:,1:]
    lam=Matrix([0]+list(kernel(D-eye(5))[:,0]))
    I2=list(combinations(range(6),2));I3=list(combinations(range(6),3))
    K2=kernel(ext(C,2)-eye(15))
    periods=Matrix([[u[i]*lam[j]-u[j]*lam[i] for i,j in I2]])*K2/m
    print('finite q2 suspension periods',m,list(periods))
    K3=kernel(ext(C,3)-eye(20));J=zeros(20)
    for i,a in enumerate(I3):
        b=tuple(k for k in range(6) if k not in a);j=I3.index(b);ab=a+b
        J[i,j]=(-1)**sum(ab[k]>ab[l] for k in range(6) for l in range(k+1,6))
    print('finite q3 Gram determinant',m,(K3.T*J*K3).det())
