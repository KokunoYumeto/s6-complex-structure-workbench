from pathlib import Path
import hashlib, json, re
from datetime import datetime, timezone

root=Path('/workspace/scratch/08a92fb2355d/S6_SERIES_PUBLISH')
base=root/'agents/ii_checks_provenance/recovery_20261121T2000Z'
folder=base/'clean_group14'
now=datetime.now(timezone.utc).isoformat()
def bind(p):
    p=Path(p)
    if not p.is_absolute(): p=root/p
    return {'path':str(p.relative_to(root)), 'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def save(name,obj):
    p=folder/name
    assert not p.exists(), p
    p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
    return bind(p)
def f(name): return folder/name
prep=json.loads(f('S6_SERIES_PUBLISH_II_clean_group14_BF_preparation_v2.json').read_text())
target=prep['targets'][0]
old=(root/target['original_full_block']['path']).read_text()
new=(root/target['proposed_full_block']['path']).read_text()
made=old
counts=[]
for g in target['guards']:
    n=made.count(g['old'])
    assert n==g['expected_occurrences_in_owning_block'],(g['change_id'],n)
    made=made.replace(g['old'],g['new'])
    counts.append({'change_id':g['change_id'],'occurrences':n})
assert made==new
source=root/'S6_SERIES_PUBLISH_II.tex'
assert source.read_text().count(old)==1
displays=lambda s:re.findall(r'\\\[(.*?)\\\]',s,re.S)
labels=lambda s:re.findall(r'\\(?:label|hypertarget|tag)\{[^}]*\}',s)
assert displays(old)==displays(new)
assert labels(old)==labels(new)
freeze=bind('agents/ii_infra/derivation_freezes/01BF/20261122T001325638493Z/S6_SERIES_PUBLISH_derivation_freeze_receipt.json')
release=bind('agents/ii_infra/released_proofs/01BF/d353b72d683f1cf3/S6_SERIES_PUBLISH_release_receipt.json')
derivation=bind(base/'clean_derivations/S6_SERIES_PUBLISH_II_01BF_fresh_derivation.md')
inputs=bind(f('S6_SERIES_PUBLISH_II_BF_prereading_inputs.json'))
prior=json.loads((root/inputs['path']).read_text())['prior_related_exposure']

comparison=r'''# BF / A.5.5: complete frozen derivation and complete source-pair comparison

The complete original statement and all eleven proof items were read after the recorded freeze/release. The complete v1 proposed block was then read. The complete final v2 was actually read in two contiguous source outputs, lines 1–180 and 181–266, on 22 November 2026 after 00:21:09 UTC and before this record was written. No Paper II rendered-page credit is claimed. Source and ledger application remain with root.

## Scope and exposure

The frozen argument proves the stated smooth compact threefold domain, rational H² vanishing, reduced divisor and reduced irreducible compact local complete-intersection critical curve, with each of the three specified generic transversal types. It proves both meromorphic pole bounds as well as the positive-genus smooth elliptic conclusion and constancy at every point. Earlier related C2d normal-jet work and its old C_jets routine had been encountered before the earlier runtime reset. The BF target proof, BF historical check and current A-checker's C2d proof were closed until the BF freeze. The target-specific conductor construction and the universal invariant program were written before release. This is not a claim of no prior exposure to related normal-jet mathematics.

## Exact notation and maps

The frozen normalization C→D and its inclusion into Y are the printed ν and j. The fresh rank-two E is printed N=(ν*(I/I²))*; fresh equation line L is printed M; fresh radical K is printed R; fresh quotient M is printed Q; fresh conductor Δ is printed Ξ. Thus the fresh a=deg K and b=deg M are printed deg R and deg Q, without any change to the underlying bundles.

Finite duality is implemented by Hom_A(B,A)={x in the total quotient ring: xB⊂A}, the conductor ideal of the normalization A⊂B, followed by tensoring with the invertible dualizing module. This gives ω_C=ν*ω_D(-Ξ). The regular-sequence conormal determinant gives det N=ν*ω_D⊗j*K_Y^{-1}. Rational H²(Y)=0 makes the pullbacks of O_Y(S) and K_Y degree zero, so deg N=2g−2+c. These are precisely A.J.1–2.

For the rank-one quadratic form the saturated radical is a line subbundle and the quotient is a line bundle; the nonzero form on the quotient gives b≤0. The injection of the locally free graded pieces into their normalization pullbacks is through the inclusion of the reduced ring into its normalization, so a quadratic or cubic class vanishing after pullback already vanishes over D. This checks the I² and I³ membership steps and their full reduced-lci scope.

For cusp clearing, fresh conductor lift H, product lift U and quadratic coefficient A0 correspond to printed d-hat, (dh)-hat and a-hat; fresh Z corresponds to printed P=d-hat X+(dh)-hat Y. The exact identity G=H²f−A0Z² is A.J.4. Its cubic restriction divided by d² is the same intrinsic radical cubic on the dense regular locus, hence the same meromorphic section on overlaps. Its pole divisor is at most 2Ξ. The inequalities a≤2c/3, b≤0, a+b=2g−2+c force g=1,c=0 under g>0. Degree-zero nonzero Hessian and cubic sections have no zeros, and the parametric Morse map followed by the local unit cube root gives the exact cusp equation at each point.

For the tacnode the vanished radical cubic yields [G]₃=ℓC₂ by monic polynomial division. Multiplication by the conductor descends every coefficient of C₂. Fresh R₂ is printed H and fresh J is printed K; the identity H_fresh⁴ f=A0 H_fresh² Z²+Z R₂+J is algebraically equivalent to printed A.J.7. The fresh invariant r₄=4αε−δ² equals exactly four times the printed invariant Δ=ae−b²/4. Consequently its bundle, zero divisor and pole bound agree, and division by 4 introduces no zero or pole. Both calculations give degree −8g+8+2b≥0 and hence g=1,b=0. This alone does not force c=0: both arguments next use the nowhere-zero Hessian coefficient, which is a unit in the local ring A, to obtain h=q_XY/a∈A. Repeating the exact construction with d=1 gives a holomorphic fourth invariant of degree −4c, forcing c=0. The parametric Morse map and fourth root give the constant tacnode equation.

For the triple case the generic vanishing of the quadratic class and local-free injection give f∈I³. The fresh cubic discriminant is the printed binary cubic discriminant: the product of the three squared exterior brackets has coefficient degree four and determinant character six. Thus its bundle is M⁴(det N)^{-6}. Its nonzero section forces 2g−2+c≤0; positive genus gives g=1,c=0. The zero-free discriminant separates the three holomorphic tangent roots. The first two branch equations give coordinate axes and the map y↦y/u(x,z) straightens the third y=xu(x,z) to y=x, preserving the first two axes. This is the printed every-point triple equation up to a unit.

## Exact lift clarification found during proposed-proof rereading

The original step 3 said to subtract a holomorphic lift of the whole quadratic class aℓ² and then claimed every change of lift is divisible by ℓ at cubic order. An arbitrary lift of that whole class can add a radical cubic. The final v2 explicitly chooses separate lifts a-hat and ℓ-hat and subtracts a-hat·ℓ-hat². Replacing a-hat by a-hat+A₁, A₁∈I, or ℓ-hat by ℓ-hat+L₂, L₂∈I², changes the cubic class by A₁ℓ²+2aℓL₂, which restricts to zero on R³. This is the product-of-lifts choice already made by the exact square in A.J.4. The clarification is a bounded D13 repair to that sentence, not a claim that an arbitrary quadratic-class lift works. The intrinsic section, all displayed formulas, theorem domain and final values are unchanged. P is also explicitly introduced at its first named use in the tacnode case rather than described as a previously named object.

## Computational comparison and limits

The old exact C_jets.py was read in full and actually run after BF release. It computes tacnode covariance by SymPy substitution in a quartic, and obtains the binary-cubic discriminant through SymPy followed by a diagonal rescaling. The fresh prerelease program uses sparse rational polynomial arithmetic: the tacnode scalar comes from the determinant of the quadratic form on (ℓ,r²), with unipotent matrix congruence, and the cubic discriminant comes from the product of three squared exterior brackets and the determinant of a general 2×2 change of basis. It separately verifies the conductor-clearing polynomial identity. These are different mathematical calculation routes, not only a software rewrite. The exact invariant comparison is r₄=4Δ. Both actual run receipts bind observed start/end times, exit status 0, code and output bytes. No historical pole-system output is counted as an additional BF or C2d check. Neither program proves the sheaf gluing, conductor bound, degree argument or analytic normal forms; those are proved in the frozen derivation and compared above.

## Publication and credit

Fourteen exact guards remove process/iteration residue, retain the full mathematical statement and every original displayed formula/tag/label, and make the two local notation/lift choices explicit. The program table proposal is one new row with its exact scope; the root must bind byte-identical code/output/receipt copies before application. Proposed event credit is one targeted proof check for the frozen derivation plus comparison and one used-and-rechecked event for the actual complete original/final proof rereading. There is no extra computation event, no credit for each cosmetic guard, and no event has been appended by this agent.
'''
comparison_path=f('S6_SERIES_PUBLISH_II_clean_group14_BF_comparison.md')
assert not comparison_path.exists()
comparison_path.write_text(comparison)
methods=save('S6_SERIES_PUBLISH_II_clean_group14_BF_computation_methods.json',{
    'schema_version':1,'paper':'II','tag':'01BF','created_utc':now,
    'prior_related_exposure':prior,
    'new_code':bind(f('S6_SERIES_PUBLISH_II_BF_prereading_invariant_certificate.py')),
    'new_output':bind(f('S6_SERIES_PUBLISH_II_BF_prereading_invariant_output.json')),
    'new_execution':bind(f('S6_SERIES_PUBLISH_II_BF_prereading_execution_receipt.json')),
    'old_code':bind('records/S6_SERIES_PUBLISH_II_opened_programs_recovery_01/C_jets.py'),
    'old_output':bind(f('S6_SERIES_PUBLISH_II_BF_old_C_jets_output.txt')),
    'old_execution':bind(f('S6_SERIES_PUBLISH_II_BF_old_program_execution_receipt.json')),
    'old_retrieval':bind('records/S6_SERIES_PUBLISH_II_opened_programs_recovery_01/receipt.json'),
    'actual_complete_code_and_output_read':True,
    'method_comparison':[
      {'quantity':'tacnode fourth invariant','old':'SymPy substitution x→x+u y² in quartic coefficients','new':'Sparse Fraction arithmetic and determinant of the quadratic-form congruence on (ell,r²)','exact_map':'new r4=4*old Delta; congruence determinant is one'},
      {'quantity':'binary cubic discriminant and character','old':'SymPy discriminant, then diagonal lambda/mu rescaling','new':'Product of three squared exterior brackets, coefficient identity and general GL2 determinant calculation','exact_map':'same cubic discriminant, determinant weight six and scalar coefficient degree four'},
      {'quantity':'conductor clearing','old':'No conductor-clearing routine occurs in the exact inspected C_jets file','new':'Exact sparse polynomial identity equivalent to A.J.7','exact_map':'fresh Z=P_print, R2=H_print, J=K_print'}],
    'timing':'New program run before BF freeze/release; exact historical file rerun after release. Earlier related C2d exposure is disclosed.',
    'exclusions':['No automatic proof of analytic extension or sheaf gluing','Old additional inverse-Jacobian/pole outputs supply no new BF or C2d event','No assertion about programs outside the exact inspected file'],
    'new_computation_event_count':0,'events_added':0})
validation=save('S6_SERIES_PUBLISH_II_clean_group14_BF_guard_validation.json',{
    'schema_version':1,'created_utc':now,'source':bind(source),
    'original_full_block':target['original_full_block'],'proposed_full_block':target['proposed_full_block'],
    'exact_guard_reconstruction':True,'guards':counts,'guard_count':len(counts),
    'literal_occurrences':sum(x['occurrences'] for x in counts),
    'current_original_occurrences':1,'all_original_display_math_unchanged':True,
    'all_labels_tags_hypertargets_unchanged':True,
    'automated_comparison_is_not_manual_reading_credit':True})
reading=save('S6_SERIES_PUBLISH_II_clean_group14_BF_final_pair_reading.json',{
    'schema_version':1,'created_utc':now,'paper':'II','checker':'i_provenance_recovery',
    'tag':'01BF','statement_owner':'cdp:st:A.5.5','freeze_receipt':freeze,'release_receipt':release,
    'original_full_block':target['original_full_block'],'proposed_full_block':target['proposed_full_block'],
    'actual_complete_original_statement_and_proof_read':True,
    'original_reading_timing':'After BF release and before preparation v1; retained actual reading, not inferred from archive existence.',
    'actual_complete_final_statement_and_proof_read':True,
    'final_reading_scope':'All 266 source lines, complete statement and eleven proof items, in contiguous lines 1–180 and 181–266 outputs after 2026-11-22 00:21:09 UTC and before this record.',
    'full_v1_read_before_v2_clarification':True,
    'comparison':bind(comparison_path),'method_record':methods,
    'findings':['Factorized quadratic lift specified, with exact cubic difference proof','P introduced where first named','Theorem domain, final values and all original displayed formulas preserved'],
    'page_images_read_for_this_record':0,'additional_independent_derivation_credit':0,
    'canonical_mutations':False,'events_added':0})
target.update({'checker':'i_provenance_recovery','freeze_receipt':freeze,'derivation':derivation,'release_receipt':release})
prep.update({'created_utc':now,'preparation':bind(f('S6_SERIES_PUBLISH_II_clean_group14_BF_preparation_v2.json')),
    'source_at_final_review':bind(source),'prereading_inputs':inputs,'comparison':bind(comparison_path),
    'computation_methods':methods,'final_pair_reading':reading,'guard_validation':validation,
    'full_proposed_reading_pending':False,'prior_exposure':prior,
    'mathematical_statement_and_values_unchanged':True,'displayed_final_conclusions_preserved':True,
    'scope_exceptions':['D13: specify the separate factor lifts for the intrinsic radical cubic; arbitrary lifts of the whole quadratic class are not authorized','D13: introduce P exactly at its first named use','All original display math, labels and tags remain byte-identical'],
    'prospective_counts':{'targeted_proof_check':1,'used_and_rechecked':1,'new_computation_event':0},
    'status':'Complete target-specific prereading derivation, different-method computation and full source-pair comparison; canonical application/admission pending root.'})
final=save('S6_SERIES_PUBLISH_II_clean_group14_BF_final_proposals.json',prep)
events=[]
for typ,scope in [
 ('targeted proof check','Complete BF derivation and universal invariant program frozen before its target proof, followed by complete printed-proof comparison; earlier related C2d exposure explicitly disclosed.'),
 ('used and rechecked in this run','Actual complete original/final v2 statement and eleven-item proof rereading after the fourteen exact guards, with no additional independent derivation.')]:
    events.append({'paper':'II','tag':'01BF','statement_owner':'cdp:st:A.5.5','checker':'i_provenance_recovery',
        'event_type':typ,'event_count':1,'scope':scope,'freeze_receipt':freeze,'frozen_derivation':derivation,
        'release_receipt':release,'original_full_block':target['original_full_block'],'proposed_full_block':target['proposed_full_block'],
        'proposal_bundle':final,'comparison':bind(comparison_path),'computation_methods':methods,'final_pair_reading':reading,
        'source_application_pending':True,'proposal_only':True,'no_extra_computation_event':True,
        'mathematical_statement_and_values_unchanged':True,'prior_exposure':prior,
        'scope_exceptions':prep['scope_exceptions']})
eventfile=save('S6_SERIES_PUBLISH_II_clean_group14_BF_event_proposals.json',{
    'schema_version':1,'paper':'II','created_utc':now,'proposal_only':True,'events':events,
    'prospective_counts':prep['prospective_counts'],'canonical_mutations':0,'events_added':0})
print(json.dumps({'final_proposals':final,'event_proposals':eventfile,'final_pair_reading':reading,'comparison':bind(comparison_path),'guard_count':len(counts)},indent=2))
