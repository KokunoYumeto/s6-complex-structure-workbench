"""Integral certificates for all-twist reductions in the two survivor classes.

The only parameters tested are the two already classified rational classes
v=0,1. The universal multiplicity and gauge statements use the proof, not
an extrapolation from a numerical multiplicity search.
"""
import sympy as S
from fourfolds_family_survivors import family
from fourfolds_two_classes_lattices import kernel,snf,factors
from sympy.matrices.normalforms import hermite_normal_form
from itertools import combinations

def exterior(M,q):
    inds=list(combinations(range(M.rows),q))
    return S.Matrix([[M.extract(i,j).det() for j in inds] for i in inds])

for v in (0,1):
    A,B=family(v);M1,M2=A.T,B.T
    print('PARAMETER',v,flush=True)
    assert factors(S.Matrix.hstack(M1-S.eye(6),M2-S.eye(6)))==[1]*5
    print('global homology coinvariants: Z, with no torsion',flush=True)
    for M,m,u in ((M1,5,S.Matrix([1,3,-2,-1,2,0])),(M2,4,S.eye(6)[:,0])):
        assert M*u==u and u[0]==1
        D=S.Matrix([[int(x) for x in row] for row in M[1:,1:].tolist()])
        lamv=kernel(D-S.eye(5))[:,0]
        lam=S.Matrix([0]+list(lamv))
        norm=sum((D**j for j in range(m)),S.zeros(5))
        DD,UU,VV=snf(norm);rhs=UU*lamv
        assert rhs[0]%DD[0,0]==0 and all(z==0 for z in rhs[1:])
        zz=S.zeros(5,1);zz[0]=rhs[0]/DD[0,0]
        qv=VV*zz;q=S.Matrix([0]+list(qv))
        assert norm*qv==lamv and q[0]==0
        w=-sum((j*M**j*q for j in range(m)),S.zeros(6,1))/m
        assert (S.eye(6)-M)*w==-lam/m+q
        K2=kernel(exterior(M.T,2)-S.eye(15))
        vals=[]
        for j in range(K2.cols):
            f=S.zeros(6)
            for coeff,(a,b) in zip(K2[:,j],combinations(range(6),2)):
                f[a,b]=coeff;f[b,a]=-coeff
            vals.append((u.T*f*lam)[0])
        gcd=S.gcd_list(vals)
        assert abs(gcd)==m
        print('finite order',m,'fixed vertical lambda',list(lam),flush=True)
        print('norm preimage q',list(q),'boundary translation w',list(w),flush=True)
        print('all invariant two-form suspension periods',vals,'gcd',abs(gcd),flush=True)
        print('arbitrary multiplicity m*k: covering cokernel Z/k by gcd(r,m*k)=1',flush=True)
print('ALL TWIST AND MULTIPLICITY CERTIFICATES PASSED',flush=True)
