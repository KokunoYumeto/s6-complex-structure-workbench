"""Every-degree tests of marked finite and cusp boundary comparison maps.

For a single peripheral generator the complement is the same mapping
torus as its boundary.  The comparison cone must therefore be acyclic,
including torsion.  This tests the map, not only separate Betti numbers.
"""
import sys
import sympy as S
from fourfolds_affine_cap_chains import AffineCap,homology
from fourfolds_global_chains import Complement,FiniteBoundaryToComplement,CuspBoundaryToComplement
from fourfolds_kuhn_cap_chains import KuhnCategory,TorusDiagram,unit_reduce,homology_all

def finite_tests():
    for name,M,v,m in [('circle2',[[1]],[1],2),('circle3',[[1]],[1],3),
                       ('Klein',[[1,0],[0,-1]],[1,0],2),
                       ('Klein_nonfixed',[[1,0],[0,-1]],[1,1],2)]:
        print('FINITE COMPARISON',name,flush=True)
        M=S.Matrix(M);r=M.rows;degree=r+2
        Y=AffineCap(S.diag(1,M),[1]+v,m);E=Complement([M])
        F=FiniteBoundaryToComplement(Y,E,0)
        DY=Y.matrices(degree)
        maps={n:F.matrix_degree(n) for n in range(degree+1)}
        cone={0:S.zeros(0,1)}
        for n in range(1,degree+2):
            nrE=len(E.bases(n-1));ncE=len(E.bases(n))
            nrY=len(Y.bases(n-2)) if n>=2 else 0;ncY=len(Y.bases(n-1))
            D=S.zeros(nrE+nrY,ncE+ncY)
            D[:nrE,:ncE]=E.matrix_degree(n)
            D[:nrE,ncE:]=maps[n-1]
            if n>=2:D[nrE:,ncE:]=-DY[n-1]
            cone[n]=D
            assert cone[n-1]*D==S.zeros(cone[n-1].rows,D.cols)
        for n in range(degree+1):
            H=homology(cone,n)
            assert H=={'rank':0,'torsion':[]}
            print('comparison cone H',n,H,flush=True)
    print('ALL FOUR FINITE BOUNDARY COMPARISONS ARE INTEGRAL EQUIVALENCES',flush=True)

def cusp_test():
    C=KuhnCategory();Y=TorusDiagram(C,True)
    U=S.eye(6);U[:3,3:]=S.eye(3)
    E=Complement([U.inv()]);F=CuspBoundaryToComplement(Y,E,S.eye(6))
    BY,DY=Y.complex();maps={}
    for n in range(8):
        print('CUSP COMPARISON DEGREE',n,'generators',len(BY[n]),flush=True)
        maps[n]=F.matrix_degree(n,BY)
        print('CUSP COMPARISON DEGREE',n,'CHAIN IDENTITY PASSED',flush=True)
    dims={n:len(E.bases(n))+len(BY.get(n-1,[])) for n in range(9)}
    cone={}
    for n in range(9):
        ne=len(E.bases(n));nem=len(E.bases(n-1)) if n else 0
        DE=E.matrix_degree(n);cone[n]={}
        for j in range(DE.cols):cone[n][j]={i:int(DE[i,j]) for i in range(DE.rows) if DE[i,j]}
        for j,col in DY.get(n-1,{}).items():
            new={i:int(maps[n-1][i,j]) for i in range(nem) if maps[n-1][i,j]}
            for i,v in col.items():new[nem+i]=-v
            cone[n][ne+j]=new
    reduced,cancellations=unit_reduce(dims,cone)
    H=homology_all(reduced)
    assert all(z=={'rank':0,'torsion':[]} for z in H.values())
    print('FULL KUHN BOUNDARY COMPARISON IS AN INTEGRAL EQUIVALENCE',
          'unit cancellations',cancellations,flush=True)

if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='cusp':cusp_test()
    else:finite_tests()
