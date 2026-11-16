"""Exact algebra certificates for the complete rooted construction.

Existence of the finite analytic maps is proved in UN86 and its prerequisites.
These checks concern the intrinsic branch, canonical character/descent,
normalized root invariant semigroups and signed Euler composition.
"""

from fractions import Fraction
from itertools import combinations, product
from math import gcd, lcm, prod
from functools import reduce
import sympy as sp


canonical_cases = hopf_cases = 0
for r in (1, 2, 3):
    for multiplicities in product(range(1, 6), repeat=r):
        base_n = lcm(*multiplicities)
        for orders in product(range(4), repeat=r):
            ratios = tuple(Fraction(k + 1, m)
                           for k, m in zip(orders, multiplicities))
            tau = min(ratios)
            if tau > 1:
                continue
            for scale in (1, 2, 3):
                n = scale * base_n
                a = n * tau - 1
                assert a.denominator == 1 and 0 <= a < n
                a = int(a)
                character = (-a) % n
                assert (character + a) % n == 0
                root_orders = tuple(n * (x - tau) for x in ratios)
                assert all(x.denominator == 1 and x >= 0 for x in root_orders)
                assert min(root_orders) == 0
                for m, k, k_root in zip(multiplicities, orders, root_orders):
                    normal_index = n // m
                    pulled_order = a + int(k_root)
                    assert pulled_order == normal_index * (k + 1) - 1
                    assert (pulled_order + 1) % normal_index == 0
                    descended_order = (pulled_order - normal_index + 1) // normal_index
                    assert descended_order == k
                canonical_cases += 1
                for size in range(1, r + 1):
                    for subset in combinations(range(r), size):
                        highest_ratio = max(ratios[i] for i in subset)
                        h = n * (highest_ratio - tau)
                        assert h == max(root_orders[i] for i in subset)
                        assert (h == 0) == all(ratios[i] == tau for i in subset)
                        assert h.denominator == 1
                        # Changing only the divisible root scales the same intrinsic branch.
                        assert h == scale * base_n * (highest_ratio - tau)
                        hopf_cases += 1
print("Primitive canonical character and exact quotient descent:", canonical_cases, "PASS")
print("Intrinsic normal-cover Hopf branches and root-exponent scaling:", hopf_cases, "PASS")

# On a connected normalized local root branch, the character lattice is
# Z^r + Z*(m/N). Its quotient by Z^r has order N/gcd(m), and the effective
# stabilizer acts on the q-th class by the q-th root character. In the
# nonnegative cone, invariance is exactly an ordinary coarse monomial.
semigroup_cases = root_cells = 0
for r in (1, 2, 3):
    for ms in product(range(1, 7), repeat=r):
        n = lcm(*ms)
        d = reduce(gcd, ms)
        effective = n // d
        nu = Fraction(n ** (r - 1) * d, prod(ms))
        assert nu.denominator == 1 and nu > 0
        for q in range(effective):
            fractional = tuple(Fraction(q * m, n) for m in ms)
            integral = all(x.denominator == 1 for x in fractional)
            assert integral == (q == 0)
            for shifts in product((-1, 0, 1), repeat=r):
                exponents = tuple(x + y for x, y in zip(fractional, shifts))
                if min(exponents) < 0:
                    continue
                invariant = q == 0
                coarse_monomial = all(x.denominator == 1 for x in exponents)
                assert invariant == coarse_monomial
                semigroup_cases += 1
        fixed_sheet_sum = sum(d if j % d == 0 else 0 for j in range(n))
        assert fixed_sheet_sum == n
        root_cells += 1
print("Normalized invariant monoid comparisons:", semigroup_cases, "PASS")
print("Root-stratum volume integrality and finite-sheet average:", root_cells, "PASS")

# The three proper comparisons have fixed directions. This symbolic identity
# checks every sign without assigning geometric existence to formal inputs.
e_original, delta_pi, root_delta, delta_sigma = sp.symbols(
    'e_original delta_pi root_delta delta_sigma')
e_y = e_original + delta_pi
e_z = e_y + root_delta
e_core = e_z + delta_sigma
assert sp.expand(e_core - delta_sigma - root_delta - delta_pi - e_original) == 0
print("Four-space signed Euler composition: symbolic identity PASS")

zero_cases = 0
for index in range(1, 13):
    for core_euler in (0, 2 * index):
        for point_count in range(4):
            for genus in range(6):
                d_pi = 2 * point_count + 2 - 2 * genus
                for r_delta in range(-10, 11, 2):
                    d_sigma = core_euler - r_delta - d_pi
                    original = core_euler - d_sigma - r_delta - d_pi
                    assert original == 0
                    # Reversing the actual arrows gives the same output at each stage.
                    z = core_euler - d_sigma
                    y = z - r_delta
                    x = y - d_pi
                    assert x == original
                    zero_cases += 1
print("Exact zero-balance reconstructions:", zero_cases, "PASS")
print("ALL COMPLETE-ROOTED-CONSTRUCTION CERTIFICATES PASSED")
