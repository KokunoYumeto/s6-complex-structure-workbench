from pathlib import Path
import re,json,hashlib,csv
O=Path('deliverables/work/maps_audit')
prov={'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17'}
base={
 'AC26':Path('sources/original/AC26_transcription.tex'),
 'E26':Path('sources/papers/arXiv_2609.38442_Engel_src/S6.tex'),
 'DGKX_v1':Path('sources/papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie.tex'),
 'DGKX_v2':Path('sources/papers/arXiv_2610.00250v2_Du_Guo_Kusakabe_Xie.tex')}
terms={
 'circle':['circle','rank 3','rank-three','Seifert','torus-knot','solid torus','character','fixed locus'],
 'real':['antiholom','anti-holom','real structure','real form','complex conjug','fixed real','real locus','involution'],
 'specialization':['specialization','specialisation','nearby','invariant','Gysin','finite index'],
 'leray':['Leray','transgression','12\\gamma','12\\psi','cohomology','coinvariant'],
 'collapse':['collapse','honeycomb','spine','retract','cellular','Mayer','Wang'],
 'pi1':['fundamental group','van Kampen','12\\ell','meridian','peripheral'],
 'sphere':['Hurewicz','Whitehead','homotopy','homology sphere','diffeomorphic','cohomology'],
 'construction':['period','torsor','toric','finite filling','logarithmic','normalisation','normalization','product of two elliptic','normal bundle','admissible']}
evidence={}
for group,queries in terms.items():
 evidence[group]={}
 for key,p in base.items():
  lines=p.read_text().splitlines();hits=[]
  for n,l in enumerate(lines,1):
   matched=[q for q in queries if q.casefold() in l.casefold()]
   if matched:hits.append({'line':n,'queries':matched,'excerpt':l[:480]})
  evidence[group][key]={'file':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'scope':'Complete attached source file searched literally, case-insensitively; relevant named sections and hits inspected as stated per result. AC26 PDF is controlling, with original-PDF statement matches retained separately.','queries':queries,'match_count':len(hits),'hits':hits}
