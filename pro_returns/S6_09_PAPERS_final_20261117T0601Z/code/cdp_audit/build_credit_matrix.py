"""Consolidate actual bounded searches, source matches and separate readers.

Absence in a keyword search is never converted into a universal priority claim.
The underlying search logs retain every command, source hash and hit locator.
"""
import csv,hashlib,json,re
from pathlib import Path
ROOT=Path('/workspace/scratch/037cd144174c')
OUT=ROOT/'deliverables/work/cdp_audit'
AUDIT=json.loads((OUT/'result_audit.json').read_text())
SEARCH=json.loads((OUT/'credit_searches_239.json').read_text())
ELSE=json.loads((OUT/'credit_elsewhere_searches_239.json').read_text())
BY={(r['source_id'],r['baseline']):r for r in SEARCH}
EBY={r['source_id']:r for r in ELSE['records']}
META={'model':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17','timezone':'UTC','reader':'/root/cdp_audit'}
contexts={
 'AC26':{'source':'sources/original/AC26_original_manuscript.pdf','controlling_source':'original PDF; transcription is an additional search aid, not the controlling text',
  'read_scopes':['Original PDF pp9–10, Lemmas2.4/2.6/2.7 with complete proofs','Original PDF pp57 and60, Theorems7.17/7.22 and their complete proofs','Original PDF pp62–64, Proposition7.27 and its complete proof; pp65–67 only the explicitly opened portion','Original PDF section10 pp84–95: every statement and displayed proof','Original PDF pp96–97, AppendixA.1 and its complete proof; following fan statement/proof only in the opened portion'],
  'limitations':'The entire paper was searched. Only these contexts and the separately retained PaperI/A5/root-reader contexts were read for this comparison. No claim that all unrelated hit contexts or all ninety-seven pages were independently rederived.'},
 'E26':{'source':'sources/papers/arXiv_2609.38442_Engel_src/S6.tex','read_scopes':['Source lines225–335, construction/main theorem and setup','Source lines1270–1325, indicated invariant/twisting context','Source lines1640–1758, concluding comparisons and period-domain discussion'],
  'limitations':'Whole source searched; only specified surrounding contexts read in this event. Other independently opened scopes remain identified in their own records.'},
 'DGKX_v1':{'source':'sources/papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie_src/v5oka_maps_modifications_deformations.tex',
  'read_scopes':['Source introduction lines310–373','Tangent-cohomology theorem source lines9445–9487','Kuranishi-line proposition source lines9876–9917'],
  'limitations':'Whole source searched. The standard-family exact tangent/Kuranishi conclusion is known. The additional invariant-reader scopes are retained separately; this record does not claim a complete independent rereading of the whole article.'},
 'DGKX_v2':{'source':'sources/papers/arXiv_2610.00250v2_Du_Guo_Kusakabe_Xie_src/submited-tams.tex','read_scopes':['Source introduction lines210–360 and section-heading inventory'],
  'limitations':'Whole source searched separately from v1. The v2 introduction and theorem inventory concern period-relative compactification, Oka maps and modifications; the v1 tangent/miniversality theorem is not silently attributed to v2. Search absence is bounded, not a claim of novelty.'}}
for c in contexts.values():
 p=ROOT/c['source']
 if p.exists():c['source_sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
(OUT/'credit_context_readings.json').write_text(json.dumps({'reader':META,'contexts':contexts,'method':'Actual whole-file queries are in credit_searches_239.json. These are the separately identified context readings used to judge whether a hit supplies the receiving statement.'},indent=2,ensure_ascii=False)+'\n')

# Full-statement and partial-input matches established from opened originals.
# Each tuple is (baseline, relation, exact locator, mathematical comparison).
matches={}
def found(sid,base,relation,locator,comparison):matches.setdefault(sid,[]).append({'baseline':base,'relation':relation,'locator':locator,'comparison':comparison})
found('A.2.3','elsewhere','full_known','Granger–Schulze2014, Theorems1.1/1.3, pp3,12','The normalization/residue normal-crossing criterion is known. The complete derivation is retained and expressly credited.')
found('C.2.NC.1','elsewhere','full_known','A’Campo1975, Theorem1 p235 and sections2.1–2.2 pp237–241','The proper analytic nearby-fibre Euler formula is known, including multiplicities; the supplied derivation is retained.')
found('C.2.RAT.6','elsewhere','full_known','Arnold1976 pp87–88,92,100–101; Merle–Teissier1977 Theorem2.1.1/Corollary2.1.3; Steenbrink1989 pp165–167','The listed local simple-singularity/spectrum cases are classical. Exact receiving enumeration and derivation are retained as known material.')
found('D.1.1','AC26','full_known','Lemma10.7, original p90','The exact semidirect-product abelianization by coinvariants is already stated and proved; keep the independent full universal-property proof with explicit credit.')
found('D.1.3','AC26','full_known','Lemma2.7 pp9–10; section10.5 p91; AppendixA.1 pp96–97','The retained monodromy invariant/coinvariant calculations and corrected component count are already present, including integral data in the opened lattice calculation.')
found('E19','AC26','full_known','Theorem7.17 p57 and Theorem7.22 p60, both complete proofs','For every admissible original twist, p=12*l0-4*l1-3*l2 is coprime to12; pi1=Z/|p|, homology degrees1,2,3,4 are Z/|p|, H5=0, H0=H6=Z, Euler2. The full tuple is known. Proposition7.27 is not the unrestricted source because its additional divisibility premise is explicit in Remark7.24. E11 miniversality is a separate extension.')
found('E9','DGKX_v1','full_known','Theorem6.12, source lines9445–9487; Proposition6.16, source lines9876–9917','The original-family tangent tuple(1,1,1,0) and smooth reduced Kuranishi line are known from v1. Its omission from v2 does not create a new result. Full proof transferred to PaperI.')
found('C.1.2','elsewhere','full_known','Campana–Demailly–Peternell1998, Corollary1.3; supplied source lines230–295','Generic endpoint vanishing is the known corollary with Serre duality. Every Picard component follows by tensoring the fixed vector bundle with a representative line bundle. An explicit family proof does not create a new conclusion.')
found('E2','elsewhere','full_known','Lehn–Rollenske–Schinko2019, Theorem3.1 and Corollary3.2, p9; full graph proof supplied source lines772–958','The nonholomorphic-pencil generic vector-bundle vanishing and resulting c3=0 are known. The complete corrected graph proof is retained; extending the notation to each Picard component is immediate by a fixed line twist.')
found('E3','elsewhere','full_known_consequence','Campana–Demailly–Peternell1998 Lemma1.4; Lehn–Rollenske–Schinko2019 Theorem3.1/Corollary3.2','Moishezon b2>0 is the exact known lemma. The exclusion of a=2,3 and a nonholomorphic reduction on S6 is its direct combination with the known nonholomorphic-pencil theorem, not a new sphere exclusion.')
found('E4','elsewhere','full_known','ViaclovskyCombs2026, Theorem2.2, pp4–5; standing section2 hypotheses; full proof source lines418–490','The proper connected smooth-manifold-to-curve R1O local-freeness theorem and proof are already supplied. The source acknowledges a Gabber outline through Conrad and describes an analytic Raynaud analogue.')

for sid,loc,text in [
 ('A.1.1','Theorem10.5 and its proof pp88–89; section10.4 pp89–90','The specific normal-crossing ambient obstruction and normalization-kernel mechanism are known; the general conormal filtration, two precise vanishings and every-hypersurface formulation have broader scope.'),
 ('A.1.2','Section10, normal-crossing local calculation pp85–89','The branchwise normalization/conductor mechanism is known. The full canonical kernel presentation and all-dimensional coordinate calculation are a distinct general formulation.'),
 ('A.2.2','Lemma10.2 p87','The conductor-square containment is known. The inverse-Jacobian formulation and general excess kernel are separate additions.'),
 ('A.4.1','Theorem10.5 pp88–89 and section10.4 pp89–90','The torsion-free vanishing and nonzero ambient fibre section on W are known. The exact ambient dimension1 is additional.'),
 ('A.5.1','Theorem10.5 pp88–89','The specified normal-crossing normalization obstruction is known. The general reduced hypersurface Jacobian/conductor injection is broader.'),
 ('C.1.1','Theorem9.1 and section10.6','The sphere example has the same HRR tangent index. The general b1=b2=0 index and Picard-component formulation is a classical calculation, not a claimed new index theorem.'),
 ('D.1.2','Section10.5 p91','The corrected rational component count is known. The receiving integral coinvariant torsion-freeness conclusion is an additional assertion under its stated hypotheses.'),
 ('D.1.5','Section10.5 p91','The bielliptic product exposes the known rank-count defect. The explicit order-two integral torsion/coherent calculations and rational-elliptic product example are distinct receiving components.'),
 ('E7','Local hexagonal cusp construction and section10 context','The original family has the known rank-two logarithmic cusp. The theorem checks this condition for the other named constructions and uses E6 for stability.'),
 ('E11','Theorems7.17/7.22 pp57,60','The construction and arbitrary admissible-twist topology are known. The exact smooth miniversal scale-line conclusion is a separate deformation result.'),
 ('E15','Original periodic hexagonal cusp construction','The cusp model is known. The exact positive-comb tangent tuple and smooth8m+1 miniversal germ are additional.')]:found(sid,'AC26','partial_known_input',loc,text)
found('A.2.1','elsewhere','partial_known_input','Granger–Schulze2014 Proposition3.4 p9 and Corollary3.5 p10','The residue/inverse-Jacobian identification is known; the full ambient twisting identity and application are separately derived.')
found('A.2.2','elsewhere','partial_known_input','Granger–Schulze2014 Proposition3.4/Corollary3.5','The fractional-ideal residue identification is an operative known input; the complete excess criterion is not equated with the cited theorem.')
found('A.5.3','elsewhere','partial_known_input','Campana–Demailly–Peternell2020 Lemma4.6 p685; Furushima1993 section1 Lemma1.1/Corollary1.4 p5','The conductor-canonical calculation is known. Furushima is a narrower projective comparison; the analytic exceptional correction is proved independently with the negative intersection matrix.')
found('A.5.12','elsewhere','partial_known_input','Campana–Demailly–Peternell2020 Lemma4.6 p685 and Proposition4.7 p686; RR70 finite duality','Known canonical and Euler conductor inputs support the new arithmetic-genus/refinement conclusion; retain the independently checked full proof.')
found('A.5.7','elsewhere','partial_known_input','Reid1994, sections3.9 and4.4–4.8, pp716–717,720–724','The derivation-kernel and characteristic-zero trace/pole mechanism is known. The analytic pure-double-conductor cusp statement is proved in the receiving text, without importing the global del Pezzo classification.')
found('A.4.9','elsewhere','known_statement_repaired_and_strengthened','Campana–Demailly–Peternell2020 Proposition7.3 pp693–694','The first generic torsion-free-cotangent conclusion is already asserted. Its printed proof has a false constant-twist genus inference. The receiving full replacement proof and irrational-uniform-transgression strengthening are distinct; describe this as a correction/extension, not a wholly new proposition.')
found('D.1.12','elsewhere','partial_known_input','ViaclovskyCombs2026 Theorem2.3, pp5–6','The torus/S6 direct-image and cup-product argument is known. The b2=0/arbitrary-base and primary-Kodaira statements extend it, with the nonzero Kodaira cup product independently checked.')
found('E6','DGKX_v1','partial_known_input','Theorem6.12 and Proposition6.16, source lines9445–9487,9876–9917','The original specific family has the known smooth Kuranishi line. The receiving theorem proves fibration persistence for an arbitrary rank-two torus fibration, including nonreduced parameter spaces.')
found('E7','E26','partial_known_input','Source main construction and good-reduction/Mumford models','The original cusp and its two independent logarithmic directions are construction inputs, not new period models.')
found('E7','DGKX_v1','partial_known_input','Original-family cusp and tangent/Kuranishi theorem','The standard-family cusp and deformation conclusion are known; the all-named-family rank criterion and general E6 application are broader.')
found('E7','elsewhere','partial_known_input','ViaclovskyCombs2026 Theorem4.1 case(i), Theorem6.1 local formulas; ViaclovskyTwo2026 mum model; Liu–Rollenske compactification proposition','The actual local period models are known construction data. The receiving proof extracts the common invertible logarithmic coefficient and applies the general stability criterion.')
found('E11','elsewhere','partial_known_input','ViaclovskyLog2026 logarithmic-transform proposition logprop and full proof, source lines350–498; Proposition4.7','The actual coprime higher-multiplicity construction and positive deformation dimension are known. Smooth exact one-dimensional miniversality is additional.')
found('E12','elsewhere','partial_known_input','Campana–Demailly–Peternell1998 Lemma1.5; Lehn–Rollenske–Schinko2019 Remark3.7; ViaclovskyCombs2026 Lemma2.1 p4','Failure of the unrestricted lemma was already noted; general base-change torsion exactness is known. The explicit Poincare-line example on A×A×P1, length-one defect and precise replacement calculation are distinct.')
found('E13','elsewhere','partial_known_input','ViaclovskyTwo2026 Proposition6.4, source lines1495–1607, and sections2–3','The actual two-parameter family and its dimension bound are known. The exact tangent tuple and smooth reduced miniversal bidisc are separately proved.')
found('E14','elsewhere','partial_known_input','Liu–Rollenske2026 surface-facts proposition lines232–285, compactification proposition lines402–485 and topology theorem lines1702–1728','The compact sphere construction and its III*/II/I1 fibres are known. The cusp-splitting direction, nonreduced jet calculation and exact tangent/miniversal surface are additional. Commented-out notes are excluded.')
found('E15','elsewhere','partial_known_input','ViaclovskyCombs2026 Theorem1.1; sections8–9, especially section9.2 smoothing bound','The positive comb construction, h01=2m+1,h02=2m and lower deformation bound8m-8 are known. The exact tangent tuple(2m+1,8m+1,6m+1,0) and smooth miniversal dimension8m+1 are additional.')
found('E17','elsewhere','partial_known_input','Lehn–Rollenske–Schinko2019 graph proof and Remark3.7; CDP98 Proposition1.1; CDP20 section3','The exceptional-cubic counterexample and need for an embedded-component exclusion are known source context. The explicit embedded-point counterexample, stabilized-section formula and pencil-specific P1 evaluation proof distinguish the receiving assertions.')
for sid in ['D.1.6','D.1.13']:
 found(sid,'elsewhere','partial_known_input','Wang2026 intro:main/main:theorem and complete fill:tate/fill:rankone/fill:a2/fill:good/fill:log proofs, source lines294–671','The compact order-two rational-homology-sphere construction and its integral invariants are known. Its use as a strict second CDP component-count/coherent-restriction counterexample is the receiving conclusion.')
found('C.2.UN.8','elsewhere','partial_known_input','Rossi2017 Proposition4 pp10–11 and Remark5 p20','The compact projective construction and ambient Hodge numbers are known. The full specific support/cohomology calculation is retained separately.')

# Preserve independent comparisons verbatim, including their different scopes.
independent={}
for file in ['deliverables/work/root/cdp_reserved_credit_comparison.json','deliverables/work/invariants_arithmetic/cdp_A5_credit_comparison.json','deliverables/work/cdp_audit/paperI_transfer_credit_audit.json']:
 for r in json.loads((ROOT/file).read_text()):
  if r.get('source_run')=='S6_03_CDP':independent.setdefault(r['source_id'],[]).append({'record_file':file,'record':r})

# Promote positive independent findings to the consolidated verdict instead of
# burying them underneath a different reader's bounded negative search result.
for sid,records in independent.items():
 for entry in records:
  rr=entry['record']
  for field,base in [('found_in_AC26','AC26'),('found_in_E26','E26'),('found_in_DGKX_v1','DGKX_v1'),('found_in_DGKX_v2','DGKX_v2')]:
   val=rr.get(field)
   if isinstance(val,dict) and val.get('status','').startswith('found'):
    m={'baseline':base,'relation':'full_known' if val.get('full_statement_found') else 'partial_known_input','locator':val.get('locator',''),'comparison':val.get('relation',''),'independent_record':entry['record_file']+'#'+sid}
    if not any(x.get('baseline')==base and x.get('locator')==m['locator'] for x in matches.get(sid,[])):matches.setdefault(sid,[]).append(m)

# Index exact source openings, keeping the named reader attached to each record.
references={}
for file in ['deliverables/work/cdp_audit/references_verified.json','deliverables/work/root/references_verified.json','deliverables/work/invariants_arithmetic/references_verified.json']:
 for r in json.loads((ROOT/file).read_text()):
  keys=r.get('keys',[]) + [r.get('key',r.get('citation_key',''))] + r.get('aliases',[])
  for key in keys:
   if key:references.setdefault(key,[]).append({'record_file':file,'key':key,'status':r.get('status',''), 'locators':r.get('opened_locators',[r.get('opened_locator',r.get('locator',''))]),'scope':r.get('verification_scope',r.get('hypotheses_and_normalization_check',r.get('verification',''))),'reader':r.get('own_check',r.get('reviewer',r.get('reader',r.get('checker',''))))})

results=[]
known=[]
for audit in AUDIT:
 sid=audit['source_id'];ms=matches.get(sid,[])
 item={'source_run':'S6_03_CDP','source_id':sid,'source_title':audit['source_title'],'source_status':audit['source_status'],'proof_sha256':audit['proof_sha256'],'source_file':audit['canonical_file'],'source_lines':[audit['canonical_line_start'],audit['canonical_line_end']], 'reader':META,'own_full_proof_check':audit['own_check'],'proof_outcome':audit['check_outcome'],'comparison_method':'Separate executed whole-file keyword searches in each baseline, bounded context readings, and exact positive statement/proof matches. Search absence is not a universal novelty assertion.','matches':ms,'independent_comparisons':independent.get(sid,[])}
 for base,field in [('AC26','found_in_AC26'),('E26','found_in_E26'),('DGKX_v1','found_in_DGKX_v1'),('DGKX_v2','found_in_DGKX_v2')]:
  s=BY[sid,base];positive=[m for m in ms if m['baseline']==base]
  result={'status':'found_in_checked_scope' if positive else 'not_found_in_checked_scope','full_statement_found':any(m['relation'].startswith('full_known') for m in positive),'terms_searched':s['terms_searched'],'search_record':'deliverables/work/cdp_audit/credit_searches_239.json#'+sid+'|'+base,'searched_files':[{'path':x['file'],'sha256':x['sha256'],'hit_count':len(x['matches'])} for x in s['scans']],'actual_reading_scope_record':'deliverables/work/cdp_audit/credit_context_readings.json#'+base,'matches':positive,'relation':'; '.join(m['comparison'] for m in positive) if positive else 'No full matching receiving statement was identified within the listed queries and actually read contexts. Related construction data or general lemmas may occur; the saved hit list is not a claim that every hit was read.'}
  # The two independent batches supply more specific positive/negative scopes.
  for rec in independent.get(sid,[]):
   r=rec['record']; alt=r.get(field)
   if alt is None and base=='DGKX_v2' and rec['record_file'].startswith('deliverables/work/root/'):
    alt=r.get('found_in_DGKX_v1')
   if alt is not None:result.setdefault('independent_scope_records',[]).append({'file':rec['record_file'],'comparison':alt})
   if sid in ['D.1.14','E9'] and 'credit_outcomes' in r:
    k={'AC26':'AC26','E26':'E26','DGKX_v1':'DGKX2026v1','DGKX_v2':'DGKX2026v2'}[base]
    result.setdefault('independent_scope_records',[]).append({'file':rec['record_file'],'comparison':r['credit_outcomes'].get(k,'')})
  item[field]=result
 text=(ROOT/audit['extracted_file']).read_text()
 citation_keys=sorted({key.strip() for group in re.findall(r'\\cite\w*(?:\[[^\]]*\])*\{([^}]+)\}',text) for key in group.split(',')})
 opened_inputs=[]
 for key in citation_keys:
  if key in references:opened_inputs.append({'citation_key':key,'relation':'cited original input or explicit comparison; not by itself a match of the full receiving statement','source_opening_records':references[key]})
 elsewhere=[m for m in ms if m['baseline']=='elsewhere']
 eb=EBY[sid]
 item['found_elsewhere']={'status':'found_in_checked_scope' if elsewhere or opened_inputs else 'not_found_in_checked_scope','full_statement_found':any(m['relation'].startswith('full_known') for m in elsewhere),'matches':elsewhere,'cited_opened_inputs':opened_inputs,'additional_attached_search_record':'deliverables/work/cdp_audit/credit_elsewhere_searches_239.json#'+sid,'terms_searched':eb['terms_searched'],'corpus_size_files':len(ELSE['files']),'bounded_absence_statement':'Beyond the explicit positive matches and opened general inputs, no full counterpart was identified in the executed attached-source searches and stated context readings. This is not an exhaustive priority search of all literature.','existing_scoped_credit_notes':audit.get('credit_checks','')}
 full=[m for m in ms if m['relation'].startswith('full_known')]
 if full:
  item['novelty_classification']='known conclusion with complete credited re-derivation'
  item['route']='PaperI known re-derivation' if sid=='E9' else 'PaperII known re-derivation appendix'
  known.append({'source_id':sid,'title':audit['source_title'],'route':item['route'],'matches':full})
 elif any(m['relation']=='known_statement_repaired_and_strengthened' for m in ms):
  item['novelty_classification']='known assertion with a repaired complete proof and a distinct strengthening';item['route']='Main body: label correction and extension explicitly'
 elif ms:
  item['novelty_classification']='mixed: prior input or special case plus a distinct receiving conclusion';item['route']='Main body with precise partial credit; retain every distinct full proof'
 else:
  item['novelty_classification']='full counterpart not located in the bounded checked scope; no universal novelty claim';item['route']='Retain complete receiving result; identify classical inputs and avoid an unsupported priority claim'
 item['credited_to']='; '.join(m['baseline']+' — '+m['locator']+': '+m['comparison'] for m in ms)
 if not item['credited_to']:
  item['credited_to']=audit.get('credit_checks','') or 'Exact original inputs are recorded in found_elsewhere.cited_opened_inputs. No full prior counterpart identified in the specified bounded comparison.'
 if sid=='D.1.14':
  item['route']='PaperI group appendix: alias with FAM F1.1; full alternate exposition retained'
  item['novelty_classification']='same result/method already present in another supplied return; not a second theorem'
  item['credited_to']+=' Supplied FAM F1.1 proves the same index-twelve kernel theorem; F1.2 is a distinct presentation and is not conflated.'
 if sid in ['C.1.1','D.1.7']:
  item['classical_preliminary_note']='Elementary/classical preliminary or direct calculation; no claim of new general theory. A full exact named external counterpart was not identified by this comparison.'
 results.append(item)

assert len(results)==239 and len({x['source_id'] for x in results})==239
assert len(SEARCH)==956 and all(len([s for s in SEARCH if s['source_id']==x['source_id']])==4 for x in results)
(OUT/'credit_comparison_239.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
fields=['source_run','source_id','source_title','source_status','proof_sha256','reader','own_full_proof_check','proof_outcome','found_in_AC26','found_in_E26','found_in_DGKX_v1','found_in_DGKX_v2','found_elsewhere','credited_to','novelty_classification','route','independent_comparisons']
with (OUT/'credit_comparison_239.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows({k:json.dumps(r[k],ensure_ascii=False) if isinstance(r.get(k),(dict,list)) else r.get(k,'') for k in fields} for r in results)
(OUT/'known_rederivation_routing.json').write_text(json.dumps(known,ensure_ascii=False,indent=2)+'\n')
# Attach a concrete credit locator to each existing proof record, preserving its text.
for r in AUDIT:r['credit_matrix_record']='deliverables/work/cdp_audit/credit_comparison_239.json#'+r['source_id']
(OUT/'result_audit.json').write_text(json.dumps(AUDIT,ensure_ascii=False,indent=2)+'\n')
fields=list(dict.fromkeys(k for row in AUDIT for k in row))
with (OUT/'result_audit.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in r.items()} for r in AUDIT)
print('Saved239 per-result comparisons,956 baseline searches,239 other-source searches,',len(known),'known-result routes.')
