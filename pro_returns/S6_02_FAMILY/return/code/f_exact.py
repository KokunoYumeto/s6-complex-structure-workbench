"""Exact certificates for statements F.1.1--F.3.3.

All arithmetic is in Z or Q.  The second matrix implementation below uses
Python Fraction and does not call SymPy.  No floating-point claim is made.
Run: python code/f_exact.py
"""
from pathlib import Path
from fractions import Fraction
import sympy as s

lines = []
def emit(label, value):
    lines.append(f"{label}: {value}")

I = s.eye(4)
A = s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
B = s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
Omega = s.Matrix([[0,0,0,6],[0,0,1,0],[0,-1,0,0],[-6,0,0,0]])
J2 = s.Matrix([[0,1],[-1,0]])
E = s.zeros(4); E[3,0] = 1

def gm(C, x, t):
    G = s.eye(4)
    G[1:3, 1:3] = C
    G[1:3, 0] = 6*s.Matrix(x)
    G[3,1:3] = -s.Matrix(x).T*J2*C
    G[3,0] = t
    return G

def data(G):
    return G[1:3,1:3], G[1:3,0]/6, G[3,0]

K = A*B**2*A**-1*B**-2
U = B*K*B**-1
V = K**-1
Z = I + 12*E
emit("A1", A.tolist()); emit("A2", B.tolist())
emit("psi", Omega.tolist())
for name, G in [("A1",A),("A2",B)]:
    emit(name+" preserves psi", G.T*Omega*G == Omega)
emit("A1^3=I", A**3 == I)
emit("A2^4=I", B**4 == I)
emit("K=[A1,A2^2]", K.tolist())
emit("U=A2 K A2^-1", U.tolist())
emit("V=K^-1", V.tolist())
emit("[U,V]=Z^-1", U*V*U**-1*V**-1 == Z**-1)
emit("U data (B,x,t)", data(U))
emit("V data (B,x,t)", data(V))
emit("central Z", Z.tolist())
emit("A1 K A1^-1", (A*K*A**-1).tolist())

x1,x2,y1,y2,t,r = s.symbols("x1 x2 y1 y2 t r")
Gx = gm(s.eye(2),[x1,x2],t)
Gy = gm(s.eye(2),[y1,y2],r)
prod = gm(s.eye(2),[x1+y1,x2+y2], t+r-6*(x1*y2-x2*y1))
emit("symbolic Heisenberg product", s.simplify(Gx*Gy-prod) == s.zeros(4))
emit("symbolic Heisenberg commutator", s.simplify(Gx*Gy*Gx.inv()*Gy.inv() - (I-12*(x1*y2-x2*y1)*E)) == s.zeros(4))

def Q(a,b): return a+b+a*b
SL2F2=[]
for a in range(2):
 for b in range(2):
  for c in range(2):
   for d in range(2):
    if (a*d-b*c)%2 == 1: SL2F2.append((a,b,c,d))
emit("SL2(F2) size",len(SL2F2))
emit("Q invariant under all SL2(F2)",all((Q(a*x+b*y,c*x+d*y)-Q(x,y))%2==0 for a,b,c,d in SL2F2 for x in range(2) for y in range(2)))
emit("Q polarization identity", s.expand(Q(x1+y1,x2+y2)-Q(x1,x2)-Q(y1,y2) - (x1*y2-x2*y1)))
emit("h(A1) mod12", int((data(A)[2]+6*Q(*data(A)[1]))%12))
emit("h(A2) mod12", int((data(B)[2]+6*Q(*data(B)[1]))%12))
logs = [U-I,V-I,Z-I]
emit("Heisenberg logarithms independent", s.Matrix.hstack(*[s.Matrix(L).reshape(16,1) for L in logs]).rank()==3)