(O/'credit_baseline_searches_I.json').write_text(json.dumps(evidence,indent=2)+'\n')
# Every comparison describes the exact strength of the overlap, not a universal novelty decision.
AC_TOPO={
 'thm:p0-integral-specialization':'Found: AC26 Proposition 7.12 and Appendix B, Theorem B.1 and Remarks B.2/B.4: integral injectivity and image equal to monodromy invariants in all degrees used here. Our complete nearby-cycle proof is a rederivation.',
 'prop:leray-e2':'Found: AC26 Lemma 7.25 and Proposition 7.26: actual specialization subsheaves, integral invariant/coinvariant groups and the required E2 terms.',
 'lem:first-transgression':'Found: AC26 Proposition 7.27: the first integral transgression from the actual finite lifts and toric meridian.',
 'lem:higher-transgressions':'Found: AC26 Proposition 7.27: multiplicativity and the two exterior identities force both higher integral coefficients.',
 'thm:h2-vanishing':'Found: AC26 Corollary 7.29 and its proof: vanishing of H1,H2,H3 in cohomology and torsion removal for H2 in homology.',
 'prop:geometric-pi1':'Found: AC26 Lemmas 7.4/7.16 and Theorem 7.17: the actual based meridians, common sign and cyclic group of order |12 l0-4 l1-3 l2|.',
 'cor:candidate-sphere':'Found: AC26 Theorem 8.1 and Lemma 8.2, with the Chern/Euler conclusion in the main theorem: underlying standard S6 and c3=2.',
 'prop:topological-spine':'Found in the relevant construction: AC26 section 7.2, Lemmas 7.5–7.10 supply the equivariant deformation-retraction route. The abstract cofibration/weak-equivalence argument is classical; our full explicit proof is retained.',
 'lem:collapse-straightening':'Found: AC26 section 7.2, Lemmas 7.5–7.10, the twist-straightening and positive toric quotient construction; expanded formula proof retained.',
 'lem:positive-collapse':'Found: AC26 section 7.2, Lemmas 7.5–7.10, positive quotient, honeycomb and compact spine; expanded proof retained.',
 'lem:phase-spread-collapse':'Found: AC26 section 7.2, Lemmas 7.5–7.10, phase-equivariant spreading and descent of the retraction; full comparison retained.',
 'prop:verified-cellular-collapse':'Found: AC26 Proposition 7.12 with section 7.2: the fixed-fibre cellular collapse and its geometric generators. Our explicit cell-matrix presentation is retained as a rederivation.',
 'prop:verified-collapse-homology':'Found: AC26 Propositions 7.11–7.12: integral homology and collapse kernel/image. Our displayed integer matrices make the same primitive-lattice computation explicit.',
 'thm:collapse-equals-specialization':'Found: AC26 Proposition 7.12 and Appendix B, Remarks B.2/B.4: the collapse pullback is analytic specialization. Our actual homotopy comparison is printed in full.',
 'topology_reduction:L600':'Audit record rather than a new theorem. Underlying claims found in AC26 section 7.2, Propositions 7.11–7.12 and Appendix B; the listed falsifier checks are our verification record.',
 'record:vankampen':'Found: AC26 Lemma 7.4, section 7.5 and Theorem 7.17: actual based inclusions and van Kampen relations.',
 'prop:actual-finite-band-maps':'Found for the underlying maps and lattices: AC26 Lemma 7.19 and Proposition 7.14. The false assertion alpha3=alpha1 is WORKING-EDITION ONLY, not an AC26 error; its replacement uses the degree-three indices 1 and 2 already correctly given in AC26.',
 'prop:cusp-mv-blocks':'Found: AC26 Lemma 7.18, Theorem 7.22 and Remark 7.23: cusp kernels and the two-stage Mayer–Vietoris argument. Explicit primitive bases and maps are retained.',
 'topology_reduction:L920':'Found at the level of the integral H1 conclusion and meridian relations: AC26 Theorem 7.17. The one-shot matrix is our explicit rederivation/check of those relations.',
 'thm:mv-leray-comparison':'Partial found: AC26 Remark 7.24 and Proposition 7.27 expressly give both routes and their common obstruction p. The complete named chain-level commuting comparison is expanded here; no new sphere theorem is claimed.',
 'topology_reduction:L1113':'Audit record rather than a new theorem. The checked homology/fundamental-group conclusions are AC26 Theorems 7.17/7.22 and Corollary 7.29; our resolved-falsifier list is retained as a check record.',
 'lem:cohomological-closure':'Found: the integral UCT/PD deduction is in AC26 Corollary 7.29 and the context of Lemma 8.2; the general six-dimensional lemma is a classical rederivation.',
 'thm:sphere-recognition':'Found: AC26 Theorem 8.1 and Lemma 8.2 use precisely the integral homology/fundamental-group recognition route, followed by Smale and Kervaire–Milnor.',
 'cor:abstract-s6':'Found as the same classical conditional recognition implication used in AC26 Theorem 8.1/Lemma 8.2. No new general recognition theorem is claimed.',
 'cor:candidate-mv-sphere':'Found: AC26 Theorem 7.22 and Theorem 8.1: the alternate Mayer–Vietoris sphere conclusion.'}
