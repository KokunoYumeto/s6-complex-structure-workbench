#!/usr/bin/env python3
"""Fresh LJ arithmetic from raw profiles and proved local formulae.

This source reads only the defining raw elliptic profiles.  It does not read
the LJ original, a historical target algorithm, or a target-derived table.
The accompanying proof supplies the geometry and the primary operations;
this calculation retains exact integer maps and checks their full identities.
"""
from pathlib import Path
from fractions import Fraction
from math import gcd, prod
from itertools import combinations, product
from functools import reduce
from datetime import datetime, timezone
import csv
import hashlib
import json
import sympy as S

W = Path(__file__).resolve().parents[1]
OUT = W / "agents/continuation7_iii_mixed_three"
RAW = W / "agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json"
NAME = "S6_SERIES_PUBLISH_III_02LJ"
J = S.Matrix([[0, 1], [-1, 0]])
E2, E4 = S.eye(2), S.eye(4)
PAIRS = list(combinations(range(4), 2))
DELTA, GAMMA = E4[:, 2], E4[:, 3]
FINITE = {"II": (6, 1), "III": (4, 2), "IV": (3, 3),
          "III*": (4, 2), "IV*": (3, 3)}


def integral(M):
    assert all(S.denom(x) == 1 for x in M), M
    return [[int(M[i, j]) for j in range(M.cols)] for i in range(M.rows)]


def sparse(M):
    integral(M)
    return {"shape": [M.rows, M.cols],
            "entries": [[i, j, int(M[i, j])] for i in range(M.rows)
                        for j in range(M.cols) if M[i, j]]}


def emit(label, value):
    print(label + "=" + json.dumps(value, separators=(",", ":"), sort_keys=True))


def bezout(a, b):
    oldr, r, oldx, x, oldy, y = a, b, 1, 0, 0, 1
    while r:
        q = oldr // r
        oldr, r = r, oldr-q*r
        oldx, x = x, oldx-q*x
        oldy, y = y, oldy-q*y
    sign = 1 if oldr >= 0 else -1
    return sign*oldr, sign*oldx, sign*oldy


def diagonalize(A):
    """Integral Smith reduction with literal left and right transformations."""
    M, U, V = S.Matrix(A), S.eye(A.rows), S.eye(A.cols)
    for k in range(min(A.shape)):
        candidates = [(abs(M[i, j]), i, j)
                      for i in range(k, M.rows) for j in range(k, M.cols)
                      if M[i, j]]
        if not candidates:
            break
        _, i, j = min(candidates)
        M.row_swap(k, i); U.row_swap(k, i)
        M.col_swap(k, j); V.col_swap(k, j)
        while True:
            for i in range(k+1, M.rows):
                if M[i, k]:
                    q = M[i, k] // M[k, k]
                    M[i, :] -= q*M[k, :]; U[i, :] -= q*U[k, :]
                    if M[i, k]:
                        M.row_swap(k, i); U.row_swap(k, i)
                    break
            else:
                for j in range(k+1, M.cols):
                    if M[k, j]:
                        q = M[k, j] // M[k, k]
                        M[:, j] -= q*M[:, k]; V[:, j] -= q*V[:, k]
                        if M[k, j]:
                            M.col_swap(k, j); V.col_swap(k, j)
                        break
                else:
                    bad = next(((i, j) for i in range(k+1, M.rows)
                                for j in range(k+1, M.cols)
                                if M[i, j] % M[k, k]), None)
                    if bad is None:
                        break
                    M[k, :] += M[bad[0], :]; U[k, :] += U[bad[0], :]
        if M[k, k] < 0:
            M[k, :] = -M[k, :]; U[k, :] = -U[k, :]
    assert U*A*V == M
    assert abs(U.det()) == abs(V.det()) == 1
    integral(U.inv()); integral(V.inv())
    assert all(not M[i, j] for i in range(M.rows)
               for j in range(M.cols) if i != j)
    ds = [int(M[i, i]) for i in range(min(M.shape)) if M[i, i]]
    assert all(t % s == 0 for s, t in zip(ds, ds[1:]))
    return M, U, V, ds


