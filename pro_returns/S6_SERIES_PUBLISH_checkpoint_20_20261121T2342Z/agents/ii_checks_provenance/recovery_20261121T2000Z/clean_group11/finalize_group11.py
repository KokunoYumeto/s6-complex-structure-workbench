from pathlib import Path
import csv
import datetime
import difflib
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
SOURCE = ROOT / 'S6_SERIES_PUBLISH_II.tex'
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()


def bound(path):
    return {'path': str(path.relative_to(ROOT)), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}


def save(name, obj):
    path = OUT / name
    assert not path.exists(), path
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n')
    return bound(path)


prep = OUT / 'S6_SERIES_PUBLISH_II_clean_group11_preparation_v3.json'
data = json.loads(prep.read_text())
source_text = SOURCE.read_text()
comparison = bound(OUT / 'S6_SERIES_PUBLISH_II_clean_group11_comparison.md')
primary_dir = ROOT / 'agents/ii_infra/recovery_20261121/F5_F7_GD_primary_inputs'
primary_rows = [
    {
        'key': 'Kawai1969',
        'pdf': bound(OUT / 'primary/Kawai1969.pdf'),
        'scope': 'Complete Proposition 2 and its proof, printed pp.605–608, read before freeze. The following corollary was read as excluded context. Publisher metadata confirms journal 21(4),604–616; the final printed page616 was separately checked in extracted text. No whole-article proof-reading claim.',
        'doi': '10.2969/jmsj/02140604',
    },
    {
        'key': 'Buchdahl1999',
        'pdf': bound(OUT / 'primary/Buchdahl1999.pdf'),
        'scope': 'Theorem11 printed p.297 and introductory theorem read before freeze; complete p.297 image actually viewed after release. The exact even-b1 criterion is the printed input.',
        'images_actually_viewed': [bound(OUT / 'primary/Buchdahl1999_printed297.png')],
        'doi': '10.5802/aif.1674',
    },
    {
        'key': 'SS2002',
        'pdf': bound(primary_dir / 'S6_SERIES_PUBLISH_II_SS2002_arxiv_v2_pdf.download'),
        'edition_binding': bound(primary_dir / 'S6_SERIES_PUBLISH_II_SS2002_v2_exact_source_binding.json'),
        'scope': 'After release, full text §1 pp.2–3 and Proposition3.1 with its complete proof pp.6–7 read. Complete primary p.3 image actually viewed, including the Picard quotient, degree-d associated line bundle and alpha multiplier. No Paper II rendered-page credit.',
        'images_actually_viewed': [bound(primary_dir / 'S6_SERIES_PUBLISH_II_SS2002_v2_page-03.png')],
    },
    {
        'key': 'Borcea1984',
        'pdf': bound(primary_dir / 'S6_SERIES_PUBLISH_II_Borcea1984_primary.pdf'),
        'scope': 'After release, extracted article text pp.373–380 read; equations missing from that extraction are not treated as read by that act. Complete images of pp.377,379,380 were then actually viewed and read, binding Remark1, the displayed period quotient and Theorem4. Reliance is on these identified loci; no claim that every omitted formula on other pages was visually read.',
        'images_actually_viewed': [bound(primary_dir / f'S6_SERIES_PUBLISH_II_Borcea1984_pdfp{n:02d}.png') for n in [6,8,9]],
    },
]
primary_receipt = save('S6_SERIES_PUBLISH_II_clean_group11_primary_receipt.json', {
    'created_utc': NOW, 'checker': 'i_provenance_recovery',
    'prereading_inputs': data['prereading_inputs'],
    'rows': primary_rows,
    'publisher_metadata': bound(OUT / 'primary/S6_SERIES_PUBLISH_II_group11_metadata_receipt.json'),
    'rendered_manuscript_page_credit': 0, 'events_added': 0,
})