AC_CON={
'lem:triangle-generator-orientations':'Partial found: AC26 Lemma 2.10 and Proposition 2.11 impose the same simultaneous generator convention. Our proof explicitly excludes mixed signs by traces.',
'prop:period-input-audit':'Found: AC26 Theorem 3.4 and sections 3.1–3.6; the full period/torsor/nondegeneracy construction is rederived.',
'prop:period-exact-admissible-constants':'Partial found: AC26 Theorem 3.4(iv), Proposition 3.15 and their invariant D argument give admissibility by adding a negative imaginary constant. The attained-maximum formulation and exact threshold are explicit here.',
'lem:toric-chart-control':'Found exactly in scope: AC26 Lemma 4.4 uses restricted polydiscs and the same logarithmic barycentric inequalities. The unrestricted-chart error belongs only to a different working Kummer block.',
'thm:candidate-cusp-geometry':'Found: AC26 Lemmas 4.2–4.4, Theorem 4.5, Proposition 4.6: action, quotient, properness, local equations, normalization and double/triple strata.',
'prop:candidate-cusp-overlap':'Found: AC26 Proposition 4.7 gives the actual exponentiation quotient and marked punctured biholomorphism.',
'lem:middle-period-proper':'Found: AC26 section 3.6, Proposition 3.19 and the construction of the middle period family; the compact-base lattice/properness details are expanded here.',
'prop:candidate-finite-fillings':'Found: AC26 Theorem 5.4 and Proposition 5.6 give the exact free affine cyclic fillings and fibre multiplicities.',
'lem:finite-filling-stalk-map':'Found: AC26 Lemma 7.3(i), Proposition 7.14 and finite-filling description: radial retraction and specialization equal to covering pullback.',
'thm:candidate-global-geometry':'Found: AC26 Construction 6.1 and Theorem 6.2: compact Hausdorff global threefold and exact exceptional fibres.',
'prop:monodromy-certificate':'Found: AC26 Lemmas 2.2/2.4 give the identical marked matrices, orders, cusp nilpotence and relation.',
'thm:cusp-lattices':'Found: AC26 Lemmas 2.6/2.7 and Appendix A, Lemma A.1 give the integral cusp and exterior-power lattices.',
'thm:coinvariants':'Found: AC26 Lemma 2.7, Appendix A and Proposition 7.26 give the global invariant/coinvariant groups; explicit Smith certificates are retained.',
'prop:finite-indices':'Found: AC26 Proposition 7.14 gives indices (3,1,1,3) and (4,2,2,4), including the conditional degree-three generator hypothesis. The source hypothesis is retained.',
'prop:terminal-group':'Found: AC26 Theorem 7.17 gives the same nonabelian presentation, abelian reduction and determinant.',
'prop:terminal-degree-two':'Found: AC26 Lemma 7.19(c), Remark 7.20 and Theorem 7.22 give the primitive degree-two image and obstruction. Explicit minors are a rederivation.',
'prop:terminal-all-degree':'Found: AC26 Theorems 7.22/8.1 and Corollary 7.29; this is a conditional expanded package, not a new sphere recognition result.',
'ffcert:prop:integral-summands':'Partial found: AC26 Lemma 2.6 and Lemma 5.7(i) give the fixed/moving decomposition and rational product. Our complete integral bases and indices 3,2 are explicit certificates.',
'ffcert:thm:product-covers':'Partial found: AC26 Theorem 5.4(iii), Lemma 5.7(i) and its proof identify the bielliptic quotient types and product isogeny. The exact unchanged period maps, kernel enumeration and degrees 9,8 are expanded here.',
'ffcert:prop:quotient-charts':'Found in underlying geometry: AC26 Theorem 5.4 and Proposition 5.6 give the same free cyclic local quotient. The product-coordinate presentation is our expanded certificate.',
'ffcert:thm:normalization':'Partial found: AC26 Theorem 5.4 gives the finite root chart and cyclic action. No corresponding full all-branches normalized base-change statement located in the inspected sections 5–7; it is proved explicitly here.',
'ffcert:thm:peripheral-kernel':'Partial found: AC26 Lemmas 6.5/7.4/7.16 and Theorem 7.17 provide the actual based peripheral relations. The full central-kernel presentation is expanded here.',
'ffcert:cor:covering-h1':'Found in underlying integral map: AC26 Lemma 7.13 and Proposition 7.14 give the first-homology/covering comparison; our product-cover coordinates are explicit.',
'ffcert:thm:normal-trivialization':'Found for exact holomorphic order: AC26 Lemma 5.7(ii) and Theorem 5.4(iv) identify the character line and its order. The explicit smooth nowhere-zero trivialization is printed here.'}
MAPS={
'A.1.1':('Partial found: AC26 page 2 and introductory Seifert discussion give the invariant character, coinvariant circle and heuristic target; no claim that its literal toric character extends.','Found: Engel Lemma 3.8 (covector psi), source lines 842–863, and Remark 8.3, lines 1685–1723, give the regular rank-three quotient and finite multiplicities.','Partial found: DGKX v1 Appendix D, lines 12055–12083, identifies the same invariant character and coinvariant circle; not the full corrected cusp quotient.','Engel for the regular quotient; AC26 for the marked construction; our explicit finite-map check.','circle'),
'A.1.2':('Not located: searched complete transcription for the circle/character/fixed-locus terms and inspected the introductory Seifert discussion, toric section 4 and section 9.5; no stated radial counterexample to literal extension found.','Correction target found: Engel Remark 8.3, lines 1685–1723, asserts continuous extension and selects the Aut0-fixed edge. The checked radial sequences refute that literal assertion; the extendible and fixed curves are different.','Not located: searched full v1 circle/character/fixed-locus matches; Appendix D records the coinvariant circle but no literal-extension counterexample.','Correction of Engel Remark 8.3; exact local counterexample and corrected edge in MAPS.','circle'),
'A.1.3':('Partial found: AC26 introductory Seifert interpretation gives multiplicities (3,4), obstruction p and S3 for |p|=1; the full oriented torus-knot exterior/lens-filling formula is not stated there.','Found for the Seifert S3 target: Engel Remark 8.3. The precise oriented exterior/filling presentation is expanded here.','Not located for the oriented Seifert/lens target: full circle/Seifert/torus-knot/solid-torus searches and Appendix D inspected; the shared integral p is recorded but no such three-manifold classification is stated.','Engel and the AC26 Seifert observation for the target; classical Seifert topology, with our full marked gluing proof.','circle'),
'A.2.1':('Not located: searched circle/character/solid-torus and inspected the Seifert introduction and toric filling; no smooth relative-collar repair theorem found.','Partial found: Remark 8.3 supplies the intended S6-to-S3 quotient, but the literal cusp assertion requires the correction in A.1.2. The smooth repaired map and replacement independence are proved here.','Not located: searched full v1 for circle quotient, solid torus, character and relative collar; Appendix D does not state this repaired map.','Engel for the quotient idea; our corrected cusp construction and relative homotopy proof.','circle'),
'A.3.1':('Not located in searched scope: complete AC26 transcription anti-holomorphic/real-structure/real-form/real-locus searches, plus inspected automorphism and toric sections; no two-class real-involution theorem found.','Not located: complete Engel source searched for anti-holomorphic, real structure/form/locus and involution; no corresponding theorem found.','Not located: complete DGKX v1 source searched for anti-holomorphic, real structure/form/locus and involution; sign involutions in its Oka constructions are unrelated to this classification.','Our family-specific calculation; Smith theory and Illman triangulation are classical ingredients.','real'),
'A.3.2':('Not located: same complete real-structure search and inspected toric/finite charts; no table of these fixed fibres found.','Not located: same complete real-structure search; no real-fibre table found.','Not located: same complete real-structure search; no candidate real-fibre table found.','Our explicit real representatives and actual marked fixed-fibre calculation.','real'),
'A.3.3':('Not located: same real-structure search and inspected automorphism/fixed-curve discussion; no classification of these real three-manifolds found.','Not located: same real-structure search; no S3 real-locus theorem found.','Not located: same real-structure search; no candidate S3 real-locus theorem found.','Our marked real-locus calculation; classical smooth circle-action and Smith ingredients credited separately.','real'),
'A.3.4':('Not located: circle and real-structure searches and inspected corresponding sections; no invariant repaired-map restriction theorem found.','Not located: Remark 8.3 contains the general quotient idea, but no real-locus restriction or null-homotopy theorem.','Not located: full circle and real-structure searches; no corresponding restriction theorem found.','Our corrected quotient restricted to the explicitly computed real loci.','real')}
rows=[]
ws=json.load(open(O/'working_results_inventory.json'))
ms=json.load(open(O/'results_audit.json'))

