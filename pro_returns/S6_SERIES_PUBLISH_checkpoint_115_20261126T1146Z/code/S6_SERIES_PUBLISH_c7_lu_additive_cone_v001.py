"""Fresh LU local cone and inverse maps, with no LT/LU original or history input.

The named component orders below are explicit fresh diagram coordinates.
They do not identify the still-unresolved literal IC8 component ordering.
Raw elliptic logarithms are taken only from the admitted defining fixture.
"""
from datetime import datetime, timezone
from hashlib import sha256
from math import gcd, lcm
from pathlib import Path
import json
import sympy as S
from sympy import ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json'
assert sha256(RAW.read_bytes()).hexdigest() == '6bda97b01ba63c0a796e3141609ca12e163791b626024b79104817ec5defc522'
PROFILES = json.loads(RAW.read_bytes())['rows']


def integer(M):
    M = S.Matrix(M)
    assert all(x.q == 1 for x in M)
    return M


def smith(M):
    M = integer(M)
    if not M.rows or not M.cols:
        D, U, V = M.copy(), S.eye(M.rows), S.eye(M.cols)
    else:
        d, u, v = smith_normal_decomp(DomainMatrix.from_Matrix(M).convert_to(ZZ))
        D, U, V = d.to_Matrix(), u.to_Matrix(), v.to_Matrix()
    Ui, Vi = integer(U.inv()), integer(V.inv())
    assert U*M*V == D and Ui*U == S.eye(U.rows) and Vi*V == S.eye(V.rows)
    rank = sum(D[i, i] != 0 for i in range(min(D.shape)))
    return D, U, V, Ui, Vi, rank


def kernel(M):
    D, U, V, Ui, Vi, rank = smith(M)
    K, L = V[:, rank:], Vi[rank:, :]
    assert M*K == S.zeros(M.rows, K.cols) and L*K == S.eye(K.cols)
    return K, L


def homology(d, dn):
    K, L = kernel(d)
    assert d*dn == S.zeros(d.rows, dn.cols)
    B = L*dn
    assert K*B == dn
    D, U, V, Ui, Vi, rank = smith(B)
    factors = [abs(int(D[i, i])) for i in range(rank) if abs(D[i, i]) > 1]
    return [K.cols-rank, factors]


def egcd(a, b):
    aa, bb, x, xx, y, yy = a, b, 1, 0, 0, 1
    while bb:
        q = aa//bb
        aa, bb, x, xx, y, yy = bb, aa-q*bb, xx, x-q*xx, yy, y-q*yy
    sign = 1 if aa >= 0 else -1
    return sign*aa, sign*x, sign*y


def bezout(values):
    result, g = [], 0
    for value in values:
        h, x, y = egcd(g, int(value))
        result = [x*z for z in result]+[y]
        g = h
    assert sum(int(a)*b for a, b in zip(values, result)) == g
    return g, S.Matrix(result)


def orbits(perm):
    remaining, result = set(range(len(perm))), []
    while remaining:
        start = min(remaining)
        orbit, at = [], start
        while at not in orbit:
            orbit.append(at)
            remaining.remove(at)
            at = perm[at]
        assert at == start
        result.append(orbit)
    return result


def raw_log(kind, order):
    for profile in PROFILES:
        for site, local_kind in enumerate(profile['fibers']):
            if local_kind != kind:
                continue
            B = S.Matrix(profile['elliptic_matrices'][site])
            g = S.Matrix(profile['generator_section_cocycle'][site])
            for b in range(1, 5):
                z = (B-S.eye(2)).inv()*(b*g)
                q = lcm(*(int(x.q) for x in z))
                if q == order:
                    assert (B-S.eye(2))*z == b*g
                    return [profile['OS'], profile['profile'], site, b], z
    raise AssertionError(('No raw marked logarithm', kind, order))


def diagram(kind):
    if kind == 'II':
        return [1], [0]
    if kind == 'III':
        return [1, 1], [1, 0]
    if kind == 'IV':
        return [1, 1, 1], [1, 2, 0]
    if kind == 'IV*':
        return [3, 2, 2, 2, 1, 1, 1], [0, 2, 3, 1, 5, 6, 4]
    if kind == 'III*':
        return [1, 2, 3, 4, 3, 2, 1, 2], [6, 5, 4, 3, 2, 1, 0, 7]
    size = {'I1*': 6, 'I3*': 8}[kind]
    perm = list(range(size))
    perm[0], perm[1], perm[-2], perm[-1] = size-2, size-1, 1, 0
    for i in range(2, size-2):
        perm[i] = size-1-i
    return [1, 1]+[2]*(size-4)+[1, 1], perm


def power_perm(perm, power):
    result = list(range(len(perm)))
    for _ in range(power):
        result = [perm[i] for i in result]
    return result


def serialize(M):
    return [[int(x) for x in row] for row in integer(M).tolist()]


