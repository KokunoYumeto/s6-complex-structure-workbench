#!/usr/bin/env python3
"""Fresh LN all-parameter integral gluing, from the admitted raw fixture.

This constructs the unsaturated six-dimensional fibre presentation, the
integer graph kernel with both coordinate maps, the transported last
cochain, every fixed normal and all five logarithmic columns. It never
reads a historical LN program/output or a target proof.
"""
from pathlib import Path
from hashlib import sha256
from itertools import combinations
from math import gcd, lcm
import json
import sympy as sp
from sympy import ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from sympy.matrices.normalforms import hermite_normal_form

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json'
assert sha256(SOURCE.read_bytes()).hexdigest() == \
    '6bda97b01ba63c0a796e3141609ca12e163791b626024b79104817ec5defc522'
ROWS = json.loads(SOURCE.read_text())['rows']
PAIRS = list(combinations(range(4), 2))
J = sp.Matrix([[0, 1], [-1, 0]])
E4 = sp.eye(4)
E6 = sp.eye(6)
DELTA, GAMMA = E4[:, 2], E4[:, 3]


def integer(M):
    assert all(x.q == 1 for x in M)
    return sp.Matrix(M)


def smith(M):
    M = integer(M)
    d, u, v = smith_normal_decomp(DomainMatrix.from_Matrix(M).convert_to(ZZ))
    D, U, V = d.to_Matrix(), u.to_Matrix(), v.to_Matrix()
    assert U*M*V == D
    # The decomposition also supplies the inverse coordinate maps.
    Ui, Vi = integer(U.inv()), integer(V.inv())
    assert Ui*U == sp.eye(U.rows) and Vi*V == sp.eye(V.rows)
    rank = sum(D[i, i] != 0 for i in range(min(D.shape)))
    return D, U, V, Ui, Vi, rank


def kernel(M):
    D, U, V, Ui, Vi, rank = smith(M)
    K, L = V[:, rank:], Vi[rank:, :]
    assert M*K == sp.zeros(M.rows, K.cols)
    assert L*K == sp.eye(K.cols)
    return K, L


def saturated_image(M):
    D, U, V, Ui, Vi, rank = smith(M)
    F, L = Ui[:, :rank], U[:rank, :]
    assert L*F == sp.eye(rank)
    return F


def invariants(M):
    D, U, V, Ui, Vi, rank = smith(M)
    tors = tuple(abs(int(D[i, i])) for i in range(rank) if abs(D[i, i]) > 1)
    # For every finite quotient generator, retain its actual annihilating chain.
    for i in range(rank):
        assert M*V[:, i] == D[i, i]*Ui[:, i]
    return M.rows-rank, tors


def wedge(x, y):
    return sp.Matrix([x[i]*y[j]-x[j]*y[i] for i, j in PAIRS])


def wedge_matrix(A):
    return sp.Matrix.hstack(*(wedge(A[:, i], A[:, j]) for i, j in PAIRS))


def ordered_pairing(x, y):
    return sp.Matrix([x[i]*y[j] for i, j in PAIRS])


def quadratic_correction(A):
    WA = wedge_matrix(A)
    D = {}
    for i in range(4):
        for j in range(i, 4):
            Dij = ordered_pairing(A[:, i], A[:, j])-WA*ordered_pairing(E4[:, i], E4[:, j])
            D[i, j] = Dij
            reverse = ordered_pairing(A[:, j], A[:, i])-WA*ordered_pairing(E4[:, j], E4[:, i])
            assert Dij == reverse
    def f(x):
        value = sp.zeros(6, 1)
        for i in range(4):
            value -= D[i, i]*x[i]*(x[i]-1)/2
            for j in range(i+1, 4):
                value -= D[i, j]*x[i]*x[j]
        return integer(value)
    return f


def bezout(a, b):
    s, t, d = sp.gcdex(a, b)
    assert a*s+b*t == d == 1
    return int(s), int(t)


