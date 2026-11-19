import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from sympy.matrices.normalforms import smith_normal_form
T1=s.Matrix([[1,0,-6,2],[0,-1,1,1],[0,-1,0,1],[0,0,0,1]])
T2=s.Matrix([[1,6,0,-3],[0,0,-1,1],[0,1,0,0],[0,0,0,1]])
A1=T1.inv().T; A2=T2.inv().T; I=s.eye(4)
N1=I+A1+A1**2; N2=I+A2+A2**2+A2**3
C=s.diag(N1,N2)
D,U,V=[a.to_Matrix() for a in smith_normal_decomp(DomainMatrix.from_Matrix(C).convert_to(s.ZZ))]
K=V[:,C.rank():]
P=s.Matrix([[1,0,0,0],[0,1,0,0]])
mapcusp=-P*I.row_join(A1)*K
B=(A1-I).col_join(A2-I)
BC=(V.inv()*B)[C.rank():,:]
print('K=',K); print('principal coords=',BC); print('Smith principal=',smith_normal_form(BC,domain=s.ZZ)); print('cusp map=',mapcusp); print('Smith cusp=',smith_normal_form(mapcusp,domain=s.ZZ))
# finite H2 computation in invariant bases
for name,A,N in [('A1',A1,N1),('A2',A2,N2)]:
 D,U,V=[a.to_Matrix() for a in smith_normal_decomp(DomainMatrix.from_Matrix(A-I).convert_to(s.ZZ))]
 K=V[:,(A-I).rank():]; NC=(V.inv()*N)[(A-I).rank():,:]
 print(name,'inv basis=',K,'norm coords=',NC,'Smith=',smith_normal_form(NC,domain=s.ZZ))