def common(source_id,run,group,ac,e,dg,elsewhere,credit,source_file='',note=''):
 return {'source_run':run,'source_id':source_id,'source_file':source_file,'paper':'I','found_in_AC26':ac,'found_in_E26':e,'found_in_DGKX_v1':dg,'found_in_DGKX_v2':('Not located for the candidate-specific real assertion: the full v2 source was searched for '+', '.join(terms['real'])+'; no such assertion found.' if group=='real' else 'Compared: v2 Appendix on the source six-sphere, lines 3127–3310, repeats the underlying AC26 construction and sphere conclusion. No separate attribution of the exact new coordinate/correction refinement follows from that summary; the full-source '+group+' search is recorded.'),'found_elsewhere':elsewhere,'credited_to':credit,'notes':note+' Targeted negative searches are not a claim of universal absence or priority.','search_group':group,'searched_baselines':{k:{'source':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'queries':terms[group],'search_scope':evidence[group][k]['scope'],'evidence':'deliverables/work/maps_audit/credit_baseline_searches_I.json#'+group+'/'+k} for k,p in base.items()},'elsewhere_search_record':'deliverables/work/maps_audit/credit_elsewhere_search_I.json','AC26_controlling_original':'sources/original/AC26_original_manuscript.pdf','AC26_original_sha256':hashlib.sha256(Path('sources/original/AC26_original_manuscript.pdf').read_bytes()).hexdigest(),'AC26_original_comparison_record':'deliverables/work/maps_audit/source_credit_checks.json; credit_AC26_original_statement_matches_I.json',**prov}
