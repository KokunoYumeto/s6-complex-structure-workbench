"""Exact rational boundary maps for all admissible (3,4) translations.

The topological identifications of these matrices are proved in B3.3.
This script verifies the integer exterior-power calculations, rather
than inferring topology from numerical ranks alone.
"""
from itertools import combinations
from pathlib import Path
from sympy import Matrix, Rational, eye, simplify, symbols

root = Path(__file__).resolve().parents[1]
lines = []
def show(label, value):
    line = f"{label}: {value}"
    lines.append(line)
    print(line)

A1 = Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2 = Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
M0 = (A1*A2).inv()
pairs = list(combinations(range(4), 2))
def exterior2(A):
    return Matrix([[A.extract(list(I), list(J)).det() for J in pairs]
                   for I in pairs])

gamma = Matrix([[1,0,0,0]])
psi1 = Matrix([[0,2,1,3]])
psi2 = Matrix([[0,1,1,2]])
eta = Matrix([[0,0,6,1,0,0]])
gamma_psi1 = Matrix([[2,1,3,0,0,0]])
gamma_psi2 = Matrix([[1,1,2,0,0,0]])
assert gamma*A1 == gamma and gamma*A2 == gamma
assert psi1*A1 == psi1 and psi2*A2 == psi2
assert eta*exterior2(A1) == eta and eta*exterior2(A2) == eta
assert gamma_psi1*exterior2(A1) == gamma_psi1
assert gamma_psi2*exterior2(A2) == gamma_psi2
for i, A in enumerate((A1,A2), 1):
    assert 4-(A-eye(4)).rank() == 2
    assert 6-(exterior2(A)-eye(6)).rank() == 2
    show(f"A{i} invariant H1 and H2 dimensions", (2,2))

alpha1 = gamma.col_join(psi1).col_join(-gamma).col_join(-psi2)
alpha2 = gamma_psi1.col_join(eta).col_join(-gamma_psi2).col_join(-eta)
nu0 = Matrix([0,-1,-1,1])
assert alpha1.rank() == 3 and alpha1*nu0 == Matrix.zeros(4,1)
assert alpha2.rank() == 3
assert Matrix([[0,1,0,1]])*alpha2 == Matrix.zeros(1,6)
show("alpha1 in the transfer-normalized bases", alpha1)
show("alpha1 rank and kernel", (alpha1.rank(), nu0))
show("alpha2 in the transfer-normalized bases", alpha2)
show("alpha2 rank and cokernel functional", (alpha2.rank(), Matrix([[0,1,0,1]])))
show("H1(U), H2(U) rational dimensions", (1,2))

w = Matrix([0,0,1,0]); delta = Matrix([0,0,0,1])
assert (eye(4)-A1.inv())*w == -nu0
assert (eye(4)-A1.inv())*delta == Matrix.zeros(4,1)
assert (M0-eye(4)).rank() == 2
show("M0", M0)
show("H1(M) dimension from the Wang sequence", 4-(M0-eye(4)).rank()+1)
show("Mayer-Vietoris boundary of xi_w", (eye(4)-A1.inv())*w)
show("Mayer-Vietoris boundary of xi_delta", (eye(4)-A1.inv())*delta)
# Left contraction by the delta-coordinate vector in eta.
skew = Matrix.zeros(4)
for coefficient, (i,j) in zip(eta, pairs):
    skew[i,j] = coefficient
    skew[j,i] = -coefficient
contraction = delta.T*skew
assert contraction == -6*gamma
show("i_delta eta", contraction)

l0,l1,l2 = symbols('l0 l1 l2', integer=True)
p = 12*l0-4*l1-3*l2
relation = Matrix([[3,-l1],[4,l2-4*l0]])
assert simplify(relation.det()+p) == 0
meridian = l0-Rational(1,3)*l1-Rational(1,4)*l2
assert simplify(meridian-p/12) == 0
boundary = Matrix([[-1,0],[0,-p/2]])
assert simplify(boundary.det()-p/2) == 0
show("fundamental-group relation matrix", relation)
show("fundamental-group determinant", relation.det())
show("Theta(toric meridian)", meridian)
show("normalized two-cycle boundary matrix", boundary)
show("normalized two-cycle determinant", boundary.det())

count = 0
for a in range(-2,3):
    for b in range(-5,6):
        for c in range(-5,6):
            if b % 3 == 0 or c % 2 == 0:
                continue
            pv = p.subs({l0:a,l1:b,l2:c})
            assert pv != 0
            assert boundary.subs({l0:a,l1:b,l2:c}).rank() == 2
            count += 1
show("additional admissible exact examples checked", count)
show("Euler number of W from its normalization strata", 6-3*2+2)
show("rational Betti numbers of each base X", (1,0,0,0,0,0,1))
(root/'outputs/b_topology.txt').write_text('\n'.join(lines)+'\n')
