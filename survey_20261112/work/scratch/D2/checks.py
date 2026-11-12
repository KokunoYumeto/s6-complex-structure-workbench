from fractions import Fraction as Fr
from math import log, sqrt, pi, sin
import itertools
F = lambda a,q,n: a*a-3*q*q-18*n*n
# local counts
def N(p,k):
    M=p**k; c=0
    sq=[(x*x)%M for x in range(M)]
    from collections import Counter
    ca=Counter(sq)
    for q in range(M):
        for n in range(M):
            c+=ca[(-2+3*sq[q]+18*sq[n])%M]
    return c
for p,k,exp in [(2,4,3*2**7),(2,5,3*2**9),(2,6,3*2**11),(3,1,2*9),(3,2,2*81),(3,3,2*729)]:
    print("N",p,k,N(p,k),"expected",exp)
for p in (5,7,11,13):
    leg = 1 if pow(3,(p-1)//2,p)==1 else -1
    # density at k=1 : N/p^2 should be (1 - p^-2)/(1 - leg/p)?? good prime: N_{p,1}=p^2+leg*p  => sigma = 1+leg/p ; compare with formula
    print("p",p,"N1",N(p,1),"p^2+chi p",p*p+leg*p, "formula sigma",(1-p**-2)/(1-leg/p),"1+chi/p",1+leg/p)
# 2-adic toggle matrix
g=[[Fr(-19,17),0,Fr(-36,17)],[0,1,0],[Fr(-2,17),0,Fr(-19,17)]]
A=[[1,0,0],[0,-3,0],[0,0,-18]]
gt=[[g[j][i] for j in range(3)] for i in range(3)]
mul=lambda X,Y:[[sum(X[i][k]*Y[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
print("g^T A g == A:", mul(mul(gt,A),g)==[[Fr(x) for x in r] for r in A])
det=lambda m: m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])-m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])+m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0])
print("det g", det(g))
# archimedean integral
import numpy as np
th=np.linspace(0,pi/2,2000001); f=1/(4+17/(3*sqrt(2))*np.sin(th)); I=np.trapezoid(f,th)/(6*sqrt(6))
print("I_inf numeric",I,"closed", log(3/(2*sqrt(2)))/(2*sqrt(3)))
S=4.5*log(2+sqrt(3))/sqrt(3)/(pi*pi/6)
print("S", S, "S*I", S*log(3/(2*sqrt(2)))/(2*sqrt(3)), "C0", 9/(2*pi**2)*log(2+sqrt(3))*log(3/(2*sqrt(2))))
# height vector: 4a+17n = <v,w>/18 with w=(72,0,-17), F(w)=-18 ; z-slicing identity 2*Delta = s^2-3t^2-18z^2
print("F(72,0,-17) =",F(72,0,-17))
import random
for _ in range(1000):
    x,y,z=[random.randint(-50,50) for _ in range(3)]
    D=4*(x*y+x*z+y*z)-(x*x+y*y+z*z)
    s=x+y+4*z;t=y-x
    assert 2*D==s*s-3*t*t-18*z*z
    n=z-4*(x+y);q=y-x;a=x+y-4*n
    assert 2*D==F(a,q,n) and z==4*a+17*n and s==17*a+72*n
print("identities ok: 2Delta = s^2-3t^2-18z^2 with s=x+y+4z=17a+72n, t=y-x=q, z=4a+17n")
# rational (non)equivalence remark: t*rho-6m^2 isotropic over Q, Delta anisotropic (mod 3 descent) -- small search
found=[(x,y,z) for x in range(-30,31) for y in range(-30,31) for z in range(-30,31) if (x,y,z)!=(0,0,0) and 4*(x*y+x*z+y*z)-(x*x+y*y+z*z)==0]
print("nonzero integer zeros of Delta in box 30:", len(found))
# first reduced roots by brute force in original coords
roots=[]
for z in range(1,140):
    for x in range(1,z):
        for y in range(x,z):
            if 4*(x+y)<=z and 4*(x*y+x*z+y*z)-(x*x+y*y+z*z)==-1: roots.append((x,y,z))
print(roots)
# Frobenius-norm identity of the quaternion bridge
r2=sqrt(2)
for (a,q,n) in [(5,3,0),(4,0,1),(1,1,0),(41,23,2)]:
    if F(a,q,n)!=-2: print("not on shell",a,q,n); continue
    M=np.array([[2+1.5*r2*q, 3*a+9*r2*n],[-0.5*a+1.5*r2*n, 2-1.5*r2*q]])
    print((a,q,n),"det",round(np.linalg.det(M),9),"Frob^2",(M**2).sum(),"14+(7a+15sqrt2 n)^2/4",14+(7*a+15*r2*n)**2/4)
