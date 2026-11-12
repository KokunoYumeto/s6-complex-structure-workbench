"""Exact finite checks for the original framing matrices and quadratic algebra."""
from pathlib import Path
from itertools import product,permutations
import hashlib,json
import sympy as S
W=Path(__file__).resolve().parents[1]
source=W/'src/the-original-six-dimensional-framing-invariant.md'
checks=[]
def check(value,name):
    assert value,name
    checks.append(name)
def left(q):
    a,b,c,d=q
    return S.Matrix([[a,-b,-c,-d],[b,a,-d,c],[c,d,a,-b],[d,-c,b,a]])
def conjugate(q):return S.Matrix([q[0],-q[1],-q[2],-q[3]])
quaternions=set()
for seed in [(1,0,0,0),(S.Rational(1,2),)*4,(S.Rational(3,5),S.Rational(4,5),0,0)]:
    for p in set(permutations(seed)):
        for signs in product([-1,1],repeat=4):
            quaternions.add(tuple(x*y for x,y in zip(p,signs)))
Q=[S.Matrix(q) for q in sorted(quaternions,key=str)]
I4=S.eye(4);I3=S.eye(3);I7=S.eye(7)
# Original target order is imaginary first factor, imaginary second factor, collar.
CA=S.zeros(7);CB=S.zeros(7)
for i in range(3):
    CA[i,i+1]=1;CA[i+3,i+4]=1
    CB[i,i+4]=-1;CB[i+3,i+1]=1
CA[6,0]=-1;CB[6,0]=-1
check(CA.det()==-1 and CB.det()==-1,'Both original product comparison matrices retain the negative collar determinant')
P=S.zeros(7)
for i,j in enumerate([0,1,2,3,5,6,4]):P[i,j]=1
for qi,q in enumerate(Q):
    L=left(q);Lb=left(conjugate(q))
    check(L.T*L==I4 and L*Lb==I4,f'Original quaternion inverse and full norm {qi}')
    R=(I4-q*q.T).row_join(-q).col_join((-q.T).row_join(S.zeros(1)))
    check(R.T*R==S.eye(5) and R.det()==-1,f'Local-sphere reflection retains every entry {qi}')
    v=q.col_join(S.ones(1))/S.sqrt(2)
    check(R==S.eye(5)-2*v*v.T,f'Exact local-sphere reflection identity {qi}')
    A=P*S.diag(R,S.eye(2))
    direct=S.zeros(7);direct[:4,:4]=I4-q*q.T;direct[:4,4]=-q
    direct[4,5]=1;direct[5,6]=1;direct[6,:4]=-q.T
    check(A==direct,f'Original local-sphere target permutation and negative collar {qi}')
    for C,label in [(CA,'A'),(CB,'B')]:
        actual=C*S.diag(Lb,I3)
        check(C.inv()*actual==S.diag(Lb,I3),f'Based product matrix for factor {label} {qi}')
Hs=[S.zeros(3),I3,-I3,S.Matrix([[1,2,-1],[0,-3,4],[5,0,2]])]
for i in range(3):
    for j in range(3):
        h=S.zeros(3);h[i,j]=1;Hs.extend([h,-h])
for hi,H in enumerate(Hs):
    tang=I3.col_join(H);normal=(-H.T).col_join(I3)
    check(tang.T*normal==S.zeros(3),f'Actual graph tangent and normal orthogonality {hi}')
    for t in [0,S.Rational(1,3),1]:
        D=I3.row_join(-t*H.T).col_join((t*H).row_join(I3))
        check(D.det()==(I3+t*t*H*H.T).det()>0,f'Full graph contraction determinant {hi} {t}')
    q=Q[hi%len(Q)];Lb=left(conjugate(q));hblock=Lb[1:4,:]
    actual=S.zeros(7);actual[:3,:4]=hblock;actual[:3,4:7]=-H.T
    actual[3:6,:4]=H*hblock;actual[3:6,4:7]=I3;actual[6,:4]=-Lb[0,:]
    D=I3.row_join(-H.T).col_join(H.row_join(I3))
    check(actual==S.diag(D,S.ones(1))*CA*S.diag(Lb,I3),f'Full original graph framing factorization {hi}')
check(S.Matrix([[0,1],[-1,0]]).det()==1,'Original integral product intersection matrix')

def parity(x):return x.bit_count()&1
def pairing(x,y,g):
    return sum(((x>>(2*i))&1)*((y>>(2*i+1))&1)+((x>>(2*i+1))&1)*((y>>(2*i))&1) for i in range(g))&1
