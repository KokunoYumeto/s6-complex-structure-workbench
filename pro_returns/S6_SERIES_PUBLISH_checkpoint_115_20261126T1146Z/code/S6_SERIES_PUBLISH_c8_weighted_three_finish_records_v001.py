"""Finish two read-back typography/citation edits and the required local records."""
import csv, hashlib
from datetime import datetime, timezone
from pathlib import Path
import S6_SERIES_PUBLISH_c8_integrate_units as units
root=Path(__file__).resolve().parent.parent
lane=root/'agents/continuation8_iii_weighted_units'
fragment='agents/continuation8_iii_integration/units/weighted/three_primary_types.tex'
p=root/fragment;old=p.read_text();text=old
assert hashlib.sha256(p.read_bytes()).hexdigest()=='6c5c8c1d78ac9e508f5350572f8436d205a16a79b95f418ea782d55a921056ad'
changes=[('LF','D23','Its C9 restriction','Its $C_9$ restriction','Typeset the cyclic group in the final suspension application.'),
 ('LJ','D18',r"forward Poincar\'e dual of \(p_1\); its identification with the intrinsic"+'\nclass is Zhubr §3.13, printed p.807.',
  r"forward Poincar\'e dual of \(p_1\). Its identification with the intrinsic"+'\n'+r'class is proved in \cite[Section~3.13, p.~807]{manZhubr75}.',
  'Use the live scholarly citation with the same already read quarter-map section and printed page.')]
table=lane/'S6_SERIES_PUBLISH_THREE_publication_defects.tsv'
with table.open(newline='') as f:
 reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
for i,(owner,kind,before,after,why) in enumerate(changes,1):
 assert text.count(before)==1,before
 line=text.count('\n',0,text.index(before))+1;text=text.replace(before,after)
 rows.append(dict(zip(fields,[f'III-C8-THREE-RECORD-FINAL-{i:03d}-{kind}',kind,
 'maps:src:D.2.'+('39' if owner=='LF' else '42'),f'three_primary_types.tex final line{line}',
 'pending page concordance','weighted/three_primary_types.tex','pending final build',before,after,why,
 'whole source/candidate/all bounded follow-ups read; source-local complete; global gates open'])))
for row in rows:row['review_status']='whole input/evidence/candidate and every final bounded edit read; source-local complete; root admission and global gates open'
units.check_permanent_identifiers(old,text);p.write_text(text,newline='\n')
with table.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
review_path=lane/'S6_SERIES_PUBLISH_THREE_unit_review.md';review=review_path.read_text()
review=review.replace('2,355 lines, SHA256','2,345 lines, SHA256').replace('168666f9f4e3a8080dba5e5e4663e8f2dd1ced07a424c8fb7f84c780d1ed8dad',hashlib.sha256(p.read_bytes()).hexdigest())
review=review.replace('The exact101-entry former-local-number map is\n`S6_SERIES_PUBLISH_THREE_equation_identities.tsv`. Former56/92 retain',
 'The exact101 former-local-number destinations are recorded in the\nold/new text of the corresponding defect rows. Former56/92 retain')
