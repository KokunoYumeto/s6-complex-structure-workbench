"""Exact finite verification of the independently proved GL2(3) glue map.

Only 48 GL2(F3) elements are constructed; the supplied original checker
already exhausts the 2304 signed-permutation/GL2(F2) candidates.
"""
from itertools import product
from fractions import Fraction as F

def mm(a,b,p):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b)))%p
                       for j in range(len(b[0]))) for i in range(len(a)))
def mv(a,v,p):
    return tuple(sum(row[k]*v[k] for k in range(len(v)))%p for row in a)
def rowmul(v,a):
    return tuple(sum(v[k]*a[k][j] for k in range(2))%3 for j in range(2))
def mat2(a,b):
    return tuple((a[i],b[i]) for i in range(2))
def tau(u):return ((u[1]+u[3])%2,(u[2]+u[3])%2)
def j(v):
    a,b=v
    return ((a+b)%3,(a+2*b)%3,a,b)

ells=((1,1),(1,2),(1,0),(0,1))
I=((1,0),(0,1))
GL3={((a,b),(c,d)) for a,b,c,d in product(range(3),repeat=4)
     if (a*d-b*c)%3}
GL2={((a,b),(c,d)) for a,b,c,d in product(range(2),repeat=4)
     if (a*d-b*c)%2}
E={u for u in product(range(2),repeat=4) if sum(u)%2==0}
C3={j(v) for v in product(range(3),repeat=2)}
glue={(tuple((3*u[i]+2*z[i])%6 for i in range(4)),tau(u))
      for u in E for z in C3}

def lift(A):
    signs=[];perm=[]
    for ell in ells:
        target=rowmul(ell,A)
        options=[(sign,k) for sign in (1,-1) for k,other in enumerate(ells)
                 if tuple(sign*t%3 for t in other)==target]
        assert len(options)==1
        sign,k=options[0];signs.append(sign);perm.append(k)
    assert len(set(perm))==4
    b1=tau(tuple((1,1,0,0)[k] for k in perm))
    b2=tau(tuple((1,0,1,0)[k] for k in perm))
    return tuple(signs),tuple(perm),mat2(b1,b2)

lifts={A:lift(A) for A in GL3}
assert len(set(lifts.values()))==48
for A,(signs,perm,B) in lifts.items():
    assert B in GL2
    for u in E: assert tau(tuple(u[k] for k in perm))==mv(B,tau(u),2)
    for v in product(range(3),repeat=2):
        assert tuple(signs[i]*j(v)[perm[i]]%3 for i in range(4))==j(mv(A,v,3))
    image={(tuple(signs[i]*x[perm[i]]%6 for i in range(4)),mv(B,y,2))
           for x,y in glue}
    assert image==glue
assert {lift(A)[2] for A in GL3}==GL2
for A in GL3:
    for C in GL3:
        sa,pa,Ba=lift(A);sc,pc,Bc=lift(C)
        composite=(tuple(sa[i]*sc[pa[i]] for i in range(4)),
                   tuple(pc[pa[i]] for i in range(4)),mm(Ba,Bc,2))
        assert lift(mm(A,C,3))==composite
print('PASS: explicit GL2(F3) <-> 48 signed-permutation/code stabilizers; homomorphism and glue preservation')

Iq=((0,1),(2,0));Jq=((1,1),(1,2));minusI=((2,0),(0,2))
Kq=mm(Iq,Jq,3)
neg=lambda A:tuple(tuple(-v%3 for v in row) for row in A)
Q={I,minusI,Iq,neg(Iq),Jq,neg(Jq),Kq,neg(Kq)}
assert mm(Iq,Iq,3)==mm(Jq,Jq,3)==minusI
assert mm(Iq,Jq,3)==neg(mm(Jq,Iq,3))
assert len(Q)==8 and Q=={A for A in GL3 if lift(A)[2]==I}
AR=((1,0),(0,2));AH=((1,2),(0,2))
assert lift(AR)==((1,1,1,-1),(1,0,2,3),((1,1),(0,1)))
assert lift(AH)==((1,1,1,-1),(0,2,1,3),((0,1),(1,0)))
assert mm(AR,AR,3)==mm(AH,AH,3)==I
ARH=mm(AR,AH,3)
assert mm(mm(ARH,ARH,3),ARH,3)==I
section={((1,a),(0,b)) for a in range(3) for b in (1,2)}
assert len({lift(A)[2] for A in section})==6 and section&Q=={I}
print('PASS: exact quaternion kernel, displayed R/H section, and Q8 semidirect S3')

R=tuple(tuple(F(-1 if i==j==0 else i==j) for j in range(4)) for i in range(4))
H=tuple(tuple(F(v,2) for v in row) for row in
        ((1,1,1,1),(1,1,-1,-1),(1,-1,1,-1),(1,-1,-1,1)))
def exactmm(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))
Id=tuple(tuple(F(i==j) for j in range(4)) for i in range(4))
RH=exactmm(R,H)
assert exactmm(R,R)==exactmm(H,H)==Id
assert exactmm(exactmm(RH,RH),RH)==Id
print('PASS: full rational D4 lift involutions and cubic relation')
print('ALL INDEPENDENT GL2/TRIALITY CHECKS PASSED')
