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

pre = 'agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_02XU_'
ip = pre + 'final_v1_index.json'
assert bind(ip)['sha256'] == 'c60d1c23abdc48b10b55e2c72dfc3690ddeb9cd8a27103791a6fbbd0ee7ab079'
idx = read(ip)
verify(idx)
pp = pre + 'final_v1_proposals.json'
p = read(pp)
verify(p)
t = p['blocks'][0]
guards = [dict(old=g['old'], new=g['new'], type=g['defect_type'], reason=g['reason']) for g in t['guards']]
old = (R / t['original_full_block']['path']).read_text()
new = old
for g in guards:
    assert new.count(g['old']) == 1
    new = new.replace(g['old'], g['new'], 1)
assert new == (R / t['proposed_full_block']['path']).read_text()
assert len(guards) == 10
assert old.count('\\item') == new.count('\\item') == 13
assert re.findall(r'\\\[(.*?)\\\]', old, re.S) == re.findall(r'\\\[(.*?)\\\]', new, re.S)
assert len(re.findall(r'\\\[(.*?)\\\]', old, re.S)) == 12
for pat in [r'\\label\{([^}]+)\}', r'\\hypertarget\{([^}]+)\}', r'\\tag\{([^}]+)\}']:
    assert re.findall(pat, old) == re.findall(pat, new)
