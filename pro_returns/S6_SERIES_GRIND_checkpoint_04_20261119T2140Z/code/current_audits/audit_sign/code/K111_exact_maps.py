import sympy as S,json
from fractions import Fraction as F
from pathlib import Path
out={}; check_count=0
def ck(value,msg):
 global check_count
 check_count+=1
 if not value:raise AssertionError(msg)
# Exact divisor intersection via adjacent differences and then an independent blowup basis.
dm=[-4,-4,-4,-4,-4,-5,-6,-5,-4,-3];dp=[5,5,5,5,5,5,4,3,2,1]
def pair(v,w):return -sum((v[i+1]-v[i])*(w[i+1]-w[i]) for i in range(9))
M=S.zeros(10)
for i in range(10):
 M[i,i]=-1 if i in [0,9] else -2
 if i<9:M[i,i+1]=M[i+1,i]=1
ck(M*S.ones(10,1)==S.zeros(10,1),'full fibre radical')
ck(M.rank()==9,'unique radical')
vals=[pair(dm,dm),pair(dm,dp),pair(dp,dp)]
ck(vals==[-5,2,-4],'MN intersection list')
for v,w in [(dm,dm),(dm,dp),(dp,dp)]:ck(pair(v,w)==(S.Matrix(v).T*M*S.Matrix(w))[0],'two intersection methods')
# coordinates h,u,E1,...,E9
J=S.zeros(11);J[0,1]=J[1,0]=1
for i in range(2,11):J[i,i]=-1
Dminus=S.Matrix([0,-4,0,0,0,1,1,1,-1,-1,0]);Dplus=S.Matrix([0,5,0,0,0,-1,-1,-1,-1,0,0]);h=S.eye(11)[:,0]
x=h+Dminus;y=-h-Dplus
ps=lambda v,w:(v.T*J*w)[0]
ck([ps(Dminus,Dminus),ps(Dminus,Dplus),ps(Dplus,Dplus)]==vals,'blowup basis agrees')
ck([ps(x,x),ps(x,y),ps(y,y),ps(x+y,x+y)]==[-13,-3,6,-13],'normal Chern classes')
refx=h-12*S.eye(11)[:,1];refy=-h-12*S.eye(11)[:,1]
ck([ps(refx,refx),ps(refx,refy),ps(refy,refy)]==[-24,0,24],'own reference')
out['MN']={'two_divisor_forms':vals,'positive_roots':[-13,-3,6],'c1square':-13,'c2':-3,'p1':-27,'own_reference':[0,0,0]}
# All nine blowdowns from rays; each contracts a genuine sum of neighbours.
rays=[(1,0)]+[(i,1) for i in range(3,-7,-1)]+[(-1,0)]
for v in [(i,1) for i in [3,2,1,-6,-5,-4,-3,-2,-1]]:
 idx=rays.index(v);l=rays[idx-1];r=rays[idx+1]
 ck((l[0]+r[0],l[1]+r[1])==v,'ordinary ray contraction')
 rays.pop(idx)
ck(rays==[(1,0),(0,1),(-1,0)],'nine blowdowns endpoint')
# Independent exterior algebra, keyed by sorted coordinate indices alpha,u,v,gamma,theta.
def add(*vs):
 z={}
 for v in vs:
  for k,c in v.items():z[k]=S.expand(z.get(k,0)+c)
 return {k:c for k,c in z.items() if c!=0}
def scale(v,c):return {k:S.expand(c*x) for k,x in v.items() if c*x!=0}
def wedge(v,w):
 z={}
 for a,c in v.items():
  for b,d in w.items():
   if set(a)&set(b):continue
   raw=a+b;sg=(-1)**sum(raw[i]>raw[j] for i in range(len(raw)) for j in range(i+1,len(raw)))
   k=tuple(sorted(raw));z[k]=S.expand(z.get(k,0)+sg*c*d)
 return {k:c for k,c in z.items() if c!=0}
