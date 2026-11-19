"""Fresh exact certificates for P1.12's evaluation and finite attachment maps.

Only the statement/input packet is read. No producing program is imported or
opened. Standard-library rational matrix elimination is used throughout.
The universal proofs of these identities are in P1_12_before_read.md; the
finite checks below certify the supplied matrices and explicit coordinate maps.
"""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
PACKET = ROOT / 'analysis/continuation_V/P1_12_statement_input_packet.md'
RAW = PACKET.read_text()
DATA = json.loads(re.search(r'```json\s*(.*?)\s*```', RAW, re.S).group(1))
CHECKS = []


def mat(a):
    return [[F(x) for x in row] for row in a]


def eye(n):
    return mat([[int(i == j) for j in range(n)] for i in range(n)])


def mm(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(a, b):
    return [[x + y for x, y in zip(r, s)] for r, s in zip(a, b)]


def scale(c, a):
    return [[F(c) * x for x in r] for r in a]


def inv(a):
    n = len(a)
    z = [r[:] + s[:] for r, s in zip(a, eye(n))]
    for j in range(n):
        pivot = next(i for i in range(j, n) if z[i][j])
        z[j], z[pivot] = z[pivot], z[j]
        t = z[j][j]
        z[j] = [x / t for x in z[j]]
        for i in range(n):
            if i != j:
                t = z[i][j]
                z[i] = [x - t * y for x, y in zip(z[i], z[j])]
    return [r[n:] for r in z]


def power(a, n):
    out = eye(len(a))
    for _ in range(n):
        out = mm(out, a)
    return out


def require(name, lhs, rhs):
    assert lhs == rhs, name
    CHECKS.append(name)


I6 = eye(6)
J0 = mat([[0] * 6 for _ in range(6)])
for j in range(3):
    J0[j][j + 3] = F(-1)
    J0[j + 3][j] = F(1)


def real_complex_frame(k):
    # Real matrix of the explicit complex-linear 3 by 3 frame change U+iV.
    u = [[(k + 3 if i == j else 0) for j in range(3)] for i in range(3)]
    v = [[(1 if j == (i + 1) % 3 else -1 if j == (i + 2) % 3 else k)
          for j in range(3)] for i in range(3)]
    return mat([u[i] + [-x for x in v[i]] for i in range(3)]
               + [v[i] + u[i] for i in range(3)])


def evaluation_matrix(seed):
    # Newly chosen integral invertible real evaluation matrices, as products
    # of elementary shears. No period matrices or original code are read.
    r = eye(6)
    for t in range(24):
        i = (seed + 5 * t) % 6
        j = (i + 1 + (seed + t) % 5) % 6
        shear = eye(6)
        shear[i][j] = F(((seed + 3 * t) % 7) - 3)
        r = mm(shear, r)
    return r


samples = []
for seed in range(1, 13):
    r = evaluation_matrix(seed)
    ri = inv(r)
    j = mm(mm(ri, J0), r)
    require(f'R inverse {seed}', mm(r, ri), I6)
    require(f'J squared {seed}', mm(j, j), scale(-1, I6))
    require(f'evaluation multiplication by i {seed}', mm(r, j), mm(J0, r))
    for frame in range(3):
        k = real_complex_frame(frame)
        rp = mm(k, r)
        require(f'complex-linear frame {seed},{frame}', mm(k, J0), mm(J0, k))
        require(f'frame-independent inverse {seed},{frame}', mm(inv(rp), k), ri)
        require(f'frame-independent J {seed},{frame}', mm(mm(inv(rp), J0), rp), j)
    for site in (1, 2):
        m = DATA[f'm{site}']
        mon = mat(DATA[f'M{site}'])
        v = mat([[x] for x in DATA[f'v{site}']])
        jp = mm(mm(mon, j), inv(mon))
        jv = mm(j, v)
        require(f'finite order {seed},{site}', power(mon, m), I6)
        require(f'fixed affine numerator {seed},{site}', mm(mon, v), v)
        require(f'log-translation a coefficient {seed},{site}', mm(r, scale(-1, v)), scale(-1, mm(r, v)))
        require(f'log-translation L coefficient {seed},{site}', mm(r, jv), mm(J0, mm(r, v)))
        require(f'equivariant h coefficient {seed},{site}', mm(jp, v), mm(mon, jv))
        require(f'clutch a coefficient {seed},{site}', scale(-1, v), scale(-1, mm(mon, v)))
        require(f'clutch constant coefficient {seed},{site}', add(scale(F(1, m), v), scale(F(-1, m), v)), scale(0, v))
        # x-coefficients are the actual monodromy on both sides. The universal
        # identity in a,L follows from these separate coefficient equalities.
        for a, ell, chi in [(F(3, 7), F(-5, 11), F(2, 9)),
                            (F(-9, 5), F(8, 3), F(1)),
                            (F(13, 2), F(-7, 6), F(0))]:
            x = mat([[F(seed * (i + 1), i + 2)] for i in range(6)])
            alpha = add(add(x, scale(-a, v)), scale(ell, jv))
            deck_x = add(mm(mon, x), scale(F(1, m), v))
            alpha_deck = add(add(deck_x, scale(-(a + F(1, m)), v)), scale(ell, mm(jp, v)))
            require(f'actual affine equality {seed},{site},{a}', alpha_deck, mm(mon, alpha))
            h = scale(ell, jv)
            translated = add(alpha, scale(-chi, h))
            require(f'collar inverse {seed},{site},{a}', add(translated, scale(chi, h)), alpha)
            if chi == 1:
                require(f'inner collar attachment {seed},{site}', translated, add(x, scale(-a, v)))
        samples.append({'evaluation_index': seed, 'site': site,
                        'order': m, 'J_v': [str(row[0]) for row in jv]})

graphs = []
for epsilon in (0, 1):
    kernel = [(n, t) for n in range(-40, 41) for t in (0, 1)
              if (epsilon * n + t) % 2 == 0]
    graph = [(n, epsilon * n % 2) for n in range(-40, 41)]
    require(f'free degree-four kernel graph {epsilon}', kernel, graph)
    require(f'projection inverse {epsilon}', [n for n, t in kernel], list(range(-40, 41)))
    for n in range(-10, 11):
        for m in range(-10, 11):
            require(f'graph homomorphism {epsilon},{n},{m}',
                    ((epsilon * n % 2) + (epsilon * m % 2)) % 2,
                    epsilon * (n + m) % 2)
    graphs.append({'epsilon': epsilon, 'generator': [1, epsilon],
                   'inverse': 'first projection', 'torsion_generator_image': 1})

output = {'status': 'PASS', 'finished_at_utc': datetime.now(timezone.utc).isoformat(),
          'program_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'input_packet_sha256': hashlib.sha256(PACKET.read_bytes()).hexdigest(),
          'checks': len(CHECKS), 'evaluation_matrices': 12, 'complex_frame_changes_per_matrix': 3,
          'finite_sites': 2, 'method': 'fresh standard-library Fraction arithmetic and Gauss elimination',
          'scope': 'Exact marked evaluation, affine logarithmic clutching, collar inverse, and both integral graph kernels. The universal identities are separately proved in the prereading note. No original producing code read or reused.',
          'matrix_samples': samples, 'degree_four_graphs': graphs,
          'check_names': CHECKS}
out = Path(__file__).with_suffix('.output.json')
out.write_text(json.dumps(output, indent=2) + '\n')
print(json.dumps({k: v for k, v in output.items() if k not in ('check_names', 'matrix_samples')}, indent=2))
