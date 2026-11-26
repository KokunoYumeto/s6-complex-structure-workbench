#!/usr/bin/env python3
"""Fresh 02JA arithmetic, written after the independent derivation and before
opening any historical maps_exact.py bytes or its outputs.

Method: plain integer/fraction arithmetic; determinant-minor exterior powers;
explicit integer row-space and primitive-image certificates; exhaustive F2
enumeration; sparse polynomial coefficient identities. No source files,
historical programs, computational outputs, SymPy, or network inputs are read.
This is a substep of one targeted proof check, not an additional check event.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from functools import reduce
from math import gcd, lcm

def ident(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]
def trans(A):
    return [list(x) for x in zip(*A)]
def mul(A, B):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def sub(A, B):
    return [[x-y for x,y in zip(r,s)] for r,s in zip(A,B)]
def vec(A, v):
    return [sum(x*y for x,y in zip(r,v)) for r in A]
def det(A):
    n=len(A)
    if n == 0: return 1
    if n == 1: return A[0][0]
    return sum((-1)**j*A[0][j]*det([r[:j]+r[j+1:] for r in A[1:]])
               for j in range(n))
def inv(A):
    d=det(A)
    assert d
    n=len(A)
    return [[Q((-1)**(i+j)*det([r[:i]+r[i+1:] for k,r in enumerate(A) if k != j]),d)
             for j in range(n)] for i in range(n)]
def integral(A):
    assert all(Q(x).denominator == 1 for r in A for x in r)
    return [[int(x) for x in r] for r in A]
def power(A,n):
    B=ident(len(A))
    for _ in range(n): B=mul(B,A)
    return B
def exterior(A,k):
    C=list(combinations(range(len(A)),k))
    return [[det([[A[i][j] for j in cols] for i in rows]) for cols in C] for rows in C]
def stack(A):
    return [r for M in A for r in M]
def unit(n,i):
    return [int(j==i) for j in range(n)]
def f2_fixed(A):
    return [list(v) for v in product((0,1),repeat=len(A[0]))
            if all(x % 2 == 0 for x in vec(A,v))]
def kernel_certificate(name, actions, v):
    """Certify ker_Z A = Z v using Av=0, lambda*v=1 and D(I-v lambda)=B A_R."""
    n=len(v)
    A=stack([sub(M,ident(n)) for M in actions])
    assert vec(A,v)==[0]*len(A)
    li=next(i for i,x in enumerate(v) if abs(x)==1)
    lam=[0]*n
    lam[li]=v[li]
    assert sum(x*y for x,y in zip(lam,v))==1
    P=[[int(i==j)-v[i]*lam[j] for j in range(n)] for i in range(n)]
    witness=None
    for rows in combinations(range(len(A)),n-1):
        R=[A[i] for i in rows]
        for cols in combinations(range(n),n-1):
            S=[[r[j] for j in cols] for r in R]
            if det(S):
                B=mul([[r[j] for j in cols] for r in P],inv(S))
                if mul(B,R)==P:
                    D=lcm(*(Q(x).denominator for r in B for x in r))
                    C=integral([[D*x for x in r] for r in B])
                    assert mul(C,R)==[[D*x for x in r] for r in P]
                    witness=(rows,cols,det(S),D,C)
                    break
        if witness: break
    assert witness is not None
    rows,cols,minor,D,C=witness
    print("KERNEL",name,"basis",v,"lambda",lam)
    print("  selected_rows",list(rows),"selected_columns",list(cols),
          "minor",minor,"D",D,"integer_B",C)
    print("  verified A*v=0; lambda*v=1; D*(I-v*lambda)=B*A_selected")
    return A
def image_certificate(name,A,K):
    """Certify im_Z A=im_Z K, with primitive K: K=AR, A=KC, LK=I."""
    r=len(K[0])
    witness=None
    for rows in combinations(range(len(K)),r):
        S=[K[i] for i in rows]
        if abs(det(S))==1:
            L=[[0]*len(K) for _ in range(r)]
            W=integral(inv(S))
            for i in range(r):
                for j,k in enumerate(rows): L[i][k]=W[i][j]
            assert mul(L,K)==ident(r)
            C=mul(L,A)
            assert mul(K,C)==A
            lifts=[]
            for j in range(r):
                lift=next((list(x) for x in product(range(-2,3),repeat=len(A[0]))
                           if vec(C,x)==unit(r,j)),None)
                assert lift is not None
                lifts.append(lift)
            R=trans(lifts)
            assert mul(A,R)==K
            witness=(L,C,R)
            break
    assert witness is not None
    L,C,R=witness
    print("IMAGE",name,"K",K,"left_inverse",L,"column_coefficients",C,"lifts",R)
    print("  verified L*K=I, A=K*C, K=A*R")
def exact_order(name,A,n):
    assert power(A,n)==ident(len(A))
    proper=[d for d in range(1,n) if n%d==0]
    assert all(power(A,d)!=ident(len(A)) for d in proper)
    print("ORDER",name,n,"proper_divisors_excluded",proper)

I=ident(4)
O1=[[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]]
O2=[[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]]
Oinf=integral(inv(mul(O1,O2)))
G=[[-2,1,0,1],[-6,0,-1,0],[0,-1,0,0],[-1,0,0,0]]
V0=[[1,-1,0,2],[0,-1,-1,6],[0,1,0,0],[0,0,0,1]]
V1=[[1,0,1,-3],[0,0,1,0],[0,-1,0,6],[0,0,0,1]]
Vinf=[[1,0,0,1],[0,1,1,0],[0,0,1,0],[0,0,0,1]]
Tstar=[[1,0,-2,-1],[0,0,-1,0],[0,1,0,-1],[0,0,0,1]]
T1=[[1,0,2,2],[0,1,1,1],[0,0,1,0],[0,0,0,1]]
T2=[[1,0,0,0],[0,1,0,0],[0,-1,1,0],[0,0,0,1]]
T3=[[1,0,0,-1],[0,1,1,0],[0,0,1,0],[0,0,0,1]]
T=[Tstar,T1,T2,T3]
H=[
 [[1,0,0,0],[-2,0,-1,0],[0,1,0,0],[1,1,0,1]],
 [[1,0,0,0],[0,1,0,0],[-2,-1,1,0],[-2,-1,0,1]],
 [[1,0,0,0],[0,1,1,0],[0,0,1,0],[0,0,0,1]],
 [[1,0,0,0],[0,1,0,0],[0,-1,1,0],[1,0,0,1]]]
R0=[[-1,-1,-1,0],[2,1,1,0],[0,0,1,0],[0,0,0,1]]
R1=[[1,1,0,1],[-2,0,-1,-1],[0,-1,1,-1],[0,0,0,1]]
Rinf=[[1,0,0,-1],[-2,0,-1,1],[2,1,2,1],[0,0,0,1]]

assert det(G)==-1
for a,b in zip([O1,O2,Oinf],[V0,V1,Vinf]):
    assert mul(G,a)==mul(b,G)
assert mul(mul(V0,V1),Vinf)==I
assert mul(mul(Rinf,R1),R0)==I
assert reduce(mul,T,I)==I
assert all(H[i]==integral(trans(inv(T[i]))) for i in range(4))
assert all(det(A)==1 for A in [O1,O2,Oinf,V0,V1,Vinf,R0,R1,Rinf]+H)
print("CONJUGACY det(G)=-1; G*O_i=V_i*G for all three returns; all product identities and det(A)=1 verified")
print("DUALITY all printed H_i=(T_i^-1)^t verified; geometric period returns H_i^-1 have pullbacks T_i")
exact_order("original finite 1",O1,3)
exact_order("original finite 2",O2,4)
exact_order("two-parameter finite",H[0],4)
exact_order("LR finite 0",R0,4)
exact_order("LR finite 1",R1,6)

e4=unit(4,3)
eps=[1,2,-4,0]; ep=[1,3,-3,0]
delta=unit(4,0); u0=[0,2,2,1]; u1=[0,3,3,1]
assert vec(G,e4)==delta
assert vec(G,eps)==[-x for x in u0]
assert vec(G,ep)==[delta[i]-u1[i] for i in range(4)]
assert vec(V0,u0)==u0 and vec(V1,u1)==u1
assert trans(G)[0][3]==-1 and G[3]==[-1,0,0,0]
ell=[1,-1,-1,0]
assert vec(H[0],ell)==ell and ell[0]==1
assert vec(R0,e4)==e4 and e4[3]==1
print("TRANSLATIONS G*d=delta; G*epsilon=-u0; G*epsilon'=delta-u1; psi*G=-gamma")
print("  coefficient certificates G*(N0*epsilon-rho0*d)=-(rho0*delta+N0*u0)")
print("  G*(N1*epsilon'-(rho1+N1)*d)=-(rho1*delta+N1*u1)")
print("  Hstar*ell=ell, psi(ell)=1; R0*e4=e4, xi(e4)=1")

systems=[
 ("original",[O1,O2,Oinf],[trans(A) for A in [O1,O2,Oinf]],e4,unit(4,0),unit(4,0)),
 ("two-parameter",H,T,e4,unit(4,0),unit(4,0)),
 ("LR",[R0,R1,Rinf],[trans(A) for A in [R0,R1,Rinf]],[-1,0,2,0],e4,[0,2,0,-1]),
 ("logarithmic",[V0,V1,Vinf],[trans(A) for A in [V0,V1,Vinf]],delta,e4,e4)]
for name,hom,coh,vh,vc,v3 in systems:
    Ah=kernel_certificate(name+" homology",hom,vh)
    Ac=kernel_certificate(name+" cohomology",coh,vc)
    found=f2_fixed(Ac)
    expected=[[0]*4,[x%2 for x in vc]]
    assert sorted(found)==sorted(expected)
    print("F2",name,"cohomology_all_16_vectors_checked",found,
          "homology_fixed_vectors",f2_fixed(Ah))
    W=[exterior(C,3) for C in coh]
    kernel_certificate(name+" exterior_cube",W,v3)
    print("WEDGE3",name,"first_two_minor_matrices",W[:2])
Kcoord=trans([unit(4,2),unit(4,3)])
image_certificate("two-parameter K1",sub(H[1],I),trans([[0,0,1,1]]))
image_certificate("two-parameter K2",sub(H[2],I),trans([[0,1,0,0]]))
image_certificate("two-parameter K3",sub(H[3],I),Kcoord)
image_certificate("original cusp",sub(Oinf,I),Kcoord)
image_certificate("LR cusp",sub(Rinf,I),trans([[1,-1,-1,0],[-1,0,2,0]]))
image_certificate("logarithmic cusp",sub(Vinf,I),trans([delta,unit(4,1)]))
for i in [1,2,3]:
    assert mul(sub(H[i],I),sub(H[i],I))==[[0]*4 for _ in range(4)]
print("NILPOTENCE all three two-parameter reduced (H_i-I)^2=0; ranks 1,1,2 by image certificates")
v=[1,-1,-1,0]; d=[-1,0,2,0]
assert vec(R1,v)==[0,-1,0,0]
Lcols=trans([v,d,[0,-1,0,0]])
assert abs(det(Lcols[:3]))==1 and Lcols[3]==[0,0,0]
print("LR LATTICE R1*(e1-e2-e3)=-e2; cusp vectors plus this image span ker(xi) integrally")

P2=[[0,-1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]]
Nlog=[[0,0,0,1],[0,0,1,0],[1,0,0,0],[0,1,0,0]]
Plog=[[0,-1,0,0],[-1,0,0,0],[0,6,-1,0],[1,-2,0,1]]
assert mul(G,Plog)==Nlog
J2=[[0,-1],[1,0]]; Jlr=[[0,1],[1,0]]; Jlog=[[0,-1],[-1,0]]
assert det(P2)==1 and det(Plog)==1
assert [det(J) for J in [J2,Jlr,Jlog]]==[1,-1,-1]
for V in [[[0,1,0],[0,0,1],[1,1,1]],[[0,1,0],[0,1,1],[1,1,1]]]:
    assert det(V)==1
print("MARKINGS P2 det=1; G*Plog=Nlog, det(Plog)=1; long degrees [1,-1,-1]")
print("RAY_DISCS both displayed three-column winding matrices have determinant +1")

# Sparse polynomial certificates in variables m0,m1,N0,N1.
def pol(c=0): return {(0,0,0,0):c} if c else {}
def var(i):
    a=[0]*4; a[i]=1
    return {tuple(a):1}
def add(a,b):
    c=dict(a)
    for k,v in b.items():
        c[k]=c.get(k,0)+v
        if c[k]==0: del c[k]
    return c
def neg(a): return {k:-v for k,v in a.items()}
def pmul(a,b):
    c={}
    for x,v in a.items():
        for y,w in b.items():
            k=tuple(i+j for i,j in zip(x,y))
            c[k]=c.get(k,0)+v*w
    return {k:v for k,v in c.items() if v}
def pmm(A,B):
    return [[reduce(add,(pmul(x,y) for x,y in zip(row,col)),{})
             for col in zip(*B)] for row in A]
m0,m1,n0,n1=[var(i) for i in range(4)]
b=add(pmul(m1,n0),pmul(m0,n1))
Mer=[[m0,neg(m1)],[neg(n0),neg(n1)]]
Adj=[[n1,neg(m1)],[neg(n0),neg(m0)]]
B=[[pmul(b,x) for x in row] for row in Adj]
detMer=add(pmul(Mer[0][0],Mer[1][1]),neg(pmul(Mer[0][1],Mer[1][0])))
assert detMer==neg(b)
b2=pmul(b,b)
assert pmm(Mer,B)==[[b2,{}],[{},b2]]
phase=pmm([[m0,neg(m1)]],B)
assert phase==[[b2,{}]]
print("MERIDIANS det([[m0,-m1],[-N0,-N1]])=-(m1*N0+m0*N1), coefficient dictionary",detMer)
print("  exact polynomial identities Mer*B=b^2*I; (m0,-m1)*B=(b^2,0)")
print("  on the stated b=+-1 domain B gives x=b(N1*mu0-N0*mu1), h=-b(m1*mu0+m0*mu1)")
assert 3*4==12 and 4%2==0 and 12%2==0
print("DEGREES the single-multiple target factor has degree 4; (3k)(4l)=12kl, both even")
print("ALL ASSERTIONS PASSED; all displayed certificates were checked by exact arithmetic.")
