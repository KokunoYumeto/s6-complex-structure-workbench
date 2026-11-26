#!/usr/bin/env python3
"""Independent arithmetic for fresh 02KQ; no target proof is read."""
from pathlib import Path
from itertools import combinations
from functools import reduce
import json
import math
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'agents/continuation6_iii_carriers/S6_SERIES_PUBLISH_III_02KQ_raw_definitions.json'
J = sp.Matrix([[0, 1], [-1, 0]])
I2, I4 = sp.eye(2), sp.eye(4)
e = [I4[:, k] for k in range(4)]
pairs = list(combinations(range(4), 2))


def wedge2(M):
    return sp.Matrix([[M.extract(i, j).det() for j in pairs] for i in pairs])


def snf_entries(M):
    S = smith_normal_form(M, domain=ZZ)
    return [abs(int(S[i, i])) for i in range(min(S.shape))]


def integer_diagonalize(M):
    """Euclidean elementary operations, keeping both exact inverse maps."""
    W, U, V = M.copy(), sp.eye(M.rows), sp.eye(M.cols)

    def swap_rows(i, k):
        W.row_swap(i, k)
        U.row_swap(i, k)

    def swap_cols(j, k):
        W.col_swap(j, k)
        V.col_swap(j, k)

    def add_row(i, k, q):
        W[i, :] = W[i, :] + q*W[k, :]
        U[i, :] = U[i, :] + q*U[k, :]

    def add_col(j, k, q):
        W[:, j] = W[:, j] + q*W[:, k]
        V[:, j] = V[:, j] + q*V[:, k]

    for k in range(min(W.shape)):
        entries = [(abs(W[i, j]), i, j)
                   for i in range(k, W.rows) for j in range(k, W.cols)
                   if W[i, j]]
        if not entries:
            break
        _, i, j = min(entries)
        swap_rows(i, k)
        swap_cols(j, k)
        while True:
            restart = False
            for i in range(k+1, W.rows):
                if W[i, k]:
                    q, rem = divmod(W[i, k], W[k, k])
                    add_row(i, k, -q)
                    if rem:
                        swap_rows(i, k)
                        restart = True
                        break
            if restart:
                continue
            for j in range(k+1, W.cols):
                if W[k, j]:
                    q, rem = divmod(W[k, j], W[k, k])
                    add_col(j, k, -q)
                    if rem:
                        swap_cols(j, k)
                        restart = True
                        break
            if restart:
                continue
            bad = next(((i, j) for i in range(k+1, W.rows)
                        for j in range(k+1, W.cols)
                        if W[i, j] % W[k, k]), None)
            if bad is None:
                break
            add_row(k, bad[0], 1)
        if W[k, k] < 0:
            W[k, :] = -W[k, :]
            U[k, :] = -U[k, :]
    assert U*M*V == W
    assert abs(U.det()) == abs(V.det()) == 1
    assert U*U.inv() == sp.eye(M.rows) and V*V.inv() == sp.eye(M.cols)
    assert [int(W[k, k]) for k in range(min(W.shape))] == snf_entries(M)
    return W, U, V


def split_inverse(M):
    W, U, V = integer_diagonalize(M)
    rank = M.rank()
    assert [W[k, k] for k in range(rank)] == [1]*rank
    out = V[:, :rank] * U[:rank, :]
    assert M*out*M == M
    return out


def rational_solve(A, rhs):
    out, parameters = A.gauss_jordan_solve(rhs)
    return out.subs({s: 0 for s in parameters})


def transvection(u):
    u = sp.Matrix(u)
    return I2 + u * u.T * J


