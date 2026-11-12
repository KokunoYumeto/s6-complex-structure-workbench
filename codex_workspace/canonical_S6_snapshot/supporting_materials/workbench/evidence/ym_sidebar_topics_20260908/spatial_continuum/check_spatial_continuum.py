"""Exact algebra diagnostics; analytic estimates are proved in spatial_continuum.md."""
from pathlib import Path
import json
import sympy as s

count=0
def check(value):
    global count
    assert bool(value)
    count+=1

m,l,q,ac,bc,cc,dc,M=s.symbols('m l q ac bc cc dc M',real=True,nonzero=True)
D=l*q+6*m*m
B=s.Matrix([[6*m,l],[-q,m]])
Bi=s.Matrix([[m,-l],[q,6*m]])/D
check(s.simplify(B*Bi)==s.eye(2))
check(s.simplify(Bi*B)==s.eye(2))
A=s.Matrix([[ac,bc],[cc,dc]])
Q=A.row_join(M*s.eye(2)).col_join(B.row_join(s.zeros(2)))
Qi=s.zeros(2).row_join(Bi).col_join((s.eye(2)/M).row_join(-A*Bi/M))
check(s.simplify(Q*Qi)==s.eye(4))
check(s.simplify(Q.det()-M*M*D)==0)
P=s.Matrix([[ac,bc,M,0],[6*m,l,0,0],[cc,dc,0,M],[-q,m,0,0]])
check(s.simplify(P.det()+M*M*D)==0)
R=s.Matrix([[0,0,0,0],[0,0,0,0],[0,1,0,0],[-1,0,0,0]])
S=s.diag(1,1,M,M)
check(R*R==s.zeros(4))
check(s.simplify(S.inv()*(s.eye(4)+M*R)*S)==s.eye(4)+R)
y1,y2=s.symbols('y1 y2',real=True)
f=2*s.pi/D**2*(m*q*y1*y1/2-l*q*y1*y2-3*m*l*y2*y2)
check(s.simplify(s.diff(f,y1)-2*s.pi*(m*y1-l*y2)*q/D**2)==0)
check(s.simplify(s.diff(f,y2)+2*s.pi*y1/D-2*s.pi*(m*y1-l*y2)*6*m/D**2)==0)
perm=s.zeros(4)
for row,col in enumerate([2,1,3,0]): perm[row,col]=1
check(perm.det()==1)
for L in range(2,13):
    r=lambda k:s.Rational(1,2)+k+k*k
    sum1=sum(r(k)**2 for k in range(-L,L))
    sum2=sum(k**4 for k in range(-L,L+1))
    check(sum1==s.Rational(L*(4*L**4+1),10))
    check(sum2==s.Rational(L*(L+1)*(2*L+1)*(3*L*L+3*L-1),15))
    AL=s.Rational(L*L*(2*L+1)*(24*L**4+24*L**3+8*L*L-4*L+3),15)
    check(AL==2*L*(2*L+1)*sum1+4*L*L*sum2)
    check(AL>=s.Rational(16,5)*L**7)
    EL=s.Rational(2,3)*(2*L*(2*L+1)*sum(r(k)**3 for k in range(-L,L))+4*L*L*sum(k**6 for k in range(-L,L+1)))
    check(EL<=16*L**9)
    check(AL-s.Rational(16,10)*L**7>=L**7)
    faces=12*L*L*(2*L+1)
    check(faces<=36*L**3)
for twice_spin in range(0,31):
    spin=s.Rational(twice_spin,2)
    weights=[-spin+k for k in range(twice_spin+1)]
    check(sum(w*w for w in weights)==(twice_spin+1)*spin*(spin+1)/3)
j=s.symbols('j',positive=True)
faces=12*j**4*(2*j*j+1)
xi=1/(j*j*faces)
g2=j*s.sqrt(faces)/2
a=1/(100*j)
kappa=2*g2/a
b=1/(2*g2*a)
check(s.simplify(1/(4*g2*g2)-xi)==0)
check(s.simplify(kappa-100*j*j*s.sqrt(faces))==0)
check(s.simplify(b-100/s.sqrt(faces))==0)
check(s.simplify(b/kappa-xi)==0)
check(s.simplify(xi*faces-1/j**2)==0)
check(s.limit(j**8*xi,j,s.oo)==s.Rational(1,24))
check(s.limit(kappa/j**5,j,s.oo)==100*s.sqrt(24))
check(s.Rational(16,5)/9/24**2==s.Rational(1,1620))
check(s.Rational(8,3)*4*36*16==6144)
check(s.Rational(5,4)*27+s.Rational(1,2)<40)
I=s.eye(2)
sigma1=s.Matrix([[0,1],[1,0]])
sigma3=s.diag(1,-1)
h1=s.Rational(3,5)*I+s.Rational(4,5)*s.I*sigma3
h2=s.Rational(5,13)*I+s.Rational(12,13)*s.I*sigma3
u1=s.Rational(8,17)*I+s.Rational(15,17)*s.I*sigma1
u2=s.Rational(20,29)*I+s.Rational(21,29)*s.I*sigma3
for v in [h1,h2,u1,u2]:
    check(v.det()==1)
    check(s.simplify(v.conjugate().T*v)==I)
