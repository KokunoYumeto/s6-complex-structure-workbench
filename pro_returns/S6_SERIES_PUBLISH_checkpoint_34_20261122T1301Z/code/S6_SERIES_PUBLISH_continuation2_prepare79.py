from pathlib import Path
import csv, datetime as dt, hashlib, json, re

R = Path(__file__).resolve().parents[1]

def bind(p):
    b = (R / p).read_bytes()
    return dict(path=p, sha256=hashlib.sha256(b).hexdigest(), bytes=len(b))

def read(p):
    return json.loads((R / p).read_text())

pre = 'agents/continuation2_B/01CL/S6_SERIES_PUBLISH_II_B2_CL_'
ip, ap = pre + 'packet_index.json', pre + 'admission_proposal.json'
assert bind(ip)['sha256'] == 'ab1b5d164bcff37a4effa7c611feaff58125751f14ca5a63ab5d31ab7734a293'
assert bind(ap)['sha256'] == 'facb1142d61d8cf8dc3d2fe84dabde348664dbc1a1753a3bd7568227675384f6'
idx, a = read(ip), read(ap)
t = a['targets'][0]
ev = {}
binding_occurrences = 0

def bindings(x):
    global binding_occurrences
    if isinstance(x, dict):
        if 'path' in x and 'sha256' in x:
            b = bind(x['path'])
            assert b['sha256'] == x['sha256'], x['path']
            if 'bytes' in x:
                assert b['bytes'] == x['bytes'], x['path']
            ev[x['path']] = b
            binding_occurrences += 1
        for v in x.values():
            bindings(v)
    elif isinstance(x, list):
        for v in x:
            bindings(v)

bindings(idx)
bindings(a)
packet_unique_bindings = len(ev)
for p in [ip, ap, 'records/S6_SERIES_PUBLISH_II_CL_root_derivation_read_01.json']:
    ev[p] = bind(p)
assert ev['records/S6_SERIES_PUBLISH_II_CL_root_derivation_read_01.json']['sha256'] == 'e64e416ca6ebeb845bfa6a35db964389bc265aaa6dad758150a1810caddaf8f3'
guards = [dict(old=g['old'], new=g['new'], type=g['defect_type'], reason=g['reason'],
               occurrences=g['expected_occurrences_in_owning_block'])
          for g in read(pre + 'body_guards.json')]
assert len(guards) == 26
old = (R / t['original_full_block']['path']).read_text()
new = (R / t['proposed_full_block']['path']).read_text()
w = old
for g in guards:
    assert w.count(g['old']) == g['occurrences']
    w = w.replace(g['old'], g['new'], g['occurrences'])
assert w == new
assert sum(g['occurrences'] for g in guards) == 28
assert old.count('\\item') == new.count('\\item') == 10
pat = r'(?<!\\)\\\[(.*?)(?<!\\)\\\]'
od, nd = re.findall(pat, old, re.S), re.findall(pat, new, re.S)
assert len(od) == 11 and len(nd) == 12
j = 0
for d in nd:
    if j < len(od) and d == od[j]:
        j += 1
assert j == 11
for pat in [r'\\label\{([^}]+)\}', r'\\hypertarget\{([^}]+)\}', r'\\tag\{([^}]+)\}']:
    assert re.findall(pat, old) == re.findall(pat, new)
source, ledger = bind('S6_SERIES_PUBLISH_II.tex'), bind('CHECK_EVENTS.tsv')
assert source['sha256'] == 'fbc83827fb6b633dd9e735146f4b87e014e2f53189f89a8a059d4c361f9c5676'
assert ledger['sha256'] == 'e0f20711c4867546863ae01f162d29919c641559b816ed9aa74c788f8ebd84ac'
extra = [dict(old=g['old'], new=g['new'], type=g['defect_type'],
              owner='Bibliography' if g['change_id'].endswith('BIB-GR') else 'Programs',
              location=g['location'], reason=g['reason']) for g in a['additional_source_guards']]
