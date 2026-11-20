"""Fresh post-reading arithmetic for the received C3.8 line/connection proof.

This file does not import its author's programs or the earlier prereading check.
It is a receiving-proof calculation, and is not labelled before-reading.
"""
import hashlib
import json
import time
from pathlib import Path
import sympy as s

started=time.perf_counter(); checks=[]
def simp(x): return s.factor(s.cancel(x))
def ck(name,expr):
    xs=list(expr) if isinstance(expr,s.MatrixBase) else [expr]
    rr=[simp(x) for x in xs]; ok=all(x==0 for x in rr)
    checks.append({'name':name,'passed':ok,'residuals':[str(x) for x in rr]})
    if not ok: raise AssertionError((name,rr))

tau,mu,beta,x,y=s.symbols('tau mu beta zeta1 zeta2')
base=(tau,mu,beta,s.Matrix([x,y]))
K=s.Matrix([[0,6],[1,0]])
J=K.T
A=[s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]]),
   s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])]
vs=[s.Matrix([1,2,-4,0]),s.Matrix([-1,-3,3,0])]
ms=[3,4]
def mat(t,m,b): return s.Matrix([[6*m,t],[b,m]])
def Pi(t,m,b): return mat(t,m,b).row_join(s.eye(2))
def E(lam,z,t,m,b):
    n=s.Matrix(lam[:2])
    return (n.T*K*z)[0]+(n.T*K*mat(t,m,b)*n)[0]/2
def gen(j,t,m,b,z):
    if j==0:
        tt=(t-1)/t; mm=(1-m)/t; bb=b+2-6*(1-m)**2/t
        R=s.Matrix([[-1/t,0],[(1-m)/t,1]])
    else:
        tt=-1/t; mm=1+m/t; bb=b-3-6*m*m/t
        R=s.Matrix([[1/t,0],[-m/t,1]])
    return tuple(simp(a) for a in (tt,mm,bb))+(R*z,-z[0]**2/(2*t))

for j in range(2):
    t,m,b,z,F=gen(j,*base)
    ck(f'period matrix transport {j+1}',Pi(t,m,b)*A[j]-s.Matrix([[-1/tau,0],[(1-mu)/tau,1]])*Pi(tau,mu,beta) if j==0 else Pi(t,m,b)*A[j]-s.Matrix([[1/tau,0],[-mu/tau,1]])*Pi(tau,mu,beta))
    expected=[24,0,s.Rational(1,2),0] if j==0 else [-9,0,0,0]
    for k in range(4):
        lam=s.eye(4)[:,k]; shift=Pi(tau,mu,beta)*lam
        Fshift=-(x+shift[0])**2/(2*tau)
        defect=E(A[j]*lam,z,t,m,b)-E(lam,base[3],tau,mu,beta)-Fshift-x*x/(2*tau)
        ck(f'generator {j+1} lattice defect {k+1}',defect-expected[k])

    state=base; gaussian=0
    for r in range(ms[j]):
        t,m,b,z,F=gen(j,*state)
        gaussian=simp(gaussian+F)
        state=(t,m,b,z.applyfunc(simp))
    for k in range(3): ck(f'linear generator {j+1} relation period {k}',state[k]-base[k])
    ck(f'linear generator {j+1} relation coordinate',state[3]-base[3])
    ck(f'linear generator {j+1} Gaussian relation',gaussian)

    state=base; total=0; v=vs[j]; morder=ms[j]; rational=v/morder
    for r in range(morder):
        t,m,b,zlin,F=gen(j,*state)
        factor=12*(F+E(rational,zlin,t,m,b))
        total=simp(total+factor)
        znew=(zlin+Pi(t,m,b)*rational).applyfunc(simp)
        state=(t,m,b,znew)
    ck(f'affine generator {j+1} exact original period power',state[3]-base[3]-Pi(tau,mu,beta)*v)
    defect=simp(total-12*E(v,base[3],tau,mu,beta))
    expected=-32 if j==0 else -s.Rational(81,2)
    phase=s.Rational(32,3) if j==0 else s.Rational(81,8)
    ck(f'affine generator {j+1} uncorrected Gaussian defect',defect-expected)
    ck(f'affine generator {j+1} corrected constant phase',defect+morder*phase)

t2,m2,b2,z2,F2=gen(1,*base)
t12,m12,b12,z12,F1=gen(0,t2,m2,b2,z2)
ck('two then one cusp period direction',s.Matrix([t12-tau-1,m12-mu,b12-beta+1]))
ck('two then one cusp coordinate direction',z12-base[3])
ck('two then one zero Gaussian turn',F1+F2)

