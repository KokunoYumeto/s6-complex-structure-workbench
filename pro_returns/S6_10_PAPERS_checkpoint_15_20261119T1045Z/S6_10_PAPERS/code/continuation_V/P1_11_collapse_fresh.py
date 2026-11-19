"""Actual dual-Kuhn angular quotient maps, newly authored with FLINT.

No target proof or producing code has been opened. Matrices are generated
from the six stated simplices and their actual saturated angular quotients.
"""
from itertools import permutations, combinations
from math import comb
from pathlib import Path
import json, hashlib
from flint import fmpz_mat


def eye(n):
    return fmpz_mat([[int(i == j) for j in range(n)] for i in range(n)]) if n else fmpz_mat(0, 0)


def zero(m, n):
    return fmpz_mat(m, n)


def sub(a, rows, cols):
    rows, cols = list(rows), list(cols)
    if not rows or not cols:
        return zero(len(rows), len(cols))
    return fmpz_mat([[a[i, j] for j in cols] for i in rows])


def integral_inverse(a):
    if a.nrows() == 0:
        return eye(0)
    check(abs(int(a.det())) == 1, 'unimodular inverse')
    b = a.inv()
    return fmpz_mat([[int(b[i, j]) for j in range(b.ncols())]
                     for i in range(b.nrows())])


def exterior(a, q):
    rows = list(combinations(range(a.nrows()), q))
    cols = list(combinations(range(a.ncols()), q))
    b = zero(len(rows), len(cols))
    for i, r in enumerate(rows):
        for j, c in enumerate(cols):
            b[i, j] = 1 if q == 0 else sub(a, r, c).det()
    return b


def normalize(vertices):
    vertices = sorted(vertices)
    first = vertices[0]
    return tuple(tuple(v[i]-first[i] for i in range(3)) for v in vertices)


checks = []


def check(ok, name):
    if not ok:
        raise AssertionError(name)
    checks.append(name)


tetrahedra = []
for perm in permutations(range(3)):
    v = [0, 0, 0]
    vertices = [tuple(v)]
    for i in perm:
        v[i] += 1
        vertices.append(tuple(v))
    tetrahedra.append(tuple(vertices))
faces = []
for r in range(4):
    faces.append(sorted({normalize(s) for tet in tetrahedra
                         for s in combinations(tet, r+1)}))
check([len(f) for f in faces] == [1, 7, 12, 6], 'exact periodic Kuhn face counts')

# Q_sigma:A->A/K_sigma and J_sigma are actual integral projection/section.
quotient = {}
section = {}
for r in range(4):
    for face in faces[r]:
        vectors = [list(v) for v in face[1:]]
        completed = None
        for indices in combinations(range(3), 3-r):
            columns = vectors + [[int(i == j) for i in range(3)] for j in indices]
            m = fmpz_mat([[columns[j][i] for j in range(3)] for i in range(3)])
            if abs(int(m.det())) == 1:
                completed = m
                break
        check(completed is not None, 'primitive face-lattice completion')
        inverse = integral_inverse(completed)
        q = sub(inverse, range(r, 3), range(3))
        j = sub(completed, range(3), range(r, 3))
        check(q*j == eye(3-r), 'quotient section identity')
        quotient[face], section[face] = q, j


def incidence(coface, face):
    return sum((-1)**i for i in range(len(coface))
               if normalize(coface[:i]+coface[i+1:]) == face)


def dimensions(p, q, target):
    if p < 0 or p > 3:
        return 0
    fiber = comb(p, q) if target and q <= p else (0 if target else comb(3, q))
    return len(faces[3-p])*fiber


def differential(p, q, target):
    a = zero(dimensions(p-1, q, target), dimensions(p, q, target))
    if p == 0 or not a.nrows() or not a.ncols():
        return a
    r = 3-p
    nsrc = comb(p, q) if target else comb(3, q)
    ndst = comb(p-1, q) if target else comb(3, q)
    for j, f in enumerate(faces[r]):
        for i, g in enumerate(faces[r+1]):
            sign = incidence(g, f)
            if not sign:
                continue
            transition = quotient[g]*section[f] if target else eye(3)
            block = exterior(transition, q)
            if target:
                check(quotient[g] == transition*quotient[f], 'actual quotient factorization')
            for u in range(ndst):
                for v in range(nsrc):
                    a[i*ndst+u, j*nsrc+v] += sign*block[u, v]
    return a


def collapse(p, q):
    a = zero(dimensions(p, q, True), dimensions(p, q, False))
    nt = comb(p, q) if q <= p else 0
    ns = comb(3, q)
    for i, f in enumerate(faces[3-p]):
        block = exterior(quotient[f], q)
        for u in range(nt):
            for v in range(ns):
                a[i*nt+u, i*ns+v] = block[u, v]
    return a


