#!/usr/bin/env python3
"""Check the released KV/KW auxiliary constants from frozen fresh cap data.

This is post-exposure arithmetic, not a new blind derivation.  It neither
imports nor executes either historical program and changes no fresh file.
"""
from pathlib import Path
from itertools import combinations
from functools import reduce
from math import gcd
import json

import sympy as S
from sympy.polys.domains import ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "agents/continuation7_iii_original_caps"
KV = json.loads((OUT / "S6_SERIES_PUBLISH_III_02KV_fresh_cap_maps.json").read_text())
KW = json.loads((OUT / "S6_SERIES_PUBLISH_III_02KW_fresh_cap_maps.json").read_text())
PAIRS = list(combinations(range(4), 2))
I4 = S.eye(4)
I6 = S.eye(6)


def array(A):
    assert all(x.q == 1 for x in A)
    return [[int(x) for x in A.row(i)] for i in range(A.rows)]


def wedge(A):
    return S.Matrix([[A.extract(i, j).det() for j in PAIRS] for i in PAIRS])


def decomp(A):
    D, U, V = smith_normal_decomp(DomainMatrix.from_Matrix(A).convert_to(ZZ))
    D, U, V = (x.to_Matrix() for x in (D, U, V))
    assert U*A*V == D and abs(U.det()) == abs(V.det()) == 1
    rank = sum(D[i, i] != 0 for i in range(min(D.shape)))
    return D, U, V, rank


def smith(A):
    D, _, _, rank = decomp(A)
    return [abs(int(D[i, i])) for i in range(rank)]


def kernel(A):
    D, U, V, rank = decomp(A)
    K = V[:, rank:]
    assert A*K == S.zeros(A.rows, K.cols)
    return K


def basis_certificate(Diff, K):
    D, U, V, rank = decomp(K)
    assert rank == K.cols == Diff.cols-Diff.rank()
    assert all(abs(D[i, i]) == 1 for i in range(rank))
    assert Diff*K == S.zeros(Diff.rows, K.cols)
    E = S.zeros(K.cols, K.rows)
    for i in range(rank):
        E[i, i] = 1/D[i, i]
    L = V*E*U
    assert L*K == S.eye(K.cols)
    return L, {
        "differential": array(Diff), "basis": array(K), "left_inverse": array(L),
        "Smith_D": array(D), "Smith_U": array(U), "Smith_Uinv": array(U.inv()),
        "Smith_V": array(V), "Smith_Vinv": array(V.inv()),
    }


def product(matrices):
    ans = I4
    for A in matrices:
        ans = ans*A
    return ans


def graph(Ts):
    """Based boundary injections, with the last peripheral eliminated."""
    N = len(Ts)
    assert product(Ts) == I4
    D = S.Matrix.hstack(*(A-I4 for A in Ts[:-1]))
    js = []
    for i in range(N-1):
        j = S.zeros(4*(N-1), 4)
        j[4*i:4*i+4, :] = I4
        js.append(j)
    last = S.Matrix.vstack(*(-product(Ts[i+1:-1]) for i in range(N-1)))
    js.append(last)
    for A, j in zip(Ts, js):
        F = kernel(A-I4)
        assert D*j*F == S.zeros(4, F.cols)
    return D, js


