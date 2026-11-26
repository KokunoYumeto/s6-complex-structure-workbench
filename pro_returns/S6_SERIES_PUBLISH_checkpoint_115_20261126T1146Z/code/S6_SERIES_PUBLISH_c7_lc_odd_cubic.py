#!/usr/bin/env python3
"""Fresh LC calculation from raw defining profiles and exact lattice maps.

No LC original, historical table, historical target algorithm, or held
calculation is read.  The only data input is the authorized raw fixture.
"""
from pathlib import Path
from fractions import Fraction
from itertools import product, combinations
from math import gcd, prod
from functools import reduce
from collections import Counter
import hashlib
import json
import csv
import sympy as S

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT / "agents/continuation7_iii_odd_cubic"
RAW = ROOT / "agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json"
RAW_SHA = "6bda97b01ba63c0a796e3141609ca12e163791b626024b79104817ec5defc522"
assert hashlib.sha256(RAW.read_bytes()).hexdigest() == RAW_SHA
profiles = json.loads(RAW.read_text())["rows"]
J = S.Matrix([[0, 1], [-1, 0]])
I2, I4 = S.eye(2), S.eye(4)
delta, gamma = I4[:, 2], I4[:, 3]


def egcd(a, b):
    rr, r, xx, x, yy, y = a, b, 1, 0, 0, 1
    while r:
        q = rr // r
        rr, r, xx, x, yy, y = r, rr-q*r, x, xx-q*x, y, yy-q*y
    if rr < 0:
        rr, xx, yy = -rr, -xx, -yy
    assert xx*a + yy*b == rr
    return rr, xx, yy


def integer(x):
    z = S.Rational(x)
    assert z.q == 1
    return int(z)


def matrix_list(M):
    return [[integer(z) for z in row] for row in M.tolist()]


def vector_list(v):
    return [integer(z) for z in v]


def is_mult(name):
    return name.startswith("I") and name[1:].isdigit()


def transvection(A, g):
    B = A-I2
    nu = reduce(gcd, (abs(integer(x)) for x in B), 0)
    assert nu > 0
    v = next(B[:, i] for i in range(2) if B[:, i] != S.zeros(2, 1))
    content = reduce(gcd, (abs(integer(x)) for x in v), 0)
    u = v/content
    if next(x for x in u if x) < 0:
        u = -u
    assert B == nu*u*(u.T*J)
    j = next(i for i in range(2) if u[i])
    kappa = integer(g[j]/u[j])
    assert g == kappa*u
    h, x, y = egcd(integer(u[0]), integer(u[1]))
    assert h == 1
    r = S.Matrix([-y, x])
    assert S.det(S.Matrix.hstack(u, r)) == 1
    return dict(nu=nu, u=u, r=r, kappa=kappa)


def is_narrow(profile, site, coefficient):
    c = profile["component_coordinates"][site]
    return all((coefficient*row[0]) % modulus == 0
               for row, modulus in zip(c["rows"], c["moduli"]))


def component_equation(nu, kappa, a, b):
    lhs, rhs = [0]*nu, [0]*nu
    for j, v in ((a*kappa, 1), (0, -1), ((a-b)*kappa, -1), (-b*kappa, 1)):
        lhs[j % nu] += v
    for j, v in ((0, -2), (1, 1), (-1, 1)):
        rhs[j % nu] += v
    return lhs == rhs


natural = []
natural_counts = []
for profile in profiles:
    height = Fraction(profile["height_of_generator"])
    assert height.numerator == 1
    d = height.denominator
    As = [S.Matrix(v) for v in profile["elliptic_matrices"]]
    gs = [S.Matrix(v) for v in profile["generator_section_cocycle"]]
    loc = [transvection(A, g) if is_mult(kind) else None
           for A, g, kind in zip(As, gs, profile["fibers"])]
    count = 0
    for zero, cusp in enumerate(loc):
        if cusp is None or d % cusp["nu"]:
            continue
        ab = d//cusp["nu"]
        # Enumerate b first; a is its exact complementary divisor.
        for b in range(1, ab+1):
            if ab % b:
                continue
            a = ab//b
            if gcd(a, b) != 1 or gcd(b*cusp["kappa"], cusp["nu"]) != 1:
                continue
            if not component_equation(cusp["nu"], cusp["kappa"], a, b):
                continue
            if any(not(is_narrow(profile, j, a) or is_narrow(profile, j, b))
                   for j in range(len(As)) if j != zero):
                continue
            natural.append(dict(profile=profile, As=As, gs=gs, loc=loc,
                                zero=zero, a=a, b=b, d=d))
            count += 1
    natural_counts.append((profile["OS"], profile["profile"], count))
