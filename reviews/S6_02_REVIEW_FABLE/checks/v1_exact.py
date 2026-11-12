# Reviewer's independent exact checks for S6_02_FAMILY (A.2, A.3, B.2, B.4, F.1, F.2).
import sympy as s, itertools, random
from sympy.matrices.normalforms import smith_normal_form
M = s.Matrix
I4 = s.eye(4)
# AC26 page 2 (transcription l.143-147): T1,T2 on V (columns = images); A_j=(T_j^{-1})^t on Lambda
T1 = M([[1, 0, -6, 2], [0, -1, 1, 1], [0, -1, 0, 1], [0, 0, 0, 1]])
T2 = M([[1, 6, 0, -3], [0, 0, -1, 1], [0, 1, 0, 0], [0, 0, 0, 1]])
A1 = (T1.inv()).T
A2 = (T2.inv()).T
A1r = M([[1, 0, 0, 0], [6, 0, 1, 0], [-6, -1, -1, 0], [-2, 1, 0, 1]])
A2r = M([[1, 0, 0, 0], [0, 0, -1, 0], [-6, 1, 0, 0], [3, 0, 1, 1]])
print("A1,A2 of the return equal (T_j^-1)^t of AC26:", A1 == A1r, A2 == A2r)
print("orders:", A1**3 == I4, A2**4 == I4, "A2^2!=I", A2**2 != I4)
A0 = (A1 * A2).inv()
print("A0 unipotent (A0-1)^2=0:", (A0 - I4)**2 == s.zeros(4), "A0 fixes w,d:", A0[:, 2] == I4[:, 2], A0[:, 3] == I4[:, 3])
g = M([[1, 0, 0, 0]])
d = M([0, 0, 0, 1])
E = d * g
print("gamma A_j = gamma:", g * A1 == g, g * A2 == g, " A_j d = d:", A1 * d == d, A2 * d == d)
eps = M([1, 2, -4, 0])
epsp = M([1, 3, -3, 0])
print("A1 eps=eps", A1 * eps == eps, " A2 epsp=epsp", A2 * epsp == epsp)
N1 = I4 + A1 + A1**2
N2 = I4 + A2 + A2**2 + A2**3
print("N1=", N1.tolist())
print("N2=", N2.tolist())
for name, A, Nm, fb in (("1", A1, N1, [eps, d]), ("2", A2, N2, [epsp, d])):
    ns = (A - I4).nullspace()
    B = M.hstack(*fb)
    cols = []
    for j in range(4):
        sol = (B.T * B).inv() * B.T * Nm[:, j]
        assert B * sol == Nm[:, j]
        cols.append(sol)
    C = M.hstack(*cols)
    # is fb a Z-basis of the fixed lattice? fixed lattice = ker(A-I) cap Z^4, saturated; check fb spans a saturated lattice
    sat = smith_normal_form(B, domain=s.ZZ).tolist()
    print("fixed rank", name, len(ns), " fb saturated (Smith of basis):", sat, " norm image in fixed basis:", C.tolist(), " Smith:", smith_normal_form(C, domain=s.ZZ).tolist())
# centraliser over Q
x = s.symbols("x0:16")
X = M(4, 4, x)
sol = s.solve(list(X * A1 - A1 * X) + list(X * A2 - A2 * X), x, dict=True)[0]
Xs = X.subs(sol)
free = sorted(Xs.free_symbols, key=str)
print("centraliser dimension", len(free), [Xs.subs({f: (1 if f == ff else 0) for f in free}).tolist() for ff in free])
# A.3.1 even shift data
n = s.symbols("n")
u = M([0, 1, 0, 0])
w = M([0, 0, 1, 0])
r1 = -n / s.Integer(3) * (u + w)
r2 = n / s.Integer(4) * (u + w)
print("(I-A1)r1 = n d/3 + l1 with l1=-n w:", (I4 - A1) * r1 - (n * d / 3 - n * w) == s.zeros(4, 1))
print("(I-A2)r2 = -n d/4 + l2 with l2=n/2 u:", (I4 - A2) * r2 - (-n * d / 4 + n * u / 2) == s.zeros(4, 1))
l0 = -A0 * ((-n * w) + A1 * (n * u / 2))
print("l0=", l0.T.tolist(), "(claimed 3n/2 w - n/2 d)")
print("N1*l1=-n*gamma(v1) d ?", N1 * (-n * w) == -n * d, "  N2*l2=-n*gamma(v2) d = n d ?", N2 * (n * u / 2) == n * d)