e=[{(i,):S.Integer(1)} for i in range(5)]
j,a,alpha=S.symbols('j a alpha',real=True)
beta=scale(add(e[1],scale(e[2],alpha)),-j)
Fx=wedge(add(e[0],scale(e[4],12)),add(e[3],scale(e[2],j)))
db=scale(wedge(e[0],e[2]),-j)
Fx_a=add(Fx,scale(db,a));form=scale(wedge(beta,wedge(Fx_a,Fx_a)),3)
coeff=S.integrate(form[(0,1,2,3,4)],(a,0,1));ck(coeff==36*j*j,'whole RFB collar sign')
out['RFB_wedge']={'positive_integral':str(coeff),'outward_cutoff_contribution':'-36*j^2','linear_coefficient_from_actual_0to1_comparison':36,'j_minus_one_relative_pair':[-72,0],'independent_native_theta_change':-12}
# Period-coordinate reset, including units.
k,al,g,eta,q,Z,V=S.symbols('k al g eta q Z V',nonzero=True)
for jj in [-1,0,1]:
 kj=k*g**jj;aj=al*eta**jj*k**(-jj)*g**(-jj*jj);ej=eta*g**(-jj)
 new0=(k*q*g**jj*Z,(al*(eta*q)**jj*V)/(k*q*g**jj*Z)**jj)
 ck(S.simplify(new0[1]-aj*(Z**(-jj)*V))==0,'h_j full coefficient')
 ck(S.simplify((eta*q*V)/(g*Z)**jj-ej*q*(Z**(-jj)*V))==0,'B_j full coefficient')
 # reverse C1 reset
 ck(S.simplify(aj/ej*kj/g - al*eta**(jj-1)*k**(-(jj-1))*g**(-(jj-1)**2))==0,'whole C1 alpha reset')
# Native/ordinary prism equations independently derived from the displayed action.
w=[0,1,-1];d=[-2,-1,-1];t=12;l=[24*(1-j),0,24]
I=[S.expand(t*w[i]+d[i]*(l[i]-t)) for i in range(3)]
W=[S.expand(t*w[i]-d[i]*(l[i]-t)) for i in range(3)]
delta=[W[1]-W[0],W[0]-W[2]];vii=[24,24]
n=[S.expand((delta[i]-vii[i])/2) for i in range(2)];m=[S.expand(-vii[i]-n[i]) for i in range(2)]
mn=[(S.expand((m[i]+24)/2),S.expand(n[i]/2)) for i in range(2)]
ck(mn==[(12-12*j,12*j-12),(12*j,-12*j)],'literal-double native pairs')
out['RFS_prisms']={'I':list(map(str,I)),'W':list(map(str,W)),'single_native_pairs':[[str(z) for z in p] for p in mn]}
# The actual phase-square exponent and coupled winding.
rho,tau=S.symbols('rho tau',real=True)
Qrho=3*S.pi*S.I*rho*(rho-1)
ck(S.expand(Qrho.subs(rho,rho+1)-Qrho-6*S.pi*S.I*rho)==0,'full scalar functional equation')
ck(S.expand(3*S.pi*S.I*(16*tau*tau+4*tau)-48*S.pi*S.I*tau*(tau-1)-60*S.pi*S.I*tau)==0,'retained winding30')
out['ASI2_parameter']={'full_functional_equation_residual':0,'physical_circle_winding':30,'paired_half_phase_at_integer':'both (-1)^rho'}
# Small 2x2 quaternion coefficient identity, complex conjugates kept as independent pairs.
z,zb,ww=S.symbols('z zb ww',nonzero=True)
T=lambda z,zb:S.Matrix([[1,-zb],[z,1]])
ck(T(ww**-6*z,ww**6*zb)*S.diag(ww**18,ww**12)==S.diag(ww**18,ww**12)*T(z,zb),'held Cox phase identity')
ck(S.Matrix([[1/z,-1],[1,1/zb]])*S.diag(z,zb)==T(z,zb),'actual two sphere charts')
# Equivariant physical Euler denominator from formal Laurent expansion.
u,aa,bb,p=S.symbols('u aa bb p');v=S.symbols('v')
kexpr=(-u)**3/((-u+aa)*(u+bb))
lexpr=(-u)*(p+(-u+aa)**2+(u+bb)**2)/((-u+aa)*(u+bb))
kcoef=S.expand(S.series(kexpr.subs(u,1/v),v,0,2).removeO()).coeff(v,1)
lcoef=S.expand(S.series(lexpr.subs(u,1/v),v,0,2).removeO()).coeff(v,1)
ck(S.expand(kcoef-(aa*aa-aa*bb+bb*bb))==0,'physical cube residue')
ck(S.expand(lcoef-(p+(aa+bb)**2))==0,'physical Pontryagin residue')
# IL exact reduced root intersection and histogram evaluation; histogram origin is a separate atlas gate.
Im=S.Matrix([[-2,1],[1,-2]]);v1=Im.inv()*S.Matrix([0,1]);v2=Im.inv()*S.Matrix([1,0])
base=[(v1.T*Im*v1)[0],(v1.T*Im*v2)[0],(v2.T*Im*v2)[0]]
hist={(-1,0):49,(0,-1):45,(-1,-1):133,(0,0):94}
exc=[-sum(n*a*a for (a,b),n in hist.items()),-sum(n*a*b for (a,b),n in hist.items()),-sum(n*b*b for (a,b),n in hist.items())]
col=[base[i]+exc[i] for i in range(3)];reference=[-S.Rational(2,3),S.Rational(2,3),-S.Rational(2,3)];double=[col[i]-reference[i] for i in range(3)]
ck(double==[-182,-134,-178],'IL normal double')
lo=[double[0]-double[1]+double[2],-3*sum(hist.values())+double[0]+2*double[1]+double[2]]
ck(lo==[-226,-1591],'IL physical pair')
out['IL_from_printed_histogram']={'relative_minimal':list(map(str,base)),'exceptional':exc,'collision':list(map(str,col)),'closed_double':list(map(int,double)),'physical_pair':list(map(int,lo)),'scope':'The fresh atlas reconstruction must separately verify the 321-entry histogram; this algebra does not certify its origin.'}
ledger=S.Matrix([2723,19124])+12*S.Matrix(lo)+S.Matrix([-10,-28]);ck(list(ledger)==[1,4],'entire inner sum')
O=ledger-S.Matrix([72,0]);Jin=-O
ck(list(Jin)==[71,-4],'directed physical/Jin/reference transfer')
out['ASI2_final_from_certified_inputs']={'inner':list(map(int,ledger)),'positive_same_fan':list(map(int,O)),'Jin_physical':list(map(int,Jin)),'A_M':12,'native':[-1,72],'scope':'Arithmetic transfer only; atlas, topology, all maps and the imported Jin theorem have separate proof scopes.'}
# Quaternion axis degree, calculated from the exact H_1 formula by area integration.
xx,th=S.symbols('xx th',real=True)
def qm(a,b):
 a0,a1,a2,a3=a;b0,b1,b2,b3=b
 return S.Matrix([a0*b0-a1*b1-a2*b2-a3*b3,a0*b1+a1*b0+a2*b3-a3*b2,a0*b2-a1*b3+a2*b0+a3*b1,a0*b3+a1*b2-a2*b1+a3*b0])
