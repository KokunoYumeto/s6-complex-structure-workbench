#!/usr/bin/env python3
"""Independent finite checks of the capacity-free shared-cutoff arguments.

Run with Python 3.10+ and no third-party dependencies:
    python check_walk.py > check_walk_output.json

Coverage:
1. Every one of the 2^16 labelled two-layer orders on A={0,1,2,3},
   B={4,5,6,7}, with arbitrary relations A -> B and no others, at m=4.
   A graph-dependent topological priority is obtained by repeatedly choosing
   the earliest available job in the template (0,4,1,5,2,6,3,7).
2. Seventy-two reproducible three-layer orders: 36 at m=4 and 36 at m=5.
   Each has three layers of m jobs; all adjacent-layer arcs are sampled by
   Python's seeded Random(20261023), with stated densities. This is a finite
   family, not an exhaustive assertion about three-layer orders.
3. One explicit order at each of m=4,5 whose shared-cutoff walk makes two
   advances during a single promotion; its construction is in the code.

For every order, the lexicographically first full schedule is computed
exactly by a subset recursion. The recursion considers every possible
minimal-job first block in lexicographic priority order, and recurses until
the first feasible continuation is found; memoization only removes repeated
remaining subsets. Thus it does not assume any separator result.

On every contiguous interval of that normalized schedule, every consecutive
pair of restricted priority prefixes and every separating starting position
(including its actual or virtual exterior left boundary) is checked.
The earliest-exception walk must end at a separator for both prefixes.
For every slot, every possible full schedule of its suffix is enumerated;
every proposed exchange with a better-priority later job is tested for
feasibility in the complete schedule. No such improving exchange may work.

These are reproducible finite checks, not the proof for arbitrary m or n.
"""

from functools import lru_cache
from itertools import combinations
from collections import Counter
from random import Random
import json


def bits(mask):
    while mask:
        low = mask & -mask
        yield low.bit_length() - 1
        mask ^= low


def transitive_predecessors(n, arcs):
    pred = [0] * n
    for u, v in arcs:
        assert 0 <= u < v < n
        pred[v] |= 1 << u
    for v in range(n):
        for u in list(bits(pred[v])):
            pred[v] |= pred[u]
    return tuple(pred)


def successor_masks(pred):
    succ = [0] * len(pred)
    for v, ancestors in enumerate(pred):
        for u in bits(ancestors):
            succ[u] |= 1 << v
    return tuple(succ)


def topological_priority(pred, template):
    remaining = (1 << len(pred)) - 1
    order = []
    while remaining:
        for v in template:
            if remaining >> v & 1 and not pred[v] & remaining:
                order.append(v)
                remaining ^= 1 << v
                break
        else:
            raise AssertionError('Cycle')
    return tuple(order)


def normalized_schedule(pred, m, priority, counters):
    @lru_cache(None)
    def solve(remaining):
        counters['normalization_subsets'] += 1
        if not remaining:
            return ()
        available = [v for v in priority
                     if remaining >> v & 1 and not pred[v] & remaining]
        for block in combinations(available, m):
            mask = sum(1 << v for v in block)
            suffix = solve(remaining ^ mask)
            if suffix is not None:
                return (mask,) + suffix
        return None

    return solve((1 << len(pred)) - 1)


def all_schedules_of_subset(pred, m, priority, remaining):
    if not remaining:
        yield ()
        return
    available = [v for v in priority
                 if remaining >> v & 1 and not pred[v] & remaining]
    for block in combinations(available, m):
        mask = sum(1 << v for v in block)
        for suffix in all_schedules_of_subset(pred, m, priority, remaining ^ mask):
            yield (mask,) + suffix


def feasible(pred, m, schedule):
    seen = 0
    for block in schedule:
        if block.bit_count() != m or block & seen:
            return False
        if any(pred[v] & ~seen for v in bits(block)):
            return False
        seen |= block
    return seen == (1 << len(pred)) - 1


def union_cones(block, cones):
    result = 0
    for v in bits(block):
        result |= cones[v]
    return result


def check_shared_walk(pred, m, priority, schedule, counters):
    succ = successor_masks(pred)
    whole = (1 << len(pred)) - 1
    for left in range(len(schedule)):
        for right in range(left + 1, len(schedule) + 1):
            domain = schedule[left:right]
            universe = 0
            for block in domain:
                universe |= block
            restricted = [v for v in priority if universe >> v & 1]
            prefix = [0]
            for v in restricted:
                prefix.append(prefix[-1] | 1 << v)
            before = []
            mask = 0
            for block in domain:
                before.append(mask)
                mask |= block
            after = [universe ^ (before[i] | domain[i])
                     for i in range(len(domain))]
            dcone = [union_cones(block, succ) for block in domain]
            pcone = [union_cones(block, pred) for block in domain]
            exterior_d = (whole if left == 0
                          else union_cones(schedule[left - 1], succ))

            def high_condition(position, low):
                if position == -1:
                    return True
                return not (before[position] & ~low & ~pcone[position])

            def low_exceptions(position, low):
                if position == -1:
                    return universe & low & ~exterior_d
                return after[position] & low & ~dcone[position]

            def separator(position, low):
                return (high_condition(position, low)
                        and not low_exceptions(position, low))

            counters['interval_domains'] += 1
            for old, new in zip(prefix, prefix[1:]):
                for start in range(-1, len(domain)):
                    if not separator(start, old):
                        continue
                    counters['shared_cutoff_premises'] += 1
                    current = start
                    advances = 0
                    while exceptions := low_exceptions(current, new):
                        assert high_condition(current, new)
                        target = next(i for i in range(current + 1, len(domain))
                                      if domain[i] & exceptions)
                        assert target > current
                        current = target
                        advances += 1
                        assert high_condition(current, old)
                        assert high_condition(current, new)
                    assert separator(current, old)
                    assert separator(current, new)
                    counters['walk_advances'] += advances
                    counters['walks_with_advance'] += (advances > 0)
                    counters['walks_with_multiple_advances'] += (advances > 1)


