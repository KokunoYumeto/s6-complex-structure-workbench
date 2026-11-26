#!/usr/bin/env python3
"""Fresh regular-log presentations and five finite-log boundary calculations."""
from pathlib import Path
from itertools import combinations
from math import gcd
import json
import sympy as s
from sympy.polys.domains import ZZ
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'agents/continuation7_iii_original_caps'
ROWS = json.loads((OUT/'S6_SERIES_PUBLISH_III_02KV_fresh_cap_maps.json').read_text())
PAIR4 = list(combinations(range(4), 2))
PAIR5 = list(combinations(range(5), 2))


def wedge(v, w):
    return s.Matrix([v[i]*w[j]-v[j]*w[i] for i, j in PAIR5])


def invf(A):
    D = smith_normal_form(A, domain=ZZ)
    return [abs(int(D[i, i])) for i in range(min(D.shape)) if D[i, i]]


def ints(A):
    assert all(x.q == 1 for x in A)
    return [[int(x) for x in A.row(i)] for i in range(A.rows)]


def certificate(A):
    D, U, V = smith_normal_decomp(DomainMatrix.from_Matrix(A).convert_to(ZZ))
    D, U, V = D.to_Matrix(), U.to_Matrix(), V.to_Matrix()
    assert U*A*V == D and abs(U.det()) == abs(V.det()) == 1
    return D, U, V


def integer_solution(A, B):
    D, U, V = certificate(A)
    C = U*B
    X = s.zeros(A.cols, B.cols)
    for i in range(min(D.shape)):
        if D[i, i]:
            for j in range(B.cols):
                assert C[i, j] % D[i, i] == 0
                X[i, j] = C[i, j]/D[i, i]
        else:
            assert all(C[i, j] == 0 for j in range(C.cols))
    for i in range(min(D.shape), D.rows):
        assert all(C[i, j] == 0 for j in range(C.cols))
    X = V*X
    assert A*X == B
    return X


