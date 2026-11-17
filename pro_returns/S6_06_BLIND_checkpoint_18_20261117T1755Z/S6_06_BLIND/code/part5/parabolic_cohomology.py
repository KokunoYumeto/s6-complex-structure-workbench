import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from sympy.matrices.normalforms import smith_normal_form
T1=s.Matrix([[1,0,-6,2],[0,-1,1,1],[0,-1,0,1],[0,0,0,1]])
T2=s.Matrix([[1,6,0,-3],[0,0,-1,1],[0,1,0,0],[0,0,0,1]])
A1=T1.inv().T; A2=T2.inv().T; A0=(A1*A2).inv()
I=s.eye(4)
N1=sum((A1**i for i in range(3)),s.zeros(4))
N2=sum((A2**i for i in range(4)),s.zeros(4))
P=s.Matrix([[1,0,0,0],[0,1,0,0]])
C=s.diag(N1,N2).col_join(P.row_join(P*A1))
D,U,V=[x.to_Matrix() for x in smith_normal_decomp(DomainMatrix.from_Matrix(C).convert_to(s.ZZ))]
r=C.rank(); K=V[:,r:]
B=(A1-I).col_join(A2-I)
assert C*K==s.zeros(C.rows,K.cols)
assert C*B==s.zeros(C.rows,4)
coords=V.inv()*B
assert coords[:r,:]==s.zeros(r,4)
coords=coords[r:,:]
print('Norm1=',N1); print('Norm2=',N2); print('C=',C); print('Smith(C)=',D)
print('Unimodular V=',V); print('Integral kernel basis K=',K)
print('Principal cocycles B=',B); print('B coordinates in K=',coords); print('Smith(coords)=',smith_normal_form(coords,domain=s.ZZ))
print('rank cocycles=',K.cols,'rank coboundaries=',coords.rank())
