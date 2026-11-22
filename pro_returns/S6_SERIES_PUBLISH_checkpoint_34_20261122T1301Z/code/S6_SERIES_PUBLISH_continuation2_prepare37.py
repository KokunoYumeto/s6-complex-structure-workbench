from pathlib import Path
import datetime as dt
import hashlib,json
R=Path(__file__).resolve().parents[1]
def read(p):return json.loads((R/p).read_text())
def bind(p):return {'path':p,'sha256':hashlib.sha256((R/p).read_bytes()).hexdigest()}
paths=['agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_Hopf_admission_recommendation.json',
 'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_YL_admission_recommendation.json',
 'agents/continuation2_B/01FS/S6_SERIES_PUBLISH_II_B2_FS_admission_proposal.json']
h,y,f=[read(p) for p in paths]
review='records/S6_SERIES_PUBLISH_II_root_continuation2_batch37_review.json'
assert not (R/review).exists()
(R/review).write_text(json.dumps(dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
 checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, root, second continuation',
 actual_reading='All seven YH, six YK, three YL and six FS original/proposed proof items, complete frozen derivations and comparative reviews read. YK full amended block reread after root found its numerical/torsion scope issue.',
 mathematical_review=[
 'YH/YK: canonical divisor torsion descends to the minimal Hopf surface, forcing a nonempty pole divisor. Reverse blowups with exceptional coefficient mu-1 preserve elliptic roots with rational trees. The full finite/proper quotient is a compact-to-Hausdorff homeomorphism and analytic-pair triangulation gives the group pushout. Killing vertex groups gives the free quotient of rank b+r-s. The negative Euler extremum has c=r=g; the printed local hypersurface branch intersection excludes it. The independently frozen alternative extends a nonzero rational Hopf character through the inverse rational matrices of the elliptic isogenies and exhibits F2 in the remaining free product. The actual normalization maps and contracted exceptional fibres agree in both arguments.',
 'YK correction: numerical triviality alone allows D=0 on a Hopf surface with b2=0, contradicting the claimed nonempty pole support. The actual YI canonical line identity and WJ torsion of omegaS give the stronger torsion input. Pushforward then makes K_T0+D0 torsion; D0=0 would make the Hopf canonical line torsion, contradicting its Kodaira dimension. The amended proof now states exactly this chain; no statement changes.',
 'YL: the reduced horizontal alternative has two simple smooth elliptic branches or one smooth bisection; reverse blowups create no pole exceptional. The YI incidence condition excludes every exceptional configuration of the normalization resolution. The coefficient-one transverse conductor calculation in WU supplies finite differential rank drop, and WM then gives minimality and Euler zero. For the doubled section, explicit root inclusion/tree collapse and ruling maps give pi1(A)≅pi1(T); the inverse amalgam map identifies pi1(S) with pi1(C), including contracted fibres. Virtual abelianness and curve Euler formula give the bound.',
 'FS: exact original-family root-bundle inputs specialize the already available I theorem with k=l=1. The logarithmic base derivative identifies the O(-5) quotient. The cup map between two O(-1) lines is a nonzero scalar. Nonzero coefficient frame scalings, the shear and quotient maps, and u->1,v->-y/x prove all cokernel identities. Local freeness at p0 forces the nonzero elementary extension O(-6)(p0)=O(6). Unique residue factors x^r2 y^r1 identify root/coarse sections and inverse maps in every integer degree. The Q character calculation and two-column Leray give all dimensions. The normalization map is the p0 evaluation quotient; the semigroup and n=-1 exception agree. The Hilbert rational-identity/recurrence method is distinct from the old monomial/Smith routine.'
 ],statement_conclusions_changed=False,page_reading_credit=0,independence='One required independent route per owner; YH/YK share one joint route and certificate. Computation associations are not extra full proof methods. Root comparative reading adds no event.',evidence=[bind(p) for p in paths]),indent=2)+'\n')
