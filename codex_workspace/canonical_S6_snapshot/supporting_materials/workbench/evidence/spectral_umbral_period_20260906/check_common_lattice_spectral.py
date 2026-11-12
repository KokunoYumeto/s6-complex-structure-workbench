"""Exact checks of the retained common-lattice spectral bridge.

The manuscript proves the identities over every C_n subset of H.  Here I
is the formal standard generator of an isomorphic complex plane, and t is
retained as an independent real variable.  No floating-point test is used.
"""

import sympy as s


def check(name, expression):
    entries = list(expression) if isinstance(expression, s.MatrixBase) else [expression]
    residues = [s.expand_complex(s.expand(x)) for x in entries]
    assert all(s.simplify(x) == 0 for x in residues), (name, residues)
    print("PASS:", name)


a0, t, mu, z, h = s.symbols("a0 t mu z h", real=True)
root2, root3, root6 = s.sqrt(2), s.sqrt(3), s.sqrt(6)
eye = s.eye(3)
cycle = s.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
a = a0 + s.I*t
y = root2*(a*cycle + s.conjugate(a)*cycle**2)
x = mu*eye+y
q = a0**2+t**2
p = a0*(a0**2-3*t**2)
omega = -s.Rational(1, 2)+root3*s.I/2
eigenvalues = [2*root2*a0, -root2*a0-root6*t, -root2*a0+root6*t]
projectors = [(eye+omega**(-j)*cycle+omega**(-2*j)*cycle**2)/3 for j in range(3)]
projectors = [m.applyfunc(s.simplify) for m in projectors]

check("trace metric retains factor twelve", s.trace(y*y)-12*q)
check("full scalar-retaining determinant", x.det()-(mu**3-6*mu*q+4*root2*p))
check("characteristic polynomial", (z*eye-y).det()-(z**3-6*q*z-4*root2*p))
check("labelled eigenvalue polynomial", s.prod(z-v for v in eigenvalues)-(z**3-6*q*z-4*root2*p))
for i in range(3):
    check(f"Hermitian projector {i}", projectors[i].conjugate().T-projectors[i])
    check(f"projector trace {i}", s.trace(projectors[i])-1)
    check(f"eigenvalue equation {i}", y*projectors[i]-eigenvalues[i]*projectors[i])
    for j in range(3):
        check(f"orthogonal idempotents {i},{j}", projectors[i]*projectors[j]-(projectors[j] if i == j else s.zeros(3)))
check("sum of projectors", sum(projectors, s.zeros(3))-eye)
check("spectral reconstruction", sum((eigenvalues[j]*projectors[j] for j in range(3)), s.zeros(3))-y)
check("direction recovered with exact coefficient", -2*root3*s.im(projectors[1][0, 1])-1)
discriminant = s.prod((eigenvalues[i]-eigenvalues[j])**2 for i in range(3) for j in range(i+1, 3))
check("full discriminant coefficient 864", discriminant-864*t**2*(3*a0**2-t**2)**2)
check("cubic-radius discriminant", q**3-p**2-t**2*(3*a0**2-t**2)**2)
check("Cartan cubic coefficient", 3*root6*y.det()-24*root3*p)

for epsilon in (-1, 1):
    point = [-3*h-epsilon, h, h, h+epsilon]
    point_q = sum(v*v for v in point)
    point_p = point[0]*(point[0]**2-3*sum(v*v for v in point[1:]))
    check(f"line radius epsilon {epsilon}", point_q-(12*h*h+8*epsilon*h+2))
    check(f"line cubic epsilon {epsilon}", point_p-(6*h+2*epsilon))
point = [-3*h, h+1, h-1, h]
check("third-line radius", sum(v*v for v in point)-(12*h*h+2))
check("third-line cubic", point[0]*(point[0]**2-3*sum(v*v for v in point[1:]))-18*h)
print("All checks are exact symbolic identities. The proof covers the singular cases separately.")