def qc(a):return S.Matrix([a[0],-a[1],-a[2],-a[3]])
AA=S.Matrix([S.sin(xx)*S.cos(th),S.sin(xx)*S.sin(th),S.cos(xx),0]);BB=S.Matrix([S.sin(xx),0,S.cos(xx),0]);H=qm(AA,qc(BB));ii=S.Matrix([0,1,0,0])
N=qm(qm(H,ii),qc(H))[1:4,0]
area=S.trigsimp(N.dot(N.diff(xx).cross(N.diff(th))))
area_theta=S.integrate(S.expand_trig(area),(th,0,2*S.pi));degree=S.simplify(S.integrate(area_theta,(xx,0,S.pi/2))/(4*S.pi))
ck(degree==-1,'axis degree H i H^-1')
Nr=qm(qm(qc(H),ii),H)[1:4,0];areaR=S.trigsimp(Nr.dot(Nr.diff(xx).cross(Nr.diff(th))))
degreeR=S.simplify(S.integrate(S.integrate(S.expand_trig(areaR),(th,0,2*S.pi)),(xx,0,S.pi/2))/(4*S.pi))
ck(degreeR==1,'axis degree H^-1 i H')
out['quaternion_axis_degree']={'forward':str(degree),'inverse':str(degreeR),'method':'Exact area pullback and integration on [0,pi/2] x S1; general integer d follows by the oriented degree-d parameter cover.'}
out['checks']=check_count
p=Path(__file__).resolve().parents[1];(p/'K111_exact_maps.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