def homology(a, b):
    # a:C_p->C_(p-1), b:C_(p+1)->C_p. All bases are integral.
    n = a.ncols()
    check(a*b == zero(a.nrows(), b.ncols()), 'boundary squared zero')
    h, t = a.transpose().hnf(transform=True)
    check(h == t*a.transpose(), 'kernel HNF identity')
    z = t.transpose()
    zi = integral_inverse(z)
    rank_a = a.rank()
    kernel = sub(z, range(n), range(rank_a, n))
    coordinates = zi*b
    check(sub(coordinates, range(rank_a), range(b.ncols())) == zero(rank_a, b.ncols()),
          'boundary lies in primitive cycle lattice')
    boundary_coordinates = sub(coordinates, range(rank_a, n), range(b.ncols()))
    hh, tt = boundary_coordinates.hnf(transform=True)
    check(hh == tt*boundary_coordinates, 'quotient HNF identity')
    rank_b = boundary_coordinates.rank()
    smith = boundary_coordinates.snf()
    torsion = [abs(int(smith[i, i])) for i in range(rank_b)]
    check(all(x == 1 for x in torsion), 'homology boundary image primitive')
    inverse_tt = integral_inverse(tt)
    hdim = n-rank_a-rank_b
    projection = sub(tt, range(rank_b, n-rank_a), range(n-rank_a))*sub(zi, range(rank_a, n), range(n))
    representatives = kernel*sub(inverse_tt, range(n-rank_a), range(rank_b, n-rank_a))
    check(projection*representatives == eye(hdim), 'actual homology projection/section')
    check(a*representatives == zero(a.nrows(), hdim), 'homology representatives are cycles')
    check(projection*b == zero(hdim, b.ncols()), 'homology projection kills boundaries')
    return {'rank': hdim, 'projection': projection, 'representatives': representatives,
            'boundary_smith': torsion}


tables = []
details = []
total_target = [0]*7
total_map = [0]*7
for q in range(4):
    ds = [differential(p, q, False) for p in range(4)]
    dt = [differential(p, q, True) for p in range(4)]
    maps = [collapse(p, q) for p in range(4)]
    for p in range(1, 4):
        check(dt[p]*maps[p] == maps[p-1]*ds[p], 'actual collapse chain square')
    for p in range(4):
        hs = homology(ds[p], ds[p+1] if p < 3 else zero(dimensions(p, q, False), 0))
        ht = homology(dt[p], dt[p+1] if p < 3 else zero(dimensions(p, q, True), 0))
        induced = ht['projection']*maps[p]*hs['representatives']
        rank = induced.rank()
        smith = induced.snf()
        nonzero = [abs(int(smith[i, i])) for i in range(rank)]
        check(all(x == 1 for x in nonzero), 'graded collapse image primitive')
        total_target[p+q] += ht['rank']
        total_map[p+q] += rank
        tables.append({'p': p, 'q': q, 'source_rank': hs['rank'],
                       'target_rank': ht['rank'], 'collapse_rank': rank,
                       'collapse_smith': nonzero})
        details.append({'p': p, 'q': q,
                        'source_differential': ds[p].tolist(),
                        'target_differential': dt[p].tolist(),
                        'collapse_chain_map': maps[p].tolist(),
                        'source_representatives': hs['representatives'].tolist(),
                        'target_projection': ht['projection'].tolist(),
                        'induced_homology_map': induced.tolist()})

check(total_target == [1, 3, 9, 9, 10, 3, 1], 'all target E2 ranks')
check(total_map == [1, 3, 9, 9, 9, 3, 1], 'all graded collapse ranks')
u = eye(6)
for i in range(3):
    u[i, i+3] = 1
fixed = [comb(6, k)-(exterior(u, k)-eye(comb(6, k))).rank() for k in range(7)]
check(fixed == total_map, 'actual maximal-cusp invariant ranks agree in every degree')
out = {'status': 'PASS', 'library': 'python-flint integral HNF and Smith forms',
       'checks': len(checks), 'check_names': checks,
       'faces': faces, 'graded_homology_maps': tables,
       'target_ranks': total_target, 'graded_collapse_ranks': total_map,
       'monodromy_fixed_ranks': fixed, 'full_exact_maps': details,
       'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'scope': 'Actual dual-cell angular quotient chain maps and their integral homology maps; higher coherences and identification with the actual log collapse are in the separate written proof.'}
def clean(x):
    if isinstance(x, dict): return {k:clean(v) for k,v in x.items()}
    if isinstance(x, (tuple, list)): return [clean(v) for v in x]
    if isinstance(x, (str, bool, int)) or x is None: return x
    return int(x)
out = clean(out)
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['status','checks','target_ranks','graded_collapse_ranks','graded_homology_maps']}, indent=2))
