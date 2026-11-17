"""Boundary-to-cap chain maps and exact Thom-cone verification.

The tested caps are a translated circle (orders2,3) and a Klein-bottle
quotient (order2).  Cone homology is checked through the full cap
dimension plus one.  The general construction accepts arbitrary
integer equivariant torus maps.
"""
import sympy as S
from fourfolds_affine_cap_chains import AffineCap,CapMap,homology

for name,M,v,m in [('circle2',[[1]],[1],2),('circle3',[[1]],[1],3),
                    ('Klein',[[1,0],[0,-1]],[1,0],2)]:
    print('BOUNDARY MAP',name,flush=True)
    M=S.Matrix(M);r=M.rows
    cap=AffineCap(M.tolist(),v,m)
    boundary=AffineCap(S.diag(1,M).tolist(),[1]+v,m)
    projection=CapMap(boundary,cap,S.eye(r+1)[1:,:])
    degree=r+3
    DC=cap.matrices(degree);DY=boundary.matrices(degree)
    maps={n:projection.matrix_degree(n) for n in range(degree+1)}
    cone={0:S.zeros(0,len(cap.bases(0)))}
    for n in range(1,degree+2):
        nrC=len(cap.bases(n-1));ncC=len(cap.bases(n))
        nrY=len(boundary.bases(n-2)) if n>=2 else 0
        ncY=len(boundary.bases(n-1))
        D=S.zeros(nrC+nrY,ncC+ncY)
        D[:nrC,:ncC]=DC[n]
        D[:nrC,ncC:]=maps[n-1]
        if n>=2:D[nrC:,ncC:]=-DY[n-1]
        cone[n]=D
        assert cone[n-1]*D==S.zeros(cone[n-1].rows,D.cols)
    for n in range(degree+1):
        H=homology(cone,n)
        expected=homology(DC,n-2) if n>=2 else {'rank':0,'torsion':[]}
        assert H==expected
        print('relative H',n,H,'Thom shift exact',flush=True)
print('ALL THREE BOUNDARY CHAIN MAPS AND THOM CONES PASSED',flush=True)
