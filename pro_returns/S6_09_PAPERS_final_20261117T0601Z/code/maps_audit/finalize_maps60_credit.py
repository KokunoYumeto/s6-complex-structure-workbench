"""Bounded source-attribution matrix; searches are not worldwide novelty proofs."""
from pathlib import Path
import json,csv,hashlib
R=Path(__file__).resolve().parents[3];W=R/'deliverables/work/maps_audit'
M=dict(reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)',effort='Pro',date='2026-11-17')
index=json.loads((W/'maps60_credit_search_index.json').read_text()); searches=json.loads((W/'maps60_credit_search_log.json').read_text()); bysid={s['search_id']:s for s in searches}
audit=json.loads((W/'results_audit.json').read_text()); byid={r['id']:r for r in audit}
# Each description distinguishes a found construction/prerequisite from a match of the full receiving assertion.
G={
'bubble':[
'AC26 §8, Theorem8.1/Lemma8.2, establishes the homotopy/smooth sphere input; the toric disc of Corollary4.8 contracts a particular base loop. These do not state the twelve relative bubble modifications of a map to S3.',
'E26 main sphere theorem supplies the domain sphere. The invariant quotient in Remark8.3 does not classify relative modifications inside a ball.',
'Found only the underlying source construction and ordinary homotopy language; no full local-bubble assertion identified in the inspected hits.',
'The source-construction appendix does not supply the relative twelve-class assertion. No full match identified in the inspected hits.'],
'framing':[
'AC26 constructs the marked manifold and proves it is a smooth six-sphere; inspected framing hits concern holomorphic line-bundle frames, not the actual stable normal framing of the kernel three-torus.',
'E26 Lemma3.8 and Remark8.3 supply the primitive covector and regular quotient. They do not compute the ambient/flat stable-framing difference or its Adams invariant.',
'Inspected frame hits concern holomorphic conic/line-bundle frames and invariant periods. No full stable-framed three-torus assertion identified.',
'Inspected invariant-frame hits concern the source family and toric lattice. No full stable-framing or Adams-invariant assertion identified.'],
'null_and_cone':[
'AC26 Corollary4.8 gives the particular null base loop and the toric retraction construction; §8 identifies the domain sphere. It does not state the homotopy class of the full holomorphic base map or these specified cofiber maps.',
'E26 Remark8.3 gives the regular circle quotient. Its wedge symbols in the searched homology section are exterior products, not this mapping-cone splitting or nullhomotopy.',
'The attached normal-crossing/cusp construction is prior input. Inspected vee/wedge hits are primarily dual bundles/exterior algebra; no full assertion about these specified cone maps identified.',
'The source-family appendix is prior input; no full cone-map assertion identified in the inspected hits.'],
'retained_angle':[
'No retained-angle/Arf/vanishing-torus theorem was located by the recorded full-file terms. The marked cusp and domain sphere are prior AC26 construction inputs.',
'No retained-angle/Arf/vanishing-torus theorem was located by the recorded full-file terms. The regular quotient is prior Engel input.',
'No retained-angle/Arf/vanishing-torus theorem located by the recorded full-file terms.',
'No retained-angle/Arf/vanishing-torus theorem located by the recorded full-file terms.'],
'named_families':[
'AC26 supplies the original marked sphere and its cusp. No simultaneous homotopy-class theorem for the later named families is asserted in the inspected sections.',
'E26 Remark8.3, lines1685–1723, supplies the regular circle quotient and (3,4) Seifert data. Its literal cusp extension needs the correction printed in Paper I; it does not calculate 6nu-prime.',
'No full named-family homotopy-class theorem identified by the recorded terms; the original family/period construction is prior input.',
'No full named-family homotopy-class theorem identified by the recorded terms; the source sphere appendix is prior input.'],
'cw':[
'AC26 §§7–8 and the cell appendix already prove the fundamental group, integral sphere homology and smooth-sphere conclusion. Original PDF p42 expressly denies tubular-neighbourhood status because the fibre is multiple; B5.1 corrects that underlying smooth-disc-bundle sentence, retaining the correct meridian winding. The explicit ribbon attachment/framing proof is an additional proof, not a new sphere theorem.',
'E26 fundamental-group and integral-Leray sections and main theorem already give the simply connected integral homology sphere. The specific ribbon CW model, cell counts and retained normal framing are not the same proof.',
'No full ribbon CW/framing assertion identified; the toric source construction is prior input.',
'No full ribbon CW/framing assertion identified; source construction and source-sphere summary are prior input.'],
' theta7':[],
' theta7_unused':[],
'smoothing':[
'AC26 supplies the singular source family and sphere. Inspected conifold/surgery terms do not identify the parameterwise S3xS3 smoothing return or its integral p1.',
'E26 supplies the elliptic/logarithmic source construction; no full parameter-smoothing/Torelli invariant theorem identified in the inspected hits.',
'DGKX v1 local conifold and small-resolution/Oka arguments, including lines294,3085,7497,8486, are geometric antecedents. They do not state the parameterwise S3xS3 return, its two integral Wang generators, or the trace invariant.',
'DGKX v2 local conifold/small-resolution arguments, including lines307,2588,2870, are antecedents, not the parameterwise Torelli/trace theorem.'],
'affine_defect':[
'AC26 fixes the affine source periods and cusp marking; no exact order-six ordinary-return obstruction identified in the inspected hits.',
'E26 elliptic/line-bundle construction supplies the source model; no exact order-six positive-parameter-return obstruction identified.',
'DGKX v1 even-shift action lines10364–10746 and quadratic strictification lines11863–11955 are actual antecedents of the closing map. The order-six ordinary quotient defect and failure of scalar interpolation are the additional calculation.',
'DGKX v2 cusp deck/shear model around1321ff is prior local input; it does not reproduce the v1 global period-classification/strictification section or this exact defect calculation.'],
'spin_c':[
'Only homotopy-sphere/h-cobordism background is located in the inspected hits; no displayed spin-c filling formula for this return.',
'Only the smooth six-sphere recognition/h-cobordism background is located; no displayed spin-c return formula.',
'Inspected coboundary hits are affine group cocycles, not the eight-dimensional spin-c characteristic formula.',
'No spin-c filling formula located by the recorded terms.'],
'cover_height':[
'AC26 gives the underlying elliptic surface, its primitive Mordell–Weil section and indefinite period form. No genus-three degree-twelve scalar-return cover with the full displayed characters/intersection calculation identified.',
'E26 §2, lines335–403, already uses Shioda height to compute the source translation/degree. This is a positive prerequisite match; the degree-twelve pulled-back surface and semistable filling signatures are additional calculations.',
'DGKX v1 finite cyclic covers are local covers used for Oka and extension arguments. No full scalar-return genus-three/character/intersection theorem identified.',
'DGKX v2 cyclic covering/Oka discussion is a construction antecedent, not the asserted scalar-return height/signature calculation.'],
'norm_torsor':[
'AC26 §3.2 and the Mordell–Weil identification around text1111 supply additive line-bundle torsors and the elliptic source section. They do not state the cyclic norm image12ZP or the genus-one torsor conductor obstruction here.',
'E26 §2 and the finite Gm-torsor construction, including lines306,621–646, are positive geometric antecedents. They do not give this cover norm lattice or F^12=t_6P torsor.',
'DGKX v1 finite etale stabilizer torsors and the coarse multiple-fibre geometry are prior inputs; they are distinct from this genus-one torsor/norm obstruction.',
'DGKX v2 source-period summary is an antecedent; no full genus-one conductor/norm theorem identified in the inspected hits.'],
'fixed_conifold':[
'AC26 supplies the source cusp and fixed-action construction; no full fixed-circle replacement, quotient tangent number or quotient-return isotopy classification identified by the recorded terms.',
'E26 supplies the source model and finite quotients; no full fixed-circle replacement/return classification located by the recorded terms.',
'DGKX v1 conifold resolutions and gluing are prior local antecedents. They do not state the fixed-circle free replacement, its p1 coefficient, or the integral shear/cube of its parameter return.',
'DGKX v2 conifold/small-resolution arguments are prior local antecedents, not the displayed free-circle quotient-return invariants.'],
'kummer':[
'AC26 periodic A2 fan and cocharacter marking are the construction input. No full corrected Kummer finite-map/sublattice/globalization theorem identified in the inspected hits.',
'E26 finite good-reduction covers and degree3/2 isogenies are antecedents; no theorem for these prescribed Kummer cusp components identified.',
'DGKX v1 cyclic finite covers, including2669ff and4151ff, are local Oka/extension inputs; they do not give the prescribed scalar cocharacter-lattice obstruction and multi-component global cover.',
'DGKX v2 covers around2206ff/2670ff are local Oka inputs, not the stated Kummer globalization theorem.'],
'fourfold':[
'No four-dimensional complex construction or rank-three Kuhn specialization theorem identified by the recorded terms; the rank-two source construction is prior input.',
'The elliptic surface and its global Weierstrass model are prior input. No full fourfold/Kuhn-cusp integral-specialization assertion identified.',
'The fibre-product hits concern lower-dimensional local models/base changes, not this compact complex fourfold or its integral homology.',
'The fibre-product hits concern local/base-change constructions, not this compact complex fourfold or its integral homology.'],
'kuhn_euler':[
'No rank-three Kuhn Euler assertion located by the recorded terms. The rank-two periodic fan is an antecedent.',
'No rank-three Kuhn Euler assertion located by the recorded terms.',
'No rank-three Kuhn Euler assertion located by the recorded terms.',
'No rank-three Kuhn Euler assertion located by the recorded terms.'],
'characteristic':[
'No eight-dimensional connected-sum characteristic classification located by the recorded terms.',
'No eight-dimensional connected-sum characteristic classification located by the recorded terms.',
'The single inspected analytic-Grauert hit is unrelated to the stated eight-dimensional classification.',
'No eight-dimensional connected-sum characteristic classification located by the recorded terms.'],
'linear_obstruction':[
'The source square-zero unipotent cusp is a lower-rank example; it does not state the general primitive rank-three normal form/centralizer or the affine fixed-point obstruction.',
'No full statement of either rank-six linear assertion located by the recorded terms.',
'DGKX v1 AppendixC has the original rank-four common centralizer and period-shift calculation. This is a related lower-rank calculation, not the displayed primitive rank-three block centralizer or affine fixed-point theorem.',
'DGKX v2 free affine local cyclic action is related construction input, not either stated general linear-algebra assertion.'],
'nonselfdual':[
'No explicit nonselfdual (5,4) rank-six eight-manifold statement located by the recorded terms.',
'No explicit nonselfdual (5,4) rank-six eight-manifold statement located by the recorded terms.',
'The inspected phrase about three connected fillings is not three-connectivity of an eight-manifold; no full matching assertion identified.',
'The inspected phrase about three connected fillings is not three-connectivity of an eight-manifold; no full matching assertion identified.'],
'polarized_obstruction':[
'AC26 Lemma2.8 and Remark3.23 explicitly obstruct a monodromy-compatible polarization of the original rank-four system by the indefinite cusp form. This is a positive related obstruction, not the global b1/b2 theorem for a polarized algebraic rank-six Engel construction.',
'E26 finite reduced fibres are abelian surfaces and the period form has signature(1,1), Remark8.3. This is related background, not the general algebraic semisimplicity obstruction asserted here.',
'Inspected algebra/semisimplicial hits concern normalization resolutions, not Deligne semisimplicity of algebraic polarized monodromy.',
'No full algebraic polarized rank-six obstruction identified by the recorded terms.'],
'explicit_periods':[
'No exact genus-two quintic/rank-six nonselfdual period construction located by the recorded terms.',
'No exact genus-two quintic/rank-six nonselfdual period construction located by the recorded terms.',
'No exact genus-two quintic/rank-six nonselfdual period construction located by the recorded terms.',
'No exact genus-two quintic/rank-six nonselfdual period construction located by the recorded terms.'],
'oka_periods':[
'No LSAP/strongly dominated unpolarized rank-six period-domain theorem located by the recorded terms.',
'No LSAP/strongly dominated unpolarized rank-six period-domain theorem located by the recorded terms.',
'DGKX v1 proves Oka/Oka-1 results for source fillings and blow-ups. These are related flexibility results, not the unpolarized rank-six period-domain tube or relative section theorem here.',
'DGKX v2 proves Oka/Oka-1 results for source fillings and blow-ups; these do not identify the rank-six period domain or provide this bounded one-cusp correction.']}
G['theta7']=[
'AC26 base-fibre mapping-torus/isotopy facts concern geometric monodromy of the torus fibration. They do not compute the parameter-circle class in Theta7.',
'E26 supplies the sphere family but no parameter-circle Theta7 value is identified in the inspected scope.',
'DGKX v1 even-shift biholomorphisms and exact affine closing supply the actual gluing antecedent; they do not themselves evaluate its smooth Theta7 class.',
'DGKX v2 gives the underlying source model but no parameter-circle Theta7 evaluation identified.']
other={
'A.2.2':'Classical relative pinch/bubble construction and pi6(S3)=Z/12; exact Hatcher/Toda scopes are checked separately. The correction refutes the claimed uniqueness from agreement outside a cusp neighbourhood.',
'B.1.1':'Bott stable groups and actual coordinate/framing comparison supply the proof. The flat regular quotient is credited to Engel; no full ambient-versus-flat framing calculation identified in the bounded attached-source comparison.',
'B.1.2':'The stable eta product, real Adams invariant and unstable suspension are classical; exact Bott1959, APSII §4 and Toda1952 Th4.1/Cor4.2–4.4 checks are in maps_B_and_weight_source_checks.json. The application identifies the actual repaired quotient fibre and framing.',
'B.2.1':'The repaired quotient construction printed in I and the classical Hopf/postcomposition calculation are inputs. The statement concerns the actual holomorphic base map, not just one null base loop.',
'B.3.1':'Classical Lie-framed torus/Arf computation: Debray–Gunningham Example3.8 and Th3.2/Rmk3.3/Th3.6, Johnson spin quadratic forms, and Pontryagin originals are positively credited in the peer retained-angle ledger. The actual cusp-collapse identification is the source-specific application; the long WB proof is separately retained.',
'B.3.2':'The original MAPS factorization proof and the separate working carrier-extension proof are retained; the latter settles only the angle-forgotten carriers and is not a replacement of the retained-angle theorem.',
'B.3.3':'The wedge/cofiber splitting is classical; the actual composite uses the checked quotient class B1.2. No matching specified splitting/map assertion identified in the bounded attached sources.',
'B.4.1':'Positive construction matches: Liu–Rollenske S6_arxiv.tex, Viaclovsky two-parameter and logarithmic-transform papers, and Engel regular quotient. attached_maps_source_checks.json records exact scopes. LR has a source target-degree typo H1 instead of H2 at lines1607–1612, corrected explicitly without changing its unit calculation. No claim that these sources already evaluate every named canonical map.',
'B.5.1':'Hatcher Propositions4G.1–4G.2 with full proofs and Waldhausen Th6.1/Cor6.5 are exact prior topological inputs. The literal smooth tubular-neighbourhood correction is to the original AC26 PDF p42; it is separate from the working-only alpha3 typo.',
'B.5.2':'The sphere conclusion is already AC26/E26. The full alternative CW/primitive-lattice/normal-framing argument is preserved with that credit. Hatcher relative Hurewicz/Whitehead and the separate course degree-one proof are classical prerequisites.',
'B.6.1':'An elementary congruence reduction. FAMILY E2.2 posed the actual value as an open question and supplied a definition, not a numerical computation. The conditional two-residue statement itself excludes no original class without b.',
'B.6.2':'PUSH C3.24 and C3.27 already provide two distinct full zero-monodromy proofs and must be credited and retained; MAPS also gives its separate direct free-circle trace proof. Krylov and Olbermann are comparative classification inputs, not an evaluation of the actual annular map.',
'B.6.3':'The actual closing map is PUSH C3.5, fully transferred to I. Conifold surgery and the homological transport calculation are distinct from the earlier local DGKX resolution geometry.',
'B.6.4':'Krylov arXiv:math/0107005v1 §2.1/Th2–3 supplies the Torelli exact sequence and normal-framing detector, with exact framed-bounding hypothesis checked. This is not a claim that Krylov identifies the actual family return.',
'B.6.5':'Classical spin characteristic/gluing formula; the actual familywise surgery trace and its vanishing classes are source-specific.',
'B.6.6':'Combines the actual conifold/closing proof with the classical Torelli exact sequence. It is a reduction to a central Theta7 class, not by itself an evaluation.',
'B.6.7':'A refutation of the proposed scalar interpolation, using the actual DGKX/PUSH affine closing. The exact order-six quotient calculation is retained; it does not obstruct arbitrary smooth isotopies.',
'B.6.8':'The order-six quotient defect is the same exact affine calculation for the higher families; it is compatible with the later zero smooth-monodromy theorem.',
'B.6.9':'Known characteristic formula: Crowley–Nordstrom spin-c coboundary formula, published2021 Lemma2.1/equation(2.1), rewritten using p1=c1²−2c2. The manuscript correctly labels this Known.',
'B.6.10':'Shioda1990 reprint Th8.4/8.6 and Prop8.12 supply the height/base-change facts; the genus, deck/Hodge characters and primitive height2 section are checked calculations for this cover.',
'B.6.11':'Engel K13 construction and PUSH A4.1/A4.4 printed in I provide the actual small-resolution H2 and null exceptional curve. The normalized intersection/signature/nonspin calculation is an additional proof, not inferred from a guessed plumbing.',
'B.6.12':'Shioda height and Griffiths1968 II Th1.1 period theorem are positive prior inputs. The actual two character systems, primitivity and norm image12ZP are explicit additional calculations.',
'B.6.13':'Classical analytic torsors/exponential and group-cohomology machinery; the exact local witnesses, global order4 class and F^12=t_6P conductor construction are checked here. No full matching torsor statement identified in the bounded attached-source comparison.',
'B.6.14':'A specific obstruction to the stated one-component conductor construction, using the preceding torsor and elementary boundary/Gysin calculations. It does not rule out more general fillings.',
'B.6.15':'Known spin-c invariant machinery from Crowley–Nordstrom2021 Lemma2.1 with exact disc-bundle orientation and integral congruence checked here; the congruence is not a newly introduced invariant.',
'B.6.16':'Classical equivariant local conifold models and the actual affine closing are prior inputs; the two actual Leray grades do not determine their extension or an integral shear.',
'B.6.17':'A complete nested tangent/quotient proof is retained in maps_fixed_quotient_tangent.tex; the coefficient−4 follows from the actual marked closing, not a numerical classifier run.',
'B.6.18':'Jin2026v2 Lem2.1,Prop3.1,Lem4.4,Lem4.8,Th4.9 supply the exact isotopy classification. The primitive/doubled-sphere characteristic pairs (1,4),(8,8) are prior source data. The actual ell=−4 identifies the displayed one-parameter class; B remains uncomputed at this intermediate stage.',
'B.6.19':'Classical spin trace and Eells–Kuiper comparison, applied to the actual fixed-curve normal data. The conditional k=−1 clause is preserved and is resolved downstream.',
'B.6.20':'The actual Euler-cube calculation closes the prior conditional step; earlier zero-monodromy proofs in PUSH remain separately credited.',
'B.6.21':'Restates the now-computed original zero class from the preceding full proof. PUSH has two earlier distinct proofs; retain them and avoid a novelty claim for a repeated conclusion.',
'B.6.22':'Extends the actual fixed-circle construction to the stated higher families; classical trace machinery is credited, with the marked affine cap data checked explicitly.',
'B.6.23':'Exact actual higher Euler-cube/tangent calculation; the distinct expanded trace/linking proof is retained, not replaced by agreement of finite symbolic output.',
'B.6.24':'A separate full free-circle/trace proof of the higher zero class already established by PUSH C. Distinct proofs are preserved with explicit cross-companion credit.',
'B.6.25':'Elementary D7×S1 filling after an actual isotopy has been proved; its zero Pontryagin square/signature do not supply a new independent monodromy proof.',
'C.1.1':'Classical toric power maps and affine semigroup/ring computations; this row corrects the proposed degree/flatness statement for the specified cusp.',
'C.1.2':'Classical smooth toric cone lattice criterion, applied to every cone of the actual periodic A2 fan. The scalar-subgroup conclusion is the explicit computation.',
'C.1.3':'Classical etale covering of a simply connected smooth compact manifold and purity/local toric analysis supply the obstruction for the prescribed whole cusp component.',
'C.1.4':'Explicit congruence-orbit calculation and finite-cover degree accounting; the result concerns a single prescribed cusp component, not arbitrary normal covers.',
'C.1.5':'Classical finite normalization/Kummer cover construction, with the explicit compatible mod-N monodromy cover and multiple cusp components. This does not contradict the smooth or single-component obstructions.',
'E.1.1':'A direct local invariant-ring counterexample to the literal normalization assertion; no independent full matching refutation identified in the bounded sources.',
'E.1.2':'Positive prior construction input: Engel elliptic Weierstrass model and Yang periodic toric fan construction. The corrected global fourfold and its section are built explicitly here.',
'E.1.3':'Chen2021 ThB gives the rational local invariant-cycle input under the exact Kähler/proper/SNC hypotheses; Deligne HodgeIII proper simplicial weights and the fully printed cellular calculation prove the stated free integral specialization. Rational invariant cycles alone do not imply integral saturation.',
'E.1.5':'Uses the preceding actual cusp/finite restrictions, Leray transgression, section, UCT and duality. Exact finite Smith computations are independently rerun; no full matching fourfold homology theorem identified in the bounded attached sources.',
'F.1.1':'Positive full generalization match: Yang, Compact_Complex_Threefolds_REPAIRED_v4_5.tex, Corollary standard grid family/kuhn-euler lines4827–4838, states n!d. The 6d assertion is the n=3 specialization, not a new general Euler formula.',
'F.1.2':'Known: characteristic-genus formulas (Esole–Kang), unimodular-lattice classification (Peters–Sterk and classical lattice theory). Exact primary scopes are in the E-agent ledger. The source correctly labels the row Known.',
'F.1.3':'Exact prior result: Mandal Corollary1.4 and the full §5 argument give the orientation-compatible almost-complex criterion; 3HP2#(−HP2) is its stated specialization. This row is Known.',
'F.1.4':'Elementary affine linear algebra: invertibility of I−A solves the fixed-point equation. This is a classical obstruction, applied to refute the proposed diagonal tuple.',
'F.2.1':'Elementary integral split exact-sequence/Smith-basis calculation and block commutator. The primitive image=kernel hypothesis is essential; no new general theorem of lattice theory is claimed.',
'F.2.5':'The explicit nonselfdual tuple and its assembled eight-manifold are source-specific. Yang supplies the Kuhn fan; characteristic/weight sources and the complete relative almost-complex extension proof are credited. Rational calculations alone do not establish F2.6.',
'F.2.6':'The original receiving proof is supplemented by the fully printed actual torsion d2 calculation (primitive theta=a+4k); finite Smith data alone were insufficient. This repaired integral conclusion is distinct from the earlier rational result.',
'F.3.4':'Deligne HodgeII1971 §4.2.2–4.2.7 is a positive operative source: algebraic polarized monodromy is semisimple. The global algebraic hypothesis is indispensable. AC26 already has a different local polarization obstruction.',
'F.3.5':'Classical Picard–Lefschetz/Hurwitz and the rank5 exterior-square construction are inputs. The exact quintic family, peripheral signs and matching to this tuple are the source-specific construction; root provides an independently reviewed elementary Sp4→SO5 bridge in downstream F2.10.',
'F.3.6':'Uses the preceding actual quintic periods, exact extension/transversality and bounded cusp correction. Do not confuse conjugated cohomology A^{-1},B^{-1} with the homology A^t,B^t marking.',
'F.3.7':'The specific candidate has explicit finite good-reduction quotients plus the marked Kuhn cusp. This is stronger at its finite punctures than the general one-cusp theorem F3.11.',
'F.3.8':'Alarcón–Forstnerič2025 spanning-tube/LSAP/Oka-1 machinery is positively credited. The nine explicit tubes and their transverse derivative span identify this period domain as an application.',
'F.3.9':'Alarcón–Forstnerič2025 relative/section principles and Forstnerič–Prezelj2002v3 frame-bundle spray are prior inputs; the rank-six period-domain application and real transversality are checked here.',
'F.3.10':'Alarcón–Forstnerič2025 definitions7.7/7.11 and Proposition7.13 with full proof give the operative LSAP bundle-fibre principle. The still-open general Oka-1-fibre question is not substituted for it.',
'F.3.11':'Uses the checked LSAP relative section principle and an explicit bounded maximal-cusp model. It proves one prescribed cusp correction on an otherwise punctured base; it does not prove simultaneous finite good reduction at every other puncture.',
'F.4.1':'The smooth classification is classical Wall normal-invariant theory as stated precisely by BHS, Nikulin unimodular-lattice results and Nagy inertia input; the almost-complex connected sum is already Mandal. The new source-specific conclusion is the explicit compact integrable construction and its checked characteristic/normal data, not a new smooth classification theorem.'}
assert set(other)=={r['source_id'] for r in index}
records=[]
for ix in index:
 sid=ix['source_id'];a=byid[sid];rs=[bysid[k] for k in ix['search_ids']]
 r=dict(source_run='S6_04_MAPS_MANIFOLDS',source_id=sid,paper='III',statement=a['statement'],source_blocks=a.get('source_blocks',[]),search_group=ix['group'],**M)
 for j,b in enumerate(['AC26','E26','DGKX_v1','DGKX_v2']):
  s=next(x for x in rs if x['baseline']==b);r['found_in_'+b]=G[ix['group']][j]
 r['found_elsewhere']=other[sid]
 r['credited_to']=other[sid]
 r['bounded_comparison_scope']='Complete-file regex searches in four version-distinct baselines and43 other unique attached LaTeX files; selected relevant mathematical hits and the separately recorded exact primary statements/proofs were opened. This is not a claim that every hit or every source proof was reread, and is not worldwide absence/priority evidence.'
 r['searched_baselines']={s['baseline']:dict(source=s['source'],sha256=s['source_sha256'],queries=s['queries'],hit_count=len(s['hits']),search_id=s['search_id'],scope=s['search_mode']) for s in rs if s['baseline']!='elsewhere'}
 r['elsewhere_searches']=[dict(source=s['source'],sha256=s['source_sha256'],queries=s['queries'],hit_count=len(s['hits']),search_id=s['search_id']) for s in rs if s['baseline']=='elsewhere']
 r['exact_search_log']='deliverables/work/maps_audit/maps60_credit_search_log.json'
 r['operative_primary_check_ledgers']=['deliverables/work/maps_audit/references_verified.json','deliverables/work/maps_audit/remaining_primary_source_checks.json','deliverables/work/maps_audit/maps_B_and_weight_source_checks.json','deliverables/work/maps_audit/fourfold_priority_source_checks.json','deliverables/work/maps_audit/attached_maps_source_checks.json','deliverables/work/maps_audit/final_citation_source_checks.json','deliverables/work/invariants_arithmetic/retained_angle_references_verified.json','deliverables/work/cdp_audit/maps_E/references_verified.json']
 records.append(r)
 # Keep historical checks and append a named new comparison, rather than replacing old check events.
 a['current_credit_comparison']=dict(record='deliverables/work/maps_audit/maps60_credit_comparison.json',source_id=sid,**M)
 for k in ['found_in_AC26','found_in_E26','found_in_DGKX_v1','found_in_DGKX_v2','found_elsewhere','credited_to']:
  if k in a and a[k]!=r[k]:a.setdefault('historical_credit_fields',{}).setdefault(k,a[k])
  a[k]=r[k]
 a.setdefault('credit_check_records',[])
 ev=dict(event_id='new-maps60-bounded-credit-20261117',comparison_record='deliverables/work/maps_audit/maps60_credit_comparison.json#'+sid,**M)
 if ev not in a['credit_check_records']:a['credit_check_records'].append(ev)
(W/'maps60_credit_comparison.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
cols=['source_run','source_id','statement','found_in_AC26','found_in_E26','found_in_DGKX_v1','found_in_DGKX_v2','found_elsewhere','credited_to','bounded_comparison_scope']
with (W/'maps60_credit_comparison.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=cols,extrasaction='ignore');w.writeheader();w.writerows(records)
(W/'results_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
(W/'maps60_credit_comparison_summary.json').write_text(json.dumps(dict(rows=len(records),actual_complete_file_searches=len(searches),groups=len({r['search_group'] for r in records}),unique_source_files=len({r['source'] for r in searches}),positive_known_matches=['F1.1 Yang general n!d','F1.3 Mandal Cor1.4','B5.2 AC26/E26 sphere conclusion','B6.9/B6.15 Crowley–Nordstrom spin-c formula','B3.1 Debray–Gunningham Lie torus','B6.18 Jin classification','F3.4 Deligne algebraic semisimplicity','F3.8–11 Alarcón–Forstnerič LSAP principles'],scope='Bounded source comparison; full statement and classical/construction antecedents distinguished; no global novelty assertion.',**M),indent=2)+'\n')
print('Saved',len(records),'rows; preserved earlier comparison/check fields.')
