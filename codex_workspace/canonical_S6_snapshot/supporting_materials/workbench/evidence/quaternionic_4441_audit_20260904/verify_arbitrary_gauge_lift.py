"""Bounded exact checks: python checker.py. No network, subprocesses, or Lean."""
import sympy as s


def comm(X, Y):
    return X * Y - Y * X


def tf(X):
    return X - s.trace(X) * s.eye(3) / 3


def total(items):
    return sum(items, s.zeros(3))


def zero(X):
    assert all(s.simplify(entry) == 0 for entry in X), X


def same(X, Y):
    zero(X - Y)


L = [s.Matrix([[0, 0, 0], [0, 0, -1], [0, 1, 0]]),
     s.Matrix([[0, 0, 1], [0, 0, 0], [-1, 0, 0]]),
     s.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])]


def cross_matrix(v):
    return total(v[j] * L[j] for j in range(3))


x, d, B, a = s.symbols('x d B a', real=True, nonzero=True)
H = s.Matrix([[0, 0, 0], [0, -x, d], [0, d, x]])
q = s.Matrix([B, 0, 0])
q11, q22, q33, q12, q13, q23 = s.symbols(
    'q11 q22 q33 q12 q13 q23', real=True)
Q = s.Matrix([[q11, q12, q13], [q12, q22, q23], [q13, q23, q33]])
h1, h2, h3 = s.symbols('h1 h2 h3', real=True)
Cd = cross_matrix([h1, h2, h3])
RH = comm(Cd, H) - a * comm(L[2], comm(L[2], H))
Rb = Cd * q + a * q
for j in range(3):
    for k in range(3):
        RH += Q[j, k] * comm(L[j], comm(L[k], H))
        Rb += Q[j, k] * L[j] * L[k] * q

RH_expected = s.Matrix([
    [2*a*x-4*d*q23+2*x*q22-2*x*q33,
     d*h2+3*d*q13+x*h3-3*x*q12,
     -d*h3+3*d*q12+x*h2+3*x*q13],
    [d*h2+3*d*q13+x*h3-3*x*q12,
     -2*a*x-2*d*h1+2*d*q23+4*x*q11+2*x*q33,
     a*d-4*d*q11-d*q22-d*q33-2*x*h1],
    [-d*h3+3*d*q12+x*h2+3*x*q13,
     a*d-4*d*q11-d*q22-d*q33-2*x*h1,
     2*d*h1+2*d*q23-4*x*q11-2*x*q22]])
same(RH, RH_expected)
same(Rb / B, s.Matrix([a-q22-q33, h3+q12, -h2+q13]))
unknowns = [q11, q22, q33, q12, q13, q23, h1, h2, h3]
solution = (0, d*q23/x, a-d*q23/x, 0, 0, q23, 0, 0, 0)
assert s.linsolve(list(RH)+list(Rb), unknowns) == s.FiniteSet(solution)
substitution = dict(zip(unknowns, solution))
zero(RH.subs(substitution))
zero(Rb.subs(substitution))
print('PASS: full real scalar residuals and necessary-and-sufficient solution')

v1, v2, v3, w1, w2, w3 = s.symbols('v1 v2 v3 w1 w2 w3', real=True)
vvec = s.Matrix([v1, v2, v3])
wvec = s.Matrix([w1, w2, w3])
Lv, Lw = cross_matrix(vvec), cross_matrix(wvec)
same(Lv*Lw, wvec*vvec.T - vvec.dot(wvec)*s.eye(3))
same(comm(Lv, Lw), cross_matrix(vvec.cross(wvec)))
assert s.simplify(-s.trace(Lv*Lw)-2*vvec.dot(wvec)) == 0
print('PASS: real commutator, product, and exact norm factor 2')


def inertia(Z, HH=H, qq=q):
    return tf(comm(HH, comm(HH, Z)) + qq*qq.conjugate().T*Z
              + Z*qq*qq.conjugate().T)


same(inertia(L[0]), 4*(x*x+d*d)*L[0])
for j in [1, 2]:
    same(inertia(L[j]), (x*x+d*d+B*B)*L[j])
print('PASS: exact real inertia on all three generators')

c1 = s.symbols('c1', real=True, nonzero=True)
c2, c3 = s.symbols('c2 c3', real=True)
c = s.Matrix([c1, c2, c3])
Qsolution = Q.subs(substitution)
P = c*c.T - Qsolution
same(P[1:, 1:] - P[1:, :1]*P[:1, 1:]/P[0, 0], -Qsolution[1:, 1:])
assert s.simplify(s.trace(Qsolution)-a) == 0
zero(Qsolution*s.Matrix([1, 0, 0]))
print('PASS: exact covariance Schur complement and positive target trace a')

