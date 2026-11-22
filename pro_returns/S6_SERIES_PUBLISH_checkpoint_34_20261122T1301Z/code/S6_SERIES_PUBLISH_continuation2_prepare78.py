from pathlib import Path
import csv, datetime as dt, hashlib, json, re

R = Path(__file__).resolve().parents[1]
def bind(p):
    b = (R/p).read_bytes()
    return dict(path=p, sha256=hashlib.sha256(b).hexdigest(), bytes=len(b))
def read(p): return json.loads((R/p).read_text())

pre = 'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_YE_v1_20261122/S6_SERIES_PUBLISH_II_A2_YE_'
mp, ap = pre+'v1_manifest.json', pre+'admission_recommendation.json'
m, a = read(mp), read(ap)
t = a['targets'][0]
assert bind(mp)['sha256'] == '6b24556f64ce8675091b2fb6b0ce6ed7a30ef6579093a027855e97197d555792'
assert bind(ap)['sha256'] == 'afa48b95f8c9bceeb4d982981b84cdfcaafd3efe63cd628707903d0a9ae48558'
evidence_by_path = {}
binding_occurrences = 0
def bindings(x):
    global binding_occurrences
    if isinstance(x, dict):
        if 'path' in x and 'sha256' in x:
            actual = bind(x['path'])
            assert actual['sha256'] == x['sha256'], x['path']
            if 'bytes' in x: assert actual['bytes'] == x['bytes']
            prior = evidence_by_path.setdefault(x['path'], actual)
            assert prior['sha256'] == x['sha256']
            binding_occurrences += 1
        for v in x.values(): bindings(v)
    elif isinstance(x, list):
        for v in x: bindings(v)
bindings(m); bindings(a)
packet_binding_count = len(evidence_by_path)
for pth in [mp, ap, 'records/S6_SERIES_PUBLISH_II_YE_root_derivation_read_01.json', 'records/S6_SERIES_PUBLISH_II_YC_root_primary_Demailly_01.json', 'records/S6_SERIES_PUBLISH_II_root_continuation2_batch76_review.json']:
    evidence_by_path[pth] = bind(pth)
p = read(a['proposal']['path'])
guards = [dict(old=g['literal_old'], new=g['literal_new'], type=','.join(g['defect_types']), reason=g['reason']) for g in p['guards']]
assert len(guards) == 31
old = (R/t['full_original_block']['path']).read_text()
new = (R/t['proposed_full_block']['path']).read_text()
w = old
for proposal, g in zip(p['guards'], guards):
    assert hashlib.sha256(w.encode()).hexdigest() == proposal['intermediate_before_sha256']
    assert w.count(g['old']) == 1
    w = w.replace(g['old'], g['new'], 1)
    assert hashlib.sha256(w.encode()).hexdigest() == proposal['intermediate_after_sha256']
assert w == new
for g in reversed(guards):
    assert w.count(g['new']) == 1
    w = w.replace(g['new'], g['old'], 1)
assert w == old
assert old.count('\\item') == new.count('\\item') == 10
new_without_labels = new
for label in p['new_equation_labels']:
    assert old.count('\\label{'+label+'}') == 0
    assert new_without_labels.count('\\label{'+label+'}') == 1
    new_without_labels = new_without_labels.replace('\\label{'+label+'}', '')
pat = r'(?<!\\)\\\[(.*?)(?<!\\)\\\]'
od = [s.strip() for s in re.findall(pat, old, re.S)]
nd = [s.strip() for s in re.findall(pat, new_without_labels, re.S)]
assert len(od) == 15 and od == nd
for pattern in [r'\\label\{([^}]+)\}', r'\\hypertarget\{([^}]+)\}', r'\\tag\{([^}]+)\}']:
    assert re.findall(pattern, old) == re.findall(pattern, new_without_labels)
assert '\\StatementRecord{night:P4R.20}{proved}{02YE}{}' in new