else_real='Not located among the 43 other attached LaTeX source files searched for real structure, real form and antiholomorphic involution. The sole real-form hit, modular_gps.tex lines 5138–5155, is the real form of the universal elliptic curve and is not this threefold/fixed-locus result. Classical Smith and equivariant triangulation inputs are found in opened Knudson2004 Theorem 4.1(1) and Illman1972 Theorem 3.1, p.48; their scopes do not prove the candidate classification by themselves.'
else_circle='No corresponding corrected quotient assertion located among the 43 other attached LaTeX source files under circle quotient, toric collapse and finite-band searches. The construction uses classical Seifert and relative-homotopy arguments; their complete proofs are printed, with the exact named operative sources checked separately.'
for r in ms:
 if r['id'] not in MAPS:continue
 ac,e,dg,credit,group=MAPS[r['id']]
 rows.append(common(r['id'],'S6_04_MAPS_MANIFOLDS',group,ac,e,dg,else_real if group=='real' else else_circle,credit,r['source_blocks'][0]['file']))
for r in ws:
 sid=r['source_id']
 if sid not in AC_TOPO:continue
 if sid in ['thm:p0-integral-specialization','thm:collapse-equals-specialization']:group='specialization'
 elif sid in ['prop:leray-e2','lem:first-transgression','lem:higher-transgressions','thm:h2-vanishing']:group='leray'
 elif sid in ['prop:geometric-pi1','record:vankampen','topology_reduction:L920']:group='pi1'
 elif sid in ['cor:candidate-sphere','lem:cohomological-closure','thm:sphere-recognition','cor:abstract-s6','cor:candidate-mv-sphere']:group='sphere'
 else:group='collapse'
 if group=='specialization':e='Found in relevant scope: Engel Lemma 7.4, source lines 1331–1480, gives the integral specialization lattices and cusp invariant cycles. No claim that Engel prints our named collapse-versus-nearby-cycle chain comparison.'
 elif group=='leray':e='Found: Engel section 7, Lemma 7.5 (pushforward-cohomology), Lemma 7.6 (transgression-calculation) and Theorem 7.7 (integral-homology), source lines 1481–1643; the marking/sign dictionary is required and retained.'
 elif group=='pi1':e='Found for the fundamental-group conclusion: Engel section 6, Proposition fundamental-group, source lines 1133–1230. His generator and translation conventions differ; our actual based-marking comparison is retained.'
 elif group=='sphere':e='Found: Engel Theorem 7.7, source lines 1617–1643, and the proof of Theorem 4.1, lines 897–904: integral homology followed by Hurewicz/Whitehead and smooth recognition.'
 else:e='Partial found: Engel section 7 records the same specialization and sphere-homology conclusions, including a Mayer–Vietoris computation of the central toric stratification at lines 1474–1476. No corresponding full named honeycomb/spine, two-stage-band, or chain-level comparison statement located in the inspected section 7 and the full collapse/spine/retract/cellular searches.'
 dg='Partial found: DGKX v1 Appendix D, lines 12034–12222, explicitly attributes the source construction, pi1 and sphere homology to AC26 (Theorem 7.17, Corollary 7.29, Theorem 8.1). The exact '+group+' proof/certificate is not reproduced there; full-source searches and the relevant hits are recorded.'
 elsewhere='Classical ingredients found in the opened Hatcher2002 (Theorems 4.5/4.32, Corollary 4.33, UCT/duality scopes), Dimca2004 nearby-cycle formalism, Brown1982 multiplicative spectral sequences, and Smale/Kervaire–Milnor recognition as applicable; exact operative scope is in topology_source_checks.json. Other attached source hits were inspected: Yang appendix nearby-cycles lines 5667–5750 contains an analogous ordered-branch calculation; Viaclovsky two-parameter sphere theorem lines 1310–1334, Liu–Rollenske main theorem proof lines 1703–1718, and Viaclovsky logarithmic-transform sphere corollary lines 1114–1136 use the same classical recognition implication for their own families. These related applications are not asserted to be identical marked statements.'
 rows.append(common(sid,'WORKING_EDITION',group,AC_TOPO[sid],e,dg,elsewhere,'AC26 for the known candidate topology; Engel for the corresponding Leray calculation; classical topology sources for the general implications; our expanded proofs/checks as stated.',r['source_file'],'The alpha3=alpha1 correction is confined to the working edition; AC26 already gives the correct degree-three indices.' if sid=='prop:actual-finite-band-maps' else ''))
