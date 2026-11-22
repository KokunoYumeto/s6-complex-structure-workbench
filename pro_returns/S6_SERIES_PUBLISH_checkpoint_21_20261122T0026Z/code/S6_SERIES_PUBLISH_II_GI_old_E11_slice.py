# Exact E11 slice of the pinned original; other owners omitted.
from fractions import Fraction
from math import gcd

def coarse_degree(d,r,q):
    ar=(d*pow(q,-1,r))%r
    aq=(d*pow(r,-1,q))%q
    ans=Fraction(d,r*q)-Fraction(ar,r)-Fraction(aq,q)
    assert ans.denominator==1
    return ans.numerator
def h0(d,r,q):
    if d<0:return 0
    return sum((d-r*j)%q==0 for j in range(d//r+1))
checked=0
for k0 in range(1,41):
    for ell in range(1,41):
        r,q=3*k0,4*ell
        if gcd(r,q)!=1:continue
        n=k0*ell
        assert coarse_degree(-n,r,q)==-1
        assert coarse_degree(-2*n,r,q)==-1
        L=r+q-r*q
        assert coarse_degree(L,r,q)==-1
        assert h0(n-2*r-2*q,r,q)==0
        assert coarse_degree(L-n,r,q)==(-1 if k0==1 else -2)
        checked+=1
print('E11 coprime multiplicity pairs k,l<=40 checked:',checked)
print('E11 all exact root cohomology identities passed')
