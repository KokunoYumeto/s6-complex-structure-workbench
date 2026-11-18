"""Unbounded order-4k logarithmic transforms for III* + 3 I1.

Exact certificates for Theorem D.2.6. Matrices are the primary K11/
Viaclovsky marking. Primitive integer kernels are supplied explicitly;
no rational nullspace basis is mistaken for an integral lattice basis.
"""
from pathlib import Path
from itertools import combinations
from math import gcd
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

ROOT = Path(__file__).resolve().parents[1]
T = [s.Matrix(M) for M in (
    [[1,0,-2,-1],[0,0,-1,0],[0,1,0,-1],[0,0,0,1]],
    [[1,0,2,2],[0,1,1,1],[0,0,1,0],[0,0,0,1]],
    [[1,0,0,0],[0,1,0,0],[0,-1,1,0],[0,0,0,1]],
    [[1,0,0,-1],[0,1,1,0],[0,0,1,0],[0,0,0,1]])]
A = [t.inv().T for t in T]
E = [s.eye(4)[:, j] for j in range(4)]
psi, u, w, delta = E
ell = psi-u-w
fixed = [s.Matrix.hstack(ell,delta),
         s.Matrix.hstack(-psi+2*u,w,delta),
         s.Matrix.hstack(psi,u,delta),
         s.Matrix.hstack(w,delta)]
D = s.Matrix.hstack(*[a-s.eye(4) for a in A[:3]])


def peripheral(i, v):
    if i < 3:
        result=s.zeros(12,1)
        result[4*i:4*i+4,0]=v
        return result
    return -(A[1]*A[2]*v).col_join(A[2]*v).col_join(v)


columns = [peripheral(i,fixed[i][:,j])
           for i in (1,2,3) for j in range(fixed[i].cols)]
K = s.Matrix.hstack(*columns,peripheral(0,ell))
q = s.zeros(4)
q[1,2],q[2,1]=1,-1
q[0,3],q[3,0]=2,-2


def coordinates(v):
    x=K.gauss_jordan_solve(v)[0]
    assert all(t.q==1 for t in x)
    return x


def finite_matrix(k, n, r=0):
    m=4*k
    if k<1 or gcd(n,m)!=1:
        raise ValueError('Require k>0 and gcd(n,4k)=1.')
    alpha,beta,common=map(int,s.gcdex(m,n))
    assert common==1 and m*alpha+n*beta==1
    v=n*ell+r*delta
    N=k*sum((A[0]**j for j in range(4)),s.zeros(4))
    # Columns for the finite H1 basis u, z=alpha*psi+beta*g.
    torus_u=s.Matrix([-int((u.T*q*v)[0])]).col_join(
        coordinates(peripheral(0,N*u)))
    torus_z=s.Matrix([-alpha*int((psi.T*q*v)[0])]).col_join(
        coordinates(peripheral(0,alpha*N*psi+beta*v)))
    mumford=s.zeros(10,8)
    mumford[1:9,:]=s.eye(8)
    full=mumford.row_join(torus_u).row_join(torus_z)
    reduced=s.Matrix([[n,-2*r*alpha],[0,1]])
    assert full.det()==reduced.det()==n
    return full,reduced


def run():
    assert A[0]*A[1]*A[2]*A[3]==s.eye(4)
    assert A[0]**4==s.eye(4)
    for i in range(4):
        assert (A[i]-s.eye(4))*fixed[i]==s.zeros(4,fixed[i].cols)
    assert D*K==s.zeros(4,9)
    assert D.rank()==3
    rows=(0,1,3,4,6,7,8,9,11)
    assert K.extract(rows,range(9)).det()==-1
    assert coordinates(peripheral(0,delta))==s.Matrix([0,0,-1,0,0,-1,0,-1,0])
    print('Graph kernel rank9; stated integer sweep columns have a unit minor -1.')
    print('Finite delta sweep lies in the eight Mumford columns.')
    pairs=list(combinations(range(4),2))
    def wedge(a):
        return s.Matrix([[a.extract(i,j).det() for j in pairs] for i in pairs])
    exterior=s.Matrix.hstack(*[wedge(a)-s.eye(6) for a in A])
    detector=s.Matrix([[0,0,2,1,0,0]])
    assert detector*exterior==s.zeros(1,24)
    erows=(0,1,2,4,5);ecols=(0,1,3,4,6)
    assert exterior.extract(erows,ecols).det()==-1
    print('Exterior coinvariants Z, detected primitively by xi; unit minor -1.')
    N=sum((A[0]**j for j in range(4)),s.zeros(4))
    assert N*u==2*delta and N*psi==4*ell
    print('N4(u)=2 delta; N4(psi)=4 ell.')
    checked=0
    for k in range(1,13):
        for n in range(-15,16):
            if gcd(n,4*k)!=1:
                continue
            for r in (0,3):
                full,reduced=finite_matrix(k,n,r)
                diag=smith_normal_form(full,domain=s.ZZ).diagonal()
                assert sorted(abs(int(x)) for x in diag)==[1]*9+[abs(n)]
                checked+=1
    print('Full 10x10 Smith matrices checked:',checked,
          '; 1<=k<=12, -15<=n<=15, gcd(n,4k)=1, r=0,3.')
    data=dict(monodromies=[a.tolist() for a in A],
              fixed_lattices=[f.tolist() for f in fixed],
              graph_kernel_basis=K.tolist(),graph_unit_minor_rows=list(rows),
              exterior_unit_minor_rows=list(erows),
              exterior_unit_minor_columns=list(ecols),
              full_smith_checks=checked,
              examples=[])
    for k,n,r in ((1,1,0),(2,1,0),(3,-1,5),(5,3,2),(6,5,-1)):
        full,reduced=finite_matrix(k,n,r)
        record=dict(m=4*k,n=n,r=r,reduced_matrix=reduced.tolist(),
                    H_torsion_order=abs(n),sphere=abs(n)==1)
        data['examples'].append(record)
        print(record)
    def encode(z):
        return int(z) if isinstance(z,s.Integer) else z
    (ROOT/'records/manifolds_iii_star.json').write_text(
        json.dumps(data,indent=2,default=encode)+'\n')


if __name__=='__main__':
    run()
