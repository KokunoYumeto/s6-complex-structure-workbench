#!/usr/bin/env python3
"""Post-exposure LK: explicit period-ideal connecting map and inverse.

Laurent polynomials are integer coefficient dictionaries.  No target
historical algorithm is read. All 139 frozen lattices are checked in
their original basis and in an orientation-preserving rotated basis.
"""
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "agents/continuation7_iii_general_cusp/S6_SERIES_PUBLISH_III_02LK_fresh_lattice_data.json"
ONE = {(0, 0): 1}
AX = {(1, 0): 1, (0, 0): -1}
AY = {(0, 1): 1, (0, 0): -1}


def add(p, q, scale=1):
    out = dict(p)
    for e, c in q.items():
        out[e] = out.get(e, 0) + scale*c
        if not out[e]:
            del out[e]
    return out


def mul(p, q):
    out = {}
    for e, c in p.items():
        for f, d in q.items():
            k = (e[0]+f[0], e[1]+f[1])
            out[k] = out.get(k, 0)+c*d
    return {e:c for e,c in out.items() if c}


def mon(e):
    return {tuple(e): 1}


def norm(e, n):
    js, sign = (range(n), 1) if n >= 0 else (range(n, 0), -1)
    return {(j*e[0], j*e[1]):sign for j in js}


def moments(p):
    return (sum(p.values()),
            sum(c*e[0] for e,c in p.items()),
            sum(c*e[1] for e,c in p.items()))


