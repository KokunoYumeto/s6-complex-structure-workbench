"""Record the admitted G3/G4 checks with exact source and ledger bindings."""
from pathlib import Path
import csv, datetime, hashlib, json

R = Path(__file__).resolve().parents[1]
m = json.loads((R / 'records/S6_SERIES_PUBLISH_required_check_completion_manifest.json').read_text())
rows = [x for x in m['rows'].values() if x['paper'] == 'II']
assert len(rows) == 63
v = json.loads((R / 'records/S6_SERIES_PUBLISH_II_G3_G4_checks_01/append_verification.json').read_text())
s = hashlib.sha256((R / 'S6_SERIES_PUBLISH_II.tex').read_bytes()).hexdigest()
assert s == '459c8c7c3dff70ff2621e567383ac56eaf92fd271b02f83775d2cb994f332d6e'
csv.field_size_limit(100_000_000)
with (R / 'S6_SERIES_PUBLISH_defects_II.tsv').open(newline='') as f:
    n = len(list(csv.DictReader(f, delimiter='\t')))
assert n == 397
assert v['after_rows'] == 8081 and v['added_rows'] == 4
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
body = f'''

## Paper II G3/G4 checks — {now}

G3 and G4 now have complete independent derivations, frozen before their target arguments were released, followed by complete proof comparisons. Paper II has 63 of 197 required rows resolved: 62 independent checks and the previously documented retirement of the production-only remark 01TQ. Admission evidence is `records/S6_SERIES_PUBLISH_II_G3_G4_checks_01/manifest.json`, SHA-256 `7d0b32035591509ccbe6a7f5c6c9e6ea796e5f5cb182c968860e1686ed3cbf9c`. The four literal source guards, including both complete original/proposed mathematical blocks, were actually read by root and the checker. The comparison, primary-source receipts, all fresh program sources and outputs, and the isolated old G4 program were reviewed. No old G3 program is claimed.

The revisions separate the statements from their arguments and record explicit maps for the primitive monomial change, monodromy evaluation pairing, invariant lattice, and coinvariant quotient. The G3 Weierstrass discriminant is checked through an exact Bezout certificate and its infinity coordinate. The G4 source locator is pinned to Wang's verified arXiv v2, with the theorem and homology computations identified in that edition. The historical word “Refuted” in the G3 title was removed; its recorded mathematical status was proved and this editorial change does not claim a refuted mathematical statement. The two frozen checks agree with the printed assertions.

Current Paper II source SHA-256 is `{s}` with {n} logged edits. Its PDF remains the 776-page recovery candidate 02 from source `9bcff959b7ee1e00779c6aeb2c4c1c921887b2fb08f0c247fbc50a8a084eeda8`; the source is 110 logged edits newer than that PDF. No Paper II page image has yet been read and no publication gate is claimed.

CHECK_EVENTS.tsv has {v['after_rows']:,} rows, SHA-256 `{v['after_ledger_sha256']}`. The four new events are two targeted checks and two complete editorial rereadings. The old byte prefix, every old row, exact new tail, and unique event identifiers are verified. Source application retained all ordered labels and hypertargets. E10 and WN–WQ are awaiting root review and admission. Paper I remains complete and untouched; the whole project remains incomplete.
'''
for name in ['PROGRESS_LEDGER.md', 'S6_SERIES_PUBLISH_report.md']:
    p = R / name
    old = p.read_bytes()
    assert b'## Paper II G3/G4 checks ' not in old
    p.write_bytes(old + body.encode())
    assert p.read_bytes().startswith(old)
print(json.dumps(dict(time=now, required_rows_resolved=63, independent_checks=62,
                      source_sha256=s, defect_rows=n, ledger_rows=v['after_rows'])))
