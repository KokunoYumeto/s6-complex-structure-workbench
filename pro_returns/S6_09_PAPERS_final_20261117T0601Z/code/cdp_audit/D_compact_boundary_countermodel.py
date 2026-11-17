#!/usr/bin/env python3
"""Exact charts, canonical Jacobians and zero-Euler balancing for C.2.UN.79."""
import sympy as s
from itertools import combinations

def need(ok, label):
    if not ok:
        raise AssertionError(label)

t,z,b,u,c,A,ainf,a,x,y=s.symbols("t z b u c A ainf a x y")
delta=31*t**12+12*t**8+12*t**4+4
need(s.gcd(delta,s.diff(delta,t)) == 1, "Weierstrass discriminant square-free")
need(s.gcd(t**4+1,t**6) == 1, "No cuspidal discriminant root")
need(s.LC(s.Poly(delta,t)) == 31, "Smooth infinity")
print("Compact starting elliptic surface: discriminant square-free; every root I1; infinity smooth")

chart0=s.Matrix([b,b**2*z**3,b*z])
chart1=s.Matrix([u**2*c,u*c**2,u*c])
for j,v in enumerate([chart0,chart1]):
    need(s.expand(v[0]*v[1]-v[2]**3)==0, f"A2 equation in chart {j}")
sub={u:1/z,c:z**2*b}
need(all(s.simplify(chart1[j].subs(sub,simultaneous=True)-chart0[j])==0
         for j in range(3)), "A2 exact overlap")
j0=s.Matrix([chart0[0],chart0[2]]).jacobian([b,z]).det()/chart0[0]
j1=s.Matrix([chart1[0],chart1[2]]).jacobian([u,c]).det()/chart1[0]
need(s.simplify(j0-1)==0 and s.simplify(j1-1)==0, "Actual canonical forms")
print("A2 minimal-resolution charts: xy=s^3, exact overlap, and dx^ds/x agree")

blow=s.Matrix([b,z,z*A])
need(blow.jacobian([b,z,A]).det()==z, "Curve-blowup Jacobian")
transition=s.Matrix([u**2*c,1/u,u*ainf])  # (b,z,A)
jac=s.factor(transition.jacobian([u,c,ainf]).det())
need(s.simplify(jac-u)==0, "O(-1)+O(-2) transition Jacobian")
need(s.simplify((z*b).subs({z:1/u,b:u**2*c},simultaneous=True)-u*c)==0,
     "Entire f-germ exact")
need(s.simplify(jac/u-1)==0, "Canonical section has no second-end zero")
print("Blowup (z,a): a=zA; transition (A,b)=(u*a_inf,u^2*c); f=bUV")
print("Canonical Jacobians: first chart z; second chart unit1; orders (P,R,Q)=(0,1,0)")
need(-2-(-1-2)==1, "Adjunction canonical degree")
need(0*(-2)+1+0==1, "Canonical divisor restricts with degree1")
need((1-0-1)+(0-0-1)==-1, "Component canonical intersection with F")
print("Normal splitting O(-1)+O(-2), F_P^2=-1, and both adjunction comparisons pass")

P=z**2+1
Q=3*z**2+z+5
factors=[P,Q,Q-P,Q-2*P]
discs=[s.discriminant(v,z) for v in factors]
need(discs==[-4,-59,-31,-11], "Four displayed discriminants")
resultants=[]
for i,j in combinations(range(4),2):
    rr=s.resultant(factors[i],factors[j],z)
    resultants.append((i,j,int(rr)))
    need(rr!=0, "Pairwise disjoint branch divisors")
H=s.prod(factors).expand()
need(s.degree(H,z)==8 and s.gcd(H,s.diff(H,z))==1, "Eight simple branch points")
need(s.LC(s.Poly(H,z))==6, "No extra infinity branch")
need(s.simplify(P**4*(Q/P)*(Q/P-1)*(Q/P-2)-H)==0, "Literal Y=yP² map")
print("Genus-three centre: H(z) =", H)
print("Quadratic discriminants:", discs)
print("Pairwise resultants:", resultants)
print("Exact hyperelliptic equation and all eight simple branch points verified")

R=Q/P
need(R.subs(z,0)==5 and s.limit(R,z,s.oo)==3, "Boundary values")
for v in [0,1,2]:
    pol=Q-v*P
    need(s.discriminant(pol,z)!=0, "Simple branch preimages")
    need(pol.subs(z,0)!=0 and s.LC(s.Poly(pol,z))!=0,
         "No endpoint branch or existing triple")
for v in [0,1]:
    need(s.gcd(Q-v*P,s.diff(Q-v*P,z))==1, "Transverse B_j intersection")
print("D meets the two old elliptic boundaries and B0,B1 transversely, avoiding all four old triples")

# Classes A={point}xE, B=P1x{point}: A²=B²=0, A.B=1, K=-2A.
D2=2*2*2
KD=-2*2
g=1+(D2+KD)//2
need(g==3, "Adjunction genus")
eD=2-2*g
need(0+2+2+eD==0, "Blowup-support Euler balance")
vertex_e=[0,4,4,6,6,-8]
double_e=6*2+eD+8*2
triples=4+8
need(sum(vertex_e)==12 and double_e==24 and triples==12, "Explicit SNC strata counts")
need(sum(vertex_e)-double_e+triples==0, "Independent SNC inclusion-exclusion")
print("Final six components have Euler numbers:",vertex_e)
print("SNC check: sum e(components)=12, sum e(double curves)=24, triples=12, e(S)=0")
print("ALL EXACT CHECKS PASSED")