def coordinates(B, w):
    u, v = B
    det = u[0]*v[1]-u[1]*v[0]
    numerators = (v[1]*w[0]-v[0]*w[1], -u[1]*w[0]+u[0]*w[1])
    assert det > 0 and all(n % det == 0 for n in numerators)
    return tuple(n//det for n in numerators)


def same_mod_alpha(xi, eta, alpha):
    diff = tuple(x-y for x,y in zip(xi, eta))
    j = next(i for i,c in enumerate(alpha) if c)
    if diff[j] % alpha[j]:
        return False
    k = diff[j]//alpha[j]
    return all(d == k*a for d,a in zip(diff, alpha))


def one(record, rotated):
    hnf = record["L"]
    ha, hb, hc = hnf[0][0], hnf[0][1], hnf[1][1]
    assert hnf[1][0] == 0
    u, v = (ha, 0), (hb, hc)
    if rotated:
        u, v = v, (-u[0], -u[1])
    B = (u, v)
    Au, Av = add(mon(u), ONE, -1), add(mon(v), ONE, -1)
    alpha = (v[0], v[1], -u[0], -u[1])
    first = math.gcd(*alpha)
    assert first == record["smith"][0]

    def representative(e):
        nv, j = divmod(e[1], hc)
        i = (e[0]-nv*hb) % ha
        return i, j

    def divide(p):
        residue, f, g = {}, {}, {}
        for e, c in p.items():
            r = representative(e)
            nu, nv = coordinates(B, (e[0]-r[0], e[1]-r[1]))
            residue = add(residue, mon(r), c)
            fterm = mul(mon(r), mul(norm(u, nu), mon((nv*v[0], nv*v[1]))))
            gterm = mul(mon(r), norm(v, nv))
            f, g = add(f, fterm, c), add(g, gterm, c)
        assert p == add(residue, add(mul(Au, f), mul(Av, g)))
        return residue, f, g

    def section(c):
        aug, mx, my = moments(c)
        assert aug == 0
        n1, n2 = coordinates(B, (mx, my))
        h = add(add(c, Au, -n1), Av, -n2)
        assert moments(h) == (0, 0, 0)
        assert divide(h)[0] == c
        return h

    def beta(xi):
        left = add({}, AX, xi[0])
        left = add(left, AY, xi[1])
        right = add({}, AX, xi[2])
        right = add(right, AY, xi[3])
        return add(mul(Au, left), mul(Av, right))

    def forward(h):
        assert moments(h) == (0, 0, 0)
        c = divide(h)[0]
        residual = add(h, section(c), -1)
        zero, f, g = divide(residual)
        assert not zero
        fm, gm = moments(f), moments(g)
        assert fm[0] == gm[0] == 0
        xi = fm[1:]+gm[1:]
        # Difference from beta(xi) is explicitly in the period ideal times I^2.
        f2 = add(add(f, AX, -xi[0]), AY, -xi[1])
        g2 = add(add(g, AX, -xi[2]), AY, -xi[3])
        assert moments(f2) == moments(g2) == (0, 0, 0)
        assert add(residual, beta(xi), -1) == add(mul(Au, f2), mul(Av, g2))
        return c, xi

    Ru = add(add(Au, AX, -u[0]), AY, -u[1])
    Rv = add(add(Av, AX, -v[0]), AY, -v[1])
    assert moments(Ru) == moments(Rv) == (0, 0, 0)
    assert beta(alpha) == add(mul(Av, Ru), mul(Au, Rv), -1)
    for j in range(4):
        xi = tuple(int(j == k) for k in range(4))
        c, inverse = forward(beta(xi))
        assert not c and same_mod_alpha(inverse, xi, alpha)
    torsion = tuple(k//first for k in alpha)
    c, inverse = forward(beta(torsion))
    assert not c and same_mod_alpha(inverse, torsion, alpha)
    for j in range(1, first+1):
        assert same_mod_alpha(tuple(j*k for k in torsion), (0, 0, 0, 0), alpha) == (j == first)

    classes = 0
    points, DK = record["components"], record["disc_basis"]
    for j in range(record["index"]-1):
        c = {tuple(p):DK[i][j] for i,p in enumerate(points) if DK[i][j]}
        assert all(representative(e) == e for e in c)
        h = section(c)
        rc, rx = forward(h)
        assert rc == c and same_mod_alpha(rx, (0, 0, 0, 0), alpha)
        xi = (2, -3, 5, -7)
        mixed = add(h, beta(xi))
        rc, rx = forward(mixed)
        assert rc == c and same_mod_alpha(rx, xi, alpha)
        shifted = add(mixed, add(mul(Au, mul(AX, AX)), mul(Av, mul(AY, AY))))
        rc, rx = forward(shifted)
        assert rc == c and same_mod_alpha(rx, xi, alpha)
        classes += 1
    # The positive syzygy changes derivative coordinates by alpha.
    f, g = mul(Av, add(ONE, AX)), mul(Au, add(ONE, AX))
    fm, gm = moments(f), moments(g)
    assert fm[1:]+tuple(-k for k in gm[1:]) == alpha
    return classes


def main():
    assert sha256(DATA.read_bytes()).hexdigest() == "0141c55f7ec26c20d6a76baa64f4ce9be67a84a524f8a095c906756cf4c6428e"
    records = json.loads(DATA.read_text())["cases"]
    counts = Counter()
    for r in records:
        for rotated in (False, True):
            counts["basis_cases"] += 1
            counts["free_section_basis_vectors"] += one(r, rotated)
            counts["negative_period_bases"] += int(rotated)
            counts["nontrivial_torsion_cases"] += int(r["smith"][0] > 1)
    assert len(records) == 139 and counts["basis_cases"] == 278
    print("PASS positive and rotated oriented bases for all 139 declared lattices", flush=True)
    print("PASS literal Laurent period-ideal division, with signed negative powers", flush=True)
    print("PASS positive beta columns and derivative inverse modulo the exact alpha", flush=True)
    print("PASS alpha relation -Au*Rv+Av*Ru, with both residuals in I^2", flush=True)
    print("PASS primitive torsion generator has exact order s in every case", flush=True)
    print("PASS every free last-kernel basis vector has an explicit I^2 section", flush=True)
    print("PASS both mixed-coordinate inverse composites and period-ideal representative changes", flush=True)
    print("PASS syzygy changes the inverse derivative coordinate by aug(k)*alpha", flush=True)
    print("COUNTS", json.dumps(dict(counts), sort_keys=True), flush=True)
    print("COMPLETED_UTC", datetime.now(timezone.utc).isoformat(), flush=True)


if __name__ == "__main__":
    main()

