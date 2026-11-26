from pathlib import Path
import csv, datetime as dt, hashlib, json, re

R = Path(__file__).resolve().parents[1]
def bind(p):
    b = (R / p).read_bytes()
    return dict(path=p, sha256=hashlib.sha256(b).hexdigest(), bytes=len(b))
def read(p):
    return json.loads((R / p).read_text())
def verify(o):
    if isinstance(o, dict):
        if 'path' in o and 'sha256' in o:
            assert bind(o['path'])['sha256'] == o['sha256'], o['path']
        for v in o.values(): verify(v)
    elif isinstance(o, list):
        for v in o: verify(v)

shared_path = 'agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_XV_XW_final_v1_shared_index.json'
assert bind(shared_path)['sha256'] == 'f963156016acc7cc0d1830a7ac03ad77a171ca6a68224f293ae03df104d5e7d0'
shared = read(shared_path)
verify(shared)
group = 'S6_SERIES_PUBLISH_II_C2_XV_XW_20261122'
assert shared['evidence_group'] == group
assert shared['unique_independent_evidence_groups'] == 1
expected = {
    '02XV': ('c894a9732d476d01814c9d6794fc2920a6e5992d443fb64c71bf1ded5dd111f6', 12, 9, 9),
    '02XW': ('e824fa861d2d5c76eb0858f5703e88119b688959b34e60707d9f212a8e247e72', 10, 8, 11),
}
now = dt.datetime.now(dt.timezone.utc).isoformat()
who = 'GPT-6 Astra (OpenAI), ChatGPT Pro mode, root, second continuation; reasoning effort not separately exposed'
targets, evidence, programs, copies = [], [bind(shared_path)], {}, []
with (R.parent / 'S6_SERIES_GRIND_tags.tsv').open() as f:
    pages = {x['tag']:x['page'] for x in csv.DictReader(f, delimiter='\t')}
for tag, (ih, items, displays, ng) in expected.items():
    pre = 'agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_' + tag + '_'
    ip = pre + 'final_v1_index.json'
    assert bind(ip)['sha256'] == ih
    idx = read(ip)
    verify(idx)
    pp = pre + 'final_v1_proposals.json'
    p = read(pp)
    verify(p)
    t = p['blocks'][0]
    guards = [dict(old=g['old'], new=g['new'], type=g['defect_type'], reason=g['reason']) for g in t['guards']]
    assert len(guards) == ng
    old = (R / t['original_full_block']['path']).read_text()
    new = old
    for g in guards:
        assert new.count(g['old']) == 1
        new = new.replace(g['old'], g['new'], 1)
    assert new == (R / t['proposed_full_block']['path']).read_text()
    assert old.count('\\item') == new.count('\\item') == items
    ods = re.findall(r'\\\[(.*?)\\\]', old, re.S)
    nds = re.findall(r'\\\[(.*?)\\\]', new, re.S)
    assert len(ods) == displays
    if tag == '02XW':
        assert ods == nds
    else:
        assert len(nds) == displays + 1
        j = 0
        for d in nds:
            if j < len(ods) and d == ods[j]: j += 1
        assert j == len(ods)
    for pat in [r'\\label\{([^}]+)\}', r'\\hypertarget\{([^}]+)\}', r'\\tag\{([^}]+)\}']:
        assert re.findall(pat, old) == re.findall(pat, new)
    eb = read(pre + 'final_v1_evidence_bindings.json')
    verify(eb)
    events = read(pre + 'final_v1_event_proposals.json')['events']
    assert len(events) == 3 and {e['evidence_group'] for e in events} == {group}
    scope = ('Second conductor image has at least three generic normalization branches, without transverse multiplicity or tangency bounds; all original incidence cases and the corrected actual normalization are checked.' if tag == '02XV' else 'The remaining degree-two image-conductor cycle cannot occur at two distinct junctions; tangent junctions, B-only factors and all scalar-zero allocations are retained.')
    targets.append(dict(owner=t['statement_owner'], tag=tag, old_page=pages[tag],
        original=t['original_full_block'], proposed=t['proposed_full_block'],
        freeze=idx['freeze_receipt'], release=idx['release_receipt'],
        events=bind(pre + 'final_v1_event_proposals.json'), guards=guards, who=who,
        scope=scope,
        event_note='Root complete frozen/original/final comparison at ' + now + '. Shared XV/XW stronger-input derivation remains checking evidence only. Original proof route and every original display retained. Root comparative review adds no independent group or page credit. XV intermediate normalization error and its postrelease repair are explicitly recorded; neither theorem statement changes.'))
    evidence.extend([bind(ip), bind(pp), idx['comparison'], idx['frozen_derivation'],
                     *eb['evidence'], bind(pre + 'final_v1_postrelease_reading_and_computation.json')])
    pr = read(pre + 'final_v1_programs_table_proposal.json')
    programs[tag] = [dict(old=g['old'], new=g['new'], type=g['defect_type'],
        owner='Programs', location='Programs', reason=g['reason']) for g in pr['guards']]
    for cp in pr['program_copy_proposals']:
        copies.extend([dict(**{'from':dict(path=cp['from'],sha256=cp['sha256'])},to=cp['to']),
                       dict(**{'from':dict(path=cp['output_from'],sha256=cp['output_sha256'])},to=cp['output_to'])])

