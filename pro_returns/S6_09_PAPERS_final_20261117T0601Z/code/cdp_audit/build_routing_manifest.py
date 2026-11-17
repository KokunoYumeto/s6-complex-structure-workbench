"""Prepare source-level routing, not a manuscript or a claim of completed audit."""
from pathlib import Path
import csv,json,re
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'deliverables/work/cdp_audit'
rows=json.loads((OUT/'result_audit.json').read_text())
groups=[
('01','Index, Picard components and endpoint cohomology',['C.1.1','C.1.2','C.1.3','E1','E2','E3']),
('02','Integral specialization, coherent restrictions and component counts',[
 'D.1.1','D.1.2','D.1.3','D.1.5','D.1.6','D.1.7','D.1.8','E4','D.1.9','D.1.10','D.1.11','D.1.12','D.1.4','D.1.13','D.1.15']),
('03','Complete smooth-fibre classification and actual Hopf occurrence',[
 'C.3.2','C.3.3','C.3.4','C.3.7','C.3.8','C.3.9','C.3.10','C.3.12','C.3.1','C.3.11','C.3.5','C.3.6']),
('04','Cotangent torsion, conductor and the printed endpoint error',[
 'A.1.1','A.2.1','A.2.2','A.1.2','A.2.4','A.2.5','A.2.6','B1','B2','B3',
 'A.3.1','A.3.2','A.3.3','A.3.4','A.3.5','A.4.1','A.4.2','A.4.3','A.4.4','A.4.5','A.4.6','A.4.7','A.4.8','A.4.9']),
('05','Normalization, conductor genus and local torus exclusions',[
 'A.5.1','A.5.2','A.5.3','A.5.4','A.5.6','A.5.9','A.5.11','A.5.12','A.5.13',
 'A.5.5','A.5.7','A.5.8','A.5.14','A.5.10','A.5.20','A.5.15','A.5.17','A.5.18','A.5.19','A.5.16','A.5.21']),
('06','Unrestricted Euler topology, component covers and semicomplete fields',[
 *[f'C.2.UN.{n}' for n in [1,2,3,4,14,15,16,17,19,20,22,23,26,28,29,31,33,36,38,39,44,47]]]),
('07','Irreducible and reducible torus-fibre Euler criteria',[
 'C.2.UN.5',*[f'C.2.CR.{n}' for n in range(1,7)],'C.2.UN.9','C.2.UN.10','C.2.IRR.1',
 *[f'C.2.VII.{n}' for n in range(1,5)],*[f'C.2.RAT.{n}' for n in [1,2,3,4,5,7,8,9]],
 'C.2.D4.1','C.2.D4.2','C.2.D4.3','C.2.UN.7','C.2.UN.12',
 *[f'C.2.INT.{n}' for n in range(1,4)],*[f'C.2.MH.{n}' for n in range(1,5)]]),
('08','Normal-crossing topology and canonical-flat component comparisons',[
 *[f'C.2.NC.{n}' for n in range(2,6)],'C2a','C2b','C2c','C2d','C.2.UN.11',
 'C.2.UN.24','C.2.UN.32','C.2.UN.64','C.2.UN.65','C.2.UN.66','C.2.UN.67','C.2.UN.68']),
('09','Compact occurrence of prescribed component classes',[
 *[f'C.2.UN.{n}' for n in [6,8,13,18,21,25,27,30,34,35,37,41,42,43,45]]]),
('10','Marked Hopf, ruled and elliptic supports with all multiplicities',[
 *[f'C.2.UN.{n}' for n in [40,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63]]]),
('11','Actual contractions, canonical reduction and finite generation',[
 *[f'C.2.UN.{n}' for n in [69,70,71,73,76,74,75,77,79,80,81,82,83,84,78,72,85,86]]]),
('12','Global CDP replacement and normalization resonance',[
 'C.2.G.1','C4a','C4b','C4c','C4d','C4e','C4f','C4g','C5a','C5b','C5c']),
('13','Constant-monodromy period comparison and compact examples',[
 'D.2.1','D.2.3','D.2.4','D.2.5','D.2.6','D.2.7','D.2.8','D.2.2']),
('14','Fibration stability and explicit deformation calculations',[
 'E5','E6','E7','E8','E10','E11','E12','E13','E14','E15','E16','E17','E18','E19']),
('A','Known source results re-derived in full',['A.2.3','C.2.NC.1','C.2.RAT.6']),
('I','Confirmed full-proof transfers and duplicate aliases in Paper I',['D.1.14','E9']),
]
mapping={}
for section,title,ids in groups:
 for pos,sid in enumerate(ids,1):
  assert sid not in mapping,sid
  mapping[sid]=(section,title,pos)
