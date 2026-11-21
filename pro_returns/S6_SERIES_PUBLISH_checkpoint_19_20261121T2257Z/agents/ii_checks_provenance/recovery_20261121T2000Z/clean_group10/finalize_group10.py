from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re

ROOT=Path('/workspace/scratch/08a92fb2355d/S6_SERIES_PUBLISH')
D=Path(__file__).parent;BASE=D.parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bind(p):return {'path':str(p.relative_to(ROOT)),'sha256':sha(p)}
def dump(p,o):
 assert not p.exists(),('immutable final already exists',p)
 p.write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n')
now=datetime.now(timezone.utc).isoformat()
prep=D/'S6_SERIES_PUBLISH_II_clean_group10_preparation_v2.json'
j=json.loads(prep.read_text())
source=ROOT/'S6_SERIES_PUBLISH_II.tex';s=source.read_text()
I=ROOT/'S6_SERIES_PUBLISH_I.tex';Is=I.read_text()
comparisons={
 '03IC':'The frozen graph-cochain argument constructs the unique edge class, its crossed representative, base-first slant sign and principal invariance. The entire original and proposed proofs were read. The frozen forward implication mu=0 -> gamma(mu)=0 replaces the unsupported converse in the statement, without asserting noninjectivity of gamma. The dated deck addendum identifies left deck T with the inverse of the clockwise endpoint-return cohomology map. All defect, balance, and pairing conclusions remain fixed.',
 '03IE':'The frozen derivation computes the pulled-back zero-section sweep on the full clockwise root circle, including the periodic real correction from the complex logarithmic translation, and obtains the norm by its exact cap Chern pairing. The complete printed proof instead substitutes the full real translation differential and integrates the mixed term. Both yield N_T d=i_v E and the stated coinvariant quotient. The corrected complete proposed proof retains every radial map, connector, differential term, and translation vector.',
 '03ID':'The frozen explicit solid-torus map has exactly the clockwise delta sweep as its boundary; the printed chart uses another filling of the same torus and states the orientation reversal. Both yield zero pairing and zero delta coefficient. The nearby-cycle naturality square is retained and now bound to the complete primary AC TheoremB.1 unit. This supplies the actual degree-two map; no H1-only specialization result is substituted.',
 '03IL':'The frozen proof uses E=nq and real coinvariants, obtaining n/2=0 without a parity premise. The complete printed proof retains its stronger integral E=2nq route. The full parity lattice and cover map are now independently located and read in AC LemmaA.4; the full degree-two specialization input is AC TheoremB.1. Both proofs give the same fibre Chern vanishing and trivial normalized cusp restriction.',
 '03IM':'The frozen proof identifies the edge image with permanent cycles and uses the exact evaluation/proper-base-change square to conclude that the cusp restriction has zero Chern class. The complete proposed proof supplies the precise primary E2 and differential input, and explicitly transports omega=epsilon*p*omega_AC with p=−1. The displayed differential retains its form because omega[delta] is now defined as the actual primitive image; no numerical epsilon has been guessed.',
 '03DR':'The frozen derivation gives the exact dual-canonical twist, conductor section, Cartier-fibre duality and top-degree base-change chain from the declared all-Picard input. The complete proposed proof retains this chain and both nonvanishings. Its construction and local canonical trivialization are bound to the current Paper I family, full cusp charts, and omega_X=O_X(−2S2) away from the disjoint finite fibre.',
 '03IW':'The frozen proof contracts E=nq with the exact vectors, divides only in the real coinvariant line by the actual orders3 and4, and obtains n/2=0. It then applies the separately derived analytic support map to the actual restriction M=L|N0. The complete proposed proof preserves that route and every coefficient, with the precise primary invariant lattice cited.',
 '03IN':'The frozen proof constructs the quadratic Cartier divisor, character difference, full-C(t) equivariance cocycle and inverse fibre action, then computes all six degrees and the logarithmic mixed Chern form −2q. The entire six-step printed proof and final proposed proof were read, including the full theta cocycle and the negative descent factor. The new coefficient-complete Fraction/interpolation program corroborates the arithmetic by a different algorithm from the positively located related SymPy program.',
 '03IH':'The frozen proof uses logarithmic factors, an explicit half-E reference extension, free-group and lattice splittings, and the actual filling sweeps to construct the crossed class and its norms. The complete longer printed proof uses filled central extensions and universal-cover comparison. Its arbitrary-lift endpoint claim required repair: the proposal selects zeta0=−alpha0 Pi(s)v at the root point fixed by the zero-section whisker and proves its endpoint is Q_log exactly. Arbitrary lift changes are conjugate by tau_lambda, as recorded separately. The proposal also identifies clockwise b=−b_plus in the cusp chart. These bounded D13/D25 repairs preserve all final norm and cusp conclusions. The final immutable proposed proof, including the final selected-root wording, was read completely in two consecutive segments.',
 '03I6':'The frozen derivation extracts integral support data from analytic-frame winding and solves the discrete degree equations, then derives the exact mixed Chern map. The complete printed proof uses the quadratic Cartier comparison bundle, component-normalized frames and the Stein maximal chart. The complete proposed proof retains the actual localized open inclusions, inverse-dual arrow, residual multiplier, its zero winding and the formula E_M((lambda,0),(0,m))=−B(B0lambda,m). All cited toric locators now explicitly name the verified2010 text.'}
