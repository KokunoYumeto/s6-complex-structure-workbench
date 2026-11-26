#!/usr/bin/env python3
"""Fresh LE raw-fixture calculation, version 001.

No target original, historical target algorithm/table/output, or earlier
target answer is an input. Every run of this source has separate stdout
and stderr artifacts. This source version is never overwritten after run.
"""
from pathlib import Path
from itertools import combinations, product
from fractions import Fraction
from functools import reduce
from collections import Counter
from math import gcd, prod
from datetime import datetime, timezone
import hashlib
import json
import csv
import sympy as S

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT / "agents/continuation7_iii_mixed_torsion"
RAW = ROOT / "agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json"
RAW_SHA = "6bda97b01ba63c0a796e3141609ca12e163791b626024b79104817ec5defc522"
assert hashlib.sha256(RAW.read_bytes()).hexdigest() == RAW_SHA
raw_profiles = json.loads(RAW.read_text())["rows"]
J = S.Matrix([[0, 1], [-1, 0]])
I2, I4 = S.eye(2), S.eye(4)
DELTA, GAMMA = I4[:, 2], I4[:, 3]
PAIRS = list(combinations(range(4), 2))
ORDERS = {"II": 6, "III": 4, "IV": 3, "III*": 4, "IV*": 3}
INDICES = {"II": 1, "III": 2, "IV": 3, "III*": 2, "IV*": 3}


def zi(x):
    x = S.Rational(x)
    assert x.q == 1, x
    return int(x)


def ml(M):
    return [[zi(x) for x in row] for row in M.tolist()]


def vl(v):
    return [zi(x) for x in v]


def bezout(a, b):
    old_r, r, old_x, x, old_y, y = a, b, 1, 0, 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r-q*r
        old_x, x = x, old_x-q*x
        old_y, y = y, old_y-q*y
    if old_r < 0:
        old_r, old_x, old_y = -old_r, -old_x, -old_y
    assert old_x*a+old_y*b == old_r
    return old_r, old_x, old_y


def row_section(row):
    g, out = 0, []
    for value in row:
        h, x, y = bezout(g, zi(value))
        out = [x*t for t in out]+[y]
        g = h
    assert g == 1
    answer = S.Matrix(out)
    assert (row*answer)[0] == 1
    return answer


