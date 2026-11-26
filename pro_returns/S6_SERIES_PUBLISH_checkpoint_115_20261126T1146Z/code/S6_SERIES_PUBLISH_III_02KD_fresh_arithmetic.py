#!/usr/bin/env python3
"""Fresh KD arithmetic from the released defining matrices, never old programs.

The proof supplies the geometric maps.  This program verifies the displayed
integral identities, including explicit image and quotient inverse certificates.
Attribution: GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical reasoning effort
not separately exposed; fourth continuation, fresh Euler role.
"""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import sympy as S

d = S.symbols('d', integer=True, positive=True)
k1, k2 = S.symbols('k1 k2', integer=True)
l0, l1, l2 = S.symbols('l0 l1 l2', integer=True)
I4 = S.eye(4)
A1 = S.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2 = S.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
e = [I4[:,i] for i in range(4)]
eps1 = S.Matrix([1,2,-4,0])
eps2 = S.Matrix([1,3,-3,0])
p0 = 12*l0-4*l1-3*l2
a1 = 4*l0-l1-l2
a2 = l1+l2-3*l0

def check_zero(M):
    assert all(S.expand(x) == 0 for x in M)

def show(label, M):
    print(label)
    print(M)

def wedge_matrix(A):
    pairs = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
    return S.Matrix([[A[i,k]*A[j,l]-A[i,l]*A[j,k]
                      for k,l in pairs] for i,j in pairs])

def form_value(c, x, y):
    pairs = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
    return S.expand(sum(c[n]*(x[i]*y[j]-x[j]*y[i])
                        for n,(i,j) in enumerate(pairs)))

def cup(c, b):
    return S.expand(c[0]*b[5]+c[5]*b[0]-c[1]*b[4]-c[4]*b[1]
                    +c[2]*b[3]+c[3]*b[2])

print('Fresh 02KD exact integral arithmetic')
print('Inputs: released A1,A2, finite affine translations, cusp period lattice.')
print('No target proof, old computational program, or old result was read.')
check_zero(A1**3-I4)
check_zero(A2**4-I4)
check_zero(A1*eps1-eps1)
check_zero(A2*eps2-eps2)
N1 = I4+A1+A1**2
N2 = I4+A2+A2**2+A2**3
check_zero(N1*e[0]-3*eps1)
check_zero(N2*e[0]-4*eps2)
assert S.expand(3*a1-l1-p0) == 0
assert S.expand(4*a2-l2+p0) == 0
assert S.expand(a1+a2-l0) == 0
show('N1 gamma =', N1*e[0])
show('N2 gamma =', N2*e[0])
show('A1 A2, cusp positive-q linear action =', A1*A2)

L = S.diag(d,1,1,1)
Ad = [L.inv()*A1*L, L.inv()*A2*L]
alpha1 = S.Matrix([2,1,3,0,0,0])
alpha2 = S.Matrix([1,1,2,0,0,0])
Q = S.Matrix([0,0,6*d,1,0,0])
bet = 2*alpha2
C2form = alpha2+Q
for j,(A,alpha) in enumerate(zip(Ad,[alpha1,alpha2]),1):
    fixed = wedge_matrix(A).T-S.eye(6)
    check_zero(fixed*alpha)
    check_zero(fixed*Q)
    rr, pivots = fixed.rref()
    assert len(pivots) == 4
    show(f'A{j} in (d gamma,u,w,delta) =', A)
    show(f'RREF of fixed 2-form equations, coefficient order gu,gw,gd,uw,ud,wd =', rr)
    B = S.Matrix.hstack(alpha,Q)
    G = S.Matrix([[cup(B[:,i],B[:,j]) for j in range(2)] for i in range(2)])
    show(f'Full invariant 2-form lattice Gram matrix {j} =', G)
    assert S.expand(G.det()) == (-9 if j == 1 else -4)

G1 = S.Matrix([[cup(x,y) for y in [alpha1,Q]] for x in [alpha1,Q]])/3
G2 = S.Matrix([[cup(x,y) for y in [bet,C2form]] for x in [bet,C2form]])/4
assert G1.det() == -1 and G2.det() == -1
show('Finite H2 Gram matrix 1 for orientation induced by the ordered real lattice =', G1)
show('Finite H2 Gram matrix 2 for orientation induced by the ordered real lattice =', G2)
print('The complex orientations give the negatives of these Gram matrices:')
print('det_R(Pi_c)=Im(tau)*(Im(beta_c)-6*Im(mu)^2/Im(tau))<0.')

M2 = S.Matrix([[2,1,3,0,0,0],
               [0,0,6*d,1,0,0],
               [-2,-2,-4,0,0,0],
               [-1,-1,-2-6*d,-1,0,0]])
