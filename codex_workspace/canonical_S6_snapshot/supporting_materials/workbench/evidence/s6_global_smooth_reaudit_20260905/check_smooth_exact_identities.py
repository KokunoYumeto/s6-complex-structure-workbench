"""Independent exact algebra supplement. No file writes or numerical samples."""
import json
import sympy as s

I = s.I
sqrt = s.sqrt
R = s.Rational
checks = []

def equal(name, left, right):
    diff = left - right
    entries = list(diff) if isinstance(diff, s.MatrixBase) else [diff]
    residuals = [s.simplify(s.expand_complex(x)) for x in entries]
    if any(x != 0 for x in residuals):
        raise AssertionError((name, residuals))
    checks.append(name)

def bracket(a, b):
    return a*b-b*a

def X(v):
    return s.Matrix.vstack(s.Matrix.hstack(s.zeros(1), -v.adjoint()),
                           s.Matrix.hstack(v, s.zeros(2)))

def inertia(H, q, Y):
    raw = bracket(H, bracket(H, Y)) + q*q.adjoint()*Y + Y*q*q.adjoint()
    return raw-s.trace(raw)*s.eye(3)/3

def spatial_K(v, w, Y):
    return -bracket(X(v), bracket(X(v), Y))-bracket(X(w), bracket(X(w), Y))

r, delta = sqrt(6)/4, sqrt(R(2, 3))
x, d0 = R(1, 2), 1/(2*sqrt(2))
S = s.Matrix([[d0, -(r+x)], [r+x, d0]])/sqrt(2*r*(r+x))
U = s.diag(1, S)
H0 = s.Matrix([[0,0,0],[0,-x,d0],[0,d0,x]])
q = s.Matrix([d0,0,0])
A0 = sqrt(2)*s.Matrix([[0,-1,0],[1,0,0],[0,0,0]])
F0 = -2*H0+s.diag(-2,1,1)
equal("retained literal force", bracket(A0, bracket(A0,H0)), F0)
equal("retained U unitary", U.adjoint()*U, s.eye(3))
equal("retained U determinant", U.det(), s.Integer(1))
equal("retained U diagonalizes H0", U.adjoint()*H0*U, s.diag(0,r,-r))
equal("retained U fixes q", U*q, q)

vr1, vi1, vr2, vi2, wr1, wi1, wr2, wi2 = s.symbols(
    "vr1 vi1 vr2 vi2 wr1 wi1 wr2 wi2", real=True)
v = s.Matrix([vr1+I*vi1,vr2+I*vi2])
w = s.Matrix([wr1+I*wi1,wr2+I*wi2])
M = v*v.adjoint()+w*w.adjoint()
N = I*(v*w.adjoint()-w*v.adjoint())
a,h,zr,zi,e,t,omega = s.symbols("a h zr zi e t omega", real=True)
z = zr+I*zi
Cd = s.Matrix([[I*a,0,0],[0,I*(h-a)/2,z],[0,-s.conjugate(z),-I*(a+h)/2]])
Hd=s.diag(0,r,-r)
Fd=-2*Hd+s.diag(-2,1,1)
temporal_scalar=s.Matrix([
    [2-2*r*(M[0,0]-M[1,1]),0,0],
    [0,-4*r*(zr*zr+zi*zi)+2*r*M[0,0]-1+2*r,-2*I*r*h*z],
    [0,2*I*r*h*s.conjugate(z),4*r*(zr*zr+zi*zi)-2*r*M[1,1]-1-2*r]])
equal("full first-frame scalar matrix", bracket(Cd,bracket(Cd,Hd))+spatial_K(v,w,Hd)-Fd,temporal_scalar)
equal("full first-frame scalar vector", (Cd*Cd-X(v)*X(v)-X(w)*X(w))*q+2*q,
      (-a*a+s.trace(M)+2)*q)
equal("inertia on complete spatial class", inertia(H0,q,X(v)),X(v)/2)

H=s.Matrix([[0,0,0],[0,0,r],[0,r,0]])
F=-2*H+s.diag(-2,1,1)
C=I*e*s.diag(1,0,-1)
Q=s.diag(1,2)
E=s.diag(R(2,3),-R(5,6))
real_m=s.re(M[0,1]).expand(complex=True)
scalar=s.Matrix([[2-4*r*real_m,0,0],
 [0,2*r*real_m-1,r*(s.trace(M)-e*e+2)],
 [0,r*(s.trace(M)-e*e+2),2*r*real_m-1]])
equal("full classified scalar matrix", bracket(C,bracket(C,H))+spatial_K(v,w,H)-F,scalar)
equal("full classified scalar vector",(C*C-X(v)*X(v)-X(w)*X(w))*q+2*q,
      (s.trace(M)-e*e+2)*q)
