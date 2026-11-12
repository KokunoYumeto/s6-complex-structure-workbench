"""Exact replay of the bounded invariant-sector jet counterexamples.

This program does not read or change canonical files.
"""
import sympy as sp

u = sp.Matrix([1, 1, 1])
b = sp.Matrix([1, -1, 0])
v = sp.Matrix([1, 1, -2])
D = sp.diag(1, -1, 0)
A = u * v.T + v * u.T
zero3 = sp.zeros(3)
zero_vector = sp.zeros(3, 1)

def contractions(Phi, b0, Phi_dot, b_dot):
    return tuple(sp.simplify(x[0]) for x in (
        u.T*b0,
        u.T*b_dot,
        u.T*Phi*b0,
        u.T*(Phi_dot*b0+Phi*b_dot),
        u.T*Phi_dot*b_dot,
    ))

assert contractions(D, b, zero3, zero_vector) == (0, 0, 2, 0, 0)
assert contractions(zero3, b, D, zero_vector) == (0, 0, 0, 2, 0)
assert contractions(zero3, b, A, v) == (0, 0, 0, 0, 18)
assert A == sp.Matrix([[2, 2, -1], [2, 2, -1], [-1, -1, -4]])
assert sp.trace(A) == 0 and A.T == A
assert A*b == zero_vector and A*v == 6*u
assert contractions(zero3, b, A/3, v) == (0, 0, 0, 0, 6)
assert (A/3)*v == 2*u

# Prove the trace-free adjugate identity by a fully variable Hermitian matrix.
p, q, r, x, y, z, h, k = sp.symbols('p q r x y z h k', real=True)
Phi = sp.Matrix([[p, x+sp.I*y, z+sp.I*h],
                 [x-sp.I*y, q, r+sp.I*k],
                 [z-sp.I*h, r-sp.I*k, -p-q]])
t = sp.trace(Phi*Phi)
assert sp.simplify(Phi.adjugate() - (Phi*Phi-t*sp.eye(3)/2)) == zero3

# The dimensions count actual original coordinates, without fixing scales.
assert tuple(d*d+(3-d)*(3-d)-1+2*d for d in (1, 2)) == (6, 8)
print('PASS: exact adjugate identity, dimensions (6,8), and three jet counterexamples.')
