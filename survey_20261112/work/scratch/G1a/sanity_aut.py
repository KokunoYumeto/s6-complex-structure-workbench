import sympy as S, itertools
from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form as hnf
I=S.eye(4)
A1=S.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=S.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
# lattice Z of pairs (l1,l2) in Z^8 with l1 in im(A1-I), l2 in im(A2-I), (l1+A1 l2)_{0,1}=0
# parametrize by generators: e1=(0,1,-2,0), f1=(0,0,-3,1), e2=(0,1,-1,0), f2=(0,0,-2,1)
e1=S.Matrix([0,1,-2,0]);f1=S.Matrix([0,0,-3,1]);e2=S.Matrix([0,1,-1,0]);f2=S.Matrix([0,0,-2,1])
a,b,c,d=S.symbols('a b c d',integer=True)
l1=a*e1+b*f1; l2=c*e2+d*f2
cc=l1+A1*l2
print('l1+A1 l2 =',cc.T.tolist())
# constraint: cc[1]==0
print('constraint:',S.expand(cc[1]),'= 0')
# coboundaries: lam -> ((I-A1)lam,(I-A2)lam) expressed in (a,b,c,d)
def coords(vec,e,f):
    s=S.symbols('s t')
    sol=S.solve(list(s[0]*e+s[1]*f-vec),s,dict=True)[0]
    return [sol[s[0]],sol[s[1]]]
cob=[]
for i in range(4):
    lam=I[:,i]
    cob.append(coords((I-A1)*lam,e1,f1)+coords((I-A2)*lam,e2,f2))
Cb=S.Matrix(cob).T
print('coboundary generators (a,b,c,d) columns:',Cb.tolist())
# admissible lattice: kernel of the constraint row on Z^4
row=S.Matrix([[S.expand(cc[1]).coeff(v) for v in (a,b,c,d)]])
print('constraint row',row.tolist())
ker=row.nullspace()
print('rational kernel basis',[k.T.tolist() for k in ker])
# check coboundaries satisfy constraint
print('row*Cb =',(row*Cb).tolist())
# index of coboundary lattice in kernel lattice: build integer basis of kernel
# kernel lattice = {v in Z^4: row.v=0}
import sympy
from sympy import ilcm
K=S.Matrix.hstack(*[k*ilcm(*[S.fraction(x)[1] for x in k]) for k in ker])
print('K',K.tolist(),' SNF(K)',smith_normal_form(K,domain=S.ZZ).tolist())
# saturate K: compute via HNF of integer kernel using diophantine approach
from sympy.polys.matrices import DomainMatrix
dm=DomainMatrix.from_Matrix(row).convert_to(S.ZZ)
# brute-force integer kernel basis from small vectors
vecs=[S.Matrix(v) for v in itertools.product(range(-3,4),repeat=4) if (row*S.Matrix(v))[0]==0 and any(v)]
M=S.Matrix.hstack(*vecs)
H=hnf(M)
print('integer kernel HNF',H.tolist())
print('coboundary HNF',hnf(Cb).tolist())
print('same lattice:',hnf(M)==hnf(S.Matrix.hstack(M,Cb)) and hnf(Cb)==hnf(S.Matrix.hstack(M,Cb)))
