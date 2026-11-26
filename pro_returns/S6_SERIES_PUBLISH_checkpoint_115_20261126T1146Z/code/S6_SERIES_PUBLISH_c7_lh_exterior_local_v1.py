#!/usr/bin/env python3
"""Fresh LH all-row exterior, local saturated kernels and finite lattices.

The admitted raw defining fixture and LD defining matrices are the only
mathematical data inputs.  Every tested map is recomputed with reversible
integer Smith maps; no LH target original or historical code is opened.
"""
from collections import Counter
from hashlib import sha256
from math import gcd, lcm
from pathlib import Path
import json
import re
from sympy import Matrix, Rational, eye, zeros
from sympy.matrices.normalforms import hermite_normal_form
from S6_SERIES_PUBLISH_c7_lh_integral import (
    integral, rows, bezout, bezout_vector, exterior, wedge, smith, kernel,
    saturated_image, image_basis, right_inverse, invariants,
    component_data, permutation_power, cycles,
)

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT/"agents/continuation7_iii_odd_weighted"
LD = ROOT/"agents/continuation7_iii_weighted_catalogue"
RAW = ROOT/"agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json"
assert sha256(RAW.read_bytes()).hexdigest() == "6bda97b01ba63c0a796e3141609ca12e163791b626024b79104817ec5defc522"
raw = {(r["OS"], r["profile"]): r for r in json.loads(RAW.read_text())["rows"]}
source = json.loads((LD/"S6_SERIES_PUBLISH_III_02LD_fresh_exterior_data.json").read_text())
catalogue = source["rows"]
WEIGHTS = (1, 2, 3, 5, 7, 9, 15, 21, 25, 35, 45, 105, 315, 1001)
FINITE = {"II": 6, "III": 4, "IV": 3, "III*": 4, "IV*": 3}
J = Matrix([[0, 1], [-1, 0]])
DELTA = eye(4)[:, 2]
records, report = [], Counter()
finite_records, local_records = [], []
profile_counts = Counter()


def vanishing(B, section, nu):
    M = B-eye(2)
    col = next(M[:, j] for j in range(2) if M[:, j] != zeros(2, 1))
    u = col/gcd(*(int(x) for x in col))
    if next(x for x in u if x) < 0:
        u = -u
    common, x, y = bezout(int(u[0]), int(u[1]))
    assert common == 1 and M == nu*u*u.T*J
    r = Matrix([-y, x])
    kappa = next(section[j]/u[j] for j in range(2) if u[j])
    assert kappa.q == 1 and section == kappa*u
    return u, r, int(kappa)


def local_kernel(row, rawrow, site, D, original):
    """Actual weight-one kernels and their all-D rational cover preimages."""
    A1 = Matrix(row["monodromies"][site])
    S = Matrix.diag(1, 1, 1, D)
    A = integral(S.inv()*A1*S)
    E = exterior(A)-eye(6)
    E1 = exterior(A1)-eye(6)
    kind = row["fibres"][site]
    a, b = row["key"][2:4]
    q, residue = row["components"][site]
    nonzero = (a*residue) % q != 0
    k1 = kd = None
    if original and nonzero:
        B = Matrix(rawrow["elliptic_matrices"][site])
        sec = Matrix(rawrow["generator_section_cocycle"][site])
        if re.fullmatch(r"I\d+", kind):
            nu = int(kind[1:])
            u, r, kap = vanishing(B, sec, nu)
            assert b % nu == 0
            common, x, z = bezout(a*kap, nu)
            assert common == 1
            beta0 = Matrix([*(x*u), z, 0])
            ell1 = Matrix([*list(-Rational(b*kap, nu)*r), 0, 1])
            elld = Matrix([*list(-Rational(D*b*kap, nu)*r), 0, 1])
        else:
            z = (B-eye(2)).inv()*sec
            assert b % q == 0
            rho = integral(q*Matrix([[a*z[1], -a*z[0], 1]]))
            common, vv = bezout_vector(list(rho))
            assert common == 1
            beta0 = Matrix([*vv, 0])
            ell1 = Matrix([*list(-b*z), 0, 1])
            elld = Matrix([*list(-D*b*z), 0, 1])
        k1, kd = integral(wedge(beta0, ell1)), integral(wedge(beta0, elld))
        assert exterior(S)*kd == D*k1
        old = Matrix.hstack(E1, k1)
        new = Matrix.hstack(E, kd)
    else:
        old, new = E1, E
    K1, L1, Q1, sec1 = saturated_image(old)
    KD, LDinv, QD, secD = saturated_image(new)
    transfer_fibre = integral(D*exterior(S).inv())
    assert exterior(S)*transfer_fibre == D*eye(6)
    pulled, pulled_inverse = kernel(Q1*exterior(S))
    assert hermite_normal_form(pulled) == hermite_normal_form(KD)
    cover_on_quotient = integral(Q1*exterior(S)*secD)
    transfer_on_quotient = integral(QD*transfer_fibre*sec1)
    assert cover_on_quotient*transfer_on_quotient == D*eye(Q1.rows)
    assert transfer_on_quotient*cover_on_quotient == D*eye(QD.rows)
    assert Q1*exterior(S) == cover_on_quotient*QD
    return KD, {
        "kernel": rows(KD), "kernel_left_inverse": rows(LDinv),
        "quotient": rows(QD), "quotient_section": rows(secD),
        "cover_quotient": rows(cover_on_quotient),
        "transfer_quotient": rows(transfer_on_quotient),
        "weight_one_quotient": rows(Q1),
        "extra_actual_generator": rows(kd) if kd is not None else None,
    }


