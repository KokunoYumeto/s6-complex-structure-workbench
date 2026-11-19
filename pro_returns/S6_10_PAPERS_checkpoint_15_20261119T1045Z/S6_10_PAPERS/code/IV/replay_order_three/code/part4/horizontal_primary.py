#!/usr/bin/env python3
"""Exhaustive two-component, one-cycle graph counts for P4R.18."""
from pathlib import Path
from itertools import combinations_with_replacement
import json

records=[]
pairs=[(0,0),(0,1),(1,1)]
patterns=[]
for a,b in combinations_with_replacement(pairs,2):
    if (0,1) not in (a,b):continue
    patterns.append([a,b])
patterns += [[(0,0,1)],[(0,1,1)]]
for pattern in patterns:
    assert sum(len(p)-1 for p in pattern)==2
    for primary in [0,1]:
        points=sum(p.count(primary) for p in pattern)
        singular_points=sum(p.count(primary)>1 for p in pattern)
        extra=(4-3*singular_points)//3
        possible_branch_values=points+extra
        assert extra>=0
        assert possible_branch_values<=3
        records.append({'branch_labels_at_identifications':[list(p) for p in pattern],
                        'primary_component':primary,'primary_points_above_identifications':points,
                        'primary_singular_identifications':singular_points,
                        'maximum_additional_unibranch_singularities':extra,
                        'maximum_branch_values':possible_branch_values})
out={'status':'PASS','statement':'P4R.18','primary_defect_bound':4,
     'cost_of_each_primary_singularity_at_least':3,
     'degree_two_Riemann_Hurwitz_minimum_branch_values':4,'patterns':records,
     'maximum_over_all_patterns':max(r['maximum_branch_values'] for r in records)}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(f'PASS: {len(records)} labelled primary cases; every connected one-cycle graph gives at most3 branch values, below4.')
