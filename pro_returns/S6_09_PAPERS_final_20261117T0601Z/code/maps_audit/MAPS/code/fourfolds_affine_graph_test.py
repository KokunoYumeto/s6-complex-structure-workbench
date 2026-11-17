"""Six exact small affine-graph boundary comparisons, including lift twists.

Every boundary-to-complement cone is acyclic.  Every boundary-to-cap
cone has the complete integral Thom-shift homology.  The v=3/2 and
negative/nonfixed numerators test the integer lift rather than only
the induced affine map of the torus.
"""
import sympy as S
from fourfolds_affine_cap_chains import AffineCap,homology
from fourfolds_global_chains import Complement,AffineGraphBoundary

cases=[('circle2',[[1]],[1],2),('circle3',[[1]],[1],3),
       ('circle_twist3',[[1]],[3],2),('circle_negative',[[1]],[-1],2),
       ('Klein',[[1,0],[0,-1]],[1,0],2),
       ('Klein_nonfixed',[[1,0],[0,-1]],[3,1],2)]
for name,M,v,m in cases:
    print('AFFINE GRAPH CASE',name,flush=True)
    M=S.Matrix(M);r=M.rows;degree=r+2
    cap=AffineCap(M,v,m);E=Complement([M]);Y=AffineGraphBoundary(cap,E,0)
    DC=cap.matrices(degree)
    for to_cap in [False,True]:
        target=cap if to_cap else E
        maps={n:Y.map_degree(n,to_cap) for n in range(degree+1)}
        cone={0:S.zeros(0,1)}
        for n in range(1,degree+2):
            nr=len(target.bases(n-1));nc=len(target.bases(n))
            nry=len(Y.bases(n-2)) if n>=2 else 0;ncy=len(Y.bases(n-1))
            D=S.zeros(nr+nry,nc+ncy)
            D[:nr,:nc]=DC[n] if to_cap else E.matrix_degree(n)
            D[:nr,nc:]=maps[n-1]
            if n>=2:D[nr:,nc:]=-Y.matrix_degree(n-1)
            cone[n]=D
            assert cone[n-1]*D==S.zeros(cone[n-1].rows,D.cols)
        for n in range(degree+1):
            H=homology(cone,n)
            expected=homology(DC,n-2) if to_cap and n>=2 else {'rank':0,'torsion':[]}
            assert H==expected
        print('  map',('to cap: integral Thom cone' if to_cap else 'to complement: integral equivalence'),'PASSED',flush=True)
print('ALL SIX AFFINE GRAPH BOUNDARIES PASSED BOTH COMPLETE MAP TESTS',flush=True)
