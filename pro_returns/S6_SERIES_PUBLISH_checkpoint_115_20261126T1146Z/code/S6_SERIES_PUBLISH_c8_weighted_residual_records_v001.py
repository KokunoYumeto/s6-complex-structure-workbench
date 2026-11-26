"""Write only the required residual unit review-derived local records."""
import csv
from datetime import datetime, timezone
import hashlib
from pathlib import Path
import re
root=Path(__file__).resolve().parent.parent
lane=root/'agents/continuation8_iii_weighted_units'
fragment='agents/continuation8_iii_integration/units/weighted/residual_even_types.tex'
p=root/fragment
assert hashlib.sha256(p.read_bytes()).hexdigest()=='730728c6a6e74e3dae8536a7da662ac060d04e42a73fafc6a49bbff9d9a41366'
ll=(root/'agents/continuation7_iii_residual_two_primary/S6_SERIES_PUBLISH_III_02LL_receiving.tex').read_text()
lm=(root/'agents/continuation7_iii_residual_twenty_receiving/S6_SERIES_PUBLISH_III_02LM_receiving.tex').read_text()
matches=[]
for leading in range(3):
 for middle in range(1,7):
  for trailing in range(7):
   candidate='\n'*leading+ll.strip()+'\n'*middle+lm.strip()+'\n'*trailing
   if hashlib.sha256(candidate.encode()).hexdigest()=='e49edaf4acbcebff50ca0da3faeeb21662b7a644c3b6f6069bcb6dd580d722ca':
    matches.append((leading,middle,trailing))
assert len(matches)==1,matches
print('EXACT_REPAIRED_INPUT_RECEIVER_BOUNDARY_LFS',matches[0],'NO_INTERIOR_DIFFERENCE')

def write(name,header,rows):
 with (lane/name).open('w',newline='') as f:
  w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(header);w.writerows(rows)

review_path=lane/'S6_SERIES_PUBLISH_RESIDUAL_unit_review.md'
review=review_path.read_text()
criteria=[]
for line in review.splitlines():
 if line.startswith('| '):
  cells=[x.strip() for x in line.strip('|').split('|')]
  if cells[0] in {f'D{i:02}' for i in range(1,28)}|{'Structure'}:
   assert len(cells)==2
   criteria.append([cells[0],'source-local complete; root admission/global gates open',cells[1]])
assert len(criteria)==28
write('S6_SERIES_PUBLISH_RESIDUAL_unit_criteria.tsv',['criterion','proposed_state','evidence'],criteria)
now=datetime.now(timezone.utc).isoformat()
fields=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where']
scopes=[
 ('LL','maps:src:D.2.44','Whole876-line admitted receiver through exact repaired input comparison; whole released statement/proof, comparison, root/source and438-line auxiliary notes; whole publication proof and all bounded changes read. All7 patterns, both signs, characteristic trace/index, every permanently labeled Brown/frame/critical auxiliary, full coefficient invariants and actual marked models preserved. Q24Z fully read and derived from the complete Cartier/cap map and inverse. No independent-check increment; global gates open.'),
 ('LM','maps:src:D.2.45','Whole998-line admitted receiver through exact repaired input comparison; whole released statement/proof, comparison, root/source and387-line auxiliary notes; whole publication proof and all bounded changes read. All11 patterns and all finite/affine parameters preserved. One bounded D25 individual-curve assertion repaired through exact Q24Z map/inverse; its integral sum and all downstream K/λ/P/µ/model data unchanged. Full b20 odd-copy frame bridge and full CRT/CW maps retained. No independent-check increment; global gates open.'),
 ('Q24X','maps:def:semistable-residual-data','Whole final input definition read:7 semistable patterns, both ordinary signs, prescribed primitive fans, exact i0=i−1 inverse and actual c-fold tube/conic-disjoint line surgery embeddings. No independent-proof increment; global gates open.'),
 ('Q24Y','maps:def:additive-residual-data','Whole final input definition read:11 residual additive patterns, every positive m=6k, every permitted e/r/n and affine twist, primitive fixed lift, exact index map and identical marked models with precise Q207 locator. No independent-proof increment; global gates open.')]
events=[]
for short,statement,scope in scopes:
 event='III-C8-RESIDUAL-'+short+'-PUBLICATION-READBACK'
 events.append([statement,'2026-11-25','GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical reasoning effort not separately exposed; continuation eight weighted-unit editor','used and rechecked in this run',scope,event,'continuation-eight-publication',str(review_path.relative_to(root)),'whole substantive review','used and rechecked in this run',event,'','',now,fragment])
write('S6_SERIES_PUBLISH_RESIDUAL_CHECK_EVENTS.tsv',fields,events)

table=lane/'S6_SERIES_PUBLISH_RESIDUAL_publication_defects.tsv'
with table.open(newline='') as f:
 reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
