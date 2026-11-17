"""Independent exact finite-band correction; no source matrix is imported."""
from itertools import combinations
from sympy import Matrix, eye, ZZ
from sympy.matrices.normalforms import smith_normal_form
A1=Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
triples=list(combinations(range(4),3))
def wedge3(A):return Matrix([[A.extract(i,j).det() for j in triples] for i in triples])
b=Matrix([1,0,0,0]);c1=Matrix([0,-4,-2,1]);c2=Matrix([0,-3,-3,1])
assert wedge3(A1.T)*b==b and wedge3(A1.T)*c1==c1
assert wedge3(A2.T)*b==b and wedge3(A2.T)*c2==c2
alpha=Matrix.vstack(b.T,c1.T,-2*b.T,-c2.T)
snf=smith_normal_form(alpha,domain=ZZ)
assert [abs(snf[i,i]) for i in range(4)]==[1,1,1,0]
assert alpha*Matrix([0,1,1,6])==Matrix.zeros(4,1)
print('alpha3=',alpha.tolist())
print('Smith diagonal:',[snf[i,i] for i in range(4)])
print('All exterior-invariance, kernel, and integral-image checks passed.')