def local_raw(B, g, kind):
    if kind.startswith('I') and kind[1:].isdigit():
        N = B-sp.eye(2)
        col = next(N[:, j] for j in range(2) if N[:, j] != sp.zeros(2, 1))
        u = col/gcd(*[abs(int(x)) for x in col])
        if next(x for x in u if x) < 0:
            u = -u
        s, t = bezout(int(u[0]), int(u[1]))
        r = sp.Matrix([-t, s])
        H = sp.Matrix.hstack(u, r)
        nu = int((H.inv()*N*H)[0, 1])
        kappa = int((H.inv()*g)[0])
        assert N == nu*u*u.T*J and g == kappa*u
        z = sp.Rational(kappa, nu)*r
        return z, (nu, kappa, u, r)
    return (B-sp.eye(2)).inv()*g, None


def make_local(row, a, b, weights, mode):
    answer = []
    for i, kind in enumerate(row['fibers']):
        B = sp.Matrix(row['elliptic_matrices'][i])
        g = sp.Matrix(row['generator_section_cocycle'][i])
        z0, mult = local_raw(B, g, kind)
        qorder = lcm(*[int(x.q) for x in z0])
        narrow_p, narrow_q = a % qorder == 0, b % qorder == 0
        assert narrow_p or narrow_q
        w = weights.get(i, 0)
        assert not w or mult is not None
        r = -a*g.T*J*B
        A = sp.eye(4)
        A[:2, :2], A[:2, 3], A[2, :2] = B, b*g, r
        A[2, 3] = (r*(b*z0))[0]+w
        A = integer(A)
        assert A.det() == 1
        cap = 'positive' if w else 'original'
        finite_good = kind in ('II', 'III', 'IV', 'III*', 'IV*')
        if mode == 'finite' and finite_good:
            cap = 'log'
        elif not w and mult is not None and mode in ('mixed', 'exception'):
            cap = 'mumford' if mode == 'exception' or i % 2 == 0 else 'original'
        data = dict(A=A, B=B, g=g, z=b*z0, kind=kind, w=w, cap=cap,
                    narrow_p=narrow_p, narrow_q=narrow_q, mult=mult, b=b)
        if cap == 'log':
            h = next(h for h in range(1, 7) if A**h == E4)
            assert narrow_q
            v = sp.Matrix([-b*z0[0], -b*z0[1], 0, 1])
            data.update(m=h, v=integer(v))
        answer.append(data)
    return answer


def regular_zero(w):
    assert w > 0
    A = sp.eye(4)
    A[2, 3] = w
    return dict(A=A, kind='regular', w=w, cap='positive', mult=None,
                narrow_p=True, narrow_q=True)


def regular_log(m, v, kind='regular-log'):
    return dict(A=E4, kind=kind, w=0, cap='log', m=m, v=sp.Matrix(v))


def orbit_count(kind, b):
    if kind == 'II':
        p = [0]
    elif kind == 'III':
        p = [1, 0]
    elif kind == 'IV':
        p = [1, 2, 0]
    elif kind == 'IV*':
        p = [1, 2, 0, 4, 5, 3, 6]
    elif kind == 'III*':
        p = [1, 0, 3, 2, 5, 4, 6, 7]
    elif kind.startswith('I') and kind.endswith('*'):
        n = int(kind[1:-1])
        p = [1, 2, 3, 0] + [4+n-j for j in range(n+1)]
    else:
        raise ValueError(kind)
    power = []
    for i in range(len(p)):
        j = i
        for unused in range(b % 12):
            j = p[j]
        power.append(j)
    seen, count = set(), 0
    for i in range(len(p)):
        if i not in seen:
            count += 1
            j = i
            while j not in seen:
                seen.add(j)
                j = power[j]
    return count, len(p)


