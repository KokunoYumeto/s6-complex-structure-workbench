"""An exact unbounded integral (5,4) family, before its affine/homology test.

All family identities are symbolic over Q[v]. Integer-valued half-polynomials
are checked by the two parity cases. The optional finite sample checks at
the end have the explicitly stated bound -6 <= v <= 10 and imply nothing
outside that range. Infinite conclusions use the symbolic proofs only.
"""
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
from math import prod

v, x, t = s.symbols('v x t')
I = s.eye(5)
A = s.zeros(5)
for j in range(5):
    A[(j+1) % 5, j] = 1
q = v*v-v+1
X = I[:, 0].row_join(I[:, 2]+v*I[:, 4])
Y = s.Matrix([[0, -q, -v*v, -1, v],
              [0, 1-v*q, -v*q, v*v-v, q]])
N = X*Y
C = (I+N)*A
B = A.inv()*(I-N)
zero = lambda M: M.applyfunc(s.expand) == s.zeros(*M.shape)
assert zero(Y*X)
assert zero(Y*(A+I).inv()*X-s.eye(2))
assert zero(N*N)
assert zero(A**5-I) and zero(C**4-I)
assert zero(A*B-I+N)
assert s.factor(C.charpoly(x).as_expr()) == (x-1)*(x+1)**2*(x*x+1)
# 2(A+I)^-1 X is integral, so the cokernel of Y is killed by 2.
assert all(s.denom(s.factor(e)) == 1 for e in 2*(A+I).inv()*X)
for parity in (0, 1):
    Ym = Y.subs(v, parity).applyfunc(lambda z: int(z) % 2)
    minors = [int(Ym[:, [i,j]].det()) % 2
              for i in range(5) for j in range(i+1,5)]
    assert 1 in minors
assert s.expand((Y*s.ones(5, 1))[0]+2*q) == 0
assert s.ones(1, 5)*X == s.Matrix([[1, v+1]])
H = Y*A*X
Hp = Y*A.inv()*X
d = s.factor(H.det())
dp = s.factor(Hp.det())
assert s.expand(d-(1-v*v*q)) == 0
assert s.expand(dp-(1+v*v*q)) == 0
assert s.factor(s.trace(A**2*C**2)) == v**5-v**4+3
pencil = ((I+t*N)*A).charpoly(x).as_expr()
expected = (1-t)*A.charpoly(x).as_expr()+t*C.charpoly(x).as_expr()
expected += t*(t-1)*x*x*(d*x-dp)
assert s.expand(pencil-expected) == 0
print('rank-five A (cycle):', A.tolist())
print('X:', X.tolist())
print('Y:', Y.tolist())
print('q:', q, 'd:', s.expand(d), 'dprime:', s.expand(dp))
print('trace A^2 C^2:', v**5-v**4+3)
print('primitive N: index divides 2, both parity cases have rank 2 mod 2')
print('global invariants vanish by Y*ones first entry = -2q')
print('global coinvariants vanish by ones^T*X=(1,v+1) and rank(Y)=2')

# A stable index-q overlattice removes the odd cusp extension index.
P = I.copy()
P[:, 0] = s.ones(5, 1)/q
An = (P.inv()*A*P).applyfunc(s.factor)
Bn = (P.inv()*B*P).applyfunc(s.factor)
assert all(s.denom(e) == 1 for e in An)
assert all(s.denom(e) == 1 for e in Bn)
ss = v*v+v-1
rr = -(v+1)*(v*v-2)/2
f = v**3-v-1
assert s.expand(ss*f+2*v*v*rr) == 1
for parity in (0, 1):
    assert int(((v+1)*(v*v-2)).subs(v, parity)) % 2 == 0
beta = s.Matrix([[ss, ss-v*rr, v*v*ss+v*rr, rr, -v*ss-rr]])
AA = s.diag(1, An)
BB = s.diag(1, Bn)
BB[0, 1:] = beta
NN = AA*BB-s.eye(6)
assert zero(AA**5-s.eye(6)) and zero(BB**4-s.eye(6))
assert zero(NN*NN)
assert zero(beta*(An*Bn-I))
print('overlattice basis P:', P.tolist())
print('integral An:', An.tolist())
print('integral Bn:', Bn.tolist())
print('integer-valued Bezout coefficients:', ss, rr)
print('rank-six extension row beta:', beta.tolist())
print('exact cusp extension identity s*(v^3-v-1)+2*v^2*r=1')