criteria_changes={
 'D01':'Every own-run, earlier-version and execution-history sentence is removed from the mathematical body. The complete pattern enumeration, formulas and conclusions remain; their historical comparison belongs in this review.',
 'D02':'Defensive clauses are replaced by the positive proved content: the integral kernel, fixed-lattice norm, nonprimitive first column, edge-quotient inverse, full scalar-weight range, direct-sum bordism isomorphism and odd-group quarter-map. No needed assertion or map is removed.',
 'D03':'Both numbered theorems classify the defined constructed manifolds. Neither theorem refutes a workflow proposal or an unseen prompt; admitted historical errors are recorded only in the comparison.',
 'D04':'Internal K8 wording is removed. All theorem and equation references use permanent live labels whose printed numbers root will regenerate; the input locator is the numbered Q110 definition.',
 'D05':'Q223 and Q229 define all mathematical inputs in the paper, including every allowed finite/affine parameter and ordinary clutch. No prompt item or request supplies an unstated hypothesis.',
 'D11':'Repeated negative scope disclaimers are removed. The theorem/input domains state the scope, and the proof gives each necessary positive parameter or map assertion at its use.',
 'D17':'Published homology, cochain, suspension and recognition results have exact source locators at their used forms. The explicit cap/chart, common-character and CRT inverse constructions remain because their precise marked forms are required and are not supplied by a bare general citation.',
 'D23':'The whole source and all bounded changes were read. Neron, Poincare and Bezout accents, cyclic-group typesetting, proof-title capitalization and parallel map grammar are corrected. Final typeset line breaks, page fitting and live statement-number kinds remain root gates.',
 'D24':'This body unit now has exactly the two ordered smooth-classification results described here. Root must match the final introduction and organization to the complete assembled paper; that global comparison is not claimed by this local reading.'}
lines=review.splitlines()
for i,line in enumerate(lines):
 for criterion,evidence in criteria_changes.items():
  if line.startswith('| '+criterion+' |'):lines[i]='| '+criterion+' | '+evidence+' |'
review='\n'.join(lines)+'\n'
review=review.replace('342 sequential edits represented by782 single-type rows','436 sequential edits represented by916 single-type rows')
review=review.replace('Every\nactual success output and empty error stream was read.',
 'The subsequent register-concordance pass made74 prose edits, with\nall positive maps and parameter scopes preserved. Its full diff was read;\n18 bounded grammar/line-end/diacritic edits and two final citation/symbol\nedits were then individually read. The completed total is436 exact\nedits and916 single-type rows. Every actual success output and empty\nerror stream was read.')
review+='\nThe redundant local equation-transport table was removed under the\nparent\'s section0.5 direction. Every exact old/new identity is already\nin the defect rows and the substantive mapping above. No manifest,\nreceipt or additional transport table is created.\n'
review_path.write_text(review,newline='\n')
redundant=lane/'S6_SERIES_PUBLISH_THREE_equation_identities.tsv'
assert redundant.is_file();redundant.unlink()
def write_tsv(name,header,data):
 with (lane/name).open('w',newline='') as f:
  w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(header);w.writerows(data)
criteria=[]
for line in review.splitlines():
 if line.startswith('| '):
  cells=[s.strip() for s in line.strip('|').split('|')]
  if cells[0] in {f'D{i:02}' for i in range(1,28)}|{'Structure'}:
   assert len(cells)==2;criteria.append([cells[0],'source-local complete; root admission/global gates open',cells[1]])
assert len(criteria)==28
write_tsv('S6_SERIES_PUBLISH_THREE_unit_criteria.tsv',['criterion','proposed_state','evidence'],criteria)
now=datetime.now(timezone.utc).isoformat()
event_fields=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where']
scopes=[
 ('LF','maps:src:D.2.39','Whole admitted796-line LF receiver through exact repaired-input comparison, whole released statement/proof and comparison/source/root evidence, whole publication proof and all changed passages. All8 patterns, exact cap/line/Borel maps, full Z9 detector/bordism and framed degree3 model preserved. No independent-check increment; global gates open.'),
 ('LJ','maps:src:D.2.42','Whole admitted1476-line LJ receiver through exact repaired-input comparison, whole released statement/proof and comparison/input/root evidence, whole publication proof and all changed passages. All14 patterns, arbitrary finite lifts, full 18/45/90 invariants, physical weights, CRT/CW inverses and marked models preserved. No independent-check increment; global gates open.'),
 ('Q223','maps:def:minimal-three-data','Whole final input definition:8 patterns/7 selected-site cases in6 coalesced printed rows, all positive finite multiples/free affine lifts/ordinary clutches and the degree3 framed graph model. No independent-proof credit; global gates open.'),
 ('Q229','maps:def:mixed-three-data','Whole final input definition: natural minimal residual6/15/30 data, every allowed finite/affine/ordinary parameter, prescribed fans, exact input-index map and the three marked connected-sum families. No independent-proof credit; global gates open.')]
