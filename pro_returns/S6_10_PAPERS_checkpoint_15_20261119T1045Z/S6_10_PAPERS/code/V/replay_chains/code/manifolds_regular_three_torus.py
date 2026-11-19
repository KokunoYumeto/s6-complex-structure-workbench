"""Actual regular H3 inclusion from a marked torsion-linking calculation.

The ordinary order-one clutch disc contains the chosen regular fibre.
Only its normal Thom 3-chains meet that fibre; all remaining presentation
chains lie in the complement.  Their loop coefficient therefore computes
the linking of a torsion H2 generator with a regular 3-torus.
"""
from pathlib import Path
import json
import sympy as s
import manifolds_all_weighted_profiles as B
from manifolds_rankone_families import decomp

def calculate():
    matches=[]
    for i,p in enumerate(B.W.PATTERNS):
        if B.W.key(p)!=(55,'default',5,4,2):continue
        if any(v=='original' for _,v in p['multiplicative_choices']):continue
        matches.append(i)
    assert matches==[219]
    i=matches[0];p=B.W.PATTERNS[i]
    result=B.compute(i,1,e=1)
    M=s.Matrix(result['H2_matrix'])
    D,U,V,rank=decomp(M)
    sites=len(B.W.MONO[B.W.key(p)]['local'])+1
    offset=6*sites
    records=[]
    for j in range(rank):
        d=abs(int(D[j,j]))
        if d<=1:continue
        cycle=U.inv()[:,j]
        coeff=V[:,j]*(1 if D[j,j]>0 else -1)
        assert M*coeff==d*cycle
        v=s.Matrix([0,0,0,-1])
        clutch=coeff[offset:offset+4,:]+v*coeff[offset+4]
        assert [int(x%d) for x in clutch]==[0,0,1,0] and d==4
        records.append(dict(order=d,clutch=list(map(int,clutch)),
                            clutch_mod=[int(x%d) for x in clutch],
                            cycle=cycle.T.tolist()[0],
                            bounding_coefficients=coeff.T.tolist()[0]))
    assert len(records)==1
    record=dict(pattern=i,key=B.W.key(p),e=1,homology=result['homology'],
                clutch_column_offset=offset,torsion_cycles=records,
                regular_three_torus='e1 wedge e2 wedge gamma',
                image='generator of H3(X)=Z/4; linking +1/4 up to the common orientation convention')
    (Path(__file__).resolve().parents[1]/'records/manifolds_c4_regular_three_torus.json').write_text(
        json.dumps(record,indent=2,default=int)+'\n')
    print('Exact torsion bounding relation M*c=4*z: PASS')
    print('Ordinary-clutch loop vector:',records[0]['clutch'])
    print('Mod4:',records[0]['clutch_mod'],'; regular T_(e1,e2,gamma) has exact order4.')

if __name__=='__main__':calculate()
