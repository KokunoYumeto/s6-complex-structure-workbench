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

pre = 'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_YB_v1_20261122/S6_SERIES_PUBLISH_II_A2_YB_'
mp = pre+'v1_manifest.json'; ap = pre+'admission_recommendation.json'
m = read(mp); a = read(ap); t = a['targets'][0]
assert bind(mp)['sha256'] == '5a554d61987bcc3197c621647b60bedf401c91a8b5eca3fbde42a084dea89948'
assert bind(ap)['sha256'] == '042a5aac07fad8d5924532aee39cd5567173cc6271849802f47c0591b4b44f18'
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
assert len(evidence_by_path) == 29
for p in [mp, ap, 'records/S6_SERIES_PUBLISH_II_YB_root_primary_01.json', 'records/S6_SERIES_PUBLISH_II_prepare75_failure01.json']:
    evidence_by_path[p] = bind(p)
p = read(a['proposal']['path'])
guards = [dict(old=g['literal_old'], new=g['literal_new'], type=','.join(g['defect_types']), reason=g['reason']) for g in p['guards']]
assert len(guards) == 20
old = (R/t['full_original_block']['path']).read_text()
new = (R/t['proposed_full_block']['path']).read_text()
w = old
for proposal, g in zip(p['guards'], guards):
    assert hashlib.sha256(w.encode()).hexdigest() == proposal['intermediate_before_sha256']
    assert w.count(g['old']) == 1
    w = w.replace(g['old'], g['new'], 1)
    assert hashlib.sha256(w.encode()).hexdigest() == proposal['intermediate_after_sha256']
assert w == new
assert old.count('\\item') == new.count('\\item') == 8
new_without_labels = new
for label in p['new_equation_labels']:
    assert old.count('\\label{'+label+'}') == 0
    assert new_without_labels.count('\\label{'+label+'}') == 1
    new_without_labels = new_without_labels.replace('\\label{'+label+'}', '')
pat = r'(?<!\\)\\\[(.*?)(?<!\\)\\\]'
od = [s.strip() for s in re.findall(pat, old, re.S)]
nd = [s.strip() for s in re.findall(pat, new_without_labels, re.S)]
assert len(od) == 7 and od == nd
for pattern in [r'\\label\{([^}]+)\}', r'\\hypertarget\{([^}]+)\}', r'\\tag\{([^}]+)\}']:
    assert re.findall(pattern, old) == re.findall(pattern, new_without_labels)