N = S.Matrix([[1,0,0],[0,1,0],[0,0,2],[0,-1,1]])
K = S.Matrix([[2,1,3,0,0,0],[0,0,6*d,1,0,0],[-1,-1,-2,0,0,0]])
J = S.Matrix([[1,0,1],[-1,0,-2],[0,0,0],[0,1,0],[0,0,0],[0,0,0]])
lam = S.Matrix([[0,2,-1,2]])
h = S.Matrix([0,0,-1,0])
P = S.Matrix([[1,0,0,0],[0,1,0,0],[0,1,0,1]])
check_zero(M2-N*K)
check_zero(N-M2*J)
check_zero(lam*N)
check_zero(I4-h*lam-N*P)
assert (lam*h)[0] == 1
show('MV H2 map (q1_*,-q2_*) =', M2)
show('Primitive image basis N =', N)
show('M2=N*K certificate K =', K)
show('N=M2*J certificate J =', J)
show('Integral cokernel coordinate lambda =', lam)
show('Cokernel inverse generator h =', h)
show('I-h*lambda=N*P certificate P =', P)

for sign in [1,-1]:
    p = sign*d
    nu1 = S.Matrix([-sign,-2*p,4*p,k1])
    nu2 = S.Matrix([sign,3*p,-3*p,k2])
    P1 = S.Matrix([[-3*sign,0,0,0],[3*sign*k1,2,1,3]])
    P2 = S.Matrix([[4*sign,0,0,0],[-2*sign*k2,1,1,2]])
    check_zero(P1*(Ad[0]-I4))
    check_zero(P2*(Ad[1]-I4))
    check_zero(P1*nu1-S.Matrix([3,0]))
    check_zero(P2*nu2-S.Matrix([4,0]))
    M1 = P1.col_join(-P2)
    Nsmall = S.Matrix([[0,0,3],[1,0,0],[0,0,4],[0,1,0]])
    Ksmall = S.Matrix([[3*sign*k1,2,1,3],[2*sign*k2,-1,-1,-2],[-sign,0,0,0]])
    Jsmall = S.Matrix([[0,0,-sign],[1,1,3*k1+2*k2],[-1,-2,-3*k1-4*k2],[0,0,0]])
    pi = S.Matrix([[4,0,-3,0]])
    z0 = S.Matrix([1,0,1,0])
    Psmall = S.Matrix([[0,1,0,0],[0,0,0,1],[-1,0,1,0]])
    b = S.Matrix([0,1,1,-1])
    check_zero(M1-Nsmall*Ksmall)
    check_zero(Nsmall-M1*Jsmall)
    check_zero(I4-z0*pi-Nsmall*Psmall)
    check_zero(M1*b)
    assert M1.rank() == 3 and (pi*z0)[0] == 1
    T1 = S.Matrix([form_value(alpha1,nu1,e[3])/3,
                   form_value(Q,nu1,e[3])/3])
    T2 = S.Matrix([form_value(bet,nu2,e[3])/4,
                   form_value(C2form,nu2,e[3])/4])
    delta_image = S.expand((lam*T1.col_join(T2))[0])
    assert delta_image == -p
    R = S.Matrix([[0,-p],[1,0]])
    assert R.det() == p
    show(f'For sign(p)={sign}: nu1,nu2 =', S.Matrix.hstack(nu1,nu2))
    show('H1 finite fibre pushforward 1 =', P1)
    show('H1 finite fibre pushforward 2 =', P2)
    show('H1 MV map =', M1)
    show('Primitive H1 image basis =', Nsmall)
    show('H1 image preimages J =', Jsmall)
    show('Kernel generator b =', b)
    show('H1 quotient coordinate, inverse =', (pi,z0))
    show('Finite (t1,delta) torus coordinates =', T1)
    show('Finite (t2,delta) torus coordinates =', T2)
    print('Their actual H2(U) coordinate =',delta_image)
    show('Cusp relative H3 to H2(U), bases ((q,w),(q,delta)) and (h,z) =',R)

a = S.Matrix([0,-1,-1,1])
b1 = S.Matrix([0,1,-2,0])
b2 = S.Matrix([0,-1,1,0])
check_zero(a-2*b1-3*b2-e[3])
show('Integral delta nullhomology identity a-2 b1-3 b2 =',a-2*b1-3*b2)

# On the toric cover use the ordered cocharacters (w,delta,q).
Gu = S.Matrix([[1,0,1],[0,1,0],[0,0,1]])
Gdg = S.Matrix([[1,0,0],[0,1,-d],[0,0,1]])
pairs3 = [(0,1),(0,2),(1,2)]
def wedge3(A):
    return S.Matrix([[A[i,k]*A[j,l]-A[i,l]*A[j,k]
                      for k,l in pairs3] for i,j in pairs3])
show('Period action of u on H2(T), order w-delta,w-q,delta-q =', wedge3(Gu))
show('Period action of d gamma on H2(T) =', wedge3(Gdg))
rel = (wedge3(Gu)-S.eye(3)).row_join(wedge3(Gdg)-S.eye(3))
assert rel.rank() == 1
assert any(abs(x) == 1 for x in rel[0,:])
assert all(x == 0 for x in rel[1:,:])
show('Coinvariant relation matrix, killing exactly w wedge delta =', rel)

print('All exact assertions passed.')
print('Completed UTC:', datetime.now(timezone.utc).isoformat())
print('Program SHA256:', sha256(Path(__file__).read_bytes()).hexdigest())
