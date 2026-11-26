from S6_SERIES_PUBLISH_c3_edit import *
import json

folder=ROOT/'agents/continuation3_foundations'
guards=json.loads((folder/'S6_SERIES_PUBLISH_torus_consolidation_guards.json').read_text())
before=SOURCE.read_text(); after=before
for guard in guards:
    assert after.count(guard['old'])==1, guard['key']
    after=after.replace(guard['old'],guard['new'],1)
preserve_identifiers(before,after)
old_ids=identifiers(before);new_ids=identifiers(after)
for old,new in zip(old_ids,new_ids):
    for name in old:
        assert new[name]==old[name],name
SOURCE.write_text(after,newline='\n')
for name,target,key in [
    ('S6_SERIES_PUBLISH_torus_consolidation_defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),
    ('S6_SERIES_PUBLISH_torus_consolidation_CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _,rows=read_tsv(folder/name)
    print(name,append_rows(ROOT/target,rows,key))

apply_edit(r'\item \SeriesRef{night:P4.2}\quad A compact torus fibration with three singular fibres.',
    r'\item \SeriesRef{cdp:st:D.2.7}\quad A simply connected compact torus fibration and its integral homology.',
    'II-C3-TORUS-LIST-OWNER',['D12','D24'],'cdp:st:D.2.7','further-results list',
    'The exact chartwise identification makes D.2.7 and P4.2/P4.4/P4.5 one global construction. Keep one list entry for that owner and retain the two distinct local results.')
for label,description in [
    ('night:P4.4','Fundamental group and first two homology groups.'),
    ('night:P4.5','Invariants of the compact torus fibration.')]:
    apply_edit('\\item \\SeriesRef{'+label+'}\\quad '+description+'\n','',
        'II-C3-TORUS-LIST-'+label.split(':')[-1].replace('.','-'),['D12','D24'],label,
        'further-results list','Remove the duplicate list entry after preserving this exact original statement scope as an alias of D.2.7.')

# The user defines units by subsections; the five statement-level proposal
# scopes are bounded evidence, not five new ledger units.
path=ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv'
fields,rows=read_tsv(path)
removed=[r for r in rows if r['paper']=='II' and r['unit_id']=='night:P4.1']
assert len(removed)==26
rows=[r for r in rows if r not in removed]
for row in rows:
    if row['paper']=='II' and row['unit_id']=='sec:II:fibre-classification':
        row['evidence']='CHECK_EVENTS.tsv: publish:c3:torus-consolidation:D27-full and related construction/consumer events'
        row['detail']+=' The exact common construction and its local geometry, homology and basis remark now stand once in this subsection. Removed later subsection rows are a scope migration with no new closure credit.'
        if row['defect_type']=='D14' or row['row_kind']=='structure':
            row['status']='open'
        row['date_utc']=now()
write_tsv(path,fields,rows)
add_event('cdp:st:D.2.7; night:P4.1; night:P4.3; rem:II:torus-quotient-coordinates',
    'II-C3-ROOT-TORUS-CONSOLIDATION-ADMISSION','used and rechecked in this run',
    'Root read all461lines of the receiving construction plus the full P213 and D.2.8 replacements. Agent complete original/receiving proof comparisons are imported as exposed evidence. Exact guards match once, all old identifiers retain their multiplicities, three global aliases now share one owner and one further-results entry. Five statement-scope progress proposals are not imported as subsection units; obsolete later unit rows are removed without movement credit. No final-PDF credit.',
    'S6_SERIES_PUBLISH_II.tex',source='code/S6_SERIES_PUBLISH_c3_torus_consolidation_admit.py')
print('Single earlier construction admitted; obsolete later subsection removed; all old labels/targets preserved.')
