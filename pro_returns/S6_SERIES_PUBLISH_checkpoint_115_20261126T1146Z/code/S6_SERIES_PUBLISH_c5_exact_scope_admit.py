"""Admit root-reviewed checks whose actual argument scopes were separated.

The old structural grouping stays unchanged. Each admission validates the
individually released argument, its fresh chronology and its exact guard.
This does not apply a manuscript edit or refresh any derived inventory.
"""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import argparse
import csv
import io
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SCOPES = {
    '037X': (23788, 24094, False),
    '037Y': (24117, 24131, True),
    '0382': (24097, 24110, True),
    '02KA': (8217, 8268, False),
    '037N': (25752, 25754, False),
    '03DH': (28552, 28562, False),
    '036V': (26612, 26659, False),
    '036Z': (26662, 26674, False),
    '037K': (26681, 26703, False),
}
SOURCE_SHA = '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
csv.field_size_limit(100000000)


def read(path):
    with path.open(newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        return reader.fieldnames, list(reader)


def digest(value):
    return sha256(value).hexdigest()


def moment(value):
    result = datetime.fromisoformat(value.replace('Z', '+00:00'))
    assert result.tzinfo is not None
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tag', choices=SCOPES, required=True)
    parser.add_argument('--root-reviewed-comparison-sha', required=True)
    parser.add_argument('--root-reviewed-replacement-sha', required=True)
    args = parser.parse_args()
    progress = ROOT / 'S6_SERIES_PUBLISH_required_progress_III.tsv'
    original_progress = progress.read_bytes()
    fields, rows = read(progress)
    row = next(r for r in rows if r['tag'] == args.tag)
    other_rows = [dict(r) for r in rows if r['tag'] != args.tag]
    assert row['status'] == 'open'
    assert row['source_ownership_status'] == 'verified_exact_individual_scope' or (
        args.tag == '037N' and row['source_ownership_status'] == 'verified')
    assert row['root_release_authorization']
    assert row['proof_status'] == 'released_after_derivation'
    assert moment(row['derivation_completed_utc']) < moment(row['proof_released_utc'])
    fresh = ROOT / row['derivation_path']
    assert digest(fresh.read_bytes()) == row['derivation_sha256']
    folder = fresh.parent
    source = ROOT / 'S6_SERIES_PUBLISH_III.tex'
    original_source = source.read_bytes()
    assert digest(original_source) == SOURCE_SHA == row['released_source_sha256']
    text = original_source.decode()
    first, last, final_lf = SCOPES[args.tag]
    argument = '\n'.join(text.splitlines()[first - 1:last])
    if final_lf:
        argument += '\n'
    assert digest(argument.encode()) == row['released_proof_sha256']
    release_kind = 'argument' if args.tag in {'037N', '03DH', '036Z', '037K'} else 'proof'
    released = (folder / f'S6_SERIES_PUBLISH_III_{args.tag}_released_{release_kind}.tex').read_text()
    if args.tag == '037N':
        assert digest(released[released.index(argument):].rstrip('\n').encode()) == row['released_proof_sha256']
    else:
        assert row['released_proof_sha256'] in released
    assert argument in released and row['proof_released_utc'] in released
    comparison_path = folder / f'S6_SERIES_PUBLISH_III_{args.tag}_comparison.md'
    comparison = comparison_path.read_text()
    assert digest(comparison_path.read_bytes()) == args.root_reviewed_comparison_sha
    assert SOURCE_SHA in comparison and row['released_proof_sha256'] in comparison
    assert len(comparison.split()) >= 100
    if args.tag in {'02KA', '037N', '03DH'}:
        guards = json.loads((folder / f'S6_SERIES_PUBLISH_III_{args.tag}_guards.json').read_text())
        assert len(guards) == 1
        old, new = guards[0]['old'], guards[0]['new']
        assert (folder / f'S6_SERIES_PUBLISH_III_{args.tag}_receiving.tex').read_text() == new + '\n'
        scope = {'02KA': (8202, 8268), '037N': (25723, 25755), '03DH': (28552, 28562)}[args.tag]
        assert text[:text.index(old)].count('\n') + 1 == scope[0]
        assert text[:text.index(old) + len(old)].count('\n') + 1 == scope[1]
    else:
        _, guards = read(folder / f'S6_SERIES_PUBLISH_III_{args.tag}_replacements.tsv')
        assert len(guards) == 1
        guard = guards[0]
        assert guard['statement_id'] == row['label']
        old, new = guard['old_text'], guard['new_text']
    assert text.count(old) == 1 and argument in old
    assert digest(new.encode()) == args.root_reviewed_replacement_sha
    for pattern in [r'\\label\{([^}]+)\}', r'\\hypertarget\{([^}]+)\}', r'\\tag\{([^}]+)\}']:
        assert sorted(re.findall(pattern, old)) == sorted(re.findall(pattern, new))
    events_path = ROOT / 'CHECK_EVENTS.tsv'
    original_events = events_path.read_bytes()
    event_fields, events = read(events_path)
    proposal_path = folder / f'S6_SERIES_PUBLISH_III_{args.tag}_CHECK_EVENTS.tsv'
    proposal_fields, proposals = read(proposal_path)
    assert proposal_fields == event_fields and len(proposals) == 1
    event = proposals[0]
    event_suffix = 'completed-targeted' if args.tag in {'02KA', '037N', '03DH'} else 'targeted'
    assert event['event_id'] == f'publish:c5:III:{args.tag}:{event_suffix}'
    assert event['statement_id'] == row['label']
    assert event['type'] == 'targeted proof check'
    assert event['event_id'] not in {e['event_id'] for e in events}
    assert moment(row['proof_released_utc']) <= moment(event['date_utc']) <= datetime.now(timezone.utc)
    relative_comparison = str(comparison_path.relative_to(ROOT))
    assert relative_comparison in event['where'] and row['derivation_path'] in event['where']
    assert row['released_proof_sha256'] in event['outcome']
    if args.tag == '037N':
        event['outcome'] += (' Root read every original and receiving definition line, the complete comparison, all four defect rows and the exact guard. Root-admitted replacement text SHA256 '
                             + args.root_reviewed_replacement_sha + '.')
    assert args.root_reviewed_replacement_sha in event['outcome']
    row.update(status='done', packet_status='required_check_complete',
               source_ownership_status='verified_exact_individual_scope',
               check_event_id=event['event_id'],
               proof_comparison_evidence=relative_comparison,
               completion_evidence=row['derivation_path'] + '; ' + relative_comparison + '; CHECK_EVENTS.tsv event ' + event['event_id'],
               notes=row['notes'] + ' Root read every old/new argument line, the complete comparison, all guard/defect/event rows, and admitted this exact individual scope. Publication application and final page review retain their own open rows.')
    result = io.StringIO(newline='')
    writer = csv.DictWriter(result, fields, delimiter='\t', lineterminator='\n')
    writer.writeheader(); writer.writerows(rows)
    product = result.getvalue().encode()
    checked = list(csv.DictReader(io.StringIO(product.decode()), delimiter='\t'))
    assert [r for r in checked if r['tag'] != args.tag] == other_rows
    append = io.StringIO(newline='')
    csv.DictWriter(append, event_fields, delimiter='\t', lineterminator='\n').writerow(event)
    assert original_events.endswith(b'\n')
    assert progress.read_bytes() == original_progress and events_path.read_bytes() == original_events
    assert source.read_bytes() == original_source
    events_path.write_bytes(original_events + append.getvalue().encode())
    progress.write_bytes(product)
    print('Admitted', event['event_id'], 'at', datetime.now(timezone.utc).isoformat())
    print('Preserved individual argument SHA256', row['released_proof_sha256'])
    print('Other rows, previous events, structural index and manuscript remain unchanged.')


if __name__ == '__main__':
    main()
