"""Freeze actual partial reading evidence at the scheduled twelfth checkpoint."""
from pathlib import Path
import datetime as dt
import hashlib
import json
import subprocess
import sys

R = Path(__file__).resolve().parents[1]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
now = dt.datetime.now(dt.timezone.utc)
assert now >= dt.datetime(2026, 11, 21, 17, 41, 17, tzinfo=dt.timezone.utc)
source = '3542f2632cad8f1eb78f0f30f8a64ca91998f3bd1d97010ca76d89297c4bffe7'
assert sha(R / 'S6_SERIES_PUBLISH_I.tex') == source
locations = {
    'root': 'records',
    'edits': 'agents/i_cont_edits',
    'provenance': 'agents/i_cont_provenance',
    'infra': 'agents/continuation_infra',
}
snapshots = []
for role, directory in locations.items():
    originals = sorted((R / directory).glob(f'S6_SERIES_PUBLISH_I_*candidate18_reading_{role}*.json'))
    for number, original in enumerate(originals, 1):
        data = original.read_bytes()
        parsed = json.loads(data)
        assert parsed['source_sha256'] == source
        destination = R / 'records' / f'S6_SERIES_PUBLISH_I_final_checkpoint12_reading_snapshot_{role}_{number:02}.json'
        assert not destination.exists()
        destination.write_bytes(data)
        snapshots.append({'role': role, 'original': str(original.relative_to(R)),
                          'snapshot': str(destination.relative_to(R)), 'sha256': sha(destination)})
record = R / 'records/S6_SERIES_PUBLISH_checkpoint12_reading_snapshots.json'
assert not record.exists()
record.write_text(json.dumps({'recorded_utc': now.isoformat(), 'source_sha256': source,
                             'snapshots': snapshots, 'mathematical_events_added': 0,
                             'reading_credit_added_by_copying': 0}, indent=2) + '\n')
result = subprocess.run([sys.executable, 'code/S6_SERIES_PUBLISH_reading_coverage.py',
                         'I', '--render', 'render/I_candidate18'], cwd=R,
                        text=True, capture_output=True)
(R / 'code/S6_SERIES_PUBLISH_checkpoint12_coverage.out').write_text(result.stdout + result.stderr)
assert result.returncode == 0, result.stderr
coverage = json.loads((R / 'records/S6_SERIES_PUBLISH_I_page_coverage.json').read_text())
status = {
    'status': (
        f'Paper I candidate18 has a clean 346-page PDF with {coverage["covered_pages"]} '
        'current whole-page images read. The109 exact changes are applied in2196 logged rows, '
        'including64 body guards and45 bibliography entries from a complete117-entry primary '
        'metadata review. All243 continuation edits reconstruct forward and backward. The new '
        'reading confirmed four unaccented Neron–Severi spellings and a visible underfull paragraph '
        'on page321; D23 remains open, and their exact repairs are being prepared. Two possible '
        'D08 recap passages are undergoing complete contextual review. The remaining '
        'changed images, final source/PDF/ledger bindings and42 provenance claims retain their '
        'explicit gates. Paper V retains its earlier individual completion and published-v2 '
        'text of record. Papers II, III and IV remain queued in the prescribed order. The '
        'five-paper task remains incomplete.'
    ),
    'pending': (
        'Finish every changed candidate18 image; apply the four confirmed name-accent repairs '
        'and the justified paragraph-spacing repair with complete before/after comparisons; '
        'rebuild and read changed images; bind the final metadata, provenance, defect loci '
        'and individual Paper I completion. Continue II, III, IV, then the five-together review.'
    ),
}
status_path = R / 'records/S6_SERIES_PUBLISH_checkpoint12_status.json'
assert not status_path.exists()
status_path.write_text(json.dumps(status, ensure_ascii=False, indent=2) + '\n')
result = subprocess.run([sys.executable, 'code/S6_SERIES_PUBLISH_continuation_milestone.py',
                         '--candidate', '18', '--checkpoint', '12', '--status-file',
                         str(status_path)], cwd=R, text=True, capture_output=True)
(R / 'code/S6_SERIES_PUBLISH_checkpoint12_milestone.out').write_text(result.stdout + result.stderr)
assert result.returncode == 0, result.stderr
print(json.dumps({'snapshots': snapshots, 'coverage': coverage['covered_pages'],
                  'pages': coverage['page_count'], 'milestone_output': result.stdout}, indent=2))
