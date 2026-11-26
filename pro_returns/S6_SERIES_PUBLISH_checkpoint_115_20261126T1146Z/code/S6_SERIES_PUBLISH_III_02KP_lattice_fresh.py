#!/usr/bin/env python3
"""Fresh exact lattice maps for the still-unopened OS56/II target.

Only the raw elliptic matrices and section increments are inputs. All
four-dimensional lifts, complements and relation witnesses are rebuilt.
"""
from pathlib import Path
from itertools import combinations
from datetime import datetime, timezone
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

ROOT=Path(__file__).resolve().parents[1]
A=[s.Matrix(x) for x in
   ([[5,8],[-2,-3]],[[27,37],[-19,-26]],
    [[61,80],[-45,-59]],[[4,3],[-3,-2]])]
g=[s.Matrix(x) for x in ((-2,1),(0,0),(4,-3),(1,-1))]
J=s.Matrix([[0,1],[-1,0]])
I=s.eye(2)


def integer(M):
    assert all(x.q == 1 for x in M)
    return [[int(x) for x in M.row(i)] for i in range(M.rows)]


def rational_solution(M,b):
    v,params=M.gauss_jordan_solve(b)
    return v.subs({x:0 for x in params})


def lift(a,c,p,q,weight):
    beta=-p*c.T*J*a
    z=rational_solution(a-I,q*c)
    out=s.eye(4)
    out[:2,:2]=a
    out[:2,3]=q*c
    out[2,:2]=beta
    out[2,3]=(beta*z)[0]+weight
    return out


# The saturated parabolic kernel has a direct, integral split because the
# II block of its relation is the unimodular matrix A1.
bs=[s.Matrix([2,-1]),s.eye(2),s.Matrix([4,-3]),s.Matrix([1,-1])]
prefix=s.eye(2)
blocks=[]
cblocks=[]
for a,b in zip(A,bs):
    blocks.append(prefix*b)
    cblocks.append(b.inv()*(a-I) if b.cols==2 else
                   s.Matrix([[(a-I)[0,j]/b[0] for j in range(2)]]))
    prefix=prefix*a
assert prefix==I
R=s.Matrix.hstack(*blocks)
C=s.Matrix.vstack(*cblocks)
assert R*C==s.zeros(2,2)
free=[0,3,4]
K=s.zeros(5,3)
for j,i in enumerate(free):
    K[i,j]=1
    K[1:3,j]=-A[0].inv()*R[:,i]
assert R*K==s.zeros(2,3)
gvec=s.Matrix([-1,0,0,1,1])
assert R*gvec==s.zeros(2,1)
Q=s.Matrix.hstack(C,gvec)
Qfree=Q[free,:]
assert Qfree.det()==1
quotient=Qfree.inv()*s.Matrix([[1,0,0,0,0],[0,0,0,1,0],[0,0,0,0,1]])
assert quotient*Q==s.eye(3)
assert Q*quotient*K==K
print('Parabolic relation R:',integer(R))
print('Coboundary C:',integer(C))
print('Kernel coordinates (h1,h2,g coefficient):',integer(quotient))
print('Q free determinant:',Qfree.det())

# Full height identity, including arbitrary integer coboundaries.
aa,h1,h2=s.symbols('a h1 h2')
cvec=aa*gvec+C*s.Matrix([h1,h2])
cs=[bs[0]*cvec[0],cvec[1:3,0],bs[2]*cvec[3],bs[3]*cvec[4]]
height_product=s.eye(4)
for a,c in zip(A,cs):
    height_product=height_product*lift(a,c,1,1,0)
assert s.simplify(height_product[2,3]+aa**2/s.Integer(30))==0
assert s.simplify(height_product-height_product[2,3]*s.eye(4)[:,2]*s.eye(4)[3,:])==s.eye(4)
print('Full arbitrary-coboundary height:',s.factor(-height_product[2,3]))

T=[lift(a,c,30,1,int(i==0)) for i,(a,c) in enumerate(zip(A,g))]
assert T[0]*T[1]*T[2]*T[3]==s.eye(4)
for t in T: integer(t)
omega=s.zeros(4,4)
omega[0,1]=30;omega[1,0]=-30;omega[2,3]=-1;omega[3,2]=1
assert all(t.T*omega*t==omega for t in T)
print('Full lifts:',[integer(t) for t in T])

# Cyclic order II,I5,I3,I2.
t0,t1,t2,t3=T[1],T[2],T[3],T[0]
e=s.eye(4)
gamma=e[:,3];delta=e[:,2]
wc=s.Matrix([2,-1,15,0]);rc=s.Matrix([1,0,0,0])
Hc=s.Matrix.hstack(wc,rc,delta,gamma)
assert Hc.det()==1
Nc=Hc.inv()*(t3-s.eye(4))*Hc
assert Nc==s.Matrix([[0,2,0,-1],[0,0,0,0],[0,0,0,1],[0,0,0,0]])
w1=s.Matrix([4,-3,-6,0]);a1=s.Matrix([-1,1,2,-5])
w2=s.Matrix([1,-1,-10,0]);a2=s.Matrix([1,0,0,-3])
H1=s.Matrix.hstack(w1,gamma,a1,delta)
H2=s.Matrix.hstack(w2,gamma,a2,delta)
for h,t in ((H1,t1),(H2,t2)):
    assert abs(h.det())==1
    assert h.inv()*t*h==s.eye(4)+e[:,0]*e[1,:]