u = s.Matrix([1, 1, 1])
v = s.Matrix([1, -1, 0])
w = s.Matrix([1, 1, -2])
K = s.Matrix.hstack(v/s.sqrt(2), w/s.sqrt(6), u/s.sqrt(3))
Phi0 = -x*w*w.T/6 + x*u*u.T/3 + d*(w*u.T+u*w.T)/s.sqrt(18)
b0 = B*v/s.sqrt(2)
J0 = s.Matrix([[0, -1, 1], [1, 0, -1], [-1, 1, 0]])
same(K.T*K, s.eye(3))
assert s.simplify(K.det()) == 1
same(K.T*Phi0*K, H)
same(K.T*b0, q)
same(K.T*J0*K, s.sqrt(3)*L[2])
same(J0*J0, -3*(s.eye(3)-u*u.T/3))
instance = {x:s.Rational(1, 2), d:1/(2*s.sqrt(2)),
            B:1/(2*s.sqrt(2)), a:2}
same(Phi0.subs(instance), s.Matrix([[1,1,1],[1,1,1],[1,1,-2]])/4)
same(b0.subs(instance), s.Matrix([1,-1,0])/4)
HH, qq = H.subs(instance), q.subs(instance)
ss = s.simplify(s.trace(HH*HH)+2*(qq.T*qq)[0])
assert ss == 1
assert 1+ss == 2
same(-2*HH+6*tf(HH.adjugate()-qq*qq.T),
     2*comm(L[2], comm(L[2], HH)))
same(2*L[2]*L[2]*qq, -2*qq)
print('PASS: original-coordinate maps, rational instance, couplings, and frequency')

# A full complex, noncommuting test quadruple, with no real-skew restriction.
I = s.I
C = L[0] + 2*L[1] + I*s.diag(1, -3, 2)
Z = [L[2] + I*s.Matrix([[0,1,2],[1,0,0],[2,0,0]]),
     2*L[0] - L[1] + I*s.diag(2, -1, -1),
     L[1] + I*s.Matrix([[1,0,1],[0,-1,3],[1,3,0]])]
for M in [C]+Z:
    zero(M.conjugate().T+M)
    assert s.trace(M) == 0
N = cross_matrix([1, 2, 3])
W = 2*N
R = (s.eye(3)+N/4)*(s.eye(3)-N/4).inv()
same(R.T*R, s.eye(3))
same(R*W, W*R)
assert R.det() == 1
Rd, Rdd = R*W, R*W*W


def mix(M, triplet):
    return [total(M[i,j]*triplet[j] for j in range(3)) for i in range(3)]


Y, Yd, Ydd = mix(R, Z), mix(Rd, Z), mix(Rdd, Z)
EE = [Yd[i]+comm(C,Y[i]) for i in range(3)]
EEcovd = [Ydd[i]+2*comm(C,Yd[i])+comm(C,comm(C,Y[i])) for i in range(3)]


def II(M):
    return inertia(M, HH, qq)


def KK(triplet, M):
    return -total(comm(NN, comm(NN, M)) for NN in triplet)


g2 = s.Rational(11, 7)
FHH = 2*comm(L[2], comm(L[2], HH))
rot_phi = comm(C,comm(C,HH))+KK(Z, HH)-FHH
time_phi = comm(C,comm(C,HH))+KK(Y, HH)-FHH
same(time_phi, rot_phi)
same((C*C-total(M*M for M in Y))*qq+2*qq,
     (C*C-total(M*M for M in Z))*qq+2*qq)
GW = total(W[i,j]*comm(Z[i],Z[j]) for i in range(3) for j in range(3))
same(total(comm(Y[i],Yd[i]) for i in range(3)), GW)
gauss = 2/g2*total(comm(Y[i],EE[i]) for i in range(3))+II(C)
gauss_reduced = II(C)+2/g2*KK(Z,C)+2/g2*GW
same(gauss, gauss_reduced)
Jtime = comm(HH,comm(C,HH))+qq*(C*qq).conjugate().T-(C*qq)*qq.T
same(tf(Jtime), -II(C))
for M in Y:
    Jspace = comm(HH,comm(M,HH))-qq*qq.T*M-M*qq*qq.T
    same(tf(Jspace), -II(M))
WZ, WWZ = mix(W,Z), mix(W*W,Z)
reduced_spatial = [WWZ[i]+2*comm(C,WZ[i])+comm(C,comm(C,Z[i]))
                   +KK(Z,Z[i])+g2*II(Z[i])/2 for i in range(3)]
time_spatial = [EEcovd[i]+KK(Y,Y[i])+g2*II(Y[i])/2 for i in range(3)]
for actual, expected in zip(time_spatial,mix(R,reduced_spatial)):
    same(actual, expected)
omega = s.symbols('omega', real=True)
Wz = omega*L[2]
same(total(Wz[i,j]*comm(Z[i],Z[j]) for i in range(3) for j in range(3)),
     -2*omega*comm(Z[0],Z[1]))
print('PASS: all rigid-rotation scalar, Gauss, current, and spatial equations')
print('ALL EXACT CHECKS PASSED; general complex SU(3) existence remains open.')
