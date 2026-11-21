#!/usr/bin/env python3
"""Bind individually completed defect rows to the actually reviewed candidate16."""
from pathlib import Path
import datetime
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
source = ROOT / 'S6_SERIES_PUBLISH_I.tex'
expected = '61ffa2e316814c140fc69723e080b4414ea4016ba27e0ac84bd2d9347fbc93fc'
assert sha(source) == expected
dossier_path = ROOT / 'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate16_type_closure_preparation.json'
assert sha(dossier_path) == '0b77945c49f60963e2c96fff0eaef6c4c31c1107c02fbe326054fc2d4c0e2a35'
dossier = json.loads(dossier_path.read_text())
assert dossier['source_sha256'] == expected
coverage_path = ROOT / 'records/S6_SERIES_PUBLISH_I_candidate16_complete_coverage_snapshot.json'
coverage = json.loads(coverage_path.read_text())
assert coverage['source_sha256'] == expected and coverage['all_pages_read']
assert coverage['page_count'] == coverage['covered_pages'] == 346
open_types = ['D08', 'D13', 'D18', 'D23']
closed = []
for row in dossier['rows']:
    if row['type_id'] in open_types:
        assert row['remaining_content_issues']
    else:
        assert row['source_clear_in_recorded_review_scope'] and not row['remaining_content_issues']
        closed.append(row['type_id'])
assert len(closed) == 21
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
record = {
    'recorded_utc': now, 'paper': 'I', 'source_sha256': expected,
    'pdf_sha256': coverage['pdf_sha256'],
    'defect_log_sha256': sha(ROOT / 'S6_SERIES_PUBLISH_defects_I.tsv'),
    'dossier_path': str(dossier_path.relative_to(ROOT)), 'dossier_sha256': sha(dossier_path),
    'coverage_path': str(coverage_path.relative_to(ROOT)), 'coverage_sha256': sha(coverage_path),
    'types_closed': closed, 'types_open': open_types,
    'newly_closed_types': ['D01', 'D02', 'D11', 'D16'],
    'root_review': 'Root read every one of the twenty-five complete per-type dispositions, the exact applied guards and source comparisons at their stated scopes, and the current full-page findings. The four remaining content categories are explicit. Final PDF/provenance/page mapping bindings remain separate from individual current-source closure under continuation rule0.3.',
    'mathematical_events_added': 0,
}
out = ROOT / 'records/S6_SERIES_PUBLISH_I_candidate16_type_progress.json'
assert not out.exists()
out.write_text(json.dumps(record, indent=2) + '\n')
ledger_path = ROOT / 'PROGRESS_LEDGER.md'
text = ledger_path.read_text()
for code in closed:
    text, count = re.subn(rf'^(\| I \| {code}: .*? \|) [^|]* \|$',
        rf'\1 done; individually reviewed at candidate16 source61ffa2e3; records/S6_SERIES_PUBLISH_I_candidate16_type_progress.json |', text, flags=re.M)
    assert count == 1, code
entry = (f'\n## Paper I individual defect rows at candidate16 — {now}\n\n'
         'D01, D02, D11 and D16 now reach their done state after the sixty-two applied guards, complete affected-block comparisons and current page reading. Twenty-one types are closed at this exact source snapshot. D08, D13, D18 and D23 remain open for the recorded announcement, convention-placement, bibliography and accent findings. All 346 candidate16 images have actual whole-page reading evidence; every changed image in the next build will reopen. '
         'Root read all twenty-five per-type dispositions. This status operation adds no mathematical check event. Evidence: `records/S6_SERIES_PUBLISH_I_candidate16_type_progress.json`.\n')
ledger_path.write_text(text + entry)
report_path = ROOT / 'S6_SERIES_PUBLISH_report.md'
report_path.write_text(report_path.read_text() + entry)
print(json.dumps({'record': str(out.relative_to(ROOT)), 'sha256': sha(out), 'closed': len(closed), 'open': open_types, 'newly_closed': record['newly_closed_types']}))