def solve_integer(A, B):
    D, U, V, ds = diagonalize(A)
    C = U*B
    Z = S.zeros(A.cols, B.cols)
    for i in range(A.rows):
        d = D[i, i] if i < A.cols else 0
        if d:
            for j in range(B.cols):
                assert C[i, j] % d == 0
                Z[i, j] = C[i, j] // d
        else:
            assert C[i, :] == S.zeros(1, B.cols)
    X = V*Z
    assert A*X == B
    return X, ds


def exterior(A):
    return S.Matrix([[A[i, k]*A[j, l]-A[i, l]*A[j, k]
                      for k, l in PAIRS] for i, j in PAIRS])


def lift(u):
    return S.Matrix([u[0], u[1], 0, 0])


def multiplicative(t):
    return t[0] == "I" and t[1:].isdigit()


def local_marking(A, g):
    N = A-E2
    nu = reduce(gcd, (abs(int(x)) for x in N), 0)
    col = next(N[:, j] for j in range(2) if N[:, j] != S.zeros(2, 1))
    u = col/reduce(gcd, (abs(int(x)) for x in col), 0)
    if next(x for x in u if x) < 0:
        u = -u
    assert N == nu*u*(u.T*J)
    one, x, y = bezout(int(u[0]), int(u[1]))
    assert one == 1
    v = S.Matrix([-y, x])
    assert S.det(u.row_join(v)) == 1
    kap = next(g[i]/u[i] for i in range(2) if u[i])
    assert S.denom(kap) == 1 and g == kap*u
    return nu, u, v, int(kap)


def narrow(component, n):
    return all(n*int(row[0]) % int(q) == 0
               for q, row in zip(component["moduli"], component["rows"]))


