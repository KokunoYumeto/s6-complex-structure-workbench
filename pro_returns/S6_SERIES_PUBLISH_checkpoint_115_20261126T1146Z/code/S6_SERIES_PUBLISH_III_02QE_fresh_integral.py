#!/usr/bin/env python3
"""Fresh exact-integer arithmetic for the supplied 02QE statement data.

This program reads no manuscript, prior proof, check event or previous output.
It constructs the supplied exterior forms, computes all integer minors, and
checks explicit unimodular and image certificates. The global covering maps
and their full integral pullback lattices remain outside this calculation.
"""

from argparse import ArgumentParser
from datetime import datetime, timezone
from itertools import combinations, permutations
from math import gcd
from pathlib import Path
import json


def sign_of(sequence):
    return -1 if sum(sequence[i] > sequence[j]
                     for i in range(len(sequence))
                     for j in range(i + 1, len(sequence))) % 2 else 1


def wedge(left, right):
    result = {}
    for a, ca in left.items():
        for b, cb in right.items():
            word = a + b
            if len(set(word)) != len(word):
                continue
            key = tuple(sorted(word))
            result[key] = result.get(key, 0) + ca * cb * sign_of(word)
    return {key: value for key, value in result.items() if value}


def add_forms(*terms):
    result = {}
    for coefficient, form in terms:
        for key, value in form.items():
            result[key] = result.get(key, 0) + coefficient * value
    return {key: value for key, value in result.items() if value}


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def multiply(left, right):
    assert left and right and len(left[0]) == len(right)
    return [[sum(left[i][k] * right[k][j] for k in range(len(right)))
             for j in range(len(right[0]))] for i in range(len(left))]


def apply(matrix, vector):
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def identity(size):
    return [[int(i == j) for j in range(size)] for i in range(size)]


def determinant(matrix):
    size = len(matrix)
    assert all(len(row) == size for row in matrix)
    answer = 0
    for permutation in permutations(range(size)):
        term = sign_of(permutation)
        for row, column in enumerate(permutation):
            term *= matrix[row][column]
        answer += term
    return answer


