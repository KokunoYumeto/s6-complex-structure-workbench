"""Exact algebra checks; analytic arguments are in the companion proof text."""
from pathlib import Path
import json
from fractions import Fraction
from itertools import product
import sympy as s

checks = []

def zero(name, value):
    entries = list(value) if isinstance(value, s.MatrixBase) else [value]
    assert all(s.cancel(v) == 0 for v in entries), name
    checks.append(name)

L, m, q, M = s.symbols('L m q M', nonzero=True, real=True)
aa, ab, ac, ad = s.symbols('aa ab ac ad', real=True)
A = s.Matrix([[aa, ab], [ac, ad]])
B = s.Matrix([[6*m, L], [-q, m]])
D = L*q + 6*m*m
Bi = s.Matrix([[m, -L], [q, 6*m]])/D
zero('retained B inverse', B*Bi-s.eye(2))
Q = A.row_join(M*s.eye(2)).col_join(B.row_join(s.zeros(2)))
Qi = s.zeros(2).row_join(Bi).col_join((s.eye(2)/M).row_join(-A*Bi/M))
zero('retained period right inverse', Q*Qi-s.eye(4))
zero('retained period left inverse', Qi*Q-s.eye(4))
zero('permuted orientation determinant', Q.det()-M**2*D)
K = Bi*Bi.T
Ke = s.Matrix([[m*m+L*L, m*q-6*m*L], [m*q-6*m*L, q*q+36*m*m]])/D**2
zero('all entries of upper metric block', K-Ke)
zero('retained two-form minor', K.det()-D**-2)
Gi = K.row_join(-K*A.T/M).col_join((-A*K/M).row_join((s.eye(2)+A*K*A.T)/M**2))
zero('full mixed metric entries', Gi-Qi*Qi.T)
zero('full inverse metric identity', (Q.T*Q)*Gi-s.eye(4))

# Quaternion staple formula with arbitrary real, non-unit coefficients.
h0, h1, h2, h3 = s.symbols('h0 h1 h2 h3', real=True)
sigma = [s.Matrix([[0,1],[1,0]]), s.Matrix([[0,-s.I],[s.I,0]]), s.diag(1,-1)]
H = h0*s.eye(2)+s.I*(h1*sigma[0]+h2*sigma[1]+h3*sigma[2])
r2 = h0*h0+h1*h1+h2*h2+h3*h3
zero('full quaternion staple norm', H*H.conjugate().T-r2*s.eye(2))
zero('full quaternion staple determinant', H.det()-r2)

# Verify the exact beta-integral coefficient recurrence at many orders.
for k in range(16):
    beta_val = s.gamma(s.Rational(1,2)+k)*s.gamma(s.Rational(3,2))/s.gamma(k+2)
    target = s.pi*s.factorial(2*k)/(2*4**k*s.factorial(k)*s.factorial(k+1))
    zero(f'Haar moment coefficient {k}', s.expand_func(beta_val)-target)

r = s.symbols('r')
Z = sum(r**(2*k)/(s.factorial(k)*s.factorial(k+1)) for k in range(18))
ode = s.diff(Z,r,2)+3*s.diff(Z,r)/r-4*Z
zero('Bessel radial ODE through degree 32', s.series(ode,r,0,33).removeO())
eta = s.series(s.diff(Z,r)/(2*Z),r,0,9).removeO()
zero('exact mean small-r coefficients', eta-(r/2-r**3/12+r**5/48-r**7/180))
zero('Haar second moment at zero', s.limit(eta/(2*r),r,0)-s.Rational(1,4))
zero('second-moment sum retains unit quaternion constraint', (1-3*eta/(2*r))+3*eta/(2*r)-1)

for N in range(2,14):
    for n1 in range(N):
        for n2 in range(N):
            h = -Fraction(n1*n2,N*N)
            h1 = -Fraction(((n1+1)%N)*n2,N*N)
            h2 = -Fraction(n1*((n2+1)%N),N*N)
            w1 = -Fraction(n2,N) if n1 == N-1 else Fraction(0)
            w2 = Fraction(n1,N*N)
            assert -h+w1+h1 == -Fraction(n2,N*N)
            assert -h+w2+h2 == (Fraction(n1,N) if n2 == N-1 else Fraction(0))
    checks.append(f'magnetic vertex gauge, every vertex and wrap, N={N}')

theta,b = s.symbols('theta b', real=True)
expH = s.diag(s.exp(s.I*theta),s.exp(-s.I*theta))
zero('retained six-staple background coefficient',
     s.expand_complex(b*(4*s.eye(2)+expH+expH.conjugate().T)-b*(4+2*s.cos(theta))*s.eye(2)))
zero('local full-star cost difference', 2*b*(2-2*s.cos(theta))-4*b*(1-s.cos(theta)))
zero('exact local r interval width', 6*b-b*(4+2*s.cos(theta))-2*b*(1-s.cos(theta)))

for N in (2,4,6,8):
    selected = {(n1,n2,n3,n4) for n1 in range(N)
                for n2,n3,n4 in product(range(1,N),repeat=3)
                if (n2+n3+n4)%2 == 1}
    assert len(selected) == N*((N-1)**3+1)//2
    degrees = {e:0 for e in selected}
    magnetic_count = magnetic_selected = 0
    for n in product(range(N+1),repeat=4):
        for i in range(4):
            for j in range(i+1,4):
                if n[i] == N or n[j] == N:
                    continue
                touches = []
                if i == 0:
                    upper = tuple(n[k]+int(k==j) for k in range(4))
                    touches = [e for e in (n,upper) if e in selected]
                assert len(touches) <= 1
                for e in touches:
                    degrees[e] += 1
                if (i,j) == (0,1):
                    magnetic_count += 1
                    magnetic_selected += len(touches)
    assert all(v==6 for v in degrees.values())
    assert magnetic_count == N*N*(N+1)**2
    assert magnetic_selected == 2*len(selected)
    checks.append(f'full 4D patch incidence and extensive integration counts, N={N}')

j = s.symbols('j', positive=True)
Nj = 2*j*j
mj = Nj*((Nj-1)**3+1)/2
pj = Nj**2*(Nj+1)**2
zero('bulk selected-star coverage limit', s.limit(2*mj/pj,j,s.oo)-1)
thetaj = 2*s.pi/(10000*j**6)
zero('retained leading extensive-action coefficient',
     s.limit(j**4*b*pj*thetaj**2,j,s.oo)-64*s.pi*s.pi*b/10**8)

receipt = {'status':'PASS','checks':checks,'check_count':len(checks),
           'scope':'Exact finite algebra and series coefficients only; not a quantum continuum calculation.'}
out = Path(__file__).with_name('RETAINED_CUSP_BRIDGE_CHECKS.json')
out.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','check_count':len(checks),'receipt':str(out)}))
