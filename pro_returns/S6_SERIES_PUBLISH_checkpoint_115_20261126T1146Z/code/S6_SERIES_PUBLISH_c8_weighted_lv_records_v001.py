"""Write the final LV publication review-derived local records."""
import csv
from datetime import datetime, timezone
import hashlib
from pathlib import Path
root=Path(__file__).resolve().parent.parent
lane=root/'agents/continuation8_iii_weighted_units'
fragment='agents/continuation8_iii_integration/units/weighted/weighted_os45.tex'
p=root/fragment
assert hashlib.sha256(p.read_bytes()).hexdigest()=='bb2d72b21bb254ba6c30d1f14656ba61ef8ac572895b71604a195eaa2570223f'
review_path=lane/'S6_SERIES_PUBLISH_LV_unit_review.md'
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
write('S6_SERIES_PUBLISH_LV_unit_criteria.tsv',['criterion','proposed_state','evidence'],criteria)
fields=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where']
now=datetime.now(timezone.utc).isoformat()
scopes=[
 ('LV','maps:src:D.2.53','Whole repaired1365-line input read, with exact complete blank-line difference to admitted v005 receiver; whole407-line comparison,129-line source note,124-line root sign review and73-line root admission reread. Whole1368-line candidate plus all26 readback changes, final actual order-eight transgression and exact citation change read. Final1404-line unit preserves all69 old identities, complete OF5-OF14 boundary extension, signed Thom map/eighth factors, negative physical characters, original edge/Phi, full Wang detector, degree4 reference, integral Borel/whole-chain link and full P/mu. Q252 exact link wholly read. No new refutation, required row or independent-check increment; global gates open.'),
 ('Q251','maps:def:weighted-os45-data','Whole new input definition read: actual Q110 OS45 base profile and ordered marking, P2G/Q8G, weights(2,0,0,0,0) supported atI8, all prescribed multiplicative Mumford caps, ordinary e1 and complex orientation. Original D.PC3 identity retained at this definition. No independent-proof increment; global gates open.')]
events=[]
for short,statement,scope in scopes:
 event='III-C8-LV-'+short+'-PUBLICATION-READBACK'
 events.append([statement,'2026-11-25','GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical reasoning effort not separately exposed; continuation eight weighted-unit editor','used and rechecked in this run',scope,event,'continuation-eight-publication',str(review_path.relative_to(root)),'whole substantive review','used and rechecked in this run',event,'','',now,fragment])
write('S6_SERIES_PUBLISH_LV_CHECK_EVENTS.tsv',fields,events)
table=lane/'S6_SERIES_PUBLISH_LV_publication_defects.tsv'
with table.open(newline='') as f:
 r=csv.DictReader(f,delimiter='\t');fields=r.fieldnames;rows=list(r)
