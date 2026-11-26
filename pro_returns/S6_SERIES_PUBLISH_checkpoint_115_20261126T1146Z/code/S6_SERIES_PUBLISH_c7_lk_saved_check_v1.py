#!/usr/bin/env python3
"""Read-only LK saved-record and text verification; no target proof is read."""
import ast
import json
import re
from collections import Counter
from hashlib import sha256
from itertools import combinations
from math import gcd
from pathlib import Path
from sympy import Matrix, Rational, eye, zeros

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT/"agents/continuation7_iii_general_cusp"
PREFIX = "S6_SERIES_PUBLISH_III_02LK_"
DATA = LANE/(PREFIX+"fresh_lattice_data.json")


def integer_matrix(value, shape):
    assert isinstance(value,list) and len(value) == shape[0]
    assert all(isinstance(row,list) and len(row) == shape[1] for row in value)
    assert all(type(x) is int for row in value for x in row)
    return Matrix(value) if shape[0] else zeros(*shape)


def wedge_matrix(M):
    pairs = list(combinations(range(4),2))
    return Matrix([[M.extract(i,j).det() for j in pairs] for i in pairs])


records = json.loads(DATA.read_text())["cases"]
seen = set()
counts = Counter()
fields = {
    "L","index","smith","components","shifts","normalization_coker",
    "torsion_generator","torsion_order","torus_H1_paths","period_basis",
    "period_basis_inverse","wedge_quotient_basis","wedge_quotient_inverse",
    "fibre_kernel","disc_basis","disc_inverse","cap_H2","boundary_H2",
}
for record in records:
    assert set(record) == fields
    B = integer_matrix(record["L"],(2,2))
    a,b,c = int(B[0,0]),int(B[0,1]),int(B[1,1])
    assert B[1,0] == 0 and a>0 and c>0 and 0<=b<a
    key = (a,b,c)
    assert key not in seen
    seen.add(key)
    D = a*c
    s,t = record["smith"]
    assert s == gcd(gcd(a,b),c) and t == D//s
    assert record["index"] == D and record["torsion_order"] == s
    counts[D] += 1
    values = [(p,q) for q in range(c) for p in range(a)]
    assert record["components"] == [list(v) for v in values]
    index = {v:i for i,v in enumerate(values)}
    shifts = []
    for dx,dy in ((1,0),(0,1),(-1,1)):
        permutation = []
        for p,q in values:
            k,y = divmod(q+dy,c)
            permutation.append(index[((p+dx-b*k)%a,y)])
        shifts.append(permutation)
    assert record["shifts"] == shifts
    torsion = []
    for v,(p,q) in enumerate(values):
        pa,qa = values[shifts[0][v]]
        pb,qb = values[shifts[1][v]]
        pc,qc = values[shifts[2][v]]
        raw = (q-qa,-p+pb,-p-q+pc+qc)
        assert all(x%s == 0 for x in raw)
        torsion.extend(x//s for x in raw)
    assert record["torsion_generator"] == torsion
    assert record["normalization_coker"] == [D+2,([s] if s>1 else [])]
    assert record["cap_H2"] == [D+3,([s] if s>1 else [])]
    assert record["boundary_H2"] == [6,([s,s] if s>1 else [])]

    P = integer_matrix(record["period_basis"],(4,4))
    Pi = integer_matrix(record["period_basis_inverse"],(4,4))
    Q = integer_matrix(record["wedge_quotient_basis"],(6,6))
    Qi = integer_matrix(record["wedge_quotient_inverse"],(6,6))
    assert P*Pi == Pi*P == eye(4)
    assert Q*Qi == Qi*Q == eye(6)
    A = eye(4)
    A[:2,2:] = B
    As = eye(4)
    As[0,1],As[2,3] = s,t
    assert A*P == P*As
    area,zeta = zeros(6,1),zeros(6,1)
    area[1] = 1
    zeta[1],zeta[2],zeta[3] = t,1,t//s
    assert Q == Matrix.hstack(area,zeta,eye(6)[:,0],eye(6)[:,3],
                             eye(6)[:,4],eye(6)[:,5])
    K = integer_matrix(record["fibre_kernel"],(6,2))
    assert K == wedge_matrix(P)*Matrix.hstack(area,s*zeta)
    entry_gcd,minor_gcd = 0,0
    for x in K:
        entry_gcd = gcd(entry_gcd,int(x))
    for pair in combinations(range(6),2):
        minor_gcd = gcd(minor_gcd,int(K.extract(pair,(0,1)).det()))
    assert abs(entry_gcd) == 1 and abs(minor_gcd) == s

    paths = integer_matrix(record["torus_H1_paths"],(3*D,2))
    boundary,displacement = zeros(D,2),zeros(2,2)
    for v in range(D):
        for j,(dx,dy) in enumerate(((1,0),(0,1),(-1,1))):
            for k in range(2):
                coefficient = paths[3*v+j,k]
                boundary[shifts[j][v],k] += coefficient
                boundary[v,k] -= coefficient
                displacement[:,k] += coefficient*Matrix([dx,dy])
    assert boundary == zeros(D,2) and displacement == B

    DK = integer_matrix(record["disc_basis"],(D,D-1))
    DI = Matrix([[Rational(x) for x in row] for row in record["disc_inverse"]]) if D>1 else zeros(0,1)
    assert DI.shape == (D-1,D) and DI*DK == eye(D-1)
    assert Matrix.ones(1,D)*DK == zeros(1,D-1)
    # The Smith short basis U^{-1} is read from P itself.
    Ui = Matrix.hstack(P[:2,0],P[:2,2])
    U = Ui.inv()
    labels = []
    for p,q in values:
        v = U*Matrix([p,q])
        labels.append((int(v[0])%s,int(v[1])%t))
    assert len(set(labels)) == D
    M = Matrix([[x for x,y in labels],[y for x,y in labels]])
    image = M*DK
    assert all(int(image[0,j])%s == 0 and int(image[1,j])%t == 0
               for j in range(D-1))
    origin = labels.index((0,0))
    minor = DK.extract([i for i in range(D) if i != origin],list(range(D-1)))
    assert abs(minor.det()) == D

expected = {(a,b,n//a) for n in range(1,13)
            for a in range(1,n+1) if n%a == 0 for b in range(a)}
expected.update([(3,0,6),(4,0,4),(4,2,4),(4,0,8),(5,0,5),(6,0,6),
                 (6,3,6),(6,2,6),(8,4,4),(9,3,3),(12,6,3),(2,1,18)])
assert seen == expected and len(records) == 139
for index,count in sorted(counts.items()):
    print("PASS saved index",index,"records",count,
          "all structures, explicit generators, inverse equations and full disc index")

for suffix in ("fresh_derivation.md","fresh_source_scope.md"):
    path = LANE/(PREFIX+suffix)
    raw = path.read_bytes()
    assert raw.endswith(b"\n") and b"\r" not in raw
    assert not any(x<32 and x not in (9,10) for x in raw)
    text = raw.decode()
    assert text.count(r"\(") == text.count(r"\)")
    assert text.count(r"\[") == text.count(r"\]")
    stack = []
    pairs = {r"\(":r"\)",r"\[":r"\]"}
    for token in re.findall(r"\\[()\[\]]",text):
        if token in pairs:
            stack.append(pairs[token])
        else:
            assert stack and stack.pop() == token
    assert not stack
    print("PASS text",path.name,"lines",len(text.splitlines()),
          "math_fragments",text.count(r"\(")+text.count(r"\["),
          "SHA256",sha256(raw).hexdigest())
for stem in ("lattices_v1","saved_check_v1"):
    path = ROOT/"code"/("S6_SERIES_PUBLISH_c7_lk_"+stem+".py")
    ast.parse(path.read_text())
    print("PASS source AST",path.name,"lines",len(path.read_text().splitlines()),
          "SHA256",sha256(path.read_bytes()).hexdigest())
stdout = ROOT/"code/S6_SERIES_PUBLISH_c7_lk_lattices_v1.out"
stderr = ROOT/"code/S6_SERIES_PUBLISH_c7_lk_lattices_v1.err"
assert len(stdout.read_text().splitlines()) == 145 and stderr.read_bytes() == b""
print("PASS complete derivation stdout145; stderr empty")
print("PASS saved data139 records, all serialized fields exhaustively checked; not manual matrix reading")
print("DATA_SHA256",sha256(DATA.read_bytes()).hexdigest())
print("SCOPE finite saved-data and text checks only; all-L geometry is in the written proof")
