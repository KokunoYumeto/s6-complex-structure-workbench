"""Record the two observed converged builds; this grants no page-reading credit."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import io
import importlib.util

root = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('c9_build_diagnostics', root / 'code/S6_SERIES_PUBLISH_c9_build_III.py')
driver = importlib.util.module_from_spec(spec)
spec.loader.exec_module(driver)
assert hashlib.sha256((root / 'S6_SERIES_PUBLISH_III.tex').read_bytes()).hexdigest() == '12ac7263a7720a8ec8910f588a4f753e60294036cb4a57ad1aa9e36c47694e65'
observations = [('current', 'candidate02', 3, '482f63f9871dd1da8f3065664f4a44cec2d1d8345b46119429541a44761aee01'),
                ('legacy', 'candidate01', 4, '37acaa8a50852587feca9d1b7111dffa2b9dc9bbe49718cf626f81acee3d6e49')]
logs = []
for kernel, run, final_pass, identity in observations:
    stem = f'code/S6_SERIES_PUBLISH_c9_build_III_{kernel}_{run}'
    out = (root / (stem + '.out')).read_text()
    assert 'UTC complete ' in out and f'Pass {final_pass} exit 0' in out
    assert 'Pages:           696' in out
    assert not (root / (stem + '.err')).read_bytes()
    log = f'code/S6_SERIES_PUBLISH_c9_III_{kernel}_{run}_pass{final_pass:02d}.log'
    overflow, unresolved, fonts, anchors = driver.diagnostics((root / log).read_text(errors='replace'))
    assert [width for width, _ in overflow] == [0.83005, 1.34203]
    assert not unresolved and not fonts and not anchors
    pdf = root / f'agents/continuation9_build_III/{kernel}/S6_SERIES_PUBLISH_III.pdf'
    assert hashlib.sha256(pdf.read_bytes()).hexdigest() == identity
    logs.append(log)
path = root / 'S6_SERIES_PUBLISH_build_progress.tsv'
old = path.read_bytes()
reader = csv.DictReader(io.StringIO(old.decode()), delimiter='\t')
fields, rows = reader.fieldnames, list(reader)
row, = [row for row in rows if row['paper'] == 'III']
assert row['status'] == 'open'
row.update(status='done', date_utc=datetime.now(timezone.utc).isoformat(),
    source_file='S6_SERIES_PUBLISH_III.tex',
    pdf_file='agents/continuation9_build_III/current/S6_SERIES_PUBLISH_III.pdf',
    pdf_sha256=observations[0][3], log_files='; '.join(logs),
    evidence='code/S6_SERIES_PUBLISH_c9_build_III.py; code/S6_SERIES_PUBLISH_c9_build_III_current_candidate02.out; code/S6_SERIES_PUBLISH_c9_build_III_legacy_candidate01.out',
    detail='The same source converged under LaTeX 2026-11-01 in three passes and LaTeX 2024-11-01 patch2 in four. Both have 696 pages, no undefined references/citations, missing fonts or duplicate/missing anchors, and only 0.83005pt and 1.34203pt overfull boxes. The current-kernel candidate is the page-reading input. All rendered-page, T1 alias and joint-series gates retain their own scope; this build row gives no page-reading or mathematical-check credit.')
stream = io.StringIO(newline='')
writer = csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n')
writer.writeheader(); writer.writerows(rows)
assert path.read_bytes() == old
path.write_text(stream.getvalue(), newline='\n')
print('Paper III clean-build row closed for both observed kernels; 696 pages each.')
print('No mathematical check event, T1 completion or page-reading credit was added.')