def cap_data(c):
    A, kind = c['A'], c['kind']
    R = wedge_matrix(A)-E6
    fixed, fixed_read = kernel(A-E4)
    if c['cap'] == 'positive' and c['mult'] is not None:
        nu, kappa, u, r = c['mult']
        angle = wedge(fixed[:, 0], fixed[:, 1])
        F = sp.Matrix.hstack(R, angle)
        h4 = nu*c['w']
        killed = fixed
        s = gcd(*[abs(int(x)) for x in (A-E4)])
        # This uses the literal matrix; saturation would destroy the order-s class.
        assert invariants(R) == (4, (s, s) if s > 1 else ())
        assert invariants(F) == (4, (s,) if s > 1 else ())
        return F, fixed, killed, h4, s
    if c['cap'] in ('positive', 'mumford'):
        F = saturated_image(R)
        killed = saturated_image(A-E4)
        rho = gcd(*[abs(int(x)) for x in (A-E4)])
        assert killed.cols == 1 and rho > 0
        return F, fixed, killed, rho, None
    assert c['cap'] == 'original'
    if c['narrow_p']:
        F = saturated_image(R)
        killed = saturated_image(A-E4)
        if c['mult'] is not None:
            nu, kappa, u, r = c['mult']
            rho = gcd(nu, c['b']*kappa)
        else:
            rho, count = orbit_count(kind, c['b'])
        return F, fixed, killed, rho, None
    assert c['narrow_q']
    ell = integer(sp.Matrix([-c['z'][0], -c['z'][1], 0, 1]))
    if c['mult'] is None:
        omega = sp.Matrix([[1, 0, c['z'][1], 0, -c['z'][0], 0]])
        F, read = kernel(omega)
        killed = E4[:, :3]
        rho, count = orbit_count(kind, c['b'])
        return F, fixed, killed, count, None
    nu, kappa, u, r = c['mult']
    ue = sp.Matrix([u[0], u[1], 0, 0])
    F = sp.Matrix.hstack(wedge(ue, DELTA), wedge(ue, ell), wedge(DELTA, ell))
    killed = sp.Matrix.hstack(ue, DELTA)
    return F, fixed, killed, nu, None


