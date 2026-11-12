"""Portable exact checks for the homogeneous gauge-lift audit.

Run: python verify_gauge_lift.py
Dependency: SymPy. No files, network services or repository paths are used.
The accompanying report supplies proofs; these checks independently replay
potential derivatives, every homogeneous field variation, and orbit identities.
"""
import sympy as S

I = S.I
Z3 = S.zeros(3)
eye = S.eye(3)
checks = 0


def comm(a, b):
    return a * b - b * a


def tf(a):
    return a - S.trace(a) * eye / 3


def zero(label, value):
    global checks
    entries = list(value) if isinstance(value, S.MatrixBase) else [value]
    assert all(S.simplify(S.expand(e)) == 0 for e in entries), label
    checks += 1


def eij(i, j):
    out = S.zeros(3)
    out[i, j] = 1
    return out


anti = []
herm = []
for i in range(3):
    for j in range(i + 1, 3):
        anti += [eij(i, j) - eij(j, i), I * (eij(i, j) + eij(j, i))]
        herm += [eij(i, j) + eij(j, i), I * (eij(i, j) - eij(j, i))]
diag = [S.diag(1, -1, 0), S.diag(0, 1, -1)]
anti += [I * d for d in diag]
herm += diag
vec = [eye[:, i] for i in range(3)] + [I * eye[:, i] for i in range(3)]


def lincomb(basis, values):
    return sum((v * b for v, b in zip(values, basis)), S.zeros(*basis[0].shape))


# All fourteen potential derivatives, with independent generic coordinates.
pp = S.symbols("p0:8", real=True)
bb = S.symbols("b0:6", real=True)
m2, Gamma, kap = S.symbols("m2 Gamma kappa", real=True)
phi = lincomb(herm, pp)
b = lincomb(vec, bb)
s = S.trace(phi * phi) + 2 * (b.H * b)[0]
a = m2 + Gamma * s
potential = m2 * s / 2 + Gamma * s**2 / 4 - kap * (phi.det() - (b.H * phi * b)[0])
grad_phi = a * phi - kap * tf(phi.adjugate() - b * b.H)
grad_b = (a * eye + kap * phi) * b
for n, direction in enumerate(herm):
    zero("potential Phi derivative " + str(n),
         S.diff(potential, pp[n]) - S.trace(grad_phi * direction))
for n, direction in enumerate(vec):
    zero("potential b derivative " + str(n),
         S.diff(potential, bb[n]) - 2 * S.re((direction.H * grad_b)[0]))


# Independent componentwise Euler-Lagrange test at an exact generic two-jet.
# The left side is differentiated from the displayed raw homogeneous Lagrangian.
eps, t = S.symbols("eps t", real=True)
g2 = S.Integer(7)
mm, gg, kk = S.Integer(2), S.Integer(3), S.Integer(5)
names = ["A0", "A1", "A2", "A3", "phi", "b"]
bases = {name: anti for name in names[:4]}
bases.update(phi=herm, b=vec)


def state(order):
    result = {}
    for index, name in enumerate(names):
        coefficients = [
            S.Rational(((index + 2) * (j + 3) + 5 * order) % 11 - 5, j % 3 + 1)
            for j in range(len(bases[name]))
        ]
        result[name] = lincomb(bases[name], coefficients)
    return result


q, qd, qdd = state(0), state(1), state(2)


def kinetic(q, qd):
    aa0, ph, bv = q["A0"], q["phi"], q["b"]
    electric = [qd["A" + str(i)] + comm(aa0, q["A" + str(i)]) for i in (1, 2, 3)]
    xx = qd["phi"] + comm(aa0, ph)
    vv = qd["b"] + aa0 * bv
    return -sum(S.trace(e * e) for e in electric) / g2 + S.trace(xx * xx) / 2 + (vv.H * vv)[0]


def lagrangian(q, qd):
    ph, bv = q["phi"], q["b"]
    spatial = [q["A" + str(i)] for i in (1, 2, 3)]
    magnetic = sum(S.trace(comm(spatial[i], spatial[j])**2)
                   for i in range(3) for j in range(i + 1, 3)) / g2
    spatial_matter = sum(S.trace(comm(ai, ph)**2) / 2 + ((ai * bv).H * (ai * bv))[0]
                         for ai in spatial)
    norm = S.trace(ph**2) + 2 * (bv.H * bv)[0]
    pot = mm * norm / 2 + gg * norm**2 / 4 - kk * (ph.det() - (bv.H * ph * bv)[0])
    return kinetic(q, qd) + magnetic - spatial_matter - pot