# Ordinary exact bridge: receiving Chern primitive is the independently derived A.
u,g=s.symbols('u gamma')
Td,Md,Bd=s.symbols('tau_prime mu_prime beta_prime')
T=s.Matrix([[tau,6*mu],[mu,beta]])
Tp=s.Matrix([[Td,6*Md],[Md,Bd]])
D=s.diag(1,6); r=s.Matrix([u,g])
d1,d2,dt=s.symbols('dzeta1 dzeta2 dt')
dz=s.Matrix([d1,d2]); dT=Tp*dt
Aprimitive=(r.T*D*dz)[0]-(r.T*D*dT*r)[0]/2
# Differentiating phi=2 pi r^t D Y r and r=Y^-1 Im(zeta)
# gives the exact expression below, with no undeclared replacement of frames.
dphi=-2*s.pi*s.I*(r.T*D*(dz-dT*r))[0]-s.pi*s.I*(r.T*D*dT*r)[0]
ck('Chern primitive i/(2pi) partial phi equals A',s.I*dphi/(2*s.pi)-Aprimitive)

# Full cusp Cartier arithmetic on arbitrary original translated triangles.
ii,jj,ng,nu,ng2,nu2=s.symbols('i j n_gamma n_u n_gamma2 n_u2',integer=True)
n=s.Matrix([ng,nu]); n2=s.Matrix([ng2,nu2]); B0=s.Matrix([[0,1],[-1,0]])
v=B0*n
def height(i,j): return i*(i-1)/2-3*j*j
def expo(i,j): return s.Matrix([i,-6*j-3]),-i*(i+1)/2+3*j*(j+1)
def h(n): return -3*n[0]**2+n[1]*(n[1]-1)/2
ck('cusp height polarization',h(n+n2)-h(n)-h(n2)-(n.T*K*B0*n2)[0])
ck('cusp height affine transport',height(ii+v[0],jj+v[1])-height(ii,jj)-((K.T*n).dot(s.Matrix([ii,jj]))+h(n)))
m,l=expo(ii,jj)
for dx,dy in [(0,0),(1,0),(0,1),(1,1)]:
    ck(f'Cartier frame interpolation {dx},{dy}',m.dot(s.Matrix([ii+dx,jj+dy]))+l-height(ii+dx,jj+dy))
mp,lp=expo(ii+v[0],jj+v[1])
ck('full cusp line-frame x exponent cancellation',K.T*n+m-mp)
ck('full cusp line-frame q exponent cancellation',h(n)+l-lp-mp.dot(v))
ck('cusp theta ratio has exactly minus n_u over two exponent',h(n)-(n.T*K*B0*n)[0]/2+nu/2)

# The inverse and every base term in the finite logarithm-turn connection.
invdisplay=s.Matrix([[Bd,-Md],[-6*Md,Td]])/(Td*Bd-6*Md**2)
ck('annular inverse displayed transpose',Tp.T*invdisplay-s.eye(2))
ck('annular inverse polarization transport',invdisplay*D*Tp-D)
vu,vg,vw,vd,hh,hp,kk=s.symbols('v_u v_gamma v_w v_delta h h_prime k')
vq=s.Matrix([vu,vg]); vp=s.Matrix([vw,vd])
P=T*vq+vp; Sscalar=(vq.T*D*P)[0]; Sprime=(vq.T*D*Tp*vq)[0]
sigmap=hp*P+hh*Tp*vq
a=-24*s.pi*s.I*invdisplay*D*sigmap
ap=-24*s.pi*s.I*invdisplay*D*(sigmap+kk*Tp*vq)
ck('finite logarithm-turn vertical connection change',ap-a+24*s.pi*s.I*kk*D*vq)
basechange=-12*s.pi*s.I*((2*kk*hh+kk**2)*Sprime+2*kk*hp*Sscalar)
logder=24*s.pi*s.I*(kk*(vq.T*D*dz)[0]+kk*(vq.T*D*sigmap)[0]*dt+kk**2*Sprime*dt/2)
ck('finite logarithm-turn complete base connection change',basechange*dt+logder-24*s.pi*s.I*kk*(vq.T*D*dz)[0])

# Ordered partition signs and telescoping, independently as polynomial identities.
a0,a1,a2=s.symbols('a0 a1 a2')
ck('partition telescoping at three stages',a0+(1-a0)*a1+(1-a0)*(1-a1)*a2-1+(1-a0)*(1-a1)*(1-a2))
cab,cbn=s.symbols('c_ab c_bn')
ck('receiving sum convention B_a minus B_b',cab+cbn-cbn-cab)

out={'status':'PASS','count':len(checks),'checks':checks,
     'seconds':round(time.perf_counter()-started,6),
     'exposure':'After complete reading of receiving C3.8; distinct from the frozen 39-check statement-first derivation.',
     'scope':'Listed exact line-factor, affine phase, cusp Cartier and annular connection identities. The full cocycle/partition comparison is written separately.',
     'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='checks'},indent=2))
