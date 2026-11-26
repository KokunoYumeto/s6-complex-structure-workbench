"""Close supplied T1 after the two full builds and all seven actual equation images."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib
ROOT=Path(__file__).resolve().parents[1]
assert hashlib.sha256((ROOT/'S6_SERIES_PUBLISH_III.tex').read_bytes()).hexdigest()=='12ac7263a7720a8ec8910f588a4f753e60294036cb4a57ad1aa9e36c47694e65'
for kind,digest in [('current','482f63f9871dd1da8f3065664f4a44cec2d1d8345b46119429541a44761aee01'),('legacy','37acaa8a50852587feca9d1b7111dffa2b9dc9bbe49718cf626f81acee3d6e49')]:
 assert hashlib.sha256((ROOT/f'agents/continuation9_build_III/{kind}/S6_SERIES_PUBLISH_III.pdf').read_bytes()).hexdigest()==digest
 evidence=ROOT/f'agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_T1_{kind}_inspect.out'
 assert 'PASS: all 28 ordinary/cref records occur once' in evidence.read_text()
 assert not evidence.with_suffix('.err').read_text()
p=ROOT/'S6_SERIES_PUBLISH_findings_III.tsv'
with p.open(newline='') as f:
 reader=csv.DictReader(f,delimiter='\t'); fields=reader.fieldnames; rows=list(reader)
r=next(r for r in rows if r['id']=='T1')
assert r['status']=='open'
r['status']='done';r['date_utc']=datetime.now(timezone.utc).isoformat()
r['source_resolution']='The complete frozen manuscript converged under LaTeX2026-11-01 and2024-11-01 patch2. Root read both actual full-build alias inspection outputs: all28 ordinary/@cref records occur once, all7 alias pairs agree completely, and all7 shared equation anchors plus their permanent tags resolve once on the recorded pages. All3046 internal named links resolve. The7 equation displays were actually image-read on42/44 by the global reader and538/541/542 by root; each is printed once, complete and legible.'
r['remaining_gate']='Resolved for current candidate02 and legacy candidate01. The later repaired final-source build retains the general PDF/alias recheck gate; no independent proof or unobserved page credit.'
r['evidence'] += '; agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_T1_build_review.md; agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_T1_current_inspect.out; agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_T1_legacy_inspect.out; agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_current_pdf_pages_001_174.md; agents/continuation9_root/S6_SERIES_PUBLISH_III_pages_523_696_reading.md'
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
print('T1 closed after both full builds, exact alias inspection and all7 actual equation images. No source edit or new mathematical-check event.')
