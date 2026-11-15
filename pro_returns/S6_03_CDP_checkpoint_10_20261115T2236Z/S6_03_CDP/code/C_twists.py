"""Exact weighted-line and local-complex checks for C.5."""
import sympy as S
from sympy.matrices.normalforms import smith_normal_form
s=S.symbols('s')
R=S.QQ.poly_ring(s)

def degree(n): return (n-4*(n%3)-3*((3*n)%4))//12
def u(n): return max(degree(n)+1,0)
def v(n): return max(-degree(n)-1,0)
def monomials(n): return sum((n-3*a)%4==0 for a in range(n//3+1)) if n>=0 else 0
def dims(n):
    return (u(n)+u(n-1),v(n)+v(n-1)+u(n)+u(n-1)+u(n+2),
            v(n)+v(n-1)+v(n+2)+u(n+6)+(n%3!=0),v(n+6))
for n in range(-240,241):
    assert u(n)==monomials(n)
    assert v(n)==monomials(-n-7)
    h=dims(n)
    assert h[0]-h[1]+h[2]-h[3]==1
print('481 exact weighted cohomology/monomial/index comparisons passed')
for n in range(-12,13):
    print('n',n,'h(T tensor M_n)',dims(n),'h3(logT)',v(n-6),
          'normalization map rank',int(u(n+6)>0))

def complex_matrices(a1,a2,K):
    k11,k12,k21,k22=K[0,0],K[0,1],K[1,0],K[1,1]
    d0=S.Matrix([[a1,0,k11],[a2,0,k12],[0,a1,k21],[0,a2,k22],[0,0,a1],[0,0,a2]])
    d1=S.Matrix([[-a2,a1,0,0,-k12,k11],[0,0,-a2,a1,-k22,k21],[0,0,0,0,-a2,a1]])
    return d0,d1
def jet_matrix(A,N):
    B=S.zeros(A.rows*N,A.cols*N)
    for i in range(A.rows):
        for j in range(A.cols):
            p=S.Poly(A[i,j],s)
            for k in range(N):
                for (power,),coeff in p.terms():
                    if k+power<N: B[i*N+k+power,j*N+k]+=coeff
    return B

for name,a2,K in [('regular',s,S.Matrix([[0,1],[1,0]])),
                  ('order_three',s*s,S.Matrix([[0,s],[s,1]]))]:
    d0,d1=complex_matrices(0,a2,K)
    assert d1*d0==S.zeros(3,3)
    # Polynomial cycles u=e1*g2,w=e2*g2,v=e2*g1+(a2/K21)*h*g2.
    cycles=S.zeros(6,3)
    cycles[1,0]=1; cycles[3,1]=1; cycles[2,2]=1; cycles[5,2]=a2/K[1,0]
    P=S.Matrix([[a2,0,K[0,1]],[0,a2,K[1,1]],[0,0,K[1,0]]])
    assert d1*cycles==S.zeros(3,3) and cycles*P==d0
    print(name,'H1 presentation Smith =',smith_normal_form(P,domain=R))
    print(name,'H2 presentation Smith =',smith_normal_form(d1,domain=R))
    N=8
    j0,j1=jet_matrix(d0,N),jet_matrix(d1,N)
    assert j1*j0==S.zeros(3*N,3*N)
    r0,r1=j0.rank(),j1.rank()
    print(name,'independent length-eight jet cohomology =',(3*N-r0,6*N-r0-r1,3*N-r1))

for n in range(12):
    count=lambda m,l,w:sum(j%m==w%m for j in range(l))
    Q=count(3,2,n-1)
    H1_3=count(3,2,n+2)+count(3,3,n+2)
    H2_3=count(3,2,n+2)+count(3,3,n)
    H1_4=count(4,1,3*n+1)+count(4,1,3*n+2)
    H2_4=count(4,2,3*n+2)
    assert Q==(n%3!=0)
    assert H1_3==H2_3==1+(n%3!=0)
    assert H1_4==H2_4==int(n%4 in (1,2))
    print('n residue',n,'integral Q',Q,'nonintegral root lengths',H1_3,H1_4)
n,k=S.symbols('n k')
ell1=S.Matrix([[n,-2*k,-k,-3*k]])
ell2=S.Matrix([[n,-k,-k,-2*k]])
print('order-three affine character numerator =',(ell1*S.Matrix([1,2,-4,0]))[0])
print('order-four affine character numerator =',(ell2*S.Matrix([-1,-3,3,0]))[0])
print('joint transverse coefficient / (i*k/pi) =',S.Rational(123,64))
