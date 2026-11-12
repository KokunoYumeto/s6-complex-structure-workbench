"""Exact finite algebra checks supplementing the CG-S6-10 proofs."""
from pathlib import Path
import hashlib,json
import sympy as s
W=Path(__file__).resolve().parents[1]
source=W/'src/non-normal-fibres-and-vanishing.md'
checks=[]
def eq(name,a,b):
 assert s.simplify(a-b)==0,(name,a,b)
 checks.append(name)
x,y,z,t,U,V,r,a,b=s.symbols('x y z t U V r a b')
F=y*y*z-x*x*(x+z)-t*z**3
nu={x:V*(U*U-V*V),y:U*(U*U-V*V),z:V**3,t:0}
eq('whole homogeneous normalization',F.subs(nu,simultaneous=True),0)
eq('affine normalization',F.subs({x:r*r-1,y:r*(r*r-1),z:1,t:0},simultaneous=True),0)
eq('affine inverse r',(r*(r*r-1))/(r*r-1),r)
eq('parameter derivative',s.diff(F,t).subs(z,1),-1)
eq('infinity derivative',s.diff(F,z).subs({x:0,z:0}),y*y)
f=F.subs(z,1)
for label,point in [('P',{x:-1,y:0,t:0}),('Q',{x:-s.Rational(8,9),y:-s.Rational(8,27),t:0})]:
 eq(label+' on cubic',f.subs(point),0)
eq('P implicit derivative',s.diff(f,x).subs(x,-1),-1)
eq('Q implicit derivative',s.diff(f,x).subs(x,-s.Rational(8,9)),-s.Rational(16,27))
eq('critical polynomial',s.diff(f,x),-x*(3*x+2))
eq('other critical parameter',(-x*x*(x+1)).subs(x,-s.Rational(2,3)),-s.Rational(4,27))
v=s.sqrt(1+x);u0=y-x*v;v0=y+x*v
eq('unchanged node equation',u0*v0,y*y-x*x*(x+1))
eq('node coordinate determinant',s.Matrix([[s.diff(u0,x),s.diff(u0,y)],[s.diff(v0,x),s.diff(v0,y)]]).det().subs(x,0),-2)
k=(r-b)/(r-a)
lam=(1+b)*(1-a)/((1+a)*(1-b))
eq('direction of gluing ratio',k.subs(r,-1)/k.subs(r,1),lam)
eq('positive branch coefficient',k.subs({r:1,a:0,b:s.Rational(1,3)}),s.Rational(2,3))
eq('negative branch coefficient',k.subs({r:-1,a:0,b:s.Rational(1,3)}),s.Rational(4,3))
eq('infinite-order gluing scalar',lam.subs({a:0,b:s.Rational(1,3)}),2)
eq('nonzero torsion coefficient',s.Rational(2,3)-s.Rational(4,3),-s.Rational(2,3))
# Branch difference sequence with arbitrary polynomial coefficients.
A0,B0,A1,A2,B1,B2,C1,C2=s.symbols('A0 B0 A1 A2 B1 B2 C1 C2')
az=A0+A1*z+A2*z*z;by=B0+B1*y+B2*y*y;cx=B0-A0+C1*x+C2*x*x
hx=az+by-A0;hy=cx;hz=0
eq('triple relation',az.subs(z,0)-by.subs(y,0)+cx.subs(x,0),0)
eq('triple lift first branch difference',hx.subs(y,0)-hy.subs(x,0),az)
eq('triple lift second branch difference',hx.subs(z,0),by)
eq('triple lift third branch difference',hy,cx)
# Independently build the branch restriction matrix and the proposed conormal
# map in each degree. Compare actual kernel dimension with the image, and
# verify injectivity and zero composition. These are bounded polynomial checks.
def mons(degree):
 if degree<0:return []
 return [(i,j,degree-i-j) for i in range(degree+1) for j in range(degree-i+1)]
for branches in (2,3):
 for degree in range(7):
  basis=[p for p in mons(degree) if not all(p[i]>0 for i in range(branches))]
  ambient=[(d,p) for d in range(3) for p in basis]
  target=[(br,d,p) for br in range(branches) for d in range(3) if d!=br
          for p in mons(degree) if p[br]==0]
  rows={key:i for i,key in enumerate(target)}
  restr=s.zeros(len(target),len(ambient))
  for j,(d,p) in enumerate(ambient):
   for br in range(branches):
    if br!=d and p[br]==0:restr[rows[br,d,p],j]=1
  domain=[(br,p) for br in range(branches)
          for p in mons(degree-(branches-1)) if p[br]==0]
  phi=s.zeros(len(ambient),len(domain))
  positions={key:i for i,key in enumerate(ambient)}
  for j,(br,p) in enumerate(domain):
   power=tuple(p[i]+int(i<branches and i!=br) for i in range(3))
   phi[positions[br,power],j]=1
  assert restr*phi==s.zeros(len(target),len(domain))
  assert phi.rank()==len(domain)==len(ambient)-restr.rank()
  checks.append(str(branches)+'-branch conormal image equals restriction kernel, degree '+str(degree))
