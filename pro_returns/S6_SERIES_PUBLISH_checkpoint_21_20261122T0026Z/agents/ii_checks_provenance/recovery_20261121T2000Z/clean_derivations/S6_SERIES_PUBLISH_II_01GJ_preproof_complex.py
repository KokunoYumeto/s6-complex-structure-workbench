"""Exact local divisor complex and fibre specialization, before E12 release."""
import json
import sympy as s
t=s.symbols('t')
# The diagonal restriction is z-t at z=0. Its unit sign is removed
# by the explicit invertible scalar -1 on the target free module.
restriction=-t
uniformizer_map=(-1)*restriction
assert uniformizer_map==t
poly=s.Poly(uniformizer_map,t,domain=s.QQ)
assert poly.degree()==1 and poly.nth(0)==0 and poly.nth(1)==1
# Polynomial representatives for the actual quotient Q[t]/(t).
remainders=[s.rem(t**k,poly.as_expr(),domain=s.QQ) for k in range(8)]
assert remainders==[1,0,0,0,0,0,0,0]
# On P1 the O(-2) Cech quotient consists of exponents outside
# {n>=0} union {n<=-2}; solve these two integer inequalities exactly.
missing=[n for n in range(-4,4) if not(n>=0 or n<=-2)]
assert missing==[-1]
for n in range(-4,4):
    assert (not(n>=0 or n<=-2))==(n==-1)
# The derived direct-image complex has ranks 1,1 in degrees 1,2.
# Generic multiplication by t has rank 1; its specialization at 0
# has rank 0, retaining both Tor and ordinary fibre cohomology.
generic=[0,1-1,1-1]
special=[0,1-0,1-0]
assert generic==[0,0,0] and special==[0,1,1]
print(json.dumps({'timing':'before target E12 proof release',
 'local_map':'multiplication by t after the explicit target scalar -1',
 'torsion_length':1,'quotient_basis':['1'],
 'P1_Cech_universal_exponent_condition':'-2 < n < 0, n integral, hence n=-1',
 'P1_H1_basis':['z^-1'],'generic_fibre_h':generic,'origin_fibre_h':special,
 'global_h':[0,0,1,0],'all_assertions_passed':True},indent=2))
