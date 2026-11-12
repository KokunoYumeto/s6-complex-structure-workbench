"""Bounded exact checks for the shared mathematical module.

The arithmetic checks use independent ordered/unordered parametrizations.
The Fourier checks use Z[zeta_6] as Z[t]/(t^2-t+1), without floating point.
The structural audit reads only the adjacent module and bibliography files.
"""
from collections import Counter
from fractions import Fraction
from math import gcd
from pathlib import Path
import re

base = Path(__file__).resolve().parent
module = (base / "es_niemeier_shared.tex").read_text(encoding="utf-8")
bibliography = (base / "es_niemeier_bibliography.tex").read_text(encoding="utf-8")
labels = re.findall(r"\\label\{([^}]+)\}", module)
assert labels and all(label.startswith("esn:") for label in labels)
assert all(n == 1 for n in Counter(labels).values())
references = re.findall(r"\\(?:eqref|ref)\{([^}]+)\}", module)
assert set(references) <= set(labels)
keys = re.findall(r"\\bibitem\{([^}]+)\}", bibliography)
assert len(keys) == len(set(keys)) == 5
citations = [
    key.strip()
    for group in re.findall(r"\\cite(?:\[[^\]]*\])?\{([^}]+)\}",
                            module + bibliography)
    for key in group.split(",")
]
assert set(citations) <= set(keys)
assert all(key.startswith("esn:") for key in keys)
assert not re.search(
    r"\\(?:documentclass|usepackage|newcommand|renewcommand|providecommand|"
    r"newtheorem|input|include)\b", module
)
assert not re.search(
    r"[A-Za-z]:[/\\](?:Users|Documents|Temp|home)[/\\]|/Users/|es-audit:",
    module + bibliography,
)
assert not re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", module + bibliography)
assert r"\mathcal H_D" not in module and r"\(Hx\)" not in module
assert len(re.findall(r"\\subsection\{", module)) == 9
stack = []
for op, env in re.findall(r"\\(begin|end)\{([^}]+)\}", module):
    if op == "begin":
        stack.append(env)
    else:
        assert stack and stack.pop() == env
assert not stack
print(f"PASS: {len(labels)} unique esn labels; all references and five citations resolve; nine self-contained subsections")
print("PASS: no host redefinitions, nested inputs, stale audit labels, control characters, or reader-local paths")

checked = 0
for R0 in range(1, 13):
    for N0 in range(1, 25):
        if gcd(R0, N0) != 1:
            continue
        divisors = {
            d for d in range(1, N0*N0 + 1)
            if N0*N0 % d == 0 and (d + N0) % R0 == 0
        }
        ordered = {
            ((N0+d)//R0, (N0+N0*N0//d)//R0) for d in divisors
        }
        assert len(ordered) == len(divisors)
        for b, c in ordered:
            assert Fraction(R0, N0) == Fraction(1, b) + Fraction(1, c)
            assert R0*b-N0 in divisors
        # Independent enumeration: for b <= c, N0/R0 < b <= 2*N0/R0.
        unordered = set()
        for b in range(N0//R0 + 1, (2*N0)//R0 + 1):
            denominator = R0*b-N0
            if N0*b % denominator == 0:
                c = N0*b//denominator
                if b <= c:
                    unordered.add((b, c))
        assert unordered == {tuple(sorted(pair)) for pair in ordered}
        delta = int(2 % R0 == 0)
        assert 2*len(unordered) == len(divisors) + delta
        assert sum(b == c for b, c in ordered) == delta
        checked += 1
print(f"PASS: exact divisor bijection and complement fixed-point count in {checked} coprime modulus/denominator cases")

def add(x, y):
    return (x[0]+y[0], x[1]+y[1])

def mul(x, y):
    a, b = x
    c, d = y
    return (a*c-b*d, a*d+b*c+b*d)

def scale(n, x):
    return (n*x[0], n*x[1])

def total(xs):
    result = (0, 0)
    for x in xs:
        result = add(result, x)
    return result

one = (1, 0)
zeta = (0, 1)
powers = [one]
for _ in range(6):
    powers.append(mul(powers[-1], zeta))
assert powers[6] == one and len(set(powers[:6])) == 6
for m in range(6):
    assert total(powers[(k*m) % 6] for k in range(6)) == (
        (6, 0) if m == 0 else (0, 0)
    )
for k in range(6):
    vector = [powers[k*j % 6] for j in range(6)]
    translated = [vector[(j-1) % 6] for j in range(6)]
    assert translated == [mul(powers[-k % 6], x) for x in vector]
for weights in ((0, 0, 0, 0, 0, 0), (6, 0, 0, 0, 0, 0),
                (2, 0, 3, 1, 0, 6), (1, -2, 3, -4, 5, -6)):
    transformed = [
        total(scale(weights[j], powers[-k*j % 6]) for j in range(6))
        for k in range(6)
    ]
    for j in range(6):
        assert total(mul(transformed[k], powers[k*j % 6])
                     for k in range(6)) == (6*weights[j], 0)
    augmented = [6*w-sum(weights) for w in weights]
    assert sum(augmented) == 0
    for j in range(6):
        assert total(mul(transformed[k], powers[k*j % 6])
                     for k in range(1, 6)) == (augmented[j], 0)
print("PASS: exact Fourier inversion, the negative eigenvalue exponent, and all integral augmentation coefficients")
print("ALL SHARED-MODULE CHECKS PASSED")