assert len(extra) == 2
s = (R / 'S6_SERIES_PUBLISH_II.tex').read_text()
assert s.count(old) == 1
s = s.replace(old, new, 1)
for g in extra:
    assert s.count(g['old']) == 1
    s = s.replace(g['old'], g['new'], 1)
assert hashlib.sha256(s.encode()).hexdigest() == '7479f18411be8c59f79cfedd89a079b089c6742a81faed216b7b26e5d8ae1874'
now = dt.datetime.now(dt.timezone.utc).isoformat()
primary_images = []
for number, page in [(12,274),(13,275),(14,276),(15,277),(16,278)]:
    p = R.parent / 'temporary_B_pdf' / f'S6_SERIES_PUBLISH_CL_GR1970_page-{number}.png'
    payload = p.read_bytes()
    primary_images.append(dict(path=str(p), printed_page=page, sha256=hashlib.sha256(payload).hexdigest(),
                               actual_root_image_read=True, publication_page_credit=0))
review = 'records/S6_SERIES_PUBLISH_II_root_continuation2_batch79_review.json'
rd = dict(
    created_utc=now,
    checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, root, second continuation; reasoning effort not separately exposed',
    actual_reading='Root read the entire 26988-byte frozen derivation before opening the target, as separately timestamped. Root subsequently read all 10 original and final proof items, all 11 original displays and the new duality sequence, the entire postrelease comparison and review, both full program sources, every final check object and the complete numerical evidence including all 13 root-position configurations and all 17 weighted charts. The local, chart, increment and quotient evidence repeated between outputs was explicitly byte/object-compared after its first full reading. Root read all 26 body guards, both supplementary guards, the entire 411-line target diff, supplementary diff, all metadata/chronology/execution/identity/reading receipts, and the whole 15369-byte BX supporting block. The oversized initial primary-image call after the preceding context boundary yielded no readable content; root subsequently viewed and actually read each of the five GR images separately or in a two-image return. One later combined receipt/admission output was truncated only within embedded guards; admission metadata was reread with guards excluded, while all guards had already been read completely. No reading credit comes from either truncated return. Assembly scripts are hash-bound but no mathematical-reading credit is assigned to them.',
    chronology='Agent start09:56:21.104399 UTC; final prereading program10:04:56.480849--10:04:56.986991 UTC; complete derivation freeze10:05:51.965756 UTC; target release10:06:03.764539 UTC. Root derivation-reading receipt precedes root target opening. The stronger uniform original q=0 and all weighted-node/cusp rationality conclusions were compared after release; this timing is retained. The independent frozen proof covers every target case, with different local and compact-pairing routes kept in records.',
    primary_reading=dict(
        images=primary_images,
        scope='Actual complete printed pp274--278 of Grauert--Riemenschneider1970: Satz2.3 and its complete proof, Satz2.4 and proof, and the canonical-sheaf definition plus Satz3.1 statement on p278. The proof of Satz3.1 continues on p279 and no root full-proof reading of that result is claimed. Root also read the complete mathematical bodies of official Stacks0AU3 and0A81, including proper duality4(c), Theorem47.18.3 and Lemma47.18.4 with their proofs.',
        urls=['https://www.math.uni-hamburg.de/home/riemenschneider/OR1970c.pdf', 'https://stacks.math.columbia.edu/tag/0AU3', 'https://stacks.math.columbia.edu/tag/0A81'],
        web_refs=['turn508194781view0', 'turn508194781view1'],
        doi='10.1007/BF01403182',
        doi_metadata='Agent Crossref receipt fully read; publisher DOI was inaccessible to the agent. Author-hosted primary supplies correct accented title. No root fresh reading of 0FVU/0A9Q or earlier primary articles is claimed.'),
    mathematical_review=[
        'The full RAT1 domain remains: torus fibre, rational normalization, specified ruled-boundary map, noncontracted connected degree-two normalization cover of an ordinary-triple image, including every common cubic zero with multiplicity. A5.19 makes a singular image have degree-one normalization cover, so H is smooth; Riemann--Hurwitz from C=P1 makes H=P1. With lines convention W=P(N), degN=-2, xi^2=2, K_W=-2xi, and the cubic root divisor has class3xi.',
        'The original splitting proof N=O(a)+O(-2-a), a>=-1, is retained. For a>=0 and v>0 the coefficient of the first pure cube has degree-3a-v and vanishes; the irreducible residual quadratic has nonzero first-square coefficient of degree2-a-v. Thus a+v<=2. For a=-1, tensoring lines with O(1), inverse O(-1), gives W=P1xP1, xi=(1,1), R1=(1,d), R2=(2,3-v-d), d>=0. Integrality of R2 requires its second degree>=1, so v<=2. The frozen root-line method gives p_a(R2)=3+ell-v and R1.R2=2-ell-v; its exact correspondence is ell=-1-d in the balanced case and ell=0 for the unbalanced v2 case. Both methods cover the same root divisors. At v2 the two rational normalization components of B_h give total delta1. Completing the local quadratic by X=(x+b(t)/2)/sqrt(d(t)), with inverse x=sqrt(d(t))X-b(t)/2, gives X^2=t^mu; delta1 means mu2 or3, the full node/cusp alternatives.',
        'For A=p+q the reduced branch B=R1+R2+Fp+Fq has class3xi. Its connected normal cyclic cover X0 is projective and Gorenstein, omega_X0=O, H1(O_X0)=0 and chi(O_X0)=2. The complete local list is A1,A2,A3 with p_g/linkb1=0, and D4,D5,D6 with p_g1, linkb1 respectively2,0,0. Each positive genus consumes the sole horizontal delta, so totalP<=1 and lambda<=2. This list agrees between the embedded-resolution/monodromy calculation and the independent Koszul Hilbert-series computation.',
        'The stronger original uniform q=0 argument is retained. For a projective resolution rho and a sufficiently positive ample line A0 on X0, actual GR1970 Satz2.3 gives R^i rho_*(rho^*A0 tensor omega_X)=0 for i>0. Projection formula and tensoring A0^-1 give R^i rho_*omega_X=0. Set M=R1rho_*O_X, finite length with local dimension p_g. Dualize O_X0 -> Rrho_*O_X -> M[-1] against omega_X0[2]. Proper duality identifies the middle dual with Rrho_*omega_X[2]. Local duality concentrates the finite-length dual in Ext2(M,omega_X0), equal to its completed Matlis dual, of lengthP. Cohomology of the dualized triangle gives 0 -> rho_*omega_X -> omega_X0 -> Ext2(M,omega_X0) ->0. The first arrow is restriction to the common smooth locus followed by extension in the reflexive target omega_X0; the second is the connecting map. P>0 makes the canonical ideal proper at a point, so no global nonzero constant lies in it; p_g(X)=0, chi(O_X)=2-P, q=P-1=0. For P0 the sequence and chi give q0 directly.',
        'For D=X minus U a simple-normal-crossing boundary, write g^*B_i=3Btilde_i+sum a_ji E_j. A base relation alpha maps to strict coefficients alpha and exceptional coefficients sum a_ji alpha_i/3; pushforward followed by projection to strict coefficients is its inverse. With four branch classes spanning rank2 and independent exceptional classes, there are exactly2 boundary relations. Their span contains g^*xi of square6, so Hodge index makes it nondegenerate. The pair and normalization sequences give b1(U)=2, e(U)=3(nu-4), b1(D)=nu-3+lambda and compact intersection rank2nu-8-lambda.',
        'The existing evaluation isomorphism U -> {v in N:q3(v)=1} sends a nonzero dual root w on a line ell to its unique v with w(v)=1, and the converse is the inverse. The radial derivative is3; compact transport with the full fibre multiplicity embeds a compact core into a nearby torus. Its fundamental-group image has rank<=2. The core map lifts to the corresponding torus cover; H2 maps to the exterior square of that image, whose fourth wedge is zero. Therefore its preserved compact intersection form has rank0, giving nu=4+lambda/2<=5. The two special fibre branch counts are2+a_p+a_q, a_p,a_q in{1,2}. Lost attachment values number at most a_p+a_q-2 plus outside multibranch excess, namely nu-4<=1. The same actual conductor C and all vertical images enter the existing graph; wholly exceptional trees are bounded by N0 and the residual ordinary-triple branch gives r_dom<=1. Hence e(S)>=2-r_dom-loss>=0.',
        'For A=2p the normalized cyclic algebra is O+L^-1+L^-2(Fp), with extra integral generator w^2/s at w^3=s^2u. The normal surface is Cohen--Macaulay; finite pushforward to the smooth surface is locally free, and its character lines are rank-one reflexive. The divisorwise generator identifications therefore extend uniquely over all crossings. Relative duality gives R1p_*L^-2(Fp)=O(-1), so H1(O_X0)=0.',
        'The original uniform rationality proof is retained, including all allowed weighted node/cusp positions. At a branch D1+2D2 point, write m1+2m2=3k+j, 0<=j<3. A blowup with exceptional equation e has Lprime=sigma^*L(-kE), D2prime=sigma^*D2-m2E+1_(j2)E. The exact generator maps are w_old=e^k w_new and w_old^2/d2=e^(2k-m2+1_(j2)) w_new^2/d2prime. Thus the character increments are k and2k-m2+1_(j2). Cases(m1,m2)=(1,1),(2,1),(2,0) give(1,1),(1,1),(0,1). The complete inherited BX contact calculation C.DD18--20 has been reread, including the complementary smooth charts and the generator w^2/s.',
        'All17 main and complementary charts have been read and checked. The weighted transverse node w^3=s^2x(x-s) gives w1^3=su(u-1) or xu^2(1-u). The contact node w^3=s^2x(s-x^2) gives, under s=xu,w=xw1 then u=xy,w1=xw2, equations w1^3=xu^2(u-x), w2^3=xy^2(y-1), with complementary su(1-su^2) and uy(1-y). The cusp w^3=s^2(x^2-s^3) gives x=su,w=sw1, then s=uv, then v=uy,w1=uw2, resulting in s(u^2-s), u^2v(u-v), uy(1-y). Complementary equations are xv^2(1-xv^3), s^2(sv^2-1), vy^2(y-1). Their reduced support is smooth or transverse at the remaining exceptional points.',
        'For every crossing w^3=x^a y^b, a,b in{1,2}, the map x=u^3,y=v^3,w=u^a v^b from C2/G has G={(zeta^i,zeta^j):ai+bj=0 mod3}. Its invariant field has degree3 over C(x,y), generated by w, and the finite normal invariant ring is the integral closure. For equal weights G has weights(1,2), ringC[u^3,v^3,uv], (uv)^3=xy; uv=w for(1,1), uv=w^2/(xy) for(2,2). For unequal weights G has weights(1,1), the cubic Veronese ring; the missing generator is w^2/x for(2,1), w^2/y for(1,2). Their resolutions are the A2 chain and O_P1(-3), respectively. The latter formal cohomology has termsH1(O(3j))=0. The former is the explicit rational A2 resolution. Thus R1O=0 in all four cases.',
        'Each exceptional increment is0 or1. The blowup exact sequence O -> O(E) -> O_P1(-1), together with the structure-sheaf direct images, gives sigma_*O(E)=O and R1sigma_*O(E)=0. Projection formula gives the same vanishing for every character line. The nonnegative generator exponents give proper birational maps f of normalized covers with p0 f=sigma pprime. Finite pushforward and Leray yield p0_*R1f_*O=R1sigma_*(pprime_*O)=0, and faithfulness makes R1f_*O=0. Proper birationality onto the normal target gives f_*O=O. Iteration and the final rational quotient resolutions prove all original local rationality claims. Thus b1(X)=lambda0. With three branch classes of rank2, b1(U)=1, e(U)=3(nu-2), b1(D)=nu-2 and compact rank2nu-4. The same torus transport gives nu2, one C-preimage at p, no multibranch point away from p, zero attachment loss and the original stronger e(S)>=2-r_dom>=1.',
        'All10 original proof items and all11 original displays remain, in order and byte identically. The only additional display is the canonical-sheaf exact sequence. Labels, hypertargets and literal equation tags are identical; the visible statement tag is retained in the minimal StatementRecord. The independently frozen alternative routes remain in the records. No original mathematical error, scope restriction or proof replacement was found. The full39-check prereading output and45-check comparison output give one computation evidence group; the earlier38-check run is retained for chronology and not counted again. The unavailable historical A_cubic_scalar_two.py is not represented as executed. The Programs rows point to the two new standalone programs. The actual-read GR article receives its precise bibliography entry; global bibliography ordering/master synchronization remains a separate pending operation. No global defect class, final provenance or final publication-page gate closes here.'
    ],
    original_proof_items_preserved=10,
    original_displays_preserved=11,
    additional_display='Canonical-sheaf exact sequence from proper and local duality',
    mathematical_errors_found_in_original=[],
    packet_unique_bindings=packet_unique_bindings,
    packet_binding_occurrences=binding_occurrences,
    publication_page_reading_credit=0,
    evidence=list(ev.values()))
