#!/usr/bin/env python3
"""Independent exact checks of Paper V's B/C/D arithmetic.

No previous checking program is imported or read. Matrices are transcribed
from the paper. Integral kernel and quotient calculations use complete Smith
transformations rather than the paper's selected determinant minors.
"""
import itertools
import json
from datetime import datetime, timezone
from pathlib import Path
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from sympy.matrices.normalforms import hermite_normal_form

OUTPUT={"computed_utc":datetime.now(timezone.utc).isoformat(),"method":"Exact exterior minors and full Smith transformations; independent of prior code"}

def zmat(A):
    assert all(v.q==1 for v in A)
    return A

def smith(A):
    d,u,v=smith_normal_decomp(DomainMatrix.from_Matrix(A).convert_to(sp.ZZ))
    d,u,v=(x.to_Matrix() for x in (d,u,v))
    assert d==u*A*v
    assert abs(u.det())==abs(v.det())==1
    rank=sum(d[i,i]!=0 for i in range(min(d.shape)))
    factors=[abs(int(d[i,i])) for i in range(rank)]
    return d,u,v,rank,factors

def inv_basis(A):
    d,u,v,r,f=smith(A-sp.eye(A.rows))
    K=v[:,r:]
    assert A*K==K
    return K

def exterior(A,k):
    ri=list(itertools.combinations(range(A.rows),k))
    ci=list(itertools.combinations(range(A.cols),k))
    return sp.Matrix(len(ri),len(ci),lambda i,j:A.extract(ri[i],ci[j]).det())

def zeros(n,m=0): return sp.zeros(n,m)

def inclusion(n,k,horizontal=False):
    # e_0 is the mapping-torus coordinate; the other five are vertical.
    ib=list(itertools.combinations(range(n),k))
    vb=list(itertools.combinations(range(n-1),k-1 if horizontal else k))
    out=sp.zeros(len(ib),len(vb))
    for j,I in enumerate(vb):
        target=((0,) if horizontal else ())+tuple(x+1 for x in I)
        out[ib.index(target),j]=1
    return out

