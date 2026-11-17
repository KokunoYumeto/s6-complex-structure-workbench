"""Exact certificate for the nine spanning tube directions in D_3.

This is a finite list of nine explicitly defined integer matrices, not a
search.  The singular-value bound is proved symbolically for every real
line parameter; no sampled positivity or floating-point calculation is used.
"""
import sympy as s

t, a = s.symbols('t a', real=True)
I = s.eye(3)
e = [I[:, j] for j in range(3)]
vectors = e + [e[0]+e[1], e[0]+e[2], e[1]+e[2]]


def cross(w):
    x, y, z = w
    return s.Matrix([[0, -z, y], [z, 0, -x], [-y, x, 0]])


directions = []
for w in vectors:
    q = (w.T*w)[0]
    K = cross(w)
    Q = q*I-w*w.T
    A = Q+K
    assert K.T == -K
    assert Q*K == K*Q == q*K
    assert K*K == -Q
    assert A*A.T == A.T*A
    assert A*w == s.zeros(3, 1)
    assert s.factor((I+t*A).det()) == (q*q+q)*t*t+2*q*t+1
    # On Rw the squared singular value is 1. On its orthogonal
    # plane it is (1+q*t)^2+q*t^2, whose minimum is 1/(q+1).
    gram = (I+t*A).T*(I+t*A)
    transverse = (1+q*t)**2+q*t*t
    assert s.simplify(gram-(w*w.T/q+transverse*(I-w*w.T/q))) == s.zeros(3)
    completed = q*(q+1)*(t+s.Rational(1, q+1))**2+s.Rational(1, q+1)
    assert s.expand(transverse-completed) == 0
    assert q in [1, 2]
    directions.append(A)
    print('w =', list(w), 'A =', A.tolist(),
          'squared lower bound =', s.Rational(1, q+1))

for w in e:
    K = cross(w)
    assert (I+t*K).T*(I+t*K) == I-t*t*K*K
    assert s.factor((I+t*K).det()) == t*t+1
    directions.append(K)
    print('skew direction', K.tolist(), 'squared lower bound = 1')

coordinate_matrix = s.Matrix.hstack(*(s.Matrix(list(A)) for A in directions))
determinant = coordinate_matrix.det()
assert determinant != 0
assert coordinate_matrix.rank() == 9
assert s.Rational(1, 4)**2 < s.Rational(1, 3)
print('row-major direction matrix determinant =', determinant)
print('complex span dimension =', coordinate_matrix.rank())
print('uniform tube radius 1/4 < 1/sqrt(3): verified exactly')
print('All nine symbolic line certificates passed.')

# Exact canonical-frame identity used in the cusp completion.
N = s.zeros(6)
N[:3, 3:] = I
assert N*N == s.zeros(6) and N.rank() == 3
entries = s.symbols('c0:9')
C = s.Matrix(3, 3, entries)
graph_C = C.col_join(I)
assert (s.eye(6)+t*N)*graph_C == (C+t*I).col_join(I)
assert (s.eye(6)+N)*(s.eye(6)+t*N) == s.eye(6)+(t+1)*N
print('Cusp canonical frame: exp(tN) graph(C) = graph(C+tI), verified.')
print('Logarithm change t -> t+1 is cancelled by monodromy I+N.')