owners = {row['statement_owner'] for row in data['targets']}
ledger = ROOT / 'CHECK_EVENTS.tsv'
with ledger.open() as f:
    historical = [{'ledger_row': n, 'event': r} for n, r in enumerate(csv.DictReader(f, delimiter='\t'), 2) if r['statement_id'] in owners]
historical_receipt = save('S6_SERIES_PUBLISH_II_clean_group11_historical_computation_scope.json', {
    'created_utc': NOW, 'ledger': bound(ledger), 'rows': historical,
    'timing': 'Exact-owner ledger rows were read only after all three independent freezes and target releases.',
    'finding': 'These 17 exact-owner rows name primary-source openings and mathematical proof comparisons. None identifies a computer routine or an unnamed program rerun for these three owners. This is a bounded finding about these rows, not a repository-wide absence claim.',
    'new_computation_events': 0, 'events_added': 0,
})

# The completed G7 input was actually read after the FF freeze.
p = source_text.index(r'\label{cdp:st:D.1.9}')
a = source_text.rfind(r'\begin{proposition}', 0, p)
b = source_text.index(r'\end{proof}', p) + len(r'\end{proof}')
g7 = OUT / 'S6_SERIES_PUBLISH_II_clean_group11_current_G7_input.tex'
assert not g7.exists()
g7.write_text(source_text[a:b])
g7_receipt = save('S6_SERIES_PUBLISH_II_clean_group11_current_G7_input.json', {
    'created_utc': NOW, 'source': bound(SOURCE), 'input': bound(g7),
    'source_span': [a,b], 'actual_reading': 'The complete current D.1.9 statement and proof were read as a postrelease input. Its integral class is nonzero on every full fibre; natural coherent base change then gives exactly FF step1.',
    'new_target_credit': False, 'events_added': 0,
})

validation_rows = []
preview = source_text
for row in data['targets']:
    before = (ROOT / row['original_full_block']['path']).read_text()
    after = (ROOT / row['proposed_full_block']['path']).read_text()
    assert source_text.count(before) == 1
    reconstructed = before
    for guard in row['guards']:
        assert reconstructed.count(guard['old']) == guard['expected_occurrences_in_owning_block']
        reconstructed = reconstructed.replace(guard['old'], guard['new'])
    assert reconstructed == after
    displays = lambda text: re.findall(r'\\\[(.*?)\\\]', text, flags=re.S)
    labels = lambda text: re.findall(r'\\(?:label|hypertarget)\{([^}]+)\}', text)
    refs = lambda text: re.findall(r'\\(?:ref\*?|eqref|SeriesRef)\{([^}]+)\}', text)
    assert displays(before) == displays(after)
    assert labels(before) == labels(after)
    assert refs(before) == refs(after)
    inline = lambda text: re.findall(r'(?<!\\)\$(?!\$)(.*?)(?<!\\)\$', text, flags=re.S)
    bi, ai = inline(before), inline(after)
    delta = [{'opcode': op, 'old': bi[x:y], 'new': ai[u:v]} for op,x,y,u,v in difflib.SequenceMatcher(a=bi,b=ai).get_opcodes() if op != 'equal']
    validation_rows.append({
        'tag': row['tag'], 'original_full_block': row['original_full_block'], 'proposed_full_block': row['proposed_full_block'],
        'exact_guard_reconstruction': True, 'all_displayed_math_identical': True,
        'label_and_tag_sequence_identical': True, 'coded_reference_sequence_identical': True,
        'inline_math_delta': delta,
        'delta_scope': 'FD adds the explicit normalization transport and its map notation. FF adds Y to the smooth-domain statement and removes only the inline symbols in a redundant negative extension disclaimer. FE inline and displayed formulas are unchanged.',
    })
    preview = preview.replace(before, after)
for guard in data['bibliography_guards']:
    assert preview.count(guard['old']) == 1
    preview = preview.replace(guard['old'], guard['new'])
inverse = preview
for guard in reversed(data['bibliography_guards']):
    assert inverse.count(guard['new']) == 1
    inverse = inverse.replace(guard['new'], guard['old'])
