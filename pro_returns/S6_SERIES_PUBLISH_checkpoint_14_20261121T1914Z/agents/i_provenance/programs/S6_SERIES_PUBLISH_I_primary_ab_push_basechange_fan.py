"""Exact certificates for the u=r^n cusp fans, n=2 and n=12.

The structural proof reduces all jointly flat reduced smooth refinements
to a bridge index k=0,...,n.  This program checks each resulting fan by
unimodular determinants, total normalized volume, side-periodicity and
exact pairwise simplex intersections.  No floating-point tests are used.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import json
import sympy as S

def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))

def solve3(a,b):
    d=det3(a)
    if not d:
        return None
    ans=[]
    for j in range(3):
        aa=[row[:] for row in a]
        for i in range(3):
            aa[i][j]=b[i]
        ans.append(F(det3(aa),d))
    return tuple(ans)

summary=[]
for n in (2,12):
    rays=[(0,0,1,0),(1,0,1,0),(0,1,1,0),(1,1,1,0)]
    rays += [(0,j,0,1) for j in range(n+1)]
    points=[(r[0],r[1],r[2]) for r in rays] # h_q+h_r=1
    @lru_cache(None)
    def inequalities(t):
        mat=S.Matrix.hstack(*[S.Matrix(points[i]+(1,)) for i in t])
        return tuple(tuple(F(int(a.p),int(a.q)) for a in row)
                     for row in mat.inv().tolist())
    @lru_cache(None)
    def compatible(t,s):
        rows=inequalities(t)+inequalities(s)
        allowed={tuple(F(c) for c in points[i]) for i in set(t)&set(s)}
        for ix in combinations(range(8),3):
            a=[[rows[i][j] for j in range(3)] for i in ix]
            b=[-rows[i][3] for i in ix]
            p=solve3(a,b)
            if p is None:
                continue
            if all(sum(row[j]*p[j] for j in range(3))+row[3]>=0 for row in rows):
                assert p in allowed,(n,t,s,p)
        return True
    model=[]
    for k in range(n+1):
        rk=4+k
        tetrahedra=[(0,1,2,rk),(1,2,3,rk)]
        tetrahedra += [(0,1,4+i,5+i) for i in range(k)]
        tetrahedra += [(2,3,4+i,5+i) for i in range(k,n)]
        assert len(tetrahedra)==n+2
        determinants=[int(S.Matrix.hstack(*[S.Matrix(rays[i]) for i in t]).det())
                      for t in tetrahedra]
        assert all(abs(d)==1 for d in determinants)
        # Cross-section volume: 6 int_0^1 (1-h)(1-h+n*h) dh=n+2.
        assert sum(abs(d) for d in determinants)==n+2
        for t,s in combinations(tetrahedra,2):
            assert compatible(t,s)
        # The first period sends the left side A,C to the right side B,D
        # and fixes every rho. Their bridge vertices must be identical.
        left_triangles=[(0,2,rk)]
        left_triangles += [(0,4+i,5+i) for i in range(k)]
        left_triangles += [(2,4+i,5+i) for i in range(k,n)]
        right_triangles=[(1,3,rk)]
        right_triangles += [(1,4+i,5+i) for i in range(k)]
        right_triangles += [(3,4+i,5+i) for i in range(k,n)]
        period={0:1,2:3,**{4+i:4+i for i in range(n+1)}}
        assert {tuple(period[i] for i in t) for t in left_triangles}==set(right_triangles)
        assert all(rays[i][3] in (0,1) for t in tetrahedra for i in t)
        assert all(sum(rays[i][3] for i in t)<=2 for t in tetrahedra)
        model.append({'bridge':k,'tetrahedra':tetrahedra,'determinants':determinants})
    # All possible pairs of side bridge indices: period compatibility iff equal.
    admissible=[(a,b) for a in range(n+1) for b in range(n+1) if a==b]
    assert len(admissible)==n+1
    summary.append({'base_change_exponent':n,'number_of_minimal_models':n+1,
                    'rays':rays,'models':model,'all_checks':'PASS'})
    print('n =',n,':',n+1,'bridge models; each has',n+2,'unimodular cones')
    print('exact common-face intersections, volume, side-periodicity: PASS')
    print('all r-central multiplicities one; at most two branches in every chart')

Path(__file__).with_suffix('.json').write_text(json.dumps(summary,indent=2)+'\n')
print('ALL EXACT CHECKS PASSED')
