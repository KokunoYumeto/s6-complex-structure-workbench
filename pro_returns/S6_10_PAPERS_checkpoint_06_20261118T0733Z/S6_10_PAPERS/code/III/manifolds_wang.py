"""Unbounded order-3k logarithmic transforms for Wang IV* + I2 + 2 I1.

Exact certificates for Theorem D.2.7. Matrices are the primary Wang marking. Primitive integer kernels are supplied explicitly;
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
    [[1,0,-6,-2],[0,-1,-1,1],[0,1,0,-1],[0,0,0,1]],
    [[1,0,6,3],[0,1,2,1],[0,0,1,0],[0,0,0,1]],
    [[1,0,0,0],[0,2,1,0],[0,-1,0,0],[0,0,0,1]],
    [[1,0,0,-1],[0,1,1,0],[0,0,1,0],[0,0,0,1]])]
A = [t.inv().T for t in T]
E = [s.eye(4)[:, j] for j in range(4)]
psi, u, w, delta = E
ell = psi-2*u-4*w
fixed = [s.Matrix.hstack(ell,delta),
         s.Matrix.hstack(-psi+3*u,w,delta),
         s.Matrix.hstack(psi,u+w,delta),
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
q[0,3],q[3,0]=6,-6


def coordinates(v):
    x=K.gauss_jordan_solve(v)[0]
    assert all(t.q==1 for t in x)
    return x


def finite_matrix(k, n, r=0):
    m=3*k
    if k<1 or gcd(n,m)!=1:
        raise ValueError('Require k>0 and gcd(n,3k)=1.')
    alpha,beta,common=map(int,s.gcdex(m,n))
    assert common==1 and m*alpha+n*beta==1
    v=n*ell+r*delta
    N=k*sum((A[0]**j for j in range(3)),s.zeros(4))
    # Columns for the finite H1 basis w, z=alpha*psi+beta*g.
    torus_u=s.Matrix([-int((w.T*q*v)[0])]).col_join(
        coordinates(peripheral(0,N*w)))
    torus_z=s.Matrix([-alpha*int((psi.T*q*v)[0])]).col_join(
        coordinates(peripheral(0,alpha*N*psi+beta*v)))
    mumford=s.zeros(10,8)
    mumford[1:9,:]=s.eye(8)
    full=mumford.row_join(torus_u).row_join(torus_z)
    reduced=s.Matrix([[-2*n,-6*r*alpha],[0,1]])
    assert full.det()==reduced.det()==-2*n
    return full,reduced


def run():
    assert A[0]*A[1]*A[2]*A[3]==s.eye(4)
    assert A[0]**3==s.eye(4)
    for i in range(4):
        assert (A[i]-s.eye(4))*fixed[i]==s.zeros(4,fixed[i].cols)
    assert D*K==s.zeros(4,9)
    assert D.rank()==3
    rows = next(rr for rr in combinations(range(12),9)
                if abs(K.extract(rr,range(9)).det())==1)
    graph_det=int(K.extract(rows,range(9)).det())
    delta_coordinates=coordinates(peripheral(0,delta))
    assert delta_coordinates[-1]==0
    print('Graph unit minor:',[r+1 for r in rows],graph_det)
    print('Finite delta sweep:',list(delta_coordinates))
    pairs=list(combinations(range(4),2))
    def wedge(a):
        return s.Matrix([[a.extract(i,j).det() for j in pairs] for i in pairs])
    exterior=s.Matrix.hstack(*[wedge(a)-s.eye(6) for a in A])
    detector=s.Matrix([[0,0,6,1,0,0]])
    assert detector*exterior==s.zeros(1,24)
    erows=(0,1,2,4,5)
    ecols = next(cc for cc in combinations(range(24),5)
                 if abs(exterior.extract(erows,cc).det())==1)
    exterior_det=int(exterior.extract(erows,ecols).det())
    print('Exterior unit minor:',[r+1 for r in erows],
          [c+1 for c in ecols],exterior_det)
    N=sum((A[0]**j for j in range(3)),s.zeros(4))
    assert N*w==-delta and N*psi==3*ell
    print('N3(w)=-delta; N3(psi)=3ell.')
    # The symmetric auxiliary line used in D.2.8 has this fixed
    # mod-two semicharacter; test the full lattice modulo two.
    from itertools import product
    refinement=lambda x:int(x[1]+x[2]+x[1]*x[2])%2
    for M in A:
        for vector in product((0,1),repeat=4):
            x=s.Matrix(vector)
            assert refinement(M*x)==refinement(x)
    aa,bb=s.symbols('a b',integer=True)
    support=-aa*(aa-1)/2+3*bb**2
    assert s.expand(support.subs(aa,aa+1)-support)==-aa
    assert s.expand(support.subs(bb,bb+1)-support)==6*bb+3
    rankone=-aa*(aa-1)
    assert s.expand(rankone.subs(aa,aa+1)-rankone)==-2*aa
    print('All 64 semicharacter identities; toric support differences and parity verified.')
    checked=0
    for k in range(1,13):
        for n in range(-15,16):
            if gcd(n,3*k)!=1:
                continue
            for r in (0,3):
                full,reduced=finite_matrix(k,n,r)
                diag=smith_normal_form(full,domain=s.ZZ).diagonal()
                assert sorted(abs(int(x)) for x in diag)==[1]*9+[2*abs(n)]
                checked+=1
    print('Full 10x10 Smith matrices checked:',checked,
          '; 1<=k<=12, -15<=n<=15, gcd(n,3k)=1, r=0,3.')
    data=dict(monodromies=[a.tolist() for a in A],
              fixed_lattices=[f.tolist() for f in fixed],
              graph_kernel_basis=K.tolist(),graph_unit_minor_rows=list(rows),
              exterior_unit_minor_rows=list(erows),
              exterior_unit_minor_columns=list(ecols),
              full_smith_checks=checked,
              examples=[])
    for k,n,r in ((1,1,0),(2,1,0),(3,-1,5),(5,2,2),(6,5,-1)):
        full,reduced=finite_matrix(k,n,r)
        record=dict(m=3*k,n=n,r=r,reduced_matrix=reduced.tolist(),
                    H1_H4_order=abs(n),H2_H3_order=2*abs(n),simply_connected=abs(n)==1)
        data['examples'].append(record)
        print(record)
    def encode(z):
        return int(z) if isinstance(z,s.Integer) else z
    (Path(__file__).resolve().parent/'manifolds_wang.json').write_text(
        json.dumps(data,indent=2,default=encode)+'\n')


if __name__=='__main__':
    run()
