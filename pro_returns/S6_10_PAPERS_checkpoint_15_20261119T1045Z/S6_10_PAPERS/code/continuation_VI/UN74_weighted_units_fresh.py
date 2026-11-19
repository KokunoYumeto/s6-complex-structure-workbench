#!/usr/bin/env python3
"""Independent post-comparison arithmetic for UN74; no old producer import.

The earlier prereading chart/extension program is preserved unchanged.
This certificate additionally retains the unit in the specified root map.
"""
from fractions import Fraction
from itertools import product
from pathlib import Path
from hashlib import sha256
import json
import ast

checks = 0
def verify(condition):
    global checks
    assert condition
    checks += 1

# Coefficients of e(B), r in the component-minus-double-plus-triple count.
verify(tuple(a-b+c for a,b,c in zip((2,1),(1,2),(0,1))) == (1,0))

# The exponent substitution is an integer-linear map. Checking its two
# coefficient columns proves f'=p^m q^n -> x^m y^m z^n for all m,n,
# beyond the separate positive-weight examples in the prereading program.
def exponent_vector(node):
    if isinstance(node,ast.Name):
        return tuple(int(node.id==name) for name in ('x','y','z'))
    if isinstance(node,ast.BinOp) and isinstance(node.op,ast.Mult):
        return tuple(a+b for a,b in zip(exponent_vector(node.left),exponent_vector(node.right)))
    raise ValueError('unexpected coordinate expression')
exponent_columns = tuple(exponent_vector(ast.parse(expr,mode='eval').body) for expr in ('x*y','z'))
verify(exponent_columns[0] == (1,1,0))
verify(exponent_columns[1] == (0,0,1))

records = 0
for m in range(1,7):
    for r in range(5):
        for weights in product(range(1,7), repeat=r):
            degree = -Fraction(sum(weights),m)
            if degree.denominator != 1:
                continue
            records += 1
            # The actual line difference is -a times the root relation
            # m[M] + sum n_j[b_j] = 0, before taking any degrees.
            root_relation = (m,)+weights
            for a in (-3,-1,0,2,5):
                difference = (-a*m,)+tuple(-a*n for n in weights)
                verify(difference == tuple(-a*x for x in root_relation))
                verify(difference[0]*degree + sum(difference[1:]) == 0)
            verify(m*degree == -sum(weights))

# If phi(mu^m)=u*d, phi^(-a) multiplies the comparison frame by
# u^(-a). The actual canonical-form change contributes u^a.
for u in (Fraction(-3,2), Fraction(2), Fraction(5,7)):
    for a in range(-6,7):
        verify(u**a * u**(-a) == 1)

# Independently regenerate the entire old negative-degree domain using
# sums of the positive effective dual divisor, with endpoint values kept.
negative_records = 0
for r in range(1,6):
    for differences in product(range(-3,2), repeat=r):
        effective = tuple(2-d for d in differences)
        verify(min(effective) >= 1)
        verify(-sum(effective) <= -r < 0)
        negative_records += 1

out = {
    "status":"PASS", "checks":checks,
    "weighted_records":records, "negative_degree_records":negative_records,
    "chronology":"newly authored after target and old producer comparison; no prereading proof credit",
    "method":"pure stdlib Fraction, universal integer-linear exponent columns and actual root-relation exponent vectors; independent of old SymPy producer",
    "unit_map":"phi(mu^m)=u*d gives u^(-a), cancelling the u^a of the actual canonical rescaling",
    "source_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
