"""The integral Leray-page route attempted before the direct E.2.6 MV proof.

This is retained as an exploratory calculation, not as a substitute for
the complete integral homology proof.  It uses the normalized original
transgressions, finite-cover indices n_i, and invariant-to-coinvariant
coefficients k_i.  The resulting associated groups leave extension
classes undetermined.  Those extensions were subsequently settled by
manifolds_shifted_mv.py; in particular one produces a Z/24 summand.

All integers below are exact. A simultaneous orientation sign in d2
does not change any printed Smith form.
"""
from math import comb, lcm, gcd
from sympy import zeros, ZZ
from sympy.matrices.normalforms import smith_normal_form

n = [1, 12, 2, 2, 12]
k = [1, 0, 12, 0, 1]
for q in range(1, 9):
    source = [(i, q-i) for i in range(5) if 0 <= q-i <= 4]
    target = [(i, q-1-i) for i in range(5) if 0 <= q-1-i <= 4]
    G = zeros(len(target), len(source))
    for a, (i, j) in enumerate(source):
        L = lcm(n[i], n[j])
        if i:
            G[target.index((i-1, j)), a] = L//n[i]*k[j]
        if j:
            G[target.index((i, j-1)), a] = (-1)**i*L//n[j]*k[i]
    D = smith_normal_form(G, domain=ZZ)
    factors = [abs(int(D[i, i])) for i in range(min(D.shape)) if D[i, i]]
    torsion = []
    for i, j in source:
        if not i or not j:
            continue
        torsion += ([n[i]]*(comb(4, j)-1)
                    + [n[j]]*(comb(4, i)-1) + [gcd(n[i], n[j])])
    torsion = [x for x in torsion if x > 1]
    print('q', q, 'source', source, 'target', target)
    print('d2', G.tolist(), 'Smith', factors)
    print('base-degree-two quotient: free rank', len(target)-len(factors),
          'torsion', [x for x in factors if x > 1])
    print('base-degree-one covering-cokernel torsion',
          {z: torsion.count(z) for z in sorted(set(torsion))})
print('No total integral homology is inferred from this associated page.')
print('The complete extension calculation is Theorem E.2.6 and its MV executable.')