def free_log(c):
    A, m, v = c['A'], c['m'], c['v']
    assert m > 0 and A*v == v
    h = next(h for h in range(1, 7) if A**h == E4)
    assert m % h == 0
    F, L = kernel(A-E4)
    norm = sum((A**j for j in range(h)), sp.zeros(4))
    H = hermite_normal_form(integer(L*norm))
    assert H.rows == H.cols == F.cols
    z = integer(L*v)
    w = integer(h*H.inv()*z)
    t = gcd(m, *map(int, w))
    assert gcd(m, *map(int, v)) == 1 and (m//t) % h == 0
    return h


def run(caps):
    As = [c['A'] for c in caps]
    n = len(As)
    product = E4
    for A in As:
        product *= A
    assert product == E4
    Dgraph = sp.Matrix.hstack(*(A-E4 for A in As[:-1]))
    K, Kread = kernel(Dgraph)
    suffix = []
    for i in range(n-1):
        P = E4
        for A in As[i+1:]:
            P *= A
        suffix.append(P)
    Js = []
    for i in range(n):
        Q = sp.zeros(4*(n-1), 4)
        if i < n-1:
            Q[4*i:4*i+4, :] = E4
        else:
            for j in range(n-1):
                Q[4*j:4*j+4, :] = -suffix[j]
        assert Dgraph*Q == As[i]-E4
        Js.append(Q)
    fs = [quadratic_correction(A) for A in As]
    def cvalue(i, x):
        if i < n-1:
            return fs[i](x)
        return -sum((fs[j](suffix[j]*x) for j in range(n-1)), sp.zeros(6, 1))
    def column(i, fibre, fixed):
        graph = Js[i]*fixed
        assert Dgraph*graph == sp.zeros(4, 1)
        assert K*(Kread*graph) == graph
        return fibre.col_join(Kread*graph)
    columns = []
    H1cols = []
    for A in As:
        for j in range(4):
            H1cols.append((A-E4)[:, j].col_join(sp.zeros(n, 1)))
    H1cols.append(sp.zeros(4, 1).col_join(sp.ones(n, 1)))
    H1after = list(H1cols)
    h4sum, chi, cusp_s, five_count = 0, 0, [], 0
    for i, c in enumerate(caps):
        A = As[i]
        R = wedge_matrix(A)-E6
        columns.extend(R[:, j].col_join(sp.zeros(K.cols, 1)) for j in range(6))
        if c['cap'] == 'log':
            h = free_log(c)
            m, v = c['m'], c['v']
            norm = sum((A**j for j in range(h)), sp.zeros(4))*(m//h)
            for j in range(4):
                lam = E4[:, j]
                first = (m//h)*sum((cvalue(i, A**k*lam) for k in range(h)), sp.zeros(6, 1))
                columns.append(column(i, first-wedge(lam, v), norm*lam))
            columns.append(column(i, cvalue(i, v), v))
            five_count += 5
            relation = (-v).col_join(sp.zeros(n, 1))
            relation[4+i] = m
            H1cols.append(relation)
            H1after.append(relation)
        else:
            F, fixed, killed, h4, s = cap_data(c)
            columns.extend(F[:, j].col_join(sp.zeros(K.cols, 1)) for j in range(F.cols))
            columns.extend(column(i, cvalue(i, fixed[:, j]), fixed[:, j])
                           for j in range(fixed.cols))
            h4sum += h4
            if s is not None:
                cusp_s.append(s)
                chi += 2*h4
            for j in range(killed.cols):
                H1after.append(killed[:, j].col_join(sp.zeros(n, 1)))
            peripheral = sp.zeros(4+n, 1)
            peripheral[4+i] = 1
            H1after.append(peripheral)
    relation = sp.Matrix.hstack(*columns)
    g, T = invariants(relation)
    b1E, AE = invariants(sp.Matrix.hstack(*H1cols))
    r, A1 = invariants(sp.Matrix.hstack(*H1after))
    q = h4sum-b1E+r
    assert q >= 0
    b2 = g+q
    b3 = 2+2*b2-2*r-chi
    assert b3 >= 0
    return dict(r=r, A1=A1, g=g, T=T, q=q, b2=b2, b3=b3, chi=chi,
                b1E=b1E, AE=AE, graph_rank=K.cols, cusp_s=cusp_s,
                log_columns=five_count, sites=n)


print('LN INTEGRAL GLUING v001: exact graph kernels, inverse Smith maps, full bar columns.', flush=True)
sample_count = 0
noncyclic = []
for row in ROWS:
    name = f"OS{row['OS']}/{row['profile']}"
    d0 = int(1/sp.Rational(row['height_of_generator']))
    local = [local_raw(sp.Matrix(B), sp.Matrix(g), kind)
             for B, g, kind in zip(row['elliptic_matrices'],
                                   row['generator_section_cocycle'], row['fibers'])]
    L = lcm(*(lcm(*[int(x.q) for x in z]) for z, mult in local))
    multiplicative = [i for i, item in enumerate(local) if item[1] is not None]
    for mode in ('mixed', 'original', 'finite'):
        if mode == 'mixed':
            a, b = L, 2*L
        elif mode == 'original':
            a, b = 1, 3*d0
        else:
            a, b = 2*L, 3*L
        total = a*b//d0
        assert a*b % d0 == 0
        weights = {}
        budget = total
        for j, i in enumerate(multiplicative[:2]):
            value = min(2 if mode == 'mixed' and j == 0 else 1, budget)
            if value:
                weights[i] = value
                budget -= value
        caps = make_local(row, a, b, weights, mode)
        if budget:
            caps.append(regular_zero(budget))
        if mode == 'finite':
            caps.append(regular_log(5, [1, 0, 0, 3]))
        caps.append(regular_log(1, [0, 0, 0, 2 if mode == 'finite' else 0], 'ordinary'))
        ans = run(caps)
        assert ans['r'] == 0 if mode == 'finite' else ans['r'] == 1
        sample_count += 1
        if any(s > 1 for s in ans['cusp_s']):
            noncyclic.append((name, mode, ans['cusp_s']))
        print(name, mode, 'a,b=', (a, b), 'weights=', weights,
              'regular_weight=', budget, '=>', ans, flush=True)
# The exceptional presentation is exercised with all finite-good caps logged
# and all positive weight at a regular place.
row = next(r for r in ROWS if (r['OS'], r['profile']) == (49, 'II'))
caps = make_local(row, 1, 6, {}, 'exception')
for c in caps[:2]:
    A, z = c['A'], c['z']
    c['cap'] = 'log'
    c['m'] = next(h for h in range(1, 7) if A**h == E4)
    c['v'] = integer(sp.Matrix([-z[0], -z[1], 0, 1]))
caps.extend([regular_zero(1), regular_log(1, [0, 0, 0, 0], 'ordinary')])
ans = run(caps)
assert ans['r'] == 0 and ans['A1'] == (9,)
print('OS49/II Klein-four case a=1,b=6, no regular logs =>', ans, flush=True)
sample_count += 1
print('COMPLETE:', sample_count, 'global exact computations.', flush=True)
print('Noncyclic positive cusp cases (literal Smith first factors):', noncyclic, flush=True)
print('These executions check the unbounded formulas; the proof derives their scope for every finite input.', flush=True)
