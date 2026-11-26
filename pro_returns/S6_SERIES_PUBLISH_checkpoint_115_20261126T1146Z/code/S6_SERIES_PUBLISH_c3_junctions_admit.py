"""Admit the common cubic genus calculation and the two complete junction exclusions."""
from S6_SERIES_PUBLISH_c3_edit import *
import json
folder=ROOT/'agents/continuation3_foundations/sec07'
before=SOURCE.read_text();after=before
for package in ['two_junctions','three_junction']:
    guards=json.loads((folder/f'S6_SERIES_PUBLISH_sec07_{package}_guards.json').read_text())
    for row in guards:
        assert after.count(row['old'])==1,(package,row['key'])
        after=after.replace(row['old'],row['new'],1)
anchor=r'\begin{lemma}[Genus of residual cubic covers]'
heading=r'\subsection{Genus of residual cubic covers}\label{subsec:II:cubic-spectral-genus}'+'\n\n'
assert after.count(anchor)==1
after=after.replace(anchor,heading+anchor,1)
preserve_identifiers(before,after)
for old,new in zip(identifiers(before),identifiers(after)):
    assert all(new[k]==v for k,v in old.items())
    assert all(new[k]==1 for k in new-old)
SOURCE.write_text(after,newline='\n')
for package,unit in [('two_junctions','night:P4.57'),('three_junction','night:P4R.20')]:
    prefix=f'S6_SERIES_PUBLISH_sec07_{package}_'
    for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
        _,rows=read_tsv(folder/(prefix+suffix))
        if suffix=='CHECK_EVENTS.tsv':
            for row in rows:
                if 'effort' not in row['who']:row['who']+='; effort setting not separately exposed'
        print(package,suffix,append_rows(ROOT/target,rows,key))
    _,statuses=read_tsv(folder/(prefix+'unit_progress.tsv'))
    for row in statuses:
        kind='structure' if row['row']=='restructuring' else row['row']
        if kind not in ['D10','D16']:
            set_unit_status(unit,kind,row['status'],row['basis'],row['fragment'])
append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',[dict(
    change_id='II-C3-ROOT-SPECTRAL-GENUS-SUBSECTION',type='D14',statement_id='lem:II:cubic-spectral-genus',
    old_location='Common genus lemma before the horizontal-cover subsection',old_page='current working source',
    new_location='Separate earlier residual-cubic-genus subsection',new_page='integrated final build pending',
    old_text=anchor,new_text=heading+anchor,
    reason='The general lemma used by P455, P457 and R20 has its own actual subsection instead of being appended to the preceding elliptic-contraction unit. Its complete statement and proof are unchanged.',
    review_status='Root read the complete receiving P323 proof and exact applications; subsection migration supplies no movement credit.')],'change_id')
fields,progress=read_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
for kind in [f'D{i:02}' for i in range(1,26)]+['structure']:
    progress.append(dict(zip(fields,['II','subsec:II:cubic-spectral-genus','Genus of residual cubic covers',
        'structure' if kind=='structure' else 'defect','' if kind=='structure' else kind,
        'open' if kind in ['D14','D23','structure'] else 'done',now(),
        'CHECK_EVENTS.tsv: II-C3-ROOT-JUNCTIONS-ADMISSION',
        'Complete common genus owner and all original transferred calculations compared. Exact quotient convention, bundle maps, common-zero divisor and normalization colength remain. Global order and final PDF reading remain open; new-unit migration earns no movement credit.'])))
keys=[(r['paper'],r['unit_id'],r['defect_type'] or r['row_kind']) for r in progress]
assert len(keys)==len(set(keys))
write_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',fields,progress)
append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',[dict(
    source='Beauville1978 (third-continuation cubic spectral genus)',url='https://numdam.org/item/AST_1978__54__R1_0.pdf',
    version='Surfaces algebriques complexes, Asterisque54(1978)',
    locus='III.17 pp45–46 and complete III.18/proof pp46–47, freshly reopened by foundations reviewer in the attached primary text',
    date_utc=now(),sha256='a2bdff071df610a8e39200a16ad7675149c1ddf601157b3e3e56cbf285994e4e',
    own_word_summary='The ruled-surface quotient convention gives the tautological and fibre classes, their intersections and the canonical class through the exact tautological bundles.',
    use='P323 writes the identical holomorphic quotient, kernel and relative tangent maps for rank-two E over P1. Its cubic residual divisor and double-component-plus-section formulas are then computed in that same basis; P455 uses e0/e2 and P457/R20 use e2.')],'source')
add_event('lem:II:cubic-spectral-genus;night:P4.55;night:P4.57;night:P4R.20',
    'II-C3-ROOT-JUNCTIONS-ADMISSION','used and rechecked in this run',
    'Foundations read complete original/current/receiving P455/P457/R20 and P323, with the complete required P251/P282/P252/P299/P458 inputs and consumer. Root read every receiving P323/P457/R20 paragraph and both full comparison records, plus the exact bounded P455/R20 genus transfers. The general arithmetic-genus calculation now has one earlier owner with the exact tautological quotient, kernel, relative tangent maps and cubic divisor. All three inherited formula labels remain there. P455 full statement and all normal derivative maps are unchanged. P457 retains all Hessian, graph, coefficient-content and factor allocations, with explicit P299 auxiliary X=0 and the parameter-preserving quadratic coordinate inverse. R20 retains the full branch domain and tree budget, the unit in the complete cubic tensor, adapted normal coordinates, exact conductor multiplication maps, unique-preimage premise for each local/global degree, and both globally marked conductor vectors. P458 uses the unchanged conclusion. The two stable original unit statuses are imported; final placement and PDF reading remain open. Exposed rereading only, with no independent or final-page credit.',
    'Common residual-cubic owner and complete two/three-junction units',source=__file__)
print('P323/P457/R20 and bounded P455 applications admitted.')
