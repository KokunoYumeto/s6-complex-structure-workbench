"""Refresh III counts once after all candidate05 source repairs are settled.

Inspect prints the exact old/new paragraph and added ledger associations.
Apply requires those reviewed totals and retains three exact defect rows.
No raw event or independent-check scope is changed; no derived-file copies
or diffs are made. Page-dependent record derivation remains separate.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import argparse
import csv
import io
import json
import os
import re
import tempfile
import textwrap
import S6_SERIES_PUBLISH_c9_III_check_counts as counts

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)


def parse(body):
    reader = csv.DictReader(io.StringIO(body.decode()), delimiter='\t')
    return reader.fieldnames, list(reader)


def encode(fields, rows):
    stream = io.StringIO(newline='')
    writer = csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=('inspect', 'apply'))
    parser.add_argument('--associations', type=int)
    parser.add_argument('--groups', type=int)
    parser.add_argument('--reviewed')
    args = parser.parse_args()
    names = ('S6_SERIES_PUBLISH_III.tex', 'S6_SERIES_PUBLISH_deposit_fields_III.json',
             'S6_SERIES_PUBLISH_deposit_fields.md', 'S6_SERIES_PUBLISH_provenance_checks.tsv',
             'S6_SERIES_PUBLISH_defects_III.tsv', 'S6_SERIES_PUBLISH_findings_III.tsv',
             'CHECK_EVENTS.tsv', 'records/S6_SERIES_PUBLISH_III_current_check_counts.json')
    original = {name: (ROOT / name).read_bytes() for name in names}
    _, findings = parse(original['S6_SERIES_PUBLISH_findings_III.tsv'])
    assert all(r['status'] == 'done' for r in findings if r['id'] not in ('P4', 'T1'))
    data = counts.current_data(ROOT)
    result = counts.summary(data)
    prior = json.loads(original[names[-1]])
    expected_added = {
        'publish:c9:III:02L0:candidate05_notation',
        'ce:c9-iii-candidate05-02l4-role-reconciliation',
        'ce:c9-iii-candidate05-02lf-role-transport-reconciliation',
        'publish:c9:III:02LJ:final-rendered-bindings',
    }
    # The previous c8/c9 summary serialized aggregates, not selected IDs.
    # Its raw ledger was preserved as an exact prefix by the admitted batch.
    # Remove precisely the four appended events and verify every preceding
    # category/group count and the exact preceding count prose.
    assert {r['event_id'] for r in data['events'][-4:]} == expected_added
    added = [r for r in data['selected'] if r['event_id'] in expected_added]
    assert len(added) == 4 and all(r['type'] == 'used and rechecked in this run' for r in added)
    earlier = dict(data)
    earlier['selected'] = [r for r in data['selected'] if r['event_id'] not in expected_added]
    earlier['counts'] = Counter(r['type'] for r in earlier['selected'])
    earlier['groups'] = {counts.group_key(r) for r in earlier['selected']}
    assert len(earlier['selected']) == prior['selected_event_associations']
    assert len(earlier['groups']) == prior['declared_evidence_groups']
    assert dict(earlier['counts']) == prior['counts']
    assert counts.count_prose(earlier) == prior['proposed_section_1_5_paragraph']
    assert result['current_formal_owners'] == prior['current_formal_owners'] == 249
    result['selected_event_ids'] = [r['event_id'] for r in data['selected']]
    result['selected_evidence_groups'] = sorted(data['groups'])
    source = original[names[0]].decode()
    start = source.index('The records associate ')
    ending = 'Each outcome specifies its scope and prior proof exposure.'
    stop = source.index(ending, start) + len(ending)
    old = source[start:stop]
    assert ' '.join(old.split()) == prior['proposed_section_1_5_paragraph']
    paragraph = counts.count_prose(data)
    new = textwrap.fill(paragraph, width=76)
    assert old != new and source.count(old) == 1
    assert sum(data['counts'].values()) == len(data['selected'])
    print('Current formal owners:', result['current_formal_owners'])
    print('Selected associations:', len(data['selected']), 'Evidence groups:', len(data['groups']))
    for kind in counts.TYPES:
        print(kind, data['counts'][kind], sep='\t')
    print('EXACT OLD PARAGRAPH\n' + old)
    print('EXACT NEW PARAGRAPH\n' + new)
    print('Added associations, all used and rechecked:')
    for event in added:
        print(event['event_id'], counts.resolved_subject(data, event), sep=' | ')
    if args.mode == 'inspect':
        print('Inspection only; no canonical file changed.')
        return
    assert args.reviewed and args.associations == len(data['selected']) and args.groups == len(data['groups'])
    candidate = dict(original)
    candidate[names[0]] = source.replace(old, new, 1).encode()
    deposit = json.loads(original[names[1]])
    old_provenance = deposit['provenance']
    old_check = 'How it was checked. ' + ' '.join(old.split())
    new_check = 'How it was checked. ' + paragraph
    assert old_provenance.count(old_check) == 1
    new_provenance = old_provenance.replace(old_check, new_check, 1)
    deposit['provenance'] = new_provenance
    candidate[names[1]] = (json.dumps(deposit, ensure_ascii=False, indent=2) + '\n').encode()
    markdown = original[names[2]].decode()
    assert markdown.count(old_provenance) == 1
    candidate[names[2]] = markdown.replace(old_provenance, new_provenance, 1).encode()
    df, defects = parse(original[names[4]])
    now = datetime.now(timezone.utc).isoformat()
    replacements = ((names[0], old, new, 'METHOD'),
                    (names[1] + '#/provenance', old_provenance, new_provenance, 'DEPOSIT'),
                    (names[2] + ' > Paper III provenance', old_provenance, new_provenance, 'MARKDOWN'))
    for location, before, after, suffix in replacements:
        identifier = 'C9-III-CANDIDATE05-FINAL-COUNTS-' + suffix
        assert not any(r['change_id'] == identifier for r in defects)
        row = dict.fromkeys(df, '')
        row.update(change_id=identifier, type='D15', statement_id='methodology',
            old_location=location, new_location=location, old_text=before, new_text=after,
            reason='All observed candidate05 source repairs are admitted. Recompute the six exact categories and evidence groups from the retained ledger using the unchanged reviewed current-owner and eight literal-intake association rules. Every added association is explicitly used-and-rechecked; no independent proof credit is added.',
            review_status=args.reviewed + ' Admitted ' + now + '. Final PDF agreement remains open.')
        defects.append(row)
    candidate[names[4]] = encode(df, defects)
    pf, claims = parse(original[names[3]])
    claim, = [r for r in claims if r['claim_id'] == 'III-C8-P19']
    values = '/'.join(str(data['counts'][kind]) for kind in counts.TYPES)
    claim['claim'] = f'The current paragraph reports {len(data["selected"]):,} event associations in {len(data["groups"]):,} evidence groups, with counts {values} in the six recorded categories.'
    claim['by_recomputation'] = f'The delivered c9 selector recomputes all six counts; their sum is {len(data["selected"]):,}. Each selected event ID occurs once. All {len(added)} associations added after candidate05 are used-and-rechecked source/context events. The exact selected IDs and declared evidence groups are retained in the count result. The exposed58-input replay still supplies one computation event.'
    claim['evidence'] += '; code/S6_SERIES_PUBLISH_c9_candidate05_finish_counts.py; code/S6_SERIES_PUBLISH_c9_candidate05_finish_counts_inspect02.out; code/S6_SERIES_PUBLISH_c9_candidate05_finish_counts_apply.out'
    claim['current_resolution'] = 'The final admitted source-context events have been included once. The source and both deposit forms contain the same exact computed paragraph. Existing final-PDF and joint-series gates remain; no independent proof credit is added.'
    candidate[names[3]] = encode(pf, claims)
    candidate[names[-1]] = (json.dumps(result, ensure_ascii=False, indent=2) + '\n').encode()
    identities = lambda text: Counter(re.findall(r'\\(?:label|hypertarget)\{[^{}]*\}', text))
    assert identities(source) == identities(candidate[names[0]].decode())
    assert candidate['CHECK_EVENTS.tsv'] == original['CHECK_EVENTS.tsv']
    assert all(b'\r' not in body for body in candidate.values())
    temporary = {}
    try:
        for name, body in original.items():
            assert (ROOT / name).read_bytes() == body, name
        for name, body in candidate.items():
            if body == original[name]:
                continue
            with tempfile.NamedTemporaryFile(dir=ROOT, prefix='c9-final-count-', delete=False) as stream:
                stream.write(body)
                temporary[name] = Path(stream.name)
        for name, body in original.items():
            assert (ROOT / name).read_bytes() == body, name
        for name, path in temporary.items():
            os.replace(path, ROOT / name)
    finally:
        for path in temporary.values():
            path.unlink(missing_ok=True)
    print('Updated final source paragraph, matching deposit fields, existing P19 claim and canonical count result; three exact defect rows retained.')
    print('No raw event, current-owner rule, prior-exposure scope or page-reading gate changed.')


if __name__ == '__main__':
    main()
