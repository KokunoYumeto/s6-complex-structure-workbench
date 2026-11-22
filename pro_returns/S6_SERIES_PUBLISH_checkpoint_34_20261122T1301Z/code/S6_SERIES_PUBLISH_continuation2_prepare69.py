from pathlib import Path
import csv, datetime as dt, hashlib, json, re

R = Path(__file__).resolve().parents[1]
def bind(p):
    b = (R/p).read_bytes()
    return dict(path=p, sha256=hashlib.sha256(b).hexdigest(), bytes=len(b))
def read(p):
    return json.loads((R/p).read_text())
def check(b):
    assert bind(b['path'])['sha256'] == b['sha256'], b['path']

pre = 'agents/continuation2_B/01CE/S6_SERIES_PUBLISH_II_B2_CE_'
ip = pre+'packet_index.json'
idx = read(ip)
assert bind(ip)['sha256'] == '61c3e9ade216e7b7fe73b5e8a6e6b17a840590999d418f86deaf243f71bc3924'
for b in [idx['admission'], idx['events'], *idx['files'], *idx['external_frozen_inputs']]:
    check(b)
ap = pre+'admission_proposal.json'
a = read(ap)
t = a['targets'][0]
assert bind(ap)['sha256'] == 'f70235d4d1f71f1c9fa908124d431b174400f7d00ee1c28f2664d6bd97007921'
guards = [dict(old=g['old'], new=g['new'], type=g['defect_type'], reason=g['reason']) for g in t['guards']]
assert len(guards) == 9
guards[-1]['type'] = 'D22,D25'
guards[-1]['reason'] += ' Root classification: D25 applies to the invalid scope application in the original proof; the immutable proposal classified it D22. The theorem and all displayed formulas remain unchanged.'
old = (R/t['original_full_block']['path']).read_text()
new = (R/t['proposed_full_block']['path']).read_text()
w = old
for g in guards:
    assert w.count(g['old']) == 1
    w = w.replace(g['old'], g['new'], 1)
assert w == new
assert old.count('\\item') == new.count('\\item') == 4
displays = re.findall(r'\\\[(.*?)\\\]', old, re.S)
assert displays == re.findall(r'\\\[(.*?)\\\]', new, re.S) and len(displays) == 4
for pat in [r'\\label\{([^}]+)\}', r'\\hypertarget\{([^}]+)\}', r'\\tag\{([^}]+)\}']:
    assert re.findall(pat, old) == re.findall(pat, new)
repair = dict(a['mathematical_repairs_to_original_source'][0])
repair.update(defect_type='D22,D25', original_proposal_defect_type='D22', root_classification_reason='The cited A.RT.21 has an explicitly restricted domain which excludes the r<=2 configuration established here. Its application as the final Euler justification was therefore unsupported. The replacement proves the required bound for the actual tree configuration at every r, with no alteration to the proposition.')
now = dt.datetime.now(dt.timezone.utc).isoformat()
review = 'records/S6_SERIES_PUBLISH_II_root_continuation2_batch69_review.json'
evidence = [bind(ip), bind(ap), a['review'], a['draft_clarification_guards'], a['draft_clarification_diff'], a['identity_guard_replay'], a['final_read_receipt'], t['derivation'], t['prerelease_read_receipt'], t['freeze_receipt'], t['release_receipt'], *a['primary_reading']]
for cp in a['computations']:
    evidence.extend([cp['program'], cp['output'], cp['receipt']])
for b in evidence:
    check(b)
