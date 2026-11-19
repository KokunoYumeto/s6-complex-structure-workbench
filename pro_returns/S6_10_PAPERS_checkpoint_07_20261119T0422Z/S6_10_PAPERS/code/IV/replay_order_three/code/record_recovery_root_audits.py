"""Record the root's completed fresh mathematical and visual recovery reviews."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
q=ROOT/'records/k88_standalone_visual_qa.json'
d=json.loads(q.read_text())
d.update(status='PASS',direct_review_utc=datetime.now(timezone.utc).isoformat(),
 direct_reviewed_pages=[1,2,3,4],
 direct_visual_review='All four pages inspected in the full contact sheet; after the table-heading repair, changed pages3 and4 inspected individually at full render size. Both headings now stay with their tables; no clipping, overlap or orphan heading remains.',
 repaired_layout='Reduced-branch table heading moved to page4 with its complete table.',
 before_overfull_above_2pt=0,after_overfull_above_2pt=0)
assert d['pdf_sha256']==sha('code/part3_root/k88_standalone.pdf')
q.write_text(json.dumps(d,indent=2)+'\n')
record={'status':'PASS','reviewer':'root','utc':datetime.now(timezone.utc).isoformat(),
 'source':'notes/part3_source_zero_vertical_pair_working.md',
 'source_sha256':sha('notes/part3_source_zero_vertical_pair_working.md'),
 'scope':'Complete reconstructed VZ.1–9 read in full after recovery.',
 'checked':['Full q-prime inverse and exact suspension square, both native normal charts and proper-height comparison.',
 'Hopf half-phase paired endpoint, degree bj and complex-versus-outward sphere orientation.',
 'Both residual line tensor terms, full outer coefficient gauge and literal free section-disc obstruction test.',
 'Complete block-triangular tangent interpolation; four relative interior pairings with their exact source frames.',
 'Actual cap clutch direction, its c2 sign, physical tautological line and K68 parameter reversal.',
 'Original-boundary Euler collar, integer fixed-scalar assembly and polynomial for every signed vertical integer.',
 'Every native phase-square edge and scalar seam, original DZ physical delta loop and its full retained winding.',
 'Corrected cap table m=4p or4p−1; chi=p and H=2p or8p−2; complete coupled integer pair and doubled ordinary seed.'],
 'certificate':'code/part3/source_zero_vertical_pair.json',
 'prior_history':'The pre-outage audit survives as conversation evidence; this record audits the reconstructed current full text.'}
(ROOT/'records/recovery_20261117/root_k89_full_text_audit.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'k88_visual':'PASS','k89_full_text':'PASS'},indent=2))
