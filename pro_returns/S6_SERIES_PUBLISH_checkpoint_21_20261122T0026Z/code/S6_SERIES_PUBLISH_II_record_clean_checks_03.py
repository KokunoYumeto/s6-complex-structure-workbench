"""Record the admitted six-owner batch without assigning visual reading credit."""
from pathlib import Path
import csv,datetime,hashlib,json
R=Path(__file__).resolve().parents[1]
m=json.loads((R/'records/S6_SERIES_PUBLISH_required_check_completion_manifest.json').read_text())
rows=[x for x in m['rows'].values() if x['paper']=='II'];assert len(rows)==61
v=json.loads((R/'records/S6_SERIES_PUBLISH_II_clean_checks_03/append_verification.json').read_text())
s=hashlib.sha256((R/'S6_SERIES_PUBLISH_II.tex').read_bytes()).hexdigest()
assert s=='12e73204ef053b62a7e47599edb4d22d90641683bbac49105f07a37c2e5f20c5'
csv.field_size_limit(100_000_000)
with (R/'S6_SERIES_PUBLISH_defects_II.tsv').open(newline='') as f:n=len(list(csv.DictReader(f,delimiter='\t')))
assert n==393
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
body=f'''

## Paper II fresh checks batch 03 — {now}

The six new completed independent checks are C.2.NC.2 (01C9), C.2.NC.3 (01CA), C5a (01FR), E12 (01GJ), E17 (01GO), and P4.13 (02WK). Paper II has 61 of 197 required rows resolved: 60 independent checks and the previously documented retirement of the production-only remark 01TQ. Exact admission evidence is `records/S6_SERIES_PUBLISH_II_clean_checks_03/manifest.json`, SHA-256 `7ecd965d7ab29f43fcf1e3fdf77317a4006c714a79493c4282d5e4e82833b557`.

All six derivations froze before target-proof release. The complete printed proofs and complete original/proposed blocks were actually read by the checker. Root read all forty-seven literal guards, all six complete proposed blocks, every comparison scope, and all fresh program sources and outputs. Exact freeze/release hashes and chronology, primary-source receipts, and source-application history were checked before admission. The E12 ancillary base-change sequence and the E17 all-integer Cech computations were compared after release and receive no additional independent event.

Two proof passages in P4.13 were repaired explicitly. The Nth power of monodromy is the operator acting unipotently on the filtered abutment. The induced cohomology action is identified by the evaluation pairing with the transpose of the homology action, and its determinant agrees by transposition. The proposition and its numerical bound are unchanged. E17 now gives the inverse maps between the full graph fibre and its Cartier-divisor quotient in the smooth ambient threefold, including nilpotents and multiplicities. The graph itself is not used as a smooth ambient space. The old and new computational methods are compared through explicit algebra and Cech maps.

Current Paper II source SHA-256 is `{s}` with {n} logged edits. Its PDF remains the 776-page recovery candidate 02 from source `9bcff959b7ee1e00779c6aeb2c4c1c921887b2fb08f0c247fbc50a8a084eeda8`; the source is now 106 logged edits newer than that PDF. No Paper II page image has yet been read and no publication gate is claimed.

CHECK_EVENTS.tsv has {v['after_rows']:,} rows, SHA-256 `{v['after_ledger_sha256']}`. The twelve new events are six targeted checks and six actual complete editorial rereadings. The old byte prefix, every old row, exact new tail and unique event identifiers are verified. Source application retained all ordered labels and hypertargets. The remaining inherited compendium interface in C.2.NC.3 is still scheduled for exact owner/source resolution; this batch does not close the paper-wide reference-defect row. G3/G4 proposals and the WN–WQ comparisons are pending admission. Paper I remains complete and untouched; the whole project remains incomplete.
'''
for name in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
 p=R/name;old=p.read_bytes();assert b'## Paper II fresh checks batch 03 ' not in old;p.write_bytes(old+body.encode());assert p.read_bytes().startswith(old)
print(json.dumps(dict(time=now,required_rows_resolved=61,independent_checks=60,source_sha256=s,defect_rows=n,ledger_rows=v['after_rows'])))
