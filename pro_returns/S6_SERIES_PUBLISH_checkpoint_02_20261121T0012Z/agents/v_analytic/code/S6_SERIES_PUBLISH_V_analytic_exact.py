"""Independent exact arithmetic for Paper V's analytic statements.

Written from the displayed geometry and matrices, without importing prior audit
programs.  Polynomial coefficient reduction reconstructs Gauss--Manin; exterior
algebra reconstructs the quotient connection and its cusp maps.
"""
import itertools, json
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

OUT=Path(__file__).resolve().parent.parent
x,t,z=s.symbols('x t z'); R=s.Rational
f=x**5+t**3*x+t**4
g=s.symbols('g0:4'); r=s.symbols('r0:5')
rp=sum(r[i]*x**i for i in range(5))
rows=[]; primitives=[]
for k in range(4):
    diff=-R(1,2)*x**k*s.diff(f,t)-f*sum(g[j]*x**j for j in range(4))-s.diff(rp,x)*f+R(1,2)*rp*s.diff(f,x)
    eq=[s.expand(diff).coeff(x,i) for i in range(9)]
    sol=s.solve(eq,g+r,dict=True)[0]
    rows.append([s.factor(sol[v]) for v in g])
    primitives.append(s.factor(rp.subs(sol)))
    assert s.cancel(diff.subs(sol))==0
# Row-frame convention: column k gives the derivative of omega_k.
G4=s.Matrix(rows).T
pairs=list(itertools.combinations(range(4),2))
W=s.zeros(6)
def add_wedge(out,a,b,c):
    if a==b: return
    if a>b: a,b,c=b,a,-c
    out[pairs.index((a,b))]+=c
for j,(a,b) in enumerate(pairs):
    v=s.zeros(6,1)
    for c in range(4):
        add_wedge(v,c,b,G4[c,a]);add_wedge(v,a,c,G4[c,b])
    W[:,j]=v
pr=s.zeros(5,6)
for i,j in enumerate([0,1,2,4,5]):pr[i,j]=1
pr[2,3]=-3
inc=s.zeros(6,5)
for i,j in enumerate([0,1,2,4,5]):inc[j,i]=1
GW=(pr*W*inc).applyfunc(s.factor)
assert pr*W*s.Matrix([0,0,3,1,0,0])==s.zeros(5,1)
display=s.Matrix([
[-8*(625*t+48)/t,-8,10*t,R(75,2)*t*t,0],
[-R(125,2)/t,-4*(625*t+48)/t,8,0,R(75,2)*t*t],
[300/t**2,-375/t,0,-48,60*t],
[120/t**3,0,R(125,2)/t,4*(625*t+48)/t,-8],
[0,120/t**3,50/t**2,-R(125,2)/t,8*(625*t+48)/t]])/(3125*t+256)
assert (GW-display).applyfunc(s.cancel)==s.zeros(5)
astar=-R(256,3125)
b=s.Matrix([[-R(25,6)/t**2,-R(125,48)/t,0,1,0]])/(t-astar)
G6=s.zeros(6);G6[0,1:]=b;G6[1:,1:]=GW
res=G6.applyfunc(lambda v:s.cancel((t-astar)*v).subs(t,astar))
assert res**2==s.zeros(6)
assert res.rank()==3
# Lifted plane columns (w0+4z e/3,w1,w2), quotient (e,w_-1,w_-2).
F=s.zeros(6,3);F[3,0]=1;F[0,0]=R(4,3)*z;F[2,1]=1;F[1,2]=1
quot=s.zeros(3,6);quot[0,0]=1;quot[0,3]=-R(4,3)*z;quot[1,4]=1;quot[2,5]=1
RR=(quot*res*F).applyfunc(s.factor)
A=-R(125,12288)*(192*z-3125);BB=-R(78125,393216)*(96*z+3125)
C=-R(125,512);E=R(78125,32768);D=-R(146484375,2097152)
assert (RR-s.Matrix([[0,A,BB],[C,0,D],[E,D,0]])).applyfunc(s.expand)==s.zeros(3)
C1=s.Matrix([[-C,A,0],[-E,0,BB],[0,-D,D]])
C2=s.Matrix([[-D,D,0],[E,0,-BB],[0,-C,A]])
det=s.factor(C1.det())
assert s.expand(det-R(476837158203125,281474976710656)*(384*z+3125))==0
assert s.expand(C2.det()+det)==0
def degree(n): return s.floor(R(4,5)*n)+s.floor(-R(3,4)*n)
ext=[[0],[0,-1,-2],[-1,-2,-3],[-3]]
def absolute(exponents):
    vals=[0]*5
    for q,ls in enumerate(ext):
        for n in exponents:
            for m in ls:
                d=degree(n+m);vals[q]+=max(d+1,0);vals[q+1]+=max(-d-1,0)
    return list(map(int,vals))
