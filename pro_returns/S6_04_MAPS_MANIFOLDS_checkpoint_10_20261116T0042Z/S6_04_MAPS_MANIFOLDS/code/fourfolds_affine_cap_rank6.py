"""Two canonical six-torus cap complexes, checked against exact Wang groups.

Orders5,4; total homology degrees0..7, hence matrices through degree8.
The computation is a full chain calculation, with d*d verified exactly.
"""
import sympy as S
from fourfolds_affine_cap_chains import AffineCap,homology
from fourfolds_survivor_test import factors,wedge_map

for m in (5,4):
    C=S.zeros(m)
    for j in range(m):C[(j+1)%m,j]=1
    D=C if m==5 else S.diag(C,-1)
    M=S.diag(1,D);v=[1,0,0,0,0,0]
    print('RANK SIX ORDER',m,flush=True)
    cap=AffineCap(M.tolist(),v,m)
    mats=cap.matrices(7,progress=True)
    for n in range(8):
        H=homology(mats,n)
        def exterior(q):return wedge_map(D,q) if 0<=q<=5 else S.zeros(0)
        E=exterior(n);F=exterior(n-1)
        rank=E.rows-(E-S.eye(E.rows)).rank()+F.rows-(F-S.eye(F.rows)).rank()
        tors=[d for d in factors(E-S.eye(E.rows)) if d>1]
        expected={'rank':rank,'torsion':tors}
        print(n,H,'Wang',expected,flush=True)
        assert H==expected
    cap.clear_intermediates()
print('BOTH RANK-SIX CAP COMPLEXES PASSED THROUGH DEGREE SEVEN',flush=True)
