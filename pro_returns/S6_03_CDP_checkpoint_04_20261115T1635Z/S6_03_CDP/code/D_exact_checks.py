"""Exact certificates for the monodromy and surface examples in Part D.

No floating point arithmetic occurs. Run with Python 3 and SymPy.
"""
from fractions import Fraction as F
from itertools import permutations, product
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

I = s.eye(4)
A1 = s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2 = s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
assert A1**3 == I and A2**4 == I
M0=(A1*A2).inv()
assert (M0-I)**2 == s.zeros(4)
R=(A1-I).row_join(A2-I)
print('AC monodromy matrices:', A1.tolist(), A2.tolist())
print('AC coinvariant Smith diagonal:', list(smith_normal_form(R, domain=ZZ).diagonal()))
print('AC invariant vectors:', (A1-I).col_join(A2-I).nullspace())
print('AC invariant covectors:', (A1.T-I).col_join(A2.T-I).nullspace())
assert R.rank()==3
assert R[0,:] == s.zeros(1,8)
assert list(smith_normal_form(R,domain=ZZ).diagonal()) == [1,1,1,0]
print('Corrected AC count r=3-1+1=3; printed count 3-1+4=6.')
J2=s.Matrix([[0,1],[-1,0]])
Omega=s.Matrix([[0,0,0,6],[0,0,1,0],[0,-1,0,0],[-6,0,0,0]])
def parabolic(B,x,t):
    out=s.eye(4)
    out[1:3,1:3]=B
    out[1:3,0]=6*s.Matrix(x)
    out[3,1:3]=-s.Matrix(x).T*J2*B
    out[3,0]=t
    return out
S=s.Matrix([[0,-1],[1,0]])
a=s.Matrix([[0,1],[-1,-1]])
assert A1==parabolic(a,[1,-1],-2)
assert A2==parabolic(S,[0,-1],3)
assert A1.T*Omega*A1==Omega and A2.T*Omega*A2==Omega
K=A1*A2**2*A1.inv()*A2**-2
Up=A2*K*A2.inv(); Vp=K.inv()
Zp=s.eye(4); Zp[3,0]=12
assert K==parabolic(s.eye(2),[0,-1],6)
assert Up==parabolic(s.eye(2),[1,0],-6)
assert Vp==parabolic(s.eye(2),[0,1],-6)
assert Up*Vp*Up.inv()*Vp.inv()==Zp.inv()
print('Index-12 group certificate: K,U,V and [U,V]=Z^(-1) verified.')

PE=s.Matrix([[0,-2,-1,-2],[2,-1,0,-1],[0,2,1,3],[-1,0,0,0]])
T0=s.Matrix([[0,-1,-1,0],[1,-1,0,0],[0,0,1,0],[0,0,0,1]])
C=s.Matrix([[1,1,0,1],[0,1,0,0],[0,-1,1,0],[0,0,0,1]])
T1local=s.Matrix([[0,1,0,0],[-1,0,-1,0],[0,0,1,0],[0,0,0,1]])
T1=C*T1local*C.inv()
assert PE.det()==-1 and T0*PE==PE*A1 and T1*PE==PE*A2
d=s.Matrix([0,0,0,1]); gamma=s.Matrix([[1,0,0,0]])
psi=s.Matrix([[0,0,0,1]]); delta0=s.Matrix([-2,-1,3,0])
v1=s.Matrix([1,2,-4,0]); v2=s.Matrix([-1,-3,3,0])
assert PE*d==delta0 and psi*PE==-gamma
assert A1*v1==v1 and A2*v2==v2
a0=-PE*v1/3; a1=-PE*v2/4
assert 12*(psi*(a0+a1))[0]==1
print('Signed Engel dictionary P_E:',PE.tolist(),'; det =',PE.det())
print('Verified T0 P_E=P_E A1 and T1 P_E=P_E A2.')
print('Verified P_E d=delta0 and psi P_E=-gamma.')
print('Standard positive-root Engel a0,a1:',list(a0),list(a1))
print('Engel p=12 psi(a0+a1)=1; retained clockwise p=-1.')

# Wang's matrices act on H^1, not on H_1.
WTstar=s.Matrix([[1,0,-6,-2],[0,-1,-1,1],[0,1,0,-1],[0,0,0,1]])
WT2=s.Matrix([[1,0,6,3],[0,1,2,1],[0,0,1,0],[0,0,0,1]])
WTplus=s.Matrix([[1,0,0,0],[0,2,1,0],[0,-1,0,0],[0,0,0,1]])
WTminus=s.Matrix([[1,0,0,-1],[0,1,1,0],[0,0,1,0],[0,0,0,1]])
WTs=[WTstar,WT2,WTplus,WTminus]
assert WTstar*WT2*WTplus*WTminus==I and WTstar**3==I
Winv=(WTstar-I).col_join(WT2-I).col_join(WTplus-I).col_join(WTminus-I).nullspace()
WR=s.Matrix.hstack(*[(T.inv().T-I) for T in WTs])
assert len(Winv)==1
print('Wang invariant H^1:',Winv)
print('Wang H_1 coinvariant Smith diagonal:',list(smith_normal_form(WR,domain=ZZ).diagonal()))
print('Corrected Wang count r=4-1+1=4; printed count 4-1+4=7.')

