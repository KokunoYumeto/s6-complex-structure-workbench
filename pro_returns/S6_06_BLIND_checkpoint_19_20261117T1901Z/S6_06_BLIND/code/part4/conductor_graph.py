"""Exact local branch-incidence combinatorics in P4.35."""
from pathlib import Path
import itertools,json
types=[frozenset([0]),frozenset([1]),frozenset([0,1])]
rows=[]
for mask in range(1,8):
 family=[types[i] for i in range(3) if mask&(1<<i)]
 pairwise=all(a&b for a,b in itertools.combinations(family,2))
 common=set.intersection(*(set(a) for a in family))
 if pairwise:assert common
 rows.append({'family':[sorted(a) for a in family],'pairwise_intersections':bool(pairwise),'common_branches':sorted(common)})
result={'proof':'P4.35','exhaustive_nonempty_type_families':rows,
        'symbolic_graph_bound':'b(D)=s-c+sum(r_q-1)>=s-c+(r_plus+r_minus-n)>=s>=1',
        'hypotheses':'r_plus>=n, r_minus>=c; D has s>=1 connected components',
        'all_checks_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('P4.35 local branch-incidence check: PASS (all seven families of subset types)')
for row in rows:
 print(row)
print(result['symbolic_graph_bound'])