targets=[]
pages={'02YH':'224','02YK':'227','02YL':'229','01FS':'268'}
for rec in (h,y):
 ed=read(rec['proposal']['path'])
 assert ed['bibliography_guards']==[]
 for t in rec['targets']:
  tag=t['tag']
  targets.append(dict(owner=t['statement_owner'],tag=tag,old_page=pages[tag],original=t['full_original_block'],proposed=t['proposed_full_block'],
   freeze=t['freeze_receipt'],release=t['release_receipt'],events=rec['event_proposals'],
   who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, ii_checks_a2, second continuation',
   guards=[dict(old=g['literal_old'],new=g['literal_new'],type=','.join(g['defect_types']),reason=g['reason']) for g in ed['guards'] if g['tag']==tag],
   scope={'02YH':'Complete smooth Hopf normalization Euler proof with disconnected conductor and exact finite pushout.',
    '02YK':'Complete Hopf normalization-resolution proof, full proper pushout, exceptional incidence and explicit torsion canonical input.',
    '02YL':'Complete elliptic ruled resolution proof; reduced-horizontal minimality through finite rank drop, and doubled-section proper pushout.'}[tag],
   event_note='Admitted after full root comparison; the YK intermediate numerical-only claim is corrected using the already supplied torsion canonical identity. Mathematical statements and labels remain.'))
t=f['targets'][0]
targets.append(dict(owner=t['statement_owner'],tag='01FS',old_page=pages['01FS'],original=t['original_full_block'],proposed=t['proposed_full_block'],
 freeze=t['freeze_receipt'],release=t['release_receipt'],events=bind('agents/continuation2_B/01FS/S6_SERIES_PUBLISH_II_B2_FS_event_proposals.json'),
 who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, continuation2_B',
 guards=[dict(old=g['old'],new=g['new'],type=g['defect_type'],reason=g['reason'],occurrences=g['expected_occurrences_in_owning_block']) for g in t['guards']],
 scope='Complete integral-twist direct-image and cohomology formulas, exact normalization-map rank set and exceptional twist, from the inherited frozen derivation and distinct Hilbert certificate.',
 event_note='Inherited freeze and event chronology retained. Exact root/coarse maps and cokernel inverses supplied, with the statement and every displayed formula unchanged.'))
source=(R/'S6_SERIES_PUBLISH_II.tex').read_text();st=source.index('\\caption{Programs and their mathematical scope.}');end=source.index('\\end{longtable}',st)
last=source[:end].splitlines(True)[-1];assert source.count(last)==1
row=(R/h['program_row']['path']).read_text()
name=Path(f['computation']['program']['path']).name
row+='Hilbert-series numerator, coefficient recurrence and integral-twist Euler identities (\\cref{cdp:st:C5b}) & '+r'\href{https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\SsixRepositoryCommit/code/'+name+r'}{\nolinkurl{'+name+r'}} \\[3pt]'+'\n'
copies=[{'from':f['computation'][key],'to':'code/'+Path(f['computation'][key]['path']).name} for key in ['program','output']]
cfg=dict(batch=37,root_review_complete=True,source_before_sha256=bind('S6_SERIES_PUBLISH_II.tex')['sha256'],ledger_before_sha256=bind('CHECK_EVENTS.tsv')['sha256'],
 review_evidence=[bind(review)]+[bind(p) for p in paths],targets=targets,code_copies=copies,
 additional_source_edits=[dict(old=last,new=last+row,type='D09',reason='Add the two reviewed exact programs to the Programs table, preserving all existing rows and the common pinned-commit macro.')],
 mathematical_repairs=[dict(owner='night:P4R.8',type='D13,D25',scope='Numerical triviality alone was claimed to force a nonempty pole support.',repair='Use the exact torsion canonical line identity from the cited pole-divisor and fibre results; D=0 on a Hopf surface supplies the counterexample to the weaker intermediate hypothesis.',statement_changed=False),
 dict(owner='night:P4R.9',type='D18,D22',scope='P4.22 statement was cited as proving minimality directly.',repair='Use its reduced-horizontal proof calculation to obtain finite rank drop, then the exact P4.15 statement.',statement_changed=False)],
 scope='Four complete checks are admitted: the smooth and resolved Hopf normalization cases, the elliptic ruled resolution case, and the integral-twist normalization-map calculation. Root review found that the Hopf-resolution proof needed torsion of the canonical divisor, not merely numerical triviality; the already available canonical line identity now supplies it explicitly. The elliptic ruled proof states its finite-rank-drop/minimality input precisely. All theorem statements retain their hypotheses and conclusions. The new rational-character Hopf proof remains in the check record; the paper retains its local-hypersurface proof. Two Programs entries are added with their actual methods and scope.')
out='records/S6_SERIES_PUBLISH_II_continuation2_batch37_config.json';assert not (R/out).exists();(R/out).write_text(json.dumps(cfg,indent=2)+'\n');print(json.dumps(bind(out),indent=2))