A=s.Matrix([[0,-1],[1,1]])
assert A**6==s.eye(2) and (A-s.eye(2)).det()==1
print('Secondary Kodaira A:', A.tolist())
print('Secondary Kodaira coinvariant Smith diagonal:',
      list(smith_normal_form(A-s.eye(2),domain=ZZ).diagonal()))
x,y,z=s.symbols('x y z')
sigma=s.Matrix([-y,x+y,z-y/2])
q=s.Matrix([x,y,z])
for k in range(6):
    q=sigma.subs({x:q[0],y:q[1],z:q[2]}, simultaneous=True).applyfunc(s.expand)
assert q==s.Matrix([x,y,z])
print('Secondary Kodaira sigma^6:', list(q))
print('Lattice preservation difference:', s.expand((z-y/2)-(-y)*(x+y)/2-(z-x*y/2)))
print('This equals xy+y(y-1)/2, an integer at integer x,y.')

t=s.symbols('t')
P=s.Matrix([[1,s.I,t,s.I*t],[-t,s.I*t,1,-s.I]])
B=s.Matrix([[-s.I*t,-t,s.I,1],[-s.I,1,-s.I*t,t]])
assert B*P.T==s.zeros(2)
print('Twistor Hodge exact-complex product B P^T:', (B*P.T).tolist())

# Quadratic field Q(sqrt(5)), represented by pairs (a,b).
zero=(F(0),F(0)); one=(F(1),F(0))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def scale(x,n): return (x[0]*n,x[1]*n)
def sumq(xs):
    out=zero
    for x in xs: out=add(out,x)
    return out
def qm(p,q):
    a,b,c,d=p; e,f,g,h=q
    return (sub(sub(sub(mul(a,e),mul(b,f)),mul(c,g)),mul(d,h)),
            add(add(mul(a,f),mul(b,e)),sub(mul(c,h),mul(d,g))),
            add(add(mul(a,g),mul(c,e)),sub(mul(d,f),mul(b,h))),
            add(add(mul(a,h),mul(d,e)),sub(mul(b,g),mul(c,f))))
def qi(p): return (p[0],neg(p[1]),neg(p[2]),neg(p[3]))
phi=(F(1,2),F(1,2)); invphi=(F(-1,2),F(1,2))
G=set()
for j in range(4):
    for sign in [-1,1]:
        q=[zero]*4; q[j]=scale(one,sign); G.add(tuple(q))
for signs in product([-1,1],repeat=4):
    G.add(tuple(scale(one,F(sign,2)) for sign in signs))
for perm in permutations(range(4)):
    inversions=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
    if inversions%2: continue
    for signs in product([-1,1],repeat=3):
        v=[zero,scale(one,signs[0]),scale(phi,signs[1]),scale(invphi,signs[2])]
        G.add(tuple(scale(v[perm[j]],F(1,2)) for j in range(4)))
assert len(G)==120
assert all(sumq(mul(a,a) for a in p)==one for p in G)
elts=sorted(G); index={q:j for j,q in enumerate(elts)}
table=[]
for p in elts:
    row=[]
    for q in elts:
        v=qm(p,q); assert v in index
        row.append(index[v])
    table.append(row)
identity=index[(one,zero,zero,zero)]
inverse=[index[qi(p)] for p in elts]
comm={table[table[table[i][j]][inverse[i]]][inverse[j]]
      for i in range(120) for j in range(120)}
generated={identity}; frontier=[identity]
while frontier:
    p=frontier.pop()
    for q in comm:
        r=table[p][q]
        if r not in generated:
            generated.add(r); frontier.append(r)
assert len(generated)==120
print('Binary icosahedral exact check: set size', len(elts),
      '; multiplication closure entries',len(elts)**2,
      '; commutator set size',len(comm),'; derived subgroup size',len(generated))
print('Secondary Hopf H1 = Z plus G_ab = Z.')

# Todd/Chern-character degree-three coefficient for a rank-three tangent bundle.
u,c1,c2,c3,l=s.symbols('u c1 c2 c3 l')
ch=3+c1*u+(c1**2-2*c2)*u**2/2+(c1**3-3*c1*c2+3*c3)*u**3/6
td=1+c1*u/2+(c1**2+c2)*u**2/12+c1*c2*u**3/24
twist=1+l*u+l**2*u**2/2+l**3*u**3/6
term=s.expand(ch*td*twist).coeff(u,3)
assert s.simplify(term.subs({c1:0,c2:0,l:0})-c3/2)==0
print('RR degree-six term:',s.factor(term))
print('RR under rational c1=c2=c1(L)=0:', term.subs({c1:0,c2:0,l:0}))
