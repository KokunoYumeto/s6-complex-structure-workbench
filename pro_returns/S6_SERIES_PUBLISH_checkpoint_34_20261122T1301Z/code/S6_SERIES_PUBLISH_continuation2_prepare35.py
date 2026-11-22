from pathlib import Path
import datetime as dt
import hashlib
import json

R = Path(__file__).resolve().parents[1]
def read(p): return json.loads((R/p).read_text())
def bind(p): return {'path':p,'sha256':hashlib.sha256((R/p).read_bytes()).hexdigest()}

paths = [
 'agents/continuation2_B/01FQ/S6_SERIES_PUBLISH_II_B2_FQ_admission_proposal.json',
 'agents/continuation2_B/01FN/S6_SERIES_PUBLISH_II_B2_FN_admission_proposal.json',
 'agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_group01_proposals.json']
proposals = [read(p) for p in paths]
review = 'records/S6_SERIES_PUBLISH_II_root_continuation2_batch35_review.json'
assert not (R/review).exists()
scopes = {
 '01FQ': 'Full original/proposed five-item proof and frozen derivation compared; finite-etale torus cover and full u-adic thickening give the claimed generic vanishing in every Picard component, including torsion first Chern classes.',
 '01FN': 'Full original/proposed five-item proof and frozen derivation compared; exact integral-CDP domain, transgression, full-fibre cases, Leray, endpoint index and fixed nonnormal obstruction checked.',
 '033D': 'Full original/proposed six-item proof and independent derivation compared; unique divisibility, rank-two central-section injection, meromorphic-map theorem, Stein base and common fixed divisor checked.',
 '033E': 'Full original/proposed nine-item proof and independent derivation compared; canonical-fibre restriction, verticality, connected divisor limit, evaluation, slope and opposite-sign arguments checked.',
 '032V': 'Full original/proposed three-item proof and independent derivation compared; negative-slope Hopf exclusion and exact transport of the connected-divisor-limit argument checked.'}
mathematics = [
 'FQ: primary AC26 Theorems 7.17 and 7.22 cover the stated original affine examples, including |p|>1. Integral-CDP A.3.4 cannot be invoked with torsion H2; finite-order representatives in each Picard component, irrational integral transgression, the finite-etale torus cover and the u-adic filtration prove the same full-fibre vanishing. Finite transfer preserves the nonzero character. The normalization tangent obstruction and Euler values remain unchanged.',
 'FN: the original full hypotheses of CDP20 Theorem 2.2 already import smoothness and a=1, now stated explicitly through the identity on Y and f. The conormal argument proves m=1 and A.3.4 proves m>=2. Proper analytic bad loci on the parameter line are discrete unless full; the finite set of singular fibres allows a simultaneous parameter. Serre duality, top base change, a sufficiently positive integral base twist, Leray and the endpoint index give the stated vanishing and inequalities. Index parity gives c3>0 => b3=0; the fixed obstruction support is nonnormal by the smooth-reduction argument.',
 '033D: H1 and H2 integral vanish on the total family by the smooth product topology, giving Pic=H1(O) and unique roots. The direct-image module is torsion free over the disc; its rank-two special-fibre quotient injects into H0 of the central fibre. CDP20 Theorem 2.1 and LRS Theorem 3.1/Corollary 3.2 imply that a meromorphic function on this S6 cannot have indeterminacy; the two-function quotient argument then forces algebraic dimension one. Stein factorization has base P1 by H1 injection. The local principal-ideal construction gives the exact common fixed divisor.',
 '033E: positive D makes KF effective. A positive fibre Kodaira dimension would produce meromorphic functions transverse to the reduction after a base twist; hence kappa=0. Minimality and the torsion canonical line imply that the effective restriction is zero, proving verticality. The total zero divisor of a generic pencil section is proper and flat with smooth connected generic torus fibre, irreducible and generically reduced. The normalized proper divisor has connected central support by Stein factorization, excluding both positive vertical fixed part and base degree greater than one. Evaluation then produces a smooth central torus fibre and the slope identity. The opposite-sign argument uses the separately frozen negative branch, with no derivational cycle; torsion K would give a holomorphic volume form contradicting H3=0 by Stokes.',
 '032V: negative D and horizontal fixed part would produce the Hopf case in E.2.8, excluded by E.2.9. Verticality supplies exactly the hypotheses used in the connected-divisor argument of E.2.6. The same holomorphic pencil line on the common limit is nontorsion; equal rational canonical slopes recover the same admissible integer pair by the displayed arithmetic formula.'
]
(R/review).write_text(json.dumps(dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
 checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, root, second continuation',
 actual_reading='Complete original and proposed blocks, frozen derivations and comparative reviews for all five owners; exact scope and source locators examined. Prior-to-compaction readings are retained, with all review findings reproduced here.',
 mathematical_review=mathematics, statement_conclusions_changed=False,
 independence='One targeted event per owner, preserving the FQ inherited freeze and the other fresh freezes. Root comparison adds no independent route. No computation event is added for these five checks.',
 page_reading_credit=0, evidence=[bind(p) for p in paths]),indent=2)+'\n')
targets=[]
for p in proposals:
 for t in p['targets']:
  tag=t['tag']; owner=t['statement_owner']
  if tag in ('01FQ','01FN'):
   freeze=t['freeze_receipt']; release=t['release_receipt']
   event=bind(f'agents/continuation2_B/{tag}/S6_SERIES_PUBLISH_II_B2_{tag[2:]}_event_proposals.json')
   who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, checker continuation2_B'
  else:
   prefix=f'agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_{tag}'
   freeze=bind(prefix+'_freeze.json'); release=bind(prefix+'_release.json')
   event=bind('agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_group01_event_proposals.json')
   who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, checker continuation2_C'
  targets.append(dict(owner=owner,tag=tag,old_page={'01FQ':'264','01FN':'259','033D':'310','033E':'311','032V':'320'}[tag],
   original=t['original_full_block'],proposed=t['proposed_full_block'],freeze=freeze,release=release,events=event,who=who,
   guards=[dict(old=g['old'],new=g['new'],type=g['defect_type'],reason=g['reason'],occurrences=g['expected_occurrences_in_owning_block']) for g in t['guards']],
   scope=scopes[tag],event_note='Admitted after complete root comparative review. Exact original/proposed block hashes and freeze/release chronology are preserved; no additional independent credit for the root review.'))
cfg=dict(batch=35,root_review_complete=True,
 source_before_sha256=bind('S6_SERIES_PUBLISH_II.tex')['sha256'],ledger_before_sha256=bind('CHECK_EVENTS.tsv')['sha256'],
 review_evidence=[bind(review)]+[bind(p) for p in paths],targets=targets,
 mathematical_repairs=[x for p in proposals for x in p.get('mathematical_repairs',[])],
 scope='Five complete checks are admitted. The three deformation-limit proofs retain their mathematical conclusions with exact primary locators and explicit line-bundle maps. FQ replaces an inapplicable integral-cohomology input by a direct torus-cover and nilpotent-filtration proof. FN separates multiplicity one from the cited multiplicity-at-least-two lemma and states the already imported CDP hypotheses explicitly. All five statements retain their scope and conclusions. No new computation event or page-image reading credit is assigned.')
out=R/'records/S6_SERIES_PUBLISH_II_continuation2_batch35_config.json'
assert not out.exists()
out.write_text(json.dumps(cfg,indent=2)+'\n')
print(json.dumps(bind(str(out.relative_to(R))),indent=2))