eb = read(pre + 'final_v1_evidence_bindings.json')
verify(eb)
now = dt.datetime.now(dt.timezone.utc).isoformat()
review = 'records/S6_SERIES_PUBLISH_II_root_continuation2_batch68_review.json'
assert not (R / review).exists()
rd = dict(
    created_utc=now,
    checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, root, second continuation; reasoning effort not separately exposed',
    actual_reading='The complete frozen derivation was read before the full original target. All thirteen original and thirteen final items, all twelve displays, the whole stepwise comparison, all ten guards, both complete program sources and outputs, freeze/release/input/postrelease/historical-locator records, three event proposals, and Programs proposal were actually read in bounded untruncated outputs. The exact BW and R19 statements were checked. The root locator exposure receipt records the scattered earlier one-line source hits; none mapped to XU. No new primary-source or final-PDF page reading is claimed.',
    mathematical_review=[
        'The completed positive ruled inputs give the same ambient Y, f, full fibre mS, normalization nu:N->S and resolution pi:T->N. The pole section H has genus g>=1 and is noncontracted. The full image conductor C has two rational normalized components and one incidence cycle, hence total identification contribution two. A third branch of A would use that entire contribution and leave no incidence joining B; joining B at that point would raise the contribution to at least three. Thus each component has at most two branches. The ruling descends through the connected vertical rational resolution fibres and its restriction is the inverse to H->N, proving that its image is a smooth embedded curve.',
        'The normalization conductor is the proper quotient of the pole tree by its connected exceptional subtrees. A repeated attachment to one strict component would already form a cycle before contraction. Thus the resulting incidence graph is a tree and each reduced component union is a forest. At a separated self-identification of B, the exact maps from every normalized conductor component to B normalization are finite and surjective. Local surface factors pairwise intersect in a curve by the two-equation height bound. Their nonempty two-color support sets therefore pairwise intersect, so they share one color. Consequently rplus>=n and rminus>=cB; the contribution rplus+rminus-n>=cB exceeds the subforest total cB-sB. This also handles a separated identification of A and places no transverse restriction on B.',
        'The complete image-conductor scheme is retained in the primary restriction. The actual canonical residue maps identify pi_*O_T(-D) with the normal conductor ideal; the conductor square injects the image-conductor functions into rho_*O_D. Effectivity and the blowup formula Dprime=beta*D-E identify functions through each blowdown, while the minimal ruled vertical layers O_P1(-2) show that a global function on D is determined by its generic doubled-section value. Therefore H0 of the primary restriction is injective and H1 is surjective, giving g-1<=chi(O_A^(2)). The generic triple-point conductor interpolation produces the exact square of the transverse maximal ideal. Purity identifies its primary extension with the symbolic double. The normalized-conormal sequence and P1 Riemann-Roch give chi=5-sum(delta+tau-r).',
        'For planar points finite duality and the residue generator give the exact defect 5delta. The prerelease nonplanar unibranch bound is at least six, sufficient for smoothness reduction. The stronger printed bound seven is checked separately: equality at six forces multiplicity3, delta2 and conormal colength6. The valuation gaps are exactly1,2, so generators can have leading orders3,4,5. The unique weights6 and7 exclude x squared and xy from all defining relations. Every gradient of order3 has only its z component at that order, so every conormal exterior minor has order at least7. The primitive saturated-kernel exterior generator makes its colength the minimal such order, contradicting6. The explicit quadratic-minor calculation gives9,9,7; higher terms cannot lower these bounds. The two-branch nonplanar bound is directly at least7. The surviving singular case is one planar delta1 point and g1.',
        'For this singular lci A, adjunction and invariance of degree under finite birational normalization give degree(E0)=0 for the pulled-back conormal bundle. Unmixed powers give I_A^(3)=I_A cubed, so the cubic tensor is an actual global section. Its zero-degree line twist is trivial on P1. Cancelling the common zero fibres gives the residual reduced horizontal divisor 3xi-bF. The derivative direction on H extends over the complete smooth curve by cancelling local common powers; distinct generic normalization points give distinct roots. This is a finite birational map to its spectral component. The remaining degree-one sheet in the quadratic case gives a section of the bundle, hence a smooth rational spectral component. These explicit maps justify the genus comparisons.',
        'For the quotient projective bundle, xi squared=e, xiF1, F squared0 and K=-2xi+(e-2)F. The degree of (3xi-bF)(xi+(e-2-b)F) is6e-6-4b and hence pa=3e-2-2b. The independent relative Cech calculation has R1p_*O(-3xi+bF)=E dual tensor(detE) inverse tensorO(b), with splitting degrees b-2alpha-beta and b-alpha-2beta. Its Euler characteristic gives the identical polynomial by the divisor exact sequence. With e0 the arithmetic genus is negative; an integral component normalized by H has pa>=g>=1, and a union with its rational section has pa>=g-1>=0. This retains the original spectral proof that A is smooth.',
        'In the degree-three case the embedded H is the sole conductor component over A and each normal point has at most one A branch. A three-branch image point has full incidence budget cB. Singleton A, singleton plus/minus, and no-singleton cases respectively force contributions at least2cB, cB+rA, or cB+ceil(rA/2), all strictly greater. Hence the image has two distinct A-B junctions. An A-only normal point at one junction forces all its normal points to carry A and consumes at least cB; pairwise intersections force a mixed A-B point at the other junction, adding at least1. Thus neither junction has an A-only branch.',
        'A simple root of the actual nonzero cubic gives the holomorphic strict equation f(yu,y,z)/y cubed. The implicit-function theorem produces u=alpha(y,z), exact division yields f1=x-yalpha, and f2 restricted to that smooth branch equals y squared times a unit because the root derivative is nonzero. This is an A-only branch, already excluded. The exact R19 statement rules out a nonzero cube along the same smooth D4 image while retaining arbitrary other critical branches. Therefore the entire cubic vanishes at both junctions. Now conormal degree is2, b>=2 and the residual cubic is integral with normalization H; pa=4-2b<=0 contradicts g>=1. Exactly one vertical rational degree-one sheet remains in the degree-two alternative; finite birationality over the smooth A gives the stated isomorphism.',
        'The frozen independent route is complete and remains separate: a nowhere-zero degree-zero discriminant on the singular arithmetic-genus-one A gives at least two actual smooth local factors z-hv_i. At a cusp at least one contains H and contradicts its embedded smooth section. At a node the two distinct normal points give at least two incidence excesses for at most two conductor components above A, forcing a cycle even with B through the node. Once A is smooth, the completed BW theorem applies by the identity of Y,f,mS,A and the actual connected triple cover H->A, forcing its complete covering curve rational. The earlier root BW/RAT.6 dependency audit excludes any use of XU. This independent ending is not substituted for the retained original spectral/graph proof.',
        'Both complete new programs and outputs were read. The prerelease resultant, frame/shear/unit weights, conductor interpolation and universal defect identities agree; the finite501 support-family examples corroborate the separately proved all-family lemma. The postrelease program additionally uses relative Cech/Riemann-Roch and a separate Chow-ring multiplication, the gradient minor bound, and150 bounded three-branch rows with minimal excess1. The universal inequalities are proved in the comparison and manuscript, not inferred from those enumerations. The old named script is absent from three attached manifests and the tree, and its exact pinned retrieval returned404; it is not credited as read, run, or method-compared. The ten guards preserve every mathematical claim, all thirteen original proof items and all twelve displays, replacing only production prose and references with the exact calculations and one Programs citation.'
    ],
    chronology='Complete derivation freeze08:02:35.748490 precedes release08:02:47.137753. XR/XS/XT and the listed supporting proofs are disclosed. BW was a statement-only input after exact scope and dependency confirmation. The retained spectral proof, stronger defect bound and full printed graph route were separately checked after release. Three events share one evidence group; root adds no independent event.',
    original_proof_items_preserved=13,
    original_displays_preserved=12,
    mathematical_errors_found=[],
    publication_page_reading_credit=0,
    evidence=[bind(ip), idx['frozen_derivation'], idx['comparison'], idx['final_proposed_block'], *eb['evidence'], bind(pre + 'final_v1_postrelease_reading_and_computation.json'), bind('records/S6_SERIES_PUBLISH_II_root_locator_exposure_01.json')],
)
(R / review).write_text(json.dumps(rd, indent=2) + '\n')
with (R.parent / 'S6_SERIES_GRIND_tags.tsv').open() as f:
    pages = {x['tag']:x['page'] for x in csv.DictReader(f, delimiter='\t')}
