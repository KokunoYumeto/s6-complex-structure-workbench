import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from itertools import combinations
T1=s.Matrix([[1,0,-6,2],[0,-1,1,1],[0,-1,0,1],[0,0,0,1]])
T2=s.Matrix([[1,6,0,-3],[0,0,-1,1],[0,1,0,0],[0,0,0,1]])
e=s.eye(4)
print('T1^3==I',T1**3==e,'T2^4==I',T2**4==e)
A1=(T1.inv()).T; A2=(T2.inv()).T
print('A1',A1.tolist()); print('A2',A2.tolist())
pairs=list(combinations(range(4),2))
ext=lambda M: s.Matrix([[M.extract(list(I),list(J)).det() for J in pairs] for I in pairs])
st=(ext(T1)-s.eye(6)).col_join(ext(T2)-s.eye(6))
print('pairs',pairs,'nullspace',[v.T.tolist() for v in st.nullspace()])
# invariants of V and coinvariants
inv=((T1-e).col_join(T2-e)).nullspace(); print('V invariants',[v.T.tolist() for v in inv])
M=(T1-e).row_join(T2-e)
print('Smith form of coinvariant relations', smith_normal_form(M,domain=s.ZZ).tolist())
MA=(A1-e).row_join(A2-e)
print('Smith form of Lambda coinvariants', smith_normal_form(MA,domain=s.ZZ).tolist())
# q = uw + 6 gamma delta as alternating matrix Q[i][j]=q(e_i,e_j) on Lambda (hat basis)
Q=s.zeros(4); Q[1,2]=1;Q[2,1]=-1;Q[0,3]=6;Q[3,0]=-6
v1=s.Matrix([1,2,-4,0]); v2=s.Matrix([-1,-3,3,0])
print('A1 v1==v1',A1*v1==v1,'A2 v2==v2',A2*v2==v2)
print('iota_v1 q',(v1.T*Q).tolist(),'iota_v2 q',(v2.T*Q).tolist())
print('A-invariance of q', A1.T*Q*A1==Q, A2.T*Q*A2==Q)
# coinvariant class = delta-coefficient (evaluation on hat delta); norm eq: 3 d1bar = k*delta-coeff(iota_v1 q), 4 d2bar = k*delta-coeff(iota_v2 q)
k=s.symbols('k')
d1=k*(v1.T*Q)[3]/3; d2=k*(v2.T*Q)[3]/4
print('d1bar',d1,'d2bar',d2,'sum',s.simplify(d1+d2))
# RR polynomial
c1,c2,c3,l,h=s.symbols('c1 c2 c3 l h')
ch=3+c1*h+(c1**2-2*c2)*h**2/2+(c1**3-3*c1*c2+3*c3)*h**3/6
td=1+c1*h/2+(c1**2+c2)*h**2/12+c1*c2*h**3/24
tw=1+l*h+l**2*h**2/2+l**3*h**3/6
print(s.expand(ch*td*tw).coeff(h,3))
# gluing scalar for N's choice: frame s/(r-2): ratio at q=-1 over p=1
print(s.Rational(1,-1-2)/s.Rational(1,1-2))