assert set(mapping)=={r['source_id'] for r in rows},(set(mapping)-{r['source_id'] for r in rows},{r['source_id'] for r in rows}-set(mapping))
known={
 'A.2.3':('Granger–Schulze2014 Theorems1.1/1.3','Normalization-residue criterion is known; retain the complete source derivation and exact hypotheses.'),
 'C.2.NC.1':('A-Campo1975 §2.2','Known local-to-global Euler formula; retain multiplicities, self-intersections and the full oriented-blowup proof.'),
 'C.2.RAT.6':('Arnold1976; Merle–Teissier1977; Steenbrink1989','Known analytic normal forms and spectrum/adjunction formulas; retain the exact delta<=5 enumeration and all suspension computations.'),
 'E9':('Supplied DGKX2026v1, p2:thm:tangent-cohomology and p2:thm:kuranishi-aut','Known original-family deformation result; parent confirmed full-proof inclusion in I under cdp:st:E9, shared with fam:A5.2.'),
}
duplicates={
 'D.1.14':('FAM F1.1','Confirmed same kernel method; merge the full alternate exposition in I, preserve source alias; not an independent F1.2 proof.'),
 'E9':('Paper I original-family tangent cohomology and Kuranishi theorem','Confirmed full-proof inclusion under cdp:st:E9, shared with fam:A5.2; complete argument preserved.'),
}
relations={
 'A.1.1':'WORKING prop:missing-cotangent-filtration; prop:missing-global-section-criterion; prop:filtration; prop:criterion',
 'A.2.2':'WORKING lem:conductor-square; prop:conductor; lem:conductor; prop:conductor-differential',
 'B1':'WORKING prop:nodal-counterexample; prop:family-geometry; lem:gluing-bundle; lem:extending-gluing; thm:nodal-test',
 'C.1.2':'WORKING lem:cdp-generic-endpoints; lem:generic-endpoints',
 'D.1.1':'WORKING lem:semidirect-abelianization; elementary coinvariant identity, printed CDP application is distinct',
 'E1':'PUSH E2.9 is related, not duplicate: Kähler general fibre versus all reduced fibres irreducible on complex S6',
 'E6':'PUSH E2.4–24 extends stability consequences; retain those distinct statements and proofs',
 'E15':'INV E2.1/E2.2 and the deformation question in E2.3; the remaining Km splitting question stays separate',
}
out=[]
for r in rows:
 sid=r['source_id'];section,title,pos=mapping[sid]
 path=ROOT/r['extracted_file'] if r['extracted_file'].startswith('deliverables/') else ROOT/'deliverables'/r['extracted_file']
 labels=re.findall(r'\\label\{([^}]+)\}',path.read_text())
 is_refuted=r['source_status'].startswith('Refuted')
 row={**r,'proposed_paper':'I' if section=='I' else 'II','proposed_section':section,'section_title':title,'section_local_order':pos,
      'source_labels':labels,'proposed_role':'counterexample with proved replacement' if is_refuted else 'known result with complete re-derivation' if sid in known else 'source result retained with complete proof',
      'duplicate_target':duplicates.get(sid,('',''))[0],'duplicate_decision':duplicates.get(sid,('','Retain separately; no exact duplicate determination made.'))[1],
      'related_sources':relations.get(sid,''),'known_credit':known.get(sid,('',''))[0],'known_proof_routing':known.get(sid,('',''))[1],
      'actual_proof_gap':'none recorded in the inspected argument' if r.get('own_check') else 'not assessed; proof audit pending',
      'completeness_warning':'A check record does not close the dependencies. Section order is an editorial proposal, not a certified topological dependency order.'}
 out.append(row)
