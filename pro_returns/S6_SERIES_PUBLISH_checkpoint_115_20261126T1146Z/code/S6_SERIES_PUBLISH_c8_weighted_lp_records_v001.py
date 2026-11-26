"""Write the LP review-derived local records without shared-table mutation."""
import csv
from datetime import datetime, timezone
import hashlib
from pathlib import Path
root=Path(__file__).resolve().parent.parent
lane=root/'agents/continuation8_iii_weighted_units'
fragment='agents/continuation8_iii_integration/units/weighted/weighted_engel_types.tex'
p=root/fragment
assert hashlib.sha256(p.read_bytes()).hexdigest()=='517efdaec2be5d29d75af2a70d74daa6ef76b9a39477f3f9c18c2976d2791a22'
review_path=lane/'S6_SERIES_PUBLISH_LP_unit_review.md'
review=review_path.read_text()
def write(name,fields,rows):
 with (lane/name).open('w',newline='') as f:
  w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(fields);w.writerows(rows)
criteria=[]
for line in review.splitlines():
 if line.startswith('| '):
  cells=[c.strip() for c in line.strip('|').split('|')]
  if cells[0] in {f'D{i:02}' for i in range(1,28)}|{'Structure'}:
   assert len(cells)==2,cells
   criteria.append([cells[0],'source-local complete; root admission/global gates open',cells[1]])
assert len(criteria)==28
write('S6_SERIES_PUBLISH_LP_unit_criteria.tsv',['criterion','proposed_state','evidence'],criteria)
fields=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where']
now=datetime.now(timezone.utc).isoformat()
scopes=[
 ('LP','maps:src:D.2.48','Whole repaired914-line input and exact complete difference to admitted910-line receiver read; whole released83-line statement and556-line two-part proof,258-line comparison,265-line source record and189-line root review read. Whole962-line candidate and all16 bounded follow-ups read. Final955-line proof preserves all parameters, full D2/D3 coefficients, negative physical characters, integral detector/odd-copy/transgression and every quaternion map. Repeated general parity proof is matched through identical framed input to D45.15. No new mathematical refutation or independent-check increment; global gates open.'),
 ('Q250','maps:def:weighted-engel-data','Whole new input definition read: every positive weight d, positive k/ell, integer n/r, affine twist, prescribed D.2.34 fan and fixed markings, both determinant signs, and actual uniform member Md. D.WI1 and its permanent identities retained. No independent-proof increment; global gates open.')]
events=[]
for short,statement,scope in scopes:
 event='III-C8-LP-'+short+'-PUBLICATION-READBACK'
 events.append([statement,'2026-11-25','GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical reasoning effort not separately exposed; continuation eight weighted-unit editor','used and rechecked in this run',scope,event,'continuation-eight-publication',str(review_path.relative_to(root)),'whole substantive review','used and rechecked in this run',event,'','',now,fragment])
write('S6_SERIES_PUBLISH_LP_CHECK_EVENTS.tsv',fields,events)
table=lane/'S6_SERIES_PUBLISH_LP_publication_defects.tsv'
with table.open(newline='') as f:
 r=csv.DictReader(f,delimiter='\t');fields=r.fieldnames;rows=list(r)
assert len(rows)==221
for row in rows:row['review_status']='whole input/originals/evidence/candidate and every bounded follow-up read; source-local complete; root admission/global gates open'
with table.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
programs=[]
historical='code/III/fourfolds_D48_thomas.py'
prefix='pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/S6_10_PAPERS/'
programs.append([historical,prefix+historical,'8e080c4fb00575274b8032e38037dbf8c13bd2d56394e4ef9117f8f9fd46ec2f','Pinned commit a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7. Earlier one isolated post-release4920-case run with whole source/stdout/empty stderr/all JSON fields read by recorded readers. Current pass reads its full execution record and arbitrary-d proof; no new run.'])
current=[
 ('S6_SERIES_PUBLISH_c7_lp_fresh_geometry_attempt1.py','Earlier failed coefficientwise-parity attempt; empty stdout/full traceback retained. No current execution.'),
 ('S6_SERIES_PUBLISH_c7_lp_fresh_geometry_attempt2.py','Earlier partial lattice and1386-case output before floating-division wall failure; actual partial stdout/full traceback retained. No current execution.'),
 ('S6_SERIES_PUBLISH_c7_lp_fresh_geometry.py','Earlier exact successful geometry calculation and complete actual streams recorded. Refined P remained open at that stage. No current execution.'),
 ('S6_SERIES_PUBLISH_c7_lp_finite_character.py','Earlier24-convolution finite Fourier obstruction; not the manifold refined-class value. Whole earlier source/combined output recorded; no current execution.'),
 ('S6_SERIES_PUBLISH_c7_lp_circle_bordism.py','Earlier symbolic endpoint and160-case calculation, with complete geometric circle-bordism companion; whole earlier source/actual output recorded. No current execution.'),
 ('S6_SERIES_PUBLISH_c7_lp_aux_primary_fetch_v001.py','Earlier successful source retrieval retained exact Thomas/historical bytes and empty Kaplan result. No current retrieval or PDF-whole-reading claim.'),
 ('S6_SERIES_PUBLISH_c7_lp_aux_comparison_v001.py','Earlier isolated historical run succeeded before comparison assertion failed on structural SymPy equality. Whole actual stdout/stderr retained. No current execution.'),
 ('S6_SERIES_PUBLISH_c7_lp_aux_comparison_v002.py','Earlier expanded-difference comparison fix; did not rerun historical source. Whole source/actual output recorded. No current execution.'),
 ('S6_SERIES_PUBLISH_c8_weighted_lp_edit_v001.py','Current source/actual21-line stdout and empty stderr read;153 exact edits plus complete receiver/input blank-line comparison. No independent-check credit.'),
 ('S6_SERIES_PUBLISH_c8_weighted_lp_readback_v001.py','Current source/actual30-line stdout and empty stderr read;16 bounded changes after complete962-line candidate reading. No mathematical refutation or independent-check credit.')]
for name,scope in current:
 path='code/'+name;programs.append([path,path,hashlib.sha256((root/path).read_bytes()).hexdigest(),scope])
write('S6_SERIES_PUBLISH_LP_program_table_proposals.tsv',['printed_path','repository_path','sha256','description'],programs)
print('UTC',now,'CRITERIA',len(criteria),'DEFECT_ROWS',len(rows),'EVENTS',len(events),'PROGRAMS',len(programs))
for short,statement,scope in scopes:print('READING_EVENT',short,statement,scope)
print('FINAL_FRAGMENT',fragment,'LINES',len(p.read_text().splitlines()),'SHA256',hashlib.sha256(p.read_bytes()).hexdigest())
print('NO_SHARED_WRITES; NO_NEW_INDEPENDENT_CREDIT; NO_MANIFEST_RECEIPT_OR_EQUATION_TRANSPORT_TABLE')
