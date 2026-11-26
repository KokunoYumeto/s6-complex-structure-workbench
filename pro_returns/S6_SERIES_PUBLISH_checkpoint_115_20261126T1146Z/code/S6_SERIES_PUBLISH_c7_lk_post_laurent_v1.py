#!/usr/bin/env python3
"""Post-exposure LK: literal Laurent matrices and the integral Tor map.

Reads only the frozen fresh lattice data, not any historical algorithm.
The universal identities prove the displayed chain equivalences.
The finite loop checks the 139 declared lattice cases and exact inverses.
"""
from datetime import datetime, timezone
from hashlib import sha256
import json
import math
from pathlib import Path

from sympy import Matrix, Rational, ZZ, eye, simplify, symbols, zeros
from sympy.matrices.normalforms import smith_normal_decomp

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT / "agents/continuation7_iii_general_cusp_receiving"
DATA = ROOT / "agents/continuation7_iii_general_cusp/S6_SERIES_PUBLISH_III_02LK_fresh_lattice_data.json"
OUTPUT = LANE / "S6_SERIES_PUBLISH_III_02LK_post_laurent_data_v1.json"
x, y = symbols("x y")
a, b = x - 1, y - 1


def clean(M):
    return M.applyfunc(simplify)


def equal(A, B):
    assert A.shape == B.shape
    assert clean(A - B) == zeros(*A.shape)


def bar(M):
    return clean(M.subs({x: 1/x, y: 1/y}, simultaneous=True))


def reflect(M):
    return clean(M.subs({y: 1/y}, simultaneous=True))


def integral(M):
    assert all(t.q == 1 for t in M)
    return Matrix(M.rows, M.cols, [int(t) for t in M])


def rows(M):
    return [[int(t) for t in row] for row in M.tolist()]


def symbolic():
    B = Matrix([[-1/x, -1, -1/x, -1/x],
                [1, 1, 1, y], [-x*y, -x*y, -1, -x*y]])
    F = Matrix([[1-x, 0], [0, x*y-1], [y-1, x*y*(y-1)]])
    U = Matrix([[1, 0, 0, 0], [-1, 1, 0, 0],
                [-1, 0, 1, 0], [-y, 0, 0, 1]])
    V = Matrix([[0, x, 0], [1, 1, x*y], [0, 0, 1]])
    diagonal = zeros(4, 3)
    diagonal[0, 0] = 1
    diagonal[1:, 1:] = F
    equal(U*B.T*V, diagonal)
    assert simplify(U.det()) == 1 and simplify(V.det()) == -x
    equal(U*U.inv(), eye(4))
    equal(V*V.inv(), eye(3))
    print("PASS 01 exact B-transpose unit cancellation, with U/V and both inverses", flush=True)

    T = Matrix([[0, 0, -1/x],
                [-1/(x*y*y), 1/(x*y), -1/(x*x*y)],
                [-1/y, 0, 0]])
    S = Matrix([[y, x*y*y], [x, 0]])
    C = Matrix([[-b, 0], [a, -b], [0, a]])
    g = Matrix([[a*a, a*b, b*b]])
    equal(T.inv()*F, C*S)
    equal(g*C, zeros(1, 2))
    assert simplify(T.det()) in (1/(x*x*y*y), -1/(x*x*y*y))
    assert simplify(S.det()) == -x*x*y*y
    print("PASS 02 literal D.GC7 identity and Laurent-unit determinants", flush=True)

    # The actual homology differential includes the deck involution.
    d = bar(B.T)
    D = Matrix.diag(x**-2, (x*y)**-1, y**-2)
    E = Matrix.diag(-1/(x*x*y), -1/(x*y*y))
    equal(D*bar(C), C*E)
    pr = eye(4)[1:, :]
    ins = pr.T
    Q = clean(D*bar(T).inv()*pr*bar(U))
    section = clean(bar(U).inv()*ins*bar(T)*D.inv())
    source_forward = clean(E*Matrix.hstack(zeros(2, 1), bar(S))*bar(V).inv())
    source_inverse = clean(bar(V)*Matrix.vstack(zeros(1, 2), bar(S).inv()*E.inv()))
    pivot = eye(4)[:, 0]
    homotopy = clean(bar(V)[:, 0]*pivot.T*bar(U))
    equal(Q*section, eye(3))
    equal(section*Q, eye(4)-d*homotopy)
    equal(Q*d, C*source_forward)
    equal(section*C, d*source_inverse)
    equal(source_forward*source_inverse, eye(2))
    equal(source_inverse*source_forward+homotopy*d, eye(3))
    equal(g*Q*d, zeros(1, 3))
    print("PASS 03 full homology differential bar(B)^t -> I^2 chain maps and homotopies", flush=True)

    # The pre-exposure half-edge presentation maps to the same ideal.
    Tf = Matrix([[1-x, 0], [0, 1-y], [-(1-y/x), 1-y/x]])
    P = Matrix([[0, 1/x, 0], [-1/x, -1/x, 1], [1/x, 0, 0]])
    W = Matrix([[0, 1/x], [-1/x, 0]])
    equal(P*Tf, C*W)
    equal(P.inv()*C, Tf*W.inv())
    equal(g*P, Matrix([[(b*b-a*b)/x, (a*a-a*b)/x, a*b]]))
    print("PASS 04 fresh half-edge presentation -> I^2 exact Laurent coordinate maps", flush=True)

    # A reversed second deck generator transports the lattice itself.
    Dr = Matrix.diag(1, -1/y, y**-2)
    Er = Matrix.diag(-1/y, y**-2)
    equal(Dr*reflect(C), C*Er)
    equal(Dr*reflect(P)*reflect(Tf), C*Er*reflect(W))
    equal(reflect(reflect(Tf)), Tf)
    print("PASS 05 reflected deck marking, square-ideal generators and inverse reflection", flush=True)

    # Koszul chain map I -> I/I^2.  Coordinates are
    # e_x tensor E1, e_y tensor E1, e_x tensor E2, e_y tensor E2.
    differential = Matrix([[a, b, 0, 0], [0, 0, a, b]])
    lift = Matrix([0, -1, 1, 0])
    equal(differential*lift, Matrix([-b, a]))
    print("PASS 06 Koszul lift 1 -> -e_y tensor E1 + e_x tensor E2", flush=True)


