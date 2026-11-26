"""Admit the second conductor component and its full common normalization owner."""
from S6_SERIES_PUBLISH_c3_edit import *
import json
folder=ROOT/'agents/continuation3_foundations/sec07'
prefix='S6_SERIES_PUBLISH_sec07_second_branches_'
guards=json.loads((folder/(prefix+'guards.json')).read_text())
assert len(guards)==2
before=SOURCE.read_text();after=before
for row in guards:
    assert after.count(row['old'])==1,row['key']
    after=after.replace(row['old'],row['new'],1)
preserve_identifiers(before,after)
for old,new in zip(identifiers(before),identifiers(after)):
    assert all(new[k]==v for k,v in old.items())
    assert all(new[k]==1 for k in new-old)
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _,rows=read_tsv(folder/(prefix+suffix))
    if suffix=='CHECK_EVENTS.tsv':
        for row in rows:
            if 'effort' not in row['who']:row['who']+='; effort setting not separately exposed'
    print(suffix,append_rows(ROOT/target,rows,key))
_,statuses=read_tsv(folder/(prefix+'unit_progress.tsv'))
for row in statuses:
    kind='structure' if row['row']=='restructuring' else row['row']
    if kind not in ['D10','D16']:
        set_unit_status('night:P4.56',kind,row['status'],row['basis'],row['fragment'])
add_event('night:P4.56;lem:II:smooth-curve-intersection',
    'II-C3-ROOT-SECOND-BRANCHES-ADMISSION','used and rechecked in this run',
    'Foundations read complete original/current and receiving P456/P299 and the complete P455/P252 premises. Root read every receiving P456 and P299 paragraph and the full comparison. The complete P455 global domain and arbitrary transverse multiplicities, exponents and tangencies remain. The graph proof includes all one/two-component and degree-one/two cases and its four labelled pairings. The shared P299 owner retains its original rank-one/two clauses and proves the additional exact parameter-Morse map, finite partial normalization, factor k=a^2 h, finite birational normal model, reduced inverse-image ideal and smooth ramified curve criterion. P456 supplies irreducibility and generic two-sheet hypotheses explicitly. The ambient function restricts with the same global coefficient at both signs, giving b>=mu_B and 2b=mu_B. R14/UN9 use only the unchanged clauses. Every label and tag remains. This is an exposed editorial rereading, with no independent-proof or final-page credit.',
    'Complete second conductor component and full common smooth-curve normalization lemma',source=__file__)
print('P456/P299 admitted.')