exposure='The Paper I construction and previously completed Paper II input results were already known and are declared inputs. IM/DR froze at21:37:31; their proofs remained closed while the eight related boundary derivations froze at22:05:10–11. All ten targets were then released at22:05:30. No target proof, target method outline or old owner check record was read before its freeze. The common frozen deck/parallel-transport terminology is corrected by the dated postrelease addendum, without changing frozen bytes. Related historical programs and additional primary locator proofs were read only after release. No independence from Paper I or from the stated input results is claimed.'
validation=[];reads=[]
for t in j['targets']:
 tag=t['tag'];original=ROOT/t['original_full_block']['path'];proposed=ROOT/t['proposed_full_block']['path']
 before=original.read_text();after=proposed.read_text();assert sha(original)==t['original_full_block']['sha256'];assert sha(proposed)==t['proposed_full_block']['sha256']
 assert s.count(before)==1,(tag,'current source changed')
 trial=before
 for g in t['guards']:
  assert trial.count(g['old'])==g['expected_occurrences_in_owning_block'],(tag,g['change_id'])
  trial=trial.replace(g['old'],g['new'])
 assert trial==after,tag
 refs=sorted(set(re.findall(r'\\CompendiumRef\{I\}\{([^}]+)\}',after)))
 for x in refs:assert Is.count('\\label{'+x+'}')==1,(tag,x)
 fj=json.loads((ROOT/t['freeze_receipt']['path']).read_text());fp=ROOT/fj['frozen_derivation_path'];assert sha(fp)==fj['derivation_sha256']
 t['frozen_derivation']=bind(fp)
 t['named_statement_scope']={'start_offset_in_release':0,'end_offset_in_release':len(before),'complete_attached_proofs':1,'additional_released_proofs_outside_independent_target_scope':0}
 t['actual_complete_proposed_proof_read']=True;t['actual_complete_original_proof_read']=True
 t['full_pair_review_completed_utc']=now;t['actual_rereading_scope']='Complete named statement and its entire attached proof, original and final v2 proposal; all exact guards manually compared. No image-only or automatic-comparison reading credit.'
 t['comparison']=comparisons[tag];t['prior_exposure']=exposure;t['proposed_editorial_event']=True
 t['proposed_event_counts']={'targeted proof check':1,'used and rechecked in this run':1}
 t['source_at_final_review']=bind(source)
 t['mathematical_statement_and_values_unchanged']=tag not in ['03IC','03IH']
 t['displayed_final_conclusions_preserved']=True
 t['guard_validation']['all_current_compendium_I_labels_resolve_once']=True
 t['guard_validation']['mathematical_exceptions']='IC: replace unsupported equivalence by the actual forward implication and specify left deck/endpoint-return map. IH: specify left deck action, select the zero-section/whisker vector lift and prove its endpoint, and name b_plus with b=−b_plus. IM: name omega by the primitive differential image through the exact epsilon*p map. These are explicit exceptions, not a blanket mathematical-byte-preservation claim.'
 validation.append({'tag':tag,'source_offset':s.index(before),'before':bind(original),'after':bind(proposed),'guards':len(t['guards']),'current_I_refs':refs,'exact_guard_application':True})
 reads.append({k:t[k] for k in ['tag','statement_owner','original_full_block','proposed_full_block','actual_complete_original_proof_read','actual_complete_proposed_proof_read','actual_rereading_scope','comparison','full_pair_review_completed_utc']})
for b in j['bibliography_guards']:
 assert s.count(b['old'])==1,b['key'];assert (ROOT/b['proposed']['path']).read_text()==b['new'];b['actual_full_pair_read']=True

reading={'schema_version':1,'paper':'II','checker':'i_provenance_recovery','completed_utc':now,'source_at_final_review':bind(source),'targets':reads,'prior_original_reading':bind(D/'S6_SERIES_PUBLISH_II_clean_group10_original_reading_receipt.json'),'canonical_mutations':0,'events_added':0,'rendered_page_credit':0,'new_independent_derivations_from_rereading':0}
dump(D/'S6_SERIES_PUBLISH_II_clean_group10_final_pair_reading.json',reading)
validation_record={'schema_version':1,'paper':'II','created_utc':now,'source':bind(source),'current_I':bind(I),'targets':validation,'all_guard_reconstructions_exact':True,'mathematical_statement_and_values_unchanged':False,'displayed_final_conclusions_preserved':True,'total_owner_guards':sum(len(t['guards']) for t in j['targets']),'bibliography_guards':len(j['bibliography_guards']),'canonical_mutations':0,'events_added':0}
dump(D/'S6_SERIES_PUBLISH_II_clean_group10_guard_validation.json',validation_record)

