#!/usr/bin/env python3
"""Fresh exhaustive degree-ten dessin calculation for the OS56/II cubic.

This program reads no target proof and imports no historical computation.
All permutations act on the left; compose(a,b)[i] = a[b[i]].
"""
from itertools import permutations, product
from datetime import datetime, timezone


def compose(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def inverse(a):
    out = [0]*len(a)
    for i, j in enumerate(a):
        out[j] = i
    return tuple(out)


def cycles(a):
    seen = set()
    out = []
    for i in range(len(a)):
        if i in seen:
            continue
        row = []
        j = i
        while j not in seen:
            seen.add(j)
            row.append(j)
            j = a[j]
        out.append(tuple(row))
    return out


def matchings(remaining):
    if not remaining:
        yield ()
        return
    a = remaining[0]
    for b in remaining[1:]:
        tail = tuple(x for x in remaining if x not in (a, b))
        for pairs in matchings(tail):
            yield ((a, b),) + pairs


def transitive(a, b):
    seen = {0}
    queue = [0]
    while queue:
        x = queue.pop()
        for y in (a[x], b[x]):
            if y not in seen:
                seen.add(y)
                queue.append(y)
    return len(seen) == len(a)


rho = (1, 2, 0, 4, 5, 3, 7, 8, 6, 9)
centralizer = []
for blocks in permutations(range(3)):
    for shifts in product(range(3), repeat=3):
        h = [0]*10
        h[9] = 9
        for b in range(3):
            for j in range(3):
                h[3*b+j] = 3*blocks[b]+(j+shifts[b]) % 3
        h = tuple(h)
        assert compose(h, rho) == compose(rho, h)
        centralizer.append((h, inverse(h)))
assert len(centralizer) == 162

classes = {}
tested = accepted = 0
for pairs in matchings(tuple(range(10))):
    tested += 1
    sigma = [0]*10
    for a, b in pairs:
        sigma[a], sigma[b] = b, a
    sigma = tuple(sigma)
    if sorted(map(len, cycles(compose(rho, sigma)))) != [2, 3, 5]:
        continue
    if not transitive(rho, sigma):
        continue
    accepted += 1
    canon = min(compose(h, compose(sigma, hi)) for h, hi in centralizer)
    classes.setdefault(canon, 0)
    classes[canon] += 1
assert tested == 945
print('All fixed-point-free involutions tested:', tested)
print('Connected pairs with infinity partition (2,3,5):', accepted)
print('Classes up to simultaneous conjugacy with rho fixed:', len(classes))
for sigma, size in sorted(classes.items()):
    print('Class size:', size)
    print('rho:', cycles(rho))
    print('sigma:', cycles(sigma))
    print('rho sigma:', cycles(compose(rho, sigma)))
    print('Euler characteristic:', len(cycles(rho))+len(cycles(sigma))
          +len(cycles(compose(rho, sigma)))-10)
print('Completed:', datetime.now(timezone.utc).isoformat())
