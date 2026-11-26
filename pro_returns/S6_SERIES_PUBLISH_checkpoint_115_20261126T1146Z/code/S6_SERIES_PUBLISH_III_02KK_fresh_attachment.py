#!/usr/bin/env python3
"""New pre-release integral maps for III 02KK; no historical code imports."""
from datetime import datetime,timezone
from itertools import combinations,product
from math import gcd
import sympy as S

R,k,l,n1,n2,r1,r2,al1,be1,al2,be2=S.symbols(
    'R k l n1 n2 r1 r2 alpha1 beta1 alpha2 beta2',integer=True)
I=S.eye(4);g,u,w,de=[I[:,j] for j in range(4)]
el=g-R*(u+w)
pairs=list(combinations(range(4),2))
def wedge(A):
    return S.Matrix([[A.extract(p,q).det() for q in pairs] for p in pairs])
def simp(A):return A.applyfunc(S.expand)
def egcd(a,b):
    aa,bb=abs(a),abs(b);x0,x1,y0,y1=1,0,0,1
    while bb:
        q,rem=divmod(aa,bb);aa,bb=bb,rem
        x0,x1=x1,x0-q*x1;y0,y1=y1,y0-q*y1
    return aa,x0*(1 if a>=0 else -1),y0*(1 if b>=0 else -1)

