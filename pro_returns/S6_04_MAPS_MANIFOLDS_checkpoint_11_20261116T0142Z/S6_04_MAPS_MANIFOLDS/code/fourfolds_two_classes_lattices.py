"""Complete integral lattice enumeration for rational parameters v=0,1.

The preceding order algorithm proves conductor2 in each rank-five class.
Therefore all quotient lattices are exhausted by all374 subspaces of F2^5.
For each, an exact Smith calculation classifies every integral extension
with finite generators and primitive rank-three square-zero cusp.
"""
import sympy as S
from itertools import combinations,product
from math import gcd,prod,lcm
from functools import reduce
from sympy.matrices.normalforms import hermite_normal_form,smith_normal_form
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from sympy.polys.domains import ZZ
from fourfolds_lattice_algorithm import order_and_conductor,integral,finite_stable_lattices
from fourfolds_family_survivors import family
import json
from pathlib import Path

def snf(M):return tuple(Z.to_Matrix() for Z in smith_normal_decomp(DomainMatrix.from_Matrix(M).convert_to(ZZ)))
def kernel(M):
    D,U,V=snf(M)
    K=V[:,M.rank():]
    assert M*K==S.zeros(M.rows,K.cols)
    return K

def factors(M):
    D=smith_normal_form(M,domain=ZZ)
    return [abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]

def spaces(n):
    for k in range(n+1):
        for pivots in combinations(range(n),k):
            free=[(i,j) for i,p in enumerate(pivots) for j in range(p+1,n) if j not in pivots]
            for values in product((0,1),repeat=len(free)):
                cols=[1<<p for p in pivots]
                for (i,j),value in zip(free,values):cols[i]|=value<<j
                yield pivots,cols

def contains(value,pivots,cols):
    for p,c in zip(pivots,cols):
        if value>>p&1:value^=c
    return value==0

def action(M,value,n):return sum((sum(int(M[i,j]) for j in range(n) if value>>j&1)%2)<<i for i in range(n))

def extension_classes(A,B,m=4):
    n=5;I=S.eye(n);NW=S.Matrix([[int(x) for x in row] for row in (A*B-I).tolist()])
    assert NW*NW==S.zeros(n)
    if factors(NW)!=[1,1]:
        print('  rejected quotient: nonprimitive cusp',factors(NW),flush=True)
        return []
    normA=sum((A**j for j in range(5)),S.zeros(n));normB=sum((B**j for j in range(m)),S.zeros(n))
    c=S.symbols('c0:10');c1=S.Matrix(1,5,c[:5]);c2=S.Matrix(1,5,c[5:])
    E,b=S.linear_eq_to_matrix(list(c1*normA)+list(c2*normB)+list((c2+c1*B)*NW),c)
    assert b==S.zeros(b.rows,1)
    K=kernel(E);assert K.cols==6
    delta=S.Matrix.vstack((A-I).T,(B-I).T)
    assert E*delta==S.zeros(E.rows,5)
    T=K.gauss_jordan_solve(delta)[0];assert integral(T)
    D,U,V=snf(T);assert T.rank()==5
    tors=[abs(int(D[i,i])) for i in range(5)]
    J=kernel(NW);H=hermite_normal_form(NW)
    coords=J.gauss_jordan_solve(H)[0];assert integral(coords)
    DJ,UJ,VJ=snf(coords)
    z=J*UJ.inv()[:,2]
    assert NW*z==S.zeros(5,1)
    kap=S.Matrix.hstack((B*z).T,z.T)*K*U.inv()
    assert list(kap[:5])==[0]*5
    print('  extension group Z plus torsion',tors,'kappa free coefficient',kap[5],flush=True)
    if abs(kap[5])!=1:return []
    out=[]
    for residues in product(*(range(d) for d in tors)):
        g=S.Matrix(list(residues)+[int(kap[5])])
        cv=K*U.inv()*g
        assert integral(cv)
        AA=S.diag(1,A);BB=S.diag(1,B)
        AA[0,1:]=S.Matrix(1,5,list(cv[:5]));BB[0,1:]=S.Matrix(1,5,list(cv[5:]))
        NN=AA*BB-S.eye(6)
        assert AA**5==S.eye(6) and BB**m==S.eye(6)
        assert NN*NN==S.zeros(6) and factors(NN)==[1,1,1]
        divs=[reduce(gcd,(abs(int(z)) for z in kernel(M.T-S.eye(6))[0,:]),0) for M in (AA,BB)]
        row={'residues':residues,'finite_divisibilities':divs,'A':AA,'B':BB}
        out.append(row)
        print('  extension',residues,'finite divisibilities',divs,flush=True)
        print('  A6=',AA.tolist(),flush=True);print('  B6=',BB.tolist(),flush=True)
    return out