def one(record):
    L = Matrix(record["L"])
    index = int(L.det())
    assert index == record["index"] > 0
    first, second = map(int, record["smith"])
    u, v = L[:, 0], L[:, 1]
    alpha = Matrix([v[0], v[1], -u[0], -u[1]])
    assert math.gcd(*(int(t) for t in alpha)) == first
    # Norm edge cycles have displacement index*e_j.
    ex = integral(L.inv()*Matrix([index, 0]))
    ey = integral(L.inv()*Matrix([0, index]))
    assert ex == Matrix([v[1], -u[1]])
    assert ey == Matrix([-v[0], u[0]])
    from_norm = Matrix([-ey[0], ex[0], -ey[1], ex[1]])
    assert from_norm == alpha

    delta, left, right = smith_normal_decomp(alpha, domain=ZZ)
    if delta[0, 0] < 0:
        flip = eye(4)
        flip[0, 0] = -1
        delta, left = flip*delta, flip*left
    assert left*alpha*right == delta
    assert int(delta[0, 0]) == first
    inverse = integral(left.inv())
    assert left*inverse == inverse*left == eye(4)
    primitive = integral(alpha/first)
    assert abs(int((left*primitive)[0])) == 1
    assert left*primitive == Matrix([int(right[0, 0]), 0, 0, 0])
    # Quotient forward is left*z, first coordinate modulo first;
    # inverse uses inverse*[residue,three free coordinates].
    probe = Matrix([2, -3, 5, -7])
    marked = left*probe
    marked[0] %= first
    back = inverse*marked
    difference = probe-back
    coefficient = integral(left*difference)[0]//first
    assert difference == inverse[:, 0]*(first*coefficient)
    assert inverse[:, 0]*first == alpha*right[0, 0]

    # This is the common free kernel J of I tensor S -> Z^2,
    # also the component-meridian augmentation kernel from the fresh proof.
    DK = Matrix(record["disc_basis"])
    if index == 1:
        assert DK.shape == (1, 0)
        DI = zeros(0, 1)
    else:
        DI = Matrix([[Rational(t) for t in row] for row in record["disc_inverse"]])
    assert DI*DK == eye(index-1)
    assert Matrix([[1]*index])*DK == zeros(1, index-1)
    assert record["normalization_coker"] == [index+2, ([first] if first > 1 else [])]
    assert record["cap_H2"] == [index+3, ([first] if first > 1 else [])]
    return {"L":rows(L), "alpha":rows(alpha), "alpha_smith":first,
            "left":rows(left), "inverse":rows(inverse),
            "source_sign":int(right[0, 0]),
            "norm_x_coordinates":rows(ex), "norm_y_coordinates":rows(ey),
            "free_last_kernel_rank":index-1,
            "normalization_rank":index+2}


def main():
    symbolic()
    assert sha256(DATA.read_bytes()).hexdigest() == "0141c55f7ec26c20d6a76baa64f4ce9be67a84a524f8a095c906756cf4c6428e"
    old = json.loads(DATA.read_text())
    records = [one(r) for r in old["cases"]]
    assert len(records) == 139
    print("PASS 07 all 139 oriented alpha_L columns from norm cycles, with exact signs", flush=True)
    print("PASS 08 all 139 Smith quotient/inverse maps, primitive vector and torsion order", flush=True)
    print("PASS 09 all 139 last-kernel coordinate inverses, including D=1", flush=True)
    print("PASS 10 all 139 Tor-derived cokernel ranks/torsion compared with fresh normalization", flush=True)
    saved = {"scope":"Post-exposure literal Laurent identities and alpha_L finite inverse checks.",
             "cases":records}
    OUTPUT.write_text(json.dumps(saved, sort_keys=True, separators=(",",":"))+"\n")
    assert json.loads(OUTPUT.read_text()) == saved
    print("PASS 11 saved data reread exactly; no historical program read or executed", flush=True)
    print("DATA_SHA256", sha256(OUTPUT.read_bytes()).hexdigest(), flush=True)
    print("COMPLETED_UTC", datetime.now(timezone.utc).isoformat(), flush=True)


if __name__ == "__main__":
    main()