with (R.parent / 'S6_SERIES_GRIND_tags.tsv').open() as f:
    pages = {x['tag']:x['page'] for x in csv.DictReader(f, delimiter='\t')}
target = dict(owner=t['statement_owner'], tag=t['tag'], old_page=pages[t['tag']],
              original=t['original_full_block'], proposed=t['proposed_full_block'],
              freeze=t['freeze_receipt'], release=t['release_receipt'], events=idx['events'], guards=guards,
              who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort not separately exposed; checker continuation2_B',
              scope='Complete rational degree-two ordinary-triple cover, all common cubic zeros and multiplicities: v<=2, both two-simple-zero and double-zero cases, all local cyclic charts, compact-pairing and conductor-graph maps, and e(S)>=0.',
              event_note='Complete root comparative review at '+now+'. All10 original items and11 displays preserved;39+45 exact checks fully read; actual primary GR images and proper/local duality locators verified. Stronger original uniform q=0 and weighted rationality routes retained. No original mathematical error, scope restriction, or independent root credit. Three events in one evidence group.')
copies=[]
for c in a['computations']:
    for kind in ['program','output','receipt']:
        b=c[kind]
        copies.append(dict(**{'from':b},to='code/'+Path(b['path']).name))
cfg=dict(batch=79,root_review_complete=True,source_before_sha256=source['sha256'],ledger_before_sha256=ledger['sha256'],
         review_evidence=[],targets=[target],additional_source_edits=extra,code_copies=copies,mathematical_repairs=[],
         scope='01CL admitted after the full frozen derivation and all10 original/final items. All11 original displays, labels, targets and equation tags retained; one explicit duality-sequence display added. Twenty-six target guards cover28 literal occurrences, plus Programs and bibliography guards. Three events in one group. Original stronger vanishing and weighted-resolution arguments retained with exact maps and primary citations. No scope restriction, original mathematical error, global-defect, final-provenance or publication-page closure.')
out='records/S6_SERIES_PUBLISH_II_continuation2_batch79_config.json'
assert not (R/review).exists() and not (R/out).exists()
(R/review).write_text(json.dumps(rd,indent=2)+'\n')
cfg['review_evidence']=[bind(review),*ev.values()]
(R/out).write_text(json.dumps(cfg,indent=2)+'\n')
print(json.dumps(dict(config=bind(out),review=bind(review),packet_unique_bindings=packet_unique_bindings,
                      packet_binding_occurrences=binding_occurrences,review_bindings=len(ev))))
