"""Exact retained-coordinate period/Gram identities; Python + SymPy only."""
import sympy as s

checks = 0
def check(label, a, b):
    global checks
    diff = a-b
    if isinstance(diff, s.MatrixBase):
        assert diff.applyfunc(s.expand) == s.zeros(*diff.shape), label
    else:
        assert s.expand(diff) == 0, label
    checks += 1
    print('PASS', label)

P=s.Matrix([[1,-1,0],[0,1,-1]])
B=s.Matrix([[0,1],[-1,0]])
Q=s.Matrix([[0,-1,1],[1,-1,0]])
S=s.Matrix([[1,1],[0,1],[0,0]])
C=P*P.T
check('P=B Q',P,B*Q)
check('PS=I',P*S,s.eye(2))
Phi=s.diag(P,Q)
def M(x): return s.BlockMatrix([[s.eye(3),x*s.eye(3)],[s.zeros(3),s.eye(3)]]).as_explicit()
MF=s.BlockMatrix([[s.eye(2),B],[s.zeros(2),s.eye(2)]]).as_explicit()
check('integral monodromy square',Phi*M(1),MF*Phi)
x,y=s.symbols('x y',real=True)
co=s.symbols('c0:4',complex=True)
C2=s.Matrix(2,2,co)
C3=S*C2*Q
Z3=(x+s.I*y)*s.eye(3)+C3
Z2=(x+s.I*y)*B+C2
Om3=s.eye(3).row_join(Z3)
Om2=s.eye(2).row_join(Z2)
check('complete period square',P*Om3,Om2*Phi)
check('remove real shear with explicit metric',Om3*M(-x),s.eye(3).row_join(s.I*y*s.eye(3)+C3))
w=s.symbols('w0:21',real=True)
W=s.zeros(6); k=0
for i in range(6):
    for j in range(i,6):
        W[i,j]=W[j,i]=w[k]; k+=1
Wx=M(-x)*W*M(-x).T
check('weight monodromy',Wx.subs(x,x+1),M(-1)*Wx*M(-1).T)
check('metric Gram square',P*Om3*W*Om3.H*P.T,Om2*Phi*W*Phi.T*Om2.H)
E=W[:3,:3]; F=W[:3,3:]; K=W[3:,3:]
Obs=s.eye(3).row_join(s.I*y*s.eye(3)+C3)
exact=y*y*K+s.I*y*(F.T-F+K*C3.H-C3*K)+E+F*C3.H+C3*F.T+C3*K*C3.H
check('full polynomial including all terms',Obs*W*Obs.H,exact)
n=s.symbols('n',real=True)
shifted=s.eye(3).row_join(Z3+n*s.eye(3))
coefficient=(shifted*W*shifted.H).applyfunc(lambda e:s.expand(e).coeff(n,2))
check('constant metric n squared coefficient',coefficient,K)
check('retained unit-metric leading matrix',C,s.Matrix([[2,-1],[-1,2]]))
check('retained leading determinant',C.det(),3)
print(f'ALL {checks} EXACT CHECKS PASSED; positivity and limiting scope are proved in TeX.')
