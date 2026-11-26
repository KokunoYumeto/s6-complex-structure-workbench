from pathlib import Path
import csv
import datetime as dt
import hashlib
import json

R = Path(__file__).resolve().parents[1]
P = 'agents/continuation2_root/01BW/S6_SERIES_PUBLISH_II_root_BW'
def bind(p):
    b = (R / p).read_bytes()
    return dict(path=p, sha256=hashlib.sha256(b).hexdigest(), bytes=len(b))
def read(p):
    return json.loads((R / p).read_text())
def save(p, obj):
    assert not (R / p).exists(), p
    (R / p).write_text(json.dumps(obj, indent=2) + '\n')
    return bind(p)

now = dt.datetime.now(dt.timezone.utc).isoformat()
who = 'GPT-6 Astra (OpenAI), ChatGPT Pro mode, root, second continuation; reasoning effort not separately exposed'
proposal = read(P + '_editorial_proposal_v1.json')
assert bind(proposal['proposed']['path'])['sha256'] == '856dda905d7f4e34d0fb6770ca695274ff5347174e1953817df39e0e845e4f5d'
original = (R / proposal['original']['path']).read_text()
work = original
for g in proposal['guards']:
    assert hashlib.sha256(work.encode()).hexdigest() == g['before_sha256']
    assert work.count(g['old']) == g['occurrences']
    work = work.replace(g['old'], g['new'])
    assert hashlib.sha256(work.encode()).hexdigest() == g['after_sha256']
assert work == (R / proposal['proposed']['path']).read_text()
for g in reversed(proposal['guards']):
    i = g['offset_before']
    assert work[i:i+len(g['new'])] == g['new']
    work = work[:i] + g['old'] + work[i+len(g['new']):]
assert work == original

programs = [
    dict(source=bind('code/S6_SERIES_PUBLISH_II_root_BW_prerelease_intersections.py'),
         output=bind(P + '_prerelease_intersections.json'),
         timing='Before the05:45:52UTC derivation freeze',
         method='Symbolic intersection ring xi squared2, xi.F1, F squared0; Riemann-Roch and Euler/Gysin polynomial substitutions'),
    dict(source=bind('code/S6_SERIES_PUBLISH_II_root_BW_koszul_spectrum.py'),
         output=bind(P + '_koszul_spectrum.json'),
         timing='After target release; executed and fully read before final proposed-proof reading',
         method='Exact integer-weight Koszul Hilbert series by coin recurrences and alternating degree shifts; spectral-degree and eigenvalue congruence counts')
]
computation = save(P + '_computation_receipt_v1.json', dict(
    created_utc=now, checker=who, programs=programs,
    all_code_and_output_fully_read=True, process_results='Both programs exited0; exact identities and every table-row assertion passed.',
    independent_method='The postrelease calculation uses the graded regular-sequence Hilbert series, instead of the printed explicit Jacobian monomial bases. The entire stated table agrees.',
    historical_program_replayed=False,
    historical_scope='The literal root_cubic_normal_cone.py filename was absent from attached/base filename indexes. The exact printed algorithm was read; the pinned raw URL opening returned DisabledError. No historical source or output is claimed retrieved or replayed.',
    scope='Finite arithmetic only; the written derivation and comparison establish the geometry, analytic classification and actual homology maps.'))
retrieval = read(P + '_primary_retrieval.json')
for x in retrieval['sources']:
    assert x['status'] == 'downloaded'
    assert hashlib.sha256(Path(x['temporary_path']).read_bytes()).hexdigest() == x['sha256']
primary = save(P + '_primary_readings_v1.json', dict(
    created_utc=now, checker=who, retrieval=bind(P + '_primary_retrieval.json'),
    editions=[dict(name=x['name'], url=x['requested_url'], sha256=x['sha256'], bytes=x['bytes']) for x in retrieval['sources']],
    loci=[
        dict(name='MerleTeissier1977', locus='Textpp11-13, PDFpages14-16, full Theorem2.1.1 and proof, Remark2.1.2 and Corollary2.1.3',
             reading='All three actual rendered page images read, in addition to primary PDF extraction.', refs=['turn828658294view0','turn279695903view0','turn789458220view0']),
        dict(name='Steenbrink1989Spectrum', locus='Printedpp165-167, weighted Jacobian spectrum, convolution theorem and genus interval(-1,0]',
             reading='All three actual rendered page images read in full.', refs=['turn828658294view1','turn279695903view1','turn789458220view1']),
        dict(name='Nemethi1991Join', locus='Printedpp1-3, full introduction, TheoremL1, Remark2.2 and Example2.4(a)',
             reading='Full primary-PDF extracted text read in one untruncated output. No new image-reading claim.', refs=['turn828658294view2','turn279695903view3'])
    ],
    exact_scope='Isolated weighted homogeneous surface suspensions, Newton-nondegenerate adjunction, monodromy of the actual join including the disconnected w-cube fibre.',
    final_publication_page_credit=0,
    open_bibliographic_issue='Official scan and metadata list Teissier before Merle; current TeX and shared bibliography list the reverse order. Correct author order and alphabetical placement in the integrated bibliography pass.',
    primary_metadata_url='https://www.numdam.org/item/SSS_1976-1977____A16_0/'))
