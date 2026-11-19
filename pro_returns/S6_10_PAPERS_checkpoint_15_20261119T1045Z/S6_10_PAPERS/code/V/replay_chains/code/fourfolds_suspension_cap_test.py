"""Five complete integral Thom-cone tests of the geometric cap shortcut."""
import sympy as S
from fourfolds_affine_cap_chains import AffineCap,homology
from fourfolds_global_chains import Complement,AffineGraphBoundary,SuspensionBoundaryToCap

cases=[('circle_positive',S.zeros(0),2,1),('circle_negative',S.zeros(0),3,-1),
       ('Klein_linear2_affine4',S.Matrix([[-1]]),4,1),
       ('Klein_negative',S.Matrix([[-1]]),2,-1),
       ('rotation_three',S.Matrix([[0,-1],[1,-1]]),3,1)]
for name,D,m,epsilon in cases:
    print('GEOMETRIC SUSPENSION',name,flush=True)
    M=S.diag(1,D);r=M.rows;degree=r+2
    cap_periodic=AffineCap(M,[epsilon]+[0]*(r-1),m)
    ambient=Complement([M]);Y=AffineGraphBoundary(cap_periodic,ambient,0)
    cap=Complement([D]);F=SuspensionBoundaryToCap(Y,cap,epsilon)
    DC={n:cap.matrix_degree(n) for n in range(degree+2)}
    maps={n:F.matrix_degree(n) for n in range(degree+1)}
    cone={0:S.zeros(0,1)}
    for n in range(1,degree+2):
        nr=len(cap.bases(n-1));nc=len(cap.bases(n))
        nry=len(Y.bases(n-2)) if n>=2 else 0;ncy=len(Y.bases(n-1))
        C=S.zeros(nr+nry,nc+ncy)
        C[:nr,:nc]=DC[n];C[:nr,nc:]=maps[n-1]
        if n>=2:C[nr:,nc:]=-Y.matrix_degree(n-1)
        cone[n]=C
        assert cone[n-1]*C==S.zeros(cone[n-1].rows,C.cols)
    for n in range(degree+1):
        H=homology(cone,n)
        expected=homology(DC,n-2) if n>=2 else {'rank':0,'torsion':[]}
        assert H==expected,(n,H,expected)
        print('relative degree',n,H,flush=True)
print('ALL FIVE GEOMETRIC CAP SHORTCUTS PASSED FULL INTEGRAL THOM TESTS',flush=True)
