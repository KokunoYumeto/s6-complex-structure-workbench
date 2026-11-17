"""Bounded, fully specified topology table across all 21 MW=Z profiles.

Bound: P=G, Q=narrow_generator*G, total degree one. The single zero is on
the first I1, or the smallest multiplicative fiber if no I1 occurs. At each
additive fiber test original filling and invariant twist (0,1/m), where m is
the minimal semistable-reduction order. All subsets are tested; integer
clutching, other numerators, higher log orders, other sections, and other
zero placements are NOT enumerated by this script.
"""
from pathlib import Path
from itertools import product
import json,re,csv
from manifolds_explorer_runs import post,datum,ROOT,OUT
profiles=json.loads((ROOT/'records/manifolds_os_configurations.json').read_text())
orders={'II':6,'III':4,'IV':3,'I0*':2,'IV*':3,'III*':4,'II*':6}
rows=[]
for r in profiles:
    types=r['kodaira_types']; n=r['narrow_generators'][0][0]
    choices=[(int(t[1:]),i) for i,t in enumerate(types) if re.fullmatch(r'I[1-9][0-9]*',t)]
    _,zero=min(choices)
    weights=[int(i==zero) for i in range(len(types))]
    additives=[i for i,t in enumerate(types) if not re.fullmatch(r'I[1-9][0-9]*',t)]
    for bits in product([0,1],repeat=len(additives)):
        logs=[None]*len(types)
        for i,bit in zip(additives,bits):
            if bit:logs[i]=['0','1/'+str(orders.get(types[i],2))]
        name='all21_%s_%s_%s'%(r['os_entry'],r['profile'],''.join(map(str,bits)) or 'none')
        payload=datum(r['os_entry'],1,n,weights,logs,r['profile'])
        answer=post('/compute',payload,name)
        row=dict(case=name,os_entry=r['os_entry'],profile=r['profile'],configuration=' + '.join(types),
                 P=1,Q=n,zero_index=zero+1,log_data=json.dumps(logs))
        if answer:
            row.update(pi1=answer['fundamental_group']['description'],
                       euler=answer['euler_characteristic'],
                       H_cohomology='; '.join(g['label'] for g in answer['cohomology']),
                       S6=answer['S6_for_supplied_smooth_model'],status='remote exact result')
        else:row.update(status='request failed or unsupported')
        rows.append(row)
        (ROOT/'records/manifolds_explorer_21.json').write_text(json.dumps(rows,indent=2))
        with (ROOT/'records/manifolds_explorer_21.csv').open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=['case','os_entry','profile','configuration','P','Q','zero_index',
                               'log_data','pi1','euler','H_cohomology','S6','status'])
            w.writeheader();w.writerows(rows)
print('BOUNDED TABLE COMPLETED:',len(rows),'exact inputs;',sum(bool(r.get('S6')) for r in rows),'sphere outputs.')