now = dt.datetime.now(dt.timezone.utc).isoformat()
review = 'records/S6_SERIES_PUBLISH_II_root_continuation2_batch75_review.json'
evidence = list(evidence_by_path.values())
rd = dict(created_utc=now,
    checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, root, second continuation; reasoning effort not separately exposed',
    actual_reading='Root read the complete 17752-byte frozen derivation before opening the original target. Then read all eight original and final proof items, the full comparison, all twenty exact owner guards, both complete standalone programs and their full outputs, input and postrelease receipts, freeze/release receipts and the complete supporting X7 proof. The initial combined guard/primary output was truncated; all twenty guards and the primary pages were subsequently read in bounded, untruncated calls. Root read all 8058 extracted bytes of the journal PDF pages5-6, printed480-481, after the acquisition receipt was written. That historical receipt deliberately retains root_reading_pending=true; this record supplies the later completed reading. No visual primary-page or publication-page reading credit is claimed. The small program-row, bibliography-entry and event files were fully read.',
    mathematical_review=[
        'The exact domain is the positive-Euler ruled case of the full torus fibration, with every reduced fibre support irreducible and normal crossing, base genus g>=1, and a noncontracted horizontal section H. The other image component is unrestricted. The completed conductor pushout XQ gives pi1(S)=pi1(C)=Z. All normalized image components are rational and the incidence graph has one cycle. The regular-part Euler bound and total bound e(S)<=2 give at most two components. X8 excludes the single-component forest possibility here. Hence C=A union B has exactly two components, and its graph branch excess is2.',
        'R6 gives the exact branch conductor coefficient c_i=2 delta_i+sum_{j!=i} I_ij. The coefficient-two horizontal section covers its image with degree d>=2. Total coefficient2 yields the transverse A3 case with d2; total3 yields D4 with d2 or3; total at least4 cannot occur. The remaining task is precisely to exclude the A3 case without a restriction on the other image component.',
        'For the A-primary conductor quotient, the sequence 0->Q->O_Csch->O_Aprimary->0 is exact. Rational singularities from X6 and the canonical trace identify sigma_*O_T(-D) with the conductor ideal I_N. The finite conductor map then gives O_Csch into nu_*(O_N/I_N) into rho_*O_D. The primary article KLS2022 section1.1 p480 states O_N=R sigma_*O_T equivalently Cohen-Macaulay plus sigma_*omega_T=omega_N; equations(1.1.1)-(1.1.3) are read with the full complex-analytic continuation p481. For the actual normal analytic N with rational singularities, this is the required trace statement. The original blowup calculation Dprime=beta^*Ddoubleprime-E uses beta_*O(E)=O and R1=0, with O_E(-1), so the divisor algebra pushes forward isomorphically. Iterating to 2H0+V0 gives the kernel layers O_P1(-2), whose H0 vanishes. Thus H0(Q)=0, H1 of the primary conductor surjects as required, and g-1<=chi(primary). The independently frozen vertical-duality route proves the same injection and remains in the check record.',
        'On the normalization of A, conormal K has degree2+degR, the saturated Hessian line L has degree sum d_i/2, and the nilradical J injects into n_*(K/L) with finite colengths b_i and q_p. The exact Euler expression is chi(primary)=4-T_A, with T_A=sum_p[delta_p+sum_i(d_i/2+b_i-r_i)+q_p]. The retained stronger original argument proves each singular point of A contributes at least3. In the planar case the radical is the complete intersection(u,h), so symbolic and ordinary powers agree. The primitive Hessian estimate gives d_i/2+b_i>=v_i and the exact finite-curve different gives sum_i(v_i-r_i)=2delta_p. Thus the local contribution is at least3delta_p+q_p. Root read X7 item4 in its complete owning block: finite Gorenstein duality gives length(A/I)=delta and length(B/I)=2delta, omega_B=I omega_A, and the order of dx/h_y is r_i-v_i. In the nonplanar case the absence of a linear equation gives b_i>=m_i, R15 gives d_i>=m_i, and r_i=m_i-1, yielding delta_p+sum_i(1+m_i/2)>=3. Smooth points contribute nonnegatively.',
        'The upper bound T_A<=5-g<=4 therefore permits at most one singular A-point. Every connected two-component graph of branch excess2 is counted: two A-B intersections; an A self-intersection plus an A-B intersection; a B self-intersection plus an A-B intersection; a triple point with two A branches; or a triple point with two B branches. Their A-normalization preimage counts, together with the permitted remaining unibranch singularity, allow at most3 possible ramification values. At a smooth conductor-image point R14 gives a transverse product tacnode or X(Y^2+XZ). The two graph maps X=plus-or-minus iY^2 have conductor parameter Z unchanged; the quadric resolution(s,v)->(-s v^2,s v,s) has strict conductor v=0 and parameter Z=s. These exact maps show no ramification at those smooth points. The degree-two Riemann-Hurwitz formula instead gives2g+2>=4 distinct branch values. This excludes A3 and proves the asserted D4 alternative.',
        'The frozen alternate weighted estimate keeps a<=1, k<=a+2, 2g+2<=k+s and T_A>=a+k/2+2s, giving T_A>=4g+1-a/2>=4g+1/2>5-g. Its five g1 graph gaps are5/2,2,5/2,1,1/2 and each increases by5 with g. The postrelease certificate separately checks the original stronger graph argument. Both programs and every output row were read. Their finite arithmetic checks do not substitute for the analytic conductor, trace or blowup maps, which are supplied by the prose derivations. The packet proposes exactly two events in one evidence group; no separate computation or supporting-result event is added.',
        'All eight original proof items, seven original displays and fifty-seven original inline mathematical formulas remain. Two semantic equation labels are added and all original labels and targets remain. No mathematical error, hypothesis change or proof substitution was found. R13 remains open; its unresolved reduced-horizontal uniqueness claim receives no credit from this check. No global defect, final provenance or final rendered-page row closes here.'
    ],
    chronology='Complete agent derivation froze09:15:35.820576 UTC; target release09:15:44.589198 UTC. Supporting completed proofs and transitive XQ Euler-zero input were disclosed. Root review compares that frozen derivation with every original step and adds no independent root event. Primary PDF acquired09:26:31.671100 UTC and its complete printed480-481 text read afterwards.',
    original_proof_items_preserved=8, original_displays_preserved=7,
    original_inline_formulas_preserved=57, mathematical_errors_found_in_original=[],
    publication_page_reading_credit=0, evidence=evidence)
