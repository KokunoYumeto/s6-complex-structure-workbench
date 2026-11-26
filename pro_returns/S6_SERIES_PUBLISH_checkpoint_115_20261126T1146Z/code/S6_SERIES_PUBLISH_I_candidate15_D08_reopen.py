#!/usr/bin/env python3
"""Record two visually found D08 instances without altering prior evidence."""
from pathlib import Path
import datetime
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
guard_path = ROOT / 'agents/i_cont_provenance/S6_SERIES_PUBLISH_I_candidate15_provenance_guards.json'
assert sha(guard_path) == 'eb55df7eba02abcb71d2e15e252b92fdd060bce5b9f202d62aa64711c4727160'
guards = [g for g in json.loads(guard_path.read_text()) if g['type'] == 'D08']
assert [g['id'] for g in guards] == ['I15-prov-04', 'I15-prov-12']
prior_path = ROOT / 'records/S6_SERIES_PUBLISH_I_candidate15_type_progress.json'
prior = json.loads(prior_path.read_text())
assert 'D08' in prior['types_closed']
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
out = ROOT / 'records/S6_SERIES_PUBLISH_I_candidate15_D08_reopen.json'
assert not out.exists()
record = {
    'recorded_utc': now, 'paper': 'I', 'type_id': 'D08',
    'candidate15_source_sha256': prior['source_sha256'],
    'candidate15_pdf_sha256': prior['pdf_sha256'],
    'superseded_D08_disposition': str(prior_path.relative_to(ROOT)),
    'prior_record_sha256': sha(prior_path),
    'guard_path': str(guard_path.relative_to(ROOT)), 'guard_sha256': sha(guard_path),
    'finding_ids': [g['id'] for g in guards],
    'candidate15_pages': [g['page'] for g in guards],
    'source_state': 'D08 reopened for the two exact source passages found in full-page reading. The earlier bounded occurrence audit and initial source-clear disposition are preserved as historical evidence and superseded for D08.',
    'types_still_closed_at_candidate15': [t for t in prior['types_closed'] if t != 'D08'],
    'types_open_until_guarded_repair': sorted(prior['types_open'] + ['D08']),
    'mathematical_events_added': 0,
}
out.write_text(json.dumps(record, indent=2) + '\n')
ledger = ROOT / 'PROGRESS_LEDGER.md'
text = ledger.read_text()
text, n = re.subn(r'^(\| I \| D08: .*? \|) done;.*? \|$',
    r'\1 open; two candidate15 full-page findings, I15-prov-04 and I15-prov-12; records/S6_SERIES_PUBLISH_I_candidate15_D08_reopen.json |', text, flags=re.M)
assert n == 1
text += f'\n## Paper I D08 reopened — {now}\n\nThe completed candidate15 full-page reading identified two D08 instances on pages 311 and 321 (guards `I15-prov-04` and `I15-prov-12`). This supersedes the earlier D08 source-clear disposition. The other eighteen closed type rows retain their recorded evidence; seven types remain open until the exact guarded repairs and their source review. The initial nineteen-type record is retained unchanged. Evidence: `records/S6_SERIES_PUBLISH_I_candidate15_D08_reopen.json`.\n'
ledger.write_text(text)
print(json.dumps({'record': str(out.relative_to(ROOT)), 'sha256': sha(out), 'types_closed': 18, 'types_open': 7}))