def memb1(vec):  # N1 Lambda = 3Z eps + Z d
    a = vec[0]
    rest = vec - a * eps
    return rest[0] == 0 and rest[1] == 0 and rest[2] == 0 and a % 3 == 0


def memb2(vec):
    a = vec[0]
    rest = vec - a * epsp
    return rest[0] == 0 and rest[1] == 0 and rest[2] == 0 and a % 4 == 0 and rest[3] % 2 == 0


gen1 = {tuple((N1 * M(v))) for v in itertools.product(range(-3, 4), repeat=4)}
gen2 = {tuple((N2 * M(v))) for v in itertools.product(range(-3, 4), repeat=4)}
ok = True
for a in range(-6, 7):
    for b in range(-3, 4):
        v1 = a * eps + b * d
        v2 = a * epsp + b * d
        if (tuple(v1) in gen1) != memb1(v1):
            ok = False
        if (tuple(v2) in gen2) != memb2(v2):
            ok = False
print("norm-image descriptions 3Z eps+Z d, 4Z epsp+2Z d agree with enumeration (window):", ok)
cnt = 0
bad = 0
for a in (1, -1):
    for nn in range(-3, 4):
        for r1_, r1p in itertools.product((1, 2, -1, -2, 4, 5), repeat=2):
            for r2_, r2p in itertools.product((1, -1, 3, -3, 5), repeat=2):
                for k2, k2p, k1, k1p in itertools.product((0, 1, 2, 3), (0, 1, 2), (0, 1), (0, 2)):
                    Sn = I4 + nn * E
                    d1 = Sn * (r1p * eps + k1p * d) - a * (r1_ * eps + k1 * d)
                    d2 = Sn * (r2p * epsp + k2p * d) - a * (r2_ * epsp + k2 * d)
                    lhs = memb1(-d1) and memb2(-d2)
                    rhs = ((r1p - a * r1_) % 3 == 0) and ((r2p - a * r2_) % 4 == 0) and ((a * k2 - k2p - nn * r2p) % 2 == 0)
                    cnt += 1
                    bad += (lhs != rhs)
print("B.2.1 norm criterion vs (B2.2):", cnt, "cases, mismatches", bad)
# B.4.1 coboundary lattice
e1 = M([0, 1, -2, 0])
f1 = M([0, 0, -3, 1])
e2 = M([0, 1, -1, 0])
f2 = M([0, 0, -2, 1])
print("Smith of I-A1, I-A2:", smith_normal_form(I4 - A1, domain=s.ZZ).tolist(), smith_normal_form(I4 - A2, domain=s.ZZ).tolist())
print("N1 e1,f1 = 0:", N1 * e1 == s.zeros(4, 1), N1 * f1 == s.zeros(4, 1), " N2 e2,f2=0:", N2 * e2 == s.zeros(4, 1), N2 * f2 == s.zeros(4, 1))
a_, b_, c_, dd = s.symbols("a b c dd")
vec = (a_ * e1 + b_ * f1) + A1 * (c_ * e2 + dd * f2)
print("u-coordinate of l1+A1 l2:", s.expand(vec[1]), " gamma-coordinate:", vec[0])
rows = []
for lam in (I4[:, 0], I4[:, 1], I4[:, 2], I4[:, 3]):
    c1 = (I4 - A1) * lam
    c2 = (I4 - A2) * lam
    s1 = s.solve(list(a_ * e1 + b_ * f1 - c1), [a_, b_], dict=True)[0]
    s2 = s.solve(list(c_ * e2 + dd * f2 - c2), [c_, dd], dict=True)[0]
    rows.append([s1[a_], s1[b_], s2[c_], s2[dd]])