actual=h1.inv()*u1*h2.inv()*u2
retained=h1.inv()*(u1*h2.inv()*u1.inv())*(u1*u2)
check(s.simplify(actual-retained)==s.zeros(2))
check(s.simplify(actual-(h1*h2).inv()*u1*u2)!=s.zeros(2))

# Exact diagnostics for Sections 9--11; analytic proofs remain in the manuscript.
x=s.symbols('xi',positive=True)
check(s.Rational(2048,3)*s.Rational(9,8)*2==1536)
check(s.Rational(2048,3)*11*2==s.Rational(45056,3))
check(s.Rational(1536,49152)==s.Rational(1,32))
check(s.Rational(45056,3*49152)==s.Rational(11,36))
check(s.Rational(512,3*49152)==s.Rational(1,288))
check(s.Rational(3,4)*(1-s.Rational(1,288))==s.Rational(287,384))
check(s.Rational(287,384)*200==s.Rational(7175,48))
g,aa,kap=s.symbols('g a kappa',positive=True)
gap=s.Rational(3,4)*(2*g**2/aa)*(1-s.Rational(512,3)/(4*g**4))
check(s.simplify(gap-(3*g**2/(2*aa)-64/(aa*g**2)))==0)
check(s.simplify(gap.subs(aa,1/(100*j))-(150*g**2-6400/g**2)*j)==0)
check(s.Rational(49152,4)==12288)
u0,u1q,u2q,u3q=s.symbols('u0 u1q u2q u3q',real=True)
sigmas=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
U=u0*s.eye(2)+s.I*sum((q0*sm for q0,sm in zip([u1q,u2q,u3q],sigmas)),s.zeros(2))
derivatives=[s.trace((-s.I*sm/2)*U) for sm in sigmas]
check(s.simplify(sum(dv**2 for dv in derivatives)-(u1q**2+u2q**2+u3q**2))==0)
check(s.simplify(sum(s.trace((-s.I*sm/2)**2*U) for sm in sigmas)+s.Rational(3,4)*s.trace(U))==0)
alpha,bb,scale,side=s.symbols('alpha B scale side',positive=True)
threshold=3*alpha*scale/32
raw=(3*alpha*scale/4-4*threshold)**2/(bb**2*scale**2)
check(s.simplify(raw-9*alpha**2/(64*bb**2))==0)
check(s.simplify(raw/4-9*alpha**2/(256*bb**2))==0)
check(s.simplify(threshold.subs(scale,(2*g**2/aa)*(4*side/aa))-3*alpha*g**2*side/(4*aa**2))==0)
gj2=1/s.log(j)
check(s.simplify((gj2/(2*aa)).subs(aa,1/(100*j))-50*j/s.log(j))==0)
check(s.simplify((2*gj2/aa).subs(aa,1/(100*j))-200*j/s.log(j))==0)
check(s.simplify((1/(2*gj2*aa)).subs(aa,1/(100*j))-50*j*s.log(j))==0)
check(s.Rational(6144,10**8)/4==s.Rational(1536,10**8))
check(s.simplify((3*alpha*g**2*side/(4*aa**2)).subs({g**2:gj2,aa:1/(100*j)})-7500*alpha*side*j**2/s.log(j))==0)
gstar2=kap/(200*j)
check(s.simplify(1/(4*gstar2**2)-10000*j**2/kap**2)==0)
check(s.simplify(2*gstar2/(1/(100*j))-kap)==0)
check(s.simplify(1/(2*gstar2/(100*j))-10000*j**2/kap)==0)
check(s.simplify(s.Rational(6144,10**8)*(10000*j**2/kap**2)/j**2-s.Rational(6144,10000)/kap**2)==0)

report={'exact_assertions':count,'status':'passed','scope':'Finite symbolic algebra and constants only; operator, compactness, and spectral proofs are in the manuscript.'}
out=Path(__file__).resolve().parent/'CHECK_RESULTS.json'
out.write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