def form(x,mask,g):
    return (parity(x&mask)+sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(g)))&1
def span(basis):
    out={0}
    for b in basis:out|={x^b for x in tuple(out)}
    return out
def zero_lagrangian(mask,g):
    V=list(range(1<<(2*g)));chosen=[];maps=[]
    for step in range(g):
        e=next(x for x in V if x and form(x,mask,g)==0)
        f=next(x for x in V if pairing(e,x,g))
        fp=f^(e if form(f,mask,g) else 0)
        project=lambda v:v^(e if pairing(v,fp,g) else 0)^(fp if pairing(v,e,g) else 0)
        sub=[x for x in V if not pairing(x,e,g) and not pairing(x,fp,g)]
        maps.append(all(project(v) in sub and v==(project(v)^(e if pairing(v,fp,g) else 0)^(fp if pairing(v,e,g) else 0)) for v in V))
        chosen.append(e);V=sub
    return chosen,all(maps)
forms=0
for g in range(4):
    V=range(1<<(2*g))
    for mask in V:
        forms+=1
        q=lambda x:form(x,mask,g)
        arf=sum(((mask>>(2*i))&1)*((mask>>(2*i+1))&1) for i in range(g))&1
        G=sum((-1)**q(x) for x in V);N0=sum(q(x)==0 for x in V)
        check(all(q(x^y)==(q(x)^q(y)^pairing(x,y,g)) for x in V for y in V),f'Complete original quadratic identity g={g} mask={mask}')
        check(G==(1<<g)*(-1)**arf and N0==((1<<(2*g))+G)//2,f'Gauss sum and both exact fibre counts g={g} mask={mask}')
        if arf==0:
            basis,maps=zero_lagrangian(mask,g);L=span(basis)
            check(maps and len(L)==1<<g and all(q(x)==0 for x in L) and all(pairing(x,y,g)==0 for x in L for y in L),f'Constructed original zero-valued Lagrangian and full inverse projections g={g} mask={mask}')
        reductions=[]
        for e in V:
            if not e or q(e):continue
            perp=[v for v in V if pairing(v,e,g)==0]
            cosets={min(v,v^e) for v in perp}
            reductions.append(len(cosets)==1<<(2*g-2) and all(q(v)==q(v^e) for v in perp) and G==2*sum((-1)**q(v) for v in cosets))
        check(all(reductions),f'All zero-line reductions with original quotient maps g={g} mask={mask}')
        if g:
            g1=g//2;mask1=mask&((1<<(2*g1))-1);mask2=mask>>(2*g1)
            G1=sum((-1)**form(v,mask1,g1) for v in range(1<<(2*g1)))
            G2=sum((-1)**form(v,mask2,g-g1) for v in range(1<<(2*(g-g1))))
            check(G==G1*G2,f'Orthogonal sum with all original coordinates g={g} mask={mask}')
check([form(x,3,1) for x in [0,1,2,3]]==[0,1,1,1],'All four values of the original anisotropic plane')
u,v,w,t=S.symbols('u v w t',real=True)
F=S.Matrix([u,v,w*w,u*w,v*w,w**3-t*w])
J=F.jacobian([u,v,w])
target=S.eye(6);target[3,0]=-w;target[4,1]=-w
residual=S.Matrix([2*w,u,v,3*w*w-t])
expected=S.zeros(6,3);expected[0,0]=expected[1,1]=1;expected[2:6,2]=residual
check(target.det()==1 and target*J==expected,'Full six-coordinate derivative reduction including the original cubic')
check(residual.jacobian([u,v,w,t]).det()==-2,'Exact signed four-dimensional local derivative degree')
Jplus=J.subs({u:0,v:0,t:w*w})
Jminus=J.subs({u:0,v:0,w:-w,t:w*w},simultaneous=True)
check(S.expand(Jplus.row_join(Jminus).det())==32*w**5,'Full six-column double-point determinant including the fifth power')
check(F.subs({u:0,v:0,t:w*w})==F.subs({u:0,v:0,w:-w,t:w*w},simultaneous=True),'Both original sheet values coincide on w squared equals t')
for a in [S.Rational(1,5),S.Rational(3,5),S.Rational(7,3)]:
    check(Jplus.row_join(Jminus).subs(w,a).det()==32*a**5,'Positive ordered intersection determinant at '+str(a))
check(Jplus.row_join(Jminus).subs(w,S.Rational(3,5)).det()==S.Rational(7776,3125),'Exercise 1 retains all six exact columns and determinant')
rho,aa,bb,cc=S.symbols('rho aa bb cc',real=True)
point=S.Matrix([u,v,w]);direction=S.Matrix([aa,bb,cc])
subplus={z:y+rho*d/2 for z,y,d in zip([u,v,w],point,direction)}
subminus={z:y-rho*d/2 for z,y,d in zip([u,v,w],point,direction)}
divided=(F.subs(subplus,simultaneous=True)-F.subs(subminus,simultaneous=True))/rho
divided=divided.applyfunc(S.expand)
check((divided.subs(rho,0)-J*direction).applyfunc(S.expand)==S.zeros(6,1),'Exact divided difference extends to the complete vertical derivative')
check(divided[5]==3*w*w*cc+rho*rho*cc**3/4-t*cc,'Divided cubic retains its rho squared correction')
check(S.det(S.eye(3).row_join(S.eye(3)).col_join(S.eye(3).row_join(-S.eye(3))))==-8,'Original Whitney immersion ordered sheet determinant')
for qi,q in enumerate(Q):
    radial=q*q.T;tan=I4-radial
    reflection=I4-2*radial
    check(reflection*reflection==I4 and reflection*q==-q,'Exact stable collar radial reflection '+str(qi))
    for radius,speed in [(S.Rational(2,3),S.Rational(7,5)),(S.Rational(9,4),S.Rational(1,3))]:
        comparison=radius*tan-radial/speed
        inverse=tan/radius-speed*radial
        check(comparison*inverse==I4 and comparison.det()==-radius**3/speed,'Full original radius and collar speed with inverse '+str((qi,radius,speed)))
    for cosine,sine in [(S.Integer(1),S.Integer(0)),(S.Rational(3,5),S.Rational(4,5)),(S.Integer(0),S.Integer(1))]:
        vv=(cosine*q).col_join(S.Matrix([sine]));RR=S.eye(5)-2*vv*vv.T
        check(RR*RR==S.eye(5) and RR.det()==-1,'Full appended-coordinate reflection homotopy '+str((qi,cosine,sine)))
origJ=S.diag(S.Matrix([[0,1],[-1,0]]),S.Matrix([[0,-1],[1,0]]),S.Matrix([[0,1],[-1,0]]))
xx,yy,uu1,vv1,uu2,vv2=S.symbols('x y u1 v1 u2 v2')
zz=S.Matrix([xx,yy,uu1,vv1,uu2,vv2])
check((origJ*zz)[2]==-vv1 and (origJ*zz)[4]==vv2 and origJ.det()==1,'Exercise 2 original integral belt signs and unimodularity')
vals=[form(x,11,3) for x in range(64)]
check(vals.count(0)==28 and vals.count(1)==36 and sum((-1)**z for z in vals)==-8,'Exercise 2 all 64 original quadratic values and Gauss sum')
L=span([4,16]);perp=[x for x in range(64) if pairing(x,4,3)==pairing(x,16,3)==0]
check(len(perp)==16 and all(form(x,11,3)==form(x&3,3,1) for x in perp),'Full two-belt perpendicular quotient and original projected quadratic function')
for g in range(3):
    for mask in range(1<<(2*g)):
        G=sum((-1)**form(x,mask,g) for x in range(1<<(2*g)))
        for belts in range(4):
            for beltvals in range(1<<belts):
                large_mask=mask
                for j in range(belts):large_mask|=((beltvals>>j)&1)<<(2*(g+j)+1)
                Gplus=sum((-1)**form(x,large_mask,g+belts) for x in range(1<<(2*(g+belts))))
                check(Gplus==(1<<belts)*G,'Complete index-three Gauss factor '+str((g,mask,belts,beltvals)))
report=dict(source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),passed=len(checks),quaternion_samples=len(Q),graph_derivative_matrices=len(Hs),quadratic_forms=forms,checks=checks,scope='Exact original quaternion and framing matrices, all small quadratic spaces, the complete local singularity derivative and divided difference, every collar radius/speed comparison, both worked examples and zero-belt Gauss reductions. The written geometric homotopy, quadratic, bordism and nullbordism proofs are separate arguments; these finite checks do not independently certify them or the smooth-recognition proof supplied in the sphere-twist companion.')
(W/'checks/FRAMED_SIX_OBSTRUCTION_CHECKS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='checks'}))