assert len(rows)==451
old=r'\cite[Remark~2.17, p.~12; \S6.1, pp.~24--25]{Redden2011StringStructures}.'
new=r'\cite[arXiv version~2, Remark~2.17, p.~12; \S6.1, pp.~24--25]{Redden2011StringStructures}.'
assert old not in p.read_text() and p.read_text().count(new)==1
for kind in ['D18','D23']:
 rows.append(dict(zip(fields,[f'III-C8-LV-PUB-350-{kind}',kind,'maps:src:D.2.53','weighted_os45.tex Redden primary citation','pending page concordance','weighted/weighted_os45.tex','pending final build',old,new,'Name the exact arXiv version2 whose page12/24-25 loci were actually read; preserve the existing key and mathematical inputs. Applied by the bounded exact patch and read back.','']))
for row in rows:row['review_status']='whole repaired input/admitted comparison/source/root/candidate and every bounded follow-up read; source-local complete; root admission/global gates open'
with table.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
historical=[
 ('III_OS45_core_independent.py','6e7ccf5a7e6e6b3aa67444c03b54d107b3915973442a0a4c97453123bc2f9009','Earlier whole261-line source and actual344-assertion replay stdout/empty stderr read. Current bounded source reread for geometric column origins; no new execution.'),
 ('III_OS45_primitive_cubic_independent.py','df8fdd2012fe0bba5cbbbf427bf382f74e64d432bfc4b4f3ab76153f3a46bc97','Earlier whole150-line source and actual19349-assertion replay stdout/empty stderr read. No current execution.'),
 ('III_OS45_annulus_independent.py','d1157bf66fec3a18e38ec08a10241fb873e2d667cb82360b01ef05705388b84d','Earlier whole116-line source and actual309-assertion replay stdout/empty stderr read. No current execution.'),
 ('III_OS45_boundary_prisms_07.py','52ba81a9799d29c511c4d67f5a3d815e0d5a42b3cf14f99d1e923837ca04db9b','Earlier whole77-line source and actual21-assertion replay stdout/empty stderr read; full77-line source reread now. Source supplies prism/cap null witnesses, not refined framing. Temporary JSON is not retained. No current execution.'),
 ('III_weighted_OS45_checks.py','173ca3d9b7ac4512b9ef700c35e0709c1cc35819ebf6ca16c8ff73f88fa9c0fd','Earlier whole72-line source and actual142-assertion replay stdout/empty stderr read. Full-refined0/4 question remained open at this numerical stage. No current execution.')]
programs=[]
for name,sha,scope in historical:
 path='../S6_PUBLISH_programs/code/'+name
 assert hashlib.sha256((root/path).read_bytes()).hexdigest()==sha
 programs.append(['S6_PUBLISH_programs/code/'+name,path,sha,scope])
current=[
 ('S6_SERIES_PUBLISH_c7_lv_fresh_lattices_v001.py','Earlier whole source reading; original execution/output scope belongs to checkpoint91. No claim of a whole fresh lattice-output reread now.'),
 ('S6_SERIES_PUBLISH_c7_lv_toric_coefficients_v001.py','Earlier whole source and continuation-eight stdout reading; original execution scope retained. No new execution.'),
 ('S6_SERIES_PUBLISH_c7_lv_graph_link_v001.py','Earlier whole source and graph stdout reading. The2591-line fresh graph-JSON reading is attributed to checkpoint91; no new whole JSON reading or execution.'),
 ('S6_SERIES_PUBLISH_c8_lv_compare_arithmetic_v001.py','Earlier whole160-line source and all18 actual stdout lines/empty stderr read; five unchanged historical replays and exact relation/Picard/critical comparisons.1746-line comparison JSON program-checked, no new whole manual read.'),
 ('S6_SERIES_PUBLISH_c8_lv_character_transport_v001.py','Earlier whole source and all10 actual stdout lines/empty stderr read; all-integer floor identities,32 orbit transitions, weights and coefficient polynomials. No current execution.'),
 ('S6_SERIES_PUBLISH_c8_weighted_lv_publication_v001.py','Current whole source and actual19-line stdout/empty stderr read; exact repaired-input comparison and322 publication edits. No mathematical independent-check credit.'),
 ('S6_SERIES_PUBLISH_c8_weighted_lv_readback_v001.py','Current whole source and actual166-line stdout/empty stderr read;26 bounded changes after whole1368-line candidate reading. No new refutation or independent credit.'),
 ('S6_SERIES_PUBLISH_c8_weighted_lv_transgression_v001.py','Current whole source and actual22-line stdout/empty stderr read; exact integral obstruction on the actual order-eight sphere before division. No new refutation or independent credit.')]
for name,scope in current:
 path='code/'+name;programs.append([path,path,hashlib.sha256((root/path).read_bytes()).hexdigest(),scope])
write('S6_SERIES_PUBLISH_LV_program_table_proposals.tsv',['printed_path','repository_path','sha256','description'],programs)
print('UTC',now,'CRITERIA',len(criteria),'DEFECT_ROWS',len(rows),'EVENTS',len(events),'PROGRAMS',len(programs))
for short,statement,scope in scopes:print('READING_EVENT',short,statement,scope)
print('FINAL_FRAGMENT',fragment,'LINES',len(p.read_text().splitlines()),'SHA256',hashlib.sha256(p.read_bytes()).hexdigest())
print('NO_SHARED_WRITES; NO_NEW_INDEPENDENT_CREDIT_OR_REQUIRED_ROW; NO_MANIFEST_RECEIPT_OR_EQUATION_TRANSPORT_TABLE')