now = dt.datetime.now(dt.timezone.utc).isoformat()
review = 'records/S6_SERIES_PUBLISH_II_root_continuation2_batch78_review.json'
evidence = list(evidence_by_path.values())
rd = dict(created_utc=now,
    checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, root, second continuation; reasoning effort not separately exposed',
    actual_reading='Root read the complete 18212-byte frozen derivation before opening the target, as separately recorded, then every paragraph of all ten original and proposed proof items and all fifteen displays. Root read the complete comparison, all31 exact owner guards and their reasons, full block diff, preservation record, both program sources and entire outputs, all input/postrelease/primary/freeze/release receipts, program scope including historical owner rows, both event proposals, Programs row, recommendation and manifest. The selected R7/R9 paragraphs establishing the doubled-section ruled model and reverse point blowups were read again from the current source. Root had already read Demailly printed79-80, including the preparation theorem used here, as bound by the R19 acquisition and completed root review. Reading/checking of these existing inputs adds no supporting-result event. The agent derivation supplies the independent check; root review is not counted separately.',
    mathematical_review=[
        'The full degree-two horizontal domain and unrestricted other image B with at least three generic normalization branches are preserved. The actual finite conductor maps have global components H,R,W1,...,Wc, H degree2 over A, R degree1 over smooth A and Wi positive degrees di over B-normalization. The degree-one finite map R to A is an isomorphism and prevents two R points from being identified in N. The normalization conductor tree has total identification budget c+1.',
        'For E=N^*_(A/Y), adjunction gives degree2. The cubic twist O_Y(S)|A has degree0 and is trivial on A=P1. The quotient projective bundle has xi^2=2, xi.F=1, F^2=0 and K=-2xi. With GammaR=xi-tF and GammaH=2xi+(t-b)F, direct adjunction and multiplication give paH=1+t-b, intersection n=4-t-b and g(H)+deltaH+n=5-2b. The actual finite derivative maps identify the normalization of GammaH with H. Since g(H)>=1 and the lengths are nonnegative, b<=2.',
        'For c>=2, pairwise intersection of the supports in A,+,- follows from intersections of local hypersurface factors. A singleton A costs at least2c>c+1; a singleton sign costs at leastc+2. Otherwise every support has at least two normalized branches. Equality with the global budget forces rA=2,r+=r-=c,np=c+1, two distinct labels at each point, and all identifications at p. Thus H and R have valence1 and each Wi has valence2: the connected tree is H-W1-...-Wc-R, with the plus point consistently on the left and minus point on the right. The finite partition program independently enumerates c=1..4; the arbitrary-c proof supplies the full domain.',
        'The endpoint factors intersect only on A with generic length2. Their one-dimensional complete-intersection ring is Cohen-Macaulay, finite torsion-free of rank2 over C{z}, hence free; reduction by z has length2. Two factors without a linear term would leave independent classes1,x,y. The factor containing two generic A sheets cannot be smooth, so fR is smooth. Take u=fR. Preparation in v and the explicit invertible shear v_new=v_old+u*alpha/2 give fH=unit*(v^2+u^2*g(u,z)). The full normal cubic has scalar product(fj|A) times u*(v^2+u^2*g(0,z)); coefficient uv^2=1 proves the exact common-zero order without cancellation.',
        'On the smooth R factor the residue generator gives conductor ideal equal to the product of the restricted other factors. The ruled-model premise in completed R7/R9 starts with a smooth section and fibres; the two blowup charts preserve simple normal crossings of the reduced total transform, and the actual pole sub-divisor inherits it. The minimal normalization resolution is an isomorphism at this smooth branch. Thus A and B-minus are smooth and transverse there. Choosing z cutting B-minus and repeating preparation with u,z fixed gives an invertible shear that fixes the u=0 surface, so it preserves both adapted curves. Each fj restricts to a unit times z^ej. Consequently e=sum ej is both the global Wc conductor coefficient and the local common cubic-zero order. The plane-curve branch formula gives e>=rB-1>=2. Together with b>=e and the spectral bound this forces b=e=2,rB=3,g(H)=1,deltaH=n=0.',
        'The spectral double curve is therefore smooth and disjoint from the third section. At the forced ramification point its equation w^2+g(0,z)=0 gives g_z nonzero. The exact map N_H={w^2+g(u,z)=0} to fH, (u,w,z) maps to (u,v=u*w,z), is finite by the monic equation, birational with inverse w=v/u off u=0, and has a smooth normal source. It is the normalization. Solving z=psi(u,w) gives order2 on H={u=0}. Transversality with W1 gives ordW1(u)=1=d1*ordBplus(u), hence d1=1. The unique smooth R sheet similarly gives dc=1. Positivity and sum di=3 then force c=3 and all di=1, with two internal exponents both1.',
        'Pulling each internal factor to the smooth H normalization gives a divisor supported only on W1. Restriction to H has order2 because its A order is1 and H has ramification index2. Transversality makes the divisor exactly2W1. The same global W3 has conductor coefficient2 over B-minus and at least2+1 over B-plus. These are restrictions of one divisorial valuation of the actual conductor ideal on the normalization. The marked vectors (4,2+pplus,2+pplus) and (1+pminus,1+pminus,2) preserve all three sheet identities. At the minus side, exponent2 on the smooth R branch forces both intersections to equal1 and thereby the other two generic branches to be smooth, accounting for the absence of intrinsic branch-delta terms.',
        'For c=1 the two W points cannot be identified without forming a conductor loop. Pairwise support intersections force both to carry A, consuming exactly budget2. In the ramified case the two factors have supports A,+ and A,-, the length2 argument makes fR smooth and no other factor contains B-minus, contrary to its being critical. In the unramified case the third A-only normalization point gives three factors; every pair has pure generic intersection length1 on smooth A. Their complete-intersection rings are the reduced A, so reduction modulo z has length1 and independent normal linear terms. Each factor is smooth and their pairwise intersections are only A, excluding both purported B critical branches.',
        'The frozen derivation uses the fully checked square-part normalization and an exact fibre product V1 times_(B-normalization) Vc, with Vc degree1, to compare the same generic pair intersection on both signs. It proves 2*b_last=m and b_first=d1*tau*m, hence b_first=2*d1*tau*b_last with all factors positive. For c=2 this contradicts equality of first/last exponents; for c>=3 the sum of exponents is at leastc>=3, contradicting b<=2. This broader argument remains in the independent-check record. The stronger original SNC and conductor-exponent route, including its full equality case and all ten items, remains in the paper. No original mathematical error, proof substitution, target refutation or hypothesis narrowing is claimed.',
        'Both complete programs and outputs were read. The first supplies finite partition counts2,4,12,48 for ramified H and the stated supplementary cases, symbolic genus and normalization identities, and endpoint pairing budgets. The second independently computes the original component intersection polynomials, unique equality tuple(2,2,3,1,0,0), degree vector(1,1,1), exponent pair(1,1), normalization substitution and exact W3 difference pplus. Finite integer sweeps supplement the proved arbitrary inequalities. All15 original displays remain byte-identical after removing8 added semantic labels; all statement labels and targets remain. The minimal StatementRecord preserves the visible permanent tag. Exactly2 events in1 evidence group are admitted; source/program/root review adds no separate check credit.'
    ],
    chronology='Agent derivation froze10:00:03.220487 UTC; target release10:00:06.448528 UTC. Root frozen derivation read was recorded10:01:11 UTC before root target reading10:15:25 UTC. Supporting XU/XV/XW exposure was fully disclosed. The sealed packet was completed10:11:33.887628 UTC; current bibliography changes do not alter its exact original block.',
    original_proof_items_preserved=10, original_displays_preserved=15,
    original_inline_occurrences=208, mathematical_errors_found_in_original=[],
    target_statement_refuted=False, proof_substitution=False,
    packet_binding_count=packet_binding_count, packet_binding_occurrences=binding_occurrences,
    publication_page_reading_credit=0, evidence=evidence)
