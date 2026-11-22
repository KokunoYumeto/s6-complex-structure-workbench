"""Append the exact E10 admission state without page-reading credit."""
from pathlib import Path
import csv, datetime, hashlib, json
R = Path(__file__).resolve().parents[1]
m = json.loads((R/'records/S6_SERIES_PUBLISH_required_check_completion_manifest.json').read_text())
assert len([x for x in m['rows'].values() if x['paper']=='II']) == 64
v = json.loads((R/'records/S6_SERIES_PUBLISH_II_clean_checks_04/append_verification.json').read_text())
s = hashlib.sha256((R/'S6_SERIES_PUBLISH_II.tex').read_bytes()).hexdigest()
assert s == '4be8221c9bd86874dcfe2b0e90ce8901d31e7d163529eba805d27aa4f5dd6f6c'
csv.field_size_limit(100_000_000)
with (R/'S6_SERIES_PUBLISH_defects_II.tsv').open(newline='') as f:
    assert len(list(csv.DictReader(f, delimiter='\t'))) == 407
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
body = f'''

## Paper II fresh checks batch 04 — {now}

E10 (01GH) is admitted after its derivation froze before target-proof release and its complete printed proof was compared. Paper II has 64 of 197 required rows resolved: 63 independent checks and one previously documented production-only retirement. The admission manifest is `records/S6_SERIES_PUBLISH_II_clean_checks_04/manifest.json`, SHA-256 `f83439efb8a1d67dbec8040ed92b8d8112c253ef8920f679c921c0e4b78c0d4a`.

The frozen construction uses the already checked elliptic surface and its base translate, with a moving genus-two double cover. It supplies exact factorization maps from the threefold to the fixed target curve and proves the fixed-target obstruction. The entire printed Hesse-surface proof was then checked, including its relative tangent kernel at a node, all direct images and all three cohomology tuples. A fresh field-norm calculation and Laurent Cech matrices provide methods different from the two isolated prior routines. These supplements retain their postrelease timing and receive no additional independent event. Both root and checker actually read the entire frozen derivation, complete original and proposed statement/proof blocks, full comparison, all fresh and isolated old programs, and their outputs. Ten exact presentation/citation edits are applied; the statement and its mathematical values are unchanged.

Current source SHA-256 is `{s}`, with 407 logged edits. CHECK_EVENTS.tsv has {v['after_rows']:,} rows, SHA-256 `{v['after_ledger_sha256']}`. Its two new events are one targeted check and one complete editorial rereading; the exact old byte prefix and exact appended tail were verified. The source is 120 logged edits newer than the 776-page recovery candidate 02 PDF. No Paper II page image has been read. Paper I remains complete and untouched; the whole project remains incomplete.
'''
for name in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
    p = R/name
    old = p.read_bytes()
    assert b'## Paper II fresh checks batch 04 ' not in old
    p.write_bytes(old+body.encode())
    assert p.read_bytes().startswith(old)
print(json.dumps(dict(time=now, required_rows_resolved=64, independent_checks=63,
    source_sha256=s, defect_rows=407, ledger_rows=v['after_rows'])))
