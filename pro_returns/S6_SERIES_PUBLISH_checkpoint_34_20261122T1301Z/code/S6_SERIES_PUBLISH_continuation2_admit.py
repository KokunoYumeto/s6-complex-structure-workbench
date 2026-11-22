#!/usr/bin/env python3
"""Apply explicitly reviewed Paper II checks, retaining lean exact change records.

This program validates byte identities and appends supplied events. Mathematical
admission is the explicit review in the configuration, never a program inference.
"""
from pathlib import Path
import csv
import datetime as dt
import difflib
import hashlib
import io
import json
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parent
csv.field_size_limit(100_000_000)

def sha(b):
    return hashlib.sha256(b).hexdigest()

def data(path):
    p = ROOT / path
    if p.is_file():
        return p.read_bytes()
    # Lean checkpoint aliases are exact bytes, never a missing-check condition.
    with (BASE / 'CP21_INDEX.tsv').open(newline='') as f:
        row = next((r for r in csv.DictReader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
                    if r['path'] == path), None)
    assert row and row['state'] in ('copy', 'prefix'), path
    b = (BASE / 'S6_SERIES_PUBLISH_checkpoint_21' / row['source']).read_bytes()[:int(row['size'])]
    assert len(b) == int(row['size']) and sha(b) == row['sha256'], path
    return b

def bound(path):
    b = data(path)
    return dict(path=path, sha256=sha(b), bytes=len(b))

def read(path):
    return json.loads(data(path))

def check(binding):
    assert sha(data(binding['path'])) == binding['sha256'], binding['path']

def tsv(rows, fields, header=True):
    out = io.StringIO(newline='')
    writer = csv.DictWriter(out, fieldnames=fields, delimiter='\t', lineterminator='\n')
    if header:
        writer.writeheader()
    writer.writerows(rows)
    return out.getvalue().encode()

def parse(b):
    reader = csv.DictReader(io.StringIO(b.decode(), newline=''), delimiter='\t')
    return list(reader), reader.fieldnames

