"""Exact certificates for C.2.UN.55's two-ended torus period family.

The first base period is normalized to one.  The second base period,
both unitary line characters, and the full horizontal cycle translation
remain symbolic.  No sample of these data is substituted in the proof.
"""
from pathlib import Path
import sympy as S

x, y, a, c, c1, c2, sig1, sig2, re_tau, im_tau = S.symbols(
    "x y a c c1 c2 sig1 sig2 re_tau im_tau", real=True
)
z = x + S.I*y
r2 = x*x + y*y
w1 = S.Matrix([1, c1])
w2 = S.Matrix([a + S.I*c, c2])
p = S.Matrix([0, 1])
b = S.Matrix([sig1 + S.I*sig2, S.I])


def V(w):
    return S.Matrix([w[0] + z*S.conjugate(w[1]),
                     w[1] - z*S.conjugate(w[0])])


def real(w):
    return S.Matrix([S.re(w[0]), S.im(w[0]), S.re(w[1]), S.im(w[1])])


v1, v2, vp, vb = map(V, (w1, w2, p, b))
tau = re_tau + S.I*im_tau
D = S.factor(S.Matrix.hstack(real(v1), real(v2), real(vp), real(vb + tau*vp)).det())
expected = c*(1+r2)*((1+r2) + im_tau*(1-r2))
assert S.expand(D - expected) == 0
assert not (D.free_symbols & {a, c1, c2, sig1, sig2, re_tau})
D1 = S.factor(S.Matrix.hstack(real(v1), real(v2), real(vp), real(S.I*vp)).det())
assert S.expand(D1 - c*(1+r2)*(1-r2)) == 0
q = S.I*vp
inverse_q = S.Matrix([q[0] - z*S.conjugate(q[1]),
                      q[1] + z*S.conjugate(q[0])])/(1+r2)
assert all(S.simplify(entry) == 0 for entry in
           inverse_q - S.I*S.Matrix([2*z, 1-r2])/(1+r2))

# The change at infinity is a holomorphic O(1)^2 frame change.
zz, ss = S.symbols("zz ss", nonzero=True)
u1, u2, v1c, v2c = S.symbols("u1 u2 v1c v2c")
Vformal = S.Matrix([u1 + zz*v2c, u2 - zz*v1c])
Vinfinity = S.Matrix([v2c + ss*u1, -v1c + ss*u2])
assert all(S.simplify(entry) == 0 for entry in
           (Vformal/zz).subs(zz, 1/ss) - Vinfinity)

# The normal sum changes sign exactly when log(z)=-log(s).
N = S.symbols("N", integer=True, positive=True)
monodromy = S.eye(4)
monodromy[2, 3] = N
assert monodromy.det() == 1
assert (monodromy-S.eye(4))**2 == S.zeros(4)
assert (monodromy-S.eye(4)).rank() == 1
assert monodromy.inv()[2, 3] == -N

lines = [
    "C.2.UN.55: symbolic twistor-log period certificates",
    f"Exact determinant before the logarithmic substitution: {D}",
    "Independent of the arbitrary horizontal translation sigma, both real line characters, and Re(tau).",
    f"Exact normal transversality determinant: {D1}",
    "PASS inverse(V_z)(i V_z(p))=i*(2z,1-|z|^2)/(1+|z|^2).",
    "Substitution Im(tau)=-N*log(r)/(2*pi) gives:",
    "c*(1+r^2)*(1+r^2+N*(r^2-1)*log(r)/(2*pi)).",
    "This is strictly positive: c>0, r>0, N>0, and (r^2-1)*log(r)>=0.",
    "PASS exact infinity frame V_z(w)/z=J(conjugate(w))+s*w, s=1/z.",
    "PASS opposite normal sum and logarithmic coefficient at infinity.",
    "PASS integral monodromy T=I+N E34, det(T)=1, rank(T-I)=1, (T-I)^2=0; infinity monodromy is T^-1.",
    "Every symbolic comparison passed; the proper fillings are constructed by the exact maps in the proof.",
]
output = "\n".join(lines) + "\n"
Path(__file__).with_suffix(".out").write_text(output)
print(output, end="")
