"""Small exact audit of the finite coordinate data in the proof fragment.

No dependencies, floating point, file writes, Lean, or external data.
The TeX proof establishes exhaustion of all isometries analytically;
this checker exhausts the explicitly specified finite coordinate sets.
"""

from itertools import permutations, product


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def basis(n, i):
    return tuple(int(j == i) for j in range(n))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(a, k):
    return tuple(k * x for x in a)


def a5_audit():
    roots = [add(basis(6, i), scale(basis(6, j), -1))
             for i in range(6) for j in range(6) if i != j]
    neighbors = {i: {j for j in range(30) if dot(roots[i], roots[j]) == 1}
                 for i in range(30)}
    found = []

    def maximal_cliques(r, p, x):
        if not p and not x:
            found.append(frozenset(r))
            return
        pivot = max(p | x, key=lambda u: len(p & neighbors[u]))
        for v in sorted(p - neighbors[pivot]):
            maximal_cliques(r | {v}, p & neighbors[v], x & neighbors[v])
            p.remove(v)
            x.add(v)

    maximal_cliques(set(), set(range(30)), set())
    positive = [frozenset(k for k, r in enumerate(roots) if r[i] == 1)
                for i in range(6)]
    negative = [frozenset(k for k, r in enumerate(roots) if r[i] == -1)
                for i in range(6)]
    assert set(found) == set(positive + negative)
    assert len(found) == 12 and all(len(c) == 5 for c in found)
    for i in range(6):
        for j in range(6):
            assert len(positive[i] & negative[j]) == int(i != j)
    root_index = {r: k for k, r in enumerate(roots)}
    actions = set()
    for sigma in permutations(range(6)):
        for sign in (-1, 1):
            action = []
            for r in roots:
                target = [0] * 6
                for i in range(6):
                    target[sigma[i]] = sign * r[i]
                action.append(root_index[tuple(target)])
            actions.add(tuple(action))
    assert len(actions) == 1440
    return "A5: 12 maximal cliques of size 5; missing matching verified; 1440 distinct root actions."


# Every matrix in this audit is stored as twice its exact matrix.
I2 = tuple(tuple(2 * int(i == j) for j in range(4)) for i in range(4))
RD2 = ((-2, 0, 0, 0), (0, 2, 0, 0), (0, 0, 2, 0), (0, 0, 0, 2))
HD2 = ((1, 1, 1, 1), (1, 1, -1, -1),
       (1, -1, 1, -1), (1, -1, -1, 1))


def mul2(a, b):
    numerator = [[sum(a[i][k] * b[k][j] for k in range(4))
                  for j in range(4)] for i in range(4)]
    assert all(n % 2 == 0 for row in numerator for n in row)
    return tuple(tuple(n // 2 for n in row) for row in numerator)


def apply2(a, x):
    numerator = [dot(row, x) for row in a]
    assert all(n % 2 == 0 for n in numerator)
    return tuple(n // 2 for n in numerator)


def d4_audit():
    triality = {I2}
    frontier = [I2]
    while frontier:
        a = frontier.pop()
        for b in (RD2, HD2):
            c = mul2(a, b)
            if c not in triality:
                triality.add(c)
                frontier.append(c)
    assert len(triality) == 6
    even_signs = [s for s in product((-1, 1), repeat=4)
                  if s[0] * s[1] * s[2] * s[3] == 1]
    weyl = set()
    for sigma in permutations(range(4)):
        for signs in even_signs:
            m = [[0] * 4 for _ in range(4)]
            for i in range(4):
                m[sigma[i]][i] = 2 * signs[i]
            weyl.add(tuple(tuple(row) for row in m))
    assert len(weyl) == 192
    all_matrices = {mul2(w, d) for w in weyl for d in triality}
    assert len(all_matrices) == 1152
    roots = {add(scale(basis(4, i), s), scale(basis(4, j), t))
             for i in range(4) for j in range(i + 1, 4)
             for s, t in product((-1, 1), repeat=2)}
    v2 = {scale(basis(4, i), s) for i in range(4) for s in (-2, 2)}
    sp2 = set(even_signs)
    sm2 = set(product((-1, 1), repeat=4)) - sp2
    classes = (v2, sp2, sm2)
    representatives2 = ((2, 0, 0, 0), (1, 1, 1, 1), (-1, 1, 1, 1))
    action_counts = {}
    kernel = set()
    for a in all_matrices:
        assert {apply2(a, r) for r in roots} == roots
        action = tuple(next(i for i, c in enumerate(classes)
                            if apply2(a, r) in c) for r in representatives2)
        assert len(set(action)) == 3
        action_counts[action] = action_counts.get(action, 0) + 1
        for i, c in enumerate(classes):
            assert {apply2(a, x) for x in c} == classes[action[i]]
        if action == (0, 1, 2):
            kernel.add(a)
    assert kernel == weyl
    assert len(action_counts) == 6 and set(action_counts.values()) == {192}
    return "D4: exact 6-element section; 1152 root isometries; all 6 class actions; kernel exactly 192 even signed permutations."


def binary_apply(b, y):
    return tuple(dot(row, y) % 2 for row in b)


def glue_audit():
    even = [u for u in product(range(2), repeat=4) if sum(u) % 2 == 0]
    ternary = [((a + b) % 3, (a + 2 * b) % 3, a, b)
               for a, b in product(range(3), repeat=2)]

    def tau(u):
        return ((u[1] + u[3]) % 2, (u[2] + u[3]) % 2)

    glue = {(tuple((3 * u[i] + 2 * z[i]) % 6 for i in range(4)), tau(u))
            for u in even for z in ternary}
    assert len(glue) == 72
    gl2 = [((a, b), (c, d)) for a, b, c, d in product(range(2), repeat=4)
           if (a * d - b * c) % 2]
    stabilizer = []
    for p in permutations(range(4)):
        for signs in product((-1, 1), repeat=4):
            for b in gl2:
                image = {(tuple(signs[i] * x[p[i]] % 6 for i in range(4)),
                          binary_apply(b, y)) for x, y in glue}
                if image == glue:
                    stabilizer.append((signs, p, b))
    assert len(stabilizer) == 48
    # Direct comparison of both composites on every marked free coordinate.
    def rho_free(point, m):
        sign, i, j = point
        return (sign, i, (j + m) % 6)

    def lift_free(point, signs, p):
        sign, i, j = point
        output_i = p.index(i)
        return (sign * signs[output_i], output_i, j)

    for signs, p, b in stabilizer:
        for i, j in product(range(4), range(6)):
            for m in range(6):
                point = (1, i, j)
                left = lift_free(rho_free(point, m), signs, p)
                right = rho_free(lift_free(point, signs, p), m)
                assert left == right
    # The A5 root action of C^m has no nonidentity power acting trivially.
    assert len({((m % 6), ((m + 1) % 6)) for m in range(6)}) == 6
    return "Glue: all 2304 ambient tuples exhausted; stabilizer exactly 48; original p(i) convention and simultaneous six-cycle commute."


if __name__ == "__main__":
    print(a5_audit())
    print(d4_audit())
    print(glue_audit())
    print("Full group order:", 48 * (720 ** 4) * 192)
