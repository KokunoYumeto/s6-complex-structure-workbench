#!/usr/bin/env python3
"""Fresh LI calculation from raw profiles and ordered central-group words.

No LI original, historical LI algorithm, LD/LH algorithm or target answer
table is read. The admitted LD JSON is a final comparison of reconstructed
input rows and presentation patterns. All sites are zero-based internally.
"""
from __future__ import annotations

import itertools
import json
import math
from collections import Counter
from functools import reduce
from pathlib import Path

from sympy import Matrix, Rational, ZZ, eye, zeros
from sympy.matrices.normalforms import (
    hermite_normal_form, smith_normal_decomp, smith_normal_form,
)

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT / "agents/continuation7_iii_all_parity"
RAW = ROOT / "agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json"
ADMITTED = ROOT / "agents/continuation7_iii_weighted_catalogue/S6_SERIES_PUBLISH_III_02LD_fresh_exterior_data.json"
PATTERNS = ROOT / "agents/continuation7_iii_weighted_catalogue/S6_SERIES_PUBLISH_III_02LD_fresh_patterns.json"
OUT = LANE / "S6_SERIES_PUBLISH_III_02LI_ordered_words_v02.json"
PAIRS = tuple(itertools.combinations(range(4), 2))
E4 = eye(4)
E6 = eye(6)
J = Matrix([[0, 1], [-1, 0]])
FINITE = {"II": 6, "III": 4, "IV": 3, "III*": 4, "IV*": 3}
COMPONENTS = {"II": 1, "III": 2, "IV": 3, "III*": 8, "IV*": 7,
              "I1*": 6, "I3*": 8}
COUNTS = Counter()
WITNESSES = []


def integral(M):
    assert all(x.q == 1 for x in M), M
    return Matrix(M.rows, M.cols, [int(x) for x in M])


def vec(v):
    return Matrix([int(x) for x in v])


def p(x, y):
    return Matrix([x[i] * y[j] for i, j in PAIRS])


def wedge(x, y):
    return p(x, y) - p(y, x)


def ext(A):
    return Matrix.hstack(*(wedge(A[:, i], A[:, j]) for i, j in PAIRS))


def product(mats, n=4):
    z = eye(n)
    for A in mats:
        z = z * A
    return z


def xgcd(a, b):
    aa, bb = abs(int(a)), abs(int(b))
    u0, u1, v0, v1 = 1, 0, 0, 1
    while bb:
        q, r = divmod(aa, bb)
        aa, bb = bb, r
        u0, u1 = u1, u0 - q * u1
        v0, v1 = v1, v0 - q * v1
    return aa, u0 * (1 if a >= 0 else -1), v0 * (1 if b >= 0 else -1)


def bezout_many(xs):
    coeff = []
    g = 0
    for x in xs:
        g1, u, v = xgcd(g, x)
        coeff = [u * t for t in coeff] + [v]
        g = g1
    assert sum(x * c for x, c in zip(xs, coeff)) == g
    return g, vec(coeff)


def denominator(xs):
    return math.lcm(*(int(x.q) for x in xs))


def smith_split(M):
    D, U, V = smith_normal_decomp(M, domain=ZZ)
    assert U * M * V == D and abs(int(U.det())) == 1 and abs(int(V.det())) == 1
    rank = sum(D[i, i] != 0 for i in range(min(D.shape)))
    Vi = integral(V.inv())
    K, Q, section = V[:, rank:], Vi[:rank, :], V[:, :rank]
    L = Vi[rank:, :]
    assert M * K == zeros(M.rows, K.cols)
    assert Q * section == eye(rank) and L * K == eye(K.cols)
    assert K * L + section * Q == eye(M.cols)
    return K, L, Q, section, D, U, V


def quotient_from_kernel_seed(seed):
    ann = seed.T.nullspace()
    Q0 = Matrix.vstack(*(integral(x.T * denominator(x)) for x in ann))
    K, L, Q, section, _, _, _ = smith_split(Q0)
    assert K.cols == seed.rank()
    assert Q * seed == zeros(Q.rows, seed.cols)
    return K, L, Q, section, Q0