target = dict(owner='night:P4.55', tag='02XU', old_page=pages['02XU'], original=t['original_full_block'], proposed=t['proposed_full_block'], freeze=idx['freeze_receipt'], release=idx['release_receipt'], events=bind(pre + 'final_v1_event_proposals.json'), guards=guards, who=rd['checker'], scope='Smooth rational horizontal image, connected degree-two horizontal cover, unique rational degree-one third sheet, and full separated-self-identification exclusion in the remaining positive ruled case.', event_note='Root complete frozen/original/final thirteen-item comparison at ' + now + '. All twelve original displays and the full spectral/graph proof remain; independent local-factor/BW route remains in checking evidence. No mathematical correction, extra independent group or final-page credit.')
pr = read(pre + 'final_v1_programs_table_proposal.json')
extra = [dict(old=g['old'], new=g['new'], type=g['defect_type'], owner='Programs', location='Programs', reason=g['reason']) for g in pr['guards']]
copies = []
for cp in pr['program_copy_proposals']:
    copies.extend([dict(**{'from':dict(path=cp['from'],sha256=cp['sha256'])},to=cp['to']), dict(**{'from':dict(path=cp['output_from'],sha256=cp['output_sha256'])},to=cp['output_to'])])
for cp in pr['additional_delivered_check_evidence']:
    copies.append(dict(**{'from':cp}, to='code/' + Path(cp['path']).name))
cfg = dict(batch=68, root_review_complete=True, source_before_sha256=bind('S6_SERIES_PUBLISH_II.tex')['sha256'], ledger_before_sha256=bind('CHECK_EVENTS.tsv')['sha256'], review_evidence=[bind(review), bind(ip), bind(pp), idx['comparison'], idx['frozen_derivation'], *eb['evidence']], targets=[target], additional_source_edits=extra, code_copies=copies, mathematical_repairs=[], scope='02XU admitted after complete independent derivation and full thirteen-item original/final comparison. All twelve displays and the original spectral/graph route remain; ten target guards and one Programs reference; three events in one group. No theorem change, global defect, provenance or page-reading closure.')
assert cfg['source_before_sha256'] == 'f36a31dacdc81b2545513acba04e6c5889749bf08ad80927cc02084263215066'
assert cfg['ledger_before_sha256'] == '89c57138921f054ec8c0ef6dd37a9a6018527f8d858a4478f2e97bfd0bd0fb0f'
out = 'records/S6_SERIES_PUBLISH_II_continuation2_batch68_config.json'
assert not (R / out).exists()
(R / out).write_text(json.dumps(cfg, indent=2) + '\n')
print(json.dumps(bind(out)))
