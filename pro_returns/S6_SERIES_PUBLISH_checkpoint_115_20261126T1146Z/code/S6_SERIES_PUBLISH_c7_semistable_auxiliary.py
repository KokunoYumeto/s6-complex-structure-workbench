#!/usr/bin/env python3
"""Post-exposure L0 auxiliary identities, independent of all historical code.

Symbolic determinants establish the displayed identities for every integer
parameter. The two finite fan calculations exhibit one actual allowed row.
No source, frozen certificate or historical target program is loaded.
"""
from itertools import combinations, permutations
from sympy import Matrix, expand, symbols

a,b,m,x,y,z,n = symbols('a b m x y z n')
R=Matrix([[-a*y,a*x,b*n,-b*z,0],
          [m,0,0,0,x],[0,m,0,0,y],[0,0,0,m,n]])
q=Matrix([-x,-y,-z,-n,m])

def determinant(A):
    """Leibniz expansion, retaining every term as a polynomial."""
    size=len(A)
    total=0
    for p in permutations(range(size)):
        inversions=sum(p[i]>p[j] for i in range(size) for j in range(i+1,size))
        term=(-1)**inversions
        for i in range(size):
            term*=A[i][p[i]]
        total+=term
    return expand(total)

cof=[]
for omit in range(5):
    cols=[j for j in range(5) if j!=omit]
    A=[[R[i,j] for j in cols] for i in range(4)]
    cof.append(expand((-1)**omit*determinant(A)))
assert Matrix(cof)==b*m*m*n*q
assert R*q==Matrix.zeros(4,1)
print('SC7 signed maximal minors, in deleted-column order:')
for j,value in enumerate(cof):
    print('  column',j+1,':',value)
print('SC7 polynomial cofactor identity and R*q=0: PASS for all parameters.')
print('For n != 0 and b,m > 0 the last minor is b*m^3*n != 0.')
print('Primitive q gives gcd of all maximal minors b*m^2*abs(n).')
print('At n=0 all maximal minors vanish; no finite-order claim is inferred.')

B=Matrix([[b,0,0],[-a*y,m,0],[a*x,0,m]])
minors=[]
for rows in combinations(range(3),2):
    for cols in combinations(range(3),2):
        value=determinant([[B[i,j] for j in cols] for i in rows])
        minors.append(value)
        print('SC8 rows',rows,'columns',cols,':',value)
assert set(minors)=={0,b*m,-a*m*x,-a*m*y,m*m}
assert determinant(B.tolist())==b*m*m
print('SC8 entry ideal (b,m,a*x,a*y), minor ideal m*(b,m,a*x,a*y), determinant b*m^2.')
print('Bezout a*c+b*d=1 identifies these ideals with (b,m,x,y) and m*(b,m,x,y).')

C=Matrix([[2,1],[-7,-3]])
delta=C.inv()*Matrix([0,1])
assert C.det()==1 and delta==Matrix([-1,2])
first=Matrix([[0,1,0],[0,0,1],[1,1,1]])
second=Matrix([[1,1,0],[1,0,1],[1,1,1]])
physical=Matrix([*delta,0])
weights1=first.inv()*physical
weights2=second.inv()*physical
assert weights1==Matrix([-1,-1,2])
assert weights2==Matrix([1,-2,1])
assert first*weights1==physical and second*weights2==physical
print('OS47, selected I2, (a,b)=(7,1), kappa=1:')
print('  C=',C.tolist(),'C^-1=',C.inv().tolist(),'delta in short basis=',list(delta))
print('  first triangle weights=',list(weights1),'inverse ray map verified.')
print('  second triangle weights=',list(weights2),'inverse ray map verified.')
print('Both vertices are isolated fixed points; a nonzero coordinate of weight 2 has stabilizer Z/2.')
print('Post-exposure auxiliary identities: PASS. No historical algorithm was imported or executed.')
