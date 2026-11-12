#!/usr/bin/env python3
"""Exact finite checks supporting the S6 candidate-specific validation update.

Scope: integer matrices and polynomial/monomial identities only.  The script does
not certify the global quotient, the topology, analytic duality, or the existence
of the candidate complex manifold.
"""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
import sympy as sp


@dataclass
class Result:
    id: str
    statement: str
    status: str
    certificate: str


def colon_principal_monomial(ideal_gen: tuple[int, ...], divisor: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a - min(a, b) for a, b in zip(ideal_gen, divisor, strict=True))


def lcm_monomial(*mons: tuple[int, ...]) -> tuple[int, ...]:
    out = mons[0]
    for m in mons[1:]:
        out = tuple(max(a, b) for a, b in zip(out, m, strict=True))
    return out


def mon(exp: tuple[int, ...]) -> str:
    names = ("x", "y", "z")
    parts: list[str] = []
    for name, n in zip(names, exp, strict=True):
        if n == 1:
            parts.append(name)
        elif n > 1:
            parts.append(f"{name}^{n}")
    return "1" if not parts else "".join(parts)


def main() -> int:
    results: list[Result] = []

    B0 = sp.Matrix([[0, 1], [-1, 0]])
    ok = B0.det() == 1 and B0.T * B0 == sp.eye(2) and B0.inv() == -B0
    results.append(Result(
        "ALG-01",
        "B0 is integral, unimodular, orthogonal, and invertible with B0^{-1}=-B0.",
        "PASS" if ok else "FAIL",
        f"det(B0)={B0.det()}, B0^T B0={list(B0.T * B0)}, B0^-1={list(B0.inv())}",
    ))

    f2 = (1, 1, 0)
    cx = colon_principal_monomial(f2, (1, 0, 0))
    cy = colon_principal_monomial(f2, (0, 1, 0))
    inter2 = lcm_monomial(cx, cy)
    results.append(Result(
        "LM-01",
        "In C{x,y,z}/(xy), the common annihilator of x and y is zero.",
        "PASS" if inter2 == f2 else "FAIL",
        f"(xy):x=({mon(cx)}), (xy):y=({mon(cy)}), intersection=({mon(inter2)})=(xy).",
    ))

    f3 = (1, 1, 1)
    colons = [
        colon_principal_monomial(f3, (0, 1, 1)),
        colon_principal_monomial(f3, (1, 0, 1)),
        colon_principal_monomial(f3, (1, 1, 0)),
    ]
    inter3 = lcm_monomial(*colons)
    results.append(Result(
        "LM-02",
        "In C{x,y,z}/(xyz), the common annihilator of yz, xz, and xy is zero.",
        "PASS" if inter3 == f3 else "FAIL",
        "Colon ideals are " + ", ".join(f"({mon(c)})" for c in colons) + f"; intersection=({mon(inter3)})=(xyz).",
    ))

    x, y, z = sp.symbols("x y z")
    c0, c1, c2, a0, a1, a2, b0, b1, b2 = sp.symbols("c0 c1 c2 a0 a1 a2 b0 b1 b2")
    k = c0 + c1*z + c2*z**2
    h1 = k + y*(a0 + a1*y + a2*z)
    h2 = k + x*(b0 + b1*x + b2*z)
    lift2 = sp.expand(h1 + h2 - k)
    ok2 = sp.expand(lift2.subs(x, 0) - h1) == 0 and sp.expand(lift2.subs(y, 0) - h2) == 0
    results.append(Result(
        "LM-03",
        "The double-locus normalization/conductor inclusion-exclusion lift restricts to both branches.",
        "PASS" if ok2 else "FAIL",
        "For compatible h1=k(z)+y a(y,z), h2=k(z)+x b(x,z), h=h1+h2-k(z) has h|_{x=0}=h1 and h|_{y=0}=h2.",
    ))

    c, ax, ay, az, A, B, C = sp.symbols("c ax ay az A B C")
    kx, ky, kz = c + ax*x, c + ay*y, c + az*z
    t1 = ky + kz - c + y*z*A
    t2 = kx + kz - c + x*z*B
    t3 = kx + ky - c + x*y*C
    lift3 = sp.expand(t1 + t2 + t3 - t1.subs(y, 0) - t1.subs(z, 0) - t2.subs(z, 0) + t1.subs({y: 0, z: 0}))
    ok3 = all(sp.expand(expr) == 0 for expr in (
        lift3.subs(x, 0) - t1,
        lift3.subs(y, 0) - t2,
        lift3.subs(z, 0) - t3,
    ))
    results.append(Result(
        "LM-04",
        "The triple-locus normalization/conductor inclusion-exclusion lift restricts to all three branches.",
        "PASS" if ok3 else "FAIL",
        "A compatible polynomial family with common vertex value and pairwise-product remainders was reconstructed exactly on x=0, y=0, z=0.",
    ))

    G2 = sp.groebner([x, y], x, y, z)
    coeff2 = [y, x, sp.Integer(0)]
    okc2 = all(G2.reduce(e)[1] == 0 for e in coeff2)
    results.append(Result(
        "LM-05",
        "The coefficients of d(xy)=y dx+x dy vanish on the reduced double conductor.",
        "PASS" if okc2 else "FAIL",
        "Groebner reduction of [y,x,0] modulo (x,y) is [0,0,0].",
    ))

    G3 = sp.groebner([x*y, x*z, y*z], x, y, z)
    coeff3 = [y*z, x*z, x*y]
    okc3 = all(G3.reduce(e)[1] == 0 for e in coeff3)
    results.append(Result(
        "LM-06",
        "The coefficients of d(xyz)=yz dx+xz dy+xy dz vanish on the reduced triple conductor.",
        "PASS" if okc3 else "FAIL",
        "Groebner reduction of [yz,xz,xy] modulo (xy,xz,yz) is [0,0,0].",
    ))

    p = 12*0 - 4*1 - 3*(-1)
    results.append(Result(
        "TOP-01",
        "The candidate's displayed twist integer is p=12*l0-4*l1-3*l2=-1.",
        "PASS" if p == -1 else "FAIL",
        f"12*0-4*1-3*(-1)={p}.",
    ))

    passed = sum(r.status == "PASS" for r in results)
    payload = {
        "title": "S6 exact finite identity checks",
        "scope": "Integer matrix and local polynomial/monomial identities only.",
        "passed": passed,
        "total": len(results),
        "results": [asdict(r) for r in results],
    }
    out = Path(__file__).resolve().parents[1] / "evidence"
    out.mkdir(parents=True, exist_ok=True)
    (out / "exact_identity_checks.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    with (out / "exact_identity_checks.txt").open("w", encoding="utf-8") as fh:
        fh.write(f"{passed}/{len(results)} checks passed\n\n")
        for r in results:
            fh.write(f"[{r.status}] {r.id}: {r.statement}\n    {r.certificate}\n")
    print(json.dumps({"passed": passed, "total": len(results)}, indent=2))
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