print('Cusp H and inverse:',integer(Hc),integer(Hc.inv()))
print('Cusp normal form:',integer(Nc))

D=s.Matrix.hstack(t0-s.eye(4),t1-s.eye(4),t2-s.eye(4))
assert D[3,:]==s.zeros(1,12)
D=D[:3,:]
remaining=[2,3,4,5,6,7,8,9,10,11]
ell0=(t0-s.eye(4))[:2,:2]
assert ell0.det()==1


def embed(y):
    out=s.zeros(12,1)
    for i,k in enumerate(remaining):out[k]=y[i]
    out[:2,0]=-ell0.inv()*D[:2,:]*out
    return out


row=(D[2,:]*s.Matrix.hstack(*(embed(s.eye(10)[:,i]) for i in range(10))))/2
v=s.zeros(10,1);v[5]=-2;v[9]=1
assert (row*v)[0]==1
z=s.zeros(10,1);z[5]=5;z[9]=-3
assert (row*z)[0]==0
Gcols=[]
for i in range(10):
    if i not in (5,9):
        y=s.eye(10)[:,i]-row[i]*v
        Gcols.append(embed(y))
Gcols.append(embed(z))
KG=s.Matrix.hstack(*Gcols)
comp=s.zeros(12,3)
comp[:2,:2]=ell0.inv()
comp[:,2]=embed(v)
big=s.Matrix.hstack(comp,KG)
assert abs(big.det())==1
big_inv=big.inv()
assert D*comp==s.diag(1,1,2)
assert D*KG==s.zeros(3,9)
assert big_inv*big==s.eye(12)


def ji(i,x):
    if i<3:
        out=s.zeros(12,1);out[4*i:4*i+4,0]=x
        return out
    return -s.Matrix.vstack(t1*t2*x,t2*x,x)


L=s.Matrix.hstack(ji(1,w1),ji(1,a1),ji(1,delta),
                  ji(2,w2),ji(2,a2),ji(2,delta),ji(3,wc),ji(3,delta))
E=ji(0,gamma)
LG=big_inv[3:,:]*L
EG=big_inv[3:,:]*E
assert D*L==s.zeros(3,8) and D*E==s.zeros(3,1)
frame=s.Matrix.hstack(EG,LG)
print('Graph complement D*C=diag(1,1,2); full determinant:',big.det())
print('Graph sweep frame determinant:',frame.det())
print('Graph reduced map Smith diagnostic:',list(smith_normal_form(LG,domain=ZZ).diagonal()))
if frame.det():
    print('Finite delta sweep in E,L coordinates:',list(frame.inv()*big_inv[3:,:]*ji(0,delta)))

pairs=list(combinations(range(4),2))


def wedge(a):
    return s.Matrix([[a.extract(rows,cols).det() for cols in pairs] for rows in pairs])


W=s.Matrix.hstack(*(wedge(t)-s.eye(6) for t in (t0,t1,t2)))
omegarow=s.Matrix([[30,0,0,0,0,-1]])
assert omegarow*W==s.zeros(1,18)
print('Fibre degree-two relations Smith diagnostic:',list(smith_normal_form(W,domain=ZZ).diagonal()))
data=dict(parabolic_relation=integer(R),parabolic_coboundary=integer(C),
          parabolic_kernel=integer(K),parabolic_inverse_coordinates=integer(quotient),
          lifts=[integer(t) for t in T],
          cusp_basis=integer(Hc),cusp_basis_inverse=integer(Hc.inv()),
          rank_one_bases=[integer(H1),integer(H2)],
          rank_one_basis_inverses=[integer(H1.inv()),integer(H2.inv())],
          graph_differential=integer(D),graph_complement=integer(comp),
          graph_kernel=integer(KG),graph_full_inverse=integer(big_inv),
          reduced_sweep_columns=integer(L),reduced_sweep_coordinates=integer(LG),
          finite_gamma_coordinates=integer(EG),
          fibre_degree_two_relations=integer(W))
out=ROOT/'agents/continuation6_iii_infra/S6_SERIES_PUBLISH_III_02KP_lattice_maps.json'
out.write_text(json.dumps(data,indent=2)+'\n',newline='\n')
print('Exact map data:',out.relative_to(ROOT))
print('This partial calculation does not close the target or a CHECK_EVENTS row.')
print('Completed:',datetime.now(timezone.utc).isoformat())
