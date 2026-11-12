# Reader G1a sanity checks (not part of the workspace).
import sympy as S
from sympy.matrices.normalforms import smith_normal_form
I=S.eye(4)
A1=S.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=S.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
g,u,w,d=[I[:,i] for i in range(4)]
v1=S.Matrix([1,2,-4,0]); v2=S.Matrix([-1,-3,3,0])
E=d*g.T
N1=I+A1+A1**2; N2=I+A2+A2**2+A2**3
print('A1^3=I',A1**3==I,'A2^4=I',A2**4==I)
print('N1 cols',N1.T.tolist()); print('N2 cols',N2.T.tolist())
# X_{c+1} = X_c with v_j -> S_1 v_j
S1=I+E
print('S1 v1 - v1 =',(S1*v1-v1).T.tolist(),' S1 v2 - v2 =',(S1*v2-v2).T.tolist())
# is delta in N_j Lambda?  solve N_j x = k*delta over Z for k=1,2
def in_lattice(N,rhs):
    # integer solvability via Smith form of augmented comparison
    from sympy import Matrix
    from sympy.matrices.normalforms import hermite_normal_form as hnf
    return hnf(N)==hnf(N.row_join(rhs))
for k in (1,2,3,4):
    print('k=',k,' k*delta in N1L:',in_lattice(N1,k*d),' in N2L:',in_lattice(N2,k*d))
# Lambda^{A_j}/N_j Lambda
for name,A,N,fix in (('j=1',A1,N1,[v1,d]),('j=2',A2,N2,[S.Matrix([1,3,-3,0]),d])):
    F=S.Matrix.hstack(*fix)
    # coordinates of N columns in fixed basis
    cols=[]
    for i in range(4):
        sol=S.linsolve((F,N[:,i]))
        cols.append(list(list(sol)[0]))
    C=S.Matrix(cols).T
    print(name,'N columns in fixed basis:',C.tolist(),' SNF:',smith_normal_form(C,domain=S.ZZ).tolist())
# Admissible affine cocycles for n=0 (automorphisms): l1 in (A1-I)L, l2 in (A2-I)L, gamma,u-coordinates of l1+A1 l2 vanish; mod coboundaries ((I-A1)lam,(I-A2)lam)
x=S.symbols('x0:4'); y=S.symbols('y0:4')
l1=(A1-I)*S.Matrix(x); l2=(A2-I)*S.Matrix(y)
c=l1+A1*l2
sol=S.solve([c[0],c[1]],list(x)+list(y),dict=True)
print('constraint solution:',sol)
# brute force over a box: collect admissible (l1,l2) and reduce modulo coboundaries
import itertools
adm=set()
R=range(-2,3)
for xv in itertools.product(R,repeat=4):
    L1=(A1-I)*S.Matrix(xv)
    for yv in itertools.product(R,repeat=4):
        L2=(A2-I)*S.Matrix(yv)
        cc=L1+A1*L2
        if cc[0]==0 and cc[1]==0:
            adm.add(tuple(L1)+tuple(L2))
print('admissible cocycles in box:',len(adm))
cob=set()
for lam in itertools.product(range(-6,7),repeat=4):
    lam=S.Matrix(lam)
    cob.add(tuple((I-A1)*lam)+tuple((I-A2)*lam))
print('all admissible in box are coboundaries:',adm<=cob, ' missing:',len(adm-cob))
# Eichler-Zagier constant
uP=S.symbols('uP')
print('roots of u^2+10u+1:',S.solve(uP**2+10*uP+1,uP),' -(5+2sqrt6)=',S.nsimplify(-(5+2*S.sqrt(6))))
