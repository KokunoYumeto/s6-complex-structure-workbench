"""Exact covering-lattice and Mayer--Vietoris certificates for D.1."""
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
from itertools import combinations
from math import gcd
T1=s.Matrix([[1,0,-6,2],[0,-1,1,1],[0,-1,0,1],[0,0,0,1]])
T2=s.Matrix([[1,6,0,-3],[0,0,-1,1],[0,1,0,0],[0,0,0,1]])
A1=T1.inv().T; A2=T2.inv().T
r=s.symbols('d',integer=True,positive=True)
D=s.diag(r,1,1,1)
for A,m in [(A1,3),(A2,4)]:
    print('Cover monodromy:',D.inv()*A*D)
    print('Norm of gamma:',sum([A**j for j in range(m)],s.zeros(4))[:,0])
A=s.Matrix([[2,1,3,0,0,0],[-4*r,-2*r,0,1,0,0],[-2,-2,-4,0,0,0],[3*r,3*r,0,-1,0,0]])
Phi=s.Matrix([[4*r,2,3*r,2]])
assert Phi*A==s.zeros(1,6)
print('alpha_2:',A)
print('Primitive dual (d odd):',Phi)
minors=[s.factor(A.extract(i,j).det()) for i in combinations(range(4),3) for j in combinations(range(6),3)]
print('Distinct nonzero maximal minors:',sorted({str(x) for x in minors if x!=0}))
print('Universal-cover test cases:')
for l0,l1,l2 in [(0,1,-1),(0,2,-1),(0,1,1),(1,1,-1),(0,5,-1),(0,4,1),(2,1,-1),(1,2,-1)]:
    p=12*l0-4*l1-3*l2; d=abs(p)
    assert gcd(d,6)==1
    h1=(l1*pow(3,-1,d))%d if d>1 else 0
    h2=(l2*pow(4,-1,d))%d if d>1 else 0
    a0=(l0-h1-h2)//d; a1=(l1-3*h1)//d; a2=(l2-4*h2)//d
    assert 12*a0-4*a1-3*a2==p//d
    AA=A.subs(r,d)
    b=s.Matrix([a1-3*a0,0,a2,0])
    aug=AA.row_join(b)
    sf=smith_normal_form(aug,domain=ZZ)
    diag=[abs(int(sf[i,i])) for i in range(4)]
    assert diag==[1,1,1,d]
    assert int((Phi.subs(r,d)*b)[0])==-p
    print({'l':(l0,l1,l2),'p':p,'d':d,'cover_l':(a0,a1,a2),'sweep':list(b),'SNF':diag,'H2_free':d-1,'H2_torsion':d,'H3_torsion':d})
print('All assertions passed.')
