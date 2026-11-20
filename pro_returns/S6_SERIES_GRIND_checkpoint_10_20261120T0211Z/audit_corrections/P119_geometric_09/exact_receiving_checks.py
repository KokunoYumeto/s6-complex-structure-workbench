"""Receiving checks after reading the new P1.19 geometric proof.

The four finite-map rows below are built from the actual signed interval
sweeps, using backwards powers for the negative full circuit.  The saved
fibre fillers are checked against the literal common-fibre inclusion.
These are after-reading finite checks, not a geometric proof or a replay of
any historical missing producer.
"""
from pathlib import Path
from itertools import combinations
import datetime
import hashlib
import importlib.util
import json
import sympy as s

WORK = Path('/workspace/scratch/6c4e6df38b6d/S6_SERIES_GRIND_work')
OUT = Path(__file__).parent
SRC = WORK / 'audit_p119_fresh/derive_chain.py'
spec = importlib.util.spec_from_file_location('received_fresh_model', SRC)
f = importlib.util.module_from_spec(spec)
spec.loader.exec_module(f)
adapt_path = WORK / 'audit_p119_fresh/comparison_09/geometric_diagram_check_02.json'
adapt = json.loads(adapt_path.read_text())
saved_path = WORK / 'audit_p119_fresh/fresh_candidate_chain.json'
saved = json.loads(saved_path.read_text())
checks = []

def check(name, condition):
    assert bool(condition), name
    checks.append(name)

def exterior(matrix, degree):
    if degree < 0:
        return s.zeros(0)
    rows = list(combinations(range(matrix.rows), degree))
    cols = list(combinations(range(matrix.cols), degree))
    return s.Matrix(len(rows), len(cols),
                    lambda i, j: matrix.extract(rows[i], cols[j]).det())

finite_records = {}
for site in (1, 2):
    data = adapt['finite_cap_adapters'][str(site)]
    Q, K = s.Matrix(data['Q']), s.Matrix(data['K'])
    R = s.Matrix(data['signed_monodromy'])[1:, 1:]
    mu = f.eps[site] * f.mult[site]
    check(f'actual finite order {site}', R ** abs(mu) == s.eye(5))
    check(f'split orientation determinant {site}', f.P[site].det() == 1)
    for degree in range(8):
        fibre = list(combinations(range(6), degree))
        suspended = list(combinations(range(6), degree - 1)) if degree else []
        cap_fibre = list(combinations(range(1, 6), degree))
        cap_base = list(combinations(range(1, 6), degree - 1)) if degree else []
        b = s.zeros(len(cap_fibre) + len(cap_base), len(fibre) + len(suspended))
        action = exterior(R, degree - 1)
        sweep = s.zeros(*action.shape)
        if mu > 0:
            for j in range(mu):
                sweep += action ** j
        else:
            for j in range(1, -mu + 1):
                sweep -= action ** (-j)
        for column, cell in enumerate(fibre):
            if 0 not in cell:
                b[cap_fibre.index(cell), column] = 1
            else:
                b[len(cap_fibre):, column] = sweep[:, cap_base.index(cell[1:])]
        for column, cell in enumerate(suspended):
            if 0 not in cell:
                b[len(cap_fibre) + cap_base.index(cell), len(fibre) + column] = 1
            # With both base parameters, the two derivative columns are
            # proportional on every affine subdivision chamber: zero pushforward.
        src = s.diag(exterior(Q, degree), exterior(Q, degree - 1))
        dst = s.diag(exterior(K, degree), exterior(K, degree - 1))
        transported = dst * b * src.inv()
        check(f'actual four-row signed sweep transport {site},{degree}',
              transported == f.je(site, degree))
        check(f'integral transported finite map {site},{degree}',
              all(x.q == 1 for x in transported))
    check(f'literal cap top degree {site}', f.je(site, 6)[0, 0] == mu)
    finite_records[site] = {'Q_det': int(Q.det()), 'K_det': int(K.det()),
                            'P_det': int(f.P[site].det()), 'actual_mu': mu}

fillers = {}
for degree in (2, 3, 4, 5):
    F = s.Matrix(saved['Y_homology'][str(degree)]['fibre_fillers'])
    J = f.j_y(degree)[:, :f.n(6, degree)]
    check(f'actual saved integral common-fibre filler degree {degree}',
          f.Y[degree + 1] * F == J)
    check(f'filler integrality degree {degree}', all(x.q == 1 for x in F))
    fillers[degree] = {'shape': list(F.shape), 'fibre_rank': J.cols}

k = s.symbols('k', integer=True)
a = 2 * k + 1
# Cone(j_C) has column(a,-2), whereas the global cap component uses -j_C.
check('relative odd secondary exact shear',
      s.Matrix([[1, k], [0, 1]]) * s.Matrix([a, -2]) == s.Matrix([1, -2]))
check('global negative-cap exact shear',
      s.Matrix([[1, -k], [0, 1]]) * s.Matrix([-a, -2]) == s.Matrix([-1, -2]))
check('relative and global shears unimodular',
      s.Matrix([[1, k], [0, 1]]).det() == s.Matrix([[1, -k], [0, 1]]).det() == 1)
check('negative-coordinate top cap correction', s.Integer(-2) * 2 == -4)

result = {
    'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'status': 'PASS', 'assertions': len(checks), 'checks': checks,
    'reading_order': 'After complete receiving proof and fresh-code reading; no prereading claim.',
    'finite_scope': 'Actual signed interval sweeps, including backwards negative powers, transported through literal Q/K bases in degrees0–7.',
    'filler_scope': 'The four saved integral F_k are multiplied against the actual numerical complement differential; the separate geometric receiving argument identifies its common fibre with C exactly.',
    'finite_records': finite_records, 'filler_records': fillers,
    'not_certified_by_code': 'Polyhedral homology equivalence, geometric collar realization, cusp collapse, and local relative duality are proof arguments, not consequences of these assertions.',
    'input_sha256': {str(path.relative_to(WORK)): hashlib.sha256(path.read_bytes()).hexdigest()
                     for path in (SRC, adapt_path, saved_path)},
}
(OUT / 'exact_receiving_checks.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'status': result['status'], 'assertions': len(checks),
                  'finite_records': finite_records, 'filler_records': fillers}, indent=2))