repair = dict(owner='night:P4.56', type='D25',
    original_error='One generic normalization sheet on the F_H side of B does not imply that F_H is smooth there. Thus the original normality claim for u squared plus k, and the dependent claim that k(0,z) has a simple zero, were unsupported and can fail.',
    exact_witness='For F_H=Y squared+X squared(z-X) cubed, the partial cover u squared+(z-X) cubed is singular along u=0,z=X. The actual cover v squared+z-X=0 maps by z=X-v squared and Y=-Xv cubed; its X=0 curve is smooth and degree-two ramified although k(0,z)=z cubed. The witness concerns the intermediate implication, not the full theorem.',
    correction='Factor k=a squared h with h reduced and use the finite birational map v squared+h=0, Y=Xav. Prove its normality, identify the reduced inverse image (X) with the embedded H_N including zeros of a, and use its smooth ramified degree-two map to force h(0,z) to have a simple zero. The actual normalization is then smooth and the original 2b=m versus b>=m>0 contradiction applies.',
    statement_changed=False,
    error_record=bind('agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_02XV_final_v1_defect_and_repair.md'))
review = 'records/S6_SERIES_PUBLISH_II_root_continuation2_batch71_review.json'
assert not (R / review).exists()
rd = dict(created_utc=now, checker=who,
    actual_reading='Complete shared frozen derivation read before either complete original target. Complete XV original/final twelve items and XW original/final ten items, both complete comparisons, the full XV error/repair record, all twenty target guards, both complete exact program sources and outputs, freeze/release/input/historical-locator records, six event proposals and both Programs proposals have been read. An initially truncated combined metadata output was followed by a bounded complete rereading of the omitted XV guards and XW freeze. Earlier scattered root source exposure is disclosed separately; root adds no independent event. No final PDF page reading or new primary-literature reading is claimed.',
    mathematical_review=[
        'The shared frozen route applies the first assertion of the completed BX proposition to precisely the same ambient Y, f, full fibre mS, rational smooth A, connected actual H->A of degree two and degree-one vertical sheet furnished by XU. The ruling p and section h satisfy ph=id and hp on H=id; the ruling descends through the vertical exceptional fibres, so H is smoothly embedded in N and isomorphic to the positive-genus ruling base. BX forces that identical covering curve H to be rational, contradicting the isomorphism on its holomorphic one-form space. The root BX dependency audit established that its first assertion uses BW and RAT.6 and does not use XV or XW. One argument is associated to two targets and remains one evidence group.',
        'XV: the conductor tree with 2+c_B components has identification budget1+c_B. The exact complete intersection Q supported on smooth A is finite torsion-free over its parameter ring, hence free of rank m. At m1 the reduction is an isomorphism; at m2 the nilradical is free of rank1 and has square zero by generic vanishing and torsion-freeness. The displayed dual-number algebra follows. Its embedding dimension forces one nonzero branch gradient; the other factor of normal order2 lies in the ordinary square of the smooth ideal, with zero gradient. This proves the smoothness implication on the original intersection scheme.',
        'XV: pairwise-intersecting supports in the two image labels share a label, yielding the exact minimum contribution. At two junctions c_B2 costs4>3. For c_B1 an unramified degree2 point costs2+1>2. The sole V point at either junction cannot be the common label, so the forced connected path is H-V-R. At R-V the H factors meet its factor only along A, with generic lengths1 or2 from the ordinary triple transversal, forcing it smooth. It contains every nearby generic B preimage and is intrinsically nonnormal along that germ, a contradiction. The one-B-component three-branch-point case has the same path and same length argument, with the two B signs separated by the tree condition.',
        'XV: with two degree1 B components, T=h+5 and budget3 give h+2<=n<=T/2. Singleton supports violate the lower bound. Thus h1,T6,n3, and every local point pairs distinct image labels. The full15 perfect matchings yield exactly4 paths, carried to H-W-V-R by the two interchanges. The H cover is actually ramified of local degree2. F_R and F_H intersect along A in length2, so F_R is smooth. Preparation followed by Y prime=Y+X alpha/2, with its explicit inverse, preserves I_A and gives Y squared+X squared k.',
        'XV: the original one-sheet-to-smoothness inference is false, as both the cusp parametrization and the square-factor example in the error record show. For k=a squared h, the ring C{X,z,v}/(v squared+h) is generated by an integral v over the original ring, and v=Y/(Xa) gives the same fraction field. Reduced h has isolated plane-curve singularities, so the new hypersurface is Cohen-Macaulay and regular in codimension1, hence normal. Its map is the actual finite normalization. Pullback I_A=(X,Y) is exactly(X). No curve is contracted under the finite map, and its generic A sheets are precisely H. The quotient by X is a one-dimensional complete intersection, generically reduced because h(0,z) is generically nonzero. With no embedded primes it is reduced, proving equality with the embedded H_N, including zeros of a.',
        'XV: the actual reduced H_N is smooth via the descended ruling and section and ramified of degree2 over z. Unit h(0,z), positive even order and odd order>=3 give respectively unramified points, two local branches and a singular curve. Thus its order is1, making the actual normalization smooth. On F_R the divisor of the last factor G is mB_minus, giving b=m I(A,B_minus)>=m. On the other smooth normalization its divisor is mW with the same generic intersection valuation on the other sign of irreducible B. The normal crossing pole divisor makes H-W transverse, so restriction has order m; pullback along H->A gives2b=m, contradiction. The repair preserves the original proof and all9 original displays and adds one actual-normalization display.',
        'XW: the leading normal Hessian at a parametrized junction has coefficient Hess(q3)(a,b), with higher normal degree and z variation of strictly greater parameter order. Cubic directional differentiation yields Hess(D_vQ)=Hess(Q)(v). The exact linear coordinate map sending the first axis to v shows that zero Hessian leaves a pure cube or zero; the stated R19 input excludes the former in this precise scope. At both junctions the common cubic zero divisor therefore has degree b>=2. For the projective bundle of conormal degree2, adjunction gives pa=4-2b. The union sequence with the rational third section gives pa=g(H)+delta+intersection-1, so the nonnegative slack identity forces b2,g1,delta0,intersection0. Relative Cech cohomology and P1 Riemann-Roch independently reproduce the same polynomial in the exact certificate.',
        'XW: graph budget excludes c_B<=2 by the earlier XV length/path argument in its unrestricted cover-degree form. At c_B>=3 a common A label costs c_B+2>c_B+1 across the junctions, so B is common to every local branch, including B-only factors. The descended ruling maps R to one point b0 on H; equality of an H point and R point in N forces that H point to be b0. Thus one of the two junctions separates all relevant normalization points. Primitive homogeneous factors over C{z} have nonzero product modulo z, proving sum b_i+sum c_j=1 with every B-only factor retained.',
        'XW: an unramified H gives at least two independent linear normal terms, whose exact local coordinate map cuts only A, contradicting common B. In the ramified case the three allocations exhaust the simple zero. A B-only allocation again makes F_H restricted to smooth F_R equal Y squared times a unit. A quadratic allocation gives Y squared h(Y,z), with h_z nonzero and extra B multiplicity1; positivity of each branch intersection permits at most one F_H branch and hence at most two total. A linear allocation gives a primitive quadratic with actual smooth ramified spectral curve. Its simple k(0,z) zero is proved first, so u squared+k=0 is a smooth finite birational normalization and supplies one generic B branch. This normalization uses no one-sheet smoothness inference.',
        'XW: the remaining factor has quadratic Taylor part z(ell X+mY)+Q2 with (ell,m) nonzero and no z squared term. The two Hessian minors are minus ell squared and minus m squared, so rank>=2. Rank3 has an isolated critical point. Rank2 splits holomorphically as U squared+V squared+h(W); a nonisolated critical set forces h prime identically0 and then h0, which factors into U+iV and U-iV and contradicts irreducibility. It therefore supplies one generic B branch; total2 contradicts XV. Every original display and all10 items are retained.',
        'Both complete new scripts and successful outputs were read. Their finite enumerations, exact matrix and polynomial identities, Cech genus, valuations and scalar budgets agree with the proof. The analytic finiteness, Serre normality, embeddedness and Morse arguments were checked separately and are not inferred from samples. The two named historical programs were absent from the attached manifests/tree and returned404 at their exact pinned URLs; neither is claimed to have been read or replayed. All twenty target guards and two Programs insertions have been reviewed, with unchanged statements, labels and tags. The current R19 required check remains open; no root claim closes it through this comparison.'
    ],
    chronology='Both independent-route freezes at08:13:01 precede both target releases at08:13:11. Shared XU supporting proof and BX statement-only inputs are disclosed. All original-route comparisons, the XV repair, and exact printed-route programs are postrelease. Earlier root locator hits are recorded. Six event rows retain one shared independent group; root adds none.',
    original_proof_items_preserved={'02XV':12,'02XW':10},
    original_displays_preserved={'02XV':9,'02XW':8},
    mathematical_errors_found=[repair], publication_page_reading_credit=0,
    evidence=evidence + [bind('records/S6_SERIES_PUBLISH_II_root_locator_exposure_01.json')])
