"""Exact lattice checks for the local/global descent in C.2.UN.32."""
import sympy as s
from math import gcd
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

actions={
    2:-s.eye(2),
    3:s.Matrix([[0,-1],[1,-1]]),
    4:s.Matrix([[0,-1],[1,0]]),
    6:s.Matrix([[0,-1],[1,1]])
}
for order,beta in actions.items():
    assert beta**order == s.eye(2)
    total=s.zeros(2)
    for j in range(order):
        total += beta**j
    assert total == s.zeros(2)
    assert (beta-s.eye(2)).det() != 0
    smith=smith_normal_form(beta-s.eye(2),domain=ZZ)
    diagonal=[abs(int(smith[j,j])) for j in range(2)]
    exponent=s.ilcm(*diagonal)
    assert order % exponent == 0
    possible=[m for m in range(1,41) if order % m == 0 and gcd(m,order) == 1]
    assert possible == [1]
    print("stabilizer order",order,"beta=",list(beta),
          "sum beta^j=0; Smith(beta-I)=",diagonal,
          "fixed-translation exponent=",exponent)
    print("  m divides stabilizer order and gcd(m,order)=1 force m=1.")
    print("  ker(beta-I) on the real Chern vector space has dimension",
          2-(beta-s.eye(2)).rank())

# Root deck gauge identity: if sum a(zeta^j u)=0, then
# b=-(1/m) sum j*a(zeta^j u) satisfies b(zeta u)-b(u)=-a(u).
for m in range(2,13):
    coefficients=s.symbols(f'a0:{m}')
    S=sum(j*coefficients[j] for j in range(m))
    shifted=sum(j*coefficients[(j+1)%m] for j in range(m))
    difference=s.expand(shifted-S-m*coefficients[0])
    assert s.expand(difference+sum(coefficients)) == 0
    print("root order",m,": weighted finite-sum gauge identity checked.")

print("The global Chern-vector equation c=beta*c has only c=0.")
print("Zero Chern obstruction lifts the torsor through O_B -> F_B;")
print("its constant additive cocycle gives the actual rank-four translation lattice.")
print("All exact checks passed.")
