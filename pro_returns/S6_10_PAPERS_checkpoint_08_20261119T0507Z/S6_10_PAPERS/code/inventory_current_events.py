#!/usr/bin/env python3
"""Attach explicit current-writing events to every matching source row.

Extraction, compilation, an old status and a computational pass do not create
a proof verdict.  Every event retains its writer's exact scope and provenance.
"""
from __future__ import annotations
import collections
import csv
import hashlib
import json
import re
from pathlib import Path

OUT = Path(__file__).resolve().parents[1]


def exact_sidecar_metadata(path, rows):
    """Recover fields omitted by an owner's fixed-column TSV export.

    A JSON sidecar contributes only to the very same recorded event: every
    populated TSV field must agree, including the labels, date, scope and
    derivation.  This transports source hashes/checkpoint numbers; it creates
    no event and broadens no reading scope.
    """
    sidecar = path.with_suffix('.json')
    if not sidecar.exists():
        return rows
    payload = json.loads(sidecar.read_text())
    if isinstance(payload, dict):
        payload = payload.get('events', payload.get('reviews', []))
    if not isinstance(payload, list):
        return rows
    candidates = collections.defaultdict(list)
    for item in payload:
        if isinstance(item, dict) and item.get('event_id'):
            candidates[str(item['event_id'])].append(item)
    enriched = []
    for row in rows:
        matching = []
        for item in candidates.get(row.get('event_id', ''), []):
            agrees = True
            for key, value in row.items():
                if value in ('', None):
                    continue
                if key not in item:
                    agrees = False
                    break
                other = item[key]
                if isinstance(other, (dict, list)):
                    try:
                        agrees = json.loads(value) == other
                    except (ValueError, TypeError):
                        agrees = False
                else:
                    agrees = str(other) == value
                if not agrees:
                    break
            if agrees:
                matching.append(item)
        if len(matching) == 1:
            merged = dict(matching[0])
            merged.update(row)
            merged['exact_metadata_sidecar'] = str(sidecar.relative_to(OUT))
            merged['metadata_transport_adds_no_check'] = True
            enriched.append(merged)
        else:
            enriched.append(row)
    return enriched


def events():
    paths = sorted(OUT.glob('records/*events.tsv'))
    paths += sorted(OUT.glob('analysis/*/current_check_events.tsv'))
    for path in paths:
        rows = exact_sidecar_metadata(path, list(csv.DictReader(path.open(), delimiter='\t')))
        for number, row in enumerate(rows, 2):
            ids = row.get('labels') or row.get('label') or row.get('statement_id') or ''
            # Some owners serialize the actual label list as a JSON array in
            # one TSV field. Parse that representation before delimiter text;
            # otherwise brackets/quotes silently prevent exact-label matches.
            if ids.lstrip().startswith('['):
                labels = json.loads(ids)
                if not isinstance(labels, list) or not all(isinstance(x, str) for x in labels):
                    raise ValueError(f'Invalid label array in {path}:{number}')
            else:
                labels = re.split(r'\s*[;,]\s*', ids)
            for label in labels:
                label = label.strip()
                if not label:
                    continue
                label = label.replace('s6:night:', 'night:')
                event = {
                    'label': label,
                    'who': row.get('who') or row.get('checker') or '',
                    'date': row.get('date') or row.get('recorded_at') or '',
                    'type': row.get('type', ''),
                    'verdict': row.get('verdict', ''),
                    'scope': row.get('scope') or row.get('outcome') or '',
                    'derivation': row.get('derivation', ''),
                    'independence': row.get('independence', ''),
                    'source': str(path.relative_to(OUT)),
                    'source_row': number,
                    'raw_event': row,
                }
                event['event_digest'] = hashlib.sha256(json.dumps(event, sort_keys=True).encode()).hexdigest()
                yield event


