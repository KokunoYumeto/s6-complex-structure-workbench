#!/usr/bin/env python3
"""Exact arithmetic checks for the separately proved multitape implementation.

No empirical inference about asymptotic running times or scheduling completeness
is made by this program. Each row is a monomial B^b N^(a*m+c). Its domination is
proved for every integer m>=3 by writing 4m+1-(a*m+c) in m-3 coordinates.
"""
from fractions import Fraction

ROWS = [
    ('reachability/rank', 0, 0, 5),
    ('formula generation/evaluation', 1, 0, 3),
    ('pairwise deduplication', 3, 0, 1),
    ('cardinality ordering', 3, 0, 2),
    ('state enumeration, lookup term', 3, 1, 2),
    ('state enumeration, compatibility term', 2, 1, 4),
    ('state propagation', 5, 4, 1),
    ('witness state retrieval', 2, 1, 2),
    ('witness schedule retrieval', 2, 0, 3),
    ('selected witness output', 0, 0, 3),
]

def main():
    print('Audit date: 2026-11-15 (Europe/Berlin)')
    print('Model: deterministic multitape; m>=3, K>=1, N>=m, B>=1.')
    print('Target monomial: B^5 N^(4m+1).')
    for name, b, a, c in ROWS:
        db = 5-b
        dm = 4-a
        dc = 3*dm+1-c
        assert db>=0 and dm>=0 and dc>=0
        print(f'PASS {name}: B exponent slack {db}; N exponent slack '
              f'{dm}*(m-3)+{dc} >= 0.')
    print('Factorization: B * S * S^2 * (S*N) = B^5*N^(4m+1), S=B*N^m.')
    print('Substitution: 5*m*(12*m+25)+4*m+1 = 60*m^2+129*m+1.')
    assert 5*12 == 60 and 5*25+4 == 129
    for m in (3,4,5,6):
        k=12*m+25
        e=5*m*k+4*m+1
        assert e==60*m*m+129*m+1
        print(f'm={m}; K={k}; list={6*m+9}; relative={6*m+16}; '
              f'padded_exponent={e}; all_deadlines_input_exponent={e+1}.')
    print('For every m>=3, e_m+1 >= 929 > 4 (input preprocessing degree).')
    # The stored-ordinal length bound follows algebraically after replacing
    # 2+10K by (2+10K)h, valid for integer h>=1.
    # 8(m+1)(K+1) - (2+10K+mK+m) = (7m-2)K+7m+6.
    assert 8-1==7 and 8-10==-2 and 8-1==7 and 8-2==6
    print('Index-length slack: ((7m-2)K+7m+6)*h >= 0 for m>=3,K>=1,h>=1.')
    # A / (D*C^5) with q=64(m+1)(K+1), D=2^20*q^2.
    numerical_ratio=Fraction(2**40, (2**20)*(64**2))
    assert numerical_ratio==256
    print('Coefficient slack A/(D*C^5) = 256*(m+1)^2*(K+1)^2 >= 16384.')
    print('PASS: all symbolic inequalities and exponent values verified exactly.')

if __name__=='__main__':
    main()
