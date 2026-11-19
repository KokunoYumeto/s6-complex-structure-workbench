"""Fresh exact checks for the Paper I audit, 2026-11-19.

Uses only Python's standard library. The multivariate polynomial arithmetic
and matrix products are implemented here; no earlier program is imported.
All output is a certificate of these finite identities, not a certificate of
the analytic extension arguments.
"""
from fractions import Fraction as F
from itertools import product
from math import gcd
import json

VARS = ('s','v','C','mu','U','b','l0','N','m','n','x','y','t')
DIM = len(VARS)

class P:
    def __init__(self, value=0):
        self.a = value if isinstance(value,dict) else {(0,)*DIM:F(value)}
        self.a = {k:F(v) for k,v in self.a.items() if v}
    def __add__(self,b):
        b = p(b); a = self.a.copy()
        for k,v in b.a.items(): a[k]=a.get(k,F(0))+v
        return P(a)
    __radd__=__add__
    def __neg__(self): return P({k:-v for k,v in self.a.items()})
    def __sub__(self,b):return self+-p(b)
    def __rsub__(self,b):return p(b)+-self
    def __mul__(self,b):
        a={}
        for k,v in self.a.items():
            for l,w in p(b).a.items():
                z=tuple(i+j for i,j in zip(k,l));a[z]=a.get(z,F(0))+v*w
        return P(a)
    __rmul__=__mul__
    def __truediv__(self,b):return self*F(1,b)
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        r=P(1)
        for _ in range(n):r=r*self
        return r
    def sub(self,**vals):
        r=P()
        for k,v in self.a.items():
            term=P(v)
            for name,e in zip(VARS,k):term*=p(vals.get(name,X[name]))**e
            r+=term
        return r
    def __eq__(self,b):return self.a==p(b).a

def p(x):return x if isinstance(x,P) else P(x)
X={name:P({tuple(int(i==j) for i in range(DIM)):1}) for j,name in enumerate(VARS)}
globals().update(X)
checks=[]
def certify(name,condition,detail):
    assert condition,name
    checks.append({'name':name,'result':'PASS','detail':detail})

# Weierstrass equation, point, discriminant and AC26 original transport.
c=t**3*(t-1); d=t**4*(t-1)**2
far=x**3-3*c*x/4+d/4
fgeom=(2*x)**3-3*c*(2*x)+2*d
certify('Weierstrass equation transport',8*far==fgeom,
        'X=2x, Y=-2sqrt(2)y; Y^2=8y^2; inverse X/2,-Y/(2sqrt(2))')
delta_ar=-16*(4*(-3*c/4)**3+27*(d/4)**2)
delta_geom=-16*(4*(-3*c)**3+27*(2*d)**2)
certify('Discriminant scale',delta_geom==64*delta_ar,
        'Delta_geom=64 Delta_ar')
certify('Discriminant factorization',delta_ar==27*t**8*(t-1)**3,
        'Delta_ar=27t^8(t-1)^3, nonzero for t!=0,1')
certify('Marked arithmetic point',far.sub(x=0)==(t**2*(t-1)/2)**2,
        'P_ar=(0,t^2(t-1)/2)')
f_original=4*x**3-3*c*x-d
certify('Original AC26 equation transport',-4*far==f_original.sub(x=-x),
        'x_ar=-x_original,y_ar=y_original/(2i); original y^2=4x^3-3Cx-D')

# General even N deck differences without a rational-function engine:
# use N*F/a = (6mu(s+Nv), C(s+Nv)-(s+Nv)^2/2+N^2v/2).
L=s+N*v
NF=[6*mu*L,C*L-L**2/2+N**2*v/2]
gamma=[6*mu,C-L]
delta=[P(0),P(1)]
for label,subst,expected in [
    ('cusp',{'s':s+N*m},[N*m*gamma[i]-N**2*m**2*delta[i]/2 for i in range(2)]),
    ('parameter',{'v':v+n},[N*n*gamma[i]-N**2*n*(n-1)*delta[i]/2 for i in range(2)])]:
    certify('General N '+label+' difference',
            all(NF[i].sub(**subst)-NF[i]==expected[i] for i in range(2)),
            'Exact polynomial coefficients vanish; divide identity by N, multiply by a')

