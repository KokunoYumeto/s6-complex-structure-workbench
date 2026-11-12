"""Exact finite checks supplementing the integral handle-chain proofs."""
from pathlib import Path
import hashlib,json
import sympy as S
W=Path(__file__).resolve().parents[1]
checks=[]
def ck(name,ok):
    assert bool(ok),name
    checks.append(name)
def zero(m):return all(S.expand(v)==0 for v in m)
# Independent ordered-frame permutation: outward normal before the u-frame.
for p in range(1,7):
    I=S.eye(p+2)
    normal_first=I[:,[p]+list(range(p))+[p+1]]
    ck(f'Outward-normal permutation at lower index {p}',normal_first.det()==(-1)**p)
    for eps in [-1,1]:
        for sign in [-1,1]:
            attaching=S.diag(sign,*([1]*(p-1)))
            intersection=eps*(-1)**p*attaching.det()
            ck(f'Original chart and incidence signs p={p} eps={eps} c={sign}',
               eps*(-1)**p*intersection==sign)
# Entire symbolic unit contraction, for both signs, including incoming/outgoing.
a1,a2,b1,b2,e11,e12,e21,e22=S.symbols('a1 a2 b1 b2 e11 e12 e21 e22')
a=S.Matrix([[a1,a2]]);b=S.Matrix([b1,b2]);E=S.Matrix([[e11,e12],[e21,e22]])
for eps in [-1,1]:
    D=S.Matrix([[eps,a1,a2],[b1,e11,e12],[b2,e21,e22]])
    U=S.eye(3);U[0,1]=-eps*a1;U[0,2]=-eps*a2
    V=S.Matrix([[eps,0,0],[b1,1,0],[b2,0,1]])
    Z=E-b*eps*a
    diag=S.diag(S.Matrix([[1]]),Z)
    ck(f'Full unit differential including Schur term eps={eps}',zero(V.inv()*D*U-diag))
    pk=S.Matrix([[0,1,0],[0,0,1]])
    ik=S.Matrix([[-eps*a1,-eps*a2],[1,0],[0,1]])
    pl=S.Matrix([[-eps*b1,1,0],[-eps*b2,0,1]])
    il=S.Matrix([[0,0],[1,0],[0,1]])
    h=S.diag(eps,0,0)
    ck(f'Unit source projection-inclusion eps={eps}',pk*ik==S.eye(2))
    ck(f'Unit target projection-inclusion eps={eps}',pl*il==S.eye(2))
    ck(f'Unit projection chain equation eps={eps}',zero(pl*D-Z*pk))
    ck(f'Unit inclusion chain equation eps={eps}',zero(D*ik-il*Z))
    ck(f'Original source homotopy eps={eps}',zero(S.eye(3)-ik*pk-h*D))
    ck(f'Original target homotopy eps={eps}',zero(S.eye(3)-il*pl-D*h))
    ck(f'Unit side condition ph eps={eps}',zero(pk*h))
    ck(f'Unit side condition hi eps={eps}',zero(h*il))
# Original six-dimensional example.
A=S.Matrix([[2,3,5]]);B=S.Matrix([[-3,-4],[2,1],[0,1]])
section=S.Matrix([-1,1,0]);U=section.row_join(B)
Ui=S.Matrix([[2,3,5],[-1,-1,-3],[0,0,1]])
h3=Ui[1:,:]
ck('Six-dimensional original AB is zero',A*B==S.zeros(1,2))
ck('Six-dimensional complete comparison inverse',U*Ui==Ui*U==S.eye(3))
ck('Six-dimensional retained determinant',U.det()==1)
ck('Six-dimensional original section',A*section==S.eye(1))
ck('Six-dimensional original chain contraction middle',B*h3+section*A==S.eye(3))
ck('Six-dimensional original contraction at top',h3*B==S.eye(2))
ck('Six-dimensional contraction square',h3*section==S.zeros(2,1))
ck('Six-dimensional original row contains no unit',all(abs(x)>1 for x in A))
# Seven-dimensional example formed with independent integral basis matrices.
# Ranks r=2, s=4, t=3, u=1.
U3=S.eye(4)
for i,j,c in [(0,2,3),(3,1,-2),(1,0,2),(2,3,5)]:
    F=S.eye(4);F[i,j]=c;U3=U3*F
