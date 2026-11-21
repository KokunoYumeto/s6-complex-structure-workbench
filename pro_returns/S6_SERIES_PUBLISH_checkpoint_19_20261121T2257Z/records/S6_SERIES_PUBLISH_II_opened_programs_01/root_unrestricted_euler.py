"""Exact arithmetic supporting C.2.UN.1--2; the parity proof is in the text."""
from itertools import combinations
import random
import sympy as s

pairs = list(combinations(range(4), 2))
def exterior_square(t):
    return s.Matrix([[t.extract(i, j).det() for j in pairs] for i in pairs])

rng = random.Random(61503)
ranks = set()
for trial in range(80):
    t = s.eye(4)
    for _ in range(12):
        i, j = rng.sample(range(4), 2)
        transvection = s.eye(4)
        transvection[i, j] = rng.choice([-2, -1, 1, 2])
        t = transvection*t
    assert t.det() == 1
    g = exterior_square(t)
    rank = (g-s.eye(6)).rank()
    ranks.add(rank)
    assert rank % 2 == 0
print('80 exact SL4 exterior-square parity checks passed; ranks:', sorted(ranks))
for n in range(-12, 13):
    k = max(1, -n)
    m = k+n
    betti = [1, 4, 7+k+m, 8+4*k, 7+k+m, 4, 1]
    e = sum((-1)**i*b for i, b in enumerate(betti))
    assert e == 2*(m-k) == 2*n
    print('n=', n, 'curve blowups=', k, 'point blowups=', m,
          'Euler=', e, 'Betti=', betti)
print('All exact realization checks passed.')
