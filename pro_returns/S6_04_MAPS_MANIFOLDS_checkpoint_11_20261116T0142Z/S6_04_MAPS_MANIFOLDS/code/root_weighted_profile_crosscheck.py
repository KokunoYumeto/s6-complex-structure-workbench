"""Cross-check the uniform weighted algorithm against the independent Engel model."""
from pathlib import Path
import json
import sympy as s
from manifolds_weighted_profiles import compute,MONO,weighted,finite_lattice,key,PATTERNS
from manifolds_weighted_engel import compute as engel
from manifolds_rankone_families import bezout
ROOT=Path(__file__).resolve().parents[1]
index=next(i for i,p in enumerate(PATTERNS) if p['a']==1 and p['b']==6 and len(p['finite_indices'])==2)
pattern=PATTERNS[index];row=MONO[key(pattern)]
records=[]
for d in [1,2,3,4,5,6,9,12]:
    for k,l,n0,n1 in [(1,1,1,-1),(2,3,1,1),(4,3,1,-1)]:
        finite={}
        for site,order,m,n in [(0,3,3*k,n0),(1,4,4*l,n1)]:
            A=weighted(row['local'][site]['matrix'],d)
            F,_,_=finite_lattice(A,order)
            co,g=bezout(list(F[3,:]));assert g==1
            v=F*s.Matrix(co)*n;assert v[3]==n
            finite[site]={'m':m,'v':list(map(int,v))}
        general=compute(index,d,finite=finite,e=0)
        special=engel(d,k,l,n0,n1)
        assert general['homology']==special['homology'],(d,k,l,n0,n1,general,special)
        records.append({'d':d,'k':k,'l':l,'n0':n0,'n1':n1,'homology':general['homology']})
(ROOT/'records/root_weighted_profile_crosscheck.json').write_text(json.dumps(records,indent=2)+'\n')
print('PASS:',len(records),'independent uniform-versus-Engel complete homology comparisons; SC, finite pi1 and zero Euler class.')