Cb = M(rows).T
print("coboundary matrix (cols = images of basis):", Cb.tolist())
K = M([[0, 1, 2], [1, 0, 0], [0, 1, 0], [0, 0, 1]])
coords = (K.T * K).inv() * K.T * Cb
print("coboundaries in allowed basis:", coords.tolist(), " K*coords==Cb:", K * coords == Cb, " Smith:", smith_normal_form(coords, domain=s.ZZ).tolist())
# B.4.2 reflection matrix
H = M([[1, 0, 0, 0], [0, 1, 0, 0], [-6, 0, -1, 0], [0, -1, 0, -1]])
print("H^2=I", H**2 == I4, " H A2 H=A2^-1", H * A2 * H == A2.inv(), " H A1 H = A2^-1 A1^-1 A2", H * A1 * H == A2.inv() * A1.inv() * A2)
print("w1p=-A2 H eps =", (-A2 * H * eps).T.tolist(), " (claimed -eps+d =", (-eps + d).T.tolist(), ")  w2p=-H(-epsp)=", (H * epsp).T.tolist(), "(claimed epsp-3d =", (epsp - 3 * d).T.tolist(), ")")
tau, mu, beta = s.symbols("tau mu beta")
tb, mb, bb = s.symbols("taub mub betab")
Pic = M([[6 * mb, tb, 1, 0], [bb, mb, 0, 1]])
Pir = M([[6 * (1 - mb), -tb, 1, 0], [-bb, 1 - mb, 0, 1]])
print("Pi_{-cbar}(iota z) H = -conj(Pi_c(z)):", s.simplify(Pir * H + Pic) == s.zeros(2, 4))
# ---------------- F ----------------
Om = M([[0, 0, 0, 6], [0, 0, 1, 0], [0, -1, 0, 0], [-6, 0, 0, 0]])
print("A_j^T Om A_j = Om:", A1.T * Om * A1 == Om, A2.T * Om * A2 == Om)
J2 = M([[0, 1], [-1, 0]])


def gB(B, x, t):
    x = M(x)
    G = s.zeros(4)
    G[0, 0] = 1
    G[1:3, 0] = 6 * x
    G[1:3, 1:3] = B
    G[3, 0] = t
    G[3, 1:3] = -(x.T * J2 * B)
    G[3, 3] = 1
    return G


Sm = M([[0, -1], [1, 0]])
Tm = M([[1, 1], [0, 1]])
am = M([[0, 1], [-1, -1]])
print("A1=g(a,(1,-1),-2):", A1 == gB(am, [1, -1], -2), " A2=g(S,(0,-1),3):", A2 == gB(Sm, [0, -1], 3), " S a = T:", Sm * am == Tm)


def parse(G):
    assert G[0, 0] == 1 and G[0, 1] == 0 and G[0, 2] == 0 and G[0, 3] == 0 and G[3, 3] == 1 and G[1, 3] == 0 and G[2, 3] == 0
    B = G[1:3, 1:3]
    x = G[1:3, 0] / 6
    t = G[3, 0]
    assert all(v.is_integer for v in x) and G == gB(B, list(x), t)
    return B, x, t


def alpha(B):
    B = B.copy()
    val = 0
    while B[1, 0] != 0:
        k = B[0, 0] // B[1, 0]
        B = Tm**(-k) * B
        val += k
        B = Sm.inv() * B
        val += 9
    if B[0, 0] == -1:
        B = Sm**2 * B
        val += 18
    assert B[0, 0] == 1 and B[1, 1] == 1
    val += B[0, 1]
    return val % 12


def chi(G):
    B, x, t = parse(G)
    Q = x[0] + x[1] + x[0] * x[1]
    return (t + 6 * Q - alpha(B)) % 12


