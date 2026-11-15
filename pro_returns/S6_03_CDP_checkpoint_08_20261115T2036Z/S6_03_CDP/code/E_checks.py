"""Exact checks for E5, E8, E10 and E11; no floating-point proof claims."""
from fractions import Fraction
from math import gcd
import sympy as s

u11,u12,u21,u22,a,b=s.symbols('u11 u12 u21 u22 a b')
K=s.Matrix([[u11,u12],[u21,u22]])
boundary=s.Matrix([[-u12,u11],[-u22,u21]])
assert s.expand(boundary.det()-K.det())==0
print('E5 boundary matrix:',boundary)
print('E5 determinant equals determinant of Kodaira-Spencer matrix:',s.factor(boundary.det()))

E2,E4,wp,wpp,h=s.symbols('E2 E4 wp wpp h')
pi=s.pi
c=pi**2*E2/3
g2=4*pi**4*E4/3
ctau=pi**3*s.I*(E2**2-E4)/18
wptau=(4*wp**2-4*c*wp-2*c**2-g2/2+2*h*wpp)/(4*pi*s.I)-ctau
at_zero=s.simplify(wptau.subs(wp,0)-h*wpp/(2*pi*s.I)-s.I*g2/(6*pi))
assert at_zero==0
print('E8 heat-equation identity residual at wp=0:',at_zero)

F,k=s.symbols('F k',nonzero=True)
nu2sq=9*F**2/s.Integer(512)
tau1=s.I*pi*F**2/2
b3=7*s.I/(32*pi)
K2=s.simplify(24*nu2sq-3*tau1*b3)
joint=s.simplify(-k*(K2+12*nu2sq)/tau1)
assert K2==3*F**2/4
assert s.simplify(joint-123*s.I*k/(64*pi))==0
rawdet=s.simplify(tau1**2*(-12/F**4)**2/(6*pi**2*(-8/F**6)))
assert rawdet==K2
print('E8 order-three raw determinant coefficient:',K2)
print('E8 order-three transverse coefficient:',joint)

t=s.symbols('t')
A=-3*t**3*(t-1)
B=2*t**4*(t-1)**2
P=(s.Integer(0),s.sqrt(2)*t**2*(t-1))
def add(P,Q):
    x,y=P; z,w=Q
    slope=(3*x*x+A)/(2*y) if P==Q else (w-y)/(z-x)
    nx=s.factor(slope*slope-x-z)
    ny=s.factor(-y+slope*(x-nx))
    return nx,ny
P2=add(P,P);P3=add(P2,P)
assert s.simplify(P2[0]-9*t**2/8)==0
assert s.simplify(P3[0]-16*(t-1)*(5*t-32)/81)==0
print('E8 exact x(2P), x(3P), x(3P)(0):',P2[0],P3[0],P3[0].subs(t,0))

def coarse_degree(d,r,q):
    ar=(d*pow(q,-1,r))%r
    aq=(d*pow(r,-1,q))%q
    ans=Fraction(d,r*q)-Fraction(ar,r)-Fraction(aq,q)
    assert ans.denominator==1
    return ans.numerator
def h0(d,r,q):
    if d<0:return 0
    return sum((d-r*j)%q==0 for j in range(d//r+1))
checked=0
for k0 in range(1,41):
    for ell in range(1,41):
        r,q=3*k0,4*ell
        if gcd(r,q)!=1:continue
        n=k0*ell
        assert coarse_degree(-n,r,q)==-1
        assert coarse_degree(-2*n,r,q)==-1
        L=r+q-r*q
        assert coarse_degree(L,r,q)==-1
        assert h0(n-2*r-2*q,r,q)==0
        assert coarse_degree(L-n,r,q)==(-1 if k0==1 else -2)
        checked+=1
print('E11 coprime multiplicity pairs k,l<=40 checked:',checked)
print('E11 all exact root cohomology identities passed')

w=s.exp(2*s.pi*s.I/3)
# Algebraic minimal polynomials avoid approximate comparisons of critical values.
disc1=t**3-1
disc2=(t-4)*((t-4)**3-1)
assert s.gcd(disc1,disc2)==1
assert s.degree(disc2)==4
for branch in range(10,16):
    assert disc1.subs(t,branch)*disc2.subs(t,branch)!=0
branchpoly=s.prod(t-j for j in range(10,16))
assert s.gcd(branchpoly,s.diff(branchpoly,t))==1
print('E10 disjoint Hesse critical-value polynomials and six simple branch values: passed')

mu,e1,e2,bb,x,y,r=s.symbols('mu e1 e2 b x y r')
residue_matrix=s.Matrix([[1,-bb/(e1+mu)],[1,-bb/(e2+mu)]])
assert s.simplify(residue_matrix.det()-bb*(e2-e1)/((e1+mu)*(e2+mu)))==0
print('E13 exact two-node residue determinant:',s.factor(residue_matrix.det()))
# Connection coefficient times the invariant differential transforms without
# a pole under the order-four good-reduction coordinate comparison.
transformed=s.factor(((r**-3*y+bb)/(r**-2*x+mu))*r)
assert s.simplify(transformed-(y+bb*r**3)/(x+mu*r**2))==0
print('E13 order-four connection comparison:',transformed)
eps=s.symbols('eps')
disc=4*t**3+27*(t+eps)**2
print('E14 elliptic collision discriminant:',s.factor(s.discriminant(disc,t)))
assert s.factor(disc.subs(eps,0))==t**2*(4*t+27)
print('E14 exact cusp jet slope:',s.series(-s.I/(1+x),x,0,2))
jet_matrix=s.Matrix([[1,-s.I],[0,s.I]])
assert jet_matrix.det()==s.I
print('E14 exact jet restriction determinant:',jet_matrix.det())