(R / review).write_text(json.dumps(rd, indent=2) + '\n')
cfg = dict(batch=71, root_review_complete=True,
    source_before_sha256=bind('S6_SERIES_PUBLISH_II.tex')['sha256'],
    ledger_before_sha256=bind('CHECK_EVENTS.tsv')['sha256'],
    review_evidence=[bind(review), *evidence], targets=targets,
    additional_source_edits=programs['02XW']+programs['02XV'], code_copies=copies,
    mathematical_repairs=[repair],
    scope='XV and XW admitted jointly after their complete shared statement-led derivation and complete original/final comparisons. Six events retain ONE independent evidence group across two required rows. XV items9-10 contained an invalid inference from one normalization sheet to smoothness; the finite birational square-part normalization and exact reduced inverse-image argument repair it, leaving both theorem statements and every original display unchanged. The original graph/spectral proof routes remain. Twenty target guards and two Programs insertions are recorded. No global defect, provenance, R19 check or final-page gate is closed.')
assert cfg['source_before_sha256'] == '00b79f4a3e5466880277c7453f3320008b40d041209f1170fc05d03874583374'
assert cfg['ledger_before_sha256'] == '71b2b1b516789f7440f6e7bbf4f6912553e99fcc9b022b39b76c8a741fae9810'
out = 'records/S6_SERIES_PUBLISH_II_continuation2_batch71_config.json'
assert not (R / out).exists()
(R / out).write_text(json.dumps(cfg, indent=2) + '\n')
print(json.dumps(bind(out)))
