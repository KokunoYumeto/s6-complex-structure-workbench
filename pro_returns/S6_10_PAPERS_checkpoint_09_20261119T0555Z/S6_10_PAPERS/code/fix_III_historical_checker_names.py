"""Expand the historical reviewer alias from the supplied S6_09 records.

Only the printed checker metadata changes. The original records, mathematical
statements and proofs remain unchanged, and no new proof credit is created.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import re

P = Path(__file__).resolve().parents[1]
source = P.parents[1] / 'sources/s6_09/S6_09_PAPERS_inventory.csv'
rows = list(csv.DictReader(source.open()))
bylabel = {r['printed_label']: r for r in rows}
old = r'/root/cdp\_audit, effort Pro, 2026-11-17'
new = r'GPT-6 Astra (OpenAI, ChatGPT Pro mode; recorded reviewer /root/cdp\_audit), effort Pro, 17 November 2026'


def named_reader(x):
    if isinstance(x, dict):
        if x.get('reader') == '/root/cdp_audit':
            assert x.get('model') == 'GPT-6 Astra (OpenAI, ChatGPT Pro mode)', x
            assert x.get('effort') == 'Pro' and x.get('date') == '2026-11-17', x
            return [x]
        return [a for v in x.values() for a in named_reader(v)]
    if isinstance(x, list):
        return [a for v in x for a in named_reader(v)]
    return []


def main():
    records = []
    targets = list((P / 'papers/III').glob('*.tex')) + [P / 'build/III_preview/preview.tex']
    for file in targets:
        s = file.read_text()
        if old not in s:
            continue
        labels = []
        for line in s.splitlines():
            if old not in line:
                continue
            match = re.search(r'\\StatementRecord\{([^}]+)\}', line)
            assert match, line[:120]
            label = match[1]
            row = bylabel[label]
            readers = []
            for key in ('your_check', 'recorded_checks'):
                try:
                    value = json.loads(row[key])
                except (ValueError, TypeError):
                    continue
                readers.extend(named_reader(value))
            assert readers, (label, 'No exact historical alias mapping')
            labels.append({'label': label, 'reader': readers[0]})
        t = s.replace(old, new)
        file.write_text(t)
        records.append({'file': str(file.relative_to(P)), 'instances': s.count(old), 'labels': labels,
                        'before_sha256': hashlib.sha256(s.encode()).hexdigest(),
                        'after_sha256': hashlib.sha256(t.encode()).hexdigest()})
    assert records, 'No remaining old alias; this one-time reconciliation has already run.'
    receipt = {'recorded_at': datetime.now(timezone.utc).isoformat(),
               'source_inventory': str(source), 'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
               'old': old, 'new': new, 'scope': __doc__, 'files': records}
    (P / 'analysis/III_historical_checker_name_reconciliation.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps({'files': len(records), 'instances_including_preview': sum(r['instances'] for r in records),
                      'distinct_receiving_labels': len({a['label'] for r in records for a in r['labels']})}))


if __name__ == '__main__':
    main()
