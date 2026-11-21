#!/usr/bin/env python3
"""Attach the eight bounded search associations to their exact inventory rows.

Each row retains its query, domains, receipt and bounded outcome. These are
literature-search records, with no mathematical checking credit.
"""
from pathlib import Path
import csv
import datetime
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100_000_000)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    inventory = ROOT/'S6_SERIES_PUBLISH_inventory.csv'
    searches = ROOT/'agents/i_cont_provenance/S6_SERIES_PUBLISH_I_cont_inventory_searches.csv'
    receipt = ROOT/'records/S6_SERIES_PUBLISH_I_continuation_inventory_searches.json'
    with inventory.open(newline='') as stream:
        reader = csv.DictReader(stream)
        fields, rows = reader.fieldnames, list(reader)
    with searches.open(newline='') as stream:
        additions = list(csv.DictReader(stream))
    before = sha(inventory)
    edits = []
    for target in rows:
        matches = [row for row in additions if (row['paper'],row['label']) == (target['paper'],target['label'])]
        if not matches:
            continue
        old = target['literature_searches']
        marker = 'Continuation 21 November 2026: '
        payload = marker + json.dumps(matches, ensure_ascii=False, sort_keys=True)
        if payload in old:
            continue
        target['literature_searches'] = old + (' | ' if old else '') + payload
        edits.append({'paper': target['paper'], 'label': target['label'], 'old_text': old,
                      'new_text': target['literature_searches'], 'associations': len(matches)})
    assert sum(len([r for r in rows if (r['paper'],r['label']) == (a['paper'],a['label'])]) for a in additions) == 8
    with inventory.open('w',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=fields)
        writer.writeheader(); writer.writerows(rows)
    if edits:
        assert not receipt.exists(), 'Preserve the original application receipt'
        result = {'recorded_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  'input_sha256': before, 'output_sha256': sha(inventory),
                  'search_csv_sha256': sha(searches), 'rows_changed': len(edits),
                  'associations': sum(e['associations'] for e in edits), 'edits': edits,
                  'mathematical_events_added': 0}
        receipt.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'rows_changed':len(edits),'search_associations':len(additions),'inventory_sha256':sha(inventory)}))


if __name__ == '__main__':
    main()