print("alpha(S),alpha(T),alpha(a):", alpha(Sm), alpha(Tm), alpha(am), " chi(A1),chi(A2):", chi(A1), chi(A2))
random.seed(1)
bad = 0
gens = [A1, A2, A1.inv(), A2.inv()]
for trial in range(300):
    G = I4
    for _ in range(random.randint(1, 14)):
        G = G * random.choice(gens)
    bad += chi(G) != 0
print("chi on 300 random words in A1,A2: nonzero count", bad)


def randSL():
    B = s.eye(2)
    for _ in range(random.randint(0, 8)):
        B = B * random.choice([Sm, Tm, Tm.inv(), Sm.inv()])
    return B


badh = 0
bada = 0
for trial in range(300):
    B1 = randSL()
    B2 = randSL()
    bada += (alpha(B1 * B2) - alpha(B1) - alpha(B2)) % 12 != 0
    G1 = gB(B1, [random.randint(-4, 4), random.randint(-4, 4)], random.randint(-20, 20))
    G2 = gB(B2, [random.randint(-4, 4), random.randint(-4, 4)], random.randint(-20, 20))
    assert G1.T * Om * G1 == Om and G1[:, 3] == d
    badh += (chi(G1 * G2) - chi(G1) - chi(G2)) % 12 != 0
print("alpha homomorphism failures:", bada, " chi homomorphism failures:", badh)
Kc = A1 * A2**2 * A1.inv() * A2**(-2)
print("K=[A1,A2^2]=", parse(Kc))
U = A2 * Kc * A2.inv()
V = Kc.inv()
Z = I4 + 12 * E
print("U=", parse(U), " V=", parse(V), " [U,V]=Z^-1:", U * V * U.inv() * V.inv() == Z.inv())
print("chi(I+E)=", chi(I4 + E), " chi(I+12E)=", chi(Z))
J0 = M([[0, 0, -1, 0], [0, 0, 0, -6], [1, 0, 0, 0], [0, s.Rational(1, 6), 0, 0]])
R = M([[1, 0, 0, 0], [0, 1, 72, 0], [0, 0, 1, 0], [-12, 0, 0, 1]])
print("J0^2=-I", J0**2 == -I4, " J0^T Om J0=Om", J0.T * Om * J0 == Om, " eig(Om J0)=", (Om * J0).eigenvals(), " q_e(J0)=", (d.T * Om * J0 * d)[0])
print("R=g(T^72,0,-12):", R == gB(Tm**72, [0, 0], -12), " chi(R)=", chi(R), " R J0=J0 R:", R * J0 == J0 * R, " (R-I)^2=0:", (R - I4)**2 == s.zeros(4))
import mpmath as mp
mp.mp.dps = 30
tauv = mp.mpc("0.3", "1.2")
muv = mp.mpc("0.5", "-0.4")
betav = mp.mpc("0.2", "-2.0")
P = mp.matrix([[6 * muv, tauv, 1, 0], [betav, muv, 0, 1]])
Rm = mp.matrix(4, 4)
for j in range(4):
    Rm[0, j] = mp.re(P[0, j])
    Rm[1, j] = mp.im(P[0, j])
    Rm[2, j] = mp.re(P[1, j])
    Rm[3, j] = mp.im(P[1, j])
Jc = mp.matrix([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]])
Jl = mp.inverse(Rm) * Jc * Rm
Omf = mp.matrix(Om.tolist())
ev = mp.matrix([0, 0, 0, 1])
qe = (ev.T * Omf * Jl * ev)[0]
D = mp.im(betav) - 6 * mp.im(muv)**2 / mp.im(tauv)
print("q_e numeric", qe, " -6/D", -6 / D, " det(real period matrix)", mp.det(Rm), " T*D", mp.im(tauv) * D)
print("|J^T Om J - Om|:", mp.norm(Jl.T * Omf * Jl - Omf))