def current_status(records):
    explicit = []
    scoped = []
    computation = []
    for event in records:
        v = event['verdict'].strip().lower()
        typ = event['type'].lower()
        if v in {'proved', 'proved as stated'}:
            explicit.append(('proved; current-writing derivation recorded', event))
        elif v == 'open':
            explicit.append(('open; current scope recorded', event))
        elif v.startswith(('false as stated', 'refuted')):
            explicit.append((event['verdict'] + '; current-writing correction recorded', event))
        elif v in {'pass', 'passed'} or 'computation' in typ or 'certificate' in typ:
            computation.append(event)
        else:
            scoped.append(event)
    # An explicit proof verdict is still scoped by its retained event; it
    # certifies neither full-series readiness nor an independent blind check.
    if explicit:
        return explicit[-1][0]
    if scoped:
        v = scoped[-1]['verdict']
        return 'current scoped check recorded; ' + (v if v else 'see exact proof scope and remaining citation gates')
    if computation:
        return 'current computational check recorded; mathematical proof review pending'
    return None


def closes_changed_argument(event, change, current_checkpoint):
    """A source/execution/Uses-only event cannot close a revised proof gate."""
    raw = event['raw_event']
    typ = event['type'].lower()
    verdict = event['verdict'].strip().lower()
    if any(word in typ for word in ('computation', 'certificate', 'execution', 'dependency', 'uses-only', 'provenance')):
        return False
    if any(word in typ for word in ('bounded local', 'local-use', 'local use')):
        return False
    mathematical = (verdict in {'proved', 'proved as stated', 'open'} or
                    verdict.startswith('open; complete receiving deduction') or
                    verdict.startswith(('false as stated', 'refuted')) or
                    any(word in typ for word in ('full proof', 'full source-proof', 'whole proof', 'whole-proof',
                                                 'mathematical rederivation', 'argument review')))
    if not mathematical:
        return False
    checkpoint = str(change.get('change_checkpoint', current_checkpoint))
    if str(raw.get('source_checkpoint', '')) == checkpoint:
        return True
    new = change.get('new_proof_block') or {}
    # An unchanged main file can include changed mathematical companions.
    # Only an exact complete input manifest may close that gate by identity.
    if change.get('included_proof_files_changed'):
        manifest = new.get('included_proof_manifest_sha256')
        return bool(manifest and raw.get('included_proof_manifest_sha256') == manifest)
    block_digest = new.get('sha256')
    return bool(block_digest and raw.get('source_proof_sha256') == block_digest)