assert not (R/review).exists()
(R/review).write_text(json.dumps(rd, indent=2)+'\n')
with (R.parent/'S6_SERIES_GRIND_tags.tsv').open() as f:
    pages = {x['tag']:x['page'] for x in csv.DictReader(f, delimiter='\t')}
target = dict(owner=t['statement_owner'], tag=t['tag'], old_page=pages[t['tag']],
    original=t['full_original_block'], proposed=t['proposed_full_block'],
    freeze=t['freeze_receipt'], release=t['release_receipt'], events=a['event_proposals'], guards=guards,
    who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort not separately exposed; checker continuation2_A',
    scope='Full positive-Euler ruled domain with noncontracted horizontal section and unrestricted other image component: transverse D4, horizontal degree2 or3; exclusion of A3 by exact primary conductor defects and branch-value count.',
    event_note='Root complete comparative review at '+now+'. All8 original items and7 displays retained; exact trace, conductor algebra, local different, blowup and normalization maps reviewed. No original mathematical error. Two events in one evidence group; no added independent root, supporting-result, computation or final-page event.')
extra = [dict(old=g['literal_old'], new=g['literal_new'], type=','.join(g['defect_types']), owner='Bibliography:KerrLazaSaito2022', location='Bibliography', reason=g['reason']) for g in p['bibliography_guards']]
anchor = read('records/S6_SERIES_PUBLISH_II_continuation2_batch74_config.json')['additional_source_edits'][0]['new'].splitlines()[-1]
program_row = (R/a['program_rows']['path']).read_text().rstrip('\n')
extra.append(dict(old=anchor, new=anchor+'\n'+program_row, type='D09', owner='Programs', location='Programs', reason='List the new program checking the finite defects and graph counts actually used in the retained original proof. The alternate frozen weighted program stays in the check records.'))
copies = [dict(**{'from':bind('agents/continuation2_A/'+name)}, to='code/'+name) for name in ('S6_SERIES_PUBLISH_II_A2_YB_primary_ramification_output.json', 'S6_SERIES_PUBLISH_II_A2_YB_original_graph_output.json')]
cfg = dict(batch=75, root_review_complete=True,
    source_before_sha256=bind('S6_SERIES_PUBLISH_II.tex')['sha256'],
    ledger_before_sha256=bind('CHECK_EVENTS.tsv')['sha256'],
    review_evidence=[bind(review), *evidence], targets=[target], additional_source_edits=extra,
    code_copies=copies, mathematical_repairs=[],
    scope='02YB admitted after the complete frozen derivation and all8 original/final items. Seven displays and57 inline formulas retained, with2 semantic labels. Twenty owner guards, one primary bibliography entry and one Programs row;2 events in1 group. The stronger original defect>=3 and blowup proof are preserved. No original error or proof substitution; no R13, global-defect, final-provenance or page-reading closure.')
assert cfg['source_before_sha256'] == '4f935c983189bf1d20148cea594fe252f8a19c702b730ea24c2d90a7874bcf53'
assert cfg['ledger_before_sha256'] == 'fbff6131b3b5be996a12c9060bfcd8e7c5d1c461a05d9ba866ede1284be0520a'
out = 'records/S6_SERIES_PUBLISH_II_continuation2_batch75_config.json'
assert not (R/out).exists()
(R/out).write_text(json.dumps(cfg, indent=2)+'\n')
print(json.dumps(bind(out)))
