"""Serialize the completed minimal-unit review and its six scoped events."""
import csv
from datetime import datetime, timezone
import hashlib
from pathlib import Path
import subprocess
import sys

root=Path(__file__).resolve().parent.parent
lane=root/'agents/continuation8_iii_weighted_units'
fragment='agents/continuation8_iii_integration/units/weighted/minimal_primary_types.tex'
programs=[
 ('S6_SERIES_PUBLISH_c7_lb_conic.py','LB complete finite symbolic table and order-two invariant check; inherited339 source/380 output lines, no new execution.'),
 ('S6_SERIES_PUBLISH_c7_lb_auxiliary_maps.py','LB exact auxiliary lattice, frame and surgery maps; inherited216 source/27 combined-output lines, no separate-stderr claim.'),
 ('S6_SERIES_PUBLISH_c7_lc_odd_cubic.py','LC exact marked odd-primary tables and physical weights; inherited474 source/690 output lines, no new execution.'),
 ('S6_SERIES_PUBLISH_c7_lc_post_exposure.py','LC post-exposure exact-map comparisons; inherited162 source/161 output lines, earlier failure-stream limits retained.'),
 ('S6_SERIES_PUBLISH_c7_le_mixed_v001.py','LE exact mixed-primary lattice and marked invariant checks; inherited477 source/333 stdout lines and actual empty stderr; savedv002 unexecuted.'),
 ('S6_SERIES_PUBLISH_c7_le_post_exposure_v001.py','LE exact auxiliary maps and864 semicharacter checks; inherited71 source/16 stdout lines and empty stderr, no new execution.')]
outcome=('LB whole repaired input and whole publication candidate read with all bounded follow-ups; compared full released statement/proof and admitted evidence; retained all15 patterns/13 rows, all finite multiples/free affine lifts, full fixed-set/global Borel proof and both framed-model maps. Q205 input and equation events have separate scopes. Source-local28 criteria complete; global numbering/references/bibliography/build/page gates remain open. No independent-check credit.')
args=[sys.executable,str(root/'code/S6_SERIES_PUBLISH_c8_weighted_packet_v001.py'),'--unit','MINIMAL','--statement','maps:src:D.2.35','--fragment',fragment,'--outcome',outcome]
for name,description in programs:
 repo='code/'+name
 args.extend(['--program','|'.join((repo,repo,hashlib.sha256((root/repo).read_bytes()).hexdigest(),description))])
subprocess.run(args,cwd=root,check=True)

table=lane/'S6_SERIES_PUBLISH_MINIMAL_CHECK_EVENTS.tsv'
with table.open(newline='') as f:
 r=csv.DictReader(f,delimiter='\t');fields=r.fieldnames;rows=list(r)
assert len(rows)==1
base=rows[0]
for unit,statement,outcome in [
 ('LC','maps:src:D.2.36','LC whole repaired input and complete publication candidate with exact readback edits; complete released statement/proof and admitted comparison/source/admission read. All36 patterns/30 rows and unrestricted permitted finite/affine choices retained; actual simultaneous physical-weight rescaling, global doubled-line/Borel comparison, full H6 and exact model markings checked. No new independent-check credit; global gates remain open.'),
 ('LE','maps:src:D.2.38','LE whole repaired input and complete publication candidate with exact readback edits; complete released statement/proof and admitted comparison/source/admission read. All12 patterns/10 rows retained; full CRT/CW proof now precedes use; actual tensor/frame maps, positive CP3 generator, order-two Cartan chain calculation, full P/h and connected-sum inverse markings checked. Exact inherited-primary locator repair only; no new independent-check credit; global gates remain open.')]:
 row=dict(base);eid='III-C8-MINIMAL-'+unit+'-PUBLICATION-READBACK'
 row.update(statement_id=statement,outcome=outcome,event_id=eid,evidence_group=eid,date_utc=datetime.now(timezone.utc).isoformat())
 rows.append(row)
with table.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)

for tag,label,scope in [
 ('Q205','maps:def:minimal-two-data','Complete15-pattern/13-row input table, positive finite multiples, free affine lifts, ordinary integer clutch, prescribed fans, cocycle sign and actual two framed models.'),
 ('Q206','maps:def:minimal-odd-data','Complete minimal odd-primary natural-row scope c=5,7, exact selected peripheral index, every finite multiple/free affine lift, prescribed cap/fan and ordinary clutch.'),
 ('Q207','maps:def:minimal-mixed-data','Complete12-pattern mixed-primary input with every allowed finite multiple/free affine lift and integer clutch, plus the three actual odd models and their explicit inverse markings.')]:
 subprocess.run([sys.executable,str(root/'code/S6_SERIES_PUBLISH_c8_weighted_definition_event_v001.py'),'--unit','MINIMAL','--tag',tag,'--label',label,'--stem','minimal_primary_types','--scope',scope],cwd=root,check=True)

all_paths=(root.parent/'REPOSITORY_PROGRAM_PATHS.txt').read_text().splitlines()
historical=['code/III/manifolds_tate_markings.py','code/III/fourfolds_D2_c2_AH.py','code/III/manifolds_odd_prime_AH.py','code/III/manifolds_mixed_prime_AH.py']
historical_rows=[]
for name in historical:
 matches=[x for x in all_paths if x.endswith('/'+name) and 'S6_10_PAPERS_checkpoint_15_20261119T1045Z/' in x]
 assert len(matches)==1,(name,matches)
 historical_rows.append([name,matches[0],'','Historical locator only; admitted packet leaves source/output unopened; no source hash or execution claim.'])
with (lane/'S6_SERIES_PUBLISH_MINIMAL_historical_program_references.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['printed_path','repository_path','sha256','scope']);w.writerows(historical_rows)
with table.open(newline='') as f:
 final=list(csv.DictReader(f,delimiter='\t'))
assert len(final)==6 and len({r['event_id'] for r in final})==6
print('SCOPED_EVENTS6: LB,LC,LE,Q205,Q206,Q207; NEW_EQUATION_IDENTITIES67_WITHIN_PROOF_SCOPE; INDEPENDENT_CREDIT0')
print('PROGRAM_PROPOSALS6; HISTORICAL_UNOPENED_LOCATORS4; SHARED_WRITES0')