rd = dict(
    created_utc=now,
    checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, root, second continuation; reasoning effort not separately exposed',
    actual_reading='Root read the entire 23858-byte frozen derivation, all four original and final proof items, all four complete-block displays, the entire comparison, all nine target guards, the Programs guard, both complete program sources and every output row (34 and25 checks), the two draft clarification guards, exact dependency proofs/passages 02Y2 and A.RT.16-21, freeze/release, prereading/final/dependency reading receipts and both execution receipts. The initial combined frozen-derivation/admission tool output truncated the final part of the frozen derivation: those remaining lines were then fully read after admission-guard exposure and before opening the complete original/final target. No truncated text receives reading credit. Root review is comparative, not an additional independent derivation.',
    mathematical_review=[
        'The actual hypotheses are the smooth torus degeneration with b2(Y;Q)=0, a rational normalization and the specified morphism from the ruled-boundary resolution. Its horizontal strict transform C is a smooth rational coefficient-two section, maps with degree2 onto the smooth rational tacnode image H, and has arbitrary vertical conductor elsewhere. Adjunction gives deg N_H/Y=-2 and topological triviality gives deg M=0. With saturated radical R=O(ell) and Q=N/R of degree-2-ell, the quadratic section is in M Q^-2 of degree4+2ell. The quartic discriminant belongs to M^2 Q^-2 R^-4 of degree4-2ell. For x_old=alpha*x_new+beta*y_new^2, y_old=gamma*y_new, and equation unit mu, the three coefficients become mu*alpha^2*A, mu*(alpha*gamma^2*B+2*alpha*beta*A), and mu*(gamma^4*C+beta*gamma^2*B+beta^2*A); B^2-4AC transforms by mu^2*alpha^2*gamma^4. Individual mixed/quartic coefficients have affine transitions, as explicitly corrected before release.',
        'The exact two blowup charts x=y*v and v=y*w yield A*w^2+B*w+C+y*Phi=0. At the generic point its distinct roots give smooth branches mapping by (w,y,t) to (y^2*w,y,t). Their finite birational map is the normalization there. The inverse quadratic-function-field maps are d=A*w+B/2 and w=(d-B/2)/A for d^2=B^2/4-AC. Integral closure identifies this same cover with C. A local odd zero k has t=s^2 and d=s^k*sqrt(u(s^2)), with inverse s=d/(t^((k-1)/2)*sqrt(u(t))); even zeros give two unramified branches. Riemann-Hurwitz for P1 to P1 degree2 gives exactly two distinct branch images.',
        'A nonzero Hessian gives the completed B7 constant transverse A3 product; its normalization has the two maps X=plus-or-minus Y^2 and conductor parameter Z, hence is unramified and has no vertical conductor. At a branch image A must vanish. A simple discriminant zero there would force A to have a simple zero, B to vanish and C to be a unit. The frozen derivation uses weights (3,2,2), the map T=A, a fourth-root change of Y and the rescaling F_s=s^-8 F(s^3 X,s^2 Y,s^2 T). Its main term is X^2*T+Y^4, identified with B5 by (x_B5,y_B5,z_B5)=(Y,X,-T), with (a,b,c)=(4,2,1) and sphere square-4. The written compact differential lift -partial_s(F_s)*conj(grad F_s)/norm(grad F_s)^2 has the reverse flow as inverse and carries the full compact intersection data into an actual nearby torus. Its pi2 vanishes, contradicting the square. The original exact B8 coordinate route is retained: complete the square using b/a, then the displayed fourth-root shear makes F-Y^4 divisible by X^2 and Z=(F-Y^4)/X^2 has nonzero z derivative. This gives the exact same excluded Y^4+X^2 Z germ.',
        'Each of the two branch images has an odd discriminant order at least3. The nonzero quadratic section has nonnegative degree4+2ell and the discriminant has degree4-2ell. Thus ell is-1: ell=-2 would give no quadratic zero, and ell>=0 gives insufficient discriminant degree. Equivalently the retained q0 notation gives A=-2q0=2 and discriminant degree6. The two branch images exhaust the zeros of the quadratic section, each simple, and both discriminant orders are3.',
        'Each original vertical fibre meets the coefficient-two section at a distinct point. A blowup at an attachment with vertical multiplicity v>=1 creates coefficient2+v-1=v+1, preserving a positive attachment; the strict section maps isomorphically to its predecessor. Every attachment maps to a Hessian zero, and each of the two Hessian zeros is a ramification image with one point above it. Therefore r<=2. The coefficient formula K_new=beta^*K+E and D_new=beta^*D-E gives a_E=mu-1; multiplicity1 leaves the reduced support unchanged while raising the complement Euler number by1, and multiplicity>=2 raises both surface and boundary Euler numbers by1. This proves the exact e(S)=2-r+N0+e(Gamma_red) used in the final display.',
        'Root read the exact A.RT.16-21 passage and confirmed that A.RT.21 is announced under the negative-boundary hypotheses, including at least3 vertical fibres in the ruled case. That scope excludes the r<=2 configuration just proved, so the old final citation leaves a real proof gap. The replacement starts with C0 union F1...Fr, a connected simply connected rational tree, and follows every reverse blowup: support unchanged, leaf addition, or edge subdivision. Z is simply connected. Completed B6 says h is an isomorphism off Gamma_red and h^-1(Gamma_red)=D_red. Consequently the explicit map from Z union_D Gamma to S, [z] to h(z) and [gamma] to gamma, is a compact-to-Hausdorff continuous bijection and thus a homeomorphism. A triangulated cofibration and its double mapping cylinder give the inclusion-induced isomorphism pi1(Gamma_red)=pi1(S); the frozen derivation supplies the explicit mapping-cylinder equivalence.',
        'Every normalized Gamma component is rational since it is dominated by a component of D. Its incidence graph gives pi1(Gamma)=F_b and e(Gamma)=c+1-b. Root read the complete 02Y2 proof: a barycentric retraction V to S and a full tube U inside V give surjections from the punctured tube group to pi1(S). The torus mapping-torus group is Z4 semidirect Z; a multiplicity-m meridian kills m times the base generator and leaves an abelian normal subgroup with finite cyclic quotient. This uses no b1(Y) condition. A finite-index abelian subgroup in F_b with b>=2 would contain nonzero powers of two free generators, whose commutator is nontrivial. Hence b<=1 and e(Gamma)>=c. For c=1 the image is the given smooth rational H and has Euler number2; for c>=2 the same lower bound is already2. Thus e(S)>=4-r+N0>=2+N0. This proves precisely the missing application, with the original statement and its four displays unchanged.',
        'The prereading program supplies34 exact checks by weighted substitution, Sylvester elimination, quadratic-cover field maps, line-bundle degrees and Euler formulas. The independent comparison program supplies25 checks through Gram-matrix congruence and determinant, printed-root algebra, branch degree inequalities and integer Euler updates. All59 checks pass and both entire sources/outputs were read; analytic and topological conclusions are supplied by the written proofs. Root adds no computation event beyond the one agent event. The two unadmitted draft clarifications make the normalization charts and the full inverse-image input explicit, and are kept immutably.'
    ],
    chronology='Agent complete derivation freeze08:02:47.185020 UTC precedes target release08:02:49.638935 UTC. Supporting B5/B7/B1/WY work and the statement-only 02Y2 input are explicitly disclosed. Root completed the frozen text after seeing admission guards but before the full target, so no full-root-preexposure claim is made. One independent evidence group and three events.',
    mathematical_errors_found_in_original=[repair],
    defect_classification=dict(proposal='D22', canonical='D22,D25', register=bind('S6_DEFECT_REGISTER.csv'), reason='D25 covers an incorrect proof reason. The old restricted Euler bound was applied outside its announced scope; the complete replacement proves the actual application.'),
    original_proof_items_preserved=4,
    original_displays_preserved=4,
    publication_page_reading_credit=0,
    evidence=evidence,
)
assert not (R/review).exists()
(R/review).write_text(json.dumps(rd, indent=2)+'\n')
with (R.parent/'S6_SERIES_GRIND_tags.tsv').open() as f:
    pages={x['tag']:x['page'] for x in csv.DictReader(f,delimiter='\t')}