all_kv = []
for row in KV:
    local = row["local"]
    Ts = [S.Matrix(x["T"]) for x in local]
    d = row["d"]
    omega = S.Matrix([[1, 0, 0, 0, 0, -d]])
    C = S.Matrix.hstack(*(wedge(T)-I6 for T in Ts))
    assert smith(C) == [1]*5 and omega*C == S.zeros(1, C.cols)
    additive = []
    for cap, T in zip(local, Ts):
        if cap["type"] in ("I1", "II"):
            continue
        z1, z2 = map(S.Rational, cap["zQ"])
        assert z1.q == z2.q == 1
        fixed = S.Matrix.hstack(I4[:, 2], S.Matrix([-z1, -z2, 0, 1]))
        assert (T-I4)*fixed == S.zeros(4, 2) and smith(fixed) == [1, 1]
        assert smith(T-I4) == [1, 1]
        assert smith(wedge(T)-I6) == [1]*4
        area = S.Matrix([[1, 0, z2, 0, -z1, 0]])
        F = S.eye(6)[:, 1:]
        F[0, :] = S.Matrix([[0, -z2, 0, z1, 0]])
        assert area*F == S.zeros(1, 5)
        assert omega*F == S.Matrix([[0, -z2, 0, z1, -d]])
        h = gcd(d, int(z1), int(z2))
        additive.append({"type": cap["type"], "zQ": [int(z1), int(z2)],
                         "h": h, "fixed_basis": array(fixed),
                         "area": array(area), "area_kernel": array(F),
                         "omega_on_kernel": array(omega*F)})
    assert reduce(gcd, (x["h"] for x in additive)) == 1
    D, js = graph([I4] + Ts)
    B = S.Matrix.hstack(*(j*kernel(T-I4) for j, T in zip(js[1:], Ts)))
    K = S.Matrix.hstack(B, js[0][:, [0, 1, 3]])
    L, cert = basis_certificate(D, K)
    assert smith(D) == [1, 1, 1]
    assert L[-3:, :]*js[0] == S.Matrix([[1, 0, 0, 0],
                                                 [0, 1, 0, 0],
                                                 [0, 0, 0, 1]])
    # Boundary H1 has one base-meridian generator in addition to coinvariants.
    boundary_ranks = [5] + [5-(T-I4).rank() for T in Ts]
    cap_ranks = [4] + [len(x["f1"]) for x in local]
    exterior_h1 = len(Ts)+1
    ranks = [sum(boundary_ranks), exterior_h1+sum(cap_ranks)]
    expected = [19, 18] if row["profile"] == "default" else (
        [14, 13] if row["OS"] in (43, 46) else [14, 12])
    assert ranks == expected, (row["OS"], row["profile"], ranks, expected)
    cert.update({"OS": row["OS"], "profile": row["profile"], "local": additive,
                 "degree_one_source_target_ranks": ranks,
                 "global_exterior_detector": array(omega)})
    all_kv.append(cert)
    print(f"PASS KV {row['OS']}/{row['profile']}: local Smith/fibre kernels; "
          f"global area quotient Z; full primitive graph basis; H1 ranks {ranks}")

all_kw = []
for row in KW:
    source = next(x for x in KV if (x["OS"], x["profile"]) ==
                  (row["OS"], row["profile"]))
    Ts = [S.Matrix(x["T"]) for x in source["local"]]
    f = row["finite_index"]
    Ts = Ts[f:] + Ts[:f]
    D, js = graph(Ts)
    ell = S.Matrix(row["ell"])
    B = S.Matrix.hstack(*(j*kernel(T-I4) for j, T in zip(js[1:], Ts[1:])))
    K = S.Matrix.hstack(B, js[0]*ell)
    L, cert = basis_certificate(D, K)
    assert K.cols == 5 and smith(D) == [1, 1, 1]
    assert (L[-1:, :]*js[0]*I4[:, 2])[0] == 0
    assert (L[-1:, :]*js[0]*ell)[0] == 1
    q, h, d = row["q"], row["h"], source["d"]
    beta = (S.Matrix([1, 0, 0, 0]) if row["finite_type"] in ("IV*", "III")
            else S.Matrix([1, 0, 1, 0]) if row["finite_type"] == "IV"
            else S.Matrix([0, 0, 1, 0]))
    rho = S.Matrix(row["rho"])
    assert (rho*beta[:3, :])[0] == 1
    N = sum((Ts[0]**i for i in range(q)), S.zeros(4))
    assert N*beta == (S.Rational(q, h))*I4[:, 2]
    assert N*ell == q*ell
    omega = S.Matrix([[1, 0, 0, 0, 0, -d]])
    def pairing(u, v):
        return (omega*S.Matrix([u[i]*v[j]-u[j]*v[i] for i, j in PAIRS]))[0]
    assert -pairing(beta, ell) == S.Rational(d, h)
    assert -pairing(ell, I4[:, 2]) == -d
    assert gcd(h, d//h) == 1
    assert all(q % p == 0 for p in S.factorint(h))
    cert.update({"OS": row["OS"], "profile": row["profile"],
                 "finite_type": row["finite_type"], "finite_index": f,
                 "q": q, "q_delta": h, "h": h, "c": d//h,
                 "beta": array(beta), "ell": array(ell), "norm_q": array(N),
                 "residual_graph_row": array(L[-1:, :]*js[0])})
    all_kw.append(cert)
    print(f"PASS KW {row['OS']}/{row['profile']} finite {row['finite_type']}: "
          f"primitive rank-five graph basis; q_delta={h}; c={d//h}; exact norm rows")

result = {"scope": "Post-exposure verification of auxiliary constants only; no historical program execution.",
          "KV": all_kv, "KW": all_kw}
(OUT / "S6_SERIES_PUBLISH_III_02KV_KW_post_exposure_constants.json").write_text(
    json.dumps(result, indent=2) + "\n", newline="\n")
print("PASS eleven auxiliary constant cases; unrestricted log elimination is proved separately.")
