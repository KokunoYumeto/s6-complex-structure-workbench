"""Exact open-box face graph, separate periodic graph, and symbol checks.

The graph arithmetic is integral/rational. Symbol checks use exact SymPy
polynomials; no numerical eigenvalue is used to assert a spectral bound.
"""

from collections import Counter, deque
from fractions import Fraction as F
from itertools import combinations, product
import sympy as s


def shift(n, i, step=1, periods=None):
    out = list(n)
    out[i] += step
    if periods is not None:
        out[i] %= periods[i]
    return tuple(out)


def boundary(face, periods=None):
    n, i, j = face
    return frozenset(((n, i), (shift(n, i, periods=periods), j),
                      (shift(n, j, periods=periods), i), (n, j)))


def graph(faces, periods=None):
    stars = {}
    for p in faces:
        for edge in boundary(p, periods):
            stars.setdefault(edge, []).append(p)
    adj = {p: set() for p in faces}
    seen_pairs = set()
    for incident in stars.values():
        for p, q in combinations(incident, 2):
            key = frozenset((p, q))
            assert key not in seen_pairs  # no double-shared physical edges
            seen_pairs.add(key)
            adj[p].add(q)
            adj[q].add(p)
    return adj, seen_pairs


for L in range(2, 6):
    m = 2*L
    faces = [(n, i, j) for n in product(range(-L, L+1), repeat=3)
             for i, j in combinations(range(3), 2) if n[i] < L and n[j] < L]
    adj, pairs = graph(faces)
    assert len(faces) == 12*L*L*(2*L+1)
    assert len(pairs) == 144*L**3-12*L
    degrees = Counter(len(adj[p]) for p in faces)
    assert degrees == {
        12: 3*(m-1)*(m-2)**2, 11: 12*(m-1)*(m-2), 10: 12*(m-1),
        8: 6*(m-2)**2, 7: 24*(m-2), 6: 24,
    }
    for n, i, j in faces:
        k = 3-i-j
        beta = lambda x: int(x == -L or x == L-1)
        expected = (8 if n[k] in (-L, L) else 12)-beta(n[i])-beta(n[j])
        assert len(adj[n, i, j]) == expected
    seen = {faces[0]}
    queue = deque(seen)
    while queue:
        p = queue.popleft()
        for q in adj[p]:
            if q not in seen:
                seen.add(q)
                queue.append(q)
    assert len(seen) == len(faces)
    assert F(4*len(pairs), len(faces)) == F(48*L*L-4, L*(2*L+1))
    assert sum(12-len(adj[p]) for p in faces) == 12*m*(3*m+1)

    # An exact integer product test verifies the factorized interior trial
    # quadratic form on the ORIGINAL whole open graph.
    ell = m-2
    one_d = {r: r*(ell+1-r) for r in range(1, ell+1)}
    sq = sum(v*v for v in one_d.values())
    cross = sum(one_d[r]*one_d[r+1] for r in range(1, ell))
    trial = {}
    for p in faces:
        n = p[0]
        value = 1
        for x in n:
            value *= one_d.get(x+L, 0)
        trial[p] = value
        if value:
            assert len(adj[p]) == 12
    norm = sum(value*value for value in trial.values())
    qform = sum((trial[p]+trial[q])**2 for p, q in (tuple(pair) for pair in pairs))
    assert norm == 3*sq**3
    assert qform == 36*sq**3+12*cross*sq**2+6*sq*(sq+cross)**2

    # f_r=sin(r t)/sin(t)=U_(r-1)(c), c=cos(pi/(ell+1)).
    # Prove the needed recurrence identities modulo U_ell(c)=0 exactly.
    c = s.symbols("c")
    sequence = [s.chebyshevu(r-1, c) for r in range(1, ell+1)]
    ss = s.expand(sum(v*v for v in sequence))
    jj = s.expand(sum(sequence[r]*sequence[r+1] for r in range(ell-1)))
    modulus = s.chebyshevu(ell, c)
    assert s.rem(jj-c*ss, modulus, c) == 0
    exact_trial = 36*ss**3+12*jj*ss**2+6*ss*(ss+jj)**2
    assert s.rem(exact_trial-(14+8*c+2*c*c)*3*ss**3, modulus, c) == 0
    print(f"L={L}: {len(faces)} faces, {len(pairs)} adjacencies; "
          "all boundary degrees, connectivity, and interior trial identities passed.")

# Independently defined periodic graph, all periods >=3.
periods = (3, 4, 5)
periodic_faces = [(n, i, j) for n in product(*(range(q) for q in periods))
                  for i, j in combinations(range(3), 2)]
periodic_adj, periodic_pairs = graph(periodic_faces, periods)
assert all(len(neighbors) == 12 for neighbors in periodic_adj.values())
assert len(periodic_pairs) == 18*periods[0]*periods[1]*periods[2]
plane_types = ((0, 1), (0, 2), (1, 2))
for p in periodic_faces:
    n, i, j = p
    expected = set()
    for direction in (i, j):
        for sign in (-1, 1):
            expected.add((shift(n, direction, sign, periods), i, j))
    for k, l in plane_types:
        if (k, l) == (i, j):
            continue
        shared = ({i, j} & {k, l}).pop()
        transverse_p = ({i, j}-{shared}).pop()
        transverse_q = ({k, l}-{shared}).pop()
        for a, b in product((0, 1), repeat=2):
            base = shift(shift(n, transverse_p, a, periods), transverse_q, -b, periods)
            expected.add((base, k, l))
    assert expected == periodic_adj[p]

# Half-phase variables x_i=e^(ik_i/2) retain all offset phases exactly.
x1, x2, x3 = s.symbols("x1 x2 x3", nonzero=True)
x = (x1, x2, x3)
symbol = s.zeros(3)
for a, (i, j) in enumerate(plane_types):
    symbol[a, a] = 12+x[i]**2+x[i]**-2+x[j]**2+x[j]**-2
for a, b in combinations(range(3), 2):
    common = (set(plane_types[a]) & set(plane_types[b])).pop()
    p = (set(plane_types[a])-{common}).pop()
    q = (set(plane_types[b])-{common}).pop()
    symbol[a, b] = (1+x[p]**2)*(1+x[q]**-2)
    symbol[b, a] = (1+x[p]**-2)*(1+x[q]**2)
phase = s.diag(*(x[i]*x[j] for i, j in plane_types))
centered = phase.inv()*symbol*phase
for a, b in combinations(range(3), 2):
    common = (set(plane_types[a]) & set(plane_types[b])).pop()
    p = (set(plane_types[a])-{common}).pop()
    q = (set(plane_types[b])-{common}).pop()
    assert s.simplify(centered[a, b]-(x[p]+1/x[p])*(x[q]+1/x[q])) == 0
    assert s.simplify(centered[a, b]-centered[b, a]) == 0
zero_momentum = symbol.subs({x1: 1, x2: 1, x3: 1})
assert zero_momentum == 12*s.eye(3)+4*s.ones(3)
t = s.symbols("t")
assert s.factor(zero_momentum.charpoly(t).as_expr()) == (t-24)*(t-12)**2
assert F(7, 15)-F(24, 21) == -F(71, 105)
print("PASS: separately specified periodic multiplicities, complete Laurent symbol,")
print("centered-face phase dictionary, zero-mode eigenvalues, and -71/105 coefficient.")
