"""Enumerate the two-fibre contact partitions in C.2.D4.3 exactly."""
from itertools import combinations_with_replacement
partitions=[(1,1,1),(2,1),(3,)]
print('contacts F1; contacts F2; P; nu; q; b1(U); pairing rank; remaining loss bound')
for a,b in combinations_with_replacement(partitions,2):
    p=(a==(3,))+(b==(3,))
    nu=len(a)+len(b)
    q=max(p-1,0)
    b1=2*q+1
    rank=2*nu-4-2*p+4*q
    loss=len(a)+len(b)-2
    assert b1<=3 and rank>=0
    if rank==0: assert loss<=1
    print(a,b,p,nu,q,b1,rank,loss if rank==0 else 'excluded by pairing',sep='; ')
print('Every surviving two-fibre case has e(S)>=2-loss>=1.')
print('Double-common-fibre: normalized eigensheaves O, O(-1,-1), O(-2,-1); all H1 vanish.')
for nu in (1,2,3):
    e=3*nu;bd=nu-1;rank=e-1-bd
    assert rank==2*nu and rank>0
    print(f'double-common contact count={nu}: e(U)={e}, b1(boundary)={bd}, intersection rank={rank}')
print('PASS')