def catalogue(raw):
    natural, counts, answers = [], [], []
    for profile in raw["rows"]:
        before = len(natural)
        d = Fraction(profile["height_of_generator"])
        assert d.numerator == 1
        d = d.denominator
        for z, typ in enumerate(profile["fibers"]):
            if not multiplicative(typ):
                continue
            A = S.Matrix(profile["elliptic_matrices"][z])
            g = S.Matrix(profile["generator_section_cocycle"][z])
            nu, u, v, kap = local_marking(A, g)
            if d % nu:
                continue
            for a in range(1, d//nu+1):
                if (d//nu) % a:
                    continue
                b = d//nu//a
                if gcd(a, b) != 1 or gcd(b*kap, nu) != 1:
                    continue
                lhs, rhs = [0]*nu, [0]*nu
                for m, j in [(1, a*kap), (-1, 0),
                             (-1, (a-b)*kap), (1, -b*kap)]:
                    lhs[j % nu] += m
                for m, j in [(-2, 0), (1, 1), (1, -1)]:
                    rhs[j % nu] += m
                if lhs != rhs:
                    continue
                if any(i != z and not narrow(comp, a) and not narrow(comp, b)
                       for i, comp in enumerate(profile["component_coordinates"])):
                    continue
                natural.append((profile, a, b, z))
        counts.append([profile["OS"], profile["profile"], len(natural)-before])
    for profile, a, b, z in natural:
        if any(t.startswith("I") and t.endswith("*") and t[1:-1].isdigit()
               for t in profile["fibers"]):
            continue
        indices, choices = [], []
        for i, typ in enumerate(profile["fibers"]):
            if multiplicative(typ):
                continue
            order, qi = FINITE[typ]
            A = S.Matrix(profile["elliptic_matrices"][i])
            g = S.Matrix(profile["generator_section_cocycle"][i])
            zq = b*(A-E2).inv()*g
            opts = []
            if all(S.denom(x) == 1 for x in zq):
                opts.append(("F", order, qi))
            if typ in {"II", "III", "IV"} and narrow(profile["component_coordinates"][i], a) and gcd(b, qi) == 1:
                opts.append(("O", 1, 1))
            indices.append(i); choices.append(opts)
        for opts in product(*choices):
            orders = [d for k, d, q in opts if k == "F"]
            if any(gcd(d, e) != 1 for d, e in combinations(orders, 2)):
                continue
            qi = prod(q for k, d, q in opts)
            if b % qi == 0 and b//qi in {6, 15, 30}:
                answers.append({"raw": profile, "a": a, "b": b, "zero": z,
                                "options": dict(zip(indices, opts)), "c": b//qi})
    answers.sort(key=lambda r: (r["c"], r["raw"]["OS"], r["raw"]["profile"],
                               r["a"], r["b"], r["zero"], str(r["options"])))
    return counts, natural, answers


def analyse(row, number):
    raw, a, b, z0, c = (row[k] for k in ("raw", "a", "b", "zero", "c"))
    name = str(raw["OS"])+("/"+raw["profile"] if raw["profile"] != "default" else "")
    print(f"\nPATTERN {number}: {name} a={a} b={b} zero={z0} c={c} options={row['options']}")
    emit("raw", {"fibers": raw["fibers"], "A": raw["elliptic_matrices"],
                 "g": raw["generator_section_cocycle"], "height": raw["height_of_generator"]})
    omega = S.Matrix([[a, 0, 0, 0, 0, -b]])
    Om = S.zeros(4); Om[0, 1] = a; Om[1, 0] = -a; Om[2, 3] = -b; Om[3, 2] = b
    Ts, fixes, angular, locals_ = [], [], [], []
    fixed_sites = {p: [] for p in (2, 3, 5) if c % p == 0}
    for i, typ in enumerate(raw["fibers"]):
        A, g = S.Matrix(raw["elliptic_matrices"][i]), S.Matrix(raw["generator_section_cocycle"][i])
        beta = -a*g.T*J*A
        if multiplicative(typ):
            nu, u, v, kap = local_marking(A, g)
            zi = S.Rational(kap, nu)*v
        else:
            zi = (A-E2).inv()*g
        ct = (beta*(b*zi))[0]+(S.Rational(1, nu) if i == z0 else 0)
        T = S.eye(4); T[:2, :2] = A; T[:2, 3] = b*g
        T[2, :2] = beta; T[2, 3] = ct
        Ti = T.inv()
        integral(T); integral(Ti)
        assert T*Ti == E4 == Ti*T and T.T*Om*T == Om
        assert T*DELTA == DELTA and T[3, :] == GAMMA.T
        loc = {"site": i, "type": typ, "T": integral(T), "T_inverse": integral(Ti)}
        emit("site", loc)
        Ts.append(T)
        if i == z0:
            rho = S.Rational(1-a*b*kap*kap, nu)
            C = S.Matrix([[nu, b*kap], [-a*kap, rho]])
            Ci = S.Matrix([[rho, -b*kap], [a*kap, nu]])
            Sp = lift(u).row_join(DELTA); Lp = lift(v).row_join(GAMMA)
            H = S.Matrix.hstack(Sp*C[:, 0], Lp[:, 0], Sp*C[:, 1], Lp[:, 1])
            assert C*Ci == E2 == Ci*C and H.det() == 1
            assert (T-E4)*Lp == Sp*C
            K = C.T*S.diag(a, -b)
            assert K == K.T and K*Ci*S.Matrix([0, 1]) == S.Matrix([0, -b])
            k, degree = b*kap, a*(nu-b*kap)
            charD = b*(a*kap*(b*kap-nu)-1)
            charU = charD//2 if b % 2 == 0 else None
            q3 = (degree**3*k*k*pow(nu*(k-nu), -1, 9)) % 9
            assert k % 3 == 0 and nu % 3 and q3 == 0
            if c % 2 == 0:
                assert a % 2 == nu % 2 == 1
                assert charD % 2 == 0 and charU % 2 == (1+kap) % 2
                assert degree % 2 == 1
            F = S.Matrix([[1, 0, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0],
                          [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]])*exterior(H.inv())
            section, ds = solve_integer(F, S.eye(4)); assert ds == [1]*4
            loc.update({"nu": nu, "kappa": kap, "u": integral(u), "v": integral(v),
                        "C": integral(C), "C_inverse": integral(Ci), "H": integral(H),
                        "H_inverse": integral(H.inv()), "K": integral(K),
                        "scalar_short": [-k, nu], "weights": [[k-nu, nu, -k], [-nu, nu-k, k]],
                        "degree": degree, "doubled_character": charD,
                        "undoubled_character": charU, "Q3_C": q3,
                        "f2": integral(F), "f2_section": integral(section)})
            cusp = loc
            fixes.append(DELTA.row_join(lift(u))); angular += [lift(u), DELTA]
        elif multiplicative(typ):
            d0 = gcd(nu, a*kap); n0 = nu//d0; aa = a*kap//d0
            bb = S.Rational(b*kap, n0); assert S.denom(bb) == 1; bb = int(bb)
            one, theta, sig = bezout(n0, aa); assert one == 1
            one, x, y = bezout(d0, bb); assert one == 1
            CS = S.Matrix([[n0, sig], [-aa, theta]])
            CL = S.Matrix([[x, -bb], [y, d0]])
            SS = lift(u).row_join(DELTA)*CS; LL = lift(v).row_join(GAMMA)*CL
            H = S.Matrix.hstack(SS[:, 0], LL[:, 0], SS[:, 1], LL[:, 1])
            assert H.det() == 1 and (T-E4)*H == H*S.Matrix([[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
            KN = SS.T*Om*LL
            assert KN[0, 0] == S.Rational(a*nu, d0*d0) and KN[0, 1] == 0
            assert KN[1, 1] == S.Rational(-b*d0*d0, nu)
            assert DELTA == -sig*SS[:, 0]+n0*SS[:, 1]
            F = S.Matrix([[1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0],
                          [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]])*exterior(H.inv())
            section, ds = solve_integer(F, S.eye(4)); assert ds == [1]*4
            characters = {}
            for p in fixed_sites:
                if n0 % p == 0:
                    fixed_sites[p].append(i)
                    assert nu == p and n0 == p and d0 == 1
                    assert (a*kap*sig) % p == 1
                    assert KN[1, 1] == -b//p
                    if p == 2:
                        assert (int(KN[0, 0])*(2*0+1)-1) % 2 == 1
                    characters[p] = {"normal": [-sig % p, sig % p],
                                     "degree": int(KN[1, 1]), "doubled_character": 0,
                                     "scalar_content": n0}
            loc.update({"nu": nu, "kappa": kap, "u": integral(u), "v": integral(v),
                        "d0": d0, "n0": n0, "sigma": sig, "CS": integral(CS),
                        "CS_inverse": integral(CS.inv()), "CL": integral(CL),
                        "CL_inverse": integral(CL.inv()), "H": integral(H),
                        "H_inverse": integral(H.inv()), "K": integral(KN),
                        "fixed_data": characters, "f2": integral(F), "f2_section": integral(section)})
            fixes.append(S.Matrix.hstack(DELTA, lift(u), LL[:, 1]))
            angular.append(SS[:, 0])
        else:
            option, order, qi = row["options"][i]
            if option == "F":
                ell = S.Matrix([-b*zi[0], -b*zi[1], 0, 1]); integral(ell)
                beta0 = DELTA if typ == "II" else S.Matrix([0, -1, (1-a)//2, 0])
                assert typ in {"II", "III"}
                M = S.Matrix.hstack(T-E4, beta0, ell)
                R, ds = solve_integer(M, E4); assert ds == [1]*4
                Y, _ = solve_integer(T-E4, DELTA-qi*beta0)
                Nd = sum((T**j for j in range(order)), S.zeros(4))
                assert Nd*beta0 == S.Rational(order, qi)*DELTA and Nd*ell == order*ell
                assert -(beta0.T*Om*ell)[0] == S.Rational(b, qi)
                loc.update({"option": option, "order": order, "q": qi,
                            "ell": integral(ell), "beta0": integral(beta0),
                            "coinvariant_section": integral(R), "vertical_boundary": integral(Y),
                            "coinvariant_inverse": integral(R[4:6, :])})
            else:
                qi = FINITE[typ][1]
                h = a*zi; integral(h)
                lam = -h.T*J
                SP = S.eye(4); SP[2, :2] = lam
                assert lam*(A-E2)+beta == S.zeros(1, 2)
                ell = S.Matrix([-qi*b*zi[0], -qi*b*zi[1], 0, qi]); integral(ell)
                F0 = S.Matrix([[qi, 0, qi*b*zi[1], 0, -qi*b*zi[0], 0],
                               [0, 0, 0, 0, 0, 1]])
                F = F0*exterior(SP)
                sec, ds = solve_integer(F, S.eye(2)); assert ds == [1, 1]
                loc.update({"option": option, "q": qi, "ell": integral(ell),
                            "line_map": integral(SP), "line_inverse": integral(SP.inv()),
                            "f2": integral(F), "f2_section": integral(sec)})
            assert T*ell == ell
            fixes.append(DELTA.row_join(ell))
        if "f2" in loc:
            F = S.Matrix(loc["f2"])
            assert F*(exterior(T)-S.eye(6)) == S.zeros(F.rows, 6)
        emit("local_maps", {k: v for k, v in loc.items() if k not in {"T", "T_inverse"}})
        locals_.append(loc)
    assert reduce(lambda X, Y: X*Y, Ts, E4) == E4
    assert all(len(sites) == 1 for sites in fixed_sites.values())
    _, x, y = bezout(a, b)
    s0 = S.Matrix([x, 0, 0, 0, 0, -y])
    B2 = S.Matrix.hstack(*(exterior(T)-S.eye(6) for T in Ts))
    R2, ds = solve_integer(B2, S.eye(6)-s0*omega)
    assert ds == [1]*5 and omega*B2 == S.zeros(1, B2.cols) and (omega*s0)[0] == 1
    K1 = S.Matrix.hstack(*angular)[:3, :]
    R1, ds = solve_integer(K1, S.eye(3)); assert ds == [1]*3
    D = S.Matrix.hstack(*(T-E4 for T in Ts))
    DD, UD, VD, ds = diagonalize(D); assert ds == [1]*3
    V0, Q0 = VD[:, 3:], VD.inv()[3:, :]
    f_all = fixes+[S.Matrix.hstack(DELTA, E4[:, 0], E4[:, 1], GAMMA)]
    blocks, relation, offset = [], [], 0
    for i, F in enumerate(f_all):
        JJ = S.zeros(D.cols, 4)
        if i < len(Ts):
            JJ[4*i:4*i+4, :] = E4
        else:
            for j in range(len(Ts)):
                JJ[4*j:4*j+4, :] = -reduce(lambda X, Y: X*Y, Ts[j+1:], E4)
        assert D*JJ*F == S.zeros(4, F.cols)
        blocks.append(JJ*F); relation += [offset]; offset += F.cols
    B = S.Matrix.hstack(*blocks)
    RG, ds = solve_integer(B, V0)
    RG = RG*Q0
    assert B*RG == V0*Q0 and D*V0 == S.zeros(4, V0.cols) and Q0*V0 == S.eye(V0.cols)
    kd = S.zeros(B.cols, 1)
    for j in relation:
        kd[j] = 1
    assert B*kd == S.zeros(B.rows, 1) and B.cols-B.rank() == 1 and all(d == 1 for d in ds)
    global_maps = {"s0": integral(s0), "wedge_section": sparse(R2), "angular_section": sparse(R1),
                   "graph_kernel_basis": sparse(V0), "graph_kernel_inverse": sparse(Q0),
                   "graph_section": sparse(RG), "graph_relation": integral(kd)}
    emit("global_maps", global_maps)
    nu, kap = cusp["nu"], cusp["kappa"]
    t = (1+kap) % 2 if c % 2 == 0 else 0
    P3 = ((b//3-a*nu)*pow(2, -1, 3)) % 3
    P5 = ((b//5-a*nu)*pow(2, -1, 5)) % 5 if c % 5 == 0 else 0
    assert P3 == 0
    P = next(j for j in range(c) if j % 3 == P3 and
             (c % 2 != 0 or j % 2 == t) and (c % 5 != 0 or j % 5 == P5))
    D3 = 3*c
    mu = next(j for j in range(D3) if j % 9 == 0 and
              (c % 2 != 0 or j % 2 == t) and (c % 5 != 0 or j % 5 == 0))
    primes = [p for p in (2, 3, 5) if c % p == 0]
    model_map = {p: c//p for p in primes}
    model_inverse = {p: pow(c//p, -1, p) for p in primes}
    for j in range(c):
        assert sum(model_map[p]*(model_inverse[p]*j % p) for p in primes) % c == j
    modelP = (model_map.get(2, 0)*t+model_map.get(5, 0)*(1 if P5 else 0)) % c
    assert modelP == P
    modelmu = (model_map.get(2, 0)**3*t) % D3
    assert modelmu == mu
    detector_orders = {p: (9 if p == 3 else p) for p in primes}
    detector_sections = {p: ((c//p)*pow(c//p, -1, p))**3 % D3 for p in primes}
    for p in primes:
        assert all(detector_sections[p] % detector_orders[q] == (1 if p == q else 0) for q in primes)
    for j in range(D3):
        assert sum(detector_sections[p]*(j % detector_orders[p]) for p in primes) % D3 == j
    result = {"number": number, "OS": raw["OS"], "profile": raw["profile"],
              "a": a, "b": b, "zero": z0, "options": {i: v[0] for i, v in row["options"].items()},
              "c": c, "nu": nu, "kappa": kap, "t": t, "P3": P3, "P5": P5, "P": P,
              "D3": D3, "mu": mu, "fixed_sites": fixed_sites, "locals": locals_,
              "global_maps": global_maps, "model_map": model_map, "model_inverse": model_inverse,
              "detector_sections": detector_sections}
    emit("RESULT", {k: v for k, v in result.items() if k not in {"locals", "global_maps"}})
    return result


def symbolic_checks():
    m, e, r, b, q = S.symbols("m e r b q", nonzero=True, integer=True)
    for eps in (-1, 1):
        n = m*e-eps; aa, bb = eps*e, -eps
        C1 = S.Matrix([b*n/q, m/q, 0])
        C2 = S.Matrix([-b*r, 0, m]); C3 = S.Matrix([0, r, n])
        K0 = aa*C2+bb*C3
        assert S.simplify(aa*m+bb*n) == 1
        assert S.simplify(C2-m*K0+bb*q*r*C1) == S.zeros(3, 1)
        assert S.simplify(C3-n*K0-aa*q*r*C1) == S.zeros(3, 1)
        assert S.simplify(K0[0]-b*e*K0[1]) == 0
        assert S.simplify(C1[0]-b*e*C1[1]) == -eps*b/q
    aa, bb, kk, nn, x, y = S.symbols("a b kappa nu x y")
    rho = (1-aa*bb*kk**2)/nn
    C = S.Matrix([[nn, bb*kk], [-aa*kk, rho]])
    K = C.T*S.diag(aa, -bb)
    X, Y = C*S.Matrix([x, y])
    physical = -aa*rho*X**2+2*aa*bb*kk*X*Y+bb*nn*Y**2+aa*X
    assert S.expand(physical+(S.Matrix([[x, y]])*K*S.Matrix([x, y]))[0]-aa*X) == 0
    print("SYMBOLIC_PASS: both signs, all m/e/r/q Thom-generator inverses and physical-support pullback.")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    raw_bytes = RAW.read_bytes(); raw = json.loads(raw_bytes)
    print("START", datetime.now(timezone.utc).isoformat())
    print("RAW_SHA256", hashlib.sha256(raw_bytes).hexdigest())
    counts, natural, rows = catalogue(raw)
    emit("NATURAL_COUNTS", counts)
    assert len(natural) == 172 and len(rows) == 14
    emit("TARGET_COUNTS", {c: sum(r["c"] == c for r in rows) for c in (6, 15, 30)})
    assert [sum(r["c"] == c for r in rows) for c in (6, 15, 30)] == [5, 7, 2]
    results = [analyse(row, i+1) for i, row in enumerate(rows)]
    symbolic_checks()
    summary = {}
    for c in (6, 15, 30):
        counter = {}
        for r in results:
            if r["c"] == c:
                key = f't={r["t"]},epsilon5={int(bool(r["P5"]))}'
                counter[key] = counter.get(key, 0)+1
        summary[c] = counter
    emit("SMOOTH_TYPE_COUNTS", summary)
    data = {"scope": "fresh LJ raw-profile arithmetic and exact displayed maps",
            "raw_sha256": hashlib.sha256(raw_bytes).hexdigest(),
            "natural_counts": counts, "patterns": results, "smooth_type_counts": summary}
    path = OUT/(NAME+"_fresh_data_v001.json")
    path.write_text(json.dumps(data, indent=2)+"\n")
    tab = OUT/(NAME+"_fresh_patterns_v001.tsv")
    fields = ["number", "OS", "profile", "a", "b", "zero", "options", "c", "nu", "kappa", "t", "P3", "P5", "P", "D3", "mu"]
    with tab.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in results:
            writer.writerow({key: row[key] for key in fields})
    for file in (path, tab):
        print("SAVED", str(file.relative_to(W)), hashlib.sha256(file.read_bytes()).hexdigest())
    print("COMPLETE", datetime.now(timezone.utc).isoformat())
    print("PASS all fourteen patterns; all exact inverses; full coefficient and model maps.")


if __name__ == "__main__":
    main()
