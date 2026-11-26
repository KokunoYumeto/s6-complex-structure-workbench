"""Admit the compared elliptic-star owners and all five remote receiving guards."""
from S6_SERIES_PUBLISH_c3_edit import *

folder=ROOT/'agents/continuation3_conductor'
prefix='S6_SERIES_PUBLISH_c3_conductor_16_'
before=SOURCE.read_text(); after=before
original=(folder/(prefix+'input.tex')).read_text()
receiving=(folder/(prefix+'replacement.tex')).read_text()
assert after.count(original)==1
after=after.replace(original,receiving,1)
_,guards=read_tsv(folder/(prefix+'remote_repairs.tsv'))
assert len(guards)==5
for row in guards:
    assert after.count(row['old_text'])==1,row['statement_id']
    after=after.replace(row['old_text'],row['new_text'],1)
preserve_identifiers(before,after)
for old,new in zip(identifiers(before),identifiers(after)):
    assert all(new[k]==v for k,v in old.items())
    assert all(new[k]==1 for k in new-old)
for tag in ['P350','P351','P352','P353']:
    assert after.count(r'\hypertarget{tag-'+tag+'}{}')==1
# The former P325 subsection keeps its complete UN64 owner.
assert after.index(r'\label{lem:II:reduced-anticanonical-hopf}') < after.index(r'\label{def:II:elliptic-star-data}')
assert after.index(r'\label{cdp:st:C.2.UN.64}') > after.index(r'\label{subsec:II:terminal-ruled-contractions}')
SOURCE.write_text(after,newline='\n')

for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _,rows=read_tsv(folder/(prefix+suffix))
    if suffix=='CHECK_EVENTS.tsv':
        assert all(r['type']=='used and rechecked in this run' for r in rows)
        assert all('effort' in r['who'] for r in rows)
    print(suffix,append_rows(ROOT/target,rows,key))

fields,progress=read_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
_,statuses=read_tsv(folder/(prefix+'unit_status.tsv'))
incoming={r['unit'] for r in statuses}
assert len(incoming)==8 and len(statuses)==208
progress=[r for r in progress if not(r['paper']=='II' and r['unit_id'] in incoming)]
for row in progress:
    if row['paper']=='II' and row['unit_id']=='sec:II:10':
        row.update(unit_title='Weighted Hopf cycles and support/tree remainder',date_utc=now(),
            evidence='CHECK_EVENTS.tsv: II-C3-ROOT-CONDUCTOR16-ADMISSION',
            detail='The original sec10 open identity remains on the actual weighted-cycle and support/tree remainder, including UN52/54/56/58-63. The complete UN49/50/53 comparisons are admitted in five actual star subsections, but their subdivision gives no original-row movement credit. D10/D16 stay done; every other original remaining criterion stays open.')
for row in statuses:
    kind='structure' if row['criterion']=='restructuring' else row['criterion']
    status='open' if kind in ['D14','D23','D24','structure'] else row['status']
    progress.append(dict(zip(fields,['II',row['unit'],row['title'],
        'structure' if kind=='structure' else 'defect','' if kind=='structure' else kind,status,now(),
        'CHECK_EVENTS.tsv: II-C3-ROOT-CONDUCTOR16-ADMISSION',
        row['reason']+' Root read every complete receiving P350/P351/P352/P353 and merged criterion, full P325/P330/P331 receivers, comparison, all owner transfers and equation destinations, and complete all-class assessments. Conductor read all original/current and receiving proofs. No independent proof, final-page or subdivision completion credit; original sec10 remainder stays open.'])))
keys=[(r['paper'],r['unit_id'],r['defect_type'] or r['row_kind']) for r in progress]
assert len(keys)==len(set(keys))
write_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',fields,progress)
_,sources=read_tsv(folder/(prefix+'primary_sources.tsv'))
incoming_sources=[dict(source=r['source_id']+' (third-continuation elliptic stars)',url=r['url'],version=r['version'],
    locus=r['exact_locus']+'; '+r['reader'],date_utc=r['date_utc'],sha256=r['sha256'],own_word_summary=r['own_paraphrase'],
    use='The exact marked Hopf centralizer and curve/line data are applied through the source-to-current coordinate maps in P325/P352/P353. These are the recorded exposed primary-locus readings; no complete external classification proof or additional root source opening is claimed.') for r in sources]
print('Sources',append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',incoming_sources,'source'))
add_event('def:II:elliptic-star-data;lem:II:elliptic-star-boundary;lem:II:hopf-single-canonical-curve;lem:II:compact-elliptic-star-insertion;cdp:st:C.2.UN.49;cdp:st:C.2.UN.50;cdp:st:C.2.UN.53;lem:II:reduced-anticanonical-hopf;lem:II:zero-chern-elliptic-torsor;lem:II:logarithmic-period-family',
    'II-C3-ROOT-CONDUCTOR16-ADMISSION','used and rechecked in this run',
    'Six atomic guards admitted after full conductor old/current/new proof comparison and root full receiving reads. P350 owns the exact root/normal/product/inverse-transform maps, including all finite secondary integers; P351 owns the unimodular peripheral maps, common core, canonical/direct-image formula and exact nonlinear/diagonal period orders. P325 moves after P337 with its proved connected nonreduced central-cover conclusion and full weighted-polynomial coordinate maps. P352 applies that owner to the complete primary/secondary single-curve canonical classification. P330 receives the exact NS14 alias and P331 the full compact rank-four lattice clause while retaining its logarithmic family. P353 preserves every analytic torsor, gluing, finite action and compact map, with explicit free quotient, uniform norm annulus, cluster and proper gluing proofs. The merged UN53 retains all UN49/50/53 conclusions and identities, including the same initially given q. The old intermediate non-torsion adjective is refuted by the permitted product torsor: all complementary line factors equal one, so M_i,0 is trivial; the proof uses degree zero and every theorem conclusion remains. All 49 equation identities and old labels/targets retain exact multiplicity. No program execution, independent proof, required-check increment, final-page or original sec10 closure.',
    'Five complete star subsections; full P325/P330/P331 receiving owners; weighted/support remainders retained',source=__file__)

report=ROOT/'S6_SERIES_PUBLISH_report.md'
text=report.read_text()
note=('## Paper II current intermediate correction — elliptic-star line\n\n'
      'The old compact star construction called M_i,0 non-torsion for every permitted inverse-transform torus. For the permitted product T0=F×B with complementary base periods having zero fibre coordinate, all its line factors are 1. Hence M_i,0 is the trivial line, of torsion order 1. The receiving P353 proof states the full degree-zero scope and retains the complete unitary gauge, norm, quotient and compact gluing argument, which uses degree zero. Every original UN49/UN50/UN53 theorem conclusion is retained in their shared criterion; this correction concerns that intermediate adjective. The exact proof comparison is II-C3-ROOT-CONDUCTOR16-ADMISSION.\n\n')
assert note not in text
report.write_text(text.replace('# S6 series publication revision\n\n','# S6 series publication revision\n\n'+note,1),newline='\n')
print('All six elliptic-star guards admitted; weighted and support/tree remainder remains open.')
