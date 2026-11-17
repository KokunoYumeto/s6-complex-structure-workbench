"""Exact finite checks for the truncated canonical-order reduction.

The geometric component-selection lemma is proved in the accompanying text.
This program checks its actual canonical-order updates, the protected Hopf
cards, the full lexicographic potential, and the endpoint branch arithmetic.
All quantities are integers; no floating-point calculation is used.
"""

from itertools import product


def potential(cards, bound):
    return tuple(sum(x == j for x in cards) for j in range(1, bound + 1))


count_moves = 0
count_below_h = 0
for bound in range(2, 9):
    for h in range(1, bound):
        for q in range(1, bound + 1):
            for additions in range(5):
                if q == bound and additions:
                    continue
                before = [0, h, q, bound]
                # Keep the marked Hopf card at index 1, even when q=h.
                after = before[:2] + before[3:] + [q + 1] * additions
                assert after[0] == 0 and after[1] == h
                assert max(after) <= bound
                assert potential(after, bound) < potential(before, bound)
                count_moves += 1
                if q <= h:
                    count_below_h += 1
                    # The height is not itself required to exceed h.
                    assert min(after) == 0
print("Protected Hopf cards and full finite-level decreases:", count_moves, "PASS")
print("Allowed lower/equal-Hopf removal orders among these:", count_below_h, "PASS")


def run_record(bound, h, extra, strategy):
    # Entries are (canonical order, protected-Hopf marker).
    deck = [(0, False), (h, True)] + [(x, False) for x in extra]
    steps = 0
    protected = tuple(x for x, flag in deck if flag)
    while max(x for x, _ in deck) > h:
        current_max = max(x for x, _ in deck)
        candidates = [i for i, (x, flag) in enumerate(deck) if x > 0 and not flag]
        assert candidates
        if strategy == 0:
            chosen = min(candidates, key=lambda i: deck[i][0])
        elif strategy == 1:
            chosen = max(candidates, key=lambda i: deck[i][0])
        else:
            chosen = candidates[(steps * 7 + h) % len(candidates)]
        q, _ = deck[chosen]
        old = potential([x for x, _ in deck], bound)
        additions = 0 if q == current_max else (steps + q + strategy) % 3
        deck.pop(chosen)
        deck.extend((q + 1, False) for _ in range(additions))
        assert potential([x for x, _ in deck], bound) < old
        assert max(x for x, _ in deck) <= current_max
        assert tuple(x for x, flag in deck if flag) == protected
        assert any(x == 0 for x, _ in deck)
        steps += 1
    assert max(x for x, _ in deck) == h
    return steps


records = total_steps = longest = 0
for bound in range(2, 8):
    for h in range(1, bound):
        for extras in product(range(bound + 1), repeat=2):
            for strategy in range(3):
                steps = run_record(bound, h, extras + (bound,), strategy)
                records += 1
                total_steps += steps
                longest = max(longest, steps)
print("Complete stopped records:", records, "; steps:", total_steps,
      "; longest:", longest, "PASS")

# A removal candidate can lie below the stopping level. Counting only
# components above h does not give a strict potential for that operation.
h, bound, q = 3, 5, 1
before = [0, h, q, bound]
after = [0, h, bound, q + 1, q + 1]
upper_before = tuple(before.count(j) for j in range(h + 1, bound + 1))
upper_after = tuple(after.count(j) for j in range(h + 1, bound + 1))
assert upper_before == upper_after
assert potential(after, bound) < potential(before, bound)
print("Why the full positive card vector is required: explicit unchanged upper vector PASS")

# Restriction to a ruling fibre: the unique section coefficient is -2,
# hence its parent has order q-1. A terminal plane line has coefficient
# -3, hence its parent has order q-2. Thus no order-zero component is removed.
ruled = planes = 0
for q in range(101):
    for parent in range(101):
        if parent - q - 1 == -2:
            assert q == parent + 1 and q >= 1
            ruled += 1
        if parent - q - 1 == -3:
            assert q == parent + 2 and q >= 2
            planes += 1
print("Exact section/plane restriction orders:", ruled, planes, "PASS")

# Once h is the global maximum, both preimages of a self-double branch
# have coefficient one. Rational coefficient-one leaves have one triple;
# two negative integral self-squares cannot add to -1.
negative_pairs = 0
for x in range(-100, 0):
    for y in range(-100, 0):
        assert x + y != -1
        negative_pairs += 1
print("Rational maximal-Hopf self-branch square exclusion:", negative_pairs, "PASS")

# If both receiving branches of a type-II move belong to one Hopf at
# the maximum h, the exact canonical height balance forces both sides
# to have height h as well; their coefficient-one curves cannot meet.
height_balances = 0
for h in range(1, 61):
    for a in range(h + 1):
        b = 2 * h - a
        if 0 <= b <= h:
            assert a == b == h
            assert h - a + 1 == h - b + 1 == 1
            height_balances += 1
print("Exact type-II same-maximal-Hopf height balances:", height_balances, "PASS")
print("ALL EXACT TRUNCATED-REDUCTION CHECKS PASSED")
