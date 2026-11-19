"""Independent coordinate-order audit of the full integral bar marking.

Replace the upper-triangular bar comparison by a reordered-coordinate
comparison, conjugate its target back, and compare complete homology.
This checks the two-primary marking and last-boundary corrections on
actual even-factor data, including higher finite orders and extra logs.
"""
from pathlib import Path
from math import gcd
import json
import sympy as s
import manifolds_all_weighted_profiles as A
import manifolds_weighted_profiles as W
from manifolds_rankone_families import wedge,PAIRS

ROOT=Path(__file__).resolve().parent
original=A.QuadraticCorrection
R=s.Matrix([[0,0,1,0],[1,0,0,0],[0,0,0,1],[0,1,0,0]])
WRinverse=wedge(R).inv()
def p_alt(u,v):
    u=R*s.Matrix(u);v=R*s.Matrix(v)
    return WRinverse*s.Matrix([u[i]*v[j] for i,j in PAIRS])

class Alternative:
    def __init__(self,M):
        self.A=s.Matrix(M);self.WA=wedge(self.A);E=s.eye(4)
        self.D=[[p_alt(self.A*E[:,i],self.A*E[:,j])-self.WA*p_alt(E[:,i],E[:,j])
                 for j in range(4)] for i in range(4)]
        assert all(self.D[i][j]==self.D[j][i] for i in range(4) for j in range(4))
    def __call__(self,v):
        v=s.Matrix(v);z=s.zeros(6,1)
        for i in range(4):
            z-=self.D[i][i]*v[i]*(v[i]-1)/2
            for j in range(i+1,4):z-=self.D[i][j]*v[i]*v[j]
        assert all(x.q==1 for x in z)
        return z
    def coefficients(self):return {'comparison':'permuted coordinates [delta,u,gamma,w]'}

# Sample distinct profiles and filling choices, always with a genuine
# shared even factor. The finite set and all parameters are retained.
chosen=[];seen=set()
for i,p in enumerate(W.PATTERNS):
    if p['a']%2:continue
    signature=(p['entry'],p['profile'],tuple(map(tuple,p['additive_choices'])),
               tuple(map(tuple,p['multiplicative_choices'])))
    if signature in seen:continue
    seen.add(signature);chosen.append(i)
    if len(chosen)==12:break
checks=[]
for i in chosen:
    p=W.PATTERNS[i];row=W.MONO[W.key(p)]
    for multiplier in [1,2]:
        d=multiplier*p['a'];assert gcd(p['a'],d)%2==0
        finite={}
        for site in p['finite_indices']:
            h=W.ORDER[row['local'][site]['type']]
            M=W.weighted(row['local'][site]['matrix'],d)
            finite[site]=W.default_finite(M,h,m=3*h)
        regular=[] if multiplier==1 else [dict(m=2,v=[1,0,0,1]),dict(m=3,v=[0,1,1,-1])]
        e=(i%3)-1
        A.QuadraticCorrection=original
        baseline=A.compute(i,d,finite=finite,regular=regular,e=e)
        A.QuadraticCorrection=Alternative
        alternate=A.compute(i,d,finite=finite,regular=regular,e=e)
        assert baseline['homology']==alternate['homology'],(i,d,baseline['homology'],alternate['homology'])
        checks.append(dict(pattern=i,key=W.key(p),weight=d,e=e,finite=finite,regular=regular,
                           homology=baseline['homology'],regular_fibre_coinvariant=baseline['regular_fibre_coinvariant']))
        print('PASS',i,W.key(p),'weight',d,'extra regular logs',len(regular),flush=True)
A.QuadraticCorrection=original
(ROOT/'root_all_weighted_coordinate_audit.json').write_text(json.dumps({
    'comparison_matrix':R.tolist(),'checks':checks,'status':'Complete homology invariant under integral bar-comparison coordinate change'},indent=2,default=int)+'\n')
print('PASS:',len(checks),'complete even-factor presentations; alternate integral bar coordinate order.')