ph, bv, a0 = q["phi"], q["b"], q["A0"]
spatial = [q["A" + str(i)] for i in (1, 2, 3)]
electric = [qd["A" + str(i)] + comm(a0, q["A" + str(i)]) for i in (1, 2, 3)]
xx = qd["phi"] + comm(a0, ph)
vv = qd["b"] + a0 * bv
j0 = tf(comm(ph, xx) + bv * vv.H - vv * bv.H)
gauss_action = j0 - 2 * sum((comm(ai, ei) for ai, ei in zip(spatial, electric)), Z3) / g2
norm = S.trace(ph**2) + 2 * (bv.H * bv)[0]
force_phi = (mm + gg * norm) * ph - kk * tf(ph.adjugate() - bv * bv.H)
force_b = ((mm + gg * norm) * eye + kk * ph) * bv
ddphi = (qdd["phi"] + comm(qd["A0"], ph) + 2 * comm(a0, qd["phi"])
         + comm(a0, comm(a0, ph)))
ddb = qdd["b"] + qd["A0"] * bv + 2 * a0 * qd["b"] + a0**2 * bv
rphi = ddphi - sum((comm(ai, comm(ai, ph)) for ai in spatial), Z3) + force_phi
rb = ddb - sum((ai**2 * bv for ai in spatial), S.zeros(3, 1)) + force_b
spatial_action = []
for i, ai in enumerate(spatial, start=1):
    d0e = (qdd["A" + str(i)] + comm(qd["A0"], ai)
           + comm(a0, qd["A" + str(i)]) + comm(a0, electric[i - 1]))
    jij = tf(comm(ph, comm(ai, ph)) - bv * bv.H * ai - ai * bv * bv.H)
    curl = sum((comm(aj, comm(aj, ai)) for aj in spatial), Z3)
    spatial_action.append(2 * (d0e - curl) / g2 - jij)

qt = {name: q[name] + t * qd[name] + t**2 * qdd[name] / 2 for name in names}
qdt = {name: qd[name] + t * qdd[name] for name in names}
for name in names:
    for n, direction in enumerate(bases[name]):
        varied_q = dict(q)
        varied_q[name] += eps * direction
        partial_q = S.diff(lagrangian(varied_q, qd), eps).subs(eps, 0)
        if name == "A0":
            momentum_dot = 0
        else:
            varied_qdt = dict(qdt)
            varied_qdt[name] += eps * direction
            momentum = S.diff(kinetic(qt, varied_qdt), eps).subs(eps, 0)
            momentum_dot = S.diff(momentum, t).subs(t, 0)
        if name == "A0":
            expected = S.trace(gauss_action * direction)
        elif name.startswith("A"):
            expected = S.trace(spatial_action[int(name[1]) - 1] * direction)
        elif name == "phi":
            expected = -S.trace(rphi * direction)
        else:
            expected = -2 * S.re((direction.H * rb)[0])
        zero("raw Euler-Lagrange " + name + ":" + str(n),
             partial_q - momentum_dot - expected)


# Exact periodic-orbit and temporal-gauge identities in the retained K frame.
x, d, B, w = S.symbols("x d B w", real=True, nonzero=True)
H = S.Matrix([[0, 0, 0], [0, -x, d], [0, d, x]])
Om = S.Matrix([[0, -w, 0], [w, 0, 0], [0, 0, 0]])
b0 = B * eye[:, 0]
hp, bp = comm(Om, H), Om * b0
hpp = comm(Om, hp)
r2 = x*x + d*d
moment_phi = comm(H, hp)
moment_b = b0 * bp.H - bp * b0.H
zero("Phi moment", moment_phi + r2 * Om)
zero("b moment", moment_b + B**2 * Om)
zero("full scalar moment", moment_phi + moment_b + (r2 + B**2) * Om)
c, cd, cdd = S.symbols("c cd cdd", real=True)
ai = I*c*H
ei = I*cd*H + I*c*hp
zero("stabilizer commutator", comm(ai, H))
zero("stabilizer vector", ai*b0)
zero("electric Gauss contribution", comm(ai, ei) - c**2*r2*Om)
zero("spatial residual 11", (I*cdd*H + 2*I*cd*hp + I*c*hpp)[0,0] + 2*I*c*w*w*x)

