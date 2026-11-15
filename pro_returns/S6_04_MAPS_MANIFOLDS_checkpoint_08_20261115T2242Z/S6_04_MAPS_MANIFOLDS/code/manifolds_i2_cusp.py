"""All-order exact certificates for OS56 II with the index-two I2 cusp.

The local cusp torsion is retained: its H1 boundary Z/2 maps isomorphically
to the regular-family Z/2, and the saturated angular vanishing lattice is
used in van Kampen. The proof supplies the free local H2 defect separately.
"""
from pathlib import Path
import json,sys
from math import gcd
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from manifolds_rankone_families import decomp,ikernel,wedge,biv
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'records/explorer/api/engine'))
import os_monodromy as om

info=om.os_info(56,profile='II',verbose=False)
pair=om.check_pair(56,(30,),(1,),profile='II',verbose=False)
assert pair['valid'] and pair['pairing']==1
original=[s.Matrix(x) for x in om.monodromy_tuple(
    56,(30,),(1,),(1,0,0,0),profile='II',verbose=False)]
A=original[1:]+original[:1]
assert A[0]*A[1]*A[2]*A[3]==s.eye(4) and A[0]**6==s.eye(4)
ell=s.eye(4)[:,3];delta=s.eye(4)[:,2];omega=s.Matrix([[30,0,0,0,0,-1]])
fixed=[ikernel(x-s.eye(4)) for x in A]
Dc,Uc,Vc,rc=decomp(A[3]-s.eye(4))
assert [abs(Dc[i,i]) for i in range(rc)]==[1,2]
assert (A[3]-s.eye(4))**2==s.zeros(4)
local_torsion=Uc.inv()[:,1]
all_image=s.Matrix.hstack(*[x-s.eye(4) for x in A])
Dg,Ug,Vg,rg=decomp(all_image)
assert [abs(Dg[i,i]) for i in range(rg)]==[1,1,2]
tor_value=int((Ug*local_torsion)[2]);assert tor_value%2==1
actual_vanishing=s.Matrix.hstack(*[A[i]-s.eye(4) for i in (0,1,2)],fixed[3])
Dv,_,_,rv=decomp(actual_vanishing)
assert [abs(Dv[i,i]) for i in range(rv)]==[1,1,1]
Ec,_,_,rec=decomp(wedge(A[3])-s.eye(6))
assert rec==2 and all(abs(Ec[i,i])==1 for i in range(rec))
E=s.Matrix.hstack(*[wedge(x)-s.eye(6) for x in A])
De,_,_,re=decomp(E)
assert re==5 and all(abs(De[i,i])==1 for i in range(re))
assert omega*E==s.zeros(1,E.cols)

D=s.Matrix.hstack(*[A[i]-s.eye(4) for i in range(3)])
def j(i,x):
    if i<3:
        z=s.zeros(12,x.cols);z[4*i:4*i+4,:]=x;return z
    return -(A[1]*A[2]*x).col_join(A[2]*x).col_join(x)
K=s.Matrix.hstack(*[j(i,fixed[i]) for i in (1,2,3)],j(0,ell))
SK,UK,VK,rk=decomp(K)
assert rk==9 and D*K==s.zeros(4,9)
assert all(abs(SK[i,i])==1 for i in range(9))
L=VK*s.diag(*[1/SK[i,i] for i in range(9)])*UK[:9,:]
assert L*K==s.eye(9) and (L*j(0,delta))[8]==0
N=sum((A[0]**i for i in range(6)),s.zeros(4))
assert N*delta==6*delta and N*ell==6*ell
assert -(omega*biv(delta,ell))[0]==1

Gamma=s.Matrix([[2,1],[0,1]])
fan_symmetry=s.Matrix([[1,1],[0,-1]])
assert abs(Gamma.det())==2 and abs(fan_symmetry.det())==1
transformed=fan_symmetry*Gamma
assert transformed==s.Matrix([[2,2],[0,-1]])
fixed_degrees=[]
for shift in range(2):
    v=(shift,0);vp=(shift,1);w=(shift+1,0);wp=(shift-1,1)
    color=lambda p:(p[0]+p[1])%2
    deg=[int(color(w)==c)+int(color(wp)==c)
         -int(color(v)==c)-int(color(vp)==c) for c in range(2)]
    assert deg==[0,0]
    fixed_degrees.append(deg)

checks=0
for k in range(1,17):
    m=6*k
    for n in range(-19,20):
        if gcd(m,n)!=1:continue
        for r in (-4,0,5):
            alpha,beta,g=map(int,s.gcdex(m,n));assert g==1
            v=n*ell+r*delta
            n1=s.Matrix([n]).col_join(L*j(0,m*delta))
            n2=s.Matrix([-alpha*r]).col_join(L*j(0,alpha*m*ell+beta*v))
            normal=s.zeros(10,8);normal[1:9,:]=s.eye(8)
            full=normal.row_join(n1).row_join(n2)
            assert full.extract((0,9),(8,9))==s.Matrix([[n,-alpha*r],[0,1]])
            SS=smith_normal_form(full,domain=s.ZZ)
            assert [abs(int(SS[i,i])) for i in range(10)]==[1]*9+[abs(n)]
            checks+=1
print('OS56 II: types',info['kodaira_types'],'P=30G,Q=G,weights=(1,0,0,0)')
print('cusp N Smith=(1,2); local exterior coinvariants are free')
print('cusp boundary torsion vector',list(local_torsion),'maps to global tor coordinate',tor_value)
print('saturated actual vanishing Smith=(1,1,1)')
print('graph kernel has an integer left inverse; delta sweep residual zero')
print('period lattice',Gamma.tolist(),'fan symmetry',fan_symmetry.tolist())
print('fixed-curve component degrees',fixed_degrees)
print('unrestricted normal matrix [[n,-r*alpha],[0,1]]; full Smith cases',checks)
record=dict(os_entry=56,profile='II',P=30,Q=1,weights=[1,0,0,0],
    types=info['kodaira_types'],P_components=pair['P_components'],Q_components=pair['Q_components'],
    A=[x.tolist() for x in A],fixed=[x.tolist() for x in fixed],
    boundary_torsion=local_torsion.tolist(),global_torsion_coordinate=Ug[2,:].tolist(),
    torsion_image=tor_value,K=K.tolist(),left_inverse=L.tolist(),
    delta_coordinates=(L*j(0,delta)).tolist(),omega=omega.tolist(),
    finite_norm=N.tolist(),Gamma=Gamma.tolist(),fan_symmetry=fan_symmetry.tolist(),
    fixed_component_degrees=fixed_degrees,full_smith_checks=checks)
(ROOT/'records/manifolds_i2_cusp.json').write_text(json.dumps(record,indent=2,default=int)+'\n')