events=[]
for short,statement,scope in scopes:
 event='III-C8-THREE-'+short+'-PUBLICATION-READBACK'
 events.append([statement,'2026-11-25','GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical reasoning effort not separately exposed; continuation eight weighted-unit editor','used and rechecked in this run',scope,event,'continuation-eight-publication',str(review_path.relative_to(root)),'whole substantive review','used and rechecked in this run',event,'','',now,fragment])
write_tsv('S6_SERIES_PUBLISH_THREE_CHECK_EVENTS.tsv',event_fields,events)
historical_prefix='pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/S6_10_PAPERS/'
historical=[('code/III/manifolds_tate_markings.py','90eb833315270ae25bb4ae76ff909816482b249bcde4729c317526dd15e2b373','Pinned a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7;66-line source/2023-line JSON earlier read; historical stdout/run unavailable.'),
 ('code/III/fourfolds_D2_c3_AH.py','c349dd8943a94a36f2974dc75a9564ffafdcd34f9929b7621757e7cea3c5d3c6','Same pinned commit;165-line source/1290-line JSON earlier read; historical degree auxiliary corrected by explicit fan maps; no historical execution.'),
 ('code/III/manifolds_three_mixed_AH.py','9ebb14d6240da9eb2a52e4411ec516a1d88c3176254f288a2669b5a9c34904fa','Same pinned commit;118-line source/724-line JSON earlier read; local arrays empty; six input files and historical stdout/run not retrieved.')]
programs=[[name,historical_prefix+name,sha,desc] for name,sha,desc in historical]
for name,desc in [
 ('S6_SERIES_PUBLISH_c7_lf_three_primary_v003.py','Earlier whole514-source/275-stdout reading; actual empty stderr; full8-pattern exact integral maps. No new execution.'),
 ('S6_SERIES_PUBLISH_c7_lf_auxiliary_maps_v001.py','Earlier163-source/36-combined-output and JSON-field reading;27 site/seven fan comparisons. No separate-stderr claim or new execution.'),
 ('S6_SERIES_PUBLISH_c7_lj_mixed_three_v001.py','Earlier488-source/208-stdout reading, empty stderr;14 patterns and all integral maps. No separate whole-JSON or new execution claim.'),
 ('S6_SERIES_PUBLISH_c7_lj_action_coefficients_v001.py','Earlier72-source/75-stdout reading, empty stderr;528 refinement identities, action markings and full CRT. No new execution.'),
 ('S6_SERIES_PUBLISH_c7_lj_post_exposure_v001.py','Earlier140-source/77-stdout reading, empty stderr;14 patterns/12 keys/464 refinements/52 adapted matrices. No new execution.')]:
  path='code/'+name;programs.append([path,path,hashlib.sha256((root/path).read_bytes()).hexdigest(),desc])
write_tsv('S6_SERIES_PUBLISH_THREE_program_table_proposals.tsv',['printed_path','repository_path','sha256','description'],programs)
print('UTC',now,'LINES',len(text.splitlines()),'DEFECT_ROWS',len(rows),'EVENTS',len(events),'CRITERIA',len(criteria),'PROGRAMS',len(programs))
print('FINAL_SHA256',hashlib.sha256(p.read_bytes()).hexdigest())
for owner,kind,before,after,why in changes:print('EXACT_FINAL_CHANGE',owner,kind,repr(before),'TO',repr(after))
for short,statement,scope in scopes:print('SCOPED_EVENT',short,statement,scope)
print('NO_SHARED_WRITES; NO_NEW_INDEPENDENT_CREDIT; NO_MANIFEST_RECEIPT_OR_TRANSPORT_TABLE')