comparison = bind(P + '_comparison_v1.md')
events = []
outcomes = [
    ('targeted proof check', 'target',
     'Complete statement-led derivation frozen before the target was released, using the supplied RAT6 statement in total delta at most4. It identifies the actual tangent-root cover by its function field, computes the ruled normal bundle and cyclic cover, derives chi2 and q<=1, proves a positive compact-core pairing and b1<=3 by Gysin and Hodge index, and embeds that same core into the original nearby torus by deformation to the normal cone of a genuine local root of f. The covering lift into R4/A makes its H2 pairing zero, giving the contradiction and both rationality and a scalar zero. The complete twelve-item target proof was then read and compared; its a0 sphere argument, local ADE table, stronger independent-boundary formulas and all morphisms were checked. The missing printed RAT6 body is separately recorded; BW itself supplies and proves its required local table. Prior accidental BY inventory-summary exposure is disclosed and gives no blind BY credit.'),
    ('computation or formal certificate', 'compute',
     'New exact intersection-ring program before freeze verifies character Euler characteristics1,0,1, genera4-2k and3+ell-k, section intersection2-ell-k, pullback square6 and the positive core-rank lower bound. A new postrelease Koszul Hilbert-series calculation recomputes every printed ADE cubic-suspension genus and link Betti number through delta4 using a different method from the displayed Jacobian bases. All agree; dynamic programming gives total genus<=1 and link b1<=2. Additional delta5 ADE arithmetic has no separate proof-check credit. Full programs and outputs read. No historical replay, analytic-classification certificate or whole-proof formal-verification claim.'),
    ('used and rechecked in this run', 'reread',
     'Read all twelve original items and every display, then the complete final twelve-item proposed proof. Sixteen exact reversible guards retain the theorem body, all twelve mathematical steps, all displays, all mathematical inline formulas and every label/tag. They remove a machine header, production numbering, internal program path and emphatic wording, and add exact opened literature pages. No mathematical error found and no alternative proof substituted. Primary MTpp11-13 and Steenbrinkpp165-167 images actually read; Nemethipp1-3 full extracted text read. These openings and this final comparison add no independent evidence group or final-paper-page credit.')
]
for kind, suffix, outcome in outcomes:
    events.append(dict(statement_id='cdp:st:C.2.D4.1', date=now[:10], date_utc=now,
                       who=who, type=kind, event_id='ce:S6_SERIES_PUBLISH_II_root_01BW_' + suffix + '_20261122',
                       evidence_group='S6_SERIES_PUBLISH_II_root_01BW_20261122', event_count=1,
                       source_file=comparison['path'], where='01BW / cdp:st:C.2.D4.1; complete statement and all twelve proof items',
                       outcome=outcome))
event_binding = save(P + '_events_v1.json', dict(created_utc=now, events=events, independent_groups=1, canonical_events_added=0))
review_path = 'records/S6_SERIES_PUBLISH_II_root_continuation2_batch53_review.json'
review = save(review_path, dict(
    created_utc=now, checker=who, complete_review=True,
    actual_reading='Entire seven-section frozen derivation; complete twelve-item original proof after release; complete final twelve-item proof; both full programs and outputs; all sixteen editorial guards; complete primary loci and all images specified in the primary record. The comparison gives every original proof item, exact maps and formula conversions.',
    comparison=comparison, computations=computation, primary_readings=primary,
    statement_body_byte_identical=True, mathematical_steps_changed=0,
    all_displays_labels_tags_and_mathematical_inline_formulas_preserved=True,
    enumeration_label_removed='The production label token is presentation, explicitly excluded from the inline-formula sequence check.',
    chronology='Derivation freeze05:45:52UTC precedes release05:45:56UTC. The Hilbert-series table and primary rereading are postrelease. The original twelve mathematical steps remain printed. No new blind claim for BY or independent RAT6 check is inferred.',
    independent_required_owners=1, independent_evidence_groups=1, proposed_events=3,
    publication_page_reading_credit=0,
    open_obligations='Missing RAT6 authority and MT author order remain explicitly open in the comparison; no global defect-class closure is credited.'))
