"""Bounded integral diagnostics after the constant 2-primary lattice change.

Parameters are exactly v=-6,...,10. All Smith/Hermite computations are
exact. This is not a proof of a statement outside that finite list.
"""
import sympy as s
from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form
from sympy.polys.domains import ZZ
from math import prod

L=s.Matrix([[-2,3,-5,-1,5,-3],[0,2,-2,2,-2,2],
 [0,-4,0,0,4,-4],[0,0,0,-4,4,-4],[0,0,4,-4,4,-4],
 [0,0,0,-4,4,0]])/4


def family(v):
    I=s.eye(5); A=s.zeros(5)
    for j in range(5): A[(j+1)%5,j]=1
    q=v*v-v+1
    X=I[:,0].row_join(I[:,2]+v*I[:,4])
    Y=s.Matrix([[0,-q,-v*v,-1,v],[0,1-v*q,-v*q,v*v-v,q]])
    B=A.inv()*(I-X*Y)
    P=I.copy(); P[:,0]=s.ones(5,1)/q
    An=P.inv()*A*P; Bn=P.inv()*B*P
    ss=v*v+v-1; rr=-(v+1)*(v*v-2)//2
    beta=s.Matrix([[ss,ss-v*rr,v*v*ss+v*rr,rr,-v*ss-rr]])
    AA=s.diag(1,An); BB=s.diag(1,Bn); BB[0,1:]=beta
    return L.inv()*AA*L,L.inv()*BB*L


def tors(M):
    D=smith_normal_form(M,domain=ZZ)
    return prod(abs(int(D[j,j])) for j in range(min(D.shape)) if D[j,j])


if __name__ == '__main__':
    for v in range(-6,11):
        A,B=family(v); A=A.applyfunc(int); B=B.applyfunc(int)
        I=s.eye(6); N=A*B-I
        assert all(z.q==1 for z in list(A)+list(B))
        assert A**5==I and B**4==I and N*N==s.zeros(6)
        cusp=[abs(int(z)) for z in smith_normal_form(N,domain=ZZ).diagonal() if z]
        r=s.eye(6)[:,0]
        da=tors((A-I).row_join(r))//tors(A-I)
        db=tors((B-I).row_join(r))//tors(B-I)
        H=hermite_normal_form(N.T[1:,:])
        for step in range(30):
            new=hermite_normal_form(H.row_join(A[1:,1:].T*H).row_join(B[1:,1:].T*H))
            if new==H:break
            H=new
        else:raise RuntimeError('explicit closure bound 30 exceeded')
        assert H.rows==5
        index=abs(int(H.det())) if H.cols==5 else 'infinite'
        print(v,'cusp Smith',cusp,'finite covector divisibilities',da,db,
              'vanishing normal lattice index',index,'closure steps',step)
    print('Bounded exact diagnostics completed for all 17 specified integers.')