U4=S.eye(3)
for i,j,c in [(0,2,-3),(1,0,4),(2,1,2)]:
    F=S.eye(3);F[i,j]=c;U4=U4*F
A0=S.Matrix([[1,0,0,0],[0,1,0,0]])
B0=S.Matrix([[0,0,0],[0,0,0],[1,0,0],[0,1,0]])
D0=S.Matrix([0,0,1])
A=A0*U3.inv();B=U3*B0*U4.inv();D=U4*D0
section=U3[:,:2];K=U3[:,2:];L=U4[:,:2]
Kinv=U3.inv()[2:,:];Bt=Kinv*B;Dinv=U4.inv()[2:,:]
h2=section;h3=L*Kinv*(S.eye(4)-section*A)
h4=Dinv*(S.eye(3)-L*Bt)
ck('Seven-dimensional original adjacent products',A*B==S.zeros(2,3) and B*D==S.zeros(4,1))
ck('Seven-dimensional exact kernel lift',B*L==K)
ck('Seven-dimensional first transformed differential',A*U3==A0)
ck('Seven-dimensional middle transformed differential',U3.inv()*B*U4==B0)
ck('Seven-dimensional last transformed differential',U4.inv()*D==D0)
ck('Seven-dimensional original contraction at degree two',A*h2==S.eye(2))
ck('Seven-dimensional original contraction at degree three',B*h3+h2*A==S.eye(4))
ck('Seven-dimensional original contraction at degree four',D*h4+h3*B==S.eye(3))
ck('Seven-dimensional original contraction at degree five',h4*D==S.eye(1))
ck('Seven-dimensional full contraction square',h3*h2==S.zeros(3,2) and h4*h3==S.zeros(1,4))
# Negative pivot: verify all exact integer operations, including the torsion.
D=S.Matrix([[-1,2,-3],[4,7,11],[-5,13,17]])
a=D[0,1:];b=D[1:,0];E=D[1:,1:];Z=E+b*a
ck('Negative pivot retains every original cross term',Z==S.Matrix([[15,-1],[3,32]]))
ck('Original determinant has negative pivot sign',D.det()==-483)
ck('Uncorrected block would give different torsion',E.det()!=483)
colswap=S.Matrix([[0,1],[1,0]]);rowadd=S.Matrix([[1,0],[32,1]])
coladd=S.Matrix([[1,15],[0,1]]);rowneg=S.diag(-1,1)
ck('First torsion operation',Z*colswap==S.Matrix([[-1,15],[32,3]]))
ck('Second torsion operation',rowadd*Z*colswap==S.Matrix([[-1,15],[0,483]]))
ck('Third torsion operation',rowadd*Z*colswap*coladd==S.diag(-1,483))
ck('Complete integral torsion comparison',rowneg*rowadd*Z*colswap*coladd==S.diag(1,483))
# Full elementary basis comparison on two neighbouring original matrices.
A=S.Matrix([[2,3,5]]);B=S.Matrix([[-3,-4],[2,1],[0,1]])
U=S.eye(3);U[0,2]=7
ck('Elementary inverse has the required negative sign',U.inv()==S.eye(3)-7*S.eye(3)[:,0]*S.eye(3)[2,:])
ck('Both neighbouring transformed matrices still compose to zero',(A*U)*(U.inv()*B)==S.zeros(1,2))
ck('Changing only one neighbouring matrix can break the chain equation',(A*U)*B!=S.zeros(1,2))
src=W/'src/integral-handle-chains-and-signed-incidences.md'
result=dict(source=src.name,source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),
            passed=len(checks),checks=checks,
            scope='Finite exact symbolic, sign and matrix checks. The singular-homology, transversality and geometric claims are justified by the written proofs, not certified by these finite checks.',
            independent_review=False)
(W/'checks/HANDLE_CHAIN_CHECKS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(checks=len(checks),sha256=result['source_sha256'])))
