from pathlib import Path
import csv, datetime as dt, hashlib, json, re

R = Path(__file__).resolve().parents[1]
def bind(p):
    b = (R/p).read_bytes()
    return dict(path=p, sha256=hashlib.sha256(b).hexdigest(), bytes=len(b))
def read(p): return json.loads((R/p).read_text())
def check(b):
    a = bind(b['path'])
    assert a['sha256'] == b['sha256'], b['path']
    if 'bytes' in b: assert a['bytes'] == b['bytes'], b['path']

pre = 'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_YC_v1_20261122/S6_SERIES_PUBLISH_II_A2_YC_'
mp = pre+'v1_manifest.json'; ap = pre+'admission_recommendation.json'
m = read(mp); a = read(ap); t = a['targets'][0]
assert bind(mp)['sha256'] == 'f6f01711251b3af20631a57bb7f42dd957ca2189f4b3c2a2a54ec8cd97f5e241'
assert bind(ap)['sha256'] == '8a64e7b42cfe50ff6fa1933c73100ccccf2f66eebb4194527af654c5b8aeb042'
evidence_by_path = {}
def bindings(x):
    if isinstance(x, dict):
        if 'path' in x and 'sha256' in x:
            check(x)
            prior = evidence_by_path.setdefault(x['path'], bind(x['path']))
            assert prior['sha256'] == x['sha256']
        for v in x.values(): bindings(v)
    elif isinstance(x, list):
        for v in x: bindings(v)
bindings(m); bindings(a)
packet_binding_count = len(evidence_by_path)
for p in [mp, ap, 'records/S6_SERIES_PUBLISH_II_YC_root_primary_Demailly_01.json', 'records/S6_SERIES_PUBLISH_II_YC_root_primary_Hatcher_01.json']:
    evidence_by_path[p] = bind(p)
p = read(a['proposal']['path'])
guards = [dict(old=g['literal_old'], new=g['literal_new'], type=','.join(g['defect_types']), reason=g['reason']) for g in p['guards']]
assert len(guards) == 21
old = (R/t['full_original_block']['path']).read_text()
new = (R/t['proposed_full_block']['path']).read_text()
w = old
for proposal, g in zip(p['guards'], guards):
    assert hashlib.sha256(w.encode()).hexdigest() == proposal['intermediate_before_sha256']
    assert w.count(g['old']) == 1
    w = w.replace(g['old'], g['new'], 1)
    assert hashlib.sha256(w.encode()).hexdigest() == proposal['intermediate_after_sha256']
assert w == new
assert old.count('\\item') == new.count('\\item') == 3
new_without_labels = new
for label in p['new_equation_labels']:
    assert old.count('\\label{'+label+'}') == 0
    assert new_without_labels.count('\\label{'+label+'}') == 1
    new_without_labels = new_without_labels.replace('\\label{'+label+'}', '')
pat = r'(?<!\\)\\\[(.*?)(?<!\\)\\\]'
od = [s.strip() for s in re.findall(pat, old, re.S)]
nd = [s.strip() for s in re.findall(pat, new_without_labels, re.S)]
assert len(od) == 17 and od == nd
for pattern in [r'\\label\{([^}]+)\}', r'\\hypertarget\{([^}]+)\}', r'\\tag\{([^}]+)\}']:
    assert re.findall(pattern, old) == re.findall(pattern, new_without_labels)

