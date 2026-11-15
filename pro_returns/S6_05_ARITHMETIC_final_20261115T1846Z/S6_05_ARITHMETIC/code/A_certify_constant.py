"""Arb certificate for the rational brackets used by A_finite_bound.cpp."""
from flint import arb, ctx, fmpq
ctx.prec=256
C=arb(9)/(2*arb.pi()**2)*(arb(2)+arb(3).sqrt()).log()*(arb(3)/(2*arb(2).sqrt())).log()
lo=fmpq(35362047799,10**12);hi=fmpq(35362047800,10**12)
assert arb(lo)<C<arb(hi)
print('precision_bits',ctx.prec)
print('C0',C)
print('certified rational lower bound',lo)
print('certified rational upper bound',hi)
print('strict enclosure PASS')