for sid in ['CG-S6-07-HOMOLOGY','CG-S6-07-HOMOTOPY']:
 r=next(x for x in ws if x['source_id']==sid)
 ac='Found: AC26 Corollary 7.29 and Theorem 7.22 give the same integral sphere homology.' if sid.endswith('HOMOLOGY') else 'Found: AC26 Lemma 8.2 explicitly chooses the degree-one map by Hurewicz and upgrades it using Whitehead; Theorem 8.1 applies it to X. Our complete path-fibration proof is an alternate classical rederivation.'
 rows.append(common(sid,'WORKING_EDITION','sphere',ac,'Found: Engel Theorem 7.7 and proof of Theorem 4.1, source lines 897–904 and 1617–1643.','Found as an attributed conclusion: DGKX v1 Appendix D, lines 12200–12222, cites AC26 for the simply connected integral homology sphere and smooth identification; it does not print this path-fibration proof.','Found: Hatcher2002 Theorem 4.32 pp.366–367 and Corollary 4.33 pp.367–368 state the exact classical Hurewicz/homological Whitehead implications. Related same implications are used by the inspected Viaclovsky and Liu–Rollenske theorem proofs. The complete course rederivations are retained in Paper I appendices.','AC26 and Engel for the candidate sphere conclusion; classical Hurewicz/Whitehead for recognition; course proofs credited as expanded rederivations.',r['source_file'],'HOMOLOGY is taken over by the existing low-degree Leray and cohomological-closure proofs; HOMOTOPY retains its full distinct path-fibration proof.'))
assert len(rows)==35,len(rows)
# Parent also needs complete attribution fields for all 24 newly audited construction rows.
cm=json.load(open(O/'paperI_construction_full_checks.json'))
for r in cm['rows']:
 sid=r['source_id'];group='construction'
 e='Partial found: Engel sections 2–3 give the related geometric construction and integral monodromy, sections 6–7 give the group/cohomology conclusions. The exact original-period coordinate certificate in this row is not identified with his differently marked presentation; full-source period/toric/normalization searches are recorded.'
 dg='Found for the source construction and conventions: DGKX v1 Appendix D, lines 12034–12222, expressly attributes the periods, finite fills, toric quotient, global compactification and topology to the corresponding AC26 statements. Its main relative-compactification construction uses the same periods and fills. The exact expanded '+sid+' certificate is not claimed to be stated verbatim there.'
 elsewhere='Classical operative sources matched in wb_foundation_source_checks.json and topology_source_checks.json: '+(', '.join(r['operative_external_source_keys']) or 'the printed elementary matrix, covering and gluing arguments')+'. The 43-file attached-literature search is recorded separately; no additional identical marked certificate was located by those terms. This is a scoped comparison, not a general novelty assertion.'
 rows.append(common(sid,'WORKING_EDITION',group,AC_CON[sid],e,dg,elsewhere,'AC26 for the identified construction/result; DGKX and Engel for the related construction; named classical sources for their exact ingredients. Explicit coordinate/integral proof expansions are our rederivations.',r['source_file']))
(O/'credit_comparison_I.json').write_text(json.dumps(rows,indent=2)+'\n')
with (O/'credit_comparison_I.csv').open('w',newline='') as f:
 fields=['source_run','source_id','paper','found_in_AC26','found_in_E26','found_in_DGKX_v1','found_in_DGKX_v2','found_elsewhere','credited_to','notes','reader','effort','date']
 w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)
# Propagate the full comparison fields without discarding old check records.
by={r['source_id']:r for r in rows}
keys=['found_in_AC26','found_in_E26','found_in_DGKX_v1','found_in_DGKX_v2','found_elsewhere','credited_to']
for file,sourcekey in [('results_audit.json','id'),('working_results_inventory.json','source_id')]:
 data=json.load(open(O/file))
 for r in data:
  if r[sourcekey] in by:
   c=by[r[sourcekey]]
   for k in keys:r[k]=c[k]
   r['credit_comparison_record']='deliverables/work/maps_audit/credit_comparison_I.json#'+r[sourcekey]
 (O/file).write_text(json.dumps(data,indent=2)+'\n')
for r in cm['rows']:
 for k in keys:r[k]=by[r['source_id']][k]
 r['credit_comparison_record']='deliverables/work/maps_audit/credit_comparison_I.json#'+r['source_id']
(O/'paperI_construction_full_checks.json').write_text(json.dumps(cm,indent=2)+'\n')
print('Saved',len(rows),'credit rows: 8 MAPS + 25 topology + 2 course + 24 construction. Prior check records retained.')
