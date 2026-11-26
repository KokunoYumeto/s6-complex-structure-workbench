"""Admit the complete rational-boundary owner and its compared consumers."""
from S6_SERIES_PUBLISH_c3_edit import *
import json

folder=ROOT/'agents/continuation3_foundations/sec11'
prefix='S6_SERIES_PUBLISH_sec11_rational_boundaries_'
guards=json.loads((folder/(prefix+'guards.json')).read_text())
assert len(guards)==3
before=SOURCE.read_text()
after=before
for guard in guards:
    assert after.count(guard['old'])==1,(guard['key'],after.count(guard['old']))
    after=after.replace(guard['old'],guard['new'],1)
old_labels,old_tags=identifiers(before)
new_labels,new_tags=identifiers(after)
assert not old_labels-new_labels
assert new_labels-old_labels==Counter({'lem:II:positive-rational-curve':1,'subsec:II:rational-boundaries-maxima':1})
assert new_tags-old_tags==Counter({'tag-P365':1})
assert not old_tags-new_tags
for guard in guards[1:]:
    assert guard['old'].split(r'\end{proposition}',1)[0]==guard['new'].split(r'\end{proposition}',1)[0]
for label in ['push:src:E.5.2','push:src:E.5.3']:
    def statement(t):
        i=t.index(r'\label{'+label+'}')
        a=t.rfind(r'\begin{',0,i)
        env=re.match(r'\\begin\{([^}]+)\}',t[a:])[1]
        b=t.index(r'\end{'+env+'}',i)+len(r'\end{'+env+'}')
        return t[a:b]
    assert statement(before)==statement(after),label
for label in ['cdp:eq:C.NM.4','cdp:eq:C.NM.5','cdp:eq:C.NM.6','cdp:eq:C.AP.8','cdp:eq:C.AP.9']:
    assert after.count(r'\label{'+label+'}')==1,label

_,statuses=read_tsv(folder/(prefix+'unit_progress.tsv'))
assert len(statuses)==26
units={r['unit'] for r in statuses}
assert units=={'subsec:II:rational-boundaries-maxima'}
fields,progress=read_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
assert not any(r['paper']=='II' and r['unit_id'] in units for r in progress)
titles={label:title for title,label in re.findall(r'^\\subsection\{([^\n]+)\}\\label\{([^}]+)\}',after,re.M)}
for row in statuses:
    kind='structure' if row['row']=='restructuring' else row['row']
    progress.append(dict(zip(fields,['II',row['unit'],titles[row['unit']],
        'structure' if kind=='structure' else 'defect','' if kind=='structure' else kind,
        'open' if kind in {'D14','D23','D24','structure'} else row['status'],now(),
        'CHECK_EVENTS.tsv: II-C3-ROOT-RATIONAL-BOUNDARIES-ADMISSION',
        row['basis']+' Foundations read every complete original and receiving UN69/UN81/UN85 proof, '
        'all stated component inputs and direct UN72 consumer. Root read the complete P365 and UN69 receivers, '
        'every bounded UN81/UN85 transfer with context, the complete comparison/status, equation map, source/events and defect reasons. '
        'Original sec11 and the full UN81/UN85 units remain open. No subdivision, independent-check, required-check or final-page credit.'])))
keys=[(r['paper'],r['unit_id'],r['defect_type'] or r['row_kind']) for r in progress]
assert len(keys)==len(set(keys))
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),
                         ('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _,rows=read_tsv(folder/(prefix+suffix))
    if suffix=='CHECK_EVENTS.tsv':
        assert all(r['type']=='used and rechecked in this run' and 'effort' in r['who'] for r in rows)
    print(suffix,append_rows(ROOT/target,rows,key))
SOURCE.write_text(after,newline='\n')
write_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',fields,progress)
_,sources=read_tsv(folder/(prefix+'sources.tsv'))
incoming=[dict(source=r['source_id']+' (third-continuation rational boundaries)',url=r['url'],version=r['version'],
    locus=r['exact_locus']+'; '+r['reader'],date_utc=r['date_utc'],sha256=r['sha256'],own_word_summary=r['own_paraphrase'],
    use='Foundations reopened the complete primary statements and analytic setup at the stated locus; the source refers elsewhere for proofs. '
        'Root read the exact receiving surface maps and source attribution. No additional root primary reading or unprinted-proof reading is claimed.') for r in sources]
print('Sources',append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',incoming,'source'))
add_event('lem:II:positive-rational-curve;cdp:st:C.2.UN.69;cdp:st:C.2.UN.81;cdp:st:C.2.UN.85',
    'II-C3-ROOT-RATIONAL-BOUNDARIES-ADMISSION','used and rechecked in this run',
    'Three exact guards admitted after exposed complete original/receiving UN69/UN81/UN85 proof comparisons. '
    'Root read all P365 and UN69 receiving statements/proofs, every bounded UN81/UN85 transfer with its surrounding context, '
    'and the complete comparison/status, equation map, source/events and distinct defect reasons. '
    'P365 uses m_i=1, t=s and G={1} in the component cover to identify the same minimal model, '
    'then the explicit pluricanonical base line, positive point discrepancies and adjunction. '
    'Its selected s-point blowups give the same square-zero pencil and rational vertical curves; '
    'its s=1 complete plane morphism satisfies rho*ell=C, factors away from C and contracts disjoint boundaries. '
    'UN69 uses its identical higher-endpoint curves and retains the full maximum, point-contraction, Euler and inverse-neighbourhood conclusions. '
    'UN81 uses (T,C)=(Q,E); UN85 names its identical +1 receiver and the unchanged AP10–13 progress block. '
    'Five equation owners transfer uniquely; all old identifiers remain. UN81/UN85 statements and E.5.2/E.5.3 are byte-identical. '
    'The source statement/setup reading is accurately limited; original sec11 and global/final-page gates stay open. '
    'No independent-check, required-check or subdivision credit.',
    'Rational boundaries and maximum components; bounded UN81/UN85 plane-map applications',
    source='code/S6_SERIES_PUBLISH_c3_rational_boundaries_admit.py')
print('P365 and rational-boundary unit admitted; original section11 reduction remainder remains open.')