j.update({'completed_utc':now,'status':'Ten prereading derivations frozen; complete original and final proposed proof comparisons, new computation and exact primary/source transports complete. Awaiting root application and admission.','source_at_final_review':bind(source),'preparation':bind(prep),'original_preparation_v1':bind(D/'S6_SERIES_PUBLISH_II_clean_group10_preparation.json'),'primary_receipt':bind(D/'S6_SERIES_PUBLISH_II_clean_group10_primary_receipt.json'),'exact_transport':bind(D/'S6_SERIES_PUBLISH_II_clean_group10_exact_transport.json'),'computation_methods':bind(D/'S6_SERIES_PUBLISH_II_clean_group10_computation_methods.json'),'CLS_author_reason_clarification':bind(D/'S6_SERIES_PUBLISH_II_CLS_author_reason_dated_addendum.json'),'final_pair_reading':bind(D/'S6_SERIES_PUBLISH_II_clean_group10_final_pair_reading.json'),'guard_validation':bind(D/'S6_SERIES_PUBLISH_II_clean_group10_guard_validation.json'),'deck_convention_correction':bind(D/'S6_SERIES_PUBLISH_II_boundary_deck_convention_addendum.json'),'mathematical_statement_and_values_unchanged':False,'displayed_final_conclusions_preserved':True,'prospective_counts':{'targeted proof check':10,'used and rechecked in this run':10,'extra_computation_events':0},'remaining_gates':['Root approval and exact canonical source application.','Root approval and append-only event admission.'],'v1_to_final_changes':['Three guessed inv:src:B.3.1 references corrected to the actual uniquely bound label inv:B3.1.','IC makes both no-translation and gamma(mu)=0 consequences of mu=0 directly.','IE connector conjugacy sentence uses the root-requested two-sentence form in one exact guard.','I6 uses grammatical let v,w be adjacent vertices.','IH selects the root point through the fixed zero-section whisker explicitly.','Primary locators, exact construction morphism, method comparison, and actual final complete readings are bound. V1 proposals and frozen derivations are preserved.']})
j['computation_evidence']=[{'tags':['03IC','03IE','03ID','03IL','03IN','03IH','03I6','03IW'],'code':bind(BASE/'clean_derivations/S6_SERIES_PUBLISH_II_boundary_preproof_exact.py'),'output':bind(BASE/'clean_derivations/S6_SERIES_PUBLISH_II_boundary_preproof_exact.output.json'),'timing':'Before the eight boundary freezes and every target proof release.','method_binding':j['computation_methods'],'scope':'Exact finite norms, invariant forms, contractions, coefficient-complete quadratic shifts, degree vectors, support recovery and mixed Chern matrix. Complete written proofs supply the analytic and all-input assertions.','no_extra_event':True}]
final=D/'S6_SERIES_PUBLISH_II_clean_group10_final_proposals.json';dump(final,j)
events=[]
for t in j['targets']:
 base={k:t[k] for k in ['tag','statement_owner','checker','freeze_receipt','frozen_derivation','release_receipt','release_envelope','named_statement_scope','original_full_block','proposed_full_block','prior_exposure','mathematical_statement_and_values_unchanged','displayed_final_conclusions_preserved']}
 for typ,scope in [('targeted proof check',t['comparison']),('used and rechecked in this run',t['actual_rereading_scope'])]:
  ev=dict(base);ev.update({'paper':'II','event_type':typ,'event_count':1,'proposal_only':True,'proposal_bundle':bind(final),'scope':scope,'source_application_pending':True,'no_extra_computation_event':True,'bounded_exception_binding':j['exact_transport']});events.append(ev)
dump(D/'S6_SERIES_PUBLISH_II_clean_group10_event_proposals.json',{'schema_version':1,'paper':'II','created_utc':now,'proposal_only':True,'events':events,'prospective_counts':j['prospective_counts'],'canonical_mutations':0,'events_added':0})
for p in [final,D/'S6_SERIES_PUBLISH_II_clean_group10_event_proposals.json',D/'S6_SERIES_PUBLISH_II_clean_group10_final_pair_reading.json',D/'S6_SERIES_PUBLISH_II_clean_group10_guard_validation.json']:
 print(json.dumps(bind(p)))
print(json.dumps({'source':bind(source),'IH_final':bind(D/'S6_SERIES_PUBLISH_II_03IH_proposed_v2.tex'),'owner_guards':validation_record['total_owner_guards'],'bibliography_guards':3,'proposed_events':len(events)}))
