"""Postrelease recovery: integral chain contraction, with no rank or Smith algorithm."""
from itertools import combinations

letters = ('a', 'c', 'b', 'd')
cells = {k: [''.join(p) or '1' for p in combinations(letters, k)] for k in range(5)}
cells[2] += ['r']
cells[3] += ['rc', 'h']
cells[4] += ['hc']
basis = [c for degree in cells for c in cells[degree]]
assert len(basis) == 20 and len(set(basis)) == 20
degree = {c: k for k, group in cells.items() for c in group}
boundary = {'r': {'a': 1}, 'rc': {'ac': 1}}
homotopy = {'a': {'r': 1}, 'ac': {'rc': 1}}
contracted = {'r', 'a', 'rc', 'ac'}


def linear(mapping, chain):
    result = {}
    for c, coefficient in chain.items():
        for t, v in mapping.get(c, {}).items():
            result[t] = result.get(t, 0) + coefficient * v
    return {c: v for c, v in result.items() if v}


def plus(*chains):
    result = {}
    for chain in chains:
        for c, v in chain.items():
            result[c] = result.get(c, 0) + v
    return {c: v for c, v in result.items() if v}


def projection(chain):
    return {c: v for c, v in chain.items() if c not in contracted}


for c in basis:
    v = {c: 1}
    assert not linear(boundary, linear(boundary, v))
    lhs = plus(linear(boundary, linear(homotopy, v)), linear(homotopy, linear(boundary, v)))
    rhs = plus(v, {x: -a for x, a in projection(v).items()})
    assert lhs == rhs, c
    assert not projection(linear(boundary, v))
    assert not linear(boundary, projection(v))
    for t in homotopy.get(c, {}):
        assert degree[t] == degree[c] + 1
    for t in boundary.get(c, {}):
        assert degree[t] == degree[c] - 1

ranks = [sum(c not in contracted for c in cells[k]) for k in range(5)]
assert ranks == [1, 3, 5, 5, 2]
for k, expected in [(1, ['a']), (2, ['ac'])]:
    torus = [''.join(p) for p in combinations(letters, k)]
    killed = [c for c in torus if not projection({c: 1})]
    assert killed == expected
    surviving = [c for c in torus if c not in killed]
    assert all(projection({c: 1}) == {c: 1} for c in surviving)
    print('torus inclusion degree', k, 'primitive integral kernel basis', killed)

print('dh+hd=id-ip checked on every one of the 20 integral basis cells')
print('p and i are chain maps; pi=id; the residual differential is zero')
print('free integral homology ranks', ranks)
