"""Exact cyclic convolution for the LP local finite-character calculation.

This checks the newly derived local expression. It assigns no P invariant
to the actual manifold, because the characteristic cobordism is still open.
"""
from fractions import Fraction


def cyclic_terms(order, terms):
    result = [0] * order
    for power, coefficient in terms:
        result[power % order] += coefficient
    return result


def product(left, right):
    n = len(left)
    assert len(right) == n
    return cyclic_terms(n, ((i+j, a*b) for i, a in enumerate(left)
                           for j, b in enumerate(right)))


count = 0
for exponent in range(2, 8):
    c = 2**exponent
    h = c//2
    for odd in (1, 3, 5, 7):
        d = c*odd
        numerator = cyclic_terms(h, ((-6*j-3, 1) for j in range(d)))
        denominator = cyclic_terms(h, ((0, 2), (1, -1), (-1, -1)))
        character = [odd if r % 2 else 0 for r in range(h)]
        multiplied = product(denominator, character)
        residual = [a-b for a, b in zip(multiplied, numerator)]
        assert residual == [-2*odd] * h
        assert character[0] == 0
        assert sum(character) == d//4
        augmentation = (-6*sum(character)) % c
        assert augmentation == c//2
        difference = -Fraction(d, 2*c)
        assert difference.denominator == 2
        assert (6*h) % c == 0
        print(f'd={d} c={c} h={h}: order-c coefficient difference={difference}; '
              f'D_h H-N_h={residual[0]} R_h; '
              f'augmentation={sum(character)}; -6 augmentation mod c={augmentation}')
        count += 1

print(f'PASS: {count} exact convolution cases; full-order obstruction retained.')
print('The unbounded coefficient proofs are in the companion note.')
print('NO MANIFOLD P VALUE: the characteristic-cobordism gate remains open.')
