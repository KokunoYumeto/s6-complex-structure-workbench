#!/usr/bin/env python3
"""New LK normalization, torsion, boundary and disc maps; no target proof read."""
import json
from datetime import datetime, timezone
from hashlib import sha256
from math import gcd, lcm
from pathlib import Path
from sympy import Matrix, Rational, eye, zeros
from S6_SERIES_PUBLISH_c7_lh_integral import integral, rows, smith, exterior

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT/"agents/continuation7_iii_general_cusp"
DATA = LANE/"S6_SERIES_PUBLISH_III_02LK_fresh_lattice_data.json"


def positive_smith(A):
    D, U, V, Ui, Vi, rank = smith(A)
    for i in range(rank):
        if D[i, i] < 0:
            D[i, :] = -D[i, :]
            U[i, :] = -U[i, :]
            Ui[:, i] = -Ui[:, i]
    assert U*A*V == D and U*Ui == eye(U.rows) and V*Vi == eye(V.rows)
    return D, U, V, Ui, Vi, rank


def group(A):
    D, U, V, Ui, Vi, r = positive_smith(A)
    return A.rows-r, [int(D[i, i]) for i in range(r) if D[i, i] > 1]


def preimage(A, decomposition, value):
    D, U, V, Ui, Vi, rank = decomposition
    z = U*value
    assert z[rank:, :] == zeros(A.rows-rank, value.cols)
    w = Matrix.vstack(
        Matrix.diag(*(Rational(1, D[i, i]) for i in range(rank)))*z[:rank, :],
        zeros(A.cols-rank, value.cols),
    )
    w = integral(V*w)
    assert A*w == value
    return w