for row in catalogue:
    key = row["key"]
    a, b, selected = key[2], key[3], key[4]-1
    rawrow = raw[tuple(key[:2])]
    assert gcd(a, b) == 1
    old_matrices = [Matrix(A) for A in row["monodromies"]]
    for D in WEIGHTS:
        g = gcd(a, D)
        if g % 2 == 0:
            continue
        S = Matrix.diag(1, 1, 1, D)
        matrices = [integral(S.inv()*A*S) for A in old_matrices]
        total = eye(4)
        for A in matrices:
            total *= A
        assert total == eye(4)
        G = Matrix.hstack(*((A-eye(4))[:3, :] for A in matrices[:-1]))
        assert hermite_normal_form(G) == Matrix.diag(1, 1, g)
        normalized = integral(Matrix.diag(1, 1, Rational(1, g))*G)
        right = right_inverse(normalized)
        K, KL = kernel(G)
        assert abs(Matrix.hstack(right, K).det()) == 1
        E = Matrix.hstack(*(exterior(A)-eye(6) for A in matrices[:-1]))
        target = Matrix.hstack(eye(6)[:, 1], eye(6)[:, 3], eye(6)[:, 2],
                              eye(6)[:, 4], D*b*eye(6)[:, 0]+a*eye(6)[:, 5])
        assert hermite_normal_form(E) == hermite_normal_form(target)
        alpha, beta = a//g, D*b//g
        common, u, v = bezout(alpha, beta)
        assert common == 1
        quotient = Matrix([[alpha, 0, 0, 0, 0, -beta],
                           [v, 0, 0, 0, 0, u]])
        section = Matrix.hstack(u*eye(6)[:, 0]-v*eye(6)[:, 5],
                               beta*eye(6)[:, 0]+alpha*eye(6)[:, 5])
        assert quotient*section == eye(2)
        assert quotient[0, :]*E == zeros(1, E.cols)
        assert all(x % g == 0 for x in quotient[1, :]*E)
        assert section[:, 1]*g == D*b*eye(6)[:, 0]+a*eye(6)[:, 5]
        assert invariants(E) == (1, [g] if g > 1 else [])
        old_q = Matrix([[a, 0, 0, 0, 0, -b]])
        assert old_q*exterior(S) == g*quotient[0, :]
        report["exteriors"] += 1
        report["shared_exteriors"] += g > 1
        profile_counts[tuple(key[:2])] += 1
        details = []
        for i, (A, kind) in enumerate(zip(matrices, row["fibres"])):
            F, FL = kernel(A-eye(4))
            assert F.cols == (3 if re.fullmatch(r"I\d+", kind) and i != selected else 2)
            q, residue = row["components"][i]
            narrow = (a*residue) % q == 0
            permutation, multiplicities = component_data(kind)
            powered = permutation_power(permutation, -D*b*residue)
            orbits = cycles(powered)
            original_options = [False, True] if i != selected and not narrow else [False]
            kernels = {}
            for orig in original_options:
                kd, cert = local_kernel(row, rawrow, i, D, orig)
                name = "original_nonzero" if orig else "ordinary"
                kernels[name] = cert
                report["local_kernels"] += 1
                if orig:
                    assert kd.cols == len(kernels["ordinary"]["kernel"][0])+1
            info = {
                "site": i+1, "type": kind, "fixed": rows(F), "fixed_inverse": rows(FL),
                "component_permutation": powered, "component_orbits": orbits,
                "component_multiplicities": multiplicities, "narrow": narrow,
                "kernels": kernels,
            }
            if i == selected:
                B = Matrix(rawrow["elliptic_matrices"][i])
                sec = Matrix(rawrow["generator_section_cocycle"][i])
                nu = int(kind[1:])
                uu, rr, kap = vanishing(B, sec, nu)
                C = integral(Matrix([[nu, b*kap],
                                     [-a*kap, Rational(1-a*b*kap*kap, nu)]]))
                assert C.det() == 1 and gcd(a, nu) == 1
                c22 = int(C[1, 1])
                assert gcd(c22, g) == 1 and D % g == 0
                assert gcd(g, c22) == 1
                disc = Matrix([[1]*D, [j*c22 for j in range(D)]])
                # The codomain is Z mu + (Z/g) delta.
                rel = Matrix.hstack(disc, Matrix([0, g]))
                assert invariants(rel) == (0, [])
                common, ss, tt = bezout(c22, g)
                assert common == 1
                if g > 1:
                    assert ss*(disc[:, 1]-disc[:, 0])+tt*Matrix([0, g]) == Matrix([0, 1])
                info["cusp_C"] = rows(C)
                info["disc_delta_coefficient"] = c22
                info["disc_delta_bezout"] = [ss, tt]
                report["cusp_disc_maps"] += 1
            if re.fullmatch(r"I\d+", kind) and i != selected and narrow:
                nu = int(kind[1:])
                B = Matrix(rawrow["elliptic_matrices"][i])
                sec = Matrix(rawrow["generator_section_cocycle"][i])
                uu, rr, kap = vanishing(B, sec, nu)
                r0 = gcd(D, nu)
                assert len(orbits) == r0 and a % nu == 0
                common, x, y = bezout(nu//r0, D*b*kap//r0)
                assert common == 1
                short = Matrix([*uu, -a*kap//nu, 0])
                first = Matrix([*(x*rr), 0, y])
                last = Matrix([*list(-D*b*kap//r0*rr), 0, nu//r0])
                basis = Matrix.hstack(short, first, DELTA, last)
                assert abs(basis.det()) == 1
                model = eye(4); model[0, 1] = r0
                assert basis.inv()*A*basis == model
                info["rank_one_period_basis"] = rows(basis)
                info["rank_one_period_inverse"] = rows(basis.inv())
                info["rank_one_components"] = r0
                report["rank_one_period_maps"] += 1
            if kind in FINITE:
                h = FINITE[kind]
                Nh = sum((A**j for j in range(h)), zeros(4, 4))
                assert A**h == eye(4)
                image = integral(FL*Nh)
                H, preH = image_basis(image)
                assert H.shape == (2, 2)
                Q = integral(H.inv()*image)
                RP = right_inverse(Q)
                assert F*H*Q == Nh and Q*RP == eye(2)
                norm_record = {
                    "key": key, "D": D, "site": i+1, "h": h,
                    "fixed": rows(F), "fixed_inverse": rows(FL), "norm": rows(Nh),
                    "norm_image_basis": rows(H), "norm_image_preimages": rows(preH),
                    "projected_quotient": rows(Q), "projected_section": rows(RP),
                    "actions": [],
                }
                annihilators = [kernel((A**j-eye(4)).T)[0] for j in range(h)]
                # Test every power by its primitive integral annihilator,
                # independently of the projected-lattice criterion.
                for multiple in (1, 2, h):
                    m = h*multiple
                    for zz in ((1, 0), (0, 1), (1, 1), (1, -1), (2, 1), (1, 2), (2, 3), (3, 2)):
                        power = F*Matrix(zz)
                        w = integral(Q*power)
                        t = gcd(m, *(int(z) for z in w))
                        predicted = gcd(m, *(int(z) for z in power)) == 1 and (m//t) % h == 0
                        actual = True
                        stabilizer = None
                        for j in range(1, m):
                            annihilator = annihilators[j % h]
                            value = Rational(j, m)*annihilator.T*power
                            if all(x.q == 1 for x in value):
                                actual, stabilizer = False, j
                                break
                        assert predicted == actual
                        core = Matrix.hstack(
                            Matrix.vstack(A-eye(4), zeros(1, 4)),
                            Matrix.vstack(-power, Matrix([m])))
                        core_free, core_torsion = invariants(core)
                        assert core_free == 2
                        Nm = multiple*Nh
                        normal_fibre = Matrix.hstack(*(-wedge(eye(4)[:, j], power) for j in range(4)))
                        assert Nm*(A-eye(4)) == zeros(4, 4)
                        # H1(core) relations disappear in the complete Thom map.
                        relation_fibre = normal_fibre*(A-eye(4))
                        assert quotient[0, :]*relation_fibre == zeros(1, 4)
                        assert all(x % g == 0 for x in quotient[1, :]*relation_fibre)
                        assert normal_fibre*power == zeros(6, 1) and Nm*power == m*power
                        norm_record["actions"].append({
                            "m": m, "power": rows(power), "projected": rows(w),
                            "free": actual, "first_stabilizer": stabilizer,
                            "core_H1_torsion": core_torsion,
                        })
                        report["finite_actions"] += 1
                        report["free_finite_actions"] += actual
                finite_records.append(norm_record)
                report["finite_positions_weighted"] += 1
            details.append(info)
        records.append({
            "key": key, "D": D, "g": g, "matrices": [rows(A) for A in matrices],
            "H1_relations": rows(G), "H1_normalized_section": rows(right),
            "graph_kernel": rows(K), "graph_kernel_left_inverse": rows(KL),
            "fibre_quotient": rows(quotient), "fibre_section": rows(section),
            "local": details,
        })

for key, count in sorted(profile_counts.items()):
    print("PROFILE", *key, "ODD_WEIGHT_CASES", count)
print("PASS", len(catalogue), "natural rows; new reversible integer quotient and inverse maps at every recorded weight.")
print("PASS exact H1 image diag(1,1,g), full fibre quotient Z plus Z/g, and primitive graph bases.")
print("PASS", report["local_kernels"], "saturated local kernels, with exact cover/transfer inverse identities.")
print("PASS", report["rank_one_period_maps"], "literal rank-one period maps and component powers, including shared indices.")
print("PASS", report["cusp_disc_maps"], "cusp component-disc maps and the unit angular residue, retaining Z/g.")
print("PASS", report["finite_actions"], "finite actions tested through EVERY proper power;", report["free_finite_actions"], "free.")
print("PASS all finite projected quotient sections and full core H1 presentations; no nonunit factor removed.")
print("PASS all core relations map to zero under the complete five-generator Thom map.")
print("COUNTS", json.dumps(dict(sorted(report.items())), sort_keys=True))
print("SCOPE finite arithmetic corroborates the separate all-parameter proof; LH original and historical code remain closed.")
(LANE/"S6_SERIES_PUBLISH_III_02LH_fresh_local_data.json").write_text(
    json.dumps({"scope": "New LH integer maps, all recorded weights and complete local outputs.",
                "weights": WEIGHTS, "counts": dict(report), "records": records}, indent=2)+"\n")
(LANE/"S6_SERIES_PUBLISH_III_02LH_fresh_finite_data.json").write_text(
    json.dumps({"scope": "New full projected-lattice and every-power tests.", "records": finite_records}, indent=2)+"\n")