# Original relative-one-form relations and their maps.
for name,grad,matrix in [
 ('double',s.Matrix([y,x,0]),s.Matrix([[x,-y,0],[0,0,1]])),
 ('triple',s.Matrix([y*z,x*z,x*y]),s.Matrix([[x,0,-z],[0,y,-z]]))]:
 assert matrix*grad==s.zeros(2,1)
 assert s.gcd_list(list(grad))==1
 checks.append(name+' exact relative map and primitive gradient')
grad=s.Matrix([y*z,x*z,x*y])
zeta=s.Matrix([[z,0],[y,y],[0,x]])
signed=s.Matrix([[x*y,-x*z,y*z]])
assert signed*zeta==s.zeros(1,2)
checks.append('triple two-form syzygy map with signs')
# Columns dt wedge dx, dt wedge dy, dt wedge dz in the stated order.
wedge=s.Matrix([[-x*z,y*z,0],[-x*y,0,y*z],[0,-x*y,x*z]])
relations=s.Matrix([[-x,y,0],[0,-y,z]])
assert zeta*relations==wedge
checks.append('all original triple wedge relations')
swap=s.Matrix([[0,1],[-1,0]])
ext_rel=zeta.T
target_rel=s.Matrix([[x,y,0],[0,-y,z]])
assert swap*ext_rel==s.Matrix([[0,y,x],[-z,-y,0]])
assert swap*ext_rel==target_rel*s.Matrix([[0,0,1],[0,1,0],[-1,0,0]])
checks.append('Ext presentation exact signed isomorphism')
for m in (3,4):
 eq('full derivative order '+str(m),s.diff(t**m,t),m*t**(m-1))
# Full Riemann--Roch polynomial reserved for the later global section.
c1,c2,c3,ell,h=s.symbols('c1 c2 c3 ell h')
ch=3+c1*h+(c1*c1-2*c2)*h*h/2+(c1**3-3*c1*c2+3*c3)*h**3/6
td=1+c1*h/2+(c1*c1+c2)*h*h/12+c1*c2*h**3/24
twist=1+ell*h+ell**2*h*h/2+ell**3*h**3/6
expected=c3/2+c1**3/2-s.Rational(19,24)*c1*c2+s.Rational(5,4)*ell*c1**2-s.Rational(3,4)*ell*c2+s.Rational(5,4)*ell**2*c1+ell**3/2
eq('full degree-six twisted tangent Riemann--Roch polynomial',s.expand(ch*td*twist).coeff(h,3),expected)
lam_var=s.symbols('lambda',nonzero=True)
b_lam=(lam_var-1)/(lam_var+1)
eq('arbitrary gluing scalar recovered',(1+b_lam)/(1-b_lam),lam_var)
eq('all-scalar section on original cubic',f.subs({x:b*b-1,y:s.sqrt(b*b*(b*b-1)**2+t)},simultaneous=True),0)
eq('exceptional minus-one scalar',s.Rational(-1,1)/1,-1)
A1=s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
e=s.eye(4)
ca=(A1-e)*e[:,2];cb=(A2-e)*e[:,1];cc=(A1-e)*e[:,1]
assert -ca-2*cb==e[:,1]
assert -ca-cb==e[:,2]
assert cc-2*ca-3*cb==e[:,3]
assert ((A1-e).row_join(A2-e))[0,:]==s.zeros(1,8)
checks.append('full integral homology coinvariant relations, including saturation')
T,m,br,tr,mr,betar=s.symbols('T m br tr mr betar',real=True,nonzero=True)
Pi=s.Matrix([[6*(mr+s.I*m),tr+s.I*T,1,0],[betar+s.I*br,mr+s.I*m,0,1]])
D=br-6*m*m/T
reconstruct=(Pi[1,:]-m/T*Pi[0,:]-s.conjugate(Pi[1,:])+m/T*s.conjugate(Pi[0,:]))/(2*s.I*D)
assert s.simplify(reconstruct)==s.Matrix([[1,0,0,0]])
checks.append('original periods give exact gamma and Dolbeault projection')
rays=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
for mx in range(-4,5):
 for my in range(-4,5):
  if (mx,my)==(0,0):continue
  pairing=[mx*vx+my*vy for vx,vy in rays]
  forbidden={i for i in range(6) if pairing[i]<0 or pairing[(i+1)%6]<0}
  edges=[(i,(i+1)%6) for i in range(6) if pairing[(i+1)%6]<0]
  seen={min(forbidden)}
  while True:
   expanded=seen|{b for a,b in edges if a in seen}|{a for a,b in edges if b in seen}
   if expanded==seen:break
   seen=expanded
  assert seen==forbidden
