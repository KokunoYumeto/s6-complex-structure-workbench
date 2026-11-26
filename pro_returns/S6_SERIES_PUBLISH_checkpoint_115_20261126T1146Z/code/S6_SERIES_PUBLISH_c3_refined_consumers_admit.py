"""Admit the exhaustive II refined-consumer comparison at exact content guards."""
from S6_SERIES_PUBLISH_c3_edit import *

folder=ROOT/'agents/continuation3_provenance/refined_consumers'
prefix='S6_SERIES_PUBLISH_refined_'
before=SOURCE.read_text();after=before
def statement(text,label):
    i=text.index(r'\label{'+label+'}',text.index(r'\begin{document}'))
    a=text.rfind(r'\begin{',0,i)
    env=re.match(r'\\begin\{([^}]+)\}',text[a:]).group(1)
    b=text.index(r'\end{'+env+'}',i)+len(r'\end{'+env+'}')
    return text[a:b]
protected={x:statement(before,x) for x in ['push:src:E.5.2','push:src:E.5.3',
                                           'night:P4R.13','night:P4.40','night:P4.51']}
_,guards=read_tsv(folder/(prefix+'guards.tsv'));assert len(guards)==10
for row in guards:
    assert after.count(row['old_text'])==1,row['change_id']
    after=after.replace(row['old_text'],row['new_text'],1)
    print('Applied',row['change_id'])
for label,old in protected.items():assert statement(after,label)==old,label
preserve_identifiers(before,after)
for old,new in zip(identifiers(before),identifiers(after)):
    for name,count in old.items():assert new[name]==count,name
    for name,count in (new-old).items():assert new[name]==1,name
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),
                         ('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _,rows=read_tsv(folder/(prefix+suffix))
    print(suffix,append_rows(ROOT/target,rows,key))
_,sources=read_tsv(folder/(prefix+'sources.tsv'))
mapped=[dict(source=r['source_id'],url=r['url'],version=r['version'],locus=r['exact_locus'],
 date_utc=r['date_utc'],sha256='PDF: '+r['source_sha256'],own_word_summary=r['established_scope'],
 use=r['exact_application']+' Reader extent: '+r['reading_extent']) for r in sources]
print('Primary reading',append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',mapped,'source'))

event='II-C3-ROOT-REFINED-CONSUMERS-ADMISSION'
add_event('night:P4R.13; night:P4.40; lem:II:horizontal-primary-conductor; lem:II:positive-ruled-conductor-graph; night:P4.51; night:P4.43; night:P4.42; night:P4R.18; night:P4.55; night:P4.58',
 event,'used and rechecked in this run',
 'The exact ten content guards replay once. Root read the entire detailed comparison and consumer maps, complete P313/P314, complete old and receiving P4.40/P4.42, and the surrounding full unchanged P206. The provenance agent read every original and receiving proof of all eight old owners and both extracted owners, as recorded in ten exposed events; root claims no additional full reading of all eight. The exhaustive II scan includes both refined labels/aliases/tags, bare names and all five R13 equation labels. Every mathematical R13 application has its exact irreducible-support and ruled-resolution hypotheses; each global Euler use keeps the all-supports irreducible-or-normal-crossing hypothesis. P4.40 has no outward mathematical consumer in II. P313 preserves primary restriction at every local branch of a globally irreducible image component, and P314 specifies the same pushout inverse and graph maps. P4.42 gains no Euler-positivity hypothesis: the unchanged zero-Euler theorem excludes its asserted two identifications before P314 is applied. R13/P4.40/P4.51 and protected E.5.2/E.5.3 statement bytes remain identical. P4.41 has now separately passed its full-function repair; P4.45 remains open. Final whole-paper placement and page reading remain open. No independent or required-check increment.',
 'S6_SERIES_PUBLISH_II.tex; agents/continuation3_provenance/refined_consumers/S6_SERIES_PUBLISH_refined_consumer_maps.tsv',
 source='agents/continuation3_provenance/refined_consumers/S6_SERIES_PUBLISH_refined_comparison.md')

# These are actual complete subsections. R13 also contains P205, and P4.51
# contains P203; those two units remain open until their remaining material
# is separately placed/read. Owner-level tables do not create unit credit.
units=['ii:excess-one-curve-germs','night:P4.41','night:P4.43','night:P4R.18','night:P4.55','night:P4.58']
for unit in units:
    for n in range(1,26):
        kind=f'D{n:02}'
        if kind in ['D10','D16']:continue
        keep_open=kind in ['D14','D23'] or (kind=='D18' and unit=='night:P4.41') or (kind=='D25' and unit in ['night:P4R.18','night:P4.55','night:P4.58'])
        detail=('Final whole-paper placement or rendered-page reading remains open.' if kind in ['D14','D23'] else
                'The external ring-condition source remains in the full bibliography-wide review.' if kind=='D18' and unit=='night:P4.41' else
                'Complete local receiving comparison is recorded; the separately managed P4.45 chain premise remains open.' if kind=='D25' and keep_open else
                'Complete original and receiving subsection read against this local class by the named readers. All found instances are logged. Root additionally read both P4.41/P4.42 proofs and the P206/P4.40 unit in full.')
        set_unit_status(unit,kind,'open' if keep_open else 'done',detail,'CHECK_EVENTS.tsv: '+event)
    set_unit_status(unit,'structure','open','Local common owners precede their applications; final whole-paper placement remains open.','CHECK_EVENTS.tsv: '+event)
print('Eight old owners and two extracted owners admitted; P205/P203 adjacent material and P4.45 remain open.')