def determinantal_divisors(matrix):
    """Enumerate every minor using integer Leibniz determinants."""
    divisors, counts, nonzero_counts = [1], [], []
    for size in range(1, min(len(matrix), len(matrix[0])) + 1):
        divisor, count, nonzero = 0, 0, 0
        for rows in combinations(range(len(matrix)), size):
            for columns in combinations(range(len(matrix[0])), size):
                minor = [[matrix[i][j] for j in columns] for i in rows]
                value = determinant(minor)
                divisor = gcd(divisor, abs(value))
                count += 1
                nonzero += value != 0
        divisors.append(divisor)
        counts.append(count)
        nonzero_counts.append(nonzero)
    rank = max(i for i, divisor in enumerate(divisors) if divisor)
    entries = [divisors[i] // divisors[i - 1] for i in range(1, rank + 1)]
    assert all(divisors[i] % divisors[i - 1] == 0 for i in range(1, rank + 1))
    assert all(entries[i + 1] % entries[i] == 0 for i in range(len(entries) - 1))
    return dict(rank=rank, determinantal_divisors=divisors,
                smith_nonzero_entries=entries, minors_by_size=counts,
                nonzero_minors_by_size=nonzero_counts)


def smith_certificate(original):
    """Construct the unit-pivot certificate, tracking both integral bases."""
    matrix = [row[:] for row in original]
    left, right = identity(4), identity(4)
    operations = []

    def row_add(target, source, multiple):
        for block in (matrix, left):
            block[target] = [x + multiple * y
                             for x, y in zip(block[target], block[source])]
        operations.append(f'R{target + 1} <- R{target + 1} + ({multiple}) R{source + 1}')

    def row_swap(a, b):
        for block in (matrix, left):
            block[a], block[b] = block[b], block[a]
        operations.append(f'R{a + 1} <-> R{b + 1}')

    def column_add(target, source, multiple):
        for block in (matrix, right):
            for row in block:
                row[target] += multiple * row[source]
        operations.append(f'C{target + 1} <- C{target + 1} + ({multiple}) C{source + 1}')

    def column_swap(a, b):
        for block in (matrix, right):
            for row in block:
                row[a], row[b] = row[b], row[a]
        operations.append(f'C{a + 1} <-> C{b + 1}')

    row_add(2, 0, 2)
    column_swap(1, 3)
    row_add(3, 1, 1)
    row_swap(2, 3)
    row_add(1, 2, 2)
    column_add(3, 2, 1)
    column_add(3, 1, 6)
    expected = [[int(i == j and i < 3) for j in range(4)] for i in range(4)]
    assert matrix == expected
    assert multiply(multiply(left, original), right) == expected
    assert abs(determinant(left)) == abs(determinant(right)) == 1
    kernel = [row[3] for row in right]
    assert apply(original, kernel) == [0, 0, 0, 0]
    return dict(left=left, right=right, diagonal=matrix,
                left_determinant=determinant(left),
                right_determinant=determinant(right),
                integer_kernel_generator=kernel, operations=operations)


def calculate():
    generators = [{(i,): 1} for i in range(4)]
    gamma, u, w, delta = generators
    h3_words = list(combinations(range(4), 3))
    h3_basis = [{word: 1} for word in h3_words]
    product = lambda a, b, c: wedge(wedge(a, b), c)
    b = product(gamma, u, w)
    c1 = add_forms((1, product(u, w, delta)),
                   (-4, product(gamma, u, delta)),
                   (-2, product(gamma, w, delta)))
    c2 = add_forms((1, product(u, w, delta)),
                   (-3, product(gamma, u, delta)),
                   (-3, product(gamma, w, delta)))
    coordinates = lambda form: [form.get(word, 0) for word in h3_words]
    b_vector, c1_vector, c2_vector = map(coordinates, (b, c1, c2))
    dual3 = [b_vector, c1_vector]
    dual4 = [[2 * x for x in b_vector], c2_vector]
    alpha3 = dual3 + [[-x for x in row] for row in dual4]
    assert alpha3 == [[1, 0, 0, 0], [0, -4, -2, 1],
                      [-2, 0, 0, 0], [0, 3, 3, -1]]

    minors = determinantal_divisors(alpha3)
    certificate = smith_certificate(alpha3)
    assert minors['rank'] == 3
    assert minors['smith_nonzero_entries'] == [1, 1, 1]
    assert certificate['integer_kernel_generator'] == [0, 1, 1, 6]

    # Columns give preimages of (1,0,-2,0), (0,1,0,0), (0,0,0,1).
    image_preimages = [[1, 0, 0], [0, 0, 0], [0, 1, 1], [0, 3, 2]]
    image_basis = [[1, 0, 0], [0, 1, 0], [-2, 0, 0], [0, 0, 1]]
    assert multiply(alpha3, image_preimages) == image_basis
    assert apply(transpose(alpha3), [2, 0, 1, 0]) == [0, 0, 0, 0]

    dual3_minors, dual4_minors = map(determinantal_divisors, (dual3, dual4))
    assert dual3_minors['smith_nonzero_entries'] == [1, 1]
    assert dual4_minors['smith_nonzero_entries'] == [1, 2]
    first = [1, 0, 0, 0]
    fourth = [0, 0, 0, 1]
    assert apply(dual3, first) == [1, 0]
    assert apply(dual3, fourth) == [0, 1]
    assert apply(dual4, first) == [2, 0]
    assert apply(dual4, fourth) == [0, 1]
    assert all(x % 2 == 0 for x in dual4[0])

    # Exact basis conversion: v -> (xi -> coefficient of v wedge xi in vol).
    pairing = [[wedge(v, xi).get((0, 1, 2, 3), 0)
                for xi in h3_basis] for v in generators]
    to_evaluation = transpose(pairing)
    assert multiply(pairing, to_evaluation) == identity(4)
    kernel_in_v = apply(pairing, certificate['integer_kernel_generator'])
    assert kernel_in_v == [6, -1, 1, 0]
    assert apply(multiply(alpha3, to_evaluation), kernel_in_v) == [0, 0, 0, 0]

    return dict(
        target='02QE / mapsaudit:finite-degree-three',
        scope='Fresh integer/exterior-algebra derivation from the supplied statement data only; no target proof or prior check outcome opened.',
        geometric_status='Awaiting exact global covering definitions, full integral pullback lattices, and homology basis/torsion data. Full target not claimed.',
        h1_basis=['gamma', 'u', 'w', 'delta'],
        volume='gamma wedge u wedge w wedge delta',
        h3_basis=['gamma u w', 'gamma u delta', 'gamma w delta', 'u w delta'],
        b=b_vector, c1=c1_vector, c2=c2_vector,
        supplied_pullback_generator_columns_3=transpose(dual3),
        supplied_pullback_generator_columns_4=transpose(dual4),
        dual_map_3=dual3, dual_map_4=dual4,
        dual_map_3_minors=dual3_minors, dual_map_4_minors=dual4_minors,
        dual_map_3_image='Z^2', dual_map_3_image_index=1,
        dual_map_4_image='2Z direct_sum Z', dual_map_4_image_index=2,
        alpha3=alpha3, alpha3_minors=minors, alpha3_smith_certificate=certificate,
        alpha3_image_basis_columns=image_basis,
        alpha3_image_preimage_columns=image_preimages,
        alpha3_image_equation='2*y1 + y3 = 0',
        alpha3_cokernel='Z, with quotient map y -> 2*y1 + y3',
        volume_pairing_rows_h1_columns_h3=pairing,
        h1_to_h3_evaluation_coordinates=to_evaluation,
        alpha3_kernel_in_evaluation_coordinates=[0, 1, 1, 6],
        alpha3_kernel_after_volume_pairing=[6, -1, 1, 0],
        coordinate_scope='The first kernel is in the four-column matrix domain. The second is its exact preimage under the displayed volume-pairing isomorphism; neither is silently identified with an unprovided geometric basis.',
    )


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path(__file__).resolve().parents[1] /
                        'agents/continuation4_iii_reductions/S6_SERIES_PUBLISH_III_02QE_fresh_integral.json')
    args = parser.parse_args()
    result = calculate()
    result['completed_utc'] = datetime.now(timezone.utc).isoformat()
    result['program'] = 'code/S6_SERIES_PUBLISH_III_02QE_fresh_integral.py'
    result['attribution'] = 'GPT-6 Astra (OpenAI), ChatGPT Pro mode; effort setting not separately exposed; fourth-continuation III reductions'
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print('alpha3 Smith entries:', result['alpha3_minors']['smith_nonzero_entries'])
    print('alpha3 integer kernel:', result['alpha3_smith_certificate']['integer_kernel_generator'])
    print('dual matrix image indices:', result['dual_map_3_image_index'], result['dual_map_4_image_index'])
    print('Geometric covering premises: awaiting exact safe setup packet.')
    print(args.output)


if __name__ == '__main__':
    main()