now = dt.datetime.now(dt.timezone.utc).isoformat()
review = 'records/S6_SERIES_PUBLISH_II_root_continuation2_batch76_review.json'
evidence = list(evidence_by_path.values())
rd = dict(created_utc=now,
    checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, root, second continuation; reasoning effort not separately exposed',
    actual_reading='Root read the complete 13912-byte frozen derivation before opening the target, followed by every paragraph of all three original and final proof items, all seventeen actual displays, the full comparison, all twenty-one exact guards, both complete program sources and outputs, input and postrelease receipts, freeze/release receipts, program scope including its historical rows, both proposed events, and both Programs rows. Root had already received the agent repair notices; no independent root event is claimed. Root subsequently read all extracted text of Hatcher printed245-246 and Demailly printed79-80. The first Demailly output was lost to context truncation; it received no reading credit. A second in-memory download and extraction reproduced the recorded PDF and text SHA256 values and supplied the full bounded text for actual reading. Historical acquisition receipts retain root_reading_pending=true; this later record supplies the completed reading. No primary diagram, complete Hatcher proof, or final publication-page visual reading is claimed.',
    mathematical_review=[
        'The domain retains the complete local reduced equation and arbitrary other critical branches in the remaining positive-Euler ruled case. On the smooth generic-D4 critical branch, the normal coefficients of order below three vanish identically. The equation is therefore in the third power of the normal ideal. Weierstrass preparation retains the original unit U. The exact change x_old=x_new-a2/3 has Jacobian one and gives depressed coefficients a1-a2^2/3 and a0-a1*a2/3+2*a2^3/27. These expressions are verified separately in the frozen computation.',
        'For W=x^3+x*y^2*B+y^3*C, the generic nonzero discriminant makes at least one finite positive order k or l along the axis available. With rho=min(k/2,l/3), weights(L+rho,L,1) and L>3rho give the three precise leading forms x^3+a*x*y^2*z^k, x^3+b*y^3*z^l, or Q(x,y*z^r) with k=2r,l=3r. Every other coefficient term involving y has a strictly positive weight gap. The finite certificate uses L=3rho+1/6, scaled by6, and tests2304 pairs; the general inequalities are proved in prose. A depressed Q that is a cube would have zero mixed coefficients by its X^2*V coefficient, contradicting the retained nonzero a or b. A double factor remains allowed.',
        'For the auxiliary conic surface uv=h over a connected smooth curve, all zeros of h being simple proves smoothness by the Jacobian. A path joining two zeros supplies the matching sphere. Writing h=rho*exp(i*phi), u=sqrt(rho)*exp(i*theta), v=sqrt(rho)*exp(i*(phi-theta)) gives cancellation of the two fibre symplectic contributions and zero base area on the path. At an endpoint h=c*s, the corrected exact cap uses sqrt(|c|*s) and (c/|c|)*sqrt(|c|*s); its smooth graph is v=(c/|c|)*conjugate(u). The complex orientation differs from the tangent/normal ordering by one transposition, so the sphere has self-intersection minus2.',
        'For each proper finite holomorphic map pi of degree d between the smooth surfaces, pullback of a compactly supported degree-two class stays compactly supported. Integration outside the branch set, which has measure zero, gives integral(pi^*alpha)^2=d*integral(alpha^2). Poincare duality with compact supports identifies the pulled-back class with ordinary compact two-dimensional homology and gives square minus2d. Hatcher Theorem3.35 on printed245 states the required compact-support duality; printed245-246 also explains proper-map pullback. This yields a compact class, with no claim that the pullback is itself an embedded sphere.',
        'In the first weight case the base is C-star, h=(1-x^3)/(a*x), and u=y^2,v=z^k give a proper finite map of degree2k. In the second, the base is C, h=(1-x^3)/b, and u=y^3,v=z^l give degree3l. Monic coordinate algebras give properness and the exact degrees. In the balanced case B_Q={Q(X,V)=1} is smooth by Euler identity and connected by the transitive scalar-cover monodromy for root multiplicities(1,1,1) or(2,1). The three zeros V=0 are simple since Q_X=3X^2 there. The exact map(x,y,z) to((x,y*z^r),u=y,w=z^r) has degree r by the monic equation z^r=w. The respective compact-class squares are minus4k,minus6l,minus2r.',
        'The original proof retains U throughout. The rescaled complete equation G_epsilon=epsilon^(-d)*f(D_epsilon) converges on a neighbourhood of the compact cycles to U(0)*P. The exact vector field minus(partial_epsilon G)*conjugate(gradient G)/norm(gradient G)^2, with cutoff one near those cycles, transports within the same regular level; scaling then embeds the transported cycles in an actual local fibre f=U(0)*epsilon^d. Complex orientation and intersection numbers are preserved. The XQ zero-pairing conclusion gives the contradiction. The frozen route removes the unit using the previously recorded exact unit-flow map; both routes were explicitly compared and the original unit-containing route remains.',
        'Two bounded original errors are repaired. The claim that two specified simple zeros make the entire conic smooth is refuted by h=t(t-1)(t-2)^2 at(t,u,v)=(2,0,0); the repair requires all zeros simple, and all three actual applications already prove precisely three simple zeros. The original endpoint formula has squared norms s and |c|^2*s, with c=2,s=1 giving1 and4. The corrected modulus factors preserve product c*s and make both squared norms |c|*s. The theorem statement and domain are unchanged. The gradient clarification concerns the regular level P=1 even when the zero divisor has a repeated factor, and introduces no exclusion of that case.',
        'All three original proof items and all seventeen original displays are retained. Five semantic equation labels are added; old labels, targets and manual equation tags remain. The two corrected cap coordinates are inline formulas; the production marker and the h=cs clarification are separately accounted for. Both programs and their full outputs were read; their finite arithmetic and symbolic checks do not replace the analytic compact-transport and properness arguments. Exactly two events in one evidence group are proposed. No R13, global-defect, final-provenance, supporting-result, independent-root, or final-page completion is added.'
    ],
    chronology='Agent derivation froze09:38:59.675445 UTC and target released09:39:02.012314 UTC. Root derivation reading preceded root target opening. Completed supporting XR and P4.17 exposure was disclosed. The preseal raw display count included two array spacing commands and was corrected to seventeen actual displays; the failed attempt remains preserved.',
    original_proof_items_preserved=3, original_displays_preserved=17,
    original_inline_occurrences=99, mathematical_errors_found_in_original=a['proof_repairs'],
    target_statement_refuted=False, proof_substitution=False,
    packet_binding_count=packet_binding_count, publication_page_reading_credit=0, evidence=evidence)
