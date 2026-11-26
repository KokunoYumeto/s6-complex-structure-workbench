"""Prereading exact certificate for 02XT: elliptic section rings and characters.

Construct the rational irreducibles from cyclotomic quotient algebras.
Solve every trace equation from the explicit geometric fixed loci.
No XT target proof or historical program is imported.
"""
import sympy as s

t=s.symbols('t')
for d,weights,N in [(3,(1,1,1),3),(2,(1,1,2),4),(1,(1,2,3),6)]:
    series=(1-t**N)/s.prod(1-t**w for w in weights)
    assert s.cancel(series-(1+d*t/(1-t)**2))==0
    print('Section ring degree',d,'weights',weights,'relation',N,'Hilbert identity exact.')

def rational_irrep(order):
    poly=s.Poly(s.cyclotomic_poly(order,t),t)
    n=poly.degree();C=s.zeros(n)
    for j in range(n-1):C[j+1,j]=1
    for i in range(n):C[i,n-1]=-poly.nth(i)
    assert C**order==s.eye(n)
    return C

def solve_character(N,traces,M,label):
    divisors=s.divisors(N);matrices=[rational_irrep(d) for d in divisors]
    table=s.Matrix([[s.trace(C**k) for C in matrices] for k in range(N)])
    values=s.Matrix(traces)
    sol=table.gauss_jordan_solve(values)[0]
    assert table*sol==values
    assert all(v.is_Integer and v>=0 for v in sol)
    nontrivial=sum(v*C.rows for d,v,C in zip(divisors,sol,matrices) if d!=1)
    assert nontrivial>M
    print(label,'divisors',divisors,'multiplicities',list(sol),
          'nontrivial lower bound',nontrivial,'transverse upper bound',M,'gap',nontrivial-M)
    return list(sol)

for roots in [1,2,3]:
    branch=3*(2-roots);chi=18-branch
    assert chi==12+3*roots
    traces=[chi,0,0,branch,0,0]
    assert solve_character(6,traces,3-roots,'Degree 3, '+str(roots)+' binary roots')==[3,roots+1,3,roots+1]
for complement,M in [(3,0),(2,1)]:
    assert solve_character(7,[7*complement]+[0]*6,M,'Degree 2, complement Euler '+str(complement))==[complement,complement]
branch_curve=9*(2-4)+3
assert branch_curve==-15
chi=-(branch_curve-3)+3
assert chi==21
assert solve_character(9,[chi,0,0,3,0,0,3,0,0],0,'Degree 1')==[3,3,2]

a,b,c,wu,wv=s.symbols('a b c wu wv')
assert s.expand(wu*a+wv*b+(a+b+c-3)-((wu+1)*a+(wv+1)*b+c-3))==0
print('Weighted blowdown degree shift is identically three.')

x,y,z,u,v,r=s.symbols('x y z u v r')
terms=[]
for i in range(4):
    for j in range(4-i):
        k=3-i-j
        terms.append(s.Symbol('g'+str(i)+str(j)+str(k))*u**i*v**j*r**k)
F3=sum(terms)
assert s.cancel(z**3*F3.subs({u:x/z,v:y/z,r:z})-F3.subs({u:x,v:y,r:z**2}))==0
print('Degree-three leading relation pulls back exactly to F3(x,y,z^2).')

b,c,d,e,f,g,h=s.symbols('b c d e f g h')
B2=b*u*u+c*u*r+d*r*r
C4=r*(e*u**3+f*u*u*r+g*u*r*r+h*r**3)
F4=v*v+B2*v+C4
P7=z*y*y+(b*x*x+c*x*z*z+d*z**4)*y+z*(e*x**3+f*x*x*z*z+g*x*z**4+h*z**6)
assert s.cancel(z**3*F4.subs({u:x/z,v:y/z,r:z})-P7)==0
assert s.expand(F4.subs({u:x,v:y*z,r:z*z})-z*P7)==0
delta=s.discriminant(F4,v)
assert s.expand(delta-(B2*B2-4*C4))==0
assert s.expand(delta.subs(r,0)-b*b*u**4)==0
assert s.expand(s.diff(delta.subs(b,0),r).subs(r,0)+4*e*u**3)==0
Q6=s.cancel(P7.subs(b,0)/z)
assert s.expand(Q6.subs(z,0)-(y*y+e*x**3))==0
print('Degree-two blowdown, projective curve map and branch coefficients exact.')

A,B=s.symbols('A B')
F6=v*v+u**3+A*u*r**4+B*r**6
P9=z*y*y+x**3+A*x*z**6+B*z**9
assert s.cancel(z**3*F6.subs({u:x/z,v:y/z,r:z})-P9)==0
q=u**3+A*u+B
assert s.expand(9*q-3*u*s.diff(q,u)-(6*A*u+9*B))==0
assert s.resultant(q,s.diff(q,u),u)==4*A**3+27*B**2
assert s.expand(s.diff(P9,z).subs({x:u*z**3,y:0})-z**8*(9*q-3*u*s.diff(q,u)))==0
print('Degree-one blowdown, gradient elimination and discriminant exact.')

for P,weights,N in [(F3.subs({u:x,v:y,r:z*z}),(2,2,1),6),(P7,(2,3,1),7),(P9,(3,4,1),9)]:
    for monomial,coefficient in s.Poly(P,x,y,z).terms():
        assert sum(a*w for a,w in zip(monomial,weights))==N
    print('All monomials have original weights',weights,'and degree',N)

print('PASS: all section-ring identities, fixed-locus characters, rank gaps and coordinate comparisons are exact.')
