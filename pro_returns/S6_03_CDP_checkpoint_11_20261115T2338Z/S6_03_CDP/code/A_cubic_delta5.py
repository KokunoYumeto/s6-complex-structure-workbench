"""Exact suspension invariants for reduced plane germs with delta <= 5.

The plane-germ classification is proved in C.2.RAT.6. This script evaluates
the weighted geometric-genus and monodromy formulas using rational arithmetic.
It extends, independently, the delta-four budget in root_cubic_normal_cone.py.
"""
from fractions import Fraction as Q
from itertools import product


def plane_rows():
    rows = []
    for n in range(1, 11):
        rows.append((f"A{n}", Q(1, 2), Q(1, n + 1),
                     [(0, j) for j in range(n)], (n + 1) // 2,
                     2 if n % 2 else 1))
    for n in range(4, 10):
        rows.append((f"D{n}", Q(n - 2, 2 * (n - 1)), Q(1, n - 1),
                     [(0, j) for j in range(n - 1)] + [(1, 0)],
                     (n + 2) // 2, 3 if n % 2 == 0 else 2))
    rows.extend([
        ("E6", Q(1, 3), Q(1, 4), list(product(range(2), range(3))), 3, 1),
        ("E7", Q(1, 3), Q(2, 9),
         [(0, j) for j in range(5)] + [(1, 0), (1, 1)], 4, 2),
        ("E8", Q(1, 3), Q(1, 5), list(product(range(2), range(4))), 4, 1),
    ])
    return rows


def compute():
    output = []
    for name, wx, wy, basis, delta, branches in plane_rows():
        assert len(basis) == 2 * delta - branches + 1
        lower = [(i, j, k) for i, j, k in product(range(12), repeat=3)
                 if (i + 1) * wx + (j + 1) * wy + Q(k + 1, 3) <= 1]
        eigen_exponents = [(i + 1) * wx + (j + 1) * wy for i, j in basis]
        link_b1 = sum(a - int(a) in (Q(1, 3), Q(2, 3))
                      for a in eigen_exponents)
        pg = len(lower)
        assert pg <= 1
        assert pg == 0 or delta >= 3
        assert link_b1 in (0, 2)
        assert (link_b1 == 2) == (name in ("A5", "D4"))
        output.append(dict(name=name, wx=wx, wy=wy, delta=delta,
                           branches=branches, mu=len(basis), pg=pg,
                           link_b1=link_b1, lower=lower))
    return output


def collections(rows):
    def walk(first, total, items):
        yield items
        for index in range(first, len(rows)):
            row = rows[index]
            if total + row["delta"] <= 5:
                yield from walk(index, total + row["delta"], items + [row])
    yield from walk(0, 0, [])


if __name__ == "__main__":
    data = compute()
    print("type; normalized weights (x,y,z); delta; branches; mu; pg; b1(link); lower monomials")
    for row in data:
        print(f'{row["name"]}; ({row["wx"]},{row["wy"]},1/3); '
              f'{row["delta"]}; {row["branches"]}; {row["mu"]}; '
              f'{row["pg"]}; {row["link_b1"]}; {row["lower"]}')
    all_collections = list(collections(data))
    for terms in all_collections:
        assert sum(r["pg"] for r in terms) <= 1
        assert sum(r["link_b1"] for r in terms) <= 2
    print(f"Checked {len(all_collections)} unordered singularity collections of total delta <=5.")
    print("Every collection has total geometric genus <=1 and total link b1 <=2.")
    print("The only local nonzero link b1 cases are A5 and D4, each of delta 3.")
    print("PASS")