for row in reversed(data['targets']):
    after = (ROOT / row['proposed_full_block']['path']).read_text()
    before = (ROOT / row['original_full_block']['path']).read_text()
    assert inverse.count(after) == 1
    inverse = inverse.replace(after, before)
assert inverse == source_text
validation = save('S6_SERIES_PUBLISH_II_clean_group11_guard_validation.json', {
    'created_utc': NOW, 'source': bound(SOURCE), 'rows': validation_rows,
    'full_source_preview_sha256': hashlib.sha256(preview.encode()).hexdigest(),
    'full_source_forward_inverse_exact': True, 'canonical_mutations': 0, 'events_added': 0,
})

reading = save('S6_SERIES_PUBLISH_II_clean_group11_final_pair_reading.json', {
    'created_utc': NOW, 'checker': 'i_provenance_recovery', 'source': bound(SOURCE),
    'rows': [{
        'tag': row['tag'], 'statement_owner': row['statement_owner'],
        'released_original_full_block': row['released_original_full_block'],
        'current_original_full_block': row['original_full_block'],
        'final_proposed_full_block': row['proposed_full_block'],
        'complete_original_statement_and_proof_actually_read': True,
        'complete_current_original_statement_and_proof_actually_read': True,
        'complete_final_proposed_statement_and_proof_actually_read': True,
        'manual_exact_guard_comparison': True,
        'final_version': {'01FD':'v3','01FE':'v2','01FF':'v1 (unchanged in later preparations)'}[row['tag']],
        'scope': 'The entire owning proof was read, including the construction, every displayed equation and all terminal deductions. Reading is an actual source-text review, not inferred from automatic validation or a page image.',
    } for row in data['targets']],
    'comparison': comparison,
    'bibliography_pairs_actually_read': True, 'primary_receipt': primary_receipt,
    'rendered_manuscript_page_credit': 0, 'canonical_mutations': 0, 'events_added': 0,
})
transport = save('S6_SERIES_PUBLISH_II_clean_group11_exact_transport.json', {
    'created_utc': NOW, 'source': bound(SOURCE), 'comparison': comparison,
    'current_G7_input': g7_receipt, 'guard_validation': validation,
    'receiver_records': [r['receiving_uses'] for r in data['targets']],
    'integral_CDP_setup': bound(ROOT / 'agents/ii_infra/S6_SERIES_PUBLISH_II_front_main_statements_conventions.tex'),
    'scope_exceptions': {
        '01FD': 'The original singular-total-space reading is not certified. Smooth connected Y is explicit. The broad compact-curve target is preserved through the proved reduction/normalization map; this clarification was written after release. Every subsequent diagram uses the lifted map and base under the declared notation.',
        '01FE': 'Current C.3.1 already provides smooth Y; no duplicate edit is proposed. Steps1–2 explicitly concern a primary surface, followed by the separately proved finite-cover descent in step3. The final statement, all inline formulas and displayed formulas are unchanged.',
        '01FF': 'The original singular-total-space reading is not certified. Smooth connected Y is explicit. All six Picard identities and their k,h,N,d,12,m factors are unchanged. The frozen local-Albanese explanation is expanded after release by the relative-closedness, fixed rank-two period quotient and local quotient map (z,t)->(z^e,t) in the comparison record.',
    },
    'no_singular_counterexample_claimed': True,
    'no_extra_independence_from_postrelease_clarifications': True,
    'all_displayed_final_conclusions_preserved': True, 'events_added': 0,
})

for row in data['targets']:
    row['proposed_full_proof_reading_pending'] = False
    row['proposed_full_proof_actually_read'] = True
    freeze = json.loads((ROOT / row['freeze_receipt']['path']).read_text())
    row['frozen_derivation'] = bound(ROOT / freeze['frozen_derivation_path'])
    assert row['frozen_derivation']['sha256'] == freeze['derivation_sha256']
