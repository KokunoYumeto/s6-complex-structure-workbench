"""Supplementary exact algebra checks; the geometric proof is in the source."""
from pathlib import Path
import hashlib,json,math,random,re
import sympy as s
W=Path(__file__).resolve().parents[1]
source=W/'src/sphere-twists-and-the-original-smooth-six-sphere-comparison.md'
checks=[]
def check(name,condition):
    assert condition,name
    checks.append(name)
def symplectic(r):
    return s.zeros(r).row_join(s.eye(r)).col_join((-s.eye(r)).row_join(s.zeros(r)))
def twist(v,m=1):
    r=len(v)//2;return s.eye(2*r)+m*v*(v.T*symplectic(r))
def pairturn(r,i):
    e=s.eye(2*r)
    return twist(e[:,i])*twist(e[:,r+i])*twist(e[:,i])
def mixed(r,i,j,m):
    e=s.eye(2*r);u=e[:,i];v=e[:,r+j]
    return twist(u+v,m)*twist(u,-m)*twist(v,-m)
def align(v):
    r=len(v)//2;M=s.eye(2*r);v=s.Matrix(v)
    def apply(A):
        nonlocal M,v
        v=A*v;M=A*M
    for i in range(r):
        while v[r+i]:
            b=int(v[r+i]);q=int(v[i])//abs(b)*(1 if b>0 else -1)
            apply(twist(s.eye(2*r)[:,i],-q));apply(pairturn(r,i))
        if v[i]<0:apply(pairturn(r,i)**2)
    for j in range(1,r):
        while v[j]:
            b=int(v[j]);q=int(v[0])//abs(b)*(1 if b>0 else -1)
            apply(mixed(r,0,j,q))
            # (A,B) -> (A-B,B) -> (A-B,A) -> (-B,A)
            apply(mixed(r,0,j,1));apply(mixed(r,j,0,-1));apply(mixed(r,0,j,1))
    if v[0]<0:apply(pairturn(r,0)**2)
    return M,v
def lagrangian_to_e(L):
    r=L.cols
    if r==0:return s.zeros(0)
    M,v=align(L[:,0]);assert v==s.eye(2*r)[:,0]
    A=M*L
    if r>1:
        rows=list(range(1,r))+list(range(r+1,2*r))
        sub=A.extract(rows,list(range(1,r)));N=lagrangian_to_e(sub)
        lift=s.eye(2*r)
        for i,row in enumerate(rows):
            for j,col in enumerate(rows):lift[row,col]=N[i,j]
        M=lift*M
    assert (M*L)[r:,:]==s.zeros(r)
    assert abs((M*L)[:r,:].det())==1
    return M
# All radial coefficients in the differential and inverse.
r,t,p=s.symbols('r theta theta_prime',positive=True,real=True)
c=s.cos(t);z=s.sin(t)
rot=s.Matrix([[c,z/r],[-r*z,c]])
inv=s.Matrix([[c,-z/r],[r*z,c]])
check('radius-dependent rotation inverse',s.simplify(rot*inv)==s.eye(2))
check('metric constraints',s.simplify(rot*s.diag(1,r*r)*rot.T)==s.diag(1,r*r))
check('full radial derivative',
 s.simplify(rot.diff(r)+rot.diff(t)*p-s.Matrix([[-z*p,c*p/r-z/r**2],[-z-r*c*p,-z*p]]))==s.zeros(2))
