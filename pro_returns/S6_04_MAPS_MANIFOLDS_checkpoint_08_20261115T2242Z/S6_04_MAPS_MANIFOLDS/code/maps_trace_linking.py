"""Exact characteristic arithmetic for B.6.24 after geometric inputs.

The trace sign is fixed by the IDENTIFIED torsion generator, not by
an arbitrary isomorphism of discriminant groups. The geometric proof
of that identification is B.6.19. No finite multiplicity cutoff is used.
"""
from pathlib import Path
from fractions import Fraction
import json
import sympy as s

d=s.symbols('d',integer=True,positive=True)
k=-d
ell=4*k
c=ell-2*k
mu_free=s.simplify((3*ell**2/k-8*ell-4*k+12)/2688)
mu_trace_same=s.simplify((c**2/k+4)/896)
mu_trace_opposite=s.simplify((c**2/(-k)-4)/896)
assert s.simplify(mu_free-mu_trace_same)==0
assert s.simplify(mu_free-(1-d)/224)==0
assert s.simplify(mu_trace_opposite+mu_trace_same)==0
assert mu_free.subs(d,1)==0
assert mu_trace_same.subs(d,1)==0
assert mu_trace_opposite.subs(d,1)==0
wrong_two=Fraction(-1,112)
assert (28*wrong_two).denominator==4
out={
    'actual_cup':'k=-d, d=k_multiplicity*l_multiplicity>0',
    'quotient_p1':'ell=4k=-4d',
    'trace_p1_coefficient':str(c),
    'mu_free':str(mu_free),
    'mu_trace_same_sign':str(mu_trace_same),
    'mu_original_same_sign':'0',
    'opposite_linking_difference':'2/k; zero modulo Z only when |k| divides 2',
    'd_one':'Both possible trace signs give zero correction and zero free invariant.',
    'd_two_wrong_mu':str(wrong_two),
    'd_two_wrong_theta_value':str(28*wrong_two),
    'd_two_obstruction':'Not an integer, contradicting the K3 normalization.',
    'all_admissible_d':'mu_original=0',
}
text=json.dumps(out,indent=2)+'\n'
print(text,end='')
Path(__file__).with_suffix('.out.json').write_text(text)