assert len(natural) == 172

order = {"II": 6, "III": 4, "IV": 3, "III*": 4, "IV*": 3}
vertical = {"II": 1, "III": 2, "IV": 3, "III*": 2, "IV*": 3}
patterns = []
for datum in natural:
    profile, a, b = datum["profile"], datum["a"], datum["b"]
    if any(k.startswith("I") and k.endswith("*") and k[1:-1].isdigit()
           for k in profile["fibers"]):
        continue
    options = []
    for j, kind in enumerate(profile["fibers"]):
        if is_mult(kind):
            continue
        opt = []
        if (kind in ("II", "III", "IV") and is_narrow(profile, j, a)
                and gcd(b, vertical[kind]) == 1):
            opt.append(dict(site=j, kind=kind, filling="O", q=1, order=1))
        z = (datum["As"][j]-I2).inv()*datum["gs"][j]
        if all((b*x).q == 1 for x in z):
            opt.append(dict(site=j, kind=kind, filling="F",
                            q=vertical[kind], order=order[kind]))
        options.append(opt)
    for choices in product(*options):
        finite = [o for o in choices if o["filling"] == "F"]
        if any(gcd(x["order"], y["order"]) != 1 for x, y in combinations(finite, 2)):
            continue
        q = prod(o["q"] for o in finite)
        if b % q or b//q not in (5, 7):
            continue
        assert len(finite) <= 1
        patterns.append((datum, choices, b//q, q))
assert len(patterns) == 36
assert len({(d["profile"]["OS"], d["profile"]["profile"], d["a"], d["b"], d["zero"])
            for d, _, _, _ in patterns}) == 30


def alternating(a, b):
    O = S.zeros(4)
    O[:2, :2] = a*J
    O[2, 3], O[3, 2] = -b, b
    return O


def lifted_T(datum, site):
    a, b = datum["a"], datum["b"]
    A, g = datum["As"][site], datum["gs"][site]
    local = datum["loc"][site]
    if local is None:
        z = (A-I2).inv()*g
    else:
        z = S.Rational(local["kappa"], local["nu"])*local["r"]
    beta = -a*g.T*J*A
    omega = S.Rational(1, local["nu"]) if site == datum["zero"] else 0
    T = I4.copy()
    T[:2, :2], T[:2, 3] = A, b*g
    T[2, :2], T[2, 3] = beta, (beta*(b*z))[0]+omega
    matrix_list(T)
    return T


def integral_right_inverse(M):
    g, terms = 0, []
    for columns in combinations(range(M.cols), M.rows):
        block = M[:, list(columns)]
        determinant = integer(block.det())
        if determinant == 0:
            continue
        h, x, y = egcd(g, determinant)
        terms = [(old_columns, old_block, x*c) for old_columns, old_block, c in terms]
        terms.append((columns, block, y))
        g = h
        if g == 1:
            break
    assert g == 1
    inverse = S.zeros(M.cols, M.rows)
    for columns, block, c in terms:
        for i, column in enumerate(columns):
            inverse[column, :] += c*block.adjugate()[i, :]
    assert M*inverse == S.eye(M.rows)
    return inverse


answers = []
for number, (datum, choices, p, q) in enumerate(patterns, 1):
    profile, a, b, zero = datum["profile"], datum["a"], datum["b"], datum["zero"]
    O = alternating(a, b)
    Ts = [lifted_T(datum, i) for i in range(len(profile["fibers"]))]
    total = I4
    for T in Ts:
        total = total*T
        assert T.T*O*T == O and T*delta == delta
    assert total == I4
    cusp = datum["loc"][zero]
    nu, u, r, kappa = (cusp[x] for x in ("nu", "u", "r", "kappa"))
    short = S.Matrix.hstack(S.Matrix([*u, 0, 0]), delta)
    long = S.Matrix.hstack(S.Matrix([*r, 0, 0]), gamma)
    C = S.Matrix([[nu, b*kappa], [-a*kappa, S.Rational(1-a*b*kappa*kappa, nu)]])
    assert C.det() == 1
    matrix_list(C)
    H = S.Matrix.hstack(short*C[:, 0], long[:, 0], short*C[:, 1], long[:, 1])
    assert H.det() == 1
    assert H.inv()*Ts[zero]*H == I4+I4[:, 0]*I4[1, :]+I4[:, 2]*I4[3, :]
    K = (short*C).T*O*long
    assert K == K.T
    dvec = C.inv()*S.Matrix([0, 1])
    assert dvec == S.Matrix([-b*kappa, nu])
    assert K*dvec == S.Matrix([0, -b])
    assert dvec[0] % p == 0 and gcd(integer(dvec[1]), p) == 1
    # The level-two line has psi(v)=v^t K v.
    slopes = (S.Matrix([K[0, 0], K[1, 1]]),
              S.Matrix([2*K[0, 1]-K[0, 0], K[1, 1]]))
    cusp_characters = [integer((m.T*dvec)[0]) for m in slopes]
    assert all(c % p == 0 for c in cusp_characters)
    cusp_degree = integer(K[0, 0]-K[0, 1])
    assert cusp_degree == a*(nu-b*kappa)
    nodes = []
    fixed = []
    kills = [short[:, 0][:3, :], delta[:3, :]]
    for i, local in enumerate(datum["loc"]):
        if local is None or i == zero:
            continue
        vnu, vu, vr, vk = (local[x] for x in ("nu", "u", "r", "kappa"))
        d0 = gcd(vnu, a*vk)
        n, A = vnu//d0, a*vk//d0
        h, t, s = egcd(n, A)
        assert h == 1 and n*t+A*s == 1
        B = integer(S.Rational(b*vk, n))
        h, x, y = egcd(d0, B)
        assert h == 1
        CS = S.Matrix([[n, s], [-A, t]])
        CL = S.Matrix([[x, -B], [y, d0]])
        assert CS.det() == CL.det() == 1
        S0 = S.Matrix.hstack(S.Matrix([*vu, 0, 0]), delta)
        L0 = S.Matrix.hstack(S.Matrix([*vr, 0, 0]), gamma)
        SN, LN = S0*CS, L0*CL
        HN = S.Matrix.hstack(SN[:, 0], LN[:, 0], SN[:, 1], LN[:, 1])
        assert HN.det() == 1
        assert HN.inv()*Ts[i]*HN == I4+I4[:, 0]*I4[1, :]
        KN = SN.T*O*LN
        assert KN[0, 1] == 0
        assert KN[0, 0] == S.Rational(a*vnu, d0*d0)
        assert KN[1, 1] == -S.Rational(b*d0*d0, vnu)
        assert CS.inv()*S.Matrix([0, 1]) == S.Matrix([-s, n])
        l = SN[:, 0]
        kills.append(l[:3, :])
        is_fixed = n % p == 0
        node = dict(site=i, kind=profile["fibers"][i], nu=vnu, kappa=vk,
                    vanishing=vector_list(l), CS=matrix_list(CS), CL=matrix_list(CL),
                    H=matrix_list(HN), H_inverse=matrix_list(HN.inv()),
                    K=matrix_list(KN), delta_short=[-s, n], fixed=is_fixed)
        nodes.append(node)
        if is_fixed:
            assert vnu == p and d0 == 1 and gcd(s, p) == 1
            assert KN[0, 0] == a*p and KN[1, 1] == -b//p
            node["normal_weights"] = [(-s) % p, s % p]
            node["line_character"] = -s*integer(KN[0, 0])
            assert node["line_character"] % p == 0
            node["degree_xi"] = integer(KN[1, 1])
            node["tate_hG_order"] = -vk
            node["tate_R_order"] = -a*b*vk*vk//p
            node["w"] = pow((-a*vk) % p, -1, p)
            assert node["w"] == (-s) % p
            fixed.append(node)
    assert len(fixed) == 1
    elliptic = fixed[0]
    Edegree = elliptic["degree_xi"]
    P1 = (-2*(Edegree+cusp_degree)) % p
    refined = (pow(4, -1, p)*P1) % p
    assert refined == ((q-a*nu)*pow(2, -1, p)) % p
    # The height identity reduces at the unique I_p to this exact congruence.
    assert (datum["d"]//p)*elliptic["kappa"]**2 % p == 1
    w = elliptic["w"]
    local_formula = q*pow(2, -1, p)*(1-nu*nu*pow(w*w, -1, p)) % p
    assert refined == local_formula
    assert (refined == 0) == ((w*w-nu*nu) % p == 0)
    generator_changes = []
    for name, coefficient in [
        ("fibre", 1),
        ("elliptic_curve", -q),
        ("tate_weight", -q*pow(w*w, -1, p)),
        ("cusp_relative_weight", -q*nu*nu*pow(w*w, -1, p)),
    ]:
        coefficient %= p
        inverse = pow(coefficient, -1, p)
        for j in range(p):
            assert ((j*coefficient)*inverse) % p == j
            assert ((j*inverse)*coefficient) % p == j
        generator_changes.append(dict(name=name, generator=coefficient,
                                      inverse_evaluation=inverse,
                                      refined=(refined*inverse) % p,
                                      mu=0))
    assert generator_changes[1]["refined"] == ((nu*nu*pow(w*w, -1, p)-1)*pow(2, -1, p)) % p
    assert generator_changes[2]["refined"] == ((nu*nu-w*w)*pow(2, -1, p)) % p
    normalized_w = w*pow(nu, -1, p) % p
    assert generator_changes[3]["refined"] == ((1-normalized_w**2)*pow(2, -1, p)) % p
    for lam in range(1, p):
        # K(lam,2)_* z3 = lam^3 z3 is the exact K8 detector map.
        for j in range(p):
            assert ((j*pow(lam, 3, p))*pow(pow(lam, 3, p), -1, p)) % p == j
    kill = S.Matrix.hstack(*kills)
    kill_inverse = integral_right_inverse(kill)
    answer = dict(number=number, OS=profile["OS"], profile=profile["profile"],
                  a=a, b=b, zero=zero, selected_nu=nu, selected_kappa=kappa,
                  p=p, q=q, choices=list(choices), fibre_form=matrix_list(O),
                  all_forward_T=[matrix_list(T) for T in Ts],
                  C=matrix_list(C), C_inverse=matrix_list(C.inv()),
                  cusp_H=matrix_list(H), cusp_H_inverse=matrix_list(H.inv()),
                  cusp_K=matrix_list(K), delta_Jordan=vector_list(dvec),
                  cusp_slopes=[vector_list(m) for m in slopes],
                  cusp_line_characters=cusp_characters,
                  cusp_normal_weights=[(-nu) % p, nu % p],
                  cusp_degree_xi=cusp_degree, rank_one=nodes,
                  elliptic=elliptic, kill=matrix_list(kill),
                  kill_right_inverse=matrix_list(kill_inverse),
                  cubic=0, p1_coefficient=P1, refined_coefficient=refined,
                  generator_changes=generator_changes,
                  acting_generator_change=pow(nu, -1, p),
                  acting_generator_change_inverse=nu % p,
                  normalized_w=normalized_w,
                  claimed_zero=(w*w % p == 1),
                  actual_zero=(refined == 0))
    answers.append(answer)

# Symbolic local characteristic identity, including unequal normal degrees.
h, z, x1, x2, weight = S.symbols("h z x1 x2 weight")
Euler = (weight*z+x1*h)*(-weight*z+x2*h)
P1normal = (weight*z+x1*h)**2+(-weight*z+x2*h)**2
assert S.rem(S.expand(P1normal+2*Euler), h*h, h) == 0

# The two exact Gaussian gauges, with all unit entries retained symbolically.
U1, U2, W1, W2, N, M, R, Z11, Z12, Z22 = S.symbols("U1 U2 W1 W2 N M R Z11 Z12 Z22")
U, W = S.Matrix([U1, U2]), S.Matrix([W1, W2])
KN = S.Matrix([[N, 0], [M, R]])
Omega = S.Matrix([[Z11, (R*Z12-M*Z22)/N], [Z12, Z22]])
assert KN.T*Omega == (KN.T*Omega).T
F = (U.T*KN*W)[0]+(W.T*KN.T*Omega*W)[0]
for j in range(2):
    ej = S.eye(2)[:, j]
    short_change = S.expand(F.xreplace({U1: U1+ej[0], U2: U2+ej[1]})-F)
    assert S.simplify(short_change-(ej.T*KN*W)[0]) == 0
    long_change = S.expand(F.xreplace({W1: W1+ej[0], W2: W2+ej[1]})-F)
    expected = (ej.T*KN.T*U)[0]+2*(ej.T*KN.T*Omega*W)[0]+(ej.T*KN.T*Omega*ej)[0]
    assert S.simplify(long_change-expected) == 0
E11 = S.Matrix([[1, 0], [0, 0]])
assert S.simplify((W.T*KN.T*E11*W)[0]-(W.T*E11*KN*W)[0]) == 0
k11, k12, k22, b11, b12, b22 = S.symbols("k11 k12 k22 b11 b12 b22")
KC = S.Matrix([[k11, k12], [k12, k22]])
BS = S.Matrix([[b11, b12], [b12, b22]])
OC = KC.inv()*BS
assert (KC*OC-BS).applyfunc(S.simplify) == S.zeros(2)
FC = (U.T*KC*W)[0]+(W.T*BS*W)[0]
for j in range(2):
    ej = S.eye(2)[:, j]
    change = S.expand(FC.xreplace({W1: W1+ej[0], W2: W2+ej[1]})-FC)
    expected = (ej.T*KC*U)[0]+2*(ej.T*BS*W)[0]+(ej.T*BS*ej)[0]
    assert S.simplify(change-expected) == 0
assert S.expand((W.T*KC*W)[0]-(W.T*KC.T*W)[0]) == 0
v1, v2, h1, h2 = S.symbols("v1 v2 h1 h2")
v, hh = S.Matrix([v1, v2]), S.Matrix([h1, h2])
assert S.expand(((v+hh).T*KC*(v+hh))[0]-(v.T*KC*v)[0]
                -2*(hh.T*KC*v)[0]-(hh.T*KC*hh)[0]) == 0

# Full finite clutching kernel: n=me-sign and b=pq.
mm, ee, nn, rr, aa, eta, pp, qq, sign = S.symbols("m e n r aa eta p q sign", integer=True)
assert S.expand(pp*(mm*ee-sign)-mm*pp*ee) == -pp*sign
# D=-be*s and aa*m+eta*n=1 gives t(ell)=br(aa+eta*e)s.
finite_sweep = (pp*qq)*rr*(aa+eta*ee)
assert S.rem(S.Poly(finite_sweep, pp).as_expr(), pp, pp) == 0

classification_maps = []
for left in answers:
    for right in answers:
        if left["p"] != right["p"] or left["actual_zero"] != right["actual_zero"]:
            continue
        p = left["p"]
        scalar = (1 if left["actual_zero"] else
                  right["refined_coefficient"]*pow(left["refined_coefficient"], -1, p) % p)
        inverse = pow(scalar, -1, p)
        assert scalar*inverse % p == 1
        assert left["refined_coefficient"]*scalar % p == right["refined_coefficient"]
        assert left["p1_coefficient"]*scalar % p == right["p1_coefficient"]
        classification_maps.append([left["number"], right["number"], scalar, inverse])
assert len(classification_maps) == 3*12*12
assert Counter((r["p"], r["actual_zero"]) for r in answers) == Counter({(5, False): 12, (5, True): 12, (7, False): 12})
assert [r["number"] for r in answers if r["claimed_zero"] != r["actual_zero"]] == [21, 22, 25, 26, 27, 28, 29, 30, 33, 34]

LANE.mkdir(exist_ok=True)
payload = dict(raw_sha256=RAW_SHA, natural_count=len(natural),
               natural_profile_counts=natural_counts, pattern_count=len(answers),
               initial_row_count=30, patterns=answers, classification_maps=classification_maps,
               symbolic_checks=["p1 normal = -2 Euler", "full nodal Gaussian gauge",
                                "full cusp Gaussian gauge and Cartier translation",
                                "both base-monodromy gauge identities",
                                "finite determinant and section-sweep divisibility",
                                "all cyclic generator inverses and 432 oriented comparison maps"])
(LANE/"S6_SERIES_PUBLISH_III_02LC_fresh_data.json").write_text(
    json.dumps(payload, indent=2)+"\n")
columns = ["number", "OS", "profile", "a", "b", "zero", "p", "q", "selected_nu",
           "selected_kappa", "elliptic_site", "tate_r", "w", "cusp_degree_xi",
           "elliptic_degree_xi", "cubic", "p1_coefficient", "refined_coefficient",
           "claimed_zero", "actual_zero", "choices"]
with (LANE/"S6_SERIES_PUBLISH_III_02LC_fresh_patterns.tsv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=columns, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    for row in answers:
        result = {k: row[k] for k in columns if k in row}
        result.update(elliptic_site=row["elliptic"]["site"],
                      tate_r=row["elliptic"]["tate_hG_order"],
                      w=row["elliptic"]["w"],
                      elliptic_degree_xi=row["elliptic"]["degree_xi"],
                      choices=",".join(f'{o["site"]}:{o["kind"]}:{o["filling"]}' for o in row["choices"]))
        writer.writerow(result)

print("RAW", RAW_SHA)
print("NATURAL PROFILE COUNTS")
for row in natural_counts:
    print(*row)
print("NATURAL TOTAL", len(natural))
print("PATTERNS", len(answers), "INITIAL ROWS", 30)
for row in answers:
    E = row["elliptic"]
    print("\nPATTERN", row["number"], row["OS"], row["profile"],
          "a,b,zero=", row["a"], row["b"], row["zero"], "p,q=", row["p"], row["q"],
          "choices=", row["choices"])
    print("C", row["C"], "C_inverse", row["C_inverse"])
    print("FORWARD", row["all_forward_T"])
    print("cusp_H", row["cusp_H"], "inverse", row["cusp_H_inverse"])
    print("K", row["cusp_K"], "delta_Jordan", row["delta_Jordan"])
    print("slopes", row["cusp_slopes"], "characters", row["cusp_line_characters"])
    print("cusp normal", row["cusp_normal_weights"], "degree xi", row["cusp_degree_xi"])
    for node in row["rank_one"]:
        print("NODE", node["site"], node["kind"], "fixed", node["fixed"],
              "vanishing", node["vanishing"], "CS", node["CS"], "CL", node["CL"],
              "K", node["K"], "delta_short", node["delta_short"])
        print("node_H", node["H"], "inverse", node["H_inverse"])
    print("FIXED E", E["site"], "weights", E["normal_weights"],
          "character", E["line_character"], "degree xi", E["degree_xi"],
          "Tate r,rho,w", E["tate_hG_order"], E["tate_R_order"], E["w"])
    print("KILL", row["kill"], "RIGHT INVERSE", row["kill_right_inverse"])
    print("INVARIANTS cubic,p1,refined", row["cubic"], row["p1_coefficient"], row["refined_coefficient"],
          "claimed zero", row["claimed_zero"], "actual zero", row["actual_zero"])
    print("GENERATOR MAPS", row["generator_changes"],
          "Cp map/inverse", row["acting_generator_change"], row["acting_generator_change_inverse"],
          "normalized w", row["normalized_w"])
print("\nCOUNTS BY p, refined-zero", sorted(Counter((r["p"], r["actual_zero"]) for r in answers).items()))
print("LOCAL-RULE MISMATCHES", [r["number"] for r in answers if r["claimed_zero"] != r["actual_zero"]])
print("ORIENTED COMPARISON MAPS", len(classification_maps))
for first in range(1, 37):
    print("FROM", first, [row[1:] for row in classification_maps if row[0] == first])
print("ALL EXACT MATRIX AND SYMBOLIC ASSERTIONS PASSED")