# Signed degree in the original polar coordinates.
rr,tt=s.symbols('rr tt',positive=True)
check('fibre signed volume coefficient',s.diff(s.cos(tt),tt)==-s.sin(tt))
check('negative polar degree with both volume factors',s.sign(-s.Rational(7,3)*s.sin(s.pi/3)**2/s.Rational(9,16))==-1)
rng=random.Random(61011)
for rank in [1,2,3]:
    J=symplectic(rank);I=s.eye(2*rank)
    for n in range(18):
        v=s.Matrix([rng.randrange(-5,6) for _ in range(2*rank)]);m=rng.randrange(-6,7)
        A=twist(v,m)
        check(f'transvection pairing {rank}:{n}',A.T*J*A==J)
        check(f'transvection inverse {rank}:{n}',A*twist(v,-m)==I)
        check(f'transvection full power {rank}:{n}',twist(v)**m==A)
    for i in range(rank):
        A=pairturn(rank,i);a=s.symbols('x:'+str(2*rank));x=s.Matrix(a);y=A*x
        check(f'signed pair rotation {rank}:{i}',y[i]==x[rank+i] and y[rank+i]==-x[i])
        for j in range(rank):
            if i==j:continue
            y=mixed(rank,i,j,3)*x;expected=x.copy();expected[i]-=3*x[j];expected[rank+j]+=3*x[rank+i]
            check(f'both mixed coordinates {rank}:{i}:{j}',y==expected)
    for n in range(24):
        while True:
            v=s.Matrix([rng.randrange(-15,16) for _ in range(2*rank)])
            if math.gcd(*map(int,v))==1:break
        A,y=align(v)
        check(f'primitive termination and image {rank}:{n}',y==I[:,0])
        check(f'primitive full pairing {rank}:{n}',A.T*J*A==J)
    for n in range(12):
        A=I
        for _ in range(7):
            v=s.Matrix([rng.randrange(-2,3) for _ in range(2*rank)])
            A=twist(v,rng.choice([-2,-1,1,2]))*A
        L=A[:,:rank];N=lagrangian_to_e(L)
        K=-J
        check(f'lagrangian exact pairing {rank}:{n}',N.T*J*N==J)
        check(f'lagrangian complementary image {rank}:{n}',(K*N*L)[:rank,:]==s.zeros(rank) and abs((K*N*L)[rank:,:].det())==1)
# The original skew correction with all integer coefficients.
for rank in [2,3,4]:
    e=s.eye(2*rank);J=symplectic(rank)
    A=s.Matrix(rank,rank,lambda i,j:rng.randrange(-8,9))
    Y=e[:,rank:]+e[:,:rank]*A;C=Y.T*J*Y
    upper=s.Matrix(rank,rank,lambda i,j:C[i,j] if i<j else 0)
    F=Y+e[:,:rank]*upper
    check(f'full skew correction {rank}',F.T*J*F==s.zeros(rank) and e[:,:rank].T*J*F==s.eye(rank))
    frame=e[:,:rank].row_join(F)
    check(f'integral inverse-coordinate basis {rank}',frame.det()==1 and frame.T*J*frame==J)
