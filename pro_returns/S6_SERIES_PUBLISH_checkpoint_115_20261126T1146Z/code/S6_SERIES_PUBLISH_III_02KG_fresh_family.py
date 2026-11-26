#!/usr/bin/env python3
"""Fresh exact identities for the statement-first 02KG derivation.

No manuscript, earlier program, earlier output or target proof is read.
The geometric freeness, compactness, gluing and transport arguments are
proved in the accompanying derivation; they are not inferred from this
symbolic calculation.
"""
import json
import sympy as s

d, n, k = s.symbols('d n k', integer=True)
c, beta, mu, tau = s.symbols('c beta mu tau')
l0, l1, l2, k2 = s.symbols('l0 l1 l2 k2', integer=True)
I4 = s.eye(4)
gam, u, w, delta = [I4[:,j] for j in range(4)]
gamma = gam.T
A1 = s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2 = s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
A0 = (A1*A2).inv()
eps1 = s.Matrix([1,2,-4,0])
eps2 = s.Matrix([1,3,-3,0])
assert A1**3 == I4 and A2**4 == I4
assert A1*eps1 == eps1 and A2*eps2 == eps2
for A in [A1,A2,A0]:
    assert A*delta == delta and gamma*A == gamma

Pi = s.Matrix([[6*mu,tau,1,0],[beta+c,mu,0,1]])
Sn = I4+n*delta*gamma
assert Pi.subs(c,c+n) == Pi*Sn
assert Sn.det() == 1
for A in [A1,A2,A0]:
    assert Sn*A == A*Sn

r1 = n*d*(u+w)/3
r2 = -n*d*(u+w)/4
L1 = n*d*w
L2 = -n*d*u/2
assert (I4-A1)*r1 == -n*d*delta/3+L1
assert (I4-A2)*r2 == n*d*delta/4+L2
assert gamma*r1 == s.zeros(1,1) and gamma*r2 == s.zeros(1,1)
assert (Pi*r1).diff(c) == s.zeros(2,1)
assert (Pi*r2).diff(c) == s.zeros(2,1)
L12 = L1+A1*L2
Lzero = -A0*L12
q = s.Matrix([3*n*d/2,-n*d/2])
assert L12 == 3*n*d*w/2-n*d*delta/2
assert Lzero == -3*n*d*w/2+n*d*delta/2
assert Pi*Lzero == -q
for col in [L1,L2,Lzero]:
    assert gamma*col == s.zeros(1,1)
    assert (Pi*col).diff(c) == s.zeros(2,1)
for entry in list(L1)+list(L2)+list(Lzero)+list(q):
    assert s.simplify(entry.subs(n,2*k)).is_integer is True

# The additive corrections are exactly minus d times the standard ones.
standard = [-n*(u+w)/3, n*(u+w)/4, -n*w, n*u/2,
            s.Matrix([-3*n/2,n/2])]
canonical = [r1,r2,L1,L2,q]
assert all(a == -d*b for a,b in zip(canonical,standard))
h = s.symbols('h', integer=True)
assert all((a.subs(n,2*h)+a.subs(n,2*k)-a.subs(n,2*(h+k)))
           .applyfunc(s.simplify) == s.zeros(a.rows,a.cols)
           for a in canonical)

B0 = s.Matrix([[0,1],[-1,0]])
assert B0.T*B0 == s.eye(2) and B0.det() == 1
v1,v2 = s.symbols('v1 v2', integer=True)
ray = lambda a,b:s.Matrix([a,b,1])
tri_a = s.Matrix.hstack(ray(v1,v2),ray(v1+1,v2),ray(v1,v2+1))
tri_b = s.Matrix.hstack(ray(v1+1,v2),ray(v1,v2+1),ray(v1+1,v2+1))
assert tri_a.det() == 1 and tri_b.det() == -1
fan_shift = s.eye(3)
fan_shift[:2,2] = q
assert fan_shift.det() == 1
assert fan_shift*ray(v1,v2) == ray(v1+q[0],v2+q[1])

p = 12*l0-4*l1-3*l2
assert p.subs({l0:0,l1:-d,l2:d}) == d
assert s.expand(p-l2) == 4*(3*l0-l1-l2)
assert s.expand(p+l1) == 3*(4*l0-l1-l2)
assert s.simplify(s.exp(-2*s.pi*s.I*k2)) == 1
assert s.exp(3*s.log(6)) == 216
assert 216**2 == 46656

def arr(matrix):
    return [[str(s.factor(x)) for x in row] for row in matrix.tolist()]

print(json.dumps({
 'scope':'Fresh pre-target-proof identities; no earlier file or output read.',
 'monodromy_orders':[3,4], 'A0':arr(A0),
 'canonical_p':'d', 'admissible_residues':{'mod2':'l2','mod3':'-l1'},
 'integer_period_shift':arr(Sn),
 'period_shift_identity':'Pi(c+n)=Pi(c) S_n; det(S_n)=1; [S_n,A_j]=0',
 'finite_correction_entries':[arr((I4-A1)*r1),arr((I4-A2)*r2)],
 'finite_period_translations':[arr(Pi*r1),arr(Pi*r2)],
 'L1_plus_A1L2':arr(L12), 'cusp_cocycle_L0':arr(Lzero),
 'cusp_fan_translation':arr(q), 'cusp_period_identity':'Pi(c) L0=-q_n',
 'even_shift_corrections_integral':True,
 'canonical_equals_minus_d_times_standard':True,
 'additive_even_shift_law':True,
 'B0_orthogonal_unimodular':True,
 'two_triangle_determinants':[1,-1],
 'fan_translation_determinant':1,
 'moduli_identity':'W^2=u for integer k2',
 'parameter_radii':{'W':216,'u':46656},
 'geometric_steps':'Proved in the written derivation, not tested by parameter sampling.'
}, indent=2))
