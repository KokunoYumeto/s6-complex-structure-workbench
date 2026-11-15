"""Exact lattice certificates for the mixed cycles of C.2.UN.51.

Start with two diagonal primary Hopf components, and insert any number
of ruled elliptic components on either edge.  The matrices below use
the actual outgoing and incoming normal meridians.  Thus they check
the cycle map, the separate ruled frames, and the primitive divisor of
the logarithmic period, rather than an abstract graph-only condition.
"""
from math import gcd
from pathlib import Path
import sympy as s

A, B, ell = s.symbols("A B ell", real=True)
n_a = s.Matrix([1, 0])
n_b = s.Matrix([0, -1])
common_periods = s.Matrix([[1, 0, A], [0, 1, B]])
e1, e2 = s.eye(2)[:, 0], s.eye(2)[:, 1]


def certificate(a, b):
    normals = [n_a] * a + [n_b] * b
    frames, outgoing, incoming, kinds = [], [], [], []
    for j, current in enumerate(normals):
        previous = normals[j - 1]
        if current != previous:
            frame = s.Matrix.hstack(current, -previous)
            kinds.append("Hopf")
            outgoing.append(e1)
            incoming.append(e2)
        else:
            transverse = n_b if current == n_a else n_a
            frame = s.Matrix.hstack(transverse, current)
            kinds.append("ruled")
            outgoing.append(e2)
            incoming.append(-e2)
        assert abs(frame.det()) == 1
        frames.append(frame)
    assert kinds.count("Hopf") == 2
    product = s.eye(2)
    for j, frame in enumerate(frames):
        nxt = (j + 1) % len(frames)
        edge = frames[nxt].inv() * frame
        assert edge * outgoing[j] == -incoming[nxt]
        assert edge * (frame.inv() * common_periods) == (
            frames[nxt].inv() * common_periods
        )
        product = edge * product
    assert product == s.eye(2)
    total_normal = -sum(normals, s.zeros(2, 1))
    assert total_normal == s.Matrix([-a, b])
    primitive_divisor = gcd(a, b)
    primitive = total_normal / primitive_divisor
    assert gcd(int(primitive[0]), int(primitive[1])) == 1
    real_period_det = s.det(s.Matrix.hstack(s.Matrix([A, B]), ell * total_normal))
    assert s.expand(real_period_det - ell * (a * B + b * A)) == 0
    # Both contraction logarithms and log|t| are negative.  Hence this
    # exact expression is positive, proving discreteness of the fourth
    # period for every one of the certified geometric families.
    numeric = real_period_det.subs({A: -1, B: -s.sqrt(2), ell: -3})
    assert numeric > 0
    return kinds, primitive_divisor, real_period_det


lines = [
    "C.2.UN.51: actual mixed-cycle normal-period certificates",
    "Common normal vectors n_a=(1,0), n_b=(0,-1).",
    "For a,b>=1: two Hopf vertices and a+b-2 ruled vertices.",
]
count = 0
for a in range(1, 14):
    for b in range(1, 14):
        certificate(a, b)
        count += 1
lines.append(f"PASS: {count} cycles; all edge inversions and rank-three periods agree.")
lines.append("PASS: every cycle product is I; every ruled frame is separately invertible.")
lines.append("PASS: u=(-a,b), d=gcd(a,b), det(real periods)=ell*(a*B+b*A)>0.")
for a, b in [(1, 1), (2, 1), (3, 2), (4, 6), (13, 13)]:
    kinds, d, determinant = certificate(a, b)
    lines.append(f"a={a}, b={b}: vertices={len(kinds)}, ruled={len(kinds)-2}, d={d}, det={determinant}")

# In an all-ruled cycle the normal constants span one complex line.
# The other coordinate of the total affine translation is untouched.
sigma, vertical, c1, c2, c3 = s.symbols("sigma vertical c1 c2 c3")
translation = s.Matrix([sigma, vertical])
normal_change = (c1 + c2 + c3) * e2
assert (translation + normal_change)[0] == sigma
lines.append("PASS: all-ruled normal constants retain the horizontal translation sigma exactly.")
lines.append("Scope: these are explicit geometric families and period comparisons; no all-ruled compact globalization is asserted.")
output = "\n".join(lines) + "\n"
Path(__file__).with_suffix(".out").write_text(output)
print(output, end="")