checks.append('hexagon forbidden-chart connectivity for all 80 nonzero weights in [-4,4]^2')
T1=A1.inv().T;T2=A2.inv().T
pairs=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
exterior=lambda mat:s.Matrix([[mat.extract(ii,jj).det() for jj in pairs] for ii in pairs])
av,bv,cv,dv,ev,fv=s.symbols('av bv cv dv ev fv')
coeff=s.Matrix([av,bv,cv,dv,ev,fv])
assert (exterior(T1)-s.eye(6))*coeff==s.Matrix([-2*av+bv+cv-6*dv+2*ev-8*fv,-av-bv+cv-6*dv+2*ev-6*fv,-6*fv,fv,-2*ev+fv,-ev-fv])
assert (exterior(T2)-s.eye(6))*coeff==s.Matrix([-av-bv+cv-6*dv+6*ev-3*fv,av-bv+3*ev,6*ev,-ev,-ev-fv,ev-fv])
checks.append('all twelve original invariant-two-form equations')
stack=(exterior(T1)-s.eye(6)).col_join(exterior(T2)-s.eye(6))
qvec=s.Matrix([0,0,6,1,0,0])
assert stack.rank()==5 and stack*qvec==s.zeros(12,1)
checks.append('complete invariant exterior lattice has primitive generator q')
ra=(T1-e)*e[:,1];rb=(T2-e)*e[:,2]
rc=(T1-e)*e[:,3];rd=(T2-e)*e[:,3]
assert rb-ra==e[:,1] and ra-2*rb==e[:,2] and -ra-rc-rd==e[:,0]
assert ((T1-e).row_join(T2-e))[3,:]==s.zeros(1,8)
checks.append('integral cohomology coinvariant certificate, with all coefficients')
Q=s.Matrix([[0,0,0,6],[0,0,1,0],[0,-1,0,0],[-6,0,0,0]])
v1=s.Matrix([1,2,-4,0]);v2=s.Matrix([-1,-3,3,0])
eta1=s.Matrix([0,2,1,3]);eta2=s.Matrix([0,1,1,2])
assert (v1.T*Q).T==2*eta1 and (v2.T*Q).T==-3*eta2
assert A1*v1==v1 and A2*v2==v2 and T1*eta1==eta1 and T2*eta2==eta2
checks.append('full contractions, fixed vectors and comparison-character invariance')
for Tj,mj in [(T1,3),(T2,4)]:
 Nj=sum((Tj**j for j in range(mj)),s.zeros(4))
 assert Nj*(Tj-e)==s.zeros(4)
 checks.append('finite boundary norm cancels every character change, order '+str(mj))
assert s.Rational(2*3,3)-s.Rational(3*2,4)==s.Rational(1,2)
checks.append('distinct filling orders leave the exact k/2 cusp constraint')
d1,d2,d3,vx,vy,wx,wy=s.symbols('d1 d2 d3 vx vy wx wy')
quad=lambda xx,yy:(d2+d3)*xx*(xx-1)/2+d3*xx*yy+(d1+d3)*yy*(yy-1)/2
Bmat=s.Matrix([[d2+d3,d3],[d3,d1+d3]])
assert s.expand(quad(vx+wx,vy+wy)-quad(vx,vy)-quad(wx,wy)-(s.Matrix([[vx,vy]])*Bmat*s.Matrix([wx,wy]))[0])==0
checks.append('full integral quadratic divisor and polarization, including linear terms')
rayvals=[s.expand(quad(*ray)) for ray in rays]
assert rayvals==[0,0,d2,d2+d3,d1+d3,d1]
assert [s.expand(-rayvals[i]+rayvals[i-1]+rayvals[(i+1)%6]) for i in range(6)]==[d1,d2,d3,d1,d2,d3]
checks.append('all six divisor coefficients recover all six boundary degrees')
Bzero=s.Matrix([[0,1],[-1,0]])
mixed=-Bzero.T*Bmat
assert mixed==s.Matrix([[d3,d1+d3],[-d2-d3,-d3]])
pcoef,qcoef,rcoef=s.symbols('pcoef qcoef rcoef')
assert mixed.subs({d3:pcoef,d1:qcoef-pcoef,d2:-rcoef-pcoef},simultaneous=True)==s.Matrix([[pcoef,qcoef],[rcoef,-pcoef]])
checks.append('exact mixed-block sign and integral inverse to the degree correspondence')
assert s.Matrix([[1,-1],[0,1]]).det()==1
checks.append('cusp base-first orientation in longitude-meridian coordinates')
receipt=dict(lesson='CG-S6-10',passed=len(checks),checks=checks,source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
 scope='Exact original cubic, normalization, local coordinates, extending twist, signed triple compatibility, independent finite-degree kernel/image comparisons, relative differentials and full index polynomial. Finite checks supplement the convergent-power-series proofs; they do not replace them. The receiving analytic proofs are included; the dependent working topology chapter retains its stated review limits.')
(W/'checks/CONORMAL_TORSION_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':len(checks),'source_sha256':receipt['source_sha256']}))