b=s.im((v.adjoint()*w)[0]).expand(complex=True)
gamma0=e*t/6+4*e*(M[0,0]+2*M[1,1])+8*omega*b
G=e*t*E-2*e*(Q*M+M*Q)-4*omega*N
equal("full classified Gauss matrix",t*inertia(H,q,C)+2*spatial_K(v,w,C)-4*omega*bracket(X(v),X(w)),I*s.diag(gamma0,G))
equal("upper Gauss trace identity",gamma0+s.trace(G),s.Integer(0))
equal("positive-factor plus outer product",(v-I*w)*(v-I*w).adjoint(),M+N)
equal("positive-factor minus outer product",(v+I*w)*(v+I*w).adjoint(),M-N)

theta=s.symbols("theta",real=True)
zeta=s.cos(theta)+I*s.sin(theta)
eta=s.cos(2*theta)+I*s.sin(2*theta)
W=s.Matrix([[-s.conjugate(zeta),-s.conjugate(zeta)],[zeta,-zeta]])/sqrt(2)
L=s.Matrix([[-1,-1],[eta,-eta]])/sqrt(2)
# These exact angle variables cover the entire unit circle; no sample is used.
def trig_equal(name,left,right):
    diff=left-right
    vals=list(diff) if isinstance(diff,s.MatrixBase) else [diff]
    if any(s.trigsimp(s.expand_complex(s.expand(x))) != 0 for x in vals):
        raise AssertionError(name)
    checks.append(name)
B=s.diag(1,W)
Bflat=s.diag(1,L)
D=s.diag(1,zeta,zeta)
trig_equal("phase square identity",eta,zeta*zeta)
trig_equal("root-free L equals zeta W",L,zeta*W)
trig_equal("root-free frame unitary",Bflat.adjoint()*Bflat,s.eye(3))
trig_equal("root-free determinant retained",Bflat.det(),eta)
trig_equal("frame relation on all entries",Bflat,B*D)
trig_equal("same entire literal temporal matrix",U*Bflat*C*Bflat.adjoint()*U.adjoint(),U*B*C*B.adjoint()*U.adjoint())
trig_equal("same entire literal first spatial matrix",U*Bflat*X(v)*Bflat.adjoint()*U.adjoint(),U*B*X(zeta*v)*B.adjoint()*U.adjoint())
trig_equal("same entire literal second spatial matrix",U*Bflat*X(w)*Bflat.adjoint()*U.adjoint(),U*B*X(zeta*w)*B.adjoint()*U.adjoint())
expected_lower=-I*e*s.Matrix([[1,s.conjugate(eta)],[eta,1]])/2
trig_equal("entire root-free temporal lower block",(Bflat*C*Bflat.adjoint())[1:3,1:3],expected_lower)
inverse_z=-I*e*s.conjugate(eta)/2
trig_equal("literal eta inverse sign",-2*I*s.conjugate(inverse_z)/e,eta)
trig_equal("first whole spatial matrix inverse",Bflat.adjoint()*(Bflat*X(v)*Bflat.adjoint())*Bflat,X(v))
trig_equal("second whole spatial matrix inverse",Bflat.adjoint()*(Bflat*X(w)*Bflat.adjoint())*Bflat,X(w))
trig_equal("common phase leaves full M unchanged",(zeta*v)*(zeta*v).adjoint()+(zeta*w)*(zeta*w).adjoint(),M)
trig_equal("common phase leaves full N unchanged",I*((zeta*v)*(zeta*w).adjoint()-(zeta*w)*(zeta*v).adjoint()),N)

u,v0,y,tau=s.symbols("u v0 y tau",real=True)
hscalar=delta*delta+y*y
d=u*v0-hscalar
c=4*v0-5*u
coupling=72*d/c
equal("coupling u derivative",s.diff(coupling,u),72*(4*v0*v0-5*hscalar)/c**2)
equal("coupling v0 derivative",s.diff(coupling,v0),72*(4*hscalar-5*u*u)/c**2)
equal("coupling y derivative",s.diff(coupling,y),-144*y/c)
equal("positive derivative identity",4*v0*v0-5*hscalar,v0*c+5*d)
inv=(4*tau*v0+72*hscalar)/(72*v0+5*tau)
equal("coupling inverse c",c.subs(u,inv),72*(4*v0*v0-5*hscalar)/(72*v0+5*tau))
equal("coupling inverse d",d.subs(u,inv),tau*(4*v0*v0-5*hscalar)/(72*v0+5*tau))
equal("coupling inverse forward composition",coupling.subs(u,inv),tau)
equal("coupling forward inverse composition",inv.subs(tau,coupling),u)
print(json.dumps({"status":"PASS","exact_groups":len(checks),"groups":checks,
                  "sympy_version":s.__version__,"numerical_samples":0,
                  "file_writes":False},indent=2))
