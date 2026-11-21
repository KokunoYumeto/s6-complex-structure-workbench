#!/usr/bin/env python3
"""Bind individually completed defect rows to the actually reviewed candidate17."""
from pathlib import Path
import datetime
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
source = ROOT / 'S6_SERIES_PUBLISH_I.tex'
expected = '5b74359a048b1eab3e478a65eab35f35b45474c4c65aadaedd639315c19a9379'
assert sha(source) == expected
dossier_path = ROOT / 'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate17_type_closure_preparation.json'
assert sha(dossier_path) == 'ff839c0a01a01b466e14b1e98bf6fa7deeec047965b0e189dd85d80a42a642e4'
dossier = json.loads(dossier_path.read_text())
assert dossier['source_sha256'] == expected
coverage_path = ROOT / 'build/I_candidate17/build_summary.json'
coverage = json.loads(coverage_path.read_text())
assert dossier['all_types_source_clear'] and not dossier['final_certified']
assert dossier['unique_edit_rows'] == 2087 and dossier['continuation_unique_edit_rows'] == 134
assert sha(ROOT / dossier['pdf_path']) == dossier['pdf_sha256']
assert sha(ROOT / dossier['defect_log_path']) == dossier['defect_log_sha256']
assert sha(ROOT / 'CHECK_EVENTS.tsv') == 'e45bf7b52aff58c0d9fb4a474cd97e9dd7615c761c4a1a79983e268bd27fe714'
open_types = []
closed = []
for row in dossier['rows']:
    assert row['source_clear_in_recorded_review_scope'] and not row['remaining_content_issues']
    closed.append(row['type_id'])
assert len(closed) == 25
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
record = {
    'recorded_utc': now, 'paper': 'I', 'source_sha256': expected,
    'pdf_sha256': dossier['pdf_sha256'],
    'defect_log_sha256': sha(ROOT / 'S6_SERIES_PUBLISH_defects_I.tsv'),
    'dossier_path': str(dossier_path.relative_to(ROOT)), 'dossier_sha256': sha(dossier_path),
    'build_path': str(coverage_path.relative_to(ROOT)), 'build_sha256': sha(coverage_path),
    'types_closed': closed, 'types_open': open_types,
    'newly_closed_types': ['D08', 'D13', 'D18', 'D23'],
    'root_review': 'Root read every one of the twenty-five complete current per-type dispositions. Previously reviewed exact guards and owning-block comparisons bind the 48 applied repairs; all four previously open source categories are clear. The remaining candidate17 changed-page reading is pending and receives no credit from this operation. Final PDF/provenance/page mapping bindings remain separate from individual current-source closure under continuation rule0.3.',
    'mathematical_events_added': 0,
}
out = ROOT / 'records/S6_SERIES_PUBLISH_I_candidate17_type_progress.json'
assert not out.exists()
out.write_text(json.dumps(record, indent=2) + '\n')
ledger_path = ROOT / 'PROGRESS_LEDGER.md'
text = ledger_path.read_text()
for code in closed:
    text, count = re.subn(rf'^(\| I \| {code}: .*? \|) [^|]* \|$',
        rf'\1 done; individually reviewed at candidate17 source5b74359a; records/S6_SERIES_PUBLISH_I_candidate17_type_progress.json |', text, flags=re.M)
    assert count == 1, code
entry = (f'\n## Paper I individual defect rows at candidate17 — {now}\n\n'
         'D08, D13, D18 and D23 now reach their done state after the forty-eight applied guards and complete affected-block comparisons. All twenty-five source types are closed at this exact source snapshot. The eight accent restorations, seven bibliography entries, thirty-three announcement/recap associations and exact convention relocation are logged in 2,087 total repair rows. Root read all twenty-five current per-type dispositions. Changed candidate17 images, final provenance and mapped defect locations retain their separate gates. This operation adds no page-reading or mathematical check credit. Evidence: `records/S6_SERIES_PUBLISH_I_candidate17_type_progress.json`.\n')
ledger_path.write_text(text + entry)
report_path = ROOT / 'S6_SERIES_PUBLISH_report.md'
report_path.write_text(report_path.read_text() + entry)
print(json.dumps({'record': str(out.relative_to(ROOT)), 'sha256': sha(out), 'closed': len(closed), 'open': open_types, 'newly_closed': record['newly_closed_types']}))