Xn=(P.inv()*X).applyfunc(s.factor)
Yn=(Y*P).applyfunc(s.factor)
z=s.Matrix([-v**3+v-1,0,0,2,2*(1-v*v)])
assert zero(Yn*z)
assert s.expand((beta*z)[0]-1)==0
assert Xn.extract([1,2],[0,1]).det()==-1
assert s.expand(z[0]-(1-2*((v**3-v+2)/2)))==0
print('primitive image basis Xnew:',Xn.tolist())
print('kernel vector z with beta*z=1:',list(z))

# Constant 2-primary lattice change returning v=0 to the original example.
L=s.Matrix([[-2,3,-5,-1,5,-3],[0,2,-2,2,-2,2],
 [0,-4,0,0,4,-4],[0,0,0,-4,4,-4],[0,0,4,-4,4,-4],
 [0,0,0,-4,4,0]])/4
assert L.det()==-s.Rational(1,4)
assert all(e.q==1 for e in L.inv())
At=(L.inv()*AA*L).applyfunc(s.expand)
Bt=(L.inv()*BB*L).applyfunc(s.expand)
assert all(c.q==1 for M in (At,Bt) for e in M for c in s.Poly(e,v).all_coeffs())
Nt=At*Bt-s.eye(6)
for parity in (0,1):
    Nm=Nt.subs(v,parity).applyfunc(lambda e:int(e)%2)
    assert any(int(Nm.extract(a,b).det())%2 for a in __import__('itertools').combinations(range(6),3)
               for b in __import__('itertools').combinations(range(6),3))
print('constant lattice matrix L:',L.tolist())
print('final A(v):',At.applyfunc(s.factor).tolist())
print('final B(v):',Bt.applyfunc(s.factor).tolist())
print('primitive final cusp: original lattice proof away from 2, both parities rank 3 mod 2')

# Explicit free affine lifts on the infinite subfamily v=20t.
seed=s.Matrix([1,3,-2,-1,2,0]); e0=s.eye(6)[:,0]
w1=sum((At.T**j*seed for j in range(5)),s.zeros(6,1))/5
w2=-sum((Bt.T**j*e0 for j in range(4)),s.zeros(6,1))/4
assert zero(At.T*w1-w1) and zero(Bt.T*w2-w2)
assert w1[0]==1 and w2[0]==-1
for w in (w1,w2):
    assert all(c.q==1 for e in w for c in s.Poly(s.expand(e.subs(v,20*t)),t).all_coeffs())
print('free affine lift vectors for v=20t:',w1.applyfunc(s.factor).tolist(),w2.applyfunc(s.factor).tolist())

# Odd global coinvariants: A identifies f0=5h and f1=...=f4=q h.
assert all(int(q.subs(v,k))%5 for k in range(5))
kappa=(s.Matrix([[5,q,q,q,q]])*(Bn-I)/q).applyfunc(s.factor)
assert s.expand(kappa[2]-kappa[1]-2*v)==0
assert s.expand(kappa[3]+f)==0
print('B relations in A-coinvariants, divided by q:',list(kappa))
print('gcd(kappa)=1: it divides gcd(2v,v^3-v-1)=1, since v^3-v-1 is odd')
print('raw global coinvariants are Z/q; the final lattice has odd part exactly Z/q')

def torsion_order(M):
    D = smith_normal_form(M, domain=ZZ)
    return prod(abs(int(D[j,j])) for j in range(min(D.shape)) if D[j,j])

print('Finite diagnostic sample only, -6<=v<=10:')
for value in range(-6, 11):
    nn = NN.subs(v, value)
    snf = smith_normal_form(nn, domain=ZZ)
    diagonal = list(snf.diagonal())
    assert [abs(int(e)) for e in diagonal if e] == [1, 1, 1]
    b = beta.subs(v, value)
    m = Bn.subs(v, value).T-I
    order = torsion_order(m)//torsion_order(m.row_join(b.T))
    print(value, 'cusp Smith', diagonal, 'order of finite B extension', order)
print('Symbolic family identities and the bounded diagnostics passed.')
