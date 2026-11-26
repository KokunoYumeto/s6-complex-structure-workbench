"""Track the supplied reading findings and the newly observed notation rows."""
from pathlib import Path
from datetime import datetime, timezone
import csv

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
now = datetime.now(timezone.utc).isoformat()
source = ROOT.parent / 'CLAUDE_READING_FINDINGS_PAPER_III.tsv'
out = ROOT / 'S6_SERIES_PUBLISH_findings_III.tsv'
assert not out.exists()
with source.open(newline='') as f:
    r = csv.DictReader(f, delimiter='\t'); rows = list(r); fields = r.fieldnames
fields += ['status', 'date_utc', 'source_resolution', 'remaining_gate', 'evidence']
for x in rows:
    x.update(status='open', date_utc=now, source_resolution='',
             remaining_gate='source settlement and current PDF verification', evidence='')
    if x['id'] == 'P4':
        x.update(status='deferred-joint-phase', source_resolution='Assigned by the controlling prompt to the five-paper dependency-table reconciliation.', remaining_gate='five-paper reconciliation')
    if x['id'] == 'T1':
        x.update(source_resolution='Kernel/AMS display-hook patch removed. Seven literal secondary labels now copy complete primary auxiliary records through SsixDisplayAliases. Legacy-kernel seven-display diagnostic converged and was visually read.',
                 remaining_gate='current-kernel diagnostic and full manuscript builds on both kernels; final PDF alias checks',
                 evidence='code/S6_SERIES_PUBLISH_c9_display_aliases.py; CLAUDE-III-T1')
with out.open('w', newline='') as f:
    w = csv.DictWriter(f, fields, delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(rows)
p = ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv'
with p.open(newline='') as f:
    r = csv.DictReader(f, delimiter='\t'); units = list(r); fields = r.fieldnames
n = 0
for x in units:
    if x['paper'] == 'III' and x['defect_type'] == 'D20' and x['unit_id'] in ('maps:src:D.2.25', 'maps:src:D.2.26'):
        assert x['status'] == 'done'
        x.update(status='open', date_utc=now,
                 evidence='continuation9 global P15 source reading; notation proposals in preparation',
                 detail='Reading identified reused M for a total multiplicity and a local node matrix; in the sixteen-profile proof P,Q also name section data and arithmetic scalars. Reopened pending complete scoped renaming, inverse comparison and readback.')
        n += 1
assert n == 2
with p.open('w', newline='') as f:
    w = csv.DictWriter(f, fields, delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(units)
print('Initialized 18 supplied finding rows: 17 open and P4 deferred to the authorized joint phase.')
print('Reopened two identified D20 unit criteria; no mathematical result or required check reopened.')