order={g[0]:i for i,g in enumerate(groups)}
out.sort(key=lambda r:(order[r['proposed_section']],r['section_local_order']))
(OUT/'paperII_source_routing.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
with (OUT/'paperII_source_routing.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
supp=[]
for filename in ['working_edition_inventory.json','invariants_part_E_audit.json']:
 for r in json.loads((OUT/filename).read_text()):
  sid=r['source_id'];taken=r.get('taken_over_by','')
  if r.get('paper')=='I':section='I'
  elif filename.startswith('invariants'):section='14'
  elif any(x in sid for x in ['duality','flatness','base-change']):section='B'
  elif any(x in sid for x in ['picard','pic0','pic-restriction','leray-edge','candidate']):section='12'
  elif any(x in sid for x in ['corrected','generic-endpoints','comparison','relative']):section='12'
  else:section='04'
  supp.append({**r,'proposed_section':section,'merge_target':taken,
               'routing_instruction':'Preserve this exact label in the concordance; retain every distinct argument. Merge only the explicitly identified same-proof part.',
               'proof_gap_status':'see exact check_outcome and notes; no gap inferred merely from an open historical question'})
(OUT/'paperII_supplemental_routing.json').write_text(json.dumps(supp,ensure_ascii=False,indent=2)+'\n')
text=['# Proposed Paper II source and proof routing','',
      'This is an editorial manifest, not a manuscript. It includes all 239 CDP final-result rows, all 46 working-edition labels, and all five assigned INV Part E rows. Every CDP row carries its actual full-proof file and hash. Pending audit is not reported as a mathematical gap. The JSON and CSV carry the individual reading scopes and remaining dependencies.','',
      'The order below groups proofs by subject. Some cross-references must be moved or expanded when the final dependency order is set. No result is deleted because a stronger later theorem exists. A source-level counterexample is printed as a true counterexample/replacement assertion, never as its refuted proposition.','',
      '## Proposed order','']
for sec,title,ids in groups:text += [f'### {sec}. {title}','',', '.join(ids),'']
text += ['## Supplementary source placement','',
         'The working-edition analytic Cartier duality, curve flatness, cohomology-complex and top-base-change proofs form a separate foundational appendix B. Their historical source theorems are credited, and the complete derivations for the precise analytic hypotheses are preserved.','',
         'Working conormal/conductor and nodal-family proofs merge into the corresponding main statements only where the same proof is explicitly identified. The independent direct boundary-Picard argument, finite norm argument, local nonzero cusp example, and analytic Appell–Humbert/support-function proof all remain separate complete methods in section12.','',
         'INV E1.1 retains its precise anticanonical-pencil stability assertion in section14. INV E2.1/E2.2 merge only shared structure/tangent computations with CDP E15; their exact assertions and any additional Hodge/canonical claims remain. INV E2.3 is split into the deformation calculation answered by E15 and the still-open Km splitting calculation. INV E2.4 retains the exact failed dependence in the universal two-field bound, with HKP2000 credited.','',
         'PUSH E2.4–E2.24 and E5 were assigned to II by the parent. Full proof blocks supplied by the parent are deliverables/work/root/push_E2_stability_for_II.tex and push_E5_for_II.tex. They are additional sources outside the239-row count and require their own source aliases.','',
         '## Confirmed transfers to I','',
         '- D1.14: confirmed same kernel argument as FAM F1.1; parent included the full alternate exposition. Saved standalone block paperI_CDP_D1_14_group_proof.tex, standalone label prop:cdp-index-twelve, source label st:D.1.14.','- E9: parent confirmed the complete original-family tangent/Kuranishi proof in I under cdp:st:E9, shared with fam:A5.2.','- WORKING lem:semidirect-abelianization: the exact first lemma and its complete proof transfer to I under wb:lem:semidirect-abelianization. The following printed-CDP applications remain in II.','',
         '## Mathematical corrections and unresolved work','',
         '- A1.1: write the two section-vanishing assumptions explicitly. The complete corrected proof block is saved.','- A2.6: replace the false raw-module equality with the B-module generated by the differential image, B=C{t}, equal to t^4B dt. The raw R-module misses t^7 and t^8. The determinant valuation19−4=15 is unchanged.','- Kawai1969 Proposition2: the orbit sum of the selected divisor supplies the necessary finite-equivariant linearization. Keep this repair explicit. The later multiple-fibre corollary is not used.','- Remaining original-source openings and unread CDP rows are audit tasks, not established logical gaps. No additional mathematical gap is asserted merely because an external theorem has not yet been opened.','- The INV E2.3 Km splitting question remains an actual open calculation; do not let E15’s Kuranishi conclusion silently answer it.','',
         'All scope qualifications and exact pending dependencies remain in result_audit.json and references_verified.json.']
(OUT/'paperII_routing_manifest.md').write_text('\n'.join(text)+'\n')
print('Saved routing for',len(out),'CDP rows and',len(supp),'supplemental labels; no manuscript assembled.')