A, B, C = [transvection(u) for u in [(1, 0), (1, -1), (1, 1)]]
assert B * C == sp.Matrix([[-1, 4], [0, -1]])
print('Fresh 02KQ arithmetic; defining rows only; all calculations exact.')
maps = {}
for row in json.loads(DATA.read_text())['rows']:
    os = row['OS']
    p, j, free_b = {46: (4, 3, 2), 50: (12, 1, 1)}[os]
    As = [sp.Matrix(a) for a in row['elliptic_matrices']]
    gs = [sp.Matrix(g) for g in row['generator_section_cocycle']]
    assert As == [A ** (j + 4) * B * C, A ** (4 - j), B, C]
    product, cocycle = I2, sp.zeros(2, 1)
    for Ai, gi in zip(As, gs):
        cocycle += product * gi
        product *= Ai
    assert product == I2 and cocycle == sp.zeros(2, 1)
    Ts = []
    local_h = []
    local_z = []
    for k, (Ai, gi) in enumerate(zip(As, gs)):
        zi = rational_solve(Ai-I2, gi)
        hi = p * zi
        beta = -p * gi.T * J * Ai
        bi = -hi.T * J
        Si = sp.eye(4)
        Si[:2, 3] = zi
        Si[2, :2] = bi
        Si[2, 3] = (bi * zi)[0]
        T = sp.eye(4)
        T[:2, :2] = Ai
        T[:2, 3] = gi
        T[2, :2] = beta
        T[2, 3] = (beta * zi)[0] + int(k == 2)
        standard = sp.diag(Ai, 1, 1)
        standard[2, 3] += int(k == 2)
        assert T == Si.inv() * standard * Si
        assert all(x.q == 1 for x in T)
        Ts.append(T)
        local_h.append(hi)
        local_z.append(zi)
    assert reduce(lambda x, y: x*y, Ts, I4) == I4
    omega = sp.Matrix([[p, 0, 0, 0, 0, -1]])
    for T in Ts:
        assert omega * wedge2(T) == omega
    print('\nOS', os, 'j', j, 'b', free_b, 'p', p)
    print('elliptic product I and section product zero; four-period matrices:')
    for k, T in enumerate(Ts, 1):
        print('T'+str(k), T.tolist())
    hs = local_h[0]
    zs = local_z[0]
    bs = -hs.T * J
    component_row = sp.Matrix([[2, 1]])
    assert (As[0]-I2).det() == 4
    assert all(int(x) % 4 == 0 for x in component_row*(As[0]-I2))
    assert component_row*sp.Matrix([0,1]) == sp.ones(1,1)
    assert int((component_row*gs[0])[0]) % 4 == 3
    assert int((component_row*(-gs[0]))[0]) % 4 == 1
    h1 = sp.Matrix([[bs[0], bs[1], 1, 0], [0, 0, 0, 1]])
    assert h1 * Ts[0] == h1
    assert h1 * sp.Matrix.hstack(e[2], e[3]) == sp.eye(2)
    l = sp.Matrix([[4, 0, 4*zs[1], 0, -4*zs[0], 0]])
    d = sp.Matrix([[0, 0, bs[0], 0, bs[1], 1]])
    assert l * wedge2(Ts[0]) == l
    assert d * wedge2(Ts[0]) == d
    assert (p // 4) * l - d == omega
    print('star H1 boundary rows', h1.tolist())
    print('star H2 boundary rows l,d', l.tolist(), d.tolist())
    print('star boundary fibre coinvariants SNF', snf_entries(wedge2(Ts[0])-sp.eye(6)))
    w_preimage = (sp.Matrix([0, 0, 0, 0, -1, -1]) if os == 46
                  else sp.Matrix([1, 0, 0, 0, 1, 9]))
    d_preimage = sp.eye(6)[:, 5]
    spec = l.col_join(d)
    spec_section = sp.Matrix.hstack(w_preimage, d_preimage)
    assert spec*spec_section == sp.eye(2)
    star_relation = wedge2(Ts[0])-sp.eye(6)
    star_split = split_inverse(star_relation)
    assert star_relation*star_split*(sp.eye(6)-spec_section*spec) == sp.eye(6)-spec_section*spec
    star_fixed = sp.Matrix.hstack(e[2], sp.Matrix([-4*zs[0], -4*zs[1], 0, 4]))
    if os == 46:
        node2_fixed = sp.Matrix.hstack(e[0], e[2], e[3])
    else:
        node2_fixed = sp.Matrix.hstack(sp.Matrix([1, 0, 8, 0]), e[2], sp.Matrix([0, 2, 0, 3]))
    cusp_fixed = sp.Matrix.hstack(sp.Matrix([1, -1, 0, 0]), e[2])
    node4_fixed = sp.Matrix.hstack(sp.Matrix([1, 1, p, 0]), e[2], sp.Matrix([0, 1, 0, 1]))
    Fs = [star_fixed, node2_fixed, cusp_fixed, node4_fixed]
    for T, F in zip(Ts, Fs):
        assert (T-I4)*F == sp.zeros(4, F.cols)
        assert snf_entries(F) == [1] * F.cols
        assert T*e[2] == e[2] and e[3].T*T == e[3].T
    H2 = (I4 if os == 46 else sp.Matrix.hstack(
        sp.Matrix([1, 0, 8, 0]), sp.Matrix([0, 1, 0, 1]),
        e[2], sp.Matrix([0, 2, 0, 3])))
    H3 = sp.diag(sp.Matrix([[1, 0], [-1, 1]]), 1, 1)
    H4 = sp.Matrix.hstack(sp.Matrix([1, 1, p, 0]), e[1], e[2], sp.Matrix([0, 1, 0, 1]))
    normal = sp.eye(4)
    normal[0, 1] = 1
    cusp_normal = normal.copy()
    cusp_normal[2, 3] = 1
    for HH, TT, NN in [(H2, Ts[1], normal), (H3, Ts[2], cusp_normal), (H4, Ts[3], normal)]:
        assert abs(HH.det()) == 1 and HH.inv()*TT*HH == NN
        assert HH*e[2] == e[2]
    D = sp.Matrix.hstack(sp.zeros(4), *[T-I4 for T in Ts[:3]])

    def inclusion(k, F):
        if k < 4:
            return sp.zeros(4*k, F.cols).col_join(F).col_join(sp.zeros(4*(3-k), F.cols))
        return -sp.Matrix.vstack(Ts[0]*Ts[1]*Ts[2]*F, Ts[1]*Ts[2]*F, Ts[2]*F, F)

    Bgraph = sp.Matrix.hstack(*[inclusion(k, F) for k, F in enumerate(Fs, 1)])
    assert D*inclusion(4, I4) == I4-Ts[3].inv()
    Kgraph = sp.Matrix.hstack(Bgraph, inclusion(0, sp.Matrix.hstack(e[0], e[1], e[3])))
    assert D * Kgraph == sp.zeros(4, Kgraph.cols)
    print('D first-three-row SNF', snf_entries(D[:3, :]))
    print('graph kernel rank and K SNF', 16-D.rank(), snf_entries(Kgraph))
    graph_left_inverse = split_inverse(Kgraph)
    graph_complement = split_inverse(D[:3, :])
    assert graph_left_inverse*Kgraph == sp.eye(13)
    assert D[:3, :]*graph_complement == sp.eye(3)
    kernel_projector = sp.eye(16)-graph_complement*D[:3, :]
    assert Kgraph*graph_left_inverse*kernel_projector == kernel_projector
    c_delta = graph_left_inverse*inclusion(0, e[2])
    assert c_delta == sp.Matrix([-1, 0, 0, -1, 0, 0, -1, 0, -1, 0, 0, 0, 0])
    B2 = sp.Matrix.hstack(sp.zeros(6), *[wedge2(T)-sp.eye(6) for T in Ts[:3]])
    print('global exterior-square relation SNF', snf_entries(B2))
    Fglobal = sp.Matrix.hstack(sp.Matrix([1, 0, 0, 0, 0, p]), *[sp.eye(6)[:, k] for k in range(1, 5)])
    global_split = split_inverse(B2)
    global_cylinders = global_split*Fglobal
    assert B2*global_cylinders == Fglobal
    s = -sp.eye(6)[:, 5]
    assert omega*s == sp.ones(1, 1)
    assert abs(sp.Matrix.hstack(s, Fglobal).det()) == 1

    # Original affine D-configuration: four outer components and 2b middle ones.
    count = 4 + 2*free_b
    permutation = [2, 3, 1, 0] + [4+2*free_b-1-k for k in range(2*free_b)]
    P = sp.zeros(count)
    for k, dest in enumerate(permutation):
        P[dest, k] = 1
    assert P**4 == sp.eye(count)
    assert (P.inv()-sp.eye(count))*(-P) == P-sp.eye(count)
    assert (-P)*(-P.inv()) == sp.eye(count)
    orbit_rows = [[0, 1, 2, 3]] + [[4+k, 4+2*free_b-1-k] for k in range(free_b)]
    orbit_quotient = sp.zeros(free_b+1, count)
    orbit_section = sp.zeros(count, free_b+1)
    orbit_sum = sp.zeros(count, free_b+1)
    for k, indices in enumerate(orbit_rows):
        orbit_section[indices[0], k] = 1
        for i in indices:
            orbit_quotient[k, i] = 1
            orbit_sum[i, k] = 1
    assert orbit_quotient*orbit_section == sp.eye(free_b+1)
    assert orbit_quotient*(P-sp.eye(count)) == sp.zeros(free_b+1, count)
    assert (P-sp.eye(count))*orbit_sum == sp.zeros(count, free_b+1)
    assert orbit_section.T*orbit_sum == sp.eye(free_b+1)
    orbit_relation_inverse = split_inverse(P-sp.eye(count))
    assert (P-sp.eye(count))*orbit_relation_inverse*(sp.eye(count)-orbit_section*orbit_quotient) == sp.eye(count)-orbit_section*orbit_quotient
    multiplicities = sp.Matrix([1]*4+[2]*(2*free_b))
    assert orbit_quotient*multiplicities == sp.ones(free_b+1, 1)*4
    print('component orbit sizes', [len(o) for o in orbit_rows], '; fibre orbit coefficients all 4')
    maps[str(os)] = {name: value.tolist() for name, value in {
        'T1': Ts[0], 'T2': Ts[1], 'T3': Ts[2], 'T4': Ts[3],
        'D': D, 'K': Kgraph, 'L': graph_left_inverse,
        'C': graph_complement, 'B2': B2, 'Z': global_cylinders,
        'star_h1': h1, 'star_spec': spec, 'star_spec_section': spec_section,
        'star_relation_inverse': star_split,
        'component_permutation': P, 'component_quotient': orbit_quotient,
        'component_section': orbit_section, 'component_invariants': orbit_sum,
        'component_relation_inverse': orbit_relation_inverse,
        'H2_local': H2, 'H3_local': H3, 'H4_local': H4,
        'star_component_row': component_row,
        'F1': Fs[0], 'F2': Fs[1], 'F3': Fs[2], 'F4': Fs[3],
    }.items()}

output = ROOT / 'agents/continuation6_iii_carriers/S6_SERIES_PUBLISH_III_02KQ_fresh_maps.json'

# The two rows are tested by a separate determinantal calculation for the log.
mS, aS, bS, cS, nS, pS = sp.symbols('m a b c n p', integer=True)
RS = sp.Matrix([[-pS*bS, pS*aS, nS, -cS, 0],
                [mS, 0, 0, 0, aS], [0, mS, 0, 0, bS],
                [0, 0, 0, mS, nS]])
qS = sp.Matrix([-aS, -bS, -cS, -nS, mS])
assert RS*qS == sp.zeros(4, 1)
cofactors = sp.Matrix([(-1)**k*RS[:, [j for j in range(5) if j != k]].det()
                       for k in range(5)])
assert sp.simplify(cofactors-mS**2*nS*qS) == sp.zeros(5, 1)
print('Symbolic maximal-minor vector is m^2*n*(-a,-b,-c,-n,m).')
normal_discs = sp.Matrix([[-nS,0,0,0,0], [mS,0,0,0,-1],
                          [0,1,0,0,-1], [0,0,1,0,-1], [0,0,0,1,-1]])
assert normal_discs.det() == -nS
assert normal_discs.subs(nS,0)*sp.Matrix([1,mS,mS,mS,mS]) == sp.zeros(5,1)
assert normal_discs.subs(nS,0).rank() == 4
theta = sp.symbols('theta', real=True)
rotation = sp.diag(sp.Matrix([[sp.cos(theta),-sp.sin(theta)],
                             [sp.sin(theta),sp.cos(theta)]]), 1, 1, 1)
reflection_pair = sp.diag(1,-1,-1,1,1)
assert reflection_pair*rotation*reflection_pair == rotation.T
assert sp.simplify(rotation.T*rotation) == sp.eye(5)
assert reflection_pair.det() == 1
print('Normal-disc determinant -n and zero-n primitive kernel checked; suspension rotation/inverse checked.')

parameter_rows = [
    (1, 0, 0, 0, 0), (1, 0, 0, 0, 1), (1, 0, 0, 0, -1),
    (2, 0, 0, 1, 0), (3, 1, 0, 0, 0), (4, 0, 1, 0, 0),
    (6, 2, 0, 3, 0), (12, 4, 6, 5, 0), (6, 0, 0, 1, 0),
    (12, 4, 0, 3, 6), (12, 4, 0, 3, -6), (8, -2, 3, 4, -6),
    (5, 0, 0, 0, 2), (5, 0, 0, 0, -2), (7, 0, 0, 0, 3),
    (8, 2, 0, 3, 4), (9, 3, 1, 0, 6), (10, 1, 2, 4, -5),
    (11, 2, 3, -5, 7), (24, 8, 0, 3, 12), (36, 4, 0, 9, 18),
    (30, 2, 0, 5, 6), (30, 2, 0, 5, -6), (16, 0, 0, 1, 8),
    (8, -11, 15, 22, 1), (8, -11, 15, 22, -1),
    (125, 5, 10, 3, 25), (72, 16, 0, 9, 24),
]
log_maps = {}
for p in (4, 12):
    shown = []
    for m, a, bp, c, n in parameter_rows:
        assert math.gcd(m, a, bp, c, n) == 1
        d1 = math.gcd(m, n, a, bp)
        d2 = math.gcd(m, n, p, c)
        t = d1*d2
        assert math.gcd(d1, d2) == 1 and m % t == 0 and n % t == 0
        R = RS.subs({mS:m, aS:a, bS:bp, cS:c, nS:n, pS:p})
        q = qS.subs({mS:m, aS:a, bS:bp, cS:c, nS:n})
        W0, U0, V0 = integer_diagonalize(q)
        assert V0 == sp.ones(1, 1) and U0*q == sp.eye(5)[:, 0]
        H, E = U0[1:, :], U0.inv()[:, 1:]
        r = U0[:1, :]
        assert H*E == sp.eye(4) and H*q == sp.zeros(4, 1)
        assert E*H+q*r == sp.eye(5)
        M = R*E
        W, U, V = integer_diagonalize(M)
        expected = [1, t, m, m*abs(n)//t if n else 0]
        assert [int(W[k, k]) for k in range(4)] == expected
        # Independent check of every determinantal divisor of R.
        for k in range(1, 5):
            minors = [abs(int(R.extract(rr, cc).det()))
                      for rr in combinations(range(4), k)
                      for cc in combinations(range(5), k)]
            wanted = math.prod(expected[:k])
            assert math.gcd(*minors) == wanted
        if n == 0:
            free_row = sp.Matrix([[m, p*bp, -p*a, c]])/d2
            assert free_row*R == sp.zeros(1, 5)
            assert math.gcd(*[int(x) for x in free_row]) == 1
            ds = math.gcd(m, a, bp)
            aa, bb, gg = sp.gcdex(c, ds)
            assert gg == 1 and aa*c+bb*ds == 1
            us = sp.Matrix([-a//ds, -bp//ds, 0, 0, m//ds])
            ed = sp.eye(5)[:, 2]
            lam = aa*us+bb*ed
            assert q == ds*us-c*ed and R*lam == sp.zeros(4, 1)
            kernel_coordinates = V.inv()*H*lam
            assert list(kernel_coordinates[:3, :]) == [0, 0, 0]
            assert abs(kernel_coordinates[3]) == 1
        if n in (-1, 1):
            primitive_delta = sp.Matrix([[0, 0, 1, -sp.Rational(c, n), 0]])
            assert primitive_delta*q == sp.zeros(1, 1)
            assert primitive_delta*sp.eye(5)[:, 2] == sp.ones(1, 1)
            assert t == 1 and expected == [1, 1, m, m]
        shown.append((m, a, bp, c, n, t, expected))
        if (m, a, bp, c, n) in [(6, 2, 0, 3, 0), (12, 4, 0, 3, -6), (8, -11, 15, 22, -1)]:
            key = f'p{p}_m{m}_n{n}_a{a}_b{bp}_c{c}'
            log_maps[key] = {name: value.tolist() for name, value in {
                'q': q, 'H': H, 'E': E, 'R': R, 'U': U, 'V': V, 'Smith': W,
            }.items()}
    print('p', p, ':', len(shown), 'primitive log cases; all minors and all inverse maps agree.')
    for m, a, bp, c, n, t, expected in shown:
        print(' log', (m,a,bp,c,n), 't', t, 'Smith', expected)
maps['log_examples'] = log_maps
output.write_text(json.dumps(maps, default=int, indent=2)+'\n')

print('\nAll exact period, graph, quotient, component, logarithm and inverse-map checks passed.')