assert not (R/review).exists()
(R/review).write_text(json.dumps(rd, indent=2)+'\n')
with (R.parent/'S6_SERIES_GRIND_tags.tsv').open() as f:
    pages = {x['tag']:x['page'] for x in csv.DictReader(f, delimiter='\t')}
target = dict(owner=t['statement_owner'], tag=t['tag'], old_page=pages[t['tag']],
    original=t['full_original_block'], proposed=t['proposed_full_block'],
    freeze=t['freeze_receipt'], release=t['release_receipt'], events=a['event_proposals'], guards=guards,
    who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort not separately exposed; checker continuation2_A',
    scope='Full positive-Euler ruled local equation with a smooth generic-D4 critical branch and unrestricted other critical branches: the nonzero normal cubic cannot be a cube. Exact preparation, weighted models, finite proper maps, compact pairings and transport reviewed.',
    event_note='Root complete comparative review at '+now+'. All3 items and17 displays retained;2 bounded auxiliary errors repaired with explicit counterexamples and exact corrected formulas. The theorem and domain are unchanged. Two events in one evidence group; no independent root, supporting-result, computation or final-page event.')
anchor = read('records/S6_SERIES_PUBLISH_II_continuation2_batch75_config.json')['additional_source_edits'][-1]['new'].splitlines()[-1]
program_rows = (R/a['program_rows']['path']).read_text().rstrip('\n')
extra = [dict(old=anchor, new=anchor+'\n'+program_rows, type='D09', owner='Programs', location='Programs', reason='List both new programs checking weights, exact finite-map equations, endpoint cap coordinates and orientation in the retained original proof.')]
copies = [dict(**{'from':bind('agents/continuation2_A/'+name)}, to='code/'+name) for name in ('S6_SERIES_PUBLISH_II_A2_YC_weighted_cubic_output.json', 'S6_SERIES_PUBLISH_II_A2_YC_original_cap_output.json')]
cfg = dict(batch=76, root_review_complete=True,
    source_before_sha256=bind('S6_SERIES_PUBLISH_II.tex')['sha256'],
    ledger_before_sha256=bind('CHECK_EVENTS.tsv')['sha256'],
    review_evidence=[bind(review), *evidence], targets=[target], additional_source_edits=extra,
    code_copies=copies, mathematical_repairs=a['proof_repairs'],
    scope='02YC admitted after the complete frozen derivation and all3 original/final items. Seventeen displays retained with5 semantic labels. Twenty-one owner guards and one Programs append containing2 rows;2 events in1 group. Two specifically refuted auxiliary assertions repaired, with the theorem and original unit-containing route preserved. No R13, global-defect, final-provenance or page-reading closure.')
assert cfg['source_before_sha256'] == 'a672fec9c1889bb4df6578e6b248f00ef2a4143375097fb8d97abddd0d323f9f'
assert cfg['ledger_before_sha256'] == '8f9c87f7875652f655689ba72559ab34fb2dfffbd52eb50a0dff2079cd63caec'
out = 'records/S6_SERIES_PUBLISH_II_continuation2_batch76_config.json'
assert not (R/out).exists()
(R/out).write_text(json.dumps(cfg, indent=2)+'\n')
print(json.dumps(dict(config=bind(out), review=bind(review), packet_binding_count=packet_binding_count)))
