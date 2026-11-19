"""Append the actual current primary-source reading, preserving every event."""
from pathlib import Path
import csv, hashlib

root = Path(__file__).resolve().parents[1]
path = root / 'CHECK_EVENTS.tsv'
with path.open(newline='') as f:
    rd = csv.DictReader(f, delimiter='\t')
    fields, rows = rd.fieldnames, list(rd)
who = ('GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited '
       'from root (not separately exposed), S6_SERIES_GRIND/corrections_audit')
outcome = ('Freshly downloaded and opened exact primary arXiv:2608.26698v2 PDF '
    'and complete mathematical HTML on 2026-11-19. PDF SHA256 '
    '69108442d3063aa0e65a16c07b0afdd806f642d47f5a1d17f339fd77fda79ce2 '
    'matches the retained historical edition. Read Proposition 3.1 and full '
    'proof pp.10–11; preferred clutch normalization and Lemma 4.4 full oriented '
    'PD proof pp.16–17; Lemma 4.8 and g=1 table p.23; Theorem 4.9 p.24; '
    'twisted-double construction and Lemma 6.2 full collar-bordism proof '
    'pp.34–35; Section 2 seam definition. Confirmed exact coordinates '
    '(k,ell)(a)=(1,4), (k,ell)(b)=(8,8), invariant (4k-ell)/24 and '
    'basis (b-8a,a). Preserved Jin seam (x,0)~(f(x),1) and manuscript '
    'inverse-endpoint transport to its forward seam. This closes the current '
    'source-opening gate at those loci; it does not claim a new independent '
    'proof of Jin’s earlier surgery-theory dependencies. Full files, hashes, '
    'locators and scope are in Jin_primary_verification.md and primary_sources/.')
for label in ['night:P3F.22', 'night:P3K.68', 'iv:i3_all_reduced_caps']:
    event = {'statement_id': label, 'date': '2026-11-19', 'who': who,
             'type': 'targeted proof check', 'outcome': outcome,
             'phase': 'S6_SERIES_GRIND'}
    event['event_id'] = 's6sg:' + hashlib.sha256(
        (label+'|source comparison|'+outcome).encode()).hexdigest()[:20]
    if not any(x['event_id'] == event['event_id'] for x in rows):
        rows.append(event)
with path.open('w', newline='') as f:
    wr = csv.DictWriter(f, fieldnames=fields, delimiter='\t')
    wr.writeheader(); wr.writerows(rows)
print(len(rows), 'typed events retained')