assert len(rows)==426
for row in rows:row['review_status']='whole input/evidence/candidate and all bounded follow-ups read; source-local complete; root admission/global gates open'
with table.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)

prefix='pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/S6_10_PAPERS/'
historical=[
 ('fourfolds_D2_2power_AH.py','6b9dcb7a97b31077920d926307d902f253593eac53d560c733a3be592dfd2abe','Earlier whole95-line source and7 selected LL AH rows read; untransported-fan character repaired by exact Cartier map; no historical execution.'),
 ('manifolds_even_critical_cycles.py','69581a5f46f1f656b8c6892cde2cd406cf5da63ba3a8376ef092e7360ee09bea','Earlier whole106-line source and14 selected signed LL rows read; geometric input corrected; no historical execution.'),
 ('fourfolds_D2_frame_certificate.py','0df6695aea66979c3f80f8059afbf6da27b416b8370281452ef2892c9bdd3fd1','Earlier whole79-line source and14 selected LL frame rows read; kernel/Bott degree established geometrically; no historical execution.'),
 ('maps_D2_II_frame_checks.py','00fc1133b781fa5da62598d39b3d54dfb55eadc7a2a9e76b318bc1918e0d9bc1','Earlier whole37-line source read; full kernel and degree2 proven in receiver; no historical execution.'),
 ('fourfolds_D2_remaining_AH.py','5cc825730be9f7246aa38ade4a91fb3b9029871784a3abaca6fd973bd7924978','Earlier whole130-line source read;1056 semicharacters/62 valuations separately rechecked; no historical execution or missing full-matrix execution.'),
 ('manifolds_extended_critical_cycles.py','4f35f8bbb9bde1de3d10a7e896e176ccf1f13ab8e9aa67f3d6edad9c07b728ec','Earlier whole228-line source read;158 saved pairings and11 preimages separately checked/replaced; large JSON parsed, no manual whole serialization or historical execution.')]
programs=[]
for name,sha,desc in historical:
 path='code/III/'+name
 programs.append([path,prefix+path,sha,'Pinned a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7. '+desc])
current=[
 ('S6_SERIES_PUBLISH_c7_ll_spin_localization.py','Earlier complete source/combined-stream reading; full7-row cyclic localization; intermediate unresolved-P data preserved. No new execution.'),
 ('S6_SERIES_PUBLISH_c7_ll_gamma_character.py','Earlier complete source/combined-stream reading; exact integral characteristic-index character. No separate-stderr claim or new execution.'),
 ('S6_SERIES_PUBLISH_c7_ll_critical_cycles_v01.py','Earlier whole182-line source/26-line combined stream and used JSON fields read; exact7-row critical chains/both signs. No new execution.'),
 ('S6_SERIES_PUBLISH_c7_lm_fresh_geometry_v003.py','Earlier whole284-line source/57-line stdout and empty stderr read; all11 critical rows and integral sections. Failed v001/429-byte stderr and successful v002 remain prior history; no new execution.'),
 ('S6_SERIES_PUBLISH_c7_lm_receive_aux_v001.py','Earlier whole source/202-line stdout and empty stderr read; all1056/62/158/11 bounded historical comparisons and replacements. No new execution.'),
 ('S6_SERIES_PUBLISH_c7_lm_receive_textfix_v001.py','Earlier whole source/actual successful streams read; exact source quotient BA=I and AB projection identities. No new execution.'),
 ('S6_SERIES_PUBLISH_c8_weighted_residual_edit_v001.py','Current whole source and actual5-line stdout/empty stderr read; exact wall M/inverse/example and publication edits. No independent-check credit.'),
 ('S6_SERIES_PUBLISH_c8_weighted_residual_readback_v001.py','Current whole source and complete actual stdout/empty stderr read; symbolic total preservation, all11 K/P/λ/order substitutions and all52 bounded changes. No independent-check credit.')]
for name,desc in current:
 path='code/'+name;programs.append([path,path,hashlib.sha256((root/path).read_bytes()).hexdigest(),desc])
write('S6_SERIES_PUBLISH_RESIDUAL_program_table_proposals.tsv',['printed_path','repository_path','sha256','description'],programs)
print('UTC',now,'CRITERIA',len(criteria),'DEFECT_ROWS',len(rows),'EVENTS',len(events),'PROGRAMS',len(programs))
for short,statement,scope in scopes:print('READING_EVENT',short,statement,scope)
print('FINAL_FRAGMENT',fragment,'LINES',len(p.read_text().splitlines()),'SHA256',hashlib.sha256(p.read_bytes()).hexdigest())
print('NO_SHARED_WRITES; NO_NEW_INDEPENDENT_CREDIT; NO_MANIFEST_RECEIPT_OR_EQUATION_TRANSPORT_TABLE')
