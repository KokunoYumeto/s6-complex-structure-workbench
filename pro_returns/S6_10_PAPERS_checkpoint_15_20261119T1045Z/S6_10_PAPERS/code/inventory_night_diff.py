#!/usr/bin/env python3
"""Compare exact night rows and proof blocks without awarding proof checks."""
from __future__ import annotations
import argparse
import collections
import csv
import hashlib
import json
import re
from pathlib import Path

from inventory_reconcile import TexIndex

OUT = Path(__file__).resolve().parents[1]
ROOT = OUT.parents[1]


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def included_proof_files(directory, path, exact):
    """Hash the main file and every literal included companion, without execution."""
    directory = directory.resolve()
    found = {str(path.resolve().relative_to(directory)): path.resolve()}
    waiting = [(path.resolve(), exact)]
    missing = []
    while waiting:
        parent, text = waiting.pop()
        for name in re.findall(r'\\input\{([^{}]+)\}', text):
            name = name if name.endswith('.tex') else name + '.tex'
            candidates = [directory/name, parent.parent/name]
            target = next((p.resolve() for p in candidates if p.is_file()), None)
            if target is None or not target.is_relative_to(directory):
                missing.append({'parent': str(parent.relative_to(directory)), 'input': name})
                continue
            rel = str(target.relative_to(directory))
            if rel not in found:
                found[rel] = target
                waiting.append((target, target.read_text()))
    files = [{'file': rel, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
             for rel, p in sorted(found.items())]
    return files, missing


def snapshot(directory, checkpoint):
    rows = {r['id']: r for r in csv.DictReader((directory/'S6_06_BLIND_results.csv').open())}
    blocks = {}
    for path in sorted((directory/'notes').glob('*.tex')):
        text = path.read_text()
        markers = list(re.finditer(r'\\begin\{statement\}\{(P[^}]+)\}\{([^}]+)\}', text))
        if not markers:
            continue
        index = TexIndex(path.resolve())
        by_start = {b['start']: b for b in index.blocks}
        for m in markers:
            block = by_start.get(m.start())
            if block is None:
                continue
            sid = m.group(1)
            exact = text[block['start']:block['end']]
            included, missing = included_proof_files(directory, path, exact)
            blocks[sid] = {
                'file': str(path.resolve().relative_to(ROOT)),
                'start': block['start'], 'end': block['end'],
                'line': text[:m.start()].count('\n')+1,
                'sha256': digest(exact), 'source_status': m.group(2),
                'proof_input_files': included,
                'included_proof_manifest_sha256': hashlib.sha256(
                    json.dumps(included, sort_keys=True, separators=(',', ':')).encode()).hexdigest(),
                'unresolved_literal_inputs': missing,
            }
    return {
        'checkpoint': str(checkpoint), 'directory': str(directory),
        'rows': rows, 'blocks': blocks,
        'row_count': len(rows),
        'source_statuses': dict(collections.Counter(r['status'] for r in rows.values())),
        'missing_proof_blocks': sorted(set(rows)-set(blocks)),
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--old-dir', type=Path, required=True)
    p.add_argument('--new-dir', type=Path, required=True)
    p.add_argument('--old-checkpoint', required=True)
    p.add_argument('--new-checkpoint', required=True)
    p.add_argument('--comparison-only', action='store_true',
                   help='Write comparison artifacts without changing the live intake registry.')
    args = p.parse_args()
    old = snapshot(args.old_dir, args.old_checkpoint)
    new = snapshot(args.new_dir, args.new_checkpoint)
    # A formerly supplemental named proof can become registered in the CSV.
    # Its existing mathematical text must be compared, not treated as unseen.
    common = (set(old['rows']) | set(old['blocks'])) & set(new['rows'])
    changed = []
    for sid in sorted(common):
        old_row = old['rows'].get(sid)
        fields = ([k for k in sorted(set(old_row) | set(new['rows'][sid]))
                   if old_row.get(k) != new['rows'][sid].get(k)]
                  if old_row is not None else ['registered_in_central_csv'])
        old_block, new_block = old['blocks'].get(sid), new['blocks'].get(sid)
        proof_changed = (old_block or {}).get('sha256') != (new_block or {}).get('sha256')
        main_rel = str(Path(new_block['file']).relative_to(args.new_dir.resolve().relative_to(ROOT))) if new_block else None
        old_inputs = {x['file']: x['sha256'] for x in (old_block or {}).get('proof_input_files', [])}
        new_inputs = {x['file']: x['sha256'] for x in (new_block or {}).get('proof_input_files', [])}
        support_changes = [name for name in sorted(set(old_inputs) | set(new_inputs))
                           if name != main_rel and old_inputs.get(name) != new_inputs.get(name)]
        if fields or proof_changed or support_changes:
            dependency_only = fields == ['depends_on'] and not proof_changed and not support_changes
            changed.append({
                'id': sid, 'label': 'night:'+sid,
                'changed_csv_fields': fields, 'proof_block_changed': proof_changed,
                'old_status': old_row['status'] if old_row is not None else old_block['source_status'],
                'new_status': new['rows'][sid]['status'],
                'old_row': old_row, 'new_row': new['rows'][sid],
                'old_proof_block': old_block, 'new_proof_block': new_block,
                'included_proof_files_changed': support_changes,
                'source_was_previously_unregistered': old_row is None,
                'current_proof_recheck_required': proof_changed or bool(support_changes) or bool(set(fields) & {'statement','status'}),
                'dependency_metadata_audit_required': 'depends_on' in fields,
                'dependency_only_change': dependency_only,
            })
    report = {
        'old_checkpoint': str(args.old_checkpoint), 'new_checkpoint': str(args.new_checkpoint),
        'old_count': old['row_count'], 'new_count': new['row_count'],
        'old_statuses': old['source_statuses'], 'new_statuses': new['source_statuses'],
        'added': sorted(set(new['rows'])-set(old['rows'])),
        'removed': sorted(set(old['rows'])-set(new['rows'])),
        'changed': changed,
        'rule': 'Exact source comparison only. Changed source proof blocks require renewed scoped review; no inherited current proof check is awarded to the changed text.',
    }
    stem = f'inventory_night_cp{args.old_checkpoint}_to_cp{args.new_checkpoint}'
    (OUT/f'analysis/{stem}.json').write_text(json.dumps(report, indent=2))
    intake = {
        'old_checkpoint': str(args.old_checkpoint), 'new_checkpoint': str(args.new_checkpoint),
        'diff_record': f'analysis/{stem}.json',
        'added': report['added'], 'removed': report['removed'],
        'changed': {x['label']: x for x in changed},
        'new_blocks': new['blocks'],
        'rule': 'Exact-text identity preserves the scope of an earlier recorded check. A changed proof or statement requires renewed review; changed dependency metadata has a separate Uses audit gate. No source copy creates a check.'
    }
    # Carry older unfinished gates forward. Moving to a new checkpoint must
    # not silently erase a Uses audit or a changed-proof review obligation.
    history = collections.defaultdict(list)
    additions = {}
    transitions = []
    for path in (OUT/'analysis').glob('inventory_night_cp*_to_cp*.json'):
        match = re.fullmatch(r'inventory_night_cp(\d+)_to_cp(\d+)\.json', path.name)
        if match and int(match.group(2)) <= int(args.new_checkpoint):
            transitions.append((int(match.group(2)), path))
    for checkpoint, path in sorted(transitions):
        previous = json.loads(path.read_text())
        for item in previous.get('changed', []):
            item = dict(item, change_checkpoint=str(checkpoint),
                        change_record=str(path.relative_to(OUT)))
            history[item['label']].append(item)
        for sid in previous.get('added', []):
            additions.setdefault(sid, str(checkpoint))
    intake['change_history'] = dict(history)
    intake['added_history'] = additions
    if not args.comparison_only:
        (OUT/'analysis/inventory_night_intake.json').write_text(json.dumps(intake, indent=2))
    for value in [old, new]:
        (OUT/f"analysis/inventory_night_cp{value['checkpoint']}_snapshot.json").write_text(json.dumps(value, indent=2))
    lines = [f"# Night checkpoint {args.old_checkpoint} → {args.new_checkpoint}", '', report['rule'], '',
             f"Rows: {old['row_count']} → {new['row_count']}. Added: {len(report['added'])}; removed: {len(report['removed'])}; changed existing: {len(changed)}.", '',
             '| Label | Old status | New status | CSV fields | Proof block changed | Recheck gate |',
             '|---|---|---|---|---|---|']
    for item in changed:
        lines.append('| '+ ' | '.join([item['label'], item['old_status'], item['new_status'], ', '.join(item['changed_csv_fields']), str(item['proof_block_changed']), str(item['current_proof_recheck_required'])])+' |')
    lines += ['', 'Added IDs: '+', '.join(report['added'])+'.', '']
    (OUT/f'analysis/{stem}.md').write_text('\n'.join(lines))
    print(json.dumps({k:v for k,v in report.items() if k!='changed'}, indent=2))
    print('Changed existing IDs:', ', '.join(x['id'] for x in changed))


if __name__ == '__main__':
    main()
