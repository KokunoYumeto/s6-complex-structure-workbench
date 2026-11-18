"""Record the audited completion of F.2 and update the current report table."""
from pathlib import Path
import json,re,datetime
root=Path(__file__).resolve().parents[1]
audit={
 'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'item':'F.2','verdict':'Complete effective classification and all marked topological computations',
 'statements':['F.2.31','F.2.33','F.2.34','F.2.35','F.2.36','F.2.37','F.2.38','F.2.39'],
 'survivor_classification':'F.2.7--F.2.30, including both directions of the finite integral tests',
 'root_proof_review':'Passed: complete chain equivalences, finite degree-nine prefix, affine integer offsets, actual peripheral signs, primitive cusp marking, all torsion and order-one clutch transport',
 'root_code_review':'Passed: global_chains.py, total_homology.py, marked_gluing.py, classify_gluing.py and identity-insertion normalizer',
 'root_exact_outputs':[
  'records/root_global_chains_audit.out','records/root_global_boundary_audit.out',
  'records/root_affine_graph_audit.out','records/root_global_cusp_audit.out',
  'records/root_peripheral_signs_audit.out','records/root_marked_survivor_audit.out',
  'records/root_full_gluing_audit.out','records/root_full_gluing_audit.json'],
 'exact_scope':{'Fox_simplices':156,'noncommuting_AW_simplices':156,
  'periodic_boundary_equivalences':4,'affine_graph_double_map_tests':6,
  'peripheral_sign_tests':7,'cusp_generators_checked':10048,
  'cusp_equivalence_unit_cancellations':5088,'full_gluing_integrations':3,
  'involution_classes':56,'identity_insertions':168,'unified_full_pipeline_tests':2},
 'computational_limit':'The general noninvolution canonical height-box algorithm is proved terminating but has not been exhaustively run; no such execution is claimed.',
 'marking_limit':'The corrected answer uses the specified Kuhn cusp marking and clutch vector; matrices alone do not specify a filling, as proved in F.2.3.',
 'preservation':'The exact former F.2.4 paragraph is in records/fourfolds_F2_4_superseded.tex; earlier checkpoints are unchanged.'}
(root/'records/root_f2_completion_audit.json').write_text(json.dumps(audit,indent=2)+'\n')
p=root/'S6_04_MAPS_MANIFOLDS_report.md';s=p.read_text()
s=re.sub(r'^\| F\.2 \|.*$',
 '| F.2 | F.2.1–F.2.39 | (a)/(b): complete effective simultaneous integral classification with canonical representatives and a proved input-dependent bound; all fundamental groups and integral homology computed for every fully marked affine gluing; every three-connected survivor characterized. The full 56-class involution catalogue and all integration tests are executed. Peripheral matrices alone are refuted as sufficient filling data |',s,flags=re.M)
s=re.sub(r'^\| D\.2 \|.*$',
 '| D.2 | D.2.1–D.2.32 | Undecided in the full requested classification. The natural sphere sector is complete on 21 profiles: 59 marked patterns on 50 rows. All original/logarithmic additive choices give 282 exact homology patterns on all 172 natural initial rows, with every free affine twist. Broader multiplicative and star fillings, higher initial weights, and the remaining nonsphere smooth types are under active proof |',s,flags=re.M)
s=re.sub(r'This is an ongoing research checkpoint, not a completed answer\..*?further confirmation\.',
 'This is an ongoing research record, not a completed answer. Work began at 14:39:41 UTC on 15 November 2026. The progress decisions at three hours and every subsequent hour through eight hours were CONTINUE because main open items were advancing. The next decision is due at approximately 23:39 UTC. F.2 closed after the eighth source freeze; D.2 and E.2 remain open. The user has authorized continued work without a further confirmation.',s,flags=re.S)
s=s.replace('## Main remaining attacks\n','## Main remaining attacks: historical record from earlier checkpoints\n\nThese paragraphs retain the earlier attempted routes and their limits. The opening table and the latest dated sections give the current state; later theorems supersede the earlier statements of what remained undecided.\n')
s+='''\n\n## F.2 completed after checkpoint08\n\nAt approximately 23:02 UTC, the final wrappers and root audits completed F.2. The complete answer is Theorem F.2.39. The linear classification uses the unconditional simultaneous integral-conjugacy decision of F.2.36 and the canonical normal form of F.2.37. Its finite stopping bound depends on the input; the unbounded trace family proves that a single global entry cutoff cannot classify every tuple. All 56 involution classes are enumerated, and all 168 insertions of an identity at the three ordered finite positions pass exact normalization tests. The general noninvolution fallback has not been exhaustively executed; its termination is proved, and that computational limitation is stated explicitly.\n\nThe topological calculation retains the actual affine orders and integer numerators, the clutch vector, and the primitive cusp marking. F.2.31 computes every fundamental group. F.2.35 constructs the actual finite integer Mayer–Vietoris cone and computes every homology group, including torsion. Root independently checked the proof and full implementation, 156 Fox simplices and 156 noncommuting Alexander–Whitney simplices, four periodic boundary equivalences, six affine boundary comparisons with their Thom cones, seven exact peripheral sign tests, and all 10,048 cusp generators. The cusp comparison cone was eliminated by 5,088 integral unit cancellations.\n\nThree complete eight-dimensional integrations passed: the original order-(5,4) survivor, the three-point order-two regular-log example with the independently predicted torsion, and an orientation-reversing involution example. Root independently recomputed their saved Smith groups, checked van Kampen abelianizations, Euler number six, mod-two Poincare duality and the top-degree orientation test. The two unified canonical-classification/topology runs also passed, including an order-one site with a nonzero numerator and the compensating suffix clutch. The exhaustive survivor parametrization and six necessary-and-sufficient integral tests were already proved in F.2.30.\n\nThe former active Open paragraph F.2.4 has been replaced by the resolved conclusion, with its exact prior text retained in records/fourfolds_F2_4_superseded.tex. The local-model counterexample F.2.3 remains a refutation: the corrected calculation specifies the marked Kuhn filling rather than pretending that its peripheral matrices alone determine it. The archived eighth checkpoint is unchanged.\n'''
p.write_text(s)
print(json.dumps(audit,indent=2))