data.update({
    'status': 'immutable final proposal; root approval and exact canonical application pending',
    'completed_utc': NOW, 'source_at_final_review': bound(SOURCE),
    'preparation': bound(prep), 'comparison': comparison, 'primary_receipt': primary_receipt,
    'historical_computation_scope': historical_receipt, 'final_pair_reading': reading,
    'exact_transport': transport, 'guard_validation': validation,
    'prospective_counts': {'targeted proof check':3, 'used and rechecked in this run':3, 'extra_computation_events':0},
    'remaining_gates': ['Root review and approval', 'Exact canonical full-block application', 'Root append-only event admission'],
})
final = save('S6_SERIES_PUBLISH_II_clean_group11_final_proposals.json', data)

scopes = {
    '01FD': 'Frozen smooth-domain invariant-cycle derivation precedes target reading. The complete original and final positive Kähler-pairing proofs were compared. Kawai Proposition2 maps and Buchdahl Theorem11 are primary-bound. The explicitly proved normalization lift is a postrelease clarification, not a new prereading derivation; the compact-curve statement is preserved. Singular total spaces are not certified.',
    '01FE': 'Frozen resonant-monomial, finite invariant-ring and analytic countability derivation precedes target reading. The complete original and final anticanonical-divisor proofs were compared. Primary scope in steps1–2 is explicit before finite-cover descent. Current C.3.1 already supplies smooth Y. Every displayed and inline formula and the final exclusion/countability conclusion are preserved.',
    '01FF': 'Frozen intrinsic-line/constant-character derivation precedes target reading. The complete printed Picard-quotient, finite-action and degree-m norm proof was compared, retaining every factor through the exact 12m identity. Smooth total space is explicit. The local-family clarification is postrelease and receives no additional independence or computation event.',
}
events = []
for row in data['targets']:
    common = {k: row[k] for k in ['tag','statement_owner','checker','freeze_receipt','frozen_derivation','release_receipt','release_envelope','released_original_full_block','original_full_block','proposed_full_block']}
    common.update({
        'paper':'II', 'proposal_only':True, 'event_count':1,
        'proposal_bundle':final, 'source_application_pending':True,
        'mathematical_statement_and_values_unchanged':False,
        'displayed_final_conclusions_preserved':True,
        'bounded_exception_binding':transport, 'no_extra_computation_event':True,
        'prior_exposure': 'The safe statements, named cited inputs and the declared primary-source material were read before freezing; no FD/FE/FF target proof, C reconstruction or old owner check record was read before its freeze. Prior FC/WI Hopf quotient work and Paper I input exposure are disclosed. Exact-owner ledger rows, the printed target proofs and the current G7 proof were read only after all three freezes. No independence from the expressly cited inputs is claimed.',
    })
    events.append(dict(common,event_type='targeted proof check',scope=scopes[row['tag']]))
    events.append(dict(common,event_type='used and rechecked in this run',scope='Complete current original and final proposed owning statement and proof actually read and all exact guards manually compared. One comparative reread scope for this owner; bibliography, source openings, images, automatic comparisons and the separate explanatory addenda give no additional event.'))
event_bundle = save('S6_SERIES_PUBLISH_II_clean_group11_event_proposals.json', {
    'schema_version':1, 'paper':'II', 'created_utc':NOW, 'proposal_only':True, 'events':events,
    'prospective_counts':data['prospective_counts'], 'canonical_mutations':0, 'events_added':0,
})
print(json.dumps({'final_proposals':final, 'event_proposals':event_bundle, 'final_pair_reading':reading, 'guard_validation':validation, 'primary_receipt':primary_receipt, 'exact_transport':transport, 'source':bound(SOURCE), 'owner_guard_records':sum(len(x['guards']) for x in data['targets']), 'owner_literal_occurrences':sum(g['expected_occurrences_in_owning_block'] for x in data['targets'] for g in x['guards']), 'bibliography_pairs':len(data['bibliography_guards'])},indent=2))
