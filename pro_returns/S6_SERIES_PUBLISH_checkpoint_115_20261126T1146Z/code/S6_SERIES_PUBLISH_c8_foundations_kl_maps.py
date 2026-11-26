"""Single symbolic verification of the explicit maps inserted in the KL unit.

This is exposed unit-revision arithmetic, with no historical module import.
"""
import sympy as s

k, n = s.symbols("k n", integer=True)
S = s.Matrix([[0,0,-1,0],[0,-1,1,1],[0,0,0,1],[-1,0,3,0]])
Sinv = s.Matrix([[-3,0,0,-1],[-1,-1,1,0],[-1,0,0,0],[0,0,1,0]])
U = s.Matrix([[0,-1,0,0],[1,-1,0,-3],[0,1,1,1],[0,0,0,1]])
MII = s.Matrix([[1,1,0,0],[-1,0,0,0],[0,0,1,0],[0,0,0,1]])
V = U.inv()*MII*U
A1 = s.Matrix([[1,0,0,0],[0,0,1,0],[-3,-1,-1,0],[-1,0,-1,1]])
A2 = s.Matrix([[1,0,0,0],[0,1,-1,0],[0,1,0,0],[0,0,0,1]])
assert S*Sinv == Sinv*S == s.eye(4)
assert U.inv().T*S == S*A1.inv().T
assert V.inv().T*S == S*A2.inv().T
assert U*Sinv.T == Sinv.T*A1 and V*Sinv.T == Sinv.T*A2
print("S inverse =", Sinv.tolist())
print("Both cohomological and homological period conjugacies, with inverse maps: exact.")
D = s.Matrix([[-1,1,0,1,0,0,0],[k,-k,3*k,0,0,0,-n],[0,0,0,-1,0,0,0],[0,0,1,0,0,0,0]])
U4 = s.Matrix([[1,0,1,0],[0,1,0,0],[0,0,0,1],[1,0,0,0]])
E = s.eye(7)
V7 = s.Matrix.hstack(E[:,1]-E[:,3], E[:,2], E[:,6], E[:,3], E[:,0]+E[:,1], E[:,4], E[:,5])
C = s.Matrix([[1,0,0],[-k,3*k,-n],[0,1,0]])
expected = s.zeros(4,7)
expected[:3,:3] = C
expected[3,3] = 1
assert U4*D*V7 == expected and abs(U4.det()) == abs(V7.det()) == 1
W = s.Matrix([[1,0,0],[0,0,1],[k,1,-3*k]])
assert W*C == s.diag(1,1,-n) and W.det() == -1
print("Full D target/source maps give C plus one unit and three zero columns: exact.")
print("W =", W.tolist(), "; W C =", (W*C).tolist())
a, b, c, q = s.symbols("a b c q", integer=True)
assert C*s.Matrix([a,c,-q]) == s.Matrix([a, -k*a+3*k*c+n*q, c])
print("Cyclic map (a,b,c) -> k a + b - 3k c mod n; inverse 1 -> (0,1,0).")
print("Kernel preimage for k a+b-3k c=nq is (a,c,-q): exact.")
print("No parameter grid or historical executable run; all identities are symbolic.")
