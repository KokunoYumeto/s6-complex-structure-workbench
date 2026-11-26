"""Fresh literal IC8 ordering/divisor check from the affine D5/D7 graphs.

No target proof or historical program is read. The two clean statement
vectors are checked by an actual permutation and by the alternative
correction d_can=-e0; no equality of different completed caps is inferred.
"""
from datetime import datetime, timezone
import json
from math import gcd
from functools import reduce
import sympy as S

def rows(M):
    return [[int(x) for x in row] for row in M.tolist()]

print('START', datetime.now(timezone.utc).isoformat(), flush=True)
for r in (5, 7):
    n = r+1
    C = -2*S.eye(n)
    edges = [(0, 2), (1, 2)] + [(i, i+1) for i in range(2, r-2)] + [(r-2, r-1), (r-2, r)]
    for i, j in edges:
        C[i, j] = C[j, i] = 1
    mu = S.Matrix([1, 1]+[2]*(r-3)+[1, 1])
    perm = [1, 0]+list(range(2, r-1))+[r, r-1]
    sigma = S.zeros(n)
    for i, j in enumerate(perm):
        sigma[j, i] = 1
    mp = S.eye(n)[:, 1]-S.eye(n)[:, 0]
    d_root, d_can = S.eye(n)[:, 1], -S.eye(n)[:, 0]
    m_root, m_can = mp+C*d_root, mp+C*d_can
    delta = d_can-d_root
    assert C*mu == S.zeros(n, 1)
    assert sigma**2 == S.eye(n) and sigma*C == C*sigma
    assert sigma*mu == mu and sigma*delta == delta
    assert sigma*m_root == m_root and sigma*m_can == m_can
    assert m_root == -m_can
    order = [0, 1, r-1, r]+list(range(2, r-1))
    P = S.Matrix([[int(j == order[i]) for j in range(n)] for i in range(n)])
    Pi = P.T
    assert P*Pi == Pi*P == S.eye(n)
    Cp, mup, sigmap, cp = P*C*Pi, P*mu, P*sigma*Pi, P*m_can
    expected = S.Matrix([1, 1, 0, 0, -1]+[0]*(n-5))
    assert cp == expected and sigmap*cp == cp and (cp.T*mup)[0] == 0
    eta = -S.eye(n)[:, 4]
    assert sigmap*eta == eta and (cp.T*eta)[0] == 1
    orbits = [[0, 1], [2, 3]] + [[i] for i in range(4, n)]
    cj = [int(cp[o[0]]) for o in orbits]
    g = reduce(gcd, map(abs, cj), 0)
    h = reduce(gcd, (abs(len(o)*int(cp[o[0]])) for o in orbits), 0)
    q = reduce(gcd, (len(o)*int(mup[o[0]]) for o in orbits), 0)
    assert g == h == 1 and q == 2
    report = dict(type=f'I{r-4}*', edges=edges, C=rows(C), mu=list(map(int, mu)),
        m_P=list(map(int, mp)), d_root=list(map(int, d_root)), d_can=list(map(int, d_can)),
        invariant_difference=list(map(int, delta)), m_root=list(map(int, m_root)),
        m_can=list(map(int, m_can)), sigma=rows(sigma), sigma_inverse=rows(sigma.inv()),
        canonical_order=order, P=rows(P), P_inverse=rows(Pi), canonical_C=rows(Cp),
        canonical_mu=list(map(int, mup)), canonical_sigma=rows(sigmap),
        canonical_sigma_inverse=rows(sigmap.inv()), canonical_c=list(map(int, cp)),
        canonical_eta=list(map(int, eta)), orbits=orbits, g=g, h=h, q=q)
    print(json.dumps(report, sort_keys=True, separators=(',', ':')), flush=True)
print('PASS two literal component/divisor/eta maps and inverse permutations; no completed-cap identification claimed.', flush=True)
print('COMPLETE', datetime.now(timezone.utc).isoformat(), flush=True)