def merge_rows(rows):
    by_label = collections.defaultdict(list)
    for event in events():
        by_label[event['label']].append(event)
    # Editorial corrections are not proof-check events.  Preserve their exact
    # reasons even when a particular corrected block has no current review.
    corrections = collections.defaultdict(list)
    correction_sources = collections.defaultdict(list)
    for correction_path in [OUT/'analysis/IV/reconciliation.json', OUT/'analysis/III_receiving_corrections.json']:
        if correction_path.exists():
            for item in json.loads(correction_path.read_text()):
                corrections[item['label']].append(item['reason'])
                correction_sources[item['label']].append(str(correction_path.relative_to(OUT)))
    known = {r['label'] for r in rows}
    intake_path = OUT/'analysis/inventory_night_intake.json'
    intake = json.loads(intake_path.read_text()) if intake_path.exists() else {}
    dependency_review_path = OUT/'analysis/inventory_night_dependency_reviews.json'
    dependency_reviews = json.loads(dependency_review_path.read_text()) if dependency_review_path.exists() else {}
    review_history_path = OUT/'analysis/inventory_night_dependency_review_history.json'
    review_history = json.loads(review_history_path.read_text()) if review_history_path.exists() else {}
    for label, review in dependency_reviews.items():
        key = label + '@cp' + str(review.get('checkpoint', ''))
        review_history[key] = review
    review_history_path.write_text(json.dumps(review_history, indent=2))
    matched = 0
    for row in rows:
        try:
            notes = json.loads(row['notes'])
        except (ValueError, TypeError):
            notes = {'source_notes': row['notes']}
        if not isinstance(notes, dict):
            notes = {'source_notes': notes}
        change = None
        if (row['source_run'] == 'S6_06_BLIND' and
                str(notes.get('night_checkpoint')) == str(intake.get('new_checkpoint'))):
            block = intake.get('new_blocks', {}).get(row['source_id'], {})
            notes['current_source_proof_block'] = block
            notes['night_intake_record'] = 'analysis/inventory_night_intake.json'
            history = intake.get('change_history', {}).get(row['label'], [])
            if not history and row['label'] in intake.get('changed', {}):
                history = [dict(intake['changed'][row['label']], change_checkpoint=str(intake['new_checkpoint']))]
            change = next((x for x in reversed(history) if x['current_proof_recheck_required']), None)
            latest_change = history[-1] if history else None
            notes['checkpoint_change_history'] = history
            dependency_gates = []
            for prior in history:
                if prior.get('dependency_metadata_audit_required'):
                    checkpoint = str(prior.get('change_checkpoint', intake['new_checkpoint']))
                    review = review_history.get(row['label'] + '@cp' + checkpoint, {})
                    dependency_gates.append({'checkpoint': checkpoint,
                                             'pending': review.get('state') != 'checked',
                                             'review': review,
                                             'source_diff': prior.get('change_record', intake.get('diff_record'))})
            notes['dependency_metadata_gates'] = dependency_gates
            notes['current_dependency_metadata_audit_pending'] = any(g['pending'] for g in dependency_gates)
            notes['current_dependency_metadata_audits'] = [g['review'] for g in dependency_gates if not g['pending']]
            if latest_change:
                notes['previous_checkpoint_row'] = latest_change['old_row']
                notes['previous_checkpoint_proof_block'] = latest_change['old_proof_block']
                notes['current_source_change_fields'] = latest_change['changed_csv_fields']
            notes['proof_text_byte_identical_to_previous_checkpoint'] = not intake.get('changed', {}).get(row['label'], {}).get('proof_block_changed', False)
            notes['included_proof_files_changed'] = intake.get('changed', {}).get(row['label'], {}).get('included_proof_files_changed', [])
            if change:
                notes['changed_proof_review_pending'] = change['current_proof_recheck_required']
                notes['changed_proof_checkpoint'] = str(change.get('change_checkpoint', intake['new_checkpoint']))
            elif row['source_id'] in intake.get('added_history', {x: intake['new_checkpoint'] for x in intake.get('added', [])}):
                notes['new_checkpoint_proof_review_pending'] = True
                notes['first_checkpoint_appearance'] = intake.get('added_history', {}).get(row['source_id'], intake['new_checkpoint'])
            row['notes'] = json.dumps(notes, ensure_ascii=False)
        if row['label'] in corrections:
            try:
                notes = json.loads(row['notes'])
            except (ValueError, TypeError):
                notes = {'source_notes': row['notes']}
            if not isinstance(notes, dict):
                notes = {'source_notes': notes}
            notes['current_editorial_corrections'] = corrections[row['label']]
            notes['editorial_correction_sources'] = sorted(set(correction_sources[row['label']]))
            notes['editorial_correction_source'] = '; '.join(notes['editorial_correction_sources'])
            notes['editorial_correction_is_not_a_proof_check'] = True
            if str(notes.get('source_status', '')).lower() == 'refuted':
                notes['current_disposition'] = 'corrected local construction retained; rejected global/sign assertion archived'
                notes['original_block_archive'] = 'analysis/IV/rejected_blocks/'
            row['notes'] = json.dumps(notes, ensure_ascii=False)
        records = by_label.get(row['label'], [])
        if not records:
            if notes.get('changed_proof_review_pending'):
                row['status'] += '; changed source block requires renewed current review'
            if notes.get('current_dependency_metadata_audit_pending'):
                row['status'] += '; added-Uses audit pending (see checkpoint gates)'
            continue
        matched += 1
        try:
            old = json.loads(row['check_record'])
        except (ValueError, TypeError):
            old = {'historical_source_record': row['check_record']}
        if not isinstance(old, dict):
            old = {'historical_source_record': old}
        old.pop('current_writing_events', None)
        old['current_writing_events'] = records
        old['current_writing_event_rule'] = 'Exact event scope retained; copying or compilation adds no check.'
        row['check_record'] = json.dumps(old, ensure_ascii=False)
        try:
            notes = json.loads(row['notes'])
        except (ValueError, TypeError):
            notes = {'source_notes': row['notes']}
        if not isinstance(notes, dict):
            notes = {'source_notes': notes}
        notes.setdefault('pre_current_event_status', row['status'])
        notes['current_event_sources'] = sorted({e['source'] for e in records})
        row['status'] = current_status(records) or row['status']
        if notes.get('new_checkpoint_proof_review_pending'):
            full_new = [e for e in records if e['verdict'].strip().lower() in {'proved', 'proved as stated'}]
            notes['new_checkpoint_proof_review_pending'] = not bool(full_new)
            if full_new:
                notes['new_checkpoint_proof_review_event_digests'] = [e['event_digest'] for e in full_new]
                notes['new_checkpoint_review_scope_rule'] = 'The first source appearance of this label is the current checkpoint; only its explicit full current proof event closes this intake gate.'
        if change and change['current_proof_recheck_required']:
            renewed = [e for e in records if closes_changed_argument(e, change, intake['new_checkpoint'])]
            notes['changed_proof_review_pending'] = not bool(renewed)
            row['status'] = current_status(renewed) or 'changed source proof requires renewed current review; earlier scoped events retained as history'
        if notes.get('current_dependency_metadata_audit_pending'):
            pending_checkpoints = sorted({g['checkpoint'] for g in notes.get('dependency_metadata_gates', []) if g['pending']})
            row['status'] += '; checkpoint ' + ','.join(pending_checkpoints) + ' added-Uses audit pending'
        if str(notes.get('source_status', '')).lower() == 'refuted':
            row['status'] = 'refuted compound source claim; current correction or retained-subclaim checks recorded with their exact scope'
            notes['current_event_scope_does_not_reinstate_refuted_source'] = True
        prior_status = str(notes.get('pre_current_event_status', '')).strip().lower()
        source_open = str(notes.get('source_status', '')).strip().lower() == 'open'
        explicit_resolution = any(e['verdict'].strip().lower() in {'proved', 'proved as stated'} or
                                  e['verdict'].strip().lower().startswith(('refuted', 'false as stated'))
                                  for e in records)
        if (prior_status.startswith('open') or source_open or notes.get('receiving_open_problem')) and not explicit_resolution:
            row['status'] = 'open; current scoped reviews of proved identities or supporting arguments retained; unresolved conclusion remains open'
            notes['current_scoped_event_does_not_resolve_open_conclusion'] = True
        # The extraction-time pending note is historical once explicit events
        # have arrived. Keep it without contradicting the current scoped state.
        if 'current_writing' in old:
            old.setdefault('initial_extraction_check_state', old['current_writing'])
        old['current_writing'] = row['status']
        old['current_writing_readiness_scope'] = 'The attached events and their remaining source/dependency gates determine the exact scope; this is not whole-series publication readiness.'
        row['check_record'] = json.dumps(old, ensure_ascii=False)
        row['notes'] = json.dumps(notes, ensure_ascii=False)
    result = {
        'current_event_labels': len(by_label),
        'source_rows_with_current_events': matched,
        'labels_with_editorial_correction_records': len(corrections),
        'unmatched_event_labels': sorted(set(by_label) - known),
        'status_counts': dict(collections.Counter(r['status'] for r in rows)),
        'rule': 'Only an explicit current proved verdict yields a proved status. Every exact event scope remains in check_record. This is not a publication-readiness determination.',
    }
    (OUT/'analysis/inventory_current_events_by_label.json').write_text(json.dumps(by_label, indent=2, ensure_ascii=False))
    (OUT/'analysis/inventory_current_event_merge.json').write_text(json.dumps(result, indent=2, ensure_ascii=False))
    return result


def main():
    path = OUT/'S6_10_PAPERS_inventory.csv'
    with path.open() as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        rows = list(reader)
    result = merge_rows(rows)
    temporary = path.with_suffix('.csv.tmp')
    with temporary.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    temporary.replace(path)
    print(json.dumps({k:v for k,v in result.items() if k!='status_counts'}, indent=2))


if __name__ == '__main__':
    main()
