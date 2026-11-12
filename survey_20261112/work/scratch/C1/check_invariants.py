# Sanity checks for C1 notes: monodromy invariants of Lambda (basis gamma,u,w,delta), columns = images.
import sympy as s, itertools
A1 = s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2 = s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
M0 = s.Matrix([[1,0,0,0],[0,1,0,0],[0,1,1,0],[-1,0,0,1]])
I = s.eye(4)
print("A1^3==I", A1**3==I, "A2^4==I", A2**4==I, "A1*A2*M0==I", A1*A2*M0==I)
print("A2*A1 =", (A2*A1).tolist())
# invariant vectors (integral): common kernel of A1-I, A2-I
K = (A1-I).col_join(A2-I)
print("invariant vectors Lambda^Delta:", [list(v) for v in K.nullspace()])
# invariant covectors: row vectors c with c*A = c
Kc = (A1.T-I).col_join(A2.T-I)
print("invariant covectors:", [list(v) for v in Kc.nullspace()])
# mod 2 invariant covectors
inv2=[c for c in itertools.product(range(2),repeat=4)
      if all(((s.Matrix([c])*A - s.Matrix([c])).applyfunc(lambda x:x%2))==s.zeros(1,4) for A in (A1,A2))]
print("mod-2 invariant covectors:", inv2)
# H^3(F;Z)=Lambda via kappa_v(a,b,c)=det(v,a,b,c); evaluate invariant v on L=<u,w,delta>
e=[I[:,i] for i in range(4)]
for v in K.nullspace():
    print("kappa_v on L-torus:", s.Matrix.hstack(v,e[1],e[2],e[3]).det(), " on <gamma,w,delta>:", s.Matrix.hstack(v,e[0],e[2],e[3]).det())
# M0 - I image
print("im(M0-I) columns:", (M0-I).columnspace())