def main():
    config_path = sys.argv[1]
    cfg = read(config_path)
    assert cfg['root_review_complete'] is True
    for binding in cfg['review_evidence']:
        check(binding)
    batch = cfg['batch']
    output = ROOT / f'records/S6_SERIES_PUBLISH_II_clean_checks_{batch:02d}'
    assert not output.exists(), output
    source_path = ROOT / 'S6_SERIES_PUBLISH_II.tex'
    source_old = source_path.read_bytes()
    assert sha(source_old) == cfg['source_before_sha256']
    source = source_old.decode()
    ledger_path = ROOT / 'CHECK_EVENTS.tsv'
    ledger_old = ledger_path.read_bytes()
    assert sha(ledger_old) == cfg['ledger_before_sha256']
    ledger_rows, ledger_fields = parse(ledger_old)
    defect_path = ROOT / 'S6_SERIES_PUBLISH_defects_II.tsv'
    defects_old = defect_path.read_bytes()
    defects, defect_fields = parse(defects_old)
    completion_path = ROOT / 'records/S6_SERIES_PUBLISH_required_check_completion_manifest.json'
    completion_old = completion_path.read_bytes()
    completion = json.loads(completion_old)
    now = dt.datetime.now(dt.timezone.utc).isoformat()
    event_rows, defect_rows, checks = [], [], []
    for target in cfg['targets']:
        owner, tag = target['owner'], target['tag']
        assert owner not in completion['rows'], owner
        for name in ('original', 'proposed', 'freeze', 'release', 'events'):
            check(target[name])
        original = data(target['original']['path']).decode()
        proposed = data(target['proposed']['path']).decode()
        assert source.count(original) == 1, owner
        temp = original
        for n, g in enumerate(target['guards'], 1):
            assert temp.count(g['old']) == g.get('occurrences', 1), (owner, n)
            temp = temp.replace(g['old'], g['new'], g.get('occurrences', 1))
            defect_rows.append(dict(change_id=f'II-C2-{batch:02d}-{tag}-{n:03d}', type=g['type'],
                statement_id=owner, old_location=owner, old_page=target['old_page'],
                new_location=owner, new_page='pending integrated PDF', old_text=g['old'],
                new_text=g['new'], reason=g['reason'],
                review_status='Complete original/proposed proof read by root; exact guarded replay verified'))
        assert temp == proposed, owner
        source = source.replace(original, proposed, 1)
        freeze, release = read(target['freeze']['path']), read(target['release']['path'])
        assert dt.datetime.fromisoformat(freeze['created_utc']) < dt.datetime.fromisoformat(release['created_utc'])
        assert release['freeze_receipt_sha256'] == target['freeze']['sha256']
        assert freeze['statement_owner'] == release['statement_owner'] == owner
        for key, hashkey in [('frozen_derivation_path','derivation_sha256'), ('packet_path','packet_sha256'),
                             ('target_proof_path','target_proof_sha256')]:
            assert sha(data(freeze[key])) == freeze[hashkey], freeze[key]
        for key, hashkey in [('released_proof_path','released_proof_sha256'),
                             ('full_owning_block_path','full_owning_block_sha256')]:
            assert sha(data(release[key])) == release[hashkey], release[key]
        proposed_events = read(target['events']['path'])
        event_date = proposed_events.get('created_utc', proposed_events.get('proposed_utc', release['created_utc']))
        targeted = 0
        for n, e in enumerate(proposed_events['events'], 1):
            assert e.get('statement_owner', e.get('statement_id')) == owner
            kind = e.get('event_type', e.get('type'))
            assert kind in ('targeted proof check','used and rechecked in this run','computation or formal certificate')
            assert e.get('event_count', 1) == 1
            targeted += kind == 'targeted proof check'
            row = {k: e.get(k, '') for k in ledger_fields}
            row.update(statement_id=owner, date=e.get('date', event_date[:10]),
                who=e.get('who', target['who']), type=kind,
                outcome=e.get('scope', e.get('outcome', ''))+' '+target.get('event_note',''),
                event_id=e.get('event_id', f'S6_SERIES_PUBLISH_II_C2_{batch:02d}_{tag}_{n:02d}_20261122'),
                phase=e.get('phase','S6_SERIES_PUBLISH_II'),
                source_file=e.get('source_file',target['events']['path']),
                source_row=e.get('source_row',str(n+1)), source_event_type=kind,
                evidence_group=e.get('evidence_group',f'S6_SERIES_PUBLISH_II_C2_{batch:02d}_{tag}'),
                publish_input_file=f'S6_SERIES_PUBLISH_continuation2_{batch:02d}_CHECK_EVENTS.tsv',
                publish_input_row=str(len(event_rows)+2),
                date_utc=e.get('date_utc',event_date), where=e.get('where',target['events']['path']))
            assert row['outcome'].strip()
            event_rows.append(row)
        assert targeted == 1, owner
        checks.append(dict(owner=owner, tag=tag, freeze=target['freeze'], release=target['release'],
                           original=target['original'], proposed=target['proposed'], scope=target['scope']))
    for n, edit in enumerate(cfg.get('additional_source_edits', []),1):
        assert source.count(edit['old']) == 1
        source = source.replace(edit['old'],edit['new'],1)
        defect_rows.append(dict(change_id=f'II-C2-{batch:02d}-SUP-{n:03d}',type=edit['type'],
            statement_id=edit.get('owner','Programs'),old_location=edit.get('location','Programs'),
            old_page=edit.get('old_page',''),new_location=edit.get('location','Programs'),
            new_page='pending integrated PDF',old_text=edit['old'],new_text=edit['new'],
            reason=edit['reason'],review_status='Root reviewed exact supplementary edit'))
    for copy in cfg.get('code_copies', []):
        check(copy['from'])
        destination = ROOT / copy['to']
        payload = data(copy['from']['path'])
        assert not destination.exists() or destination.read_bytes() == payload
    all_event_ids = [r['event_id'] for r in ledger_rows+event_rows]
    assert len(all_event_ids) == len(set(all_event_ids))
    all_change_ids = [r['change_id'] for r in defects+defect_rows]
    assert len(all_change_ids) == len(set(all_change_ids))
    output.mkdir()
    source_new = source.encode()
    diff = ''.join(difflib.unified_diff(source_old.decode().splitlines(True), source.splitlines(True),
                                      fromfile='S6_SERIES_PUBLISH_II.tex.before',tofile='S6_SERIES_PUBLISH_II.tex.after'))
    (output/'S6_SERIES_PUBLISH_source.diff').write_text(diff)
    bundle = ROOT / f'records/S6_SERIES_PUBLISH_continuation2_{batch:02d}_CHECK_EVENTS.tsv'
    assert not bundle.exists()
    bundle.write_bytes(tsv(event_rows,ledger_fields))
    (output/'S6_SERIES_PUBLISH_defect_rows.tsv').write_bytes(tsv(defect_rows,defect_fields))
    ledger_new = ledger_old + tsv(event_rows,ledger_fields,False)
    defects_new = defects_old + tsv(defect_rows,defect_fields,False)
    assert ledger_old.endswith(b'\n') and defects_old.endswith(b'\n')
    manifest = dict(schema=2, created_utc=now, approved_by_explicit_root_review=True, paper='II',
        config=bound(config_path), review_evidence=cfg['review_evidence'],
        source_before_sha256=sha(source_old),source_after_sha256=sha(source_new),
        source_diff=bound(str((output/'S6_SERIES_PUBLISH_source.diff').relative_to(ROOT))),
        ledger_before_bytes=len(ledger_old),ledger_before_sha256=sha(ledger_old),
        ledger_after_sha256=sha(ledger_new),ledger_before_rows=len(ledger_rows),
        ledger_after_rows=len(ledger_rows)+len(event_rows),appended_events=bound(str(bundle.relative_to(ROOT))),
        defect_before_bytes=len(defects_old),defect_before_sha256=sha(defects_old),
        defect_after_sha256=sha(defects_new),appended_defect_rows=len(defect_rows),
        independent_required_checks_completed=len(checks),completed_owners=[c['owner'] for c in checks],
        checks=checks,mathematical_repairs=cfg.get('mathematical_repairs',[]),
        visual_reading_credit=0,previous_full_files_kept_in_memory_only=True,
        inherited_event_dates_preserved=True,scope=cfg['scope'])
    manifest_path = output/'manifest.json'
    manifest_path.write_text(json.dumps(manifest,indent=2)+'\n')
    completed_rows = {}
    for c in checks:
        completed_rows[c['owner']] = dict(paper='II',status='done',recorded_utc=now,
            evidence_path=str(manifest_path.relative_to(ROOT)),evidence_sha256=sha(manifest_path.read_bytes()),
            scope=c['scope'],completion_kind='independent proof check')
    completion['rows'].update(completed_rows)
    completion['updated_utc']=now
    completion_new=(json.dumps(completion,indent=2)+'\n').encode()
    (output/'S6_SERIES_PUBLISH_completion_append.json').write_text(json.dumps(dict(
        before_sha256=sha(completion_old),after_sha256=sha(completion_new),rows=completed_rows),indent=2)+'\n')
    # All validation has completed; commit the specified local reversible writes.
    source_path.write_bytes(source_new)
    with ledger_path.open('ab') as f:
        f.write(ledger_new[len(ledger_old):])
    with defect_path.open('ab') as f:
        f.write(defects_new[len(defects_old):])
    completion_path.write_bytes(completion_new)
    for copy in cfg.get('code_copies', []):
        (ROOT/copy['to']).write_bytes(data(copy['from']['path']))
    actual = ledger_path.read_bytes()
    assert actual[:len(ledger_old)] == ledger_old and actual == ledger_new
    actual_rows,_=parse(actual)
    assert actual_rows[:len(ledger_rows)] == ledger_rows and actual_rows[len(ledger_rows):] == event_rows
    assert source_path.read_bytes() == source_new and defect_path.read_bytes() == defects_new
    (output/'append_verification.json').write_text(json.dumps(dict(created_utc=now,
        before_rows=len(ledger_rows),after_rows=len(actual_rows),added_rows=len(event_rows),
        before_ledger_sha256=sha(ledger_old),after_ledger_sha256=sha(actual),
        whole_old_ledger_byte_prefix_preserved=True,old_rows_unchanged=True,new_tail_exactly_bundle=True,
        all_event_ids_unique=True),indent=2)+'\n')
    resolved=sum(c['paper']=='II' for c in completion['rows'].values())
    retired=sum(c['paper']=='II' and c.get('completion_kind')=='retired nonmathematical production remark'
                for c in completion['rows'].values())
    text=f'''\n\n## Paper II fresh checks batch {batch:02d} — {now}\n\n{cfg['scope']}\n\nPaper II has {resolved} of 197 required rows resolved: {resolved-retired} independent checks and {retired} recorded production-only retirement; {197-resolved} remain. The current source SHA-256 is `{sha(source_new)}`. The defect log has {len(defects)+len(defect_rows):,} rows. CHECK_EVENTS.tsv has {len(actual_rows):,} rows, SHA-256 `{sha(actual)}`. The exact source diff, appended event rows, appended defect rows and completion entries are in `{output.relative_to(ROOT)}`. The full prior event-ledger byte prefix and every prior row were verified unchanged. Prepared check events retain their original dates and checker identities; this continuation's comparative review creates no additional independent-check count. No page-image reading credit is assigned.\n'''
    journal=[]
    for name in ('PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md'):
        p=ROOT/name;b=p.read_bytes()
        assert f'## Paper II fresh checks batch {batch:02d} —'.encode() not in b
        with p.open('a') as f:f.write(text)
        journal.append(dict(path=name,before_sha256=sha(b),after_sha256=sha(p.read_bytes()),appended_text=text))
    (output/'S6_SERIES_PUBLISH_journal_append.json').write_text(json.dumps(journal,indent=2)+'\n')
    print(json.dumps(dict(batch=batch,required_resolved=resolved,required_open=197-resolved,
        events_added=len(event_rows),defects_added=len(defect_rows),source_sha256=sha(source_new),
        ledger_sha256=sha(actual),manifest=bound(str(manifest_path.relative_to(ROOT)))),indent=2))

if __name__=='__main__':
    main()