def check(kind, power, degree, label):
    multiplicity, generator = diagram(kind)
    perm = power_perm(generator, power)
    orb = orbits(perm)
    v, rho = len(perm), len(orb)
    sigma = S.zeros(v)
    for i, j in enumerate(perm):
        sigma[j, i] = 1
    mu, c = S.Matrix(multiplicity), S.Matrix(degree)
    assert sigma*mu == mu and sigma*c == c and (c.T*mu)[0] == 0
    R, J = S.zeros(rho, v), S.zeros(v, rho)
    for j, orbit in enumerate(orb):
        for i in orbit:
            R[j, i] = 1
        J[orbit[0], j] = 1
    assert R*J == S.eye(rho)
    d2 = S.zeros(2, v+1)
    d2[0, :v] = c.T
    d3 = S.zeros(v+1, 2*v)
    d3[:v, v:] = sigma-S.eye(v)
    d3[v, v:] = c.T
    d4 = S.zeros(2*v, v)
    d4[:v, :] = S.eye(v)-sigma
    ds = [S.zeros(0, 1), S.zeros(1, 2), d2, d3, d4, S.zeros(v, 0)]
    groups = [homology(ds[i], ds[i+1]) for i in range(5)]
    order = lcm(*(len(o) for o in orb))
    q, q_inverse = bezout(list(R*mu))
    assert q == order
    raw_key, z = raw_log(kind, order)
    area = integer(S.Matrix([[q, 0, q*z[1], 0, -q*z[0], 0]]))
    area_gcd, area_section = bezout(list(area))
    assert area_gcd == 1 and area*area_section == S.ones(1, 1)
    W = integer(R*mu/q)
    record = dict(kind=kind, power=power, label=label, permutation=perm,
                  multiplicity=multiplicity, degrees=degree, orbits=orb,
                  homology=groups, q=q, q_inverse=list(map(int, q_inverse)),
                  raw_key=raw_key, z=list(map(str, z)), W=list(map(int, W)),
                  area=serialize(area), area_section=list(map(int, area_section)))
    if any(c):
        cj = S.Matrix([[c[o[0]] for o in orb]])
        weighted = [len(o)*int(c[o[0]]) for o in orb]
        h, a = bezout(weighted)
        assert h == 1
        eta = S.zeros(v, 1)
        for j, orbit in enumerate(orb):
            for i in orbit:
                eta[i] = a[j]
        assert (sigma-S.eye(v))*eta == S.zeros(v, 1) and c.T*eta == S.ones(1, 1)
        assert d3*S.zeros(v, 1).col_join(eta) == S.zeros(v, 1).col_join(S.ones(1, 1))
        F, FL = kernel(cj)
        read = FL*R.row_join(S.zeros(rho, 1))
        section = (J*F).col_join(S.zeros(1, F.cols))
        assert read*section == S.eye(F.cols) and read*d3 == S.zeros(F.cols, 2*v)
        assert d2*section == S.zeros(2, F.cols)
        K2, K2L = kernel(d2)
        error = K2-section*read*K2
        preimage = S.zeros(2*v, K2.cols)
        for column in range(error.cols):
            zz, tt = error[:v, column], error[v, column]
            assert R*zz == S.zeros(rho, 1)
            yy = S.zeros(v, 1)
            for orbit in orb:
                total = 0
                for i in orbit:
                    total += zz[i]
                    yy[i] = -total
                assert total == 0
            assert (sigma-S.eye(v))*yy == zz
            yy += (tt-(c.T*yy)[0])*eta
            preimage[v:, column] = yy
        assert d3*preimage == error
        assert cj*W == S.zeros(1, 1)
        assert bezout(list(FL*W))[0] == 1
        expected = [[1, []], [1, []], [rho-1, []], [2*rho-1, []], [rho, []]]
        record.update(h=h, eta=list(map(int, eta)), read=serialize(read),
                      section=serialize(section), cycles=serialize(K2),
                      bounding_preimage=serialize(preimage))
    else:
        expected = [[1, []], [2, []], [rho+1, []], [2*rho, []], [rho, []]]
        record['h'] = 0
    assert groups == expected
    assert sum((-1)**i*groups[i][0] for i in range(5)) == 0
    print('CASE', kind, power, label, 'c', degree, 'q', q, 'H0_to_H4', groups,
          'area', serialize(area), 'eta', record.get('eta'), 'PASS', flush=True)
    return record


print('START', datetime.now(timezone.utc).isoformat(), flush=True)
records = []
for kind, powers in [('II', [0]), ('III', [0, 1]), ('IV', [0, 1]),
                     ('IV*', [0, 1]), ('III*', [0, 1]),
                     ('I1*', [0, 2, 1]), ('I3*', [0, 2, 1])]:
    mu, generator = diagram(kind)
    for power in powers:
        records.append(check(kind, power, [0]*len(mu), 'zero'))
    if kind != 'II':
        leaves = [i for i, value in enumerate(mu) if value == 1]
        c = [0]*len(mu)
        c[leaves[0]], c[leaves[1]] = 1, -1
        records.append(check(kind, 0, c, 'identity_h1'))
for kind, power, degree in [
    ('IV', 0, [2, 3, -5]),
    ('IV*', 1, [1, 0, 0, 0, -1, -1, -1]),
    ('IV*', 1, [2, 3, 3, 3, -8, -8, -8]),
    ('III*', 1, [-7, 0, 0, 2, 0, 0, -7, 3]),
    ('I1*', 2, [-1, -1, 1, 0, 0, 0]),
    ('I1*', 2, [2, 2, 3, 0, -5, -5]),
    ('I3*', 2, [-1, -1, 1, 0, 0, 0, 0, 0]),
    ('I3*', 2, [2, 2, 3, 0, 0, 0, -5, -5]),
]:
    records.append(check(kind, power, degree, 'nonzero_h1'))
destination = ROOT / 'agents/continuation7_iii_corrected_initial/S6_SERIES_PUBLISH_III_02LU_fresh_cone_data_v001.json'
assert not destination.exists()
destination.write_text(json.dumps({'scope': __doc__, 'records': records}, indent=2)+'\n', newline='\n')
print('COMPLETE_CASES', len(records), 'NONZERO_H1', sum(r['h'] == 1 for r in records), flush=True)
print('DATA', destination.relative_to(ROOT), 'SHA256', sha256(destination.read_bytes()).hexdigest(), flush=True)
print('COMPLETE', datetime.now(timezone.utc).isoformat(), flush=True)
