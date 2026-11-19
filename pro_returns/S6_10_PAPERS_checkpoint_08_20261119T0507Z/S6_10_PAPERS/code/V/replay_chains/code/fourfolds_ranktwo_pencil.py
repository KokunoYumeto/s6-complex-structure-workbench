"""Exact rank-two characteristic-pencil invariants of the (5,4) quotient.

No search is performed. The symbolic parameter identity is checked as a
polynomial, and the two determinant invariants are computed over Q.
"""
from sympy import Matrix, eye, zeros, symbols, factor

A = Matrix([[1,-1,-1,1,0],[1,0,-1,0,0],
            [2,-1,-1,0,1],[2,0,-1,0,0],[1,1,-1,0,0]])
B = Matrix([[0,-1,0,1,0],[0,-1,0,0,1],
            [0,-1,0,0,0],[1,-1,0,0,0],[0,-1,1,0,0]])
C = B.inv()
N = C*A.inv()-eye(5)
assert N*N == zeros(5) and N.rank() == 2
assert A**5 == eye(5) and C**4 == eye(5)
V = Matrix.hstack(*N.columnspace())
H = V.gauss_jordan_solve(N*A*V)[0]
Hp = V.gauss_jordan_solve(N*A.inv()*V)[0]
assert H.trace() == -1 and Hp.trace() == 1
d, dp = H.det(), Hp.det()
x, t = symbols('x t')
f = A.charpoly(x).as_expr()
g = C.charpoly(x).as_expr()
actual = ((eye(5)+t*N)*A).charpoly(x).as_expr()
expected = (1-t)*f+t*g+t*(t-1)*x*x*(d*x-dp)
assert factor(actual-expected) == 0
print('A characteristic polynomial', factor(f))
print('C characteristic polynomial', factor(g))
print('image basis', V.tolist())
print('H=NA on image', H.tolist(), 'trace', H.trace(), 'det', d)
print('Hprime=NAinverse on image', Hp.tolist(), 'trace', Hp.trace(), 'det', dp)
print('rank-two pencil', factor(actual))
print('coefficient of t(t-1)', factor(x*x*(d*x-dp)))
print('All polynomial and lattice-independent invariants verified exactly.')