zz = S.symbols("z0:8", real=True)
z = lincomb(anti, zz)
Lm = lambda z: tf(comm(H, comm(H, z)) + b0*b0.H*z + z*b0*b0.H)
zero("matter inertia quadratic form",
     -S.trace(z*Lm(z)) - S.trace(comm(z,H)**2) - 2*((z*b0).H*(z*b0))[0])
zero("orbit current is minus inertia", moment_phi + moment_b + Lm(Om))

# Scalar-compatible nonzero-A0 connection, with non-stabilizing spatial field.
alpha, beta = S.Rational(5,3), S.Rational(4,3)
a0 = (alpha-1)*Om
a1 = beta*Om
zero("hyperbolic coefficients", alpha**2-beta**2-1)
zero("flat connection", comm(a0,a1))
zero("nonzero A0 Phi scalar equation",
     comm(alpha*Om, comm(alpha*Om,H))-comm(a1,comm(a1,H))-hpp)
zero("nonzero A0 b scalar equation",
     (alpha*Om)**2*b0-a1**2*b0-Om**2*b0)
zero("nonzero A0 current", comm(H,comm(alpha*Om,H))
     +b0*(alpha*Om*b0).H-(alpha*Om*b0)*b0.H-alpha*(moment_phi+moment_b))
assert (a1*b0)[1] != 0
checks += 1

# Constructive radial branch and exact minimum observation.
xx, beta_r, xd, bd = S.symbols("xx beta_r xd bd", real=True)
D = S.diag(-2, 1, 1)
phi_r, b_r = xx*D, beta_r*eye[:, 0]
zero("radial adjugate", tf(phi_r.adjugate()-b_r*b_r.H)
     -(-xx**2+beta_r**2/3)*D)
zero("radial current", comm(phi_r,xd*D)
     +b_r*(bd*eye[:,0]).H-(bd*eye[:,0])*b_r.H)
sr = 6*xx**2+2*beta_r**2
ar = m2+Gamma*sr
fx = -ar*xx-kap*xx**2+kap*beta_r**2/3
fb = -(ar-2*kap*xx)*beta_r
vr = m2*sr/2+Gamma*sr**2/4-2*kap*xx*(beta_r**2-xx**2)
zero("radial energy derivative",
     6*xd*fx+2*bd*fb+S.diff(vr,xx)*xd+S.diff(vr,beta_r)*bd)
zero("radial equilibrium x equation",
     fx.subs(beta_r,3*xx)+xx*(m2+24*Gamma*xx**2-2*kap*xx))
zero("radial equilibrium b equation",
     fb.subs(beta_r,3*xx)+3*xx*(m2+24*Gamma*xx**2-2*kap*xx))
xstar = (3+S.sqrt(3))/12
zero("specified exact equilibrium", 24*xstar**2-12*xstar+1)
P = S.Matrix([[1,-1,0],[0,1,-1]])
u = S.ones(3,1)
C = P*P.T
zero("minimum observed matrix", P*S.diag(0,3*xx,3*xx)*P.T
     -3*xx*S.Matrix([[1,-1],[-1,2]]))
zero("minimum determinant equals rho square",
     (P*S.diag(0,3*xx,3*xx)*P.T).det()-9*xx**2)
zero("marked projector identity", P.T*C.inv()*P-eye+u*u.T/3)
zero("general adjugate compression", (P*phi*P.T).det()-(u.T*phi.adjugate()*u)[0])


def bmat(v):
    return S.Matrix([[0,S.conjugate(v[2]),-S.conjugate(v[1])],
                     [-S.conjugate(v[2]),0,S.conjugate(v[0])],
                     [S.conjugate(v[1]),-S.conjugate(v[0]),0]])


zero("skew quadratic identity", bmat(b)*S.conjugate(bmat(b))-b*b.H+(b.H*b)[0]*eye)
chi, ct, st = S.symbols("chi ct st", real=True)
amat = chi*S.diag(3*ct**2-1,3*st**2-1,-1)
btheta = S.Matrix([0,0,-3*chi*ct*st])
zero("minimum family quaternionic coefficient", bmat(btheta)[0,1]+3*chi*ct*st)
hp_a = amat+chi*eye
# The rank-one positive complex part has adjugate b b* exactly, without
# even needing ct²+st²=1 (that relation fixes the trace/minimum spectrum).
zero("minimum family rank-one adjugate", hp_a.adjugate()-btheta*btheta.H)
zero("minimum family invariant", (btheta.H*btheta)[0]-9*chi**2*ct**2*st**2)

print("PASS:", checks, "exact checks, including all 46 real homogeneous field variations.")
