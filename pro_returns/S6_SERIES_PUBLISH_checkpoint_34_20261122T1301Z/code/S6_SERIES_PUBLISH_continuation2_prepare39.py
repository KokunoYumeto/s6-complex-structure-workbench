from pathlib import Path
import csv,datetime as dt,hashlib,json
R=Path(__file__).resolve().parents[1]
def read(p):return json.loads((R/p).read_text())
def bind(p):return {'path':p,'sha256':hashlib.sha256((R/p).read_bytes()).hexdigest()}
paths=['agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_X3_admission_recommendation.json','agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_X6_admission_recommendation.json']
recs=[read(p) for p in paths]
review='records/S6_SERIES_PUBLISH_II_root_continuation2_batch39_review.json'
assert not (R/review).exists()
(R/review).write_text(json.dumps(dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
 checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, root, second continuation; reasoning effort not separately exposed',
 actual_reading='Complete frozen derivations, original and proposed six-item 02X3 and four-item 02X6 proofs, full comparisons, event proposals and exact guards read. The full original 02X6 block was reread after combined tool output cut its middle. The exact P4.12 statement was read to verify the standing-domain transport. Stacks primary tags 0B5B and 01UM were reopened by root.',
 mathematical_review=[
 '02X3: the symbolic conormal is the torsion-free image of differentiation. Its normalization span F lies in the saturated differential kernel V. The exact sequence 0->nu_*F/M->nu_*V/M->nu_*(V/F)->0 proves tau=q+ell and transports the two Euler formulas. The primitive derivative row makes wedge^2 V have a unit coordinate, so the determinant ideal measures the DVR colength. Gradient valuations are at least 2m for embedding dimension three and at least m in the plane case. The normalization and symbolic-square sequences give chi(O/P^(2))<=-delta; equality makes normalization an isomorphism. The cited standing domain supplies precisely the zero ambient Chern pairing.',
 '02X6: evaluation at 1 and multiplication are inverse conductor/Hom maps in the common total quotient algebra. Hypersurface change of rings gives the canonical-module identification, and normality supplies Cohen-Macaulay depth two. A nonzero torsion-line section is nowhere zero and cannot lie in the proper conductor; analytic duality gives H2(N,O)=0. That is the exact vanishing shortening Leray. Torsion Riemann-Roch is applied on the smooth resolution, and the equal finite-length R1 terms transport Euler characteristics back to N. The diagonal/difference conductor square keeps the full scheme structures. For noncontracted H, the ruling is constant on every connected resolution fibre and descends to q, with q composed with the section equal to the identity. The two cohomology injections prove h1(N)=g and p=0. For contracted H, its constant composite and the inverse ruling/restriction maps prove h1(N)=0 and p=g.'
 ],statement_changed=False,page_reading_credit=0,computation_events=0,
 evidence=[bind(p) for p in paths],primary_reopened=[dict(url='https://stacks.math.columbia.edu/tag/0B5B',ref='turn124229995view0'),dict(url='https://stacks.math.columbia.edu/tag/01UM',ref='turn124229995view1')]),indent=2)+'\n')
with (R.parent/'S6_SERIES_GRIND_tags.tsv').open() as f:pages={x['tag']:x['page'] for x in csv.DictReader(f,delimiter='\t')}
targets=[]
for rec in recs:
 ed=read(rec['proposal']['path']);assert not ed['bibliography_guards'] and not ed['program_rows']
 for t in rec['targets']:
  tag=t['tag']
  targets.append(dict(owner=t['statement_owner'],tag=tag,old_page=pages[tag],original=t['full_original_block'],proposed=t['proposed_full_block'],freeze=t['freeze_receipt'],release=t['release_receipt'],events=rec['event_proposals'],
   who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, ii_checks_a2, second continuation; reasoning effort not separately exposed',
   guards=[dict(old=g['literal_old'],new=g['literal_new'],type=','.join(g['defect_types']),reason=g['reason']) for g in ed['guards'] if g['tag']==tag],
   scope={'02X3':'Full symbolic-double Euler inequality, with exact normalization-span and finite-pushforward length morphisms.','02X6':'Full normalization cohomology, scheme conductor Euler identity and both section-contraction alternatives.'}[tag],
   event_note='Full original and proposed proofs independently compared by root after the checker freeze-before-release process. All mathematical statements and original displays preserved. Root comparison creates no additional independent route or event.'))
cfg=dict(batch=39,root_review_complete=True,source_before_sha256=bind('S6_SERIES_PUBLISH_II.tex')['sha256'],ledger_before_sha256=bind('CHECK_EVENTS.tsv')['sha256'],review_evidence=[bind(review)]+[bind(p) for p in paths],targets=targets,additional_source_edits=[],code_copies=[],
 mathematical_repairs=[dict(owner='night:P4.33',type='D18,D20,D22',scope='The noncontracted-section conclusion used an unspecified comparison in the P4.29 proof.',repair='Write the ruling descent q composed with rho_N equals a and the section identity q composed with s equals id_E, then apply the precise split cohomology maps and Leray injection. No assertion is made about the unopened P4.29 proof.',statement_changed=False)],
 scope='Two complete independent checks are admitted. The symbolic-conormal argument now gives the exact normalization/pushforward module comparison; the normalization-conductor argument gives the exact canonical-module, conductor-square and descended-ruling morphisms. Both retain the original hypotheses, conclusions, displays, labels and tags. No numerical program or page-image credit is claimed.')
out='records/S6_SERIES_PUBLISH_II_continuation2_batch39_config.json';assert not (R/out).exists();(R/out).write_text(json.dumps(cfg,indent=2)+'\n');print(json.dumps(bind(out),indent=2))
