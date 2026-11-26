from S6_SERIES_PUBLISH_c3_edit import *

folder=ROOT/'agents/continuation3_conductor'
fragment=folder/'S6_SERIES_PUBLISH_c3_conductor_03_replacement.tex'
before,after=replace_fragment(
    r'\section{Normalization, conductor genus and local torus exclusions}',
    r'\section{Irreducible supports: topology, conductor and equality}',fragment)
for old,new in zip(identifiers(before),identifiers(after)):
    for name,count in old.items():
        assert new[name]==count,name
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),
                          ('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _,rows=read_tsv(folder/('S6_SERIES_PUBLISH_c3_conductor_03_'+suffix))
    print(suffix,append_rows(ROOT/target,rows,key))
import_restructured_status('sec:II:05',fragment,
    folder/'S6_SERIES_PUBLISH_c3_conductor_03_unit_status.tsv')

provenance=ROOT/'agents/continuation3_provenance'
for name in ['S6_SERIES_PUBLISH_c3_provenance_extra_program_edits.tsv',
             'S6_SERIES_PUBLISH_c3_provenance_bibliography_edits.tsv']:
    _,rows=read_tsv(provenance/name)
    text=SOURCE.read_text()
    for row in rows:
        assert text.count(row['old_text'])==1,row['change_id']
        text=text.replace(row['old_text'],row['new_text'],1)
    SOURCE.write_text(text,newline='\n')
    print(name,append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',rows,'change_id'))

add_event('sec:II:05','II-C3-ROOT-NORMALIZATION-ADMISSION',
    'used and rechecked in this run',
    'Admit the conductor agent complete original/receiving comparison events for all23 original proof blocks and their35 receiving owners. Root read the complete proposal comparison, full P222/P223/P243/A.5.8/A.5.2 receiving blocks and P232; remaining complete proof-read credit belongs to the explicitly exposed agent events. P243 insertion is not duplicated. All prior labels and targets retain multiplicity; source139 adds four pinned plain program paths,140–141 identify the cited Reid/Teleman editions. Twelve subsection units follow the actual source; subdivision gives no movement credit. D18,D23 and final global order remain open; no final-PDF or independent-check credit.',
    'S6_SERIES_PUBLISH_II.tex; agents/continuation3_conductor/S6_SERIES_PUBLISH_c3_conductor_03_comparison.md',
    source='code/S6_SERIES_PUBLISH_c3_normalization_admit.py')
print('Normalization admitted with one conductor-duality owner, one canonical-boundary identity, and existing exceptional-matrix owner.')
print('129 plain program paths now present; derived records/counts/deposit refresh remains deferred.')