if __name__=='__main__':
    allspaces=list(spaces(5));assert len(allspaces)==374
    print('Complete F2^5 subspace count',len(allspaces),flush=True)
    A=S.zeros(5)
    for j in range(5):A[(j+1)%5,j]=1
    records=[]
    for v in (0,1):
        q=v*v-v+1;X=S.eye(5)[:,0].row_join(S.eye(5)[:,2]+v*S.eye(5)[:,4])
        Y=S.Matrix([[0,-q,-v*v,-1,v],[0,1-v*q,-v*q,v*v-v,q]])
        C=(S.eye(5)+X*Y)*A;B=C.inv()
        print('PARAMETER',v,flush=True)
        order=order_and_conductor(A,C,False);assert order['conductor']==2 and order['lattice_basis']==S.eye(5)
        expected={tuple(H) for H in finite_stable_lattices(A,C,2)}
        found=set()
        stable=0;extensions=0;locally_possible=0
        for pivots,cols in allspaces:
            if not cols:continue # zero gives 2Z^5, excluded by content normalization
            if not all(contains(action(M,c,5),pivots,cols) for M in (A,B) for c in cols):continue
            stable+=1
            L=hermite_normal_form(S.Matrix.hstack(*(S.Matrix([(c>>j)&1 for j in range(5)]) for c in cols),2*S.eye(5)))
            found.add(tuple(L))
            Ai=L.inv()*A*L;Bi=L.inv()*B*L
            assert integral(Ai) and integral(Bi)
            Ai=S.Matrix([[int(x) for x in row] for row in Ai.tolist()]);Bi=S.Matrix([[int(x) for x in row] for row in Bi.tolist()])
            print(' quotient lattice',stable,'index',abs(L.det()),'basis',L.tolist(),flush=True)
            rows=extension_classes(Ai,Bi);extensions+=len(rows)
            locally_possible+=sum(row['finite_divisibilities']==[1,1] for row in rows)
            for row in rows:
                record={'parameter':v,'quotient_basis':L.tolist(),'residues':row['residues'],
                        'finite_divisibilities':row['finite_divisibilities'],
                        'A':row['A'].tolist(),'B':row['B'].tolist()}
                if row['finite_divisibilities']==[1,1]:
                    Ao,Bo=family(v)
                    zz=S.symbols('z0:36');Z=S.Matrix(6,6,zz)
                    E0,b0=S.linear_eq_to_matrix(list(row['A']*Z-Z*Ao)+list(row['B']*Z-Z*Bo),zz)
                    ns=E0.nullspace();assert len(ns)==1
                    cv=ns[0];den=lcm(*(int(S.denom(x)) for x in cv));cv*=den
                    content=reduce(gcd,(abs(int(x)) for x in cv));cv/=content
                    Z=S.Matrix(6,6,list(cv));assert abs(Z.det())==1
                    assert row['A']*Z==Z*Ao and row['B']*Z==Z*Bo
                    record['intertwiner_to_known']=Z.tolist()
                    print('  unimodular intertwiner to known survivor',Z.tolist(),flush=True)
                records.append(record)
        assert found==expected
        print('SUMMARY parameter',v,'all quotient classes',stable,'all primitive extension classes',extensions,'locally possible',locally_possible,flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(records,indent=2,default=int))
    print('ALL COMPLETE LATTICE CLASSIFICATION CHECKS PASSED',flush=True)