def one_lattice(a, b, c):
    assert a > 0 and c > 0 and 0 <= b < a
    L = Matrix([[a, b], [0, c]])
    count = a*c
    first = gcd(gcd(a, b), c)
    second = count//first
    values = [(p, q) for q in range(c) for p in range(a)]
    indices = {v:i for i, v in enumerate(values)}

    def red(p, q):
        k, q = divmod(q, c)
        return ((p-b*k) % a, q)

    def shift(v, direction):
        p, q = values[v]
        return indices[red(p+direction[0], q+direction[1])]

    directions = [(1, 0), (0, 1), (-1, 1)]
    shifts = [[shift(v, d) for v in range(count)] for d in directions]
    for perm in shifts:
        assert sorted(perm) == list(range(count))

    # Half-edge divisor presentation and its two literal quotient sections.
    C = Matrix([[1,0,0,0,1,-1], [0,1,0,0,1,0],
                [0,0,1,0,0,1], [0,0,0,1,-1,1]])
    P0 = Matrix([[1,0], [0,1], [-1,1], [-1,0], [0,-1], [1,-1]])
    H, P = zeros(4*count, 6*count), zeros(6*count, 2*count)
    SP, KP = zeros(6*count, 4*count), zeros(2*count, 6*count)
    for v in range(count):
        H[4*v:4*v+4, 6*v:6*v+6] = C
        P[6*v:6*v+6, 2*v:2*v+2] = P0
        SP[6*v:6*v+4, 4*v:4*v+4] = eye(4)
        KP[2*v,6*v+4], KP[2*v,6*v+5], KP[2*v+1,6*v+4] = -1,1,-1
    R, E = zeros(3*count,6*count), zeros(6*count,3*count)
    SE, KE = zeros(6*count,3*count), zeros(3*count,6*count)
    for v in range(count):
        for j, d in enumerate(directions):
            edge = 3*v+j
            w = shifts[j][v]
            R[edge,6*v+j] = 1
            R[edge,6*w+j+3] = 1
            E[6*v+j,edge] = 1
            E[6*w+j+3,edge] = -1
            SE[6*v+j,edge] = 1
            KE[edge,6*w+j+3] = -1
    assert H*P == zeros(4*count,2*count)
    assert R*E == zeros(3*count,3*count)
    assert H*SP == eye(4*count) and R*SE == eye(3*count)
    assert eye(6*count)-SP*H == P*KP
    assert eye(6*count)-SE*R == E*KE
    B, T = H*E, R*P
    forward, backward = R*SP, H*SE
    assert forward*backward == eye(3*count)
    assert backward*forward == eye(4*count)-B*KE*SP
    assert forward*B == -T*KP*E
    assert backward*T == -B*KE*P

    # Function convention: x f(v)=f(v+e1), y f(v)=f(v+e2).
    explicit_T = zeros(3*count,2*count)
    for v in range(count):
        explicit_T[3*v,2*v] += 1
        explicit_T[3*v,2*shifts[0][v]] -= 1
        explicit_T[3*v+1,2*v+1] += 1
        explicit_T[3*v+1,2*shifts[1][v]+1] -= 1
        explicit_T[3*v+2,2*v+1] += 1
        explicit_T[3*v+2,2*v] -= 1
        explicit_T[3*v+2,2*shifts[2][v]+1] -= 1
        explicit_T[3*v+2,2*shifts[2][v]] += 1
    assert T == explicit_T
    td = positive_smith(T)
    diagonal, TU, TV, TUi, TVi, rank = td
    assert rank == 2*count-2
    invariants = [int(diagonal[i,i]) for i in range(rank) if diagonal[i,i] > 1]
    assert invariants == ([first] if first > 1 else [])
    K = TV[:,rank:]
    constants = zeros(2*count,2)
    for v in range(count):
        constants[2*v,0], constants[2*v+1,1] = 1,1
    assert T*constants == zeros(3*count,2)
    assert K == constants*K[:2,:]
    assert abs(K[:2,:].det()) == 1

    # A primitive generator of every nontrivial normalization torsion group.
    f = Matrix([coordinate for p,q in values for coordinate in (q,-p)])
    torsion = integral(T*f/first)
    assert first*torsion == T*f
    z = TU*torsion
    assert z[rank:,:] == zeros(3*count-rank,1)
    order = 1
    for i in range(rank):
        order = lcm(order, int(diagonal[i,i])//gcd(int(diagonal[i,i]),int(z[i])))
    assert order == first

    # The dual triangulated torus, its full cycle map and inverse paths.
    d1, d2 = zeros(count,3*count), zeros(3*count,2*count)
    displacement = zeros(2,3*count)
    for v in range(count):
        for j,d in enumerate(directions):
            d1[shifts[j][v],3*v+j] += 1
            d1[v,3*v+j] -= 1
            displacement[:,3*v+j] = Matrix(d)
        vp, vq = shifts[0][v], shifts[1][v]
        d2[3*v,2*v] += 1
        d2[3*vp+2,2*v] += 1
        d2[3*v+1,2*v] -= 1
        d2[3*vp+1,2*v+1] += 1
        d2[3*vq,2*v+1] -= 1
        d2[3*vp+2,2*v+1] -= 1
    assert d1*d2 == zeros(count,2*count)
    assert displacement*d2 == zeros(2,2*count)
    d1d, d2d = positive_smith(d1), positive_smith(d2)
    assert d1d[-1] == count-1 and d2d[-1] == 2*count-1
    assert all(abs(d1d[0][i,i]) == 1 for i in range(d1d[-1]))
    assert all(abs(d2d[0][i,i]) == 1 for i in range(d2d[-1]))
    cycle_basis = d1d[2][:,count-1:]
    cycle_map = integral(L.inv()*displacement*cycle_basis)
    paths = zeros(3*count,2)
    for j in range(2):
        pos = 0
        for direction, steps in ((0,int(L[0,j])),(1,int(L[1,j]))):
            assert steps >= 0
            for _ in range(steps):
                paths[3*pos+direction,j] += 1
                pos = shifts[direction][pos]
        assert pos == 0
    assert d1*paths == zeros(count,2)
    assert L.inv()*displacement*paths == eye(2)
    cycles_to_fill = cycle_basis-paths*cycle_map
    fillings = preimage(d2,d2d,cycles_to_fill)
    assert d2*fillings+paths*cycle_map == cycle_basis
    assert d2*Matrix.ones(2*count,1) == zeros(3*count,1)

    # Actual monodromy: short/long block marking, then the Smith period basis.
    sd, U, V, Ui, Vi, lr = positive_smith(L)
    assert lr == 2 and sd == Matrix.diag(first,second)
    A = eye(4)
    A[:2,2:] = L
    basis = zeros(4,4)
    basis[:2,0], basis[2:,1], basis[:2,2], basis[2:,3] = (
        Ui[:,0],V[:,0],Ui[:,1],V[:,1])
    basis_inv = integral(basis.inv())
    As = basis_inv*A*basis
    expected = eye(4)
    expected[0,1], expected[2,3] = first,second
    assert As == expected
    wedge_basis = exterior(basis)
    assert exterior(basis_inv)*wedge_basis == eye(6)
    W = exterior(As)-eye(6)
    area, zeta = zeros(6,1),zeros(6,1)
    area[1] = 1
    zeta[1],zeta[2],zeta[3] = second,1,second//first
    Cw = Matrix.hstack(area,zeta,eye(6)[:,0],eye(6)[:,3],
                       eye(6)[:,4],eye(6)[:,5])
    Cwi = integral(Cw.inv())
    expected_image = Matrix.hstack(first*area,first*zeta)
    wd = positive_smith(W)
    preimage(W,wd,expected_image)
    image_coordinates = Cwi*W
    assert image_coordinates[2:,:] == zeros(4,6)
    assert all(int(x) % first == 0 for x in image_coordinates[:2,:])
    fibre_kernel = Matrix.hstack(area,first*zeta)
    assert group(W) == (4,([first,first] if first > 1 else []))
    assert group(fibre_kernel) == (4,([first] if first > 1 else []))
    assert Cwi*Cw == eye(6)

    # Component meridians: exact map to Z theta plus the actual finite quotient.
    smith_index = {}
    for v,(p,q) in enumerate(values):
        coord = U*Matrix([p,q])
        key = (int(coord[0]) % first,int(coord[1]) % second)
        assert key not in smith_index
        smith_index[key] = v
    assert len(smith_index) == count
    coords = {v:key for key,v in smith_index.items()}
    M = Matrix([[1]*count,
                [coords[v][0] for v in range(count)],
                [coords[v][1] for v in range(count)]])
    origin = smith_index[(0,0)]
    active = []
    if first > 1:
        active.append((0,first,smith_index[(1,0)]))
    if second > 1:
        active.append((1,second,smith_index[(0,1)]))
    others = [v for v in range(count)
              if v != origin and v not in [u[2] for u in active]]
    disk_basis, inverse_rows = [],[]
    for axis,modulus,v in active:
        col = zeros(count,1)
        col[v],col[origin] = modulus,-modulus
        disk_basis.append(col)
        inverse_rows.append(Matrix([[Rational(coords[w][axis],modulus)
                                     for w in range(count)]]))
    for v in others:
        col = zeros(count,1)
        col[v],col[origin] = 1,-1
        for axis,modulus,w in active:
            coefficient = coords[v][axis]
            col[w] -= coefficient
            col[origin] += coefficient
        disk_basis.append(col)
        row = zeros(1,count)
        row[v] = 1
        inverse_rows.append(row)
    DK = Matrix.hstack(*disk_basis) if disk_basis else zeros(count,0)
    DI = Matrix.vstack(*inverse_rows) if inverse_rows else zeros(0,count)
    assert DK.cols == count-1 and DI*DK == eye(count-1)
    rel = Matrix([[0,0],[first,0],[0,second]])
    augmented = Matrix.hstack(M,-rel)
    ad = positive_smith(augmented)
    ak = ad[2][:,ad[-1]:]
    projected = ak[:count,:]
    assert integral(DI*projected).shape == (count-1,count-1)
    assert DK*DI*projected == projected
    assert M*DK == rel*integral(Matrix.diag(
        Rational(1,first),Rational(1,second))*(M*DK)[1:,:])

    return {
        "L": rows(L), "index": count, "smith": [first,second],
        "components": [list(v) for v in values], "shifts": shifts,
        "normalization_coker": [count+2,invariants],
        "torsion_generator": [int(x) for x in torsion],
        "torsion_order": order, "torus_H1_paths": rows(paths),
        "period_basis": rows(basis), "period_basis_inverse": rows(basis_inv),
        "wedge_quotient_basis": rows(Cw), "wedge_quotient_inverse": rows(Cwi),
        "fibre_kernel": rows(wedge_basis*fibre_kernel),
        "disc_basis": rows(DK),
        "disc_inverse": [[str(x) for x in row] for row in DI.tolist()],
        "cap_H2": [count+3,([first] if first > 1 else [])],
        "boundary_H2": [6,([first,first] if first > 1 else [])],
    }


def main():
    cases = []
    for index in range(1,13):
        for a in range(1,index+1):
            if index % a == 0:
                c = index//a
                cases.extend((a,b,c) for b in range(a))
    extras = [(3,0,6),(4,0,4),(4,2,4),(4,0,8),
              (5,0,5),(6,0,6),(6,3,6),(6,2,6),
              (8,4,4),(9,3,3),(12,6,3),(2,1,18)]
    cases.extend(x for x in extras if x not in cases)
    records = []
    print("SCOPE all column-HNF sublattices of index <=12, plus 12 declared larger cases",flush=True)
    print("SCOPE new toric normalization maps; shared generic integer helper is disclosed",flush=True)
    for i,(a,b,c) in enumerate(cases,1):
        record = one_lattice(a,b,c)
        records.append(record)
        s,t = record["smith"]
        print(f"PASS {i:03d} L=({a},{b};0,{c}) D={a*c} s,t={s},{t} "
              f"norm_coker=Z^{a*c+2}+Z/{s} "
              f"capH2=Z^{a*c+3}+Z/{s} "
              f"disc_rank={a*c-1} torsion_order={record['torsion_order']}",flush=True)
    data = {"scope":"finite checks only; all-L proof is written separately",
            "cases":records}
    DATA.write_text(json.dumps(data,sort_keys=True,separators=(",",":"))+"\n")
    reread = json.loads(DATA.read_text())
    assert reread == data
    for r in reread["cases"]:
        B, Bi = Matrix(r["period_basis"]),Matrix(r["period_basis_inverse"])
        Q, Qi = Matrix(r["wedge_quotient_basis"]),Matrix(r["wedge_quotient_inverse"])
        assert B*Bi == eye(4) and Q*Qi == eye(6)
        K = Matrix(r["disc_basis"])
        if r["index"] > 1:
            Ki = Matrix([[Rational(x) for x in row] for row in r["disc_inverse"]])
            assert Ki*K == eye(r["index"]-1)
        assert r["torsion_order"] == r["smith"][0]
    print("PASS saved records reread literally; every saved period/wedge/disc inverse rechecked",flush=True)
    print("COMPLETE cases",len(records),"indices",sorted({r["index"] for r in records}),
          "nonprimitive_short",sum(r["smith"][0] > 1 for r in records),flush=True)
    print("DATA_SHA256",sha256(DATA.read_bytes()).hexdigest(),flush=True)
    print("COMPLETED_UTC",datetime.now(timezone.utc).isoformat(),flush=True)


if __name__ == "__main__":
    main()
