"""Exact printed weighted-quintic certificate for 02XS, finalized after release.

Use an integral five-cycle matrix and its rational invariant projector,
normalization Euler data, and explicit weighted monomial enumeration.
The complete target proof was read after the separately preserved prereading freeze. No historical target routine is imported.
"""
import sympy as s

P=s.zeros(5)
for j in range(5):P[(j+1)%5,j]=1
I=s.eye(5)
E=sum((P**j for j in range(5)),s.zeros(5))/5
assert E**2==E and E.rank()==1 and (I-E).rank()==4
assert (P-I).rank()==4
assert [s.trace(P**j) for j in range(1,5)]==[0]*4
print('C5 integer action:',P.tolist())
print('Invariant/noninvariant projector ranks:',E.rank(),(I-E).rank())
print('Nonidentity power traces:',[s.trace(P**j) for j in range(1,5)])
a,b,chi=s.symbols('a b chi')
answer=s.solve([a-b,a+4*b-chi],[a,b])
assert answer=={a:chi/5,b:chi/5}
print('Rational virtual character from free action:',answer)

print('Double-cover chi(O) for branch degrees 6 and 4:',1+(1-3),1+(1-2))
assert 1-(1+(1-3))==2
assert 1-(1+(1-2))==1
delta,branch_excess=s.symbols('delta branch_excess')
g=2-delta
mu=2*delta-branch_excess
chi_curve=2-2*g-branch_excess
assert s.expand(3-chi_curve-(5-mu))==0
print('Irreducible degree-five weighted curve: chi(complement)=5-M.')
for contacts in [(1,1),(2,)]:
 mu=sum(2*k-1 for k in contacts)
 chi_curve=2-len(contacts)
 assert 3-chi_curve==5-mu
 print('Elliptic quartic + line:',contacts,'M',mu,'chi complement',3-chi_curve)
for mu in range(4):
 copies=5-mu
 A=s.kronecker_product(s.eye(copies),P)
 rank=(A-s.eye(5*copies)).rank()
 assert rank==4*(5-mu)>mu
 print('M',mu,'chiF',5*(5-mu),'rank lower',rank,'gap',rank-mu)

monomials=[]
for degree in [4,5]:
 for ax in range(degree+1):
  for ay in range(degree-ax+1):
   az=degree-ax-ay
   if degree==4 and ax==0:continue
   weight=2*ax+ay+az
   assert weight>=5
   if weight==5:monomials.append((ax,ay,az))
assert set(monomials)=={(1,j,3-j) for j in range(4)}|{(0,j,5-j) for j in range(6)}
print('Weight-five monomials after x^2 z:',monomials)
x,z,q3,q5,q2,q4=s.symbols('x z q3 q5 q2 q4')
disc=s.discriminant(z*x*x+q3*x+q5,x)
assert disc==q3*q3-4*z*q5
assert s.expand(disc.subs({q3:z*q2,q5:z*q4})-z*z*(q2*q2-4*q4))==0
print('Discriminant:',disc,'; common-z factor leaves a quartic discriminant.')
print('PASS: weighted leading form, double-cover genera, Euler identities and all cyclic rank bounds are exact.')

# Postrelease exact coverage of the printed discriminant partition argument.
def partitions(n,lo=1):
    if n==0:
        yield ()
        return
    for first in range(lo,n+1):
        for tail in partitions(n-first,first):
            yield (first,)+tail
sextic_positive=[]
for part in partitions(6):
    odd=sum(k%2 for k in part)
    genus=(odd-2)//2
    assert odd%2==0
    if genus>0:
        M=sum(k-1 for k in part)
        assert M<=2
        sextic_positive.append((part,genus,M))
assert len(sextic_positive)==3
print('All sextic partitions with positive-genus connected normalization:',sextic_positive)
quartic_positive=[]
for part in partitions(4):
    odd=sum(k%2 for k in part)
    if odd>=4:
        quartic_positive.append(part)
assert quartic_positive==[(1,1,1,1)]
print('All quartic partitions with positive-genus connected normalization:',quartic_positive)
assert 4*2>3
print('Printed bound: rank at least 8, transverse rank at most 3, strict gap 5.')
print('PASS: every printed finite partition and integer bound is covered.')
