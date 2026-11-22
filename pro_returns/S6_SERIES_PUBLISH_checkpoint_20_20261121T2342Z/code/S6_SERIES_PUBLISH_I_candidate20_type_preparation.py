#!/usr/bin/env python3
"""Prepare source dispositions only after the final source/ledger release; no canonical writes."""
from pathlib import Path
import argparse
import collections
import copy
import csv
import datetime
import hashlib
import importlib.util
import io
import json
import re

from S6_SERIES_PUBLISH_I_candidate18_type_preparation import core_hash, types_of, bibliography
from S6_SERIES_PUBLISH_I_verify_reread_append import verify_append

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/i_cont_edits'
WORKFLOW = 'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate20_type_closure_workflow.json'
WORKFLOW_SHA = '0a63bd590bfd6b95d99f7c0ad3cf414bf57f7984a4e61b92f22ab3eaaf81faad'
CORE = ['change_id', 'type', 'statement_id', 'old_text', 'new_text', 'reason']
sha = lambda raw: hashlib.sha256(raw).hexdigest()
csv.field_size_limit(100_000_000)
MATH = re.compile(r'(?<!\\)\$\$(?:[\s\S]*?)(?<!\\)\$\$|(?<!\\)\$(?:\\.|[^$])*?(?<!\\)\$|\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)|\\begin\{(?:equation|align|gather|multline|eqnarray)\*?\}[\s\S]*?\\end\{(?:equation|align|gather|multline|eqnarray)\*?\}')
COMMANDS = re.compile(r'\\(?:[A-Za-z@]+\*?|.)')
REFS = re.compile(r'\\(?:label|hypertarget|ref|[cC]ref|eqref|autoref|pageref|SeriesRef|cite\w*)\*?(?:\[[^\]]*\])*\{[^}]*\}')


def bound(item):
    p = (ROOT / item['path']).resolve()
    assert p.is_relative_to(ROOT), ('outside active tree', item['path'])
    raw = p.read_bytes()
    assert sha(raw) == item['sha256'], ('bound file changed', item['path'])
    return raw


def document(item):
    return json.loads(bound(item))


def evidence(item, scope):
    bound(item)
    return {**item, 'scope': scope}


def apply_exact(text, changes):
    for c in changes:
        pos = c['applied_offset']
        assert text[pos:pos + len(c['old'])] == c['old'], c.get('guard_id', c['change_id'])
        text = text[:pos] + c['new'] + text[pos + len(c['old']):]
    return text


def undo_exact(text, changes):
    for c in reversed(changes):
        pos = c['applied_offset']
        assert text[pos:pos + len(c['new'])] == c['new']
        text = text[:pos] + c['old'] + text[pos + len(c['new']):]
    return text


def preserve_sequences(before, after):
    for pattern in (MATH, COMMANDS, REFS):
        assert pattern.findall(before) == pattern.findall(after)


def operation_applied(receipt):
    assert receipt.get('mode') == 'applied' or receipt.get('applied') is True, 'A proposal cannot discharge an application gate.'


