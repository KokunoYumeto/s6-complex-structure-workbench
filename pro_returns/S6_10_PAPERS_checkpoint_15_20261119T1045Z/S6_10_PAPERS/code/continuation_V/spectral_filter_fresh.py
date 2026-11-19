"""Fresh exact cyclotomic enumeration and exterior-square fixed spaces.

All matrix construction and arithmetic are authored for this continuation.
No producing code or certificate is opened, imported, or reused.
"""
from itertools import product, combinations
from math import gcd, lcm
from pathlib import Path
import json, hashlib
from flint import fmpq_mat


def identity(n):
    return fmpq_mat([[int(i == j) for j in range(n)] for i in range(n)])


def companion(coefficients):
    # Coefficients are ordered by increasing exponent, including monic term.
    n = len(coefficients) - 1
    a = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n - 1):
        a[i + 1][i] = 1
    for i in range(n):
        a[i][-1] = -coefficients[i]
    return fmpq_mat(a)


def direct_sum(blocks):
    n = sum(b.nrows() for b in blocks)
    a = [[0 for _ in range(n)] for _ in range(n)]
    offset = 0
    for b in blocks:
        for i in range(b.nrows()):
            for j in range(b.ncols()):
                a[offset + i][offset + j] = b[i, j]
        offset += b.nrows()
    return fmpq_mat(a)


def wedge_two(a):
    pairs = list(combinations(range(a.nrows()), 2))
    return fmpq_mat([
        [a[i, k]*a[j, l] - a[i, l]*a[j, k] for k, l in pairs]
        for i, j in pairs
    ])


def matrix_power(a, n):
    result = identity(a.nrows())
    for _ in range(n):
        result = result*a
    return result


polynomials = {
    2: [1, 1], 3: [1, 1, 1], 4: [1, 0, 1], 6: [1, -1, 1],
    5: [1, 1, 1, 1, 1], 8: [1, 0, 0, 0, 1],
    10: [1, -1, 1, -1, 1], 12: [1, 0, -1, 0, 1],
}
orders = list(polynomials)
degrees = {n: len(p)-1 for n, p in polynomials.items()}
checks = []


def check(condition, description):
    if not condition:
        raise AssertionError(description)
    checks.append(description)


spectra = []
for mult in product(*[range(4//degrees[n]+1) for n in orders]):
    if sum(a*degrees[n] for n, a in zip(orders, mult)) != 4:
        continue
    if mult[orders.index(2)] % 2:
        continue
    active = [(n, a) for n, a in zip(orders, mult) if a]
    order = lcm(*[n for n, a in active])
    if order not in (3, 4, 5, 6, 8, 10, 12):
        continue
    blocks = [identity(2)]
    for n, count in active:
        blocks.extend(companion(polynomials[n]) for _ in range(count))
    a = direct_sum(blocks)
    fixed = 15-(wedge_two(a)-identity(15)).rank()
    name = "*".join("Phi"+str(n)+(f"^{count}" if count>1 else "")
                    for n, count in active)
    check(matrix_power(a, order) == identity(6), name+" finite order")
    check(6-(a-identity(6)).rank() == 2, name+" fixed rank2")
    repeated = len(active) == 1 and active[0] in [(3, 2), (4, 2), (6, 2)]
    check(fixed == (5 if repeated else 3), name+" exterior fixed rank")
    spectra.append({"order": order, "factor": name, "multiplicities": active,
                    "exterior_fixed": fixed,
                    "matrix": [[int(a[i, j]) for j in range(6)] for i in range(6)]})

u = identity(6)
for i in range(3):
    u[i, i+3] = 1
cusp_fixed = 15-(wedge_two(u)-identity(15)).rank()
check(cusp_fixed == 9, "maximal cusp exterior fixed9")

pairs = []
survivors = []
for s, t in combinations(spectra, 2):
    if gcd(s['order'], t['order']) != 1:
        continue
    chi = -15+s['exterior_fixed']+t['exterior_fixed']+cusp_fixed
    row = {'orders': sorted([s['order'], t['order']]),
           'factors': [s['factor'], t['factor']], 'chi': chi}
    pairs.append(row)
    if chi <= 1:
        five, other = (s, t) if s['order'] == 5 else (t, s)
        check(five['order'] == 5, "every survivor contains order5")
        survivors.append({'other_order': other['order'],
                          'five_factor': five['factor'],
                          'other_factor': other['factor'], 'chi': chi})

expected = {
    (4, 'Phi2^2*Phi4'),
    (6, 'Phi2^2*Phi3'), (6, 'Phi2^2*Phi6'), (6, 'Phi3*Phi6'),
    (8, 'Phi8'),
    (12, 'Phi12'), (12, 'Phi3*Phi4'), (12, 'Phi4*Phi6'),
}
actual = {(r['other_order'], r['other_factor']) for r in survivors}
check(actual == expected, "exact eight necessary spectral pairs")
check(len(survivors) == 8, "no duplicate or missing survivor")
check(all(r['chi'] == 0 for r in survivors), "all retained exterior Euler numbers0")
check(not any(3 in r['orders'] and r['chi'] <= 1 for r in pairs),
      "all order-three pairs excluded")

out = {
    'status': 'PASS', 'library': 'python-flint exact rational matrices',
    'count': len(checks), 'checks': checks,
    'finite_spectra': spectra, 'coprime_pairs': pairs,
    'cusp_exterior_fixed': cusp_fixed,
    'survivors': sorted(survivors, key=lambda r: (r['other_order'], r['other_factor'])),
    'proof_scope': 'Complete finite enumeration only; universal Euler bound and specialization maps are prederivations_13.md.',
    'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
path = Path(__file__).with_suffix('.output.json')
path.write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({'status': out['status'], 'checks': len(checks),
                  'finite_spectra': len(spectra), 'coprime_pairs': len(pairs),
                  'survivors': survivors}, indent=2))
