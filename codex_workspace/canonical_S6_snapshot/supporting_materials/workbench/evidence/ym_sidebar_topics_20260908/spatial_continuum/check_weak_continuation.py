"""Exact constants, gauge maps and non-Abelian rectangle diagnostics.

The manuscript proves arbitrary-volume statements. Finite checks below do
not establish convergence, the operator estimates or a mass-gap conclusion.
"""
from pathlib import Path
import sympy as s
import json
count=0
def check(q):
    global count
    assert bool(q)
    count+=1
a,g,N,M,t,kapstar,j,k=s.symbols('a g N M t kapstar j k',positive=True)
kap=2*g**2/a; b=1/(2*g**2*a)
tstar=4*s.sqrt(b*M/(kap*N))
energy=3*kap*N*t/8+6*b*M/t
check(s.simplify(energy.subs(t,tstar)-3*s.sqrt(N*M)/a)==0)
check(s.simplify(tstar-2*s.sqrt(M/N)/g**2)==0)
check(s.simplify(3*s.sqrt(N*M)/a/b-6*g**2*s.sqrt(N*M))==0)
check(s.simplify(4*b*M*(3*s.sqrt(N*M)/a)/kap**2-3*M*s.sqrt(N*M)/(2*g**6))==0)
C0=768*s.pi**2*s.sqrt(3*s.sqrt(5))/10**8
Ckap=48*s.pi**2*s.sqrt(6*s.sqrt(5))/(3125*kapstar**s.Rational(3,2))
check(s.simplify(C0*(200/kapstar)**s.Rational(3,2)-Ckap)==0)
check(s.simplify(Ckap**2-13824*s.sqrt(5)*s.pi**4/(9765625*kapstar**3))==0)
check(s.simplify(12*(j/k)**2*18*s.sqrt(5)*j**6*j**(-10)-216*s.sqrt(5)/(k**2*j**2))==0)
gj2=j**(-10)
check(s.simplify(2*gj2/(1/(100*j))-200*j**(-9))==0)
check(s.simplify(1/(2*gj2/(100*j))-50*j**11)==0)
check(s.simplify(1/(4*gj2**2)-j**20/4)==0)
for L in range(2,12):
    n=6*L*(2*L+1)**2; m=12*L**2*(2*L+1)
    check(s.Rational(n,m)==1+s.Rational(1,2*L))
    check(s.Rational(n,m)<=s.Rational(5,4))

I=s.eye(2)
sigmas=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
rotations=[]
for idx in range(1,10):
    den=1+idx**2
    mat=(s.Rational(1-idx**2,den)*I+2*s.Rational(idx,den)*s.I*sigmas[idx%3]).applyfunc(s.expand)
    check(s.simplify(mat.conjugate().T*mat)==I)
    check(mat.det()==1)
    rotations.append(mat)
def prod(xs):
    z=I
    for x in xs: z=(z*x).applyfunc(s.expand)
    return z
def equal(a,b): return (a-b).applyfunc(s.expand)==s.zeros(2)
def inv(u): return u.conjugate().T

# Exact two-plaquette gluing and the required noncommuting conjugation.
A,B,C,D,E,F,G=rotations[:7]
left=prod([A,D,inv(B),inv(C)])
right=prod([E,F,inv(G),inv(D)])
outer=prod([A,E,F,inv(G),inv(B),inv(C)])
check(equal(outer,prod([A,right,inv(A),left])))
check(not equal(outer,prod([right,left])))
# General small rectangle holonomy under explicit vertex pure gauges.
for mside in range(1,5):
    q={(x,y):rotations[(x+2*y)%len(rotations)] for x in range(mside+1) for y in range(mside+1)}
    h={(x,y):rotations[(2*x+3*y+1)%len(rotations)] for x in range(mside+1) for y in range(mside+1)}
    U={}
    for x in range(mside+1):
        for y in range(mside+1):
            for dx,dy in [(1,0),(0,1)]:
                if x+dx<=mside and y+dy<=mside:
                    U[(x,y,dx,dy)]=prod([inv(q[(x,y)]),q[(x+dx,y+dy)]])
    for x in range(mside):
        for y in range(mside):
            hol=prod([U[x,y,1,0],U[x+1,y,0,1],inv(U[x,y+1,1,0]),inv(U[x,y,0,1])])
            check(equal(hol,I))
    boundary=prod([*[U[x,0,1,0] for x in range(mside)],*[U[mside,y,0,1] for y in range(mside)],*[inv(U[x,mside,1,0]) for x in reversed(range(mside))],*[inv(U[0,y,0,1]) for y in reversed(range(mside))]])
    check(equal(boundary,I))
    origin=(0,0)
    qprime={v:prod([h[origin],q[v],inv(h[v])]) for v in q}
    for (x,y,dx,dy),edge in U.items():
        endpoint=(x+dx,y+dy)
        check(equal(prod([h[(x,y)],edge,inv(h[endpoint])]),prod([inv(qprime[(x,y)]),qprime[endpoint]])))
report={'status':'passed','exact_assertions':count,'scope':'Finite exact coefficient, noncommuting face-gluing, pure-gauge and endpoint-action diagnostics; general proofs in Sections12-13.'}
path=Path(__file__).resolve().parent/'WEAK_CONTINUATION_CHECKS.json'
path.write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
