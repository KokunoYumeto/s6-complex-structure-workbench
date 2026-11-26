"""Admit the general residue and effective Hopf boundary owners and receivers."""
from S6_SERIES_PUBLISH_c3_edit import *
import json

folder=ROOT/'agents/continuation3_foundations/sec11'
prefix='S6_SERIES_PUBLISH_sec11_hopf_boundaries_'
before=SOURCE.read_text(); after=before
for row in json.loads((folder/(prefix+'guards.json')).read_text()):
    assert after.count(row['old'])==1,row['key']
    after=after.replace(row['old'],row['new'],1)
preserve_identifiers(before,after)
for old,new in zip(identifiers(before),identifiers(after)):
    assert all(new[k]==v for k,v in old.items())
    assert all(new[k]==1 for k in new-old)
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _,rows=read_tsv(folder/(prefix+suffix))
    for row in rows:
        if suffix=='CHECK_EVENTS.tsv' and 'effort' not in row['who']:
            row['who']+='; effort setting not separately exposed'
    print(suffix,append_rows(ROOT/target,rows,key))
fields,progress=read_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
_,statuses=read_tsv(folder/(prefix+'unit_progress.tsv'))
incoming_units={r['unit'] for r in statuses}
progress=[r for r in progress if not(r['paper']=='II' and r['unit_id'] in incoming_units)]
titles=dict(re.findall(r'^\\subsection\{([^\n]+)\}\\label\{([^}]+)\}',after,re.M))
titles={v:k for k,v in titles.items()}
for row in statuses:
    kind='structure' if row['row']=='restructuring' else row['row']
    status='open' if kind in ['D14','D23','D24','structure'] else row['status']
    progress.append(dict(zip(fields,['II',row['unit'],titles.get(row['unit'],row['unit']),
        'structure' if kind=='structure' else 'defect','' if kind=='structure' else kind,status,now(),
        'CHECK_EVENTS.tsv: II-C3-ROOT-HOPF-BOUNDARIES-ADMISSION',
        row['basis']+' Root read the complete P338, P325, UN64 and UN82 receiving proofs and comparison; foundations read every original and receiving proof. Subsection migration earns no movement credit; the existing section11 open remainder remains open.'])))
keys=[(r['paper'],r['unit_id'],r['defect_type'] or r['row_kind']) for r in progress]
assert len(keys)==len(set(keys))
write_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',fields,progress)
_,sources=read_tsv(folder/(prefix+'sources.tsv'))
incoming=[dict(source=r['source_id']+' (third-continuation effective Hopf boundaries)',url=r['url'],version=r['version'],
    locus=r['exact_locus']+'; '+r['reader'],date_utc=r['date_utc'],sha256=r['sha256'],own_word_summary=r['own_paraphrase'],
    use='The exact primary normal forms and unique nonlinear curve enter P325 through P327 central finite unramified covers. The complete weight equation then proves its effective-divisor dichotomy. No original classification-proof reading is claimed.') for r in sources]
print('Sources',append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',incoming,'source'))
add_event('lem:II:anticanonical-bisection;lem:II:reduced-anticanonical-hopf;cdp:st:C.2.UN.64;cdp:st:C.2.UN.82',
    'II-C3-ROOT-HOPF-BOUNDARIES-ADMISSION','used and rechecked in this run',
    'Foundations read complete original/current and receiving P325, UN64 and UN82, complete P338 and the unchanged complete UN65 consumer. Root read every receiving proof line, the full comparison and source/status records. P338 owns the same Leray-identified degree-two pullback, finite trace and Serre-dual residue map; UN64 uses the identical pair T,C and UN82 the actual minimal ruled pair T0,C0. P325 retains all former reduced conclusions and proves the full effective-divisor dichotomy by its central unramified cover, explicit positive-power multiplier equation, full weight-space calculation and exact triangular/linear coordinate maps. UN82 checks both same-surface applications and retains the full labelled-NC and self-branch domain, point-map comparison, propagation, canonical orders and normal adjunction. All labels/targets keep exact multiplicity. No conditional substitute, narrowing, independent-check, required-check increment or final-page credit. D14/final typography/front-matter/global placement remain open.',
    'Anticanonical bisections, effective Hopf boundaries and maximal Hopf leaves',source=__file__)
print('P338, P325 and complete UN64/UN82 receivers admitted.')