coh={str(w):absolute(w) for w in [[0],[0,1,2],[11],[1,2,3],[11,12,13],[5],[-6,-5,-4]]}
assert coh['[0]']==[1,1,0,0,0]
assert coh['[0, 1, 2]']==[1,3,2,0,0]
assert coh['[11]']==[0,2,3,1,0]
assert coh['[1, 2, 3]']==[0,2,3,1,0]
assert coh['[11, 12, 13]']==[2,6,7,3,0]
assert coh['[5]']==[1,2,1,0,0]
assert coh['[-6, -5, -4]']==[0,0,0,1,1]
# Orbifold canonical class = -2 H + 4 D_inf + 3 D_0,
# and L = 4 D_inf - 3 D_0.  Subtraction of -9L is
# -2H+40D_inf-24D_0 = (-2+8-6)H = 0.
assert -2+40//5-24//4==0
y=s.symbols('y');chi=s.expand((1+y)**4*R(2,240)+(((-1+10*y-y*y)**2)*R(1,144)-(1+y)**4*R(1,120))*6)
assert chi==-y+4*y*y-y**3
MonA=s.Matrix([[1,0,0,1,-1,1],[0,1,-1,-1,1,0],[0,1,0,-1,0,0],[0,2,-1,-1,0,1],[0,2,0,-1,0,0],[0,1,1,-1,0,0]])
MonB=s.Matrix([[1,0,0,0,0,0],[0,0,-1,0,1,0],[0,0,-1,0,0,1],[0,0,-1,0,0,0],[0,1,-1,0,0,0],[0,0,-1,1,0,0]])
M1,M2=MonA.T,MonB.T
vars=s.symbols('m0:36');MM=s.Matrix(6,6,vars)
central=s.linear_eq_to_matrix(list(MM*M1-M1*MM)+list(MM*M2-M2*MM),vars)[0]
assert central.rank()==35
alternating=s.zeros(6);av=s.symbols('a0:15')
for v,(i,j) in zip(av,itertools.combinations(range(6),2)):alternating[i,j]=v;alternating[j,i]=-v
alt=s.linear_eq_to_matrix(list(M1.T*alternating*M1-alternating)+list(M2.T*alternating*M2-alternating),av)[0]
assert alt.rank()==15
K=s.Matrix([[0,0,0],[0,1,0],[1,0,0],[0,0,0],[0,-1,0],[0,0,1]])
TT=s.Matrix([[0,0,0],[0,1,0],[1,0,0],[0,0,-1],[0,0,1],[0,0,-1]])
ZZ=s.Matrix([[-2,-1,1],[0,-1,1],[1,0,1]])
assert (M2-s.eye(6))*TT==K*ZZ
assert [abs(smith_normal_form(ZZ,domain=s.ZZ)[j,j]) for j in range(3)]==[1,1,2]
half=s.Matrix([0,1,1,1,1,1])/2
assert all(a.q==1 for a in (M1-s.eye(6))*half)
assert all(a.q==1 for a in (M2-s.eye(6))*half)
rr=s.Matrix([[1,0,0,0,0,0],[2,0,0,0,-1,0],[-1,0,-1,0,0,0],[-1,0,0,-1,0,0],[2,-1,0,0,0,0],[-1,1,1,1,1,1]])
assert rr*rr==s.eye(6) and rr*M1==M1.inv()*rr and rr*M2==M2.inv()*rr
anti=s.linear_eq_to_matrix(list(MM*M1-M1.inv()*MM)+list(MM*M2-M2.inv()*MM),vars)[0]
assert anti.rank()==35
S=s.Matrix([[0,0,0,1,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[-1,0,0,0,1,0],[1,0,0,0,0,1],[-1,0,0,0,0,0]])
HH=S.inv()*M2.inv()*(-rr)*S
P=HH[:3,:3]
assert P==s.Matrix([[1,0,0],[0,1,0],[1,-1,-1]])
ray=-P*s.Matrix([0,1,0]);assert ray==s.Matrix([0,-1,1])
def skew(w):
    a,b,c=w;return s.Matrix([[0,-c,b],[c,0,-a],[-b,a,0]])
vec=[s.eye(3)[:,i] for i in range(3)]+[s.Matrix(v) for v in [[1,1,0],[1,0,1],[0,1,1]]]
directions=[];ss=s.symbols('s',real=True)
for w in vec:
    q=(w.T*w)[0];Aw=q*s.eye(3)-w*w.T+skew(w);directions.append(Aw)
    assert s.expand((s.eye(3)+ss*Aw).det()-(1+q*ss)**2-q*ss**2)==0
    assert s.expand((1+q*ss)**2+q*ss**2-q*(q+1)*(ss+1/(q+1))**2)==1/(q+1)
directions.extend(skew(s.eye(3)[:,j]) for j in range(3))
tube_det=s.Matrix.hstack(*[m.reshape(9,1) for m in directions]).det()
assert tube_det==-16
data={'gauss_manin':str(G4),'exact_primitives':[str(v) for v in primitives], 'quotient_connection_matches':True,'cusp_residue_rank':res.rank(),'cusp_residue_square_zero':True,'cohomology':coh,'C1_determinant':str(det),'C2_determinant':str(-det),'chi_y':str(chi),'alternating_invariants_dimension':15-alt.rank(),'centralizer_dimension':36-central.rank(),'anti_intertwiner_dimension':36-anti.rank(),'translation_smith':[1,1,2],'ray_obstruction':list(ray),'oka_tube_determinant':int(tube_det)}
(OUT/'S6_SERIES_PUBLISH_V_analytic_exact.json').write_text(json.dumps(data,indent=2,default=str)+'\n')
print(json.dumps(data,indent=2,default=str))
# Save root connections as exact symbolic rational functions for independent
# midpoint-extrapolation integration.  This is not a numerical certificate.
u=s.symbols('u');root={}
for name,sub,pows in [('zero',u**4,[0,6,3,0,-3,-6]),('infty',u**-5,[0,-8,-4,0,4,8])]:
    DD=s.diag(*[u**j for j in pows]);gg=(DD.inv()*G6.subs(t,sub)*DD*s.diff(sub,u)+DD.inv()*DD.diff(u)).applyfunc(s.cancel)
    assert all(s.denom(v).subs(u,0)!=0 for v in gg)
    root[name]=[[str(gg[i,j]) for j in range(6)] for i in range(6)]
(OUT/'S6_SERIES_PUBLISH_V_root_connections.json').write_text(json.dumps(root,indent=2)+'\n')
root4={}
for name,sub,pows in [('zero',u**8,[9,3,-3,-9]),('infty',u**-5,[-6,-2,2,6])]:
    DD=s.diag(*[u**j for j in pows]);gg=(DD.inv()*G4.subs(t,sub)*DD*s.diff(sub,u)+DD.inv()*DD.diff(u)).applyfunc(s.cancel)
    assert all(s.denom(v).subs(u,0)!=0 for v in gg)
    root4[name]=[[str(gg[i,j]) for j in range(4)] for i in range(4)]
(OUT/'S6_SERIES_PUBLISH_V_rank4_root_connections.json').write_text(json.dumps(root4,indent=2)+'\n')