def full_block_ref(guard, name):
    value = guard[name]
    if isinstance(value, dict):
        return value
    return {'path': value, 'sha256': guard[name + '_sha256']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bindings', type=Path, required=True)
    args = parser.parse_args()
    bindings_raw = args.bindings.read_bytes()
    cfg = json.loads(bindings_raw)
    assert cfg['paper'] == 'I' and cfg['root_announced_final_source_and_ledger'] is True
    assert isinstance(cfg['root_announcement'], str) and cfg['root_announcement'].strip()
    workflow = document({'path': WORKFLOW, 'sha256': WORKFLOW_SHA})
    prior = document(workflow['prior_immutable_dossier'])
    for path, digest in workflow['protected_candidate19_records'].items():
        bound({'path': path, 'sha256': digest})
    source_bytes = (ROOT / 'S6_SERIES_PUBLISH_I.tex').read_bytes()
    ledger_bytes = (ROOT / 'CHECK_EVENTS.tsv').read_bytes()
    log_bytes = (ROOT / 'S6_SERIES_PUBLISH_defects_I.tsv').read_bytes()
    assert sha(source_bytes) == cfg['source_sha256']
    assert sha(ledger_bytes) == cfg['ledger_sha256']
    source = source_bytes.decode()
    log = list(csv.DictReader(io.StringIO(log_bytes.decode()), delimiter='\t'))
    old_count = prior['unique_edit_rows']
    assert core_hash(log[:old_count]) == prior['defect_log_content_sha256']
    # Reconstruct the immutable initial source and every prior continuation edit.
    base = ROOT.parent / 'S6_SERIES_PUBLISH_work/S6_SERIES_PUBLISH_checkpoint_10/S6_SERIES_PUBLISH_I.tex'
    baseline = base.read_text()
    assert sha(baseline.encode()) == prior['source_transport']['baseline_source_sha256']
    previous_chain = prior['source_transport']['applied_changes']
    source19 = apply_exact(baseline, previous_chain)
    assert sha(source19.encode()) == prior['source_sha256']
    body = document(cfg['body_application'])
    operation_applied(body)
    assert body['before_source_sha256'] == prior['source_sha256']
    changes = body['changes']
    assert {c['guard_id'] for c in changes} == set(workflow['expected_body_guard_ids'])
    assert len(changes) == len(workflow['expected_body_guard_ids'])
    assert body['existing_defect_rows'] == old_count
    assert body['total_defect_rows'] == old_count + len(changes)
    approved = {g['guard_id']: g for g in workflow['body_guards']}
    for c in changes:
        g = approved[c['guard_id']]
        assert [c[k] for k in ('old', 'new', 'type', 'statement_id')] == [g[k] for k in ('old', 'new', 'type', 'statement_id')]
        preserve_sequences(c['old'], c['new'])
    body_source = apply_exact(source19, changes)
    assert sha(body_source.encode()) == body['after_source_sha256']
    assert undo_exact(body_source, changes) == source19
    body_blocks = []
    block_by_guard = {}
    masked_before, masked_after = source19, body_source
    for index, archive in enumerate(body['archives']):
        before = bound({'path': archive['original'], 'sha256': archive['original_sha256']}).decode()
        after = bound({'path': archive['proposed'], 'sha256': archive['proposed_sha256']}).decode()
        bound({'path': archive['diff'], 'sha256': archive['diff_sha256']})
        proposed = before
        for c in changes:
            if c['guard_id'] in archive['guard_ids']:
                assert proposed.count(c['old']) == 1
                proposed = proposed.replace(c['old'], c['new'], 1)
        assert proposed == after
        preserve_sequences(before, after)
        assert source19.count(before) == body_source.count(after) == source.count(after) == 1
        marker = f'COMPARED_CANDIDATE20_BODY_{index}'
        masked_before = masked_before.replace(before, marker, 1)
        masked_after = masked_after.replace(after, marker, 1)
        verified = {**archive, 'current_source_complete_block_exact_match': True}
        body_blocks.append(verified)
        for gid in archive['guard_ids']:
            assert gid not in block_by_guard
            block_by_guard[gid] = verified
    assert masked_before == masked_after and set(block_by_guard) == set(approved)
    # The inspected verifier requires actual append/approval records and the exact ledger tail.
    bound(workflow['append_verifier'])
    append_receipt = document(cfg['append_receipt'])
    appended = verify_append(ROOT / cfg['append_receipt']['path'])
    assert appended['after_ledger_sha256'] == cfg['ledger_sha256']
    manifest = document(append_receipt['manifest'])
    assert manifest['new_independent_targeted_computation_credit'] == 0
    assert manifest['check_credit_from_metadata_bibliography_layout_page_images_or_automatic_comparisons_alone'] == 0
    assert len(manifest['events']) == appended['appended_events']
    assert {e['statement_id'] for e in manifest['events']} == set(appended['appended_statement_ids'])
    count_guard = document(cfg['count_guard'])
    assert count_guard['type'] == 'D15'
    count_apply = document(cfg['count_application'])
    operation_applied(count_apply)
    assert count_apply['before_source_sha256'] == body['after_source_sha256']
    assert count_apply['after_source_sha256'] == cfg['source_sha256']
    assert body_source.count(count_guard['old']) == 1
    pos = body_source.index(count_guard['old'])
    assert len(count_apply['changes']) == len(count_apply['new_defect_rows']) == 1
    recorded_change = count_apply['changes'][0]
    recorded_row = count_apply['new_defect_rows'][0]
    assert recorded_change['guard_id'] == count_guard['id']
    assert recorded_change['old'] == recorded_row['old_text'] == count_guard['old']
    assert recorded_change['new'] == recorded_row['new_text'] == count_guard['new']
    assert recorded_change['type'] == recorded_row['type'] == 'D15'
    assert recorded_change['applied_offset'] == pos
    assert recorded_change['change_id'] == recorded_row['change_id']
    assert recorded_change['statement_id'] == recorded_row['statement_id']
    assert recorded_row == log[old_count + len(changes)]
    # The count guard calls its context I:methodology; the actual approved log
    # names the same exact full methodology block as section 1.5. Preserve the
    # applied log identifier/reason and disclose that interface mapping.
    count_change = {**recorded_change, 'reason': recorded_row['reason'], 'receipt': cfg['count_application']['path'], 'guard_context_identifier': count_guard['statement_id'], 'applied_log_context_identifier': recorded_row['statement_id'], 'guard_reason_as_recorded': count_guard['reason']}
    count_interface = {'guard_context_identifier': count_guard['statement_id'], 'applied_log_context_identifier': recorded_row['statement_id'], 'same_complete_methodology_block_required': True, 'applied_reason_taken_verbatim_from_approved_receipt_log_row': True}
    assert apply_exact(body_source, [count_change]) == source
    assert undo_exact(source, [count_change]) == body_source
    preserve_sequences(count_change['old'], count_change['new'])
    old_method = bound(full_block_ref(count_guard, 'original_full_block')).decode()
    new_method = bound(full_block_ref(count_guard, 'proposed_full_block')).decode()
    assert old_method.count(count_guard['old']) == 1
    assert old_method.replace(count_guard['old'], count_guard['new'], 1) == new_method
    assert body_source.count(old_method) == source.count(new_method) == 1
    assert recorded_change['full_original_methodology'] == full_block_ref(count_guard, 'original_full_block')
    assert recorded_change['full_proposed_methodology'] == full_block_ref(count_guard, 'proposed_full_block')
    preserve_sequences(old_method, new_method)
    new_changes = [{**c, 'receipt': cfg['body_application']['path']} for c in changes] + [count_change]
    assert len(log) == old_count + len(new_changes)
    for row, change in zip(log[old_count:], new_changes):
        assert [row[k] for k in CORE] == [change[k] for k in ('change_id', 'type', 'statement_id', 'old', 'new', 'reason')]
    chain = previous_chain + new_changes
    assert apply_exact(baseline, chain) == source and undo_exact(source, chain) == baseline
    # Fresh final-source/final-ledger counts, with no future proposal totals credited.
    recount = document(cfg['fresh_recount'])
    assert recount['source_sha256'] == cfg['source_sha256'] and recount['ledger_sha256'] == cfg['ledger_sha256']
    assert recount['counts'] == manifest['counts_after'] == count_guard['counts_after']
    assert recount['merged_ledger_rows'] == appended['after_rows']
    bound(workflow['recount_implementation'])
    spec = importlib.util.spec_from_file_location('candidate20_readonly_recount', ROOT / workflow['recount_implementation']['path'])
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    fresh = module.recount(ROOT, ROOT.parent / 'S6_SERIES_PUBLISH_work')
    for key in ('counts', 'selected_event_ids', 'declared_evidence_groups'):
        assert fresh[key] == recount[key]
    old_counts = count_guard['counts_before']
    counts = recount['counts']
    used = 'used and rechecked in this run'
    assert counts[used] - old_counts[used] == appended['appended_events']
    for kind in module.KINDS:
        if kind != used:
            assert counts[kind] == old_counts[kind]
    assert str(old_counts[used]) in count_guard['old'] and str(counts[used]) in count_guard['new']
    ag = document(cfg['source_AG_binding'])
    assert ag['source_sha256'] == cfg['source_sha256'] and ag['ledger_sha256'] == cfg['ledger_sha256']
    assert ag['source_exact_forward_and_inverse_maps_verified'] and ag['all_label_and_tag_sequences_preserved']
    assert len(ag['exact_edits']) == len(chain)
    assert len(ag['headlines']) == 7 and sum(x['outline_items'] for x in ag['headlines'].values()) == 40 and len(ag['blocks']) == 80
    for c, a in zip(chain, ag['exact_edits']):
        assert (c['change_id'], c['old'], c['new']) == (a['change_id'], a['old'], a['new'])
    matrix = document(workflow['bibliography_matrix'])
    bib = bibliography(source)
    assert bibliography(source19) == bib and len(bib) == matrix['entry_count'] == 117
    for r in matrix['rows']:
        assert bib[r['key']] == r['proposed_entry'] and sha(bib[r['key']].encode()) == r['proposed_entry_sha256']
    retained = document(workflow['retained_C61_disposition'])
    retained_text = bound(retained['complete_context']).decode()
    assert source19.count(retained_text) == source.count(retained_text) == 1
    for item in workflow['complete_manual_proof_comparison_records']:
        bound(item)
    # Build and page reading are explicit gates, independent of the source disposition.
    build_gate = {'status': 'pending', 'evidence': None}
    reading_gate = {'status': 'pending', 'evidence': None}
    pdf_sha = None
    page_count = None
    if cfg.get('build'):
        build = document(cfg['build'])
        assert build['source_sha256'] == cfg['source_sha256']
        pdf_sha = build['pdf_sha256']
        pdf_path = ROOT / cfg.get('pdf_path', 'build/I_candidate20/S6_SERIES_PUBLISH_I.pdf')
        assert sha(pdf_path.read_bytes()) == pdf_sha
        for key in ('overfull_total', 'overfull_above_2pt', 'undefined_references', 'undefined_citations', 'missing_characters', 'missing_fonts', 'multiply_defined', 'duplicate_destinations'):
            assert build[key] == 0, key
        import fitz
        with fitz.open(pdf_path) as pdf:
            page_count = len(pdf)
        build_gate = {'status': 'complete', 'evidence': cfg['build'], 'page_count': page_count}
    if cfg.get('coverage'):
        assert pdf_sha
        coverage = document(cfg['coverage'])
        assert coverage['source_sha256'] == cfg['source_sha256'] and coverage['pdf_sha256'] == pdf_sha
        assert coverage['all_pages_read'] and coverage['page_count'] == page_count
        assert sorted(r['page'] for r in coverage['pages']) == list(range(1, page_count + 1))
        render_path = cfg.get('render_manifest_path', 'render/I_candidate20/manifest.json')
        render = document({'path': render_path, 'sha256': coverage['render_manifest_sha256']})
        assert render['pdf_sha256'] == pdf_sha
        rendered = {r['page']: r for r in render['rendered_pages']}
        for row in coverage['pages']:
            image_row = rendered[row['page']]
            assert image_row['image_sha256'] == row['image_sha256']
            bound({'path': image_row['image'], 'sha256': image_row['image_sha256']})
            record_raw = bound({'path': row['reading_record'], 'sha256': row['reading_record_sha256']})
            record = json.loads(record_raw)
            assert any(p['image_sha256'] == row['image_sha256'] for p in record['pages'])
        reading_gate = {'status': 'complete', 'evidence': cfg['coverage'], 'page_count': page_count}
    issues = cfg['new_content_issues']
    assert isinstance(issues, list)
    deps = []
    if build_gate['status'] != 'complete':
        deps.append('Bind the actual clean candidate20 build and exact final PDF.')
    if reading_gate['status'] != 'complete':
        deps.append('Actually read every changed complete candidate20 page image; carry prior reading only through exact whole-image hash equality.')
    deps += ['Bind the final42 source/PDF/ledger/report/deposit provenance claims.', 'Finalize the defect-page map and full mapped-log hash while preserving stable edit-content and type-association hashes.', 'Root must review individual dispositions before any canonical status update.']
    evidence_list = [evidence(workflow['prior_immutable_dossier'], 'Immutable candidate19 contextual dispositions.'), evidence(cfg['body_application'], 'Actual seven-body-guard application and exact full proof comparisons.'), evidence(cfg['append_receipt'], 'Actual authorized append-only rereading event bundle.'), evidence(cfg['count_guard'], 'Exact D15 methodology count substitution.'), evidence(cfg['count_application'], 'Actual numeric source/log update.'), evidence(cfg['fresh_recount'], 'Fresh final source and canonical ledger recount.'), evidence(cfg['source_AG_binding'], 'Exact final source and ledger A–G binding.')]
    type_rows = []
    associations = []
    for old in prior['rows']:
        typ = old['type_id']
        row = copy.deepcopy(old)
        selected = [r for r in log if typ in types_of(r['type'])]
        continuing = [c for c in chain if typ in types_of(c['type'])]
        current = [c for c in new_changes if typ in types_of(c['type'])]
        unresolved = [i for i in issues if typ in types_of(i['type_id'])]
        row['candidate19_source_review_as_recorded'] = old['source_review']
        row['candidate19_remaining_content_issues_as_recorded'] = old['remaining_content_issues']
        if typ == 'D08':
            review = 'All seven named candidate19 closing-recap findings are exactly resolved by the applied body batch. The complete original/proposed statement and proof comparisons retain every mathematical segment, command, reference, label and target. Their current complete blocks match the final source. The retained C.6.1 sentence has a separately read full-context disposition: it supplies the final inferential link from the finite-place premises to the stated A_t consequences. No keyword absence is used as a closure premise. Resolved guards: ' + ', '.join(c['guard_id'] for c in current) + '.'
        elif typ == 'D15':
            review = ('The actual authorized append of ' + str(appended['appended_events']) + ' distinct owning-statement rereading events is verified as the exact tail of the preserved ledger. Every appended event is used and rechecked in this run; no independent, targeted or computational event is created. The one D15 methodology substitution changes the recorded used-and-rechecked total from ' + str(old_counts[used]) + ' to ' + str(counts[used]) + ', matching the fresh final-source/final-ledger recount. The complete methodology pair differs by that exact numeric substitution. Existing date, model, effort-disclosure and records-link wording remain carried by the exact source map. Final42-claim source/PDF/report/deposit binding remains a separate gate.')
        else:
            review = old['source_review'] + ' This bounded source disposition is carried to candidate20 by the exact seven-body-edit and one numeric-count-edit forward/inverse maps. The recorded current batch contains no additional instance of this type; the actual clean-build, changed-image and final provenance gates remain separately recorded.'
        row.update(type_id=typ, status='open_confirmed_current_source_issue' if unresolved else 'source_clear_pending_final_bindings', source_clear_in_recorded_review_scope=not unresolved, source_review=review, proposed_disposition='Source disposition follows the named contextual reviews and exact applied resolutions; root review remains required.', remaining_content_issues=unresolved, remaining_dependencies=([i.get('remaining_dependency', 'Resolve the recorded confirmed current content issue.') for i in unresolved] + deps), exact_applied_guard_resolutions=current, applied_candidate19_guard_resolutions=current, current_edit_associations=len(selected), continuation_edit_associations=len(continuing), edit_ids=[r['change_id'] for r in selected], continuation_edit_ids=[c['change_id'] for c in continuing], edit_content_sha256=core_hash(selected), mathematical_events_added=0, new_page_credit=0)
        row['evidence'] += evidence_list
        for item in cfg.get('contextual_evidence', []):
            if typ in item['type_ids']:
                row['evidence'].append(evidence({'path': item['path'], 'sha256': item['sha256']}, item['scope']))
        row['source_absence_evidence'] = {'method': 'Exact resolution of the named confirmed instances and carried individual contextual dispositions; no keyword-absence inference.', 'named_current_guards_resolved': [c['guard_id'] for c in current], 'remaining_confirmed_instances': len(unresolved), 'final_build_gate': build_gate['status'], 'actual_image_gate': reading_gate['status']}
        type_rows.append(row)
        inherited_count = prior['unique_edit_rows'] - prior['continuation_unique_edit_rows']
        associations += [{'type_id': typ, 'change_id': r['change_id'], 'statement_id': r['statement_id'], 'origin': 'continuation' if int(r['change_id'].split('-')[1]) > inherited_count else 'inherited candidate13'} for r in selected]
    assert len(type_rows) == 25
    out = OUT / 'S6_SERIES_PUBLISH_I_candidate20_type_closure_preparation.json'
    assoc_path = OUT / 'S6_SERIES_PUBLISH_I_candidate20_type_associations.tsv'
    assert not out.exists() and not out.with_suffix('.md').exists() and not assoc_path.exists()
    stream = io.StringIO(newline='')
    writer = csv.DictWriter(stream, fieldnames=['type_id', 'change_id', 'statement_id', 'origin'], delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(associations)
    assoc_bytes = stream.getvalue().encode()
    result = {'schema': 'S6_SERIES_PUBLISH.I.type_closure_preparation.candidate20', 'paper': 'I', 'candidate': 20, 'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'source_sha256': cfg['source_sha256'], 'pdf_sha256': pdf_sha, 'page_count': page_count, 'defect_log_sha256': sha(log_bytes), 'defect_log_content_sha256': core_hash(log), 'check_ledger_sha256': cfg['ledger_sha256'], 'unique_edit_rows': len(log), 'continuation_unique_edit_rows': len(chain), 'latest_applied_guards': len(new_changes), 'latest_guard_type_associations': dict(collections.Counter(c['type'] for c in new_changes)), 'all_types_source_clear': not issues, 'source_clear_type_count': sum(r['source_clear_in_recorded_review_scope'] for r in type_rows), 'final_certified': False, 'canonical_status_modified': False, 'mathematical_events_added': 0, 'new_page_credit': 0, 'workflow': {'path': WORKFLOW, 'sha256': WORKFLOW_SHA}, 'final_execution_bindings': {'path': str(args.bindings.resolve().relative_to(ROOT)), 'sha256': sha(bindings_raw)}, 'prior_immutable_dossier': workflow['prior_immutable_dossier'], 'actual_body_application': cfg['body_application'], 'actual_count_application': cfg['count_application'], 'actual_append_verified': appended, 'actual_final_recount': cfg['fresh_recount'], 'final_counts': counts, 'current_AG_binding': cfg['source_AG_binding'], 'source_transport': {'baseline_source_sha256': sha(baseline.encode()), 'previous_source_sha256': prior['source_sha256'], 'current_source_sha256': cfg['source_sha256'], 'exact_forward_and_inverse_reconstruction': True, 'applied_changes': chain, 'latest_complete_blocks_verified': body_blocks, 'methodology_pair_verified': True}, 'bibliography_matrix': workflow['bibliography_matrix'], 'bibliography_complete_entries_verified': 117, 'candidate19_complete_actual_image_coverage': workflow['candidate19_complete_actual_image_coverage'], 'retained_C61_disposition': workflow['retained_C61_disposition'], 'complete_manual_proof_comparison_records': workflow['complete_manual_proof_comparison_records'], 'protected_candidate19_records': workflow['protected_candidate19_records'], 'clean_build_gate': build_gate, 'actual_image_gate': reading_gate, 'defect_type_associations': {'path': str(assoc_path.relative_to(ROOT)), 'sha256': sha(assoc_bytes), 'row_count': len(associations)}, 'rows': type_rows, 'remaining_dependencies': deps, 'limitations': ['All source dispositions have the explicitly recorded contextual scope; no universal correctness claim is inferred.', 'The separately authorized rereading append records exposed comparative review only; this dossier creates no mathematical event.', 'Clean compilation and source equality do not establish actual complete-page reading.']}
    result['count_receipt_interface'] = count_interface
    result['generator'] = {'path': str(Path(__file__).resolve().relative_to(ROOT)), 'sha256': sha(Path(__file__).read_bytes())}
    result['current_contextual_evidence'] = cfg.get('contextual_evidence', [])
    lines = ['# Paper I candidate20 type closure preparation', '', 'Source SHA-256: `' + cfg['source_sha256'] + '`', '', 'Ledger SHA-256: `' + cfg['ledger_sha256'] + '`', '', 'PDF SHA-256: `' + str(pdf_sha) + '`', '', 'Source-clear rows: ' + str(result['source_clear_type_count']) + '/25. Build gate: ' + build_gate['status'] + '. Actual-image gate: ' + reading_gate['status'] + '.', '']
    for row in type_rows:
        lines += ['## ' + row['type_id'] + ' — ' + row['status'], '', row['source_review'], '', 'Remaining dependencies:', ''] + ['- ' + x for x in row['remaining_dependencies']] + ['']
    assoc_path.write_bytes(assoc_bytes)
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
    out.with_suffix('.md').write_text('\n'.join(lines) + '\n')
    print(json.dumps({'dossier': str(out.relative_to(ROOT)), 'sha256': sha(out.read_bytes()), 'source_sha256': cfg['source_sha256'], 'ledger_sha256': cfg['ledger_sha256'], 'pdf_sha256': pdf_sha, 'log_rows': len(log), 'continuation_edits': len(chain), 'appended_reread_events_separately_verified': appended['appended_events'], 'all_types_source_clear': result['all_types_source_clear'], 'build_gate': build_gate['status'], 'image_gate': reading_gate['status'], 'mathematical_events_added_by_dossier': 0}, indent=2))


if __name__ == '__main__':
    main()