# Both worked examples, including the old torsion and signed comparisons.
e=s.eye(2);A=twist(e[:,0],-2)*twist(e[:,1])
check('exercise 8.1 entire matrix',A==s.Matrix([[3,-2],[-1,1]]))
check('exercise 8.1 original vector',A*s.Matrix([2,3])==s.Matrix([0,1]))
check('exercise 8.1 old torsion',abs(s.Matrix([[-3]]).det())==3)
check('exercise 8.1 signed comparison',s.Matrix([[-1]])**2==s.eye(1))
e=s.eye(4);J=symplectic(2)
A=twist(e[:,0]+e[:,3],2)*twist(e[:,2],-1)*twist(e[:,1],3)
check('exercise 8.2 full original word',A==s.Matrix([[3,-2,2,-6],[0,1,0,3],[1,0,1,0],[2,-2,2,-5]]))
L=A[:,:2];D=s.diag(-1,1)*e[:,:2].T*J*L
check('exercise 8.2 old incidence',D==s.Matrix([[-1,0],[2,-2]]))
check('exercise 8.2 exact torsion quotient',abs(D.det())==2 and math.gcd(*map(int,D))==1)
P=-J*A.inv()
check('exercise 8.2 full new gluing',P==s.Matrix([[1,2,-3,0],[0,-2,2,-1],[1,2,-2,0],[0,-5,6,-3]]))
check('exercise 8.2 actual target basis',P*L==e[:,2:])
check('exercise 8.2 signed new incidence',s.diag(-1,1)*e[:,:2].T*J*P*L==s.diag(-1,1))
x=s.Matrix(s.symbols('a1 a2 b1 b2'));m=s.symbols('m',integer=True)
y=twist(e[:,0]+e[:,3],m)*x
check('exercise 8.2 both companion changes',s.simplify(y-s.Matrix([x[0]+m*(x[2]-x[1]),x[1],x[2],x[3]+m*(x[2]-x[1])]))==s.zeros(4,1))
# The full stable-framing homotopy, with sheared frames and a nonorthogonal embedding.
Jemb=s.diag(1,2,3,4,5,6).col_join(s.Matrix([[1,-1,2,-2,3,-3],[2,0,1,0,-1,2]]))
H=Jemb.T*Jemb;Q=H.inv()*Jemb.T;Pnu=s.eye(8)-Jemb*Q
check('original Gram projection identities',Q*Jemb==s.eye(6) and Pnu*Jemb==s.zeros(8,6) and Pnu+Jemb*Q==s.eye(8))
for k in [0,2,4]:
    tau=s.eye(6+k)
    for i in range(6+k-1):tau[i,i+1]=s.Rational(i+1,i+2)
    J0=s.diag(*([s.Matrix([[0,-1],[1,0]])]*((6+k)//2)))
    Jk=s.diag(*([s.Matrix([[0,-1],[1,0]])]*(k//2))) if k else s.zeros(0)
    Iop=tau.inv()*J0*tau
    check(f'stable frame complex operator {k}',Iop**2==-s.eye(6+k))
    size=14+k
    def matrix(ct,st,inverse=False):
        ca=ct**2-st**2;sa=2*ct*st
        C=ca*s.eye(6+k)+sa*Iop;R=s.diag(s.eye(6),ca*s.eye(k)+sa*Jk)
        D=R*C;Di=(ca*s.eye(6+k)-sa*Iop)*s.diag(s.eye(6),ca*s.eye(k)-sa*Jk)
        result=[]
        for col in range(size):
            x=s.eye(size)[:,col];v=x[:6,0];a=x[6:14,0];b=x[14:,0];u=Q*a;y=Pnu*a
            if not inverse:
                vt=ct*v+st*u;wb=D*((-st*v+ct*u).col_join(b));at=y+Jemb*wb[:6,0];bt=wb[6:,0]
                result.append(vt.col_join(at).col_join(bt))
            else:
                wb=Di*(u.col_join(b));z=wb[:6,0];bt=wb[6:,0];vt=ct*v-st*z;ut=st*v+ct*z
                result.append(vt.col_join(y+Jemb*ut).col_join(bt))
        return s.Matrix.hstack(*result)
    for j,(ct,st) in enumerate([(s.Integer(1),s.Integer(0)),(s.Rational(3,5),s.Rational(4,5)),(s.Integer(0),s.Integer(1))]):
        A=matrix(ct,st);B=matrix(ct,st,True)
        check(f'full stable homotopy two-sided inverse {k}:{j}',A*B==s.eye(size) and B*A==s.eye(size))
        if j==0:check(f'stable homotopy initial identity {k}',A==s.eye(size))
        if j==2:
            endpoint=s.zeros(size);endpoint[:6,6:14]=Q;endpoint[6:14,:6]=Jemb;endpoint[6:14,6:14]=Pnu
            if k:endpoint[14:,14:]=s.eye(k)
            check(f'original full involution endpoint {k}',A==endpoint)
src=source.read_text('utf-8');tags=re.findall(r'\\tag\{([^}]+)\}',src)
check('unique numbered source equations',len(tags)==len(set(tags)))
check('all nine source sections present',len(re.findall(r'^## \d+\.',src,re.M))==9)
check('two complete exercise solutions',src.count('**Solution.**')==2)
for term in [r'D^{\rm old}_{ij}=\sigma_i\lambda(b_i,a_j)',r'D^\phi=U',r'\epsilon_j\sigma_i\delta_{ij}',r'D\phi_p\oplus1\oplus I_h',r'd\simeq g',r'\Theta_6=0']:
    check('retained receiving formula '+term,term in src)
report=dict(status='passed',passed=len(checks),source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),source=str(source.name),formulas=len(re.findall(r'\\\(.*?\\\)|\\\[.*?\\\]',src,re.S)),checks=checks,limits='Finite algebra supplements the complete written proof. It does not certify topology, source reading, geometric existence or independent review.')
(W/'checks/SPHERE_TWIST_CHECKS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='checks'}))