target=dict(owner=t['statement_owner'], tag=t['tag'], old_page=pages[t['tag']], original=t['original_full_block'], proposed=t['proposed_full_block'], freeze=t['freeze_receipt'], release=t['release_receipt'], events=idx['events'], guards=guards, who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort not separately exposed; checker continuation2_B', scope='Full stated rational double cover of a smooth tacnode image, arbitrary vertical conductor and singular normalization: r<=2 and e(S)>=2+N0.', event_note='Root complete comparative review at '+now+'. All four original items and four displays retained. The old A.RT.21 scope application is repaired by the full rational-tree conductor argument; D25 classification added to original D22 proposal. One independent evidence group; root comparative work adds no independent count.')
extra=[dict(old=g['old'],new=g['new'],type=g['defect_type'],owner=g['location'],location=g['location'],reason=g['reason']) for g in a['additional_source_guards']]
copies=[dict(**{'from':cp[k]},to='code/'+Path(cp[k]['path']).name) for cp in a['computations'] for k in ['program','output']]
cfg=dict(batch=69, root_review_complete=True, source_before_sha256=bind('S6_SERIES_PUBLISH_II.tex')['sha256'], ledger_before_sha256=bind('CHECK_EVENTS.tsv')['sha256'], review_evidence=[bind(review)]+evidence, targets=[target], additional_source_edits=extra, code_copies=copies, mathematical_repairs=[repair], scope='01CE admitted after complete prerelease derivation and full original/final four-item comparison. All four displays and the original statement are preserved. The invalid application of the restricted A.RT.21 Euler bound is repaired for the actual section-and-fibres tree at every r by explicit conductor-pushout and local-group arguments (D22,D25). Nine target guards, one Programs edit, three events in one group;59 exact computational checks. No global defect or page-reading closure.')
assert cfg['source_before_sha256']=='ea15d3b2b362c3438808cb19c36e55b4da3dc3974b988962214d94e3ac377246'
assert cfg['ledger_before_sha256']=='61e79a7a06e6c4bd94721828a6e626e55da310061fecece03eb19d29c2ed6df0'
out='records/S6_SERIES_PUBLISH_II_continuation2_batch69_config.json'
assert not (R/out).exists()
(R/out).write_text(json.dumps(cfg,indent=2)+'\n')
print(json.dumps(bind(out)))
