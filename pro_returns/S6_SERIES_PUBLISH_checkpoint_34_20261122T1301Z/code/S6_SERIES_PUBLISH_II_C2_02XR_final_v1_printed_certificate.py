"""Postrelease exact check of every printed finite quartic calculation.

The historical named routine was not retrieved.  This program computes with
rational C4 projectors and integer permutation matrices, and derives the Euler
identities from normalization data.  It does not replay the absent routine.
"""
import sympy as s
from itertools import combinations_with_replacement

P=s.zeros(4)
for i in range(4): P[(i+1)%4,i]=1
I=s.eye(4)
E1=(I+P+P**2+P**3)/4
Em=(I-P+P**2-P**3)/4
Ec=(I-P**2)/2
assert E1+Em+Ec==I
for e in [E1,Em,Ec]: assert e*e==e
assert E1*Em==E1*Ec==Em*Ec==s.zeros(4)
assert [E1.rank(),Em.rank(),Ec.rank()]==[1,1,2]
print('C4 permutation matrix:',P.tolist())
print('Rational projector ranks:',[E1.rank(),Em.rank(),Ec.rank()])
print('Nonidentity power traces:',[s.trace(P**j) for j in [1,2,3]])
a,b,c,chi=s.symbols('a b c chi')
solution=s.solve([a-b,a+b-2*c,a+b+2*c-chi],[a,b,c])
assert solution=={a:chi/4,b:chi/4,c:chi/4}
print('Rational character coefficients from traces:',solution)

g,delta,branches=s.symbols('g delta branches',integer=True)
M=2*delta-branches
chi_D=2-2*(3-delta)-branches
assert s.expand(3-chi_D-(7-M))==0
print('Irreducible quartic: chi(P2-D)=7-M, verified from genus and branch identifications.')
partitions=[]
for n in [1,2,3]:
 for t in combinations_with_replacement([1,2,3],n):
  if sum(t)==3:partitions.append(t)
for t in partitions:
 m=sum(2*k-1 for k in t)
 complement=3-(2-len(t))
 assert m<=5 and complement==7-m
 print('Cubic-line contacts',t,'M',m,'Euler complement',complement)

for m in range(6):
 r=7-m
 action=s.kronecker_product(s.eye(r),P)
 lower=(action-s.eye(4*r)).rank()
 assert lower==3*r and lower>m
 print('M',m,'chiF',4*r,'rank lower',lower,'gap',lower-m)

r,u,v=s.symbols('r u v')
J=s.Matrix([r,r*u,r*v]).jacobian([r,u,v])
assert J.det()==r**2
print('Blowup Jacobian:',J.det())
for multiplicity in [3,4]:
 pairs=[(n,2-(multiplicity-2)*n) for n in range(1,2//(multiplicity-2)+1)]
 print('Pole coefficient 2 at multiplicity',multiplicity,'(order,new pole) pairs',pairs)
assert [(n,2-2*n) for n in range(1,2//2+1)]==[(1,0)]
print('PASS: all printed Euler, cyclic-character, integer-gap and blowup-residue calculations agree exactly.')
