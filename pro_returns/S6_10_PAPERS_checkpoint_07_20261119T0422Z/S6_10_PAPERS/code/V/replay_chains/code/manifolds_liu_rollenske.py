"""Exact all-order certificates for D.2.9, Liu--Rollenske III*+II+I1.

Liu--Rollenske print homology matrices with T_infty*T_1*T_0=I.
The ordered tuple used here is (T_0,T_infty,T_1), whose product is I.
The unchanged II filling is the marked product with a cuspidal
elliptic neighborhood, not a finite logarithmic quotient.
"""
from pathlib import Path
from itertools import combinations
from math import gcd
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
ROOT=Path(__file__).resolve().parents[1]
A=[s.Matrix(m) for m in (
[[-1,-1,-1,0],[2,1,1,0],[0,0,1,0],[0,0,0,1]],
[[1,0,0,-1],[-2,0,-1,1],[2,1,2,1],[0,0,0,1]],
[[1,1,0,1],[-2,0,-1,-1],[0,-1,1,-1],[0,0,0,1]])]
e1,e2,e3,e4=[s.eye(4)[:,i] for i in range(4)]
delta=-e1+2*e3;ell=e4;a=e1-e2-e3
fixed=[s.Matrix.hstack(delta,ell),s.Matrix.hstack(a,delta),
       s.Matrix.hstack(delta,e4-e2)]
D=s.Matrix.hstack(A[0]-s.eye(4),A[1]-s.eye(4))
def j(i,x):
    if i==0:return x.col_join(s.zeros(4,1))
    if i==1:return s.zeros(4,1).col_join(x)
    return -(A[1]*x).col_join(x)
K=s.Matrix.hstack(j(1,a),j(1,delta),j(2,delta),j(2,e4-e2),j(0,ell))
q=s.zeros(4)
for i,jj,v in ((0,1,2),(1,2,-1),(2,3,-1)):
    q[i,jj]=v;q[jj,i]=-v

def coords(v):
    c=K.gauss_jordan_solve(v)[0]
    assert all(x.q==1 for x in c)
    return c

def finite_matrix(k,n,r):
    m=4*k
    if k<1 or gcd(n,m)!=1:raise ValueError('Need k>0,gcd(n,4k)=1.')
    alpha,beta,g=map(int,s.gcdex(m,n));assert m*alpha+n*beta==1==g
    v=n*ell+r*delta;N=k*sum((A[0]**i for i in range(4)),s.zeros(4))
    col_a=s.Matrix([-int((e3.T*q*v)[0])]).col_join(coords(j(0,N*e3)))
    col_z=s.Matrix([-alpha*int((e4.T*q*v)[0])]).col_join(
        coords(j(0,alpha*N*e4+beta*v)))
    normal=s.zeros(6,4);normal[1:5,:]=s.eye(4)
    full=normal.row_join(col_a).row_join(col_z)
    reduced=s.Matrix([[n,-2*r*alpha],[0,1]])
    assert full.det()==reduced.det()==n
    return full,reduced

def run():
    assert A[0]*A[1]*A[2]==s.eye(4) and A[0]**4==s.eye(4)
    for i in range(3):assert (A[i]-s.eye(4))*fixed[i]==s.zeros(4,2)
    assert D*K==s.zeros(4,5) and D.rank()==3
    rr=(0,1,3,4,5);assert K.extract(rr,range(5)).det()==1
    assert coords(j(0,delta))==s.Matrix([0,-1,-1,0,0])
    print('Graph kernel unit minor rows',[i+1 for i in rr],': +1.')
    print('Finite delta sweep = -K2-K3, killed by unchanged fillings.')
    pairs=list(combinations(range(4),2))
    wedge=lambda B:s.Matrix([[B.extract(i,jj).det() for jj in pairs] for i in pairs])
    B=s.Matrix.hstack(*[wedge(t)-s.eye(6) for t in A])
    omega=s.Matrix([[2,0,0,-1,0,-1]])
    assert omega*B==s.zeros(1,18)
    br=(0,1,2,3,4);bc=(1,3,4,5,10)
    assert B.extract(br,bc).det()==1
    print('Exterior unit minor rows',[i+1 for i in br],
          'columns',[i+1 for i in bc],': +1.')
    N=sum((A[0]**i for i in range(4)),s.zeros(4))
    assert N*e3==2*delta and N*e4==4*ell
    print('N4(e3)=2delta; N4(e4)=4ell.')
    checked=0
    for k in range(1,13):
        for n in range(-15,16):
            if gcd(n,4*k)!=1:continue
            for r in (0,3):
                full,reduced=finite_matrix(k,n,r)
                ds=smith_normal_form(full,domain=s.ZZ).diagonal()
                assert sorted(abs(int(x)) for x in ds)==[1]*5+[abs(n)]
                checked+=1
    print('Full 6x6 Smith matrices:',checked,
          '; 1<=k<=12,-15<=n<=15,gcd(n,4k)=1,r=0,3.')
    data=dict(A=[m.tolist() for m in A],fixed=[m.tolist() for m in fixed],
              K=K.tolist(),graph_minor_rows=rr,exterior_minor_rows=br,
              exterior_minor_cols=bc,checks=checked,examples=[])
    for k,n,r in ((1,1,0),(2,1,0),(3,-1,5),(5,3,2),(6,5,-1)):
        _,B=finite_matrix(k,n,r)
        ex=dict(m=4*k,n=n,r=r,reduced=B.tolist(),H1_to_H4_order=abs(n),
                sphere=abs(n)==1)
        data['examples'].append(ex);print(ex)
    enc=lambda x:int(x) if isinstance(x,s.Integer) else x
    (ROOT/'records/manifolds_liu_rollenske.json').write_text(
        json.dumps(data,indent=2,default=enc)+'\n')
if __name__=='__main__':run()