assert not (R/review).exists()
(R/review).write_text(json.dumps(rd, indent=2)+'\n')
with (R.parent/'S6_SERIES_GRIND_tags.tsv').open() as f:
    pages = {x['tag']:x['page'] for x in csv.DictReader(f, delimiter='\t')}
target = dict(owner=t['statement_owner'], tag=t['tag'], old_page=pages[t['tag']],
    original=t['full_original_block'], proposed=t['proposed_full_block'],
    freeze=t['freeze_receipt'], release=t['release_receipt'], events=a['event_proposals'], guards=guards,
    who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort not separately exposed; checker continuation2_A',
    scope='Full remaining degree-two horizontal sector with at least three generic normalization branches on the other image: exclusion of a single three-critical-branch junction. Exact graph path, spectral bound, normalization and globally marked conductor coefficients checked.',
    event_note='Root complete comparative review at '+now+'. All10 items,15 displays and original inline mathematics preserved;31 reversible owner guards and8 semantic labels. Original stronger conductor-exponent route retained, with no mathematical error or proof substitution. Two events in one evidence group; no R13 or independent-root event.')
anchor = read('records/S6_SERIES_PUBLISH_II_continuation2_batch77_config.json')['additional_source_edits'][-1]['new'].splitlines()[-1]
program_rows = (R/a['program_rows']['path']).read_text().rstrip('\n')
extra = [dict(old=anchor, new=anchor+'\n'+program_rows, type='D09', owner='Programs', location='Programs', reason='List the new program verifying the retained individual spectral, exponent, normalization and conductor-vector calculations. The separate frozen path-budget program remains check evidence.')]
copies = [dict(**{'from':bind('agents/continuation2_A/'+name)}, to='code/'+name) for name in ('S6_SERIES_PUBLISH_II_A2_YE_path_budget_output.json','S6_SERIES_PUBLISH_II_A2_YE_original_conductor_output.json')]
cfg = dict(batch=78, root_review_complete=True,
    source_before_sha256=bind('S6_SERIES_PUBLISH_II.tex')['sha256'],
    ledger_before_sha256=bind('CHECK_EVENTS.tsv')['sha256'],
    review_evidence=[bind(review), *evidence], targets=[target], additional_source_edits=extra,
    code_copies=copies, mathematical_repairs=[],
    scope='02YE admitted after the complete frozen derivation and all10 original/final items. All15 displays preserved,8 semantic labels added,31 owner guards and1 Programs append. Two events in1 group. No mathematical repair, theorem narrowing or proof substitution. R13, global-defect, provenance and final-page gates remain open.')
assert cfg['source_before_sha256'] == 'ada00878ff426b9b4c7a9a9527609847bc08122d2069528743d5cd35eb458c89'
assert cfg['ledger_before_sha256'] == '3f610c840282a4531b3c98974e014588571b09d9bb841a47e92367709fc7c562'
out = 'records/S6_SERIES_PUBLISH_II_continuation2_batch78_config.json'
assert not (R/out).exists()
(R/out).write_text(json.dumps(cfg, indent=2)+'\n')
print(json.dumps(dict(config=bind(out), review=bind(review), packet_binding_count=packet_binding_count, packet_binding_occurrences=binding_occurrences)))