# The origin subtraction, multiplied by N to avoid division by N.
a=b-N*l0
zg=[6*s*mu,-s*(s+1)/2+s*(C-N*v)]
No=[-6*b*mu*s,b*s**2/2-b*C*s+N*l0*s/2+N*v*(b*s+U)]
Nsigma=[-N*l0*zg[0]+N*6*a*mu*v,
        -N*l0*zg[1]+N*(v*U+a*C*v-N*a*v**2/2+N*a*v/2)]
certify('General N origin subtraction',all(Nsigma[i]-No[i]==a*NF[i] for i in range(2)),
        'N(sigma-o)=a*N*F_N for z_gamma=(6s mu,-s(s+1)/2+s(C-Nv))')

def matmul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def I(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def M(B,z,t):
    z1,z2=z
    return [[1,0,0,0],[6*z1,B[0][0],B[0][1],0],[6*z2,B[1][0],B[1][1],0],
            [t,z2*B[0][0]-z1*B[1][0],z2*B[0][1]-z1*B[1][1],1]]
Umat=M(I(2),[1,0],-6); Vmat=M(I(2),[0,1],-6)
Uinv=M(I(2),[-1,0],6); Vinv=M(I(2),[0,-1],6)
certify('Heisenberg commutator',matmul(matmul(matmul(Umat,Vmat),Uinv),Vinv)==M(I(2),[0,0],-12),
        '[U,V]=Z^{-1}, Z=g(I,0,12)')
S=[[0,-1],[1,0]]; T=[[1,1],[0,1]]
for name,A,al in [('S',S,9),('T',T,1),('-I',[[-1,0],[0,-1]],6)]:
    real=M([[P(2),P(1)],[P(3),P(2)]],[x,y],t)
    expected=M(matmul(A,[[P(2),P(1)],[P(3),P(2)]]),[A[0][0]*x+A[0][1]*y,A[1][0]*x+A[1][1]*y],t+al)
    certify('Lift action '+name,matmul(M(A,[0,0],al),real)==expected,
            '(B,x,t) maps to (AB,Ax,t+alpha(A))')
Q=lambda v:(v[0]+v[1]+v[0]*v[1])%2
sl2mod2=[[[a,b],[c,d]] for a,b,c,d in product(range(2),repeat=4) if (a*d-b*c)%2==1]
parity_count=0
for A in sl2mod2:
    for z,w in product(product(range(2),repeat=2),repeat=2):
        Aw=[sum(A[i][j]*w[j] for j in range(2))%2 for i in range(2)]
        rhs=(Q(z)+Q(w)+z[0]*Aw[1]-z[1]*Aw[0])%2
        lhs=Q([(z[i]+Aw[i])%2 for i in range(2)])
        assert lhs==rhs
        parity_count+=1
certify('Congruence character polynomial law',True,
        str(parity_count)+' exhaustive F2 instances for Q(x+By)-Q(x)-Q(y)=x^tJBy mod2')
certify('SL2 character relations',(4*9)%12==0 and (2*9-3*(9+1))%12==0,
        'alpha(S)^4=0 and 2alpha(S)=3(alpha(S)+alpha(T)) in Z/12')

# Finite-orbit annihilator: independent determinant calculation over integers.
rows=[[0,1,0],[6,0,1],[0,0,-1]]
det=sum((1 if (i,j,k) in [(0,1,2),(1,2,0),(2,0,1)] else -1)*rows[0][i]*rows[1][j]*rows[2][k]
        for i,j,k in product(range(3),repeat=3) if len({i,j,k})==3)
certify('Finite-orbit annihilator',det==6,
        'Rows u,6g+w,-w have determinant 6 and common rational kernel zero')

# Arithmetic hypothesis: a is a unit modulo N, checked exhaustively as a
# supplement to the Bezout proof (the check is explicitly finite).
trials=0
for k,l in product(range(1,21),repeat=2):
    m1,m2=3*k,4*l
    if gcd(m1,m2)>1:continue
    for l1 in range(m1):
        if gcd(l1,m1)>1:continue
        for l2 in range(m2):
            if gcd(l2,m2)>1:continue
            assert gcd(m2*l1+m1*l2,m1*m2)==1
            trials+=1
certify('Admissible higher family arithmetic',True,
        f'{trials} admissible residue pairs for 1<=k,l<=20; all gcd(a,12kl)=1')

print(json.dumps({'checker':'GPT-6 Astra, ChatGPT Pro mode, inherited effort',
                  'method':'fresh standard-library rational polynomial and matrix arithmetic',
                  'checks':checks,'passed':len(checks)},indent=2))
