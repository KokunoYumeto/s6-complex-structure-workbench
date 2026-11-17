"""Exhaustive finite initial data for uncorrected whole-fibre degree one.

Scope: MW=Z, M=O(P-O), J=M tensor t_Q^*M^-1=f^*O(1).
Simultaneous sign reversal is identified; ordered P,Q are not swapped.
No assertion is made that this covers component-supported linearizations,
vertical corrections of M, every logarithmic filling or every Mumford fan.
"""
from pathlib import Path
from fractions import Fraction
import sys,json,csv
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'records/explorer/api/engine'))
import os_monodromy as om
import sympy as s
profiles=json.loads((ROOT/'records/manifolds_os_configurations.json').read_text())
candidates=[];marked=[];summary=[]
for item in profiles:
    en,profile=item['os_entry'],item['profile']
    h=Fraction(item['height_matrix'][0][0]);assert h.numerator==1
    d=h.denominator;types=item['kodaira_types'];valid=0;total=0
    for a in range(1,d+1):
        if d%a:continue
        b=d//a;total+=1
        pair=om.check_pair(en,(a,),(b,),profile=profile,verbose=False)
        manual=all(not any(pc) or not any(qc) for pc,qc in zip(pair['P_components'],pair['Q_components']))
        assert manual==pair['valid'] and pair['pairing']==1
        candidates.append(dict(os_entry=en,profile=profile,d=d,a=a,b=b,
           whole_fibre_uncorrected=manual,P_components=pair['P_components'],
           Q_components=pair['Q_components'],failing_fibres=pair['failing_fibers']))
        if not manual:continue
        valid+=1
        # The API has no construction at additive zero; record it separately,
        # without treating its unsupported geometry as a nonexistence result.
        sites=[i for i,k in enumerate(types) if k.startswith('I') and not k.endswith('*') and k[1:].isdigit()]+[len(types)]
        for site in sites:
            weights=[0]*(len(types)+(site==len(types)));weights[site]=1
            A=[s.Matrix(x) for x in om.monodromy_tuple(en,(a,),(b,),tuple(weights),profile=profile,verbose=False)]
            product=s.eye(4)
            for x in A:product=product*x
            assert product==s.eye(4)
            assert all(x.det()==1 for x in A)
            additive=[dict(index=i,type=k,finite_part_order=(6 if k in ['II','II*'] else 4 if k in ['III','III*'] else 3 if k in ['IV','IV*'] else 2),potentially_good=not(k.startswith('I') and k.endswith('*') and k not in ['II*','III*','IV*'])) for i,k in enumerate(types) if i not in sites]
            marked.append(dict(os_entry=en,profile=profile,a=a,b=b,zero_index=site,
               zero_type=types[site] if site<len(types) else 'I0',weights=weights,
               additive_choices=additive,matrices=[x.tolist() for x in A]))
    summary.append(dict(os_entry=en,profile=profile,d=d,candidates=total,
                        valid_whole_fibre_pairs=valid,excluded_uncorrected_pairs=total-valid))
assert len(candidates)==104 and sum(x['whole_fibre_uncorrected'] for x in candidates)==88
assert len(marked)==sum(row['valid_whole_fibre_pairs']*(1+sum(k.startswith('I') and not k.endswith('*') and k[1:].isdigit() for k in next(x['kodaira_types'] for x in profiles if x['os_entry']==row['os_entry'] and x['profile']==row['profile']))) for row in summary)
record=dict(scope=__doc__,summary=summary,pair_candidates=candidates,marked_regular_or_multiplicative_zero_data=marked)
(ROOT/'records/manifolds_degree_one.json').write_text(json.dumps(record,indent=2,default=int)+'\n')
with (ROOT/'records/manifolds_degree_one.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(summary[0]));w.writeheader();w.writerows(summary)
for en in sorted({x['os_entry'] for x in profiles}):
    rows=[r for r in candidates if r['os_entry']==en and r['profile']=='default']
    print(en,'d',rows[0]['d'],'allowed',[(r['a'],r['b']) for r in rows if r['whole_fibre_uncorrected']],
          'excluded only for uncorrected whole-fibre problem',[(r['a'],r['b']) for r in rows if not r['whole_fibre_uncorrected']])
print('Profiles',len(profiles),'ordered pair candidates',len(candidates),'valid',88,'excluded',16,
      'marked multiplicative-or-regular zero data',len(marked),'all exact monodromy products I')
