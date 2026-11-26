"""Write bounded notation review proposals without touching canonical files.

The caller supplies already reviewed Packet operations. Complete proposed
proofs stay in scratch tmp; retained artifacts are authored code, exact defect
proposals, source differences, actual output, and scoped used-only events.
"""
from pathlib import Path
import csv
from datetime import datetime, timezone
import difflib
import re
from S6_SERIES_PUBLISH_c9_backend_notation import sha


def stage(packets, stem, folder_name, event_suffix, description):
    root = Path(__file__).resolve().parents[1]
    source_path = root / 'S6_SERIES_PUBLISH_III.tex'
    source_bytes = source_path.read_bytes()
    source = source_bytes.decode()
    out = root / 'agents' / folder_name
    tmp = root.parents[1] / 'tmp' / folder_name
    out.mkdir(exist_ok=True)
    tmp.mkdir(exist_ok=True)
    with (root / 'CHECK_EVENTS.tsv').open(newline='') as handle:
        event_fields = next(csv.reader(handle, delimiter='\t'))
    stamp = datetime.now(timezone.utc).isoformat()
    rows, events = [], []
    for p in packets:
        assert p.source == source, (p.tag, 'source changed during preparation')
        back = p.new
        for op in reversed(p.operations):
            assert back.count(op['new']) == 1, (p.tag, op['name'], 'inverse guard')
            back = back.replace(op['new'], op['old'], 1)
        assert back == p.old, (p.tag, 'complete bounded reverse')
        for pattern in [r'\\label\{[^}]+\}', r'\\hypertarget\{[^}]+\}',
                        r'\\(?:[A-Za-z]*ref|cite[A-Za-z]*)\*?(?:\[[^]]*\])?\{[^}]+\}']:
            assert re.findall(pattern, p.old) == re.findall(pattern, p.new), (p.tag, pattern)
        numeric_old, numeric_new = p.old, p.new
        for old_name, new_name in getattr(p, 'numeric_names', []):
            # A qualified symbol can replace a numeral-bearing symbol name.
            # Remove exactly those two complete name spellings from both texts;
            # all other numerals must retain their original ordered sequence.
            for name in (old_name, new_name):
                numeric_old = numeric_old.replace(name, 'NAMEDOBJECT')
                numeric_new = numeric_new.replace(name, 'NAMEDOBJECT')
        assert re.findall(r'\d+', numeric_old) == re.findall(r'\d+', numeric_new), (p.tag, 'numeric values')
        assert '\r' not in p.new
        for number, op in enumerate(p.operations, 1):
            assert source.count(op['old']) == 1, (p.tag, op['name'], 'whole-source old guard')
            rows.append(dict(
                change_id=f'CLAUDE-III-C9-P15-{event_suffix.upper()}-{p.tag}-{number:03}',
                type=op['kind'], statement_id=p.sid,
                old_location=f'{p.tag}, {op["name"]}', old_page=f'candidate02 physical {p.pages}',
                new_location='same complete statement and proof',
                new_page='pending rebuilt image review',
                old_text=op['old'], new_text=op['new'], reason=op['reason'],
                review_status='Complete proof previously read; current concrete retained roles and all affected uses reread and compared. Every operation and the complete proof reverse to the admitted baseline bytes. No new image or independent proof credit. Root admission and changed-page reading pending.'))
        (out / f'{stem}_{p.tag}.diff').write_text(''.join(difflib.unified_diff(
            p.old.splitlines(True), p.new.splitlines(True),
            fromfile=p.tag+' admitted baseline', tofile=p.tag+' retained-role proposal', n=5)))
        (tmp / f'{stem}_{p.tag}_proposed.tex').write_text(p.new)
        event_id = f'publish:c9:III:{p.tag}:{event_suffix}'
        event = {key: '' for key in event_fields}
        event.update(
            statement_id=p.sid, date=stamp[:10],
            who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; continuation nine',
            type='used and rechecked in this run',
            outcome=f'After the already recorded complete {len(p.old.splitlines())}-line proof reading, reread the concrete retained roles and every affected use under prompt0.8. Prepared {len(p.operations)} reversible fragments: '+', '.join(op['name'] for op in p.operations)+'. '+description+' Complete bounded and source-level reverse checks preserve all baseline bytes; permanent identifiers, numerical literals, map definitions and inverse formulas are retained. This is an exposed source readback, with no additional image-reading or independent-proof credit. Root admission and changed-page reading remain pending.',
            event_id=event_id, phase='publication continuation 9', source_file='S6_SERIES_PUBLISH_III.tex',
            source_row=f'{p.tag}: complete proof and concrete retained roles',
            source_event_type='used and rechecked in this run', evidence_group=event_id,
            publish_input_file='../CLAUDE_READING_LOG_PAPER_III.md',
            publish_input_row='P15; prompt0.8 whole-proof scope', date_utc=stamp,
            where=f'code/{stem}.py; agents/{folder_name}/')
        events.append(event)
        print(p.tag, 'baseline', len(p.old.splitlines()), sha(p.old),
              'candidate', len(p.new.splitlines()), sha(p.new))
        for old_name, new_name in getattr(p, 'numeric_names', []):
            print('  numeric-name allowance only', repr(old_name), '->', repr(new_name))
        for op in p.operations:
            print(' ', op['name'], '|', op['kind'])
            for count, old, new in op['details']:
                print('  exact target count', count, repr(old), '->', repr(new))
    forward = source
    for row in rows:
        assert forward.count(row['old_text']) == 1
        forward = forward.replace(row['old_text'], row['new_text'], 1)
    for p in packets:
        assert p.new in forward
    for row in reversed(rows):
        assert forward.count(row['new_text']) == 1, (row['change_id'], 'whole-source new guard')
        forward = forward.replace(row['new_text'], row['old_text'], 1)
    assert forward == source
    assert source_path.read_bytes() == source_bytes
    for suffix, items, fields in [('_defects.tsv', rows, list(rows[0])),
                                  ('_CHECK_EVENTS.tsv', events, event_fields)]:
        with (out / (stem+suffix)).open('w', newline='') as handle:
            writer = csv.DictWriter(handle, fieldnames=fields, delimiter='\t', lineterminator='\n')
            writer.writeheader()
            writer.writerows(items)
    print(len(rows), 'exact fragments;', len(events), 'used-only events; complete reverses, numeric literals and identifiers passed. Canonical files unchanged.')


def compose(*transforms):
    def change(text):
        details = []
        for transform in transforms:
            text = transform(text)
            details.extend(transform.details)
        change.details = details
        return text
    change.details = []
    return change