def diagonal_maps(M):
    """Euclidean 2x2 Smith maps, retaining every source/target operation."""
    A=[list(map(int,row)) for row in M]
    U=[[1,0],[0,1]];V=[[1,0],[0,1]]
    def swaprow():
        A[0],A[1]=A[1],A[0];U[0],U[1]=U[1],U[0]
    def swapcol():
        for B in (A,V):
            for row in B:row[0],row[1]=row[1],row[0]
    def rowadd(i,j,q):
        for B in (A,U):B[i]=[B[i][z]+q*B[j][z] for z in range(2)]
    def coladd(i,j,q):
        for B in (A,V):
            for row in B:row[i]+=q*row[j]
    nonzero=[(abs(A[i][j]),i,j) for i in range(2) for j in range(2) if A[i][j]]
    assert nonzero
    _,ii,jj=min(nonzero)
    if ii:swaprow()
    if jj:swapcol()
    steps=0
    while True:
        steps+=1
        if A[1][0]:
            rowadd(1,0,-(A[1][0]//A[0][0]))
            if A[1][0]:swaprow()
            continue
        if A[0][1]:
            coladd(1,0,-(A[0][1]//A[0][0]))
            if A[0][1]:swapcol()
            continue
        if A[1][1]%A[0][0]:
            rowadd(0,1,1)
            continue
        break
    for j in (0,1):
        if A[j][j]<0:
            A[j]=[-z for z in A[j]];U[j]=[-z for z in U[j]]
    UU,VV,AA=S.Matrix(U),S.Matrix(V),S.Matrix(A)
    assert UU*S.Matrix(M)*VV==AA
    assert abs(UU.det())==abs(VV.det())==1
    assert AA[0,1]==AA[1,0]==0 and AA[0,0]>0
    assert AA[1,1]%AA[0,0]==0
    return int(AA[0,0]),int(AA[1,1]),U,V

A2=S.Matrix([[1,0,0,0],[0,1,-1,0],[0,1,0,0],[0,0,0,1]])
E2=wedge(A2)-S.eye(6)
s=[S.eye(6)[:,j] for j in range(6)]
for typ,c,d,a in [('B',2,4,2),('C',3,3,1)]:
    A1=S.Matrix([[1,0,0,0],[0,0,1,0],[-c*R,-1,2-c,0],[-R,0,-1,1]])
    M0=(A1*A2).inv();P1=A1.inv();P2=A2.inv()
    B0=S.Matrix([[c*R,c-1],[R,1]])
    assert M0==S.eye(4)+S.zeros(2,4).col_join(B0.row_join(S.zeros(2)))
    assert B0.det()==R and A1**d==I and A2**6==I
    assert A1*el==el and A1*de==de and A2*g==g and A2*de==de
    assert P1*w==-u and P2*(-u)==w
    assert g.T*A1==g.T and g.T*A2==g.T
    print(typ,'deck/forward matrices, fixed vectors, cusp block and determinant verified')

    # Integral coinvariant maps and sections, before any parameter choices.
    Q1=S.Matrix([[1,0,0,0],[0,-1,1,-c]])
    Q2=S.Matrix([[1,0,0,0],[0,0,0,1]])
    assert Q1*(A1-I)==S.zeros(2,4) and Q2*(A2-I)==S.zeros(2,4)
    assert (A1-I)*(-u)==u+w and (A1-I)*(-u-w)==c*w+de
    assert (A2-I)*u==w and (A2-I)*(-u-w)==u
    xx=S.Matrix(S.symbols('x0:4'))
    assert xx-S.Matrix.hstack(g,w)*Q1*xx==xx[1]*(u+w)+xx[3]*(c*w+de)
    assert xx-S.Matrix.hstack(g,de)*Q2*xx==xx[1]*u+xx[2]*w
    assert de==-(A2-I)*(c*u+w)-(A1-I)*w
    print(typ,'all local and common coinvariant maps have integer sections and preimages')

    # Complete graph kernel with its explicit integral inverse.
    D=(A1-I).row_join(A2-I)
    zero=S.zeros(4,1)
    K=S.Matrix.hstack(el.col_join(zero),de.col_join(zero),
                     zero.col_join(g),(-u).col_join(w),zero.col_join(de))
    assert D*K==S.zeros(4,5)
    coords=S.Matrix(S.symbols('z0:5'))
    vv=K*coords
    assert S.Matrix([vv[0],vv[3],vv[4],vv[6],vv[7]])==coords
    aa=S.Matrix(S.symbols('a0:4'));bb=S.Matrix(S.symbols('b0:4'))
    av=aa.col_join(bb).subs({aa[1]:-R*aa[0]-bb[2],aa[2]:-R*aa[0],bb[1]:0})
    assert D*av==S.zeros(4,1)
    assert K*S.Matrix([av[0],av[3],av[4],av[6],av[7]])==av
    jw=-(A2*w).col_join(w);jd=-(A2*de).col_join(de)
    assert jw==-K[:,3] and jd==-K[:,1]-K[:,4]
    print(typ,'five graph generators, inverse coordinates and both cusp sweep cuts verified')

    # Exterior quotient, including integer preimages of every relation basis.
    E1=wedge(A1)-S.eye(6)
    xi=S.Matrix([[0,0,c*R,1,0,0]])
    assert xi*E1==xi*E2==S.zeros(1,6)
    assert E2*s[0]==s[1]
    assert -E2*s[1]-s[1]==s[0]
    assert E2*s[4]==s[5]
    assert -E2*s[5]-s[5]==s[4]
    assert s[0]+(1-c)*s[1]+R*s[4]+2*R*s[5]-E1*s[1]==s[2]-c*R*s[3]
    assert xi*s[3]==S.ones(1,1)
    print(typ,'primitive exterior quotient and all five relation preimages verified')

    m1=d*k;m2=6*l
    N1=k*sum((A1**j for j in range(d)),S.zeros(4))
    N2=l*sum((A2**j for j in range(6)),S.zeros(4))
    assert N1*g==m1*el and N1*w==-a*k*de and N1*u==a*k*de
    assert N1*de==m1*de and N2*g==m2*g and N2*de==m2*de
    assert N2*u==N2*w==S.zeros(4,1)
    X=S.zeros(4);X[0,3]=c*R;X[3,0]=-c*R;X[1,2]=1;X[2,1]=-1
    v1=n1*el+r1*de;v2=n2*g+r2*de
    assert (w.T*X*v1)[0]==R*n1 and (g.T*X*v1)[0]==c*R*r1
    assert (de.T*X*v2)[0]==-c*R*n2 and (g.T*X*v2)[0]==c*R*r2
    print(typ,'all finite norms and signed vertical contraction identities verified')

    # Target order (s,t1,D,t2); finite source order (w,z1,delta,z2).
    F=S.Matrix([[-R*n1,-c*R*r1*al1,c*R*n2,-c*R*r2*al2],
                [0,1,0,0],[-a*k,r1*be1,-m2,-r2*be2],[0,0,0,1]])
    U=S.Matrix([[1,c*R*r1*al1,0,c*R*r2*al2],
                [0,1,0,0],[0,-r1*be1,1,r2*be2],[0,0,0,1]])
    C=S.Matrix([[-R*n1,c*R*n2],[-a*k,-m2]])
    assert U.det()==1 and simp(U*F)==S.Matrix.hstack(
        S.Matrix([-R*n1,0,-a*k,0]),S.eye(4)[:,1],
        S.Matrix([c*R*n2,0,-m2,0]),S.eye(4)[:,3])
    assert S.expand(C.det()-R*(m2*n1+m1*n2))==0
    assert F.det()==C.det()
    print(typ,'full finite transfer reduces by explicit integral shear to the claimed 2x2 matrix')

    # Boundary H1 maps and sections: a_j maps to +g_j in this convention.
    J1=S.Matrix([[c*r1*be1,1,-c*r1*al1],[m1,0,n1]])
    Sec1=S.Matrix([[0,al1],[1,0],[0,be1]])
    mu1=S.Matrix([-n1,c*r1,m1])
    J2=S.Matrix([[-r2*be2,1,r2*al2],[m2,0,n2]])
    Sec2=S.Matrix([[0,al2],[1,0],[0,be2]])
    mu2=S.Matrix([-n2,-r2,m2])
    # Bezout identities are evaluated without dividing by any parameter.
    for J,Sec,mu,m,n,al,be in [(J1,Sec1,mu1,m1,n1,al1,be1),
                              (J2,Sec2,mu2,m2,n2,al2,be2)]:
        assert simp(J*mu-S.Matrix([mu[1]*(1-m*al-n*be),0]))==S.zeros(2,1)
        assert simp(J*Sec-(m*al+n*be)*S.eye(2))==S.Matrix([[1-m*al-n*be,0],[0,0]])
        assert simp(Sec*J-S.eye(3)-mu*S.Matrix([[be,0,-al]]))==S.diag(m*al+n*be-1,0,m*al+n*be-1)
    print(typ,'both finite boundary kernels and sections verified modulo the stated Bezout identity')

    Czero=C.subs({m2:m1,n2:-n1})
    # Substitute l=d*k/6 explicitly because m2 is an expression.
    Czero=C.subs({l:S.Rational(d,6)*k,n2:-n1})
    assert Czero[:,1]==c*Czero[:,0]
    print(typ,'zero-determinant matrix has exactly one independent column')

    samples=zero_count=negative_count=nontrivial_h=0
    examples=[]
    for rr,kk,ll,nn1,nn2 in product((1,2,3,4,6,8),(1,2,3),(1,2,3),(-5,-2,-1,1,2,5),(-5,-2,-1,1,2,5)):
        mm1=d*kk;mm2=6*ll
        if gcd(nn1,mm1)!=1 or gcd(nn2,mm2)!=1:continue
        PP=mm2*nn1+mm1*nn2
        hh=gcd(gcd(rr,a*kk),PP)
        Cn=[[-rr*nn1,c*rr*nn2],[-a*kk,-mm2]]
        d1,d2,UU,VV=diagonal_maps(Cn)
        assert d1==hh and d2==(rr*abs(PP)//hh if PP else 0)
        assert gcd(gcd(rr*nn1,c*rr*nn2),gcd(a*kk,mm2))==hh
        if PP==0:
            assert mm1==mm2 and nn2==-nn1
            zero_count+=1
        negative_count+=PP<0;nontrivial_h+=hh>1;samples+=1
        # Fundamental-group presentation, separately reduced by exact maps.
        p1,p2,_,_=diagonal_maps([[-nn1,mm1],[-nn2,-mm2]])
        assert p1==1 and p2==abs(PP)
        if len(examples)<3 and (PP==0 or hh>1):
            examples.append(dict(R=rr,k=kk,l=ll,n1=nn1,n2=nn2,P=PP,h=hh,U=UU,V=VV))
    print(typ,'integer cases',samples,'zero determinant',zero_count,
          'negative determinant',negative_count,'nontrivial first divisor',nontrivial_h)
    print(typ,'sample exact U,V maps',examples)

    # Original marked points: explicit comparison maps, not just matching orders.
    orig=C.subs({k:1,l:1,n1:1,n2:-1})
    if typ=='B':
        VV=S.Matrix([[3,-2],[-1,1]])
        assert orig*VV==S.diag(-R,-2) and VV.det()==1
        print('B original point: exact source map [[3,-2],[-1,1]] gives diag(-R,-2)')
    else:
        q=S.Matrix([[1,-R]])
        assert q*orig==S.Matrix([[0,3*R]])
        assert orig[:,0]==S.Matrix([-R,-1])
        print('C original point: (s,D)->s-R*D mod3R, inverse 1->s')

print('ALL FRESH SYMBOLIC MAPS AND INTEGER CASES PASS')
print('Completed UTC:',datetime.now(timezone.utc).isoformat())
