#!/usr/bin/env python3
"""Postrelease exact coefficient propagation in the retained 02X9 proof.

Geometric invariance and saddle incidence are proved in the comparison.
The slack-variable formulas cover all nonnegative integral multiplicities.
"""
import json
import sympy as s


def main():
    u,w=s.symbols('u w',integer=True,nonnegative=True)
    coefficient_regular=s.expand(w+1)
    coefficient_saddle=s.expand((1+u)+w+0)
    assert s.expand(coefficient_regular-1)==w
    assert s.expand(coefficient_saddle-1)==u+w
    degree,k=s.symbols('degree k',integer=True,positive=True)
    covered_blowups=degree*k
    assert s.expand(covered_blowups/degree)==k
    print(json.dumps({
        'tag':'02X9','phase':'after target-proof release',
        'regular_center':{'pullback_multiplicity':'w>=0','relative_order':1,
                          'new_exceptional_order':str(coefficient_regular),
                          'order_minus_one':str(coefficient_regular-1)},
        'saddle_center':{'positive_prior_exceptional_order':'1+u, u>=0',
                         'other_effective_multiplicity':'w>=0','relative_order':0,
                         'new_exceptional_order':str(coefficient_saddle),
                         'order_minus_one':str(coefficient_saddle-1)},
        'induction':'The initial foliation has no saddle. Every later saddle lies on a previously created exceptional curve. The equality cases d=1-epsilon therefore make every created exceptional order positive.',
        'covered_blowup_count':str(covered_blowups),
        'scope':'Symbolic recomputation of the printed coefficient recurrence and cover count. The proof supplies the effective pushforwards, the invariant-curve property and the occurrence of a previous exceptional curve at each saddle; this program does not infer those facts.',
        'all_assertions_passed':True,
    },indent=2))


if __name__=='__main__':
    main()