def cokernel(M):
    S = smith_normal_form(M, domain=ZZ)
    diag = [abs(int(S[i, i])) for i in range(min(S.shape)) if S[i, i]]
    return M.rows - len(diag), tuple(x for x in diag if x > 1)


def tate(B, g):
    N = B - eye(2)
    nu = math.gcd(*(int(x) for x in N))
    col = next(N[:, j] for j in range(2) if N[:, j] != zeros(2, 1))
    u = col / math.gcd(*(int(x) for x in col))
    if next(x for x in u if x) < 0:
        u = -u
    u = integral(u)
    assert N == nu * u * u.T * J
    j = next(j for j in range(2) if u[j])
    kappa = Rational(g[j], u[j])
    assert kappa.q == 1 and g == kappa * u
    gg, s, t = xgcd(u[0], u[1])
    assert gg == 1
    r = vec([-t, s])
    assert Matrix.hstack(u, r).det() == 1
    return int(nu), u, r, int(kappa)


def multiplicative(kind):
    return kind.startswith("I") and kind[1:].isdigit()


def component(raw, i):
    c = raw["component_coordinates"][i]
    return (int(c["moduli"][0]), int(c["rows"][0][0])) if c["moduli"] else (1, 0)


def reconstruct_rows(raws):
    result = []
    for raw in raws:
        den = int(1 / Rational(raw["height_of_generator"]))
        for star, kind in enumerate(raw["fibers"]):
            if not multiplicative(kind):
                continue
            nu = int(kind[1:])
            if den % nu:
                continue
            size = den // nu
            for a in range(1, size + 1):
                if size % a or math.gcd(a, size // a) != 1:
                    continue
                b = size // a
                _, k = component(raw, star)
                p0, q0 = a * k % nu, b * k % nu
                if math.gcd(q0, nu) != 1:
                    continue
                if any((int(j == p0) - int(j == 0) - int(j == (p0-q0) % nu)
                        + int(j == (-q0) % nu))
                       != (-2 * int(j == 0) + int(j == 1 % nu) + int(j == (-1) % nu))
                       for j in range(nu)):
                    continue
                if any(a * k0 % q and b * k0 % q
                       for i in range(len(raw["fibers"])) if i != star
                       for q, k0 in [component(raw, i)]):
                    continue
                mats, sites = [], []
                for i, (kind, B0, g0) in enumerate(zip(raw["fibers"], raw["elliptic_matrices"], raw["generator_section_cocycle"])):
                    B, g = Matrix(B0), vec(g0)
                    beta = -a * g.T * J * B
                    if multiplicative(kind):
                        n, u, r, kap = tate(B, g)
                        c = Rational(-a*b*kap*kap + int(i == star), n)
                        z = None
                    else:
                        z = (B - eye(2)).inv() * g
                        c = (beta * (b*z))[0]
                        n = u = r = kap = None
                    A = E4.copy()
                    A[:2, :2], A[:2, 3], A[2, :2], A[2, 3] = B, b*g, beta, c
                    A = integral(A)
                    assert A.det() == 1
                    q, kc = component(raw, i)
                    sites.append(dict(kind=kind, B=B, g=g, z=z, nu=n, u=u, r=r,
                                      kappa=kap, q=q, component=kc, narrow=(a*kc % q == 0)))
                    mats.append(A)
                assert product(mats) == E4
                choices = []
                for i, site in enumerate(sites):
                    if i == star:
                        choices.append(("C",))
                    elif site["kind"] in FINITE:
                        choices.append(("O", "F"))
                    elif "*" in site["kind"]:
                        choices.append(("O",))
                    elif site["narrow"]:
                        choices.append(("M",))
                    else:
                        choices.append(("M", "O"))
                result.append(dict(key=(raw["OS"], raw["profile"], a, b, star+1),
                                   star=star, a=a, b=b, sites=sites, matrices=mats,
                                   patterns=list(itertools.product(*choices))))
    return result


class Lift:
    """Lift made by descending generator words; quadratic f is only a test."""
    def __init__(self, A):
        self.A, self.W = A, ext(A)
        self.Ai, self.Wi = integral(A.inv()), integral(self.W.inv())
        self.cache = {}

    def f(self, x):
        key = tuple(x)
        if key not in self.cache:
            current, centre = zeros(4, 1), zeros(6, 1)
            for j in (3, 2, 1, 0):
                n, v = int(x[j]), self.A[:, j]
                term = n * v
                centre += (n*(n-1)//2) * p(v, v) + p(current, term)
                current += term
            assert current == self.A * x
            self.cache[key] = -centre
        return self.cache[key]

    def formula(self, x):
        out = zeros(6, 1)
        for i in range(4):
            out -= int(x[i]) * (int(x[i])-1)//2 * p(self.A[:, i], self.A[:, i])
            for j in range(i+1, 4):
                defect = p(self.A[:, i], self.A[:, j]) - self.W * p(E4[:, i], E4[:, j])
                out -= x[i] * x[j] * defect
        return out

    def forward(self, x, z):
        return self.A*x, self.W*z-self.f(x)

    def inverse(self, x, z):
        y = self.Ai*x
        return y, self.Wi*(z+self.f(y))


class Graph:
    def __init__(self, mats, a, b, weight):
        self.mats, self.a, self.b, self.weight = mats, a, b, weight
        self.r = len(mats)-1
        assert product(mats) == E4
        self.lifts = [Lift(A) for A in mats[:-1]]
        self.g = math.gcd(a, weight)
        self.alpha, self.beta = a//self.g, weight*b//self.g
        gg, self.bu, self.bv = xgcd(self.alpha, self.beta)
        assert gg == 1
        self.G = Matrix.hstack(*(A-E4 for A in mats[:-1]))
        assert self.G[3, :] == zeros(1, self.G.cols)
        self.K, self.Kinv, _, _, D, _, self.V = smith_split(self.G[:3, :])
        assert [abs(int(D[i, i])) for i in range(3)] == [1, 1, self.g]
        self.R = Matrix.hstack(*(ext(A)-E6 for A in mats))
        standard = Matrix.hstack(E6[:, 1], E6[:, 2], E6[:, 3], E6[:, 4],
                                 weight*b*E6[:, 0]+a*E6[:, 5])
        assert hermite_normal_form(self.R) == hermite_normal_form(standard)
        self.suffix = [product(mats[j+1:-1]) for j in range(self.r)]
        self.hcols = []
        for j in range(self.K.cols):
            k = self.K[:, j]
            z, prefix, alternating = zeros(6, 1), zeros(4, 1), zeros(6, 1)
            for i, lift in enumerate(self.lifts):
                u = k[4*i:4*i+4, :]
                z += lift.f(u) + p(u, -u)
                for v in (lift.A*u, -u):
                    z -= p(prefix, v)
                    alternating += wedge(prefix, v)
                    prefix += v
            assert prefix == zeros(4, 1)
            self.hcols.append(self.q(2*z+alternating))
        self.H = Matrix.hstack(*self.hcols)
        COUNTS["primitive_graph_bases"] += 1

    def q(self, x):
        return vec([self.alpha*x[0]-self.beta*x[5], self.bv*x[0]+self.bu*x[5]])

    def same(self, x, y):
        d = self.q(x-y)
        return d[0] == 0 and int(d[1]) % self.g == 0

    def cq_same(self, x, y):
        d = x-y
        return d[0] == 0 and int(d[1]) % self.g == 0

    def c(self, i, x):
        if i < self.r:
            return self.lifts[i].f(x)
        y, z = x, zeros(6, 1)
        for lift in self.lifts:
            y, z = lift.inverse(y, z)
        assert y == self.mats[-1]*x
        formula = -sum((self.lifts[j].f(self.suffix[j]*self.mats[-1]*x)
                        for j in range(self.r)), zeros(6, 1))
        assert self.same(-z, formula)
        return -z

    def j(self, i, x):
        v = zeros(4*self.r, 1)
        if i < self.r:
            v[4*i:4*i+4, 0] = x
        else:
            for j, suffix in enumerate(self.suffix):
                v[4*j:4*j+4, 0] = -suffix*x
        assert self.G*v == zeros(4, 1)
        k = self.Kinv*v
        assert self.K*k == v
        return k

    def fixed_column(self, i, v):
        k, c = self.j(i, v), self.q(self.c(i, v))
        assert self.cq_same(2*c, self.H*k)
        if self.g % 2:
            half = vec([(self.H*k)[0]//2,
                        int((self.H*k)[1])*pow(2, -1, self.g) if self.g > 1 else 0])
            assert int((self.H*k)[0]) % 2 == 0 and self.cq_same(c, half)
        return c.col_join(k)

    def log_columns(self, i, h, m, v):
        A = self.mats[i]
        assert m % h == 0 and A**h == E4 and A*v == v
        Nh = sum((A**j for j in range(h)), zeros(4))
        N = (m//h)*Nh
        out = []
        for j in range(4):
            x = E4[:, j]
            ff = (m//h)*sum((self.c(i, A**nu*x) for nu in range(h)), zeros(6, 1))
            c = self.q(ff-wedge(x, v))
            k = self.j(i, N*x)
            assert self.cq_same(2*c+2*self.q(wedge(x, v)), self.H*k)
            out.append(c.col_join(k))
        out.append(self.fixed_column(i, v))
        # Every core relation, with torsion retained.
        L = Matrix.hstack(*out)
        for j in range(4):
            d = L[:, :4]*(A-E4)[:, j]
            assert all(x == 0 for x in d[2:, :]) and d[0] == 0 and int(d[1]) % self.g == 0
        d = m*L[:, 4]-L[:, :4]*v
        assert all(x == 0 for x in d[2:, :]) and d[0] == 0 and int(d[1]) % self.g == 0
        COUNTS["five_column_maps"] += 1
        return out

    def check_lifts(self):
        x, y, z = vec([-2, 3, -1, 2]), vec([1, -1, 2, -3]), vec([2, 0, -1, 1, -2, 3])
        for lift in self.lifts:
            for t in [x, y, x+y, *[E4[:, j] for j in range(4)]]:
                assert lift.f(t) == lift.formula(t)
            xa, za = lift.forward(x, z)
            assert lift.inverse(xa, za) == (x, z)
            xi, zi = lift.inverse(x, z)
            assert lift.forward(xi, zi) == (x, z)
            defect = p(lift.A*x, lift.A*y)-lift.W*p(x, y)
            assert lift.f(x)+lift.f(y)-lift.f(x+y) == defect
            COUNTS["ordered_word_lifts"] += 1
        self.c(self.r, x)
        # The exact central inverse, including its diagonal term.
        assert p(x, x)+p(x, -x) == zeros(6, 1)


def fixed_basis(A):
    K, L, _, _, _, _, _ = smith_split(A-E4)
    return K, L


def extra_kernel(site, a, b, weight):
    if multiplicative(site["kind"]):
        nu, kap = site["nu"], site["kappa"]
        gg, x, z = xgcd(a*kap, nu)
        assert gg == 1 and (weight*b*kap) % nu == 0
        beta = vec([x*site["u"][0], x*site["u"][1], z, 0])
        ell = vec([-weight*b*kap*site["r"][0]//nu,
                   -weight*b*kap*site["r"][1]//nu, 0, 1])
        denom = nu
    else:
        zz, denom = site["z"], site["q"]
        rho = integral(denom*Matrix([[a*zz[1], -a*zz[0], 1]]))
        gg, xyz = bezout_many(list(rho))
        assert gg == 1
        beta = xyz.col_join(Matrix([0]))
        ell = integral(Matrix([-weight*b*zz[0], -weight*b*zz[1], 0, 1]))
    k = wedge(beta, ell)
    assert a*k[0]-weight*b*k[5] == -Rational(weight*b, denom)
    return k


def cap_data(site, A1, A, a, b, weight, choice):
    seed1 = ext(A1)-E6
    seedD = ext(A)-E6
    if choice == "O" and not site["narrow"]:
        seed1 = seed1.row_join(extra_kernel(site, a, b, 1))
        seedD = seedD.row_join(extra_kernel(site, a, b, weight))
    K1, L1, Q1, sec1, _ = quotient_from_kernel_seed(seed1)
    S = Matrix.diag(1, 1, 1, weight)
    W = ext(S)
    KD, LD, QD, secD, _, _, _ = smith_split(Q1*W)
    assert QD*seedD == zeros(QD.rows, seedD.cols) and KD.cols == seedD.rank()
    cover = Q1*W*secD
    transfer = integral(QD*(weight*W.inv())*sec1)
    assert cover*transfer == weight*eye(Q1.rows)
    assert transfer*cover == weight*eye(QD.rows)
    assert KD*LD+secD*QD == E6
    F, Finv = fixed_basis(A)
    if not multiplicative(site["kind"]):
        zz = site["z"]
        gD = denominator(weight*b*zz)
        ell = integral(Matrix([-gD*weight*b*zz[0], -gD*weight*b*zz[1], 0, gD]))
        literal = Matrix.hstack(E4[:, 2], ell)
        assert hermite_normal_form(F) == hermite_normal_form(literal)
    COUNTS["cap_cover_transfer_inverse_maps"] += 1
    return KD, F


def finite_data(site, A, b, weight):
    h = FINITE[site["kind"]]
    assert A**h == E4
    zz = site["z"]
    gD = denominator(weight*b*zz)
    ell = integral(Matrix([-gD*weight*b*zz[0], -gD*weight*b*zz[1], 0, gD]))
    F = Matrix.hstack(E4[:, 2], ell)
    N = sum((A**j for j in range(h)), zeros(4))
    fn = integral(Matrix.vstack(N[2, :], N[3, :]/gD))
    assert F*fn == N
    H = hermite_normal_form(fn)
    Q = integral(H.inv()*fn)
    _, _, _, _, SD, SU, SV = smith_split(Q)
    assert abs(int(SD[0, 0])) == abs(int(SD[1, 1])) == 1
    right = integral(SV[:, :2]*Matrix.diag(1/SD[0, 0], 1/SD[1, 1])*SU)
    assert Q*right == eye(2)
    m = h*h
    v = E4[:, 2]+m*ell
    w = integral(h*H.inv()*vec([1, m]))
    t = math.gcd(m, *(int(x) for x in w))
    assert math.gcd(m, *(int(x) for x in v)) == 1 and (m//t) % h == 0
    # Exhaust all nonidentity powers for this honest free action.
    for j in range(1, m):
        projection_integral = all(Rational(j*x, m).q == 1 for x in w)
        if j % h:
            assert not projection_integral
        else:
            assert not all(Rational(j*x, m).q == 1 for x in v)
    COUNTS["finite_projected_lattices_and_all_powers"] += 1
    return h, m, v, gD


def check_shear(graph, i, h, m, v):
    A, lam = graph.mats[i], vec([-1, 2, 1, -2])
    N = (m//h)*sum((A**j for j in range(h)), zeros(4))
    fm = (m//h)*sum((graph.c(i, A**j*lam) for j in range(h)), zeros(6, 1))
    assert graph.same(fm, graph.c(i, N*lam)+wedge(N*lam, lam))
    vp = v+N*lam
    newroot = graph.c(i, vp)+wedge(A*vp, lam)
    oldrootplusnormal = graph.c(i, v)+fm-wedge(lam, v)
    assert graph.same(newroot, oldrootplusnormal)
    for x in [E4[:, j] for j in range(4)]:
        newfm = (m//h)*sum((graph.c(i, A**j*x)+wedge(A**(j+1)*x, lam)
                     for j in range(h)), zeros(6, 1))
        oldfm = (m//h)*sum((graph.c(i, A**j*x) for j in range(h)), zeros(6, 1))
        assert graph.same(newfm-wedge(x, vp), oldfm-wedge(x, v))
    COUNTS["even_safe_peripheral_shear_maps"] += 1


def global_matrix(row, weight, pattern, shift, regular=False):
    a, b, star = row["a"], row["b"], row["star"]
    order = list(range(star+1, len(row["sites"])))+list(range(star+1))
    S = Matrix.diag(1, 1, 1, weight)
    base = [integral(S.inv()*row["matrices"][i]*S) for i in order]
    # Insert the clutch (and optional regular sites) before the selected cusp.
    regspec = [(7, vec([1, 2, 3, 4])), (5, vec([1, -1, 2, 3]))] if regular else []
    mats = base[:-1]+[E4]*(len(regspec)+1)+base[-1:]
    graph = Graph(mats, a, b, weight)
    graph.check_lifts()
    finite = {}
    sum_mu = Rational(0)
    for pos, original in enumerate(order[:-1]):
        if pattern[original] == "F":
            data = finite_data(row["sites"][original], mats[pos], b, weight)
            finite[pos] = data
            sum_mu += Rational(data[2][3], data[1])
    for m, v in regspec:
        sum_mu += Rational(v[3], m)
    # In regular examples an integer clutch makes r=0 automatically.
    e = int(sum_mu) + shift
    r_expected = int(sum_mu == e)
    dim = 2+graph.K.cols
    relations = [vec([0, graph.g]+[0]*graph.K.cols)]
    named = ["fibre_torsion_relation"]
    L = 0
    for pos, original in enumerate(order):
        actual = pos if pos < len(order)-1 else len(mats)-1
        site, choice = row["sites"][original], pattern[original]
        if choice == "F":
            h, m, v, _ = finite[actual]
            columns = graph.log_columns(actual, h, m, v)
            check_shear(graph, actual, h, m, v)
            relations += columns
            named += [f"site{original}:norm{j}" for j in range(4)]+[f"site{original}:root"]
        else:
            KD, F = cap_data(site, row["matrices"][original], mats[actual], a, b, weight, choice)
            for j in range(KD.cols):
                relations.append(graph.q(KD[:, j]).col_join(zeros(graph.K.cols, 1)))
                named.append(f"site{original}:primitive_fibre{j}")
            for j in range(F.cols):
                relations.append(graph.fixed_column(actual, F[:, j]))
                named.append(f"site{original}:fixed_normal{j}")
            L += int(choice == "O" and not site["narrow"])
    offset = len(base)-1
    for j, (m, v) in enumerate(regspec):
        relations += graph.log_columns(offset+j, 1, m, v)
        named += [f"regular{j}:norm{k}" for k in range(4)]+[f"regular{j}:root"]
    cv = -e*E4[:, 3]
    relations += graph.log_columns(offset+len(regspec), 1, 1, cv)
    named += [f"clutch:norm{k}" for k in range(4)]+["clutch:root"]
    B = Matrix.hstack(*relations)
    assert B.rows == dim
    free, torsion = cokernel(B)
    assert free == (r_expected if L == 0 else 0), (row["key"], weight, pattern, e, L, free, r_expected)
    COUNTS["full_global_presentations"] += 1
    COUNTS["shared_even_presentations"] += int(graph.g % 2 == 0)
    if graph.g % 2 == 0 and len(WITNESSES) < 3:
        naive = B.copy()
        for j, name in enumerate(named):
            if ":fixed_normal" in name or name.endswith(":root"):
                naive[:2, j] = zeros(2, 1)
        nf, nt = cokernel(naive)
        if (nf, nt) != (free, torsion):
            D, U, V = smith_normal_decomp(B, domain=ZZ)
            assert U*B*V == D
            WITNESSES.append(dict(key=row["key"], selected_zero_index=star,
                                  weight=weight, choices=pattern, e=e, g=graph.g,
                                  relation_names=named, matrix=[list(map(int, B.row(i))) for i in range(B.rows)],
                                  smith=[int(D[i, i]) for i in range(min(D.shape))],
                                  free=free, torsion=torsion,
                                  deleted_fixed_corrections_free=nf, deleted_fixed_corrections_torsion=nt))
    return free, torsion


def main():
    raw = json.loads(RAW.read_text())
    rows = reconstruct_rows(raw["rows"])
    assert len(rows) == 172
    admitted = {tuple(r["key"]): r for r in json.loads(ADMITTED.read_text())["rows"]}
    assert set(admitted) == {r["key"] for r in rows}
    patterns = set()
    narrow = set()
    counts = Counter()
    for row in rows:
        assert [A.tolist() for A in row["matrices"]] == admitted[row["key"]]["monodromies"]
        counts[row["key"][:2]+("rows",)] += 1
        for pattern in row["patterns"]:
            key = (row["key"], pattern)
            patterns.add(key)
            counts[row["key"][:2]+("broad",)] += 1
            projected = tuple("O" if p0 == "F" and "*" in s["kind"] else p0
                              for s, p0 in zip(row["sites"], pattern))
            assert projected in row["patterns"]
            if projected == pattern:
                narrow.add(key)
                counts[row["key"][:2]+("stars_original",)] += 1
    saved = json.loads(PATTERNS.read_text())["patterns"]
    assert patterns == {(tuple(x["key"]), tuple(x["choices"])) for x in saved}
    assert len(patterns) == 495 and len(narrow) == 459 and len(patterns-narrow) == 36
    print("RAW RECONSTRUCTION: 21 profiles, 172 rows, 495 broad patterns, 459 all-star-original, 36 extra.", flush=True)
    print("Selected-site comparison is zero-based internal -> one-based admitted key, with exact matrices.", flush=True)
    completed_profiles = set()
    for number, row in enumerate(rows):
        weights = sorted({1, 2, 4, row["a"], 2*row["a"]})
        for weight in weights:
            for pattern in row["patterns"]:
                for shift in (0, 1):
                    global_matrix(row, weight, pattern, shift)
        # Arbitrary-regular-site formula is proved algebraically; these two
        # simultaneous new identity blocks check the full implemented map.
        global_matrix(row, 2*row["a"], row["patterns"][0], 1, regular=True)
        profile = row["key"][:2]
        if number+1 == len(rows) or rows[number+1]["key"][:2] != profile:
            completed_profiles.add(profile)
            print("PROFILE", profile, "rows", counts[profile+("rows",)],
                  "broad", counts[profile+("broad",)], "stars-original", counts[profile+("stars_original",)],
                  "cumulative matrices", COUNTS["full_global_presentations"], flush=True)
    assert len(completed_profiles) == 21
    report = dict(scope="New ordered-generator lifts and complete cap matrices; finite checks support the written unbounded proof.",
                  counts=dict(COUNTS), profiles=[dict(OS=o, profile=p0,
                      rows=counts[(o,p0,"rows")], broad=counts[(o,p0,"broad")],
                      stars_original=counts[(o,p0,"stars_original")])
                      for o,p0 in sorted(completed_profiles)], even_witnesses=WITNESSES)
    OUT.write_text(json.dumps(report, indent=2)+"\n")
    print("ALL COUNTS", json.dumps(dict(COUNTS), sort_keys=True), flush=True)
    print("EVEN WITNESSES", len(WITNESSES), flush=True)
    print("PASS: ordered words/formulas, exact last inverse, graph sections, saturated cap maps, cover/transfer inverses,")
    print("      all-power finite freeness, five full Thom columns, even-safe shear and complete global Smith matrices.")
    print("OUTPUT", OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