def integer_section(M):
    """Exact integer section, via Euclidean row/column operations.

    The final section, not an unrecorded Smith claim, is the certificate.
    It is checked by M R=I and retained in the mathematical data/output.
    """
    A, U, V = M.copy(), S.eye(M.rows), S.eye(M.cols)
    r, n = A.shape
    def swap_rows(i, j):
        A.row_swap(i, j)
        U.row_swap(i, j)
    def swap_cols(i, j):
        A.col_swap(i, j)
        V.col_swap(i, j)
    def row_add(i, j, q):
        A[i, :] = A[i, :]+q*A[j, :]
        U[i, :] = U[i, :]+q*U[j, :]
    def col_add(i, j, q):
        A[:, i] = A[:, i]+q*A[:, j]
        V[:, i] = V[:, i]+q*V[:, j]
    for k in range(r):
        pivot = next((i, j) for i in range(k, r) for j in range(k, n)
                     if A[i, j])
        swap_rows(k, pivot[0])
        swap_cols(k, pivot[1])
        while True:
            changed = False
            for i in range(k+1, r):
                if A[i, k]:
                    q = zi(A[i, k]//A[k, k])
                    row_add(i, k, -q)
                    if A[i, k]:
                        swap_rows(i, k)
                    changed = True
                    break
            if changed:
                continue
            for j in range(k+1, n):
                if A[k, j]:
                    q = zi(A[k, j]//A[k, k])
                    col_add(j, k, -q)
                    if A[k, j]:
                        swap_cols(j, k)
                    changed = True
                    break
            if changed:
                continue
            bad = next(((i, j) for i in range(k+1, r)
                        for j in range(k+1, n) if A[i, j] % A[k, k]), None)
            if bad is None:
                break
            row_add(k, bad[0], 1)
        if A[k, k] < 0:
            A[k, :], U[k, :] = -A[k, :], -U[k, :]
    assert U*M*V == A
    assert A == S.eye(r).row_join(S.zeros(r, n-r)), ml(A)
    R = V[:, :r]*U
    assert M*R == S.eye(r)
    ml(R)
    return R


def mult(kind):
    return kind.startswith("I") and kind[1:].isdigit()


def star(kind):
    return kind.startswith("I") and kind.endswith("*") and kind[1:-1].isdigit()


def local_data(A, g):
    B = A-I2
    nu = reduce(gcd, (abs(zi(x)) for x in B), 0)
    column = next(B[:, j] for j in range(2) if B[:, j] != S.zeros(2, 1))
    content = reduce(gcd, (abs(zi(x)) for x in column), 0)
    u = column/content
    if next(x for x in u if x) < 0:
        u = -u
    assert B == nu*u*(u.T*J)
    k = next(j for j in range(2) if u[j])
    kappa = zi(g[k]/u[k])
    assert g == kappa*u
    one, x, y = bezout(zi(u[0]), zi(u[1]))
    assert one == 1
    companion = S.Matrix([-y, x])
    assert S.det(S.Matrix.hstack(u, companion)) == 1
    return nu, u, companion, kappa


def narrow(profile, j, coefficient):
    c = profile["component_coordinates"][j]
    return all((coefficient*row[0]) % modulus == 0
               for row, modulus in zip(c["rows"], c["moduli"]))


def component_eq(nu, kappa, a, b):
    difference = [0]*nu
    for j, sign in [(a*kappa, 1), (0, -1), ((a-b)*kappa, -1), (-b*kappa, 1),
                    (0, 2), (1, -1), (-1, -1)]:
        difference[j % nu] += sign
    return not any(difference)


profiles, natural = [], []
profile_counts = []
for profile_index, raw in enumerate(raw_profiles):
    As = [S.Matrix(M) for M in raw["elliptic_matrices"]]
    gs = [S.Matrix(g) for g in raw["generator_section_cocycle"]]
    locals_ = [local_data(A, g) if mult(kind) else None
               for A, g, kind in zip(As, gs, raw["fibers"])]
    height = Fraction(raw["height_of_generator"])
    assert height.numerator == 1
    profile = dict(raw=raw, index=profile_index, As=As, gs=gs,
                   locals=locals_, height_den=height.denominator)
    profiles.append(profile)
    count = 0
    for zero, local in enumerate(locals_):
        if local is None:
            continue
        nu, u, companion, kappa = local
        d = height.denominator
        if d % nu:
            continue
        total = d//nu
        for a in range(1, total+1):
            if total % a:
                continue
            b = total//a
            if gcd(a, b) != 1 or gcd(b*kappa, nu) != 1:
                continue
            if not component_eq(nu, kappa, a, b):
                continue
            if any(not(narrow(raw, j, a) or narrow(raw, j, b))
                   for j in range(len(As)) if j != zero):
                continue
            natural.append(dict(profile=profile, zero=zero, a=a, b=b))
            count += 1
    profile_counts.append((raw["OS"], raw["profile"], count))


patterns = []
for datum in natural:
    profile, a, b = datum["profile"], datum["a"], datum["b"]
    raw = profile["raw"]
    if any(star(kind) for kind in raw["fibers"]):
        continue
    choices_by_site = []
    for j, kind in enumerate(raw["fibers"]):
        if mult(kind):
            continue
        choices = []
        if kind in ("II", "III", "IV") and narrow(raw, j, a) and gcd(b, INDICES[kind]) == 1:
            choices.append(dict(site=j, kind=kind, choice="O", q=1, order=1))
        z = (profile["As"][j]-I2).inv()*profile["gs"][j]
        if all(S.Rational(b*x).q == 1 for x in z):
            choices.append(dict(site=j, kind=kind, choice="F", q=INDICES[kind], order=ORDERS[kind]))
        choices_by_site.append(choices)
    for choice in product(*choices_by_site):
        finite = [x for x in choice if x["choice"] == "F"]
        if any(gcd(x["order"], y["order"]) != 1 for x, y in combinations(finite, 2)):
            continue
        q = prod(x["q"] for x in finite)
        if b % q == 0 and b//q in (10, 14):
            patterns.append((datum, choice, b//q, q))
patterns.sort(key=lambda x: (x[2], x[0]["profile"]["index"], x[0]["a"],
                            x[0]["zero"], tuple(z["choice"] for z in x[1])))


def period_matrix(datum, site):
    profile, a, b = datum["profile"], datum["a"], datum["b"]
    A, g = profile["As"][site], profile["gs"][site]
    local = profile["locals"][site]
    if local is None:
        z = (A-I2).inv()*g
    else:
        nu, u, companion, kappa = local
        z = S.Rational(kappa, nu)*companion
    beta = -a*g.T*J*A
    weight = S.Rational(1, local[0]) if site == datum["zero"] else 0
    T = I4.copy()
    T[:2, :2], T[:2, 3] = A, b*g
    T[2, :2], T[2, 3] = beta, (beta*(b*z))[0]+weight
    ml(T)
    return T


def exterior_square(T):
    return S.Matrix([[T[i, k]*T[j, l]-T[i, l]*T[j, k]
                      for k, l in PAIRS] for i, j in PAIRS])


def qref(v):
    return zi(v[0]*v[1]+v[0]+v[1]) % 2


answers = []
print("LE fresh version 001 start UTC", datetime.now(timezone.utc).isoformat(), flush=True)
print("RAW", str(RAW.relative_to(ROOT)), RAW_SHA, flush=True)
print("ALL_RAW_PROFILE_NATURAL_COUNTS", profile_counts, flush=True)
print("TOTAL_NATURAL", len(natural), "TOTAL_MIXED_PATTERNS", len(patterns), flush=True)
assert len(natural) == 172
assert len(patterns) == 12
for number, (datum, choices, c, q) in enumerate(patterns, 1):
    profile, zero, a, b = datum["profile"], datum["zero"], datum["a"], datum["b"]
    raw = profile["raw"]
    prime = c//2
    assert prime in (5, 7) and a % 2 == 1 and b % 4 == 2
    finite = [z for z in choices if z["choice"] == "F"]
    assert len(finite) <= 1
    O = S.zeros(4)
    O[:2, :2] = a*J
    O[2, 3], O[3, 2] = -b, b
    omega = S.Matrix([[a, 0, 0, 0, 0, -b]])
    Ts = [period_matrix(datum, j) for j in range(len(raw["fibers"]))]
    total = I4
    for T in Ts:
        total = total*T
        assert T.T*O*T == O and T*DELTA == DELTA
        assert all(qref(T*S.Matrix(v)) == qref(S.Matrix(v)) for v in product(range(2), repeat=4))
    assert total == I4
    nu, u, companion, kappa = profile["locals"][zero]
    S0 = S.Matrix.hstack(S.Matrix([*u, 0, 0]), DELTA)
    L0 = S.Matrix.hstack(S.Matrix([*companion, 0, 0]), GAMMA)
    C = S.Matrix([[nu, b*kappa], [-a*kappa, S.Rational(1-a*b*kappa*kappa, nu)]])
    assert C.det() == 1
    ml(C)
    H = S.Matrix.hstack(S0*C[:, 0], L0[:, 0], S0*C[:, 1], L0[:, 1])
    assert H.det() == 1 and H.inv()*Ts[zero]*H == I4+I4[:, 0]*I4[1, :]+I4[:, 2]*I4[3, :]
    K = (S0*C).T*O*L0
    dvec = C.inv()*S.Matrix([0, 1])
    assert K == K.T and K*dvec == S.Matrix([0, -b])
    assert dvec == S.Matrix([-b*kappa, nu]) and gcd(nu, c) == 1
    eps = S.Matrix([qref(S0*C[:, j]) for j in range(2)])
    assert eps == S.Matrix([1, 0])
    mplus = S.Matrix([(K[0, 0]-1)/2, K[1, 1]/2])
    mminus = S.Matrix([(2*K[0, 1]-K[0, 0]-1)/2, K[1, 1]/2])
    ml(mplus); ml(mminus)
    phase = zi((eps.T*dvec)[0]/2)
    chars = [zi(phase+(m.T*dvec)[0]) for m in (mplus, mminus)]
    cchar = zi(S.Rational(b, 2)*(a*kappa*(b*kappa-nu)-1))
    assert chars[0] == cchar and all(z % c == cchar % c for z in chars)
    cdeg = zi(K[0, 0]-K[0, 1])
    assert cdeg == a*(nu-b*kappa) and cdeg % 2 == 1
    assert cchar % 2 == (1+kappa) % 2 and cchar % prime == 0
    kills = [S0[:, 0], DELTA]
    kill_preimages = [(zero, L0*C.inv()[:, j]) for j in range(2)]
    nodes, fixed = [], {2: [], prime: []}
    for site, local in enumerate(profile["locals"]):
        if local is None or site == zero:
            continue
        vn, vu, vr, vk = local
        d0 = gcd(vn, a*vk)
        n, A = vn//d0, a*vk//d0
        one, t, sigma = bezout(n, A)
        assert one == 1
        B = zi(S.Rational(b*vk, n))
        one, x, y = bezout(d0, B)
        assert one == 1
        CS = S.Matrix([[n, sigma], [-A, t]])
        CL = S.Matrix([[x, -B], [y, d0]])
        NS = S.Matrix.hstack(S.Matrix([*vu, 0, 0]), DELTA)*CS
        NL = S.Matrix.hstack(S.Matrix([*vr, 0, 0]), GAMMA)*CL
        NH = S.Matrix.hstack(NS[:, 0], NL[:, 0], NS[:, 1], NL[:, 1])
        assert CS.det() == CL.det() == NH.det() == 1
        assert NH.inv()*Ts[site]*NH == I4+I4[:, 0]*I4[1, :]
        NK = NS.T*O*NL
        assert NK[0, 1] == 0 and NK[0, 0] == S.Rational(a*vn, d0*d0)
        assert NK[1, 1] == -S.Rational(b*d0*d0, vn)
        l = NS[:, 0]
        f = S.Matrix([[*(d0*vu.T*J), 0, S.Rational(b*vk*d0, vn)]])
        assert Ts[site]-I4 == l*f
        fh = row_section(f)
        assert (Ts[site]-I4)*fh == l
        kills.append(l)
        kill_preimages.append((site, fh))
        node = dict(site=site, kind=raw["fibers"][site], nu=vn, kappa=vk, d0=d0,
                    primitive_n=n, CS=ml(CS), CS_inverse=ml(CS.inv()),
                    CL=ml(CL), CL_inverse=ml(CL.inv()), H=ml(NH), H_inverse=ml(NH.inv()),
                    K=ml(NK), vanishing=vl(l), row=ml(f), row_section=vl(fh),
                    delta_short=vl(CS.inv()*S.Matrix([0, 1])))
        for ell in (2, prime):
            if n % ell == 0:
                assert vn == ell and d0 == 1
                fixed[ell].append(site)
                assert (sigma*a*vk) % ell == 1
                node[str(ell)+"_weights"] = [(-sigma) % ell, sigma % ell]
                node[str(ell)+"_degree"] = zi(NK[1, 1])
                node[str(ell)+"_doubled_character"] = -sigma*zi(NK[0, 0])
                assert node[str(ell)+"_doubled_character"] % ell == 0
                if ell == 2:
                    node["half_character"] = (1-a) % 2
                    assert node["half_character"] == 0 and zi(NK[1, 1]) % 2 == 1
                else:
                    w = pow((-a*vk) % prime, -1, prime)
                    assert w == (-sigma) % prime
                    node["Tate_r"] = -vk
                    node["Tate_w"] = w
                    assert (w*w*a-nu*(b//prime)) % prime == 0
        nodes.append(node)
    assert len(fixed[2]) == len(fixed[prime]) == 1
    KM = S.Matrix.hstack(*kills)[:3, :]
    KR = integer_section(KM)
    assert KM*KR == S.eye(3)
    for k, (site, preimage) in zip(kills, kill_preimages):
        assert (Ts[site]-I4)*preimage == k
    one, alpha, minus_beta = bezout(a, b)
    assert one == 1
    s0 = S.Matrix([alpha, 0, 0, 0, 0, -minus_beta])
    assert (omega*s0)[0] == 1
    P = S.Matrix.hstack(s0, S.Matrix([b, 0, 0, 0, 0, a]), *[S.eye(6)[:, j] for j in range(1, 5)])
    assert abs(P.det()) == 1
    wedge = S.Matrix.hstack(*[exterior_square(T)-S.eye(6) for T in Ts])
    assert omega*wedge == S.zeros(1, wedge.cols)
    lower = (P.inv()*wedge)[1:, :]
    WR = integer_section(lower)
    chain = WR*P.inv()[1:, :]
    assert wedge*chain == S.eye(6)-s0*omega
    cube2 = (1+kappa) % 2
    Pp = ((b//prime-a*nu)*pow(2, -1, prime)) % prime
    odd_node = next(z for z in nodes if z["site"] == fixed[prime][0])
    w = odd_node["Tate_w"]
    assert Pp == ((b//prime)*pow(2, -1, prime)*(1-nu*nu*pow(w*w, -1, prime))) % prime
    Pfull = next(z for z in range(c) if z % 2 == cube2 and z % prime == Pp)
    mufull = prime*cube2
    model2 = prime
    modelp = (Pfull-cube2*prime) % c if Pp else (1-prime) % c
    assert modelp % 2 == 0 and modelp % prime == (Pp if Pp else 1)
    inv_odd = pow(Pp, -1, prime) if Pp else 1
    for x in range(2):
        for y in range(prime):
            out = (x*model2+y*modelp) % c
            assert (out % 2, (out*inv_odd) % prime) == (x, y)
    assert (cube2*model2+(1 if Pp else 0)*modelp) % c == Pfull
    assert (cube2*pow(model2, 3, c)) % c == mufull
    finite_data = []
    for option in finite:
        site = option["site"]
        zQ = (profile["As"][site]-I2).inv()*(b*profile["gs"][site])
        ell = S.Matrix([-zQ[0], -zQ[1], 0, 1])
        assert Ts[site]*ell == ell
        finite_data.append(dict(**option, ell=vl(ell), zQ=vl(zQ),
                                first_fibre_coefficient=b//option["q"],
                                sample_m=option["order"], sample_e=1,
                                sample_n=option["order"]-1, sample_r0=0))
    answer = dict(number=number, OS=raw["OS"], profile=raw["profile"], a=a, b=b,
                  zero=zero, fibers=raw["fibers"], choices=choices, c=c, p=prime,
                  nu=nu, kappa=kappa, Q_f=b//prime, raw_As=[ml(z) for z in profile["As"]],
                  raw_gs=[vl(z) for z in profile["gs"]], Ts=[ml(z) for z in Ts],
                  T_inverses=[ml(z.inv()) for z in Ts], omega=ml(omega), s0=vl(s0),
                  fibre_basis=ml(P), fibre_basis_inverse=ml(P.inv()),
                  fibre_chain_inverse=ml(chain), C=ml(C), C_inverse=ml(C.inv()),
                  H=ml(H), H_inverse=ml(H.inv()), K=ml(K), delta_short=vl(dvec),
                  epsilon=vl(eps), cusp_slopes=[vl(mplus), vl(mminus)],
                  cusp_dense_phase=phase, cusp_characters=chars, cusp_degree=cdeg,
                  nodes=nodes, angular_columns=ml(KM), angular_section=ml(KR),
                  angular_preimages=[dict(site=j, vector=vl(v)) for j, v in kill_preimages],
                  fixed_sites={str(k): v for k, v in fixed.items()}, finite=finite_data,
                  cube2=cube2, cube_p=0, mu=mufull, P_p=Pp, P_full=Pfull,
                  odd_epsilon=int(Pp != 0), model_map=[model2, modelp],
                  model_inverse=dict(mod2=1, modp=inv_odd), all_parameter_scope=True)
    answers.append(answer)
    print("PATTERN", number, raw["OS"], raw["profile"], (a, b), "zero", zero,
          "choices", list(choices), "c", c, "nu,kappa", (nu, kappa), flush=True)
    for key in ("raw_As", "raw_gs", "Ts", "T_inverses", "C", "C_inverse", "H", "H_inverse",
                "K", "delta_short", "epsilon", "cusp_slopes", "cusp_dense_phase",
                "cusp_characters", "cusp_degree", "angular_columns", "angular_section",
                "angular_preimages", "omega", "s0", "fibre_basis", "fibre_basis_inverse",
                "fibre_chain_inverse", "nodes", "finite"):
        print(key, json.dumps(answer[key], separators=(",", ":")), flush=True)
    print("INVARIANTS", {k: answer[k] for k in ("cube2", "cube_p", "mu", "P_p", "P_full",
                                                "odd_epsilon", "model_map", "model_inverse")}, flush=True)

row_keys = {(z["OS"], z["profile"], z["a"], z["b"], z["zero"]) for z in answers}
assert len(row_keys) == 10
type_counts = Counter((z["c"], z["cube2"], z["odd_epsilon"]) for z in answers)
pair_maps = []
for source in answers:
    for target in answers:
        if (source["c"], source["cube2"], source["odd_epsilon"]) != (target["c"], target["cube2"], target["odd_epsilon"]):
            continue
        c, p = source["c"], source["p"]
        tmodp = target["P_p"]*pow(source["P_p"], -1, p) % p if source["P_p"] else 1
        t = next(x for x in range(c) if x % 2 == 1 and x % p == tmodp)
        inverse = pow(t, -1, c)
        assert t*source["P_full"] % c == target["P_full"]
        assert pow(t, 3, c)*source["mu"] % c == target["mu"]
        assert t*inverse % c == 1
        pair_maps.append(dict(source=source["number"], target=target["number"], t=t, inverse=inverse))
print("ALL_TYPE_COUNTS", sorted(type_counts.items()), flush=True)
print("ALL_MARKED_PAIR_MAPS", pair_maps, flush=True)
print("PATTERNS", len(answers), "ROWS", len(row_keys), "TYPES", len(type_counts), flush=True)
print("FRESH_COMPLETE_UTC", datetime.now(timezone.utc).isoformat(), flush=True)
LANE.mkdir(parents=True, exist_ok=True)
data = dict(scope="Fresh LE raw-only exact calculation", raw_sha256=RAW_SHA,
            profile_counts=profile_counts, natural_count=len(natural), patterns=answers,
            type_counts=[dict(c=k[0], cube2=k[1], odd_epsilon=k[2], count=v)
                         for k, v in sorted(type_counts.items())], pair_maps=pair_maps)
(LANE / "S6_SERIES_PUBLISH_III_02LE_fresh_data_v001.json").write_text(json.dumps(data, indent=2)+"\n")
with (LANE / "S6_SERIES_PUBLISH_III_02LE_fresh_patterns_v001.tsv").open("w", newline="") as f:
    fields = ["number", "OS", "profile", "a", "b", "zero", "c", "p", "nu", "kappa",
              "cube2", "P_p", "P_full", "mu", "odd_epsilon"]
    writer = csv.DictWriter(f, fields, delimiter="\t", extrasaction="ignore")
    writer.writeheader()
    writer.writerows(answers)
print("PASS: all exact maps, inverses, prescribed-fan values, full CRT coordinates and marked model maps", flush=True)