def check_suffix_exchange(pred, m, priority, schedule, counters):
    rank = {v: i for i, v in enumerate(priority)}
    for r in range(len(schedule)):
        suffix_jobs = 0
        for block in schedule[r + 1:]:
            suffix_jobs |= block
        for suffix in all_schedules_of_subset(pred, m, priority, suffix_jobs):
            reordered = schedule[:r + 1] + suffix
            assert feasible(pred, m, reordered)
            counters['suffix_reorderings'] += 1
            for later in range(r + 1, len(reordered)):
                for y in bits(reordered[r]):
                    for x in bits(reordered[later]):
                        if rank[x] >= rank[y]:
                            continue
                        counters['improving_exchange_candidates'] += 1
                        exchanged = list(reordered)
                        exchanged[r] ^= (1 << y) | (1 << x)
                        exchanged[later] ^= (1 << y) | (1 << x)
                        assert not feasible(pred, m, exchanged), {
                            'm': m, 'pred': pred, 'priority': priority,
                            'schedule': schedule, 'reordered': reordered,
                            'r': r, 'later': later, 'x': x, 'y': y}


def check_case(pred, m, priority, counters):
    schedule = normalized_schedule(pred, m, priority, counters)
    assert schedule is not None
    assert feasible(pred, m, schedule)
    counters['orders'] += 1
    check_shared_walk(pred, m, priority, schedule, counters)
    check_suffix_exchange(pred, m, priority, schedule, counters)


def exhaustive_two_layer_four():
    counters = Counter()
    template = (0, 4, 1, 5, 2, 6, 3, 7)
    for edges in range(1 << 16):
        arcs = [(u, 4 + v) for u in range(4) for v in range(4)
                if edges >> (4 * u + v) & 1]
        pred = transitive_predecessors(8, arcs)
        priority = topological_priority(pred, template)
        check_case(pred, 4, priority, counters)
    assert counters['orders'] == 65536
    return dict(counters)


def deterministic_three_layer_cases():
    rng = Random(20261023)
    results = {}
    for m in (4, 5):
        counters = Counter()
        for density in (0.0, 0.05, 0.15, 0.3, 0.6, 1.0):
            for repetition in range(6):
                arcs = [(layer * m + u, (layer + 1) * m + v)
                        for layer in range(2) for u in range(m) for v in range(m)
                        if rng.random() < density]
                pred = transitive_predecessors(3 * m, arcs)
                template = list(range(3 * m))
                rng.shuffle(template)
                priority = topological_priority(pred, template)
                check_case(pred, m, priority, counters)
        assert counters['orders'] == 36
        results[str(m)] = dict(counters)
    return results


def forced_multiple_advance_cases():
    results = {}
    for m in (4, 5):
        # Boundary A is first. In the remaining two slots all m jobs of B
        # have a successor, so B must be the first entire slot and C the
        # second. In C, x=2m is low and descends from A but not from B.
        # Promoting p=m moves the separator A -> B -> C in one walk.
        alpha, p, q, r, x, u, v = 0, m, m + 1, m + 2, 2*m, 2*m + 1, 2*m + 2
        arcs = [(alpha, x), (p, u), (q, u), (r, v)]
        arcs += [(m + j, 2*m + j) for j in range(3, m)]
        pred = transitive_predecessors(3 * m, arcs)
        priority = tuple(range(m)) + (x,) + tuple(range(m, 2*m)) + tuple(range(2*m + 1, 3*m))
        counters = Counter()
        check_case(pred, m, priority, counters)
        assert counters['walks_with_multiple_advances'] > 0
        results[str(m)] = dict(counters)
    return results


def main():
    exhaustive = exhaustive_two_layer_four()
    layered = deterministic_three_layer_cases()
    forced = forced_multiple_advance_cases()
    print(json.dumps({
        'status': 'All asserted checks passed.',
        'exhaustive_two_layer_m4': exhaustive,
        'deterministic_three_layer': layered,
        'forced_multiple_advance': forced,
        'violations': 0,
        'scope': 'Finite verification only; the all-instance results are proved in the accompanying mathematical argument.'
    }, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
