"""Locate the minimal nonstar simply connected smooth-classification cases.

Use D.2.23's proved Seifert criterion, D.2.30's exact finite lattices,
and D.2.26's c=b/product(q) in the primitive-gamma sector.  This
enumerates finite initial patterns only, not a cutoff on logarithmic
orders or twists.  It does not assert any uncomputed smooth invariant.
"""
from pathlib import Path
from math import gcd,prod
from collections import Counter
import json
root=Path(__file__).resolve().parent
data=json.loads((root/'manifolds_all_finite_logs.json').read_text())
key=lambda r:(r['entry'],r['profile'],r['a'],r['b'],r['zero_index'])
rows={key(r):r for r in data['rows']}
remaining=[];counts=Counter()
for pattern in data['all_nonstar_patterns']:
    row=rows[key(pattern)]
    sites=[row['local'][i] for i in pattern['finite_indices']]
    if any(site['gamma_index']!=1 for site in sites):continue
    if len(sites)>2:continue
    if len(sites)==2 and gcd(sites[0]['log_order'],sites[1]['log_order'])!=1:continue
    Q=prod(site['q'] for site in sites)
    assert row['b']%Q==0
    c=row['b']//Q
    counts[c]+=1
    if c>1:
        rec=dict(pattern)
        rec.update(c=c,finite_linear_orders=[site['log_order'] for site in sites],
                   minimal_no_regular_log_H2=['Z/'+str(c)],
                   smooth_status='Requires complete refined spin invariants or geometric comparison')
        remaining.append(rec)
record={'scope':__doc__,'potentially_simply_connected_pattern_counts_by_c':dict(sorted(counts.items())),
        'nontrivial_c_patterns':remaining}
(root/'root_remaining_smooth_profiles.json').write_text(json.dumps(record,indent=2)+'\n')
print('Potentially simply connected nonstar minimal patterns:',sum(counts.values()))
print('Counts by c:',dict(sorted(counts.items())))
print('Patterns with c>1:',len(remaining))
print('These counts locate cases; they are not a smooth classification.')