J0 = s.Matrix([[0,0,-1,0],[0,0,0,-6],[1,0,0,0],[0,s.Rational(1,6),0,0]])
R0 = gm(s.Matrix([[1,6],[0,1]]),[0,0],-1)
R = R0**12
delta = s.Matrix([0,0,0,1])
emit("null J0", J0.tolist())
emit("J0^2=-I", J0**2 == -I)
emit("J0 symplectic", J0.T*Omega*J0 == Omega)
emit("g0=psi(.,J0.)", (Omega*J0).tolist())
emit("g0 eigenvalues", (Omega*J0).eigenvals())
emit("q_delta(J0)", (delta.T*Omega*J0*delta)[0])
emit("R0",R0.tolist()); emit("R=R0^12",R.tolist())
emit("R symplectic",R.T*Omega*R==Omega)
emit("R commutes with J0",R*J0==J0*R)
emit("(R-I)^2=0",(R-I)**2==s.zeros(4))
emit("rank(R-I)",(R-I).rank())
emit("character of R mod12",(-12-72)%12)

Ytau,Ymu,Ybeta=s.symbols("Ytau Ymu Ybeta",real=True)
Y=s.Matrix([[6*Ymu,Ytau],[Ybeta,Ymu]])
abcd=Y.inv()*s.Matrix([0,1])
emit("coefficient gamma of Jdelta",s.factor(abcd[0]))
emit("q_delta=-6/D",s.simplify(-6*abcd[0]+6/(Ybeta-6*Ymu**2/Ytau))==0)

tt=s.symbols("t")
aa=-3*tt**3*(tt-1); bb=2*tt**4*(tt-1)**2
ellj=s.cancel(1728*4*aa**3/(4*aa**3+27*bb**2))
emit("Weierstrass j",ellj)
emit("Weierstrass discriminant",s.factor(-16*(4*aa**3+27*bb**2)))
emit("K(z1)/tau_dot^2",s.Rational(6,9)-s.Rational(2,3))

# Second implementation: exact Fraction matrices, no SymPy operations.
def fq(M): return [[Fraction(v) for v in row] for row in M]
def mm(X,Y): return [[sum(X[i][k]*Y[k][j] for k in range(len(Y))) for j in range(len(Y[0]))] for i in range(len(X))]
def mt(X): return list(map(list,zip(*X)))
def mid(n): return [[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
def mp(X,n):
    Y=mid(len(X))
    for _ in range(n): Y=mm(Y,X)
    return Y
def sub(X,Y): return [[a-b for a,b in zip(xx,yy)] for xx,yy in zip(X,Y)]
Af=fq([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
Bf=fq([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
Of=fq([[0,0,0,6],[0,0,1,0],[0,-1,0,0],[-6,0,0,0]])
Jf=fq([[0,0,-1,0],[0,0,0,-6],[1,0,0,0],[0,Fraction(1,6),0,0]])
Rf=fq([[1,0,0,0],[0,1,72,0],[0,0,1,0],[-12,0,0,1]])
Kf=mm(mm(mm(Af,mp(Bf,2)),mp(Af,2)),mp(Bf,2))
emit("independent Fraction A1 order",mp(Af,3)==mid(4))
emit("independent Fraction A2 order",mp(Bf,4)==mid(4))
emit("independent Fraction K",[[int(v) for v in row] for row in Kf])
emit("independent Fraction A1 symplectic",mm(mm(mt(Af),Of),Af)==Of)
emit("independent Fraction A2 symplectic",mm(mm(mt(Bf),Of),Bf)==Of)
emit("independent Fraction J0 square",mm(Jf,Jf)==[[-v for v in row] for row in mid(4)])
emit("independent Fraction J0 symplectic",mm(mm(mt(Jf),Of),Jf)==Of)
emit("independent Fraction R symplectic",mm(mm(mt(Rf),Of),Rf)==Of)
emit("independent Fraction stabilizer commutation",mm(Rf,Jf)==mm(Jf,Rf))
emit("independent Fraction R nilpotence",mm(sub(Rf,mid(4)),sub(Rf,mid(4)))==fq([[0]*4 for _ in range(4)]))

output="\n".join(lines)+"\n"
print(output,end="")
Path(__file__).with_suffix(".out.txt").write_text(output)
