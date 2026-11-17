"""Scoped attribution for 39 working/reader rows and two necessary inputs.

Preserves all prior proof checks.  This event reads the full statements and
compares exact contexts; it does not claim a second full carrier-proof audit.
"""
import csv,hashlib,json,re,shutil
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'deliverables/work/cdp_audit/carrier_credit'
META={'model':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17','timezone':'UTC','reader':'/root/cdp_audit'}
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
PLAN=json.loads((OUT/'search_plan_41.json').read_text())
SEARCH=json.loads((OUT/'searches_164.json').read_text())
BY={(r['source_id'],r['baseline']):r for r in SEARCH}
snap=json.loads((ROOT/'deliverables/work/cdp_audit/carrier_working_inventory_snapshot.json').read_text())
extra=json.loads((ROOT/'deliverables/work/cdp_audit/carrier_prerequisite_inventory_2.json').read_text())
inventory=list(csv.DictReader((ROOT/'deliverables/S6_09_PAPERS_inventory.csv').open()))
FIELDS=list(inventory[0]);assert len(FIELDS)==17
ORIG={(r['source_run'],r['source_id']):r for r in inventory}
ORIG.update({(r['source_run'],r['source_id']):r for r in snap+extra})
printed=(ROOT/'deliverables/S6_09_PAPERS_III.tex').read_text()

SCOPE={
 'cusp-cover-extension-theorem':'The scaled residual period C(v^N)/N, degree N^3 map to the original cusp, degree N^2 base-changed factor, exact nonflat double/triple loci, and marked deck lattice are the receiving calculations. The periodic toric cusp is a prior input; the toric monomial mechanism is classical.',
 'cusp-cover-naive-action-failure':'The two explicit equivariance factors differ before the residual action is corrected. This is a specific compatibility calculation, not a new general theorem about toric powers.',
 'cusp-cover-global-scope':'The full-monodromy failure of the displayed sublattice is a marked matrix check. Local Kummer construction is not an asserted global cover or sphere construction.',
 'cusp-spec-globalization-obstruction':'Engel already gives the invariant covector and regular circle-quotient idea. The exact marked metric, minimal-copy statement, finite target gluing, and literal cusp nonextension must be separated from Engel’s defective literal-extension sentence. Cartesian-product/smash dimensions and almost-complex obstructions are classical inputs.',
 'cusp-cone-native-descent':'The trivial rank-two cusp quotient follows from the existing image/kernel monodromy lattice; the receiving lemma writes the actual flat map, integral kernel and radial isometry. It is an explicit application to the marked family.',
 'cusp-cone-S12-route':'The localized retained-angle quotient, exact radial restriction and target are specified constructions. Sphere smash identities, suspension homology and the Kunneth computation are classical; no matching full marked construction was found in the compared contexts.',
 'cusp-cone-S24-local-route':'The localized circle quotient is an application of the known invariant character. Its compactified map and full smash-target homology are explicit receiving constructions using classical suspension and product formulas.',
 'cusp-cone-S24-route':'The finite Seifert pieces originate in the existing torus construction and Engel’s circle-quotient idea. The coned target, its actual glued map and integral relative homology are the receiving construction; no literal global flat extension is asserted.',
 'cusp-cone-target-slice-embeddings':'This is a definition of three explicit slice embeddings. Their compact-to-Hausdorff injectivity argument is standard point-set topology, not a separate novelty claim.',
 'cusp-cone-metric-scope':'Uniform collapse at a cone endpoint and boundedness of a compatible compact metric are classical topological facts. The exact intrinsic systolic growth is the marked period calculation; the combined scope statement concerns these particular slices.',
 'cusp-cone-S12-almost-complex-obstruction':'The entire nonexistence conclusion, including all smooth structures on the topological sphere, is classical Borel–Serre. Retain all three complete distinct proofs with explicit credit: reduced powers, Bott integrality, and the standard-sphere Pontryagin calculation.',
 'cusp-cone-obstructions':'Mixed result: marked invariant-kernel/finite-cover and fixed-target restrictions are receiving applications. Product/smash/join identities, covering-space triviality for simply connected sources, and Borel–Serre sphere obstructions are classical components and must be credited accordingly.',
 'cusp-cone-optimal-exponents':'The ranks2r and r are the explicit bounded-lattice and full-monodromy restrictions for this native quotient class. The statement expressly does not optimize arbitrary continuous quotients or rescaled metrics.',
 'cusp-cone-angle-forgotten-sphere-carriers':'The exact angle-forgetting maps, all collapsed loci, moving embedded spheres and onto-ball quotient metrics are specific constructions. Reduced suspension, torus CW quotients and sphere smashes are classical ingredients.',
 'cusp-cone-S12-sphere-map-null':'The square vanishing is a formal consequence of the fully printed universal S6-to-S3 smash pairing, itself derived from published low homotopy groups. The application to the particular surjective representative is separate from its point-set data.',
 'cusp-cone-S24-sphere-map-null':'The original proof is a classical low-stem deduction: the sixfold suspension lies in pi12(S8)=pi4S=0, hence its smash square and every higher power vanish. Preserve this proof even after the stronger actual one-copy extension homotopy.',
 'cusp-cone-literal-R4-open-cells':'The open-cell identifications and compact-metric obstruction are standard topology applied to the explicitly embedded moving spheres. Exact radial ball claims use the separately proved quotient metrics.',
 'cusp-cone-moving-S4-null-homotopy':'Sliding a reduced-suspension slice to the endpoint is the complete elementary classical homotopy. It concerns the inclusion of the moving sphere, not the full specified carrier map.',
 'cusp-cone-sphere-map-homotopy-status':'This is a scope/consequence record. The original circle one-copy open sentence is superseded by the complete writing-stage extension homotopy; the rank-two framed proof and older independent smash arguments remain distinct.',
 'cusp-cone-explicit-carriers':'The explicit diagonal-height embeddings identify Cone(T4) in the actual targets. Cone local homology and the local homology-manifold test are classical; the specified placement and radial restrictions are receiving data.',
 'cusp-cone-target-homotopy-types':'Suspension-of-product splitting, smash distribution, relative Hurewicz and homological Whitehead are classical. The concrete Seifert presentation, integral homology and multiplicities determine these particular target homotopy types.',
 'cusp-cone-exact-decompactification-space':'The exact varying-lattice quotient with Euclidean boundary, Hausdorff/chart proof and nonquotient comparison-map topology are specific receiving constructions. No full matching statement was found by the bounded queries.',
 'cusp-cone-sharp-global-R4-scope':'This is a synthesis of the proved open-cell, intrinsic metric and boundary-fibre constructions, with the classical compactness obstruction for continuous images and fixed metrics.',
 'cusp-s12-full-carrier-null':'Classical low-dimensional calculation: factor x smash y through the stable three-stem, use the even image from an order12 source and the exponent2 target. Published inputs are exact low homotopy groups; no literal previously printed pairing theorem is claimed to have been found.',
 'cusp-s12-all-higher-smashes-null':'A full elementary corollary of the preceding external-pairing calculation: smash a based nullhomotopy with the remaining factors. It is presented as a classical derivation, not a new general smash-product theorem.',
 'cusp-s12-one-copy-invariant':'The injective suspension into the even subgroup of the three-stem is classical and explicitly in Hatcher. The particular marked inverse torus and its actual zero coefficient use the receiving geometric nullbordism; an unframed T3 alone is not that computation.',
 'cusp-s12-nullity-scope':'This distinguishes a sphere-valued postcomposition from a different conical-target map. It is a logical scope statement about the specific maps, not a general new homotopy theorem.',
 'cusp-null:thm':'The exact map and its complete three-framed inverse torus/cap calculation are specific receiving data. Milnor’s Pontryagin–Thom and relative constructions are known tools, and the original cusp and zero-section disc are prior inputs.',
 'cusp_s12_carrier_homotopy:L567':'The zero coefficient, zero suspension and zero marked-character composite are complete formal consequences of the particular one-copy nullhomotopy. Do not infer a different target’s nullity.',
 'G2-8':'The fixed-orientation almost-complex homotopy conclusion is already explicitly stated in AC26 Section1.4 p7. The reader note’s tentative absence claim is false. The complete SU4/CP3, twisted-section extension and bundle-ODE argument is a classical expanded proof, with orientation carefully fixed.',
 'carrier-real-periods':'Necessary marked real-period and dual-lattice computation, separated from the excluded spectral assertions. The literal complex periods are prior construction inputs; inversion and lattice duality are classical linear algebra.',
 'carrier-native-quotient':'Necessary compact real quotient and integral kernel calculation. Projection of the explicit marked periods, the singular-value lower bound and onto-ball isometry provide the full nonspectral geometric proof.',
 'sphere-metric-uniform-collapse':'Classical uniform-continuity consequence of the compact cone parametrization: all shrinking-height slices approach the common quotient point for every fixed compatible metric. Its particular three target names are application data.',
 'sphere-metric-fixed-realization':'Specific fixed conic metrics are constructed on the actual compact targets. Exact first fundamental forms, controlled shortcuts and regular-stratum coordinate blowups distinguish vertical R4 limits from ambient R8/R12 limits; no matching construction was found in the baselines.',
 'sphere-metric-scaling-trichotomy':'Specific scalar rescaling analysis of the proved marked flat slices and conic targets. The point/square-torus/Euclidean regimes and ambient dimension statements use the exact metrics; general metric scaling is classical.',
 'sphere-metric-unit-volume':'Direct classical covolume calculation applied to the marked matrices: determinant normalization produces the square flat four-torus. It is a complete consequence of the period limit, not a new general volume principle.',
 'sphere-metric-tangent-scope':'Cones, joins, local homology and compact blow-down diameter are classical tools. The actual links and complete integral local groups of these specific smash targets are the receiving calculations; topology alone does not choose a metric tangent.',
 'h24:ret:chart-lemma':'The whole regular inverse image is placed injectively in one original toric coordinate neighbourhood by the literal holomorphic-unit change. The period model is known; the exact complete native inverse-torus formula is a detailed receiving step of MAPS B3.1.',
 'h24:ret:orientation-lemma':'This is the exact determinant and orientation comparison for the actual normal four-frame and tangent two-frame, a detailed receiving calculation in MAPS B3.1. General orientation conventions are classical.',
 'h24:ret:framing-proposition':'The actual differential frame is explicitly contracted to the Lie framing, with its orientation sign retained. Pontryagin–Thom, spin and framed bordism are classical inputs; the particular frame comparison is a receiving step of MAPS B3.1. Its additional external-source openings remain separately owned by invariants_arithmetic.',
 'h24:ret:q2-detected-quotient':'The exact quotient by the postcomposition kernel is the elementary first-isomorphism theorem applied to the proved nonzero MAPS B3.1 class in pi6(S4)=Z/2. The particular detected quotient and odd-multiple conclusion are an explicit corollary; no full order or splitting is inferred.'}
assert set(SCOPE)=={r['source_id'] for r in PLAN}

contexts={
 'AC26':{'source':'sources/original/AC26_original_manuscript.pdf','sha256':sha(ROOT/'sources/original/AC26_original_manuscript.pdf'),
  'own_new_opening':'Original p7 Section1.4, entire paragraph visually read; expressly states fixed-orientation almost-complex connectedness and the only almost-complex even spheres. Exact statement match for G2-8 and the S12 exclusion.',
  'prior_scopes':'work/cdp_audit/credit_context_readings.json and work/maps_audit/source_credit_checks.json; original toric cusp Lemmas4.2–4.3, Theorem4.5, Propositions4.6–4.7; zero-section disc Corollary4.8 p30; topology Theorems7.17/7.22 and8.1.',
  'limit':'The p7 paragraph states the classical homotopy fact but does not supply the full twistor-bundle proof. Its complete expanded proof is retained. Other prior contexts retain their original reading ownership; no complete rereading of the source is asserted.'},
 'E26':{'source':'sources/papers/arXiv_2609.38442_Engel_src/S6.tex',
  'own_new_opening':'Lines842–863: Lemma3.8 invariant covector and following finite action; lines1685–1736: full Remark8.3 quotient discussion and following indefinite-period remark.',
  'match':'The invariant covector and regular circle quotient are prior. The literal cusp-extension sentence in Remark8.3 is not used as a theorem: the complete actual-map nonextension proof is retained and credited as a correction.',
  'limit':'No exact smash-carrier, marked quotient metric or fixed-metric bubble theorem was identified in the queried/read contexts.'},
 'DGKX_v1':{'source':'sources/papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie_src/v5oka_maps_modifications_deformations.tex',
  'own_new_opening':'Lines1425–1502, full periodic-conical-fan statement/printed proof and q=z0z1z2 charts; lines12040–12218, complete construction comparison including invariant character, cusp quotient lattice and residual toric action.',
  'match':'Known marked sphere-family, fan, finite fillings and cusp input, explicitly credited there to AC26. These supply the receiving construction’s input, not the new carrier conclusions.',
  'limit':'No claim of a full new reading of all v1 proofs.'},
 'DGKX_v2':{'source':'sources/papers/arXiv_2610.00250v2_Du_Guo_Kusakabe_Xie_src/submited-tams.tex',
  'own_new_opening':'Lines1125–1202, full periodic-conical-fan statement/printed proof and chart formula; lines3130–3304, complete construction-comparison scope including the marked lattice and toric residual action.',
  'match':'Same explicitly credited underlying sphere/toric construction inputs checked separately in this edition. No carrier or fixed-metric result is silently imported from v1.',
  'limit':'Whole-file queries are saved separately; neither the entire source nor all broad hit contexts are claimed read.'}}
for b,c in contexts.items():
 if 'sha256' not in c:c['sha256']=sha(ROOT/c['source'])
write(OUT/'context_readings.json',{'reader':META,'contexts':contexts,'method':'164 executed result/baseline searches, full receiving statements and these explicit source contexts. Negative comparisons are bounded and do not establish global novelty.'})
visual=ROOT/'reference_downloads/carrier_credit';visual.mkdir(parents=True,exist_ok=True)
if Path('/tmp/cdp_AC26_p7.png').exists():shutil.copyfile('/tmp/cdp_AC26_p7.png',visual/'AC26_p7.png')
write(OUT/'AC26_G2_positive_match.json',{'reader':META,'status':'verified in the specified scope','key':'AC26Root','source':contexts['AC26']['source'],'sha256':contexts['AC26']['sha256'],'locator':'Section1.4, original printed p7, first paragraph','visual':'reference_downloads/carrier_credit/AC26_p7.png','match':'The fixed-orientation almost-complex connectedness statement is expressly present, as is the restriction of almost-complex even spheres to S2 and S6. G2-8 absence wording is corrected; the complete classical proof is retained.','limit':'This is an attribution/statement check, not an assertion that this introductory paragraph contains the expanded proof.'})

REF=json.loads((ROOT/'deliverables/work/maps_audit/carrier_source_checks.json').read_text())
REF={r['key']:r for r in REF}
specific={
 'cusp-cone-S12-almost-complex-obstruction':['BorelSerre1953','Husemoller1994','KonstantisParton2018'],
 'cusp-spec-globalization-obstruction':['BorelSerre1953'],
 'cusp-cone-obstructions':['BorelSerre1953'],
 'cusp-cone-S12-sphere-map-null':['Hatcher2002','IsaksenWangXu2023'],
 'cusp-cone-S24-sphere-map-null':['Hatcher2002','IsaksenWangXu2023'],
 'cusp-s12-full-carrier-null':['Hatcher2002','IsaksenWangXu2023'],
 'cusp-s12-all-higher-smashes-null':['Hatcher2002','IsaksenWangXu2023'],
 'cusp-s12-one-copy-invariant':['HatcherSpectralSequences','CuspNullMilnor1965'],
 'cusp-null:thm':['CuspNullMilnor1965'],
 'cusp_s12_carrier_homotopy:L567':['HatcherSpectralSequences','CuspNullMilnor1965']}
PURE={'G2-8','cusp-cone-S12-almost-complex-obstruction','cusp-s12-full-carrier-null','cusp-s12-all-higher-smashes-null'}
CLASSICAL={'cusp-cone-moving-S4-null-homotopy','cusp-s12-full-carrier-null','cusp-s12-all-higher-smashes-null','sphere-metric-uniform-collapse','sphere-metric-unit-volume'}

def statement_now(label,fallback):
 needle='\\label{'+label+'}'
 if needle not in printed:return fallback
 pos=printed.index(needle)
 starts=list(re.finditer(r'\\begin\{(theorem|proposition|lemma|corollary|remark|definition)\}',printed[:pos]))
 if not starts:return fallback
 m=starts[-1];end=printed.index('\\end{'+m[1]+'}',pos)+len('\\end{'+m[1]+'}')
 return printed[m.start():end]

rich=[];overlays=[]
for p in PLAN:
 sid=p['source_id'];run=p['source_run'];label='mapsaudit:almost-complex-homotopy' if sid=='G2-8' else ('mapsIII:carrier-real-periods' if sid=='carrier-real-periods' else 'wb:cusp-spec-native-quotient' if sid=='carrier-native-quotient' else 'wb:'+sid)
 r={'source_run':run,'source_id':sid,'source_file':p['source_file'],'source_sha256':p['source_sha256'],'printed_label':label,
    'comparison_reader':META,'statement_reading':'Every word of the original receiving statement was read for this comparison; corrected/current statement also compared where already placed.',
    'original_statement':p['original_statement'],'current_statement':statement_now(label,p['original_statement']),
    'substantive_comparison':SCOPE[sid], 'receiving_full_proof_scope':'Use the retained prior full receiving-check event; this credit-only record does not claim a second full proof reading.',
    'prior_full_check_record':'deliverables/work/maps_audit/check_events.json; working_carrier_full_checks.json'}
 if sid.startswith('sphere-metric-'):
  r['prior_full_check_record']='deliverables/work/root/late_carrier_full_reading.json: /root completed every source line1–917. This attribution event does not claim a second full proof reading.'
 if sid.startswith('h24:ret:'):
  r['prior_full_check_record']='deliverables/work/root/late_carrier_full_reading.json: /root completed every in-scope source line4378–5111. First three exact support labels added by the assembler; main theorem shared with MAPS B3.1. Additional original-source gate remains separate.'
 if sid.startswith('carrier-'):
  r['prior_full_check_record']='deliverables/work/cdp_audit/carrier_integration_audit.json, including own complete proof reading and separate parent complete receiving review.'
 positives=[]
 for b in ['AC26','E26','DGKX_v1','DGKX_v2']:
  full=b=='AC26' and sid in ['G2-8','cusp-cone-S12-almost-complex-obstruction']
  partial=sid not in PURE
  if full:
   locator='Original Section1.4, printed p7, first paragraph (controlling PDF visually reopened).'
   relation='The full main classical conclusion is explicitly stated; the expanded independent proof is not contained in that introductory paragraph.'
  elif partial:
   locator={'AC26':'Original Lemmas4.2–4.3, Theorem4.5, Propositions4.6–4.7 and Corollary4.8 p30; sphere recognition Theorem8.1. Prior exact full-read scopes retained.',
            'E26':'Original torus/sphere construction; Lemma3.8 (source842–850) and Remark8.3 (1685–1723) for the invariant-circle antecedent.',
            'DGKX_v1':'Periodic-conical-fan proposition, source1425–1502; construction comparison12040–12218.',
            'DGKX_v2':'Periodic-conical-fan proposition, source1125–1202; construction comparison3130–3304.'}[b]
   relation='Known underlying marked complex torus/sphere family and cusp/finite-fillings data only. '+SCOPE[sid]
  else:
   locator='No full matching statement located in the specified query/context scope.'
   relation='No full-statement match in these bounded searches and actual context readings; this is not a global novelty assertion.'
  scan=BY[(sid,b)]
  r['found_in_'+b]={'status':'full_main_conclusion_found' if full else 'known_construction_input_found' if partial else 'not_found_in_scoped_comparison',
    'full_statement_found':full,'locator':locator,'relation':relation,'terms_searched':scan['terms_searched'],
    'search_record':'deliverables/work/cdp_audit/carrier_credit/searches_164.json#'+sid+'|'+b,
    'searched_file':scan['source'],'searched_sha256':scan['source_sha256'],'hit_count':len(scan['matches']),
    'context_record':'deliverables/work/cdp_audit/carrier_credit/context_readings.json#'+b}
  if full or partial:positives.append(b+': '+locator+' '+relation)
 opened=[]
 for k in specific.get(sid,[]):
  source=REF[k]
  opened.append({'key':k,'locators':source['opened_locators'],'scope':source['verification_scope'],
                 'source_reader_record':'deliverables/work/maps_audit/carrier_source_checks.json#'+k,
                 'reader_scope':'The named prior reader opened and matched this original. This event reuses that exact scope, not a new full-source reading.'})
 full_else=sid=='cusp-cone-S12-almost-complex-obstruction'
 r['found_elsewhere']={'status':'full_classical_conclusion_found' if full_else else 'opened_classical_inputs_found' if opened else 'standard_methods_with_complete_receiving_derivation',
     'full_statement_found':full_else,'opened_originals':opened,
     'method_scope':SCOPE[sid],
     'limits':'Only named originals and the four attached baselines were compared; no exhaustive worldwide search is claimed. A formal classical deduction is not silently represented as an identical theorem in the cited source.'}
 if sid in ['G2-8','cusp-cone-S12-almost-complex-obstruction']:
  r['route']='Known source-results appendix; retain the entire statement and every distinct complete proof with explicit original credit.'
  r['novelty_classification']='Wholly known main conclusion; full expanded derivation retained.'
 elif sid in CLASSICAL:
  r['route']='Retain as an explicitly classical complete derivation/application. No exact full-statement publication is claimed from the bounded search.'
  r['novelty_classification']='Classical calculation or formal consequence; no novelty assertion.'
 elif sid=='cusp-cone-target-slice-embeddings':
  r['route']='Retain the definition and complete embedding argument with the constructions.';r['novelty_classification']='Definition; no theorem-priority claim.'
 else:
  r['route']='Retain the complete marked construction/proof and credit each specified known ingredient.'
  r['novelty_classification']='No full matching receiving statement found in the bounded comparison; no worldwide novelty conclusion.'
 r['credited_to']=' '.join(positives+[k+': '+', '.join(REF[k]['opened_locators']) for k in specific.get(sid,[])])
 r['all_searches_completed']=True
 rich.append(r)
 prior=ORIG.get((run,sid),{})
 row={k:prior.get(k,'') for k in FIELDS}
 row.update(source_run=run,source_id=sid,source_file=p['source_file'],paper='III',printed_label=label,
            statement_as_printed=r['current_statement'])
 if not row['kind']:
  mm=re.search(r'\\begin\{([^}]+)\}',p['original_statement']);row['kind']=mm[1] if mm else 'classical corollary'
 for b in ['AC26','E26','DGKX_v1']:row['found_in_'+b]=json.dumps(r['found_in_'+b],ensure_ascii=False)
 row['found_elsewhere']=json.dumps({'elsewhere':r['found_elsewhere'],'DGKX_v2':r['found_in_DGKX_v2']},ensure_ascii=False)
 row['credited_to']=r['credited_to']
 row['notes']=(row['notes']+' | '+r['route']+' '+r['novelty_classification']+' Detailed bounded credit record: work/cdp_audit/carrier_credit/working_credit_39.json#'+sid if run!='WRITING_REPAIR' else row['notes']+' | '+r['route']+' Detailed credit: work/cdp_audit/carrier_credit/prerequisite_credit_2.json#'+sid).strip(' |')
 row['your_check']=(row['your_check']+' | Credit comparison only, GPT-6 Astra (OpenAI, ChatGPT Pro mode), effort Pro,17 November2026UTC, /root/cdp_audit: complete statement read; four actual source searches and positive contexts matched; prior full-proof scope preserved.').strip(' |')
 if sid=='G2-8':row['wording_vs_source']+=' The original tentative claim of absence from AC26 is corrected: Section1.4 p7 explicitly states the main conclusion.'
 if sid=='cusp-cone-sphere-map-homotopy-status':row['wording_vs_source']+=' Obsolete open circle-class sentence replaced at its original use by the full extension-homotopy result; original historical wording retained only in audit.'
 overlays.append(row)

working=[r for r in rich if r['source_run']!='WRITING_REPAIR'];prereq=[r for r in rich if r['source_run']=='WRITING_REPAIR']
assert len(working)==39 and len(prereq)==2
write(OUT/'working_credit_39.json',working);write(OUT/'prerequisite_credit_2.json',prereq)
for name,rs in [('working_credit_inventory_overlay_39',[r for r in overlays if r['source_run']!='WRITING_REPAIR']),('prerequisite_credit_inventory_overlay_2',[r for r in overlays if r['source_run']=='WRITING_REPAIR'])]:
 write(OUT/(name+'.json'),rs)
 with (OUT/(name+'.csv')).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader();w.writerows(rs)
write(OUT/'known_routing.json',[{'source_id':r['source_id'],'printed_label':r['printed_label'],'route':r['route'],'main_positive':r['found_in_AC26'],'elsewhere':r['found_elsewhere']} for r in working if r['source_id'] in ['G2-8','cusp-cone-S12-almost-complex-obstruction']])
write(OUT/'comparison_summary.json',{'reader':META,'working_rows':39,'prerequisite_rows':2,'executed_searches':164,
 'full_main_conclusions_found':['G2-8: AC26 §1.4 p7','cusp-cone-S12-almost-complex-obstruction: Borel–Serre §15 Proposition15.1 p434; also stated AC26 §1.4 p7'],
 'source_correction':'G2 reader note’s tentative not-in-AC26 claim is false; corrected after visual opening of original p7.',
 'proof_scope':'Complete prior receiving proofs remain credited to their actual reader. Only exact repair contexts, helper proofs and G2 supplementary proof were independently reread here; all39 statement texts were read for attribution.',
 'limits':'No full new reading of every source proof or all baseline hit contexts; no worldwide absence or novelty assertion.'})
print('Saved39 working/G2 attribution rows, two prerequisite rows, exact17-column overlays,164 searches and two positive known-result routes.')