regular_count = 0
for m in range(1, 13):
    vectors = [(0,0,1,0), (0,0,0,1), (2,3,1,4), (m,0,1,m),
               (0,m,1,-m), (m//2,0,1,0), (2,4,3,6), (-1,2,-1,-3)]
    for a,b,c,n in vectors:
        if gcd(m, gcd(a, gcd(b, gcd(c,n)))) != 1:
            continue
        rel = s.Matrix([-a,-b,-c,-n,m])
        # Generators: seven exterior complement classes, three rims, then
        # the ten exterior products of the five logarithmic lattice symbols.
        P = s.zeros(20, 15)
        for j in range(5):
            P[10:, j] = wedge(rel, s.eye(5)[:, j])
        for j, (x,y) in enumerate(PAIR4):
            P[10+PAIR5.index((x,y)), 5+j] = 1
        rim = {0:7, 1:8, 3:9}
        for x in range(4):
            if x in rim:
                P[rim[x], 11+x] = 1
            P[10:, 11+x] -= wedge(s.eye(5)[:,4], s.eye(5)[:,x])
        g = gcd(m, gcd(a, gcd(b,n)))
        expected = sorted(x for x in (g,m,m) if x > 1)
        got = invf(P)
        assert [x for x in got if x > 1] == expected
        assert P.rows-len(got) == 7
        regular_count += 1
print(f'PASS {regular_count} literal regular-log exterior-power presentations: torsion (g,m,m), free rank 7 before the n=0 kernel')

finite_records = []
finite_count = 0
for osno, prof, fin, q, h, bfree in [
        (49,'III',0,3,3,1), (49,'III',1,4,2,6),
        (50,'IV',1,3,3,5), (43,'II',1,6,1,7),
        (46,'II',1,6,1,7)]:
    record = next(x for x in ROWS if x['OS']==osno and x['profile']==prof)
    loc = record['local']
    order = [(fin+1)%3, (fin+2)%3]
    f1 = [s.Matrix(loc[i]['f1']) for i in order]
    f2 = [s.Matrix(loc[i]['f2']) for i in order]
    M1 = s.Matrix.vstack(f1[0], -f1[1])
    M2 = s.Matrix.vstack(f2[0], -f2[1])
    D1,U1,V1 = certificate(M1)
    rank1 = M1.rank()
    K = V1[:,rank1:]
    Kleft = V1.inv()[rank1:,:]
    assert K.cols == 2 and M1*K == s.zeros(M1.rows,2)
    assert invf(M1) == [1]*rank1
    assert invf(M2) == [1,1,1,1,h]
    assert M2.rows-M2.rank() == bfree-1
    vertical = s.zeros(M2.rows,6)
    vertical[:f2[0].rows,:] = f2[0]
    D2,U2,V2 = certificate(M2)
    vertical_coordinates = U2*vertical
    assert all(x == 0 for x in vertical_coordinates[5:,:])
    torsion_row = vertical_coordinates[4,:]
    Tf = s.Matrix(loc[fin]['T'])
    zq = s.Matrix([s.Rational(x) for x in loc[fin]['zQ']])
    zg = s.Matrix([s.Rational(x) for x in loc[fin]['zG']])
    ell = s.Matrix([-zq[0],-zq[1],0,1])
    B = s.eye(4); B[:,3] = ell
    assert B.det()==1 and Tf**q==s.eye(4)
    R = (B.inv()*Tf*B)[:3,:3]
    assert B.inv()*Tf*B == s.diag(R,1)
    rho = s.Matrix([[h*zg[1],-h*zg[0],h]])
    ints(rho)
    assert rho*(R-s.eye(3)) == s.zeros(1,3)
    assert gcd(*(int(x) for x in rho))==1
    assert invf(R-s.eye(3))==[1,1]
    A1,A2 = [s.Matrix(loc[i]['T']) for i in order]
    assert A1*A2*Tf == s.eye(4)
    sweep = (A1-s.eye(4))*A2*ell
    assert M1*sweep == s.zeros(M1.rows,1)
    rc = Kleft*sweep
    assert invf(rc) == [1]
    # The first boundary row is the elliptic area; the second is the
    # coefficient of the invariant delta sweep in the mapping torus.
    area = s.Matrix([[1,0,zq[1],0,-zq[0],0]])
    primitive_sweep = s.Matrix([[0,0,rho[0],0,rho[1],rho[2]]])
    eps = -1 if osno==50 else 1
    residue_difference = torsion_row-torsion_row[0]*area-eps*primitive_sweep
    assert all(x % h == 0 for x in residue_difference)
    for k in range(1,5):
        m=q*k
        for n in range(-9,10):
            if gcd(n,m)!=1:
                continue
            for r in (-3,0,2):
                # Edge-kernel coordinates, sigma of order h, and cap A,B.
                P = s.zeros(5,9)
                P[2,0] = h
                P[2,1:7] = torsion_row
                P[3,1:7] = -area
                P[4,1:7] = -(s.Rational(m,h)*primitive_sweep)
                P[4,7] = n
                P[:2,8] = rc
                P[4,8] = -r
                assert invf(P)==[1,1,1,1]
                aa,bb,gg = s.gcdex(n,m)
                assert gg==1 and aa*n+bb*m==1
                H1 = s.Matrix([[0,1,0],[1,-r*aa*h,r*bb*h],[0,m,n]])
                assert invf(H1) == [1,1,abs(n)]
                finite_count += 1
    rec = {'OS':osno,'profile':prof,'finite_index':fin,
           'finite_type':loc[fin]['type'],'q':q,'h':h,'b':bfree,
           'cap_order':order,'MV1':ints(M1),'MV2':ints(M2),
           'kernel_basis':ints(K),'kernel_left_inverse':ints(Kleft),
           'MV2_smith_D':ints(D2),'MV2_smith_U':ints(U2),
           'MV2_smith_Uinv':ints(U2.inv()),'MV2_smith_V':ints(V2),
           'vertical_torsion_row':ints(torsion_row),
           'torsion_sweep_unit':eps,
           'residue_difference_divided_by_h':ints(residue_difference/h),
           'ell':ints(ell),'R':ints(R),'rho':ints(rho),
           'ell_sweep_kernel_coordinates':ints(rc),
           'area_row':ints(area),'primitive_sweep_row':ints(primitive_sweep)}
    finite_records.append(rec)
    print(f'PASS {osno}/{prof}, finite {loc[fin]["type"]}: exterior H2=Z^{bfree+1} plus Z/{h}; primitive ell sweep {list(rc)}; vertical torsion retained and killed by the literal log maps; finite H2=Z^{bfree}')

(OUT/'S6_SERIES_PUBLISH_III_02KW_fresh_cap_maps.json').write_text(json.dumps(finite_records,indent=2)+'\n')
print(f'PASS {finite_count} finite-log boundary presentations: H1=Z/|n|, H2=Z^b; n, r and all sampled k retain their literal integer values')
print('PASS regular and finite logarithmic computations completed without reading either embargoed target proof')
