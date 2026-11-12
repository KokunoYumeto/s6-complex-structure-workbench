"""Exact checks of explicit image witnesses and independent bounded exploration.

The global theorem is proved algebraically in THREE_LINE_IMAGE_PROOF.md.
The divisor/three-square exploration is retained as development provenance,
but neither the theorem nor the explicit reconstruction depends on it.
"""

from math import isqrt


def divisors(n):
    ds = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            ds.append(d)
            if d * d != n:
                ds.append(n // d)
    return sorted(ds)


def three_square_admissible(s):
    if s < 0:
        return False
    if s == 0:
        return True
    while s % 4 == 0:
        s //= 4
    return s % 8 != 7


def candidate_data(n):
    if n == 0:
        return [(0, 0, True)]
    out = []
    for d in divisors(abs(n)):
        for x in (-d, d):
            numerator = x * x - n // x
            if numerator % 3:
                continue
            s = numerator // 3
            if s % 2 != x % 2:
                continue
            out.append((x, s, three_square_admissible(s)))
    return out


def admissible(n):
    return n % 2 == 0 and (n % 3 != 0 or n % 9 == 0)


def polynomial(a):
    x, y, z, w = a
    return x * (x * x - 3 * (y * y + z * z + w * w))


def explicit_witness(n):
    if not admissible(n):
        return None
    if n % 18 == 0:
        h = n // 18
        return (-3 * h, h + 1, h - 1, h)
    h = n // 2
    epsilon = 1 if h % 3 == 1 else -1
    r = (h - epsilon) // 3
    return (-3 * r - epsilon, r, r, r + epsilon)


def main():
    limit = 10000
    for n in range(-limit, limit + 1):
        witness = explicit_witness(n)
        assert (witness is not None) == admissible(n)
        if witness is not None:
            assert sum(witness) == 0
            assert polynomial(witness) == n
    print(f"Explicit original-coordinate witnesses checked for every integer in [{-limit}, {limit}].")
    missing = [n for n in range(2, limit + 1, 2)
               if admissible(n) and not any(ok for _, _, ok in candidate_data(n))]
    print(f"Locally admissible positive integers omitted by divisor/three-square criterion through {limit}:")
    print(missing)
    assert not missing
    line_direction = (-3, 1, 1, 1)
    assert sum(line_direction) == 0 and polynomial(line_direction) == 0
    for r in range(-limit, limit + 1):
        for epsilon in (-1, 1):
            a = (-3 * r - epsilon, r, r, r + epsilon)
            assert sum(a) == 0 and polynomial(a) == 6 * r + 2 * epsilon
        a = (-3 * r, r + 1, r - 1, r)
        assert sum(a) == 0 and polynomial(a) == 18 * r
    for x in range(-8, 9):
        for y in range(-8, 9):
            for z in range(-8, 9):
                for w in range(-8, 9):
                    if (x + y + z + w) % 2 == 0:
                        assert admissible(polynomial((x, y, z, w)))
    print("All three line identities checked on parameters -10000 through 10000.")
    print("Necessity checked on every D4 vector in the original coordinate box [-8,8]^4.")
    print("Exact proved global residue classes modulo 18: [0, 2, 4, 8, 10, 14, 16].")


if __name__ == "__main__":
    main()
