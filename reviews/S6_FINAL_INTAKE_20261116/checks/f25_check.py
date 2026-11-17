import sympy as s
A=s.Matrix([[1,0,0,1,-1,1],[0,1,-1,-1,1,0],[0,1,0,-1,0,0],[0,2,-1,-1,0,1],[0,2,0,-1,0,0],[0,1,1,-1,0,0]])
B=s.Matrix([[1,0,0,0,0,0],[0,0,-1,0,1,0],[0,0,-1,0,0,1],[0,0,-1,0,0,0],[0,1,-1,0,0,0],[0,0,-1,1,0,0]])
I=s.eye(6); M1=A.T; M2=B.T; M0=(M1*M2).inv(); N=M0-I
print('det',A.det(),B.det(),'A^5=I',A**5==I,'B^4=I',B**4==I,'B^2=I',B**2==I)
print('N^2=0',N**2==s.zeros(6),'rank N',N.rank())
from sympy.matrices.normalforms import smith_normal_form
print('Smith N',[smith_normal_form(N,domain=s.ZZ)[i,i] for i in range(6)])
x=s.symbols('x')
print(s.factor(A.charpoly(x).as_expr()),'|',s.factor(B.charpoly(x).as_expr()))
l=s.Matrix([[1,0,0,0,0,0]])
print('ell M1=ell',l*M1==l,'ell M2=ell',l*M2==l)
v1=s.Matrix([1,3,-2,-1,2,0]); v2=s.Matrix([-1,0,0,0,0,0])
print('M1 v1=v1',M1*v1==v1,'M2 v2=v2',M2*v2==v2,'ell(v1),ell(v2)',(l*v1)[0],(l*v2)[0])
# common invariants / coinvariants of H_1 monodromy
K=(M1-I).col_join(M2-I); print('dim common invariant vectors',6-K.rank())
Kc=(M1-I).row_join(M2-I); print('rank of coinvariant relations',Kc.rank(),' Smith',[smith_normal_form(Kc,domain=s.ZZ)[i,i] for i in range(6)])
# Seifert-type pi1 relation: 5a=h, 4b=-h, a+b=0 (cusp clutching zero)
R=s.Matrix([[5,0,-1],[0,4,1],[1,1,0]]); print('det relation matrix',R.det())
# F.3.5: exterior squares of companion matrices
Cf=s.Matrix([[0,0,0,-1],[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]]); Cg=s.Matrix([[0,0,0,-1],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
import itertools
idx=list(itertools.combinations(range(4),2))
def ext2(Mx):
    return s.Matrix(6,6,lambda r,c: Mx[idx[r][0],idx[c][0]]*Mx[idx[r][1],idx[c][1]]-Mx[idx[r][0],idx[c][1]]*Mx[idx[r][1],idx[c][0]])
Q=s.eye(6); 
for i in range(6): Q[i,0]=1
EA=Q.inv()*ext2(Cf.inv())*Q; EB=Q.inv()*ext2(Cg)*Q
print('rank(Cf^-1 - Cg)',(Cf.inv()-Cg).rank(),' F.11 for A:',EA[1:,1:]==A[1:,1:],' for B:',EB[1:,1:]==B[1:,1:])
print('charpolys Cf,Cg:',s.factor(Cf.charpoly(x).as_expr()),s.factor(Cg.charpoly(x).as_expr()))