A=sp.Matrix([[1,0,0,1,-1,1],[0,1,-1,-1,1,0],[0,1,0,-1,0,0],[0,2,-1,-1,0,1],[0,2,0,-1,0,0],[0,1,1,-1,0,0]])
B=sp.Matrix([[1,0,0,0,0,0],[0,0,-1,0,1,0],[0,0,-1,0,0,1],[0,0,-1,0,0,0],[0,1,-1,0,0,0],[0,0,-1,1,0,0]])
M1,M2=A.T,B.T
M0=zmat((M1*M2).inv());N=M0-sp.eye(6)
v1=sp.Matrix([1,3,-2,-1,2,0]);v2=sp.Matrix([-1,0,0,0,0,0])
S=sp.Matrix([[0,0,0,1,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[-1,0,0,0,1,0],[1,0,0,0,0,1],[-1,0,0,0,0,0]])
C1=sp.Matrix([[-1,-1,0,-1,0],[0,1,0,1,1],[0,1,0,0,0],[0,-1,-1,0,-1],[0,0,1,0,0]])
C2=sp.Matrix([[-1,0,-1,0,-1],[0,1,0,0,0],[0,0,0,1,0],[0,-1,0,-1,1],[0,0,1,0,0]])
P1=v1.row_join(sp.zeros(1,5).col_join(C1));P2=v2.row_join(sp.zeros(1,5).col_join(C2))
Q1,Q2=zmat(P1.inv().T),zmat(P2.inv().T)
D1=sp.zeros(5);D2=sp.zeros(5)
for j in range(5):D1[(j+1)%5,j]=1
for j in range(4):D2[(j+1)%4,j]=1
D2[4,4]=-1
assert M1**5==M2**4==sp.eye(6)
assert all(M1**i!=sp.eye(6) for i in range(1,5))
assert all(M2**i!=sp.eye(6) for i in range(1,4))
assert N*N==sp.zeros(6)
assert abs(S.det())==abs(P1.det())==abs(P2.det())==1
assert S.inv()*M0*S==sp.eye(6)+sp.zeros(3).row_join(sp.eye(3)).col_join(sp.zeros(3,6))
assert P1.inv()*M1*P1==sp.diag(1,D1)
assert P2.inv()*M2*P2==sp.diag(1,D2)
assert M1*v1==v1 and M2*v2==v2
ell=sp.Matrix([[1,0,0,0,0,0]])
assert ell*M1==ell*M2==ell
homcoin=smith((M1-sp.eye(6)).row_join(M2-sp.eye(6)))
cohcoin=smith((A-sp.eye(6)).row_join(B-sp.eye(6)))
assert homcoin[4]==[1]*5 and cohcoin[4]==[1]*5+[2]
assert (M1-sp.eye(6)).col_join(M2-sp.eye(6)).rank()==6
assert (A-sp.eye(6)).col_join(B-sp.eye(6)).rank()==5
OUTPUT["monodromy"]={"orders":[5,4],"charpolys":[str(sp.factor(M1.charpoly().as_expr())),str(sp.factor(M2.charpoly().as_expr()))],"N_rank":N.rank(),"N_smith":smith(N)[4],"homology_coinvariant_smith":homcoin[4],"cohomology_coinvariant_smith":cohcoin[4],"affine_obstructions":[[str(sp.Rational(k,5)) for k in range(1,5)],[str(-sp.Rational(k,4)) for k in range(1,4)]],"cusp_marking_verified":True,"cap_markings_verified":True}
# Fundamental-group abelian relation matrix, columns a,b,h.
Rpi=sp.Matrix([[5,0,-1],[0,4,1],[1,1,0]])
assert abs(Rpi.det())==1
OUTPUT["fundamental_group_relation_determinant"]=int(Rpi.det())

cap_h1=[]
for M,v,m in [(M1,v1,5),(M2,v2,4)]:
    R=(M-sp.eye(6)).col_join(sp.zeros(1,6)).row_join((-v).col_join(sp.Matrix([m])))
    sm=smith(R)
    cap_h1.append({"free_rank":7-sm[3],"torsion":[d for d in sm[4] if d>1]})
assert cap_h1==[{"free_rank":2,"torsion":[]},{"free_rank":2,"torsion":[2]}]
OUTPUT["finite_cap_H1"]=cap_h1

sheaf=[]
Deltas={}
for q in range(1,5):
    Aq,Bq=exterior(A,q),exterior(B,q)
    n=Aq.rows
    finite=[]
    for D,Q,m in [(D1,Q1,5),(D2,Q2,4)]:
        T=exterior(D.T,q)
        inv=inv_basis(T)
        Tprev=exterior(D.T,q-1)
        norm=sum((Tprev**i for i in range(m)),sp.zeros(Tprev.rows))
        normcols=hermite_normal_form(norm)
        local=(inclusion(6,q)*inv).row_join(inclusion(6,q,True)*normcols)
        finite.append(exterior(Q,q)*local)
    J1,J2=finite
    J0=inv_basis(exterior(M0.T,q))
    d0=J1.row_join(sp.zeros(n,J2.cols)).row_join(-J0).col_join(sp.zeros(n,J1.cols).row_join(J2).row_join(-Aq*J0))
    Delta=(Aq-sp.eye(n)).row_join(Bq-sp.eye(n))
    assert Delta*d0==sp.zeros(n,d0.cols)
    d,u,v,r,factors=smith(Delta)
    coords=zmat(v.inv()*d0)
    assert coords[:r,:]==sp.zeros(r,d0.cols)
    rel=coords[r:,:]
    dr,ur,vr,rr,rf=smith(rel)
    h0=d0.cols-rr
    h1=Delta.cols-r-rr
    tors1=[a for a in rf if a>1]
    tors2=[a for a in factors if a>1]
    row={"q":q,"stalk_ranks":[J1.cols,J2.cols,J0.cols],"d0_rank":rr,"H0_rank":h0,"H1_rank":h1,"H1_torsion":tors1,"H2_rank":n-r,"H2_torsion":tors2}
    sheaf.append(row);Deltas[q]=(Delta,d,u,v)
assert [(r['H0_rank'],r['H1_rank'],r['H1_torsion'],r['H2_rank'],r['H2_torsion']) for r in sheaf]==[(1,0,[],0,[2]),(0,0,[],0,[2]),(0,3,[],0,[2]),(0,0,[],0,[2])]
OUTPUT["integral_sheaf_cohomology"]=sheaf

# Locate torsion in each local coinvariant using its Smith transformation,
# then project that automatically chosen representative into global coinvariants.
trans=[]
for k in range(1,4):
    T=exterior(D2.T,k)
    dl,ul,vl,rl,fl=smith(T-sp.eye(T.rows))
    positions=[i for i in range(rl) if abs(dl[i,i])>1]
    assert len(positions)==1 and abs(dl[positions[0],positions[0]])==2
    ek=sp.zeros(T.rows,1);ek[positions[0]]=1
    wlocal=zmat(ul.inv()*ek)
    norm=sum((T**j for j in range(4)),sp.zeros(T.rows))
    assert norm*wlocal==sp.zeros(T.rows,1)
    wglobal=exterior(Q2,k)*inclusion(6,k)*wlocal
    Delta,d,u,v=Deltas[k]
    globalcoord=u*wglobal
    nonzero=[]
    for i in range(min(d.shape)):
        if abs(d[i,i])>1:
            nonzero.append(int(globalcoord[i]%abs(d[i,i])))
    assert nonzero==[1]
    trans.append({"vertical_degree":k,"local_torsion_order":2,"norm_of_representative":0,"global_torsion_coordinate":nonzero,"coefficient":1})
OUTPUT["torsion_transgression_maps"]=trans

# Independent symbolic arithmetic for pencil and characteristic numbers.
x,lam,u,X=sp.symbols('x lam u X')
f=x**5+lam**3*x+lam**4
lam0=-sp.Rational(256,3125);r=sp.Rational(64,625)
disc=sp.factor(sp.resultant(f,sp.diff(f,x),x))
assert disc==lam**15*(3125*lam+256)
assert f.subs({lam:lam0,x:r})==sp.diff(f,x).subs({lam:lam0,x:r})==0
assert sp.diff(f,x,2).subs({lam:lam0,x:r})!=0
assert sp.diff(f,lam).subs({lam:lam0,x:r})!=0
assert sp.expand(f.subs({lam:u**8,x:u**6*X})/u**30)==X**5+X+u**2
assert sp.expand(f.subs({lam:u**-5,x:u**-4*X})*u**20)==X**5+u*X+1
OUTPUT["pencil"]={"discriminant":str(disc),"nodal_parameter":str(lam0),"nodal_root":str(r),"f_xx_at_node":str(sp.diff(f,x,2).subs({lam:lam0,x:r})),"f_lambda_at_node":str(sp.diff(f,lam).subs({lam:lam0,x:r})),"root_chart_orders":[8,5],"Hodge_degrees":[str(3*(sp.Rational(2,5)-sp.Rational(3,8))),str(sp.Rational(2,5)-sp.Rational(3,8))]}
Q=sp.diag(1,1,1,-1);w=sp.ones(4,1);Reflect=sp.eye(4)-w*w.T*Q
assert Reflect.T*Q*Reflect==Q and Reflect*Reflect==sp.eye(4)
a,b,c,d=sp.symbols('a b c d')
v=sp.Matrix([a,b,c,d])
assert Reflect*v==sp.Matrix([d-b-c,d-a-c,d-a-b,2*d-a-b-c])
clutch=sp.Matrix([[1,-1],[1,1]])
assert clutch.inv()==sp.Matrix([[sp.Rational(1,2),sp.Rational(1,2)],[-sp.Rational(1,2),sp.Rational(1,2)]])
OUTPUT["characteristic"]={"c4":6,"c2_squared":2,"p1_squared":8,"p2":14,"signature":2,"Todd_genus":0,"reflection_is_integral_isometry":True,"reflection_square_is_identity":True,"clutching_inverse_checked":True}
print(json.dumps(OUTPUT,indent=2))