freeze = bind('agents/ii_infra/derivation_freezes/01BW/20261122T054552868651Z/S6_SERIES_PUBLISH_derivation_freeze_receipt.json')
release = bind('agents/ii_infra/released_proofs/01BW/cb2f1578c62bf37c/S6_SERIES_PUBLISH_release_receipt.json')
with (R.parent / 'S6_SERIES_GRIND_tags.tsv').open() as f:
    pages = {x['tag']: x['page'] for x in csv.DictReader(f, delimiter='\t')}
target = dict(owner='cdp:st:C.2.D4.1', tag='01BW', old_page=pages['01BW'],
              original=proposal['original'], proposed=proposal['proposed'], freeze=freeze, release=release,
              events=event_binding, who=who, guards=proposal['guards'],
              scope='Complete connected degree-three normalization-cover exclusion over a smooth rational image: the cover is rational and its whole cubic normal tensor has a zero.',
              event_note='Complete frozen/original/final comparison and two new calculations with their exact chronology. All twelve original mathematical steps remain; three events share one group. No extra RAT6, BY, publication-page or global defect-class credit.')
s = (R / 'S6_SERIES_PUBLISH_II.tex').read_text()
a = s.index('\\section*{Programs}')
b = s.index('\\end{longtable}', a)
last = s[s.rfind('\n', a, b - 1) + 1:b]
assert 'WW_original_foliation.py' in last
rows = ''
for description, name in [
    ('Cubic-cover intersection numbers and compact-core ranks', 'S6_SERIES_PUBLISH_II_root_BW_prerelease_intersections.py'),
    ('Cubic-suspension Jacobian spectra by the Koszul Hilbert series', 'S6_SERIES_PUBLISH_II_root_BW_koszul_spectrum.py')
]:
    rows += (description + r' (\cref{cdp:st:C.2.D4.1}) & \href{https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\SsixRepositoryCommit/code/' + name + r'}{\nolinkurl{' + name + r'}} \\[3pt]' + '\n')
extra = dict(old=last, new=last+rows, type='D09,D18', location='Programs',
             reason='List once each exact intersection and graded-spectrum program that verifies the retained triple-cover proof calculations.')
copies = [dict(**{'from': x['output']}, to='code/' + Path(x['output']['path']).name) for x in programs]
cfg = dict(batch=53, root_review_complete=True,
           source_before_sha256=bind('S6_SERIES_PUBLISH_II.tex')['sha256'],
           ledger_before_sha256=bind('CHECK_EVENTS.tsv')['sha256'],
           review_evidence=[review, comparison, computation, primary, bind(P+'_editorial_proposal_v1.json'), bind(P+'_primary_retrieval.json'), event_binding] +
                           [x[k] for x in programs for k in ('source','output')],
           targets=[target], additional_source_edits=[extra], code_copies=copies, mathematical_repairs=[],
           scope='01BW admitted after its complete prerelease statement-led derivation and complete original/final twelve-step comparison. The exact root-curve identification, cyclic compactification, local singularity bounds, compact-core pairing and embedding into the original torus were verified. New prerelease intersection arithmetic and postrelease Koszul spectra agree with every displayed value. All original mathematical steps and formulas remain, with sixteen presentation/citation guards and two Programs rows. Three events form one independent group. Missing RAT6 authority and a primary author-order discrepancy remain recorded editorial obligations; no global defect class or final-PDF page is closed.')
assert cfg['source_before_sha256'] == '6610c70b1e3ea2fdcfe3554b340c3ce80719a923cfda48635fffaa6da76d1caa'
assert cfg['ledger_before_sha256'] == 'f16c30453263a9eec3ffd318db45c663a116938455d8261502e536ef652c3a12'
out = 'records/S6_SERIES_PUBLISH_II_continuation2_batch53_config.json'
print(json.dumps(save(out, cfg), indent=2))
