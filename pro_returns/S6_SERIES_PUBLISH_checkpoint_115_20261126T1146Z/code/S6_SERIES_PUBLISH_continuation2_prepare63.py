from pathlib import Path
import csv, datetime as dt, hashlib, json, re

R = Path(__file__).resolve().parents[1]

def bind(p):
    return dict(path=p, sha256=hashlib.sha256((R / p).read_bytes()).hexdigest())

def read(p):
    return json.loads((R / p).read_text())

def verify(o):
    if isinstance(o, dict):
        if 'path' in o and 'sha256' in o:
            assert bind(o['path'])['sha256'] == o['sha256'], o['path']
        for v in o.values():
            verify(v)
    elif isinstance(o, list):
        for v in o:
            verify(v)

ap = 'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_X7_v1_20261122/S6_SERIES_PUBLISH_II_A2_X7_admission_recommendation.json'
assert bind(ap)['sha256'] == '42bf5f1c04478ff9eda124190feec3e992392edac8c89c6c55b8f742a520475a'
a = read(ap)
verify(a)
at = a['targets'][0]
p = read(a['proposal']['path'])
guards = [dict(old=g['literal_old'], new=g['literal_new'], type=','.join(g['defect_types']), reason=g['reason']) for g in p['guards']]
old = (R / at['full_original_block']['path']).read_text()
new = (R / at['proposed_full_block']['path']).read_text()
w = old
for g in guards:
    assert w.count(g['old']) == 1
    w = w.replace(g['old'], g['new'], 1)
assert w == new and old.count('\\item') == new.count('\\item') == 9
assert re.findall(r'\\\[(.*?)\\\]', old, re.S) == re.findall(r'\\\[(.*?)\\\]', new, re.S)
for pat in [r'\\label\{([^}]+)\}', r'\\hypertarget\{([^}]+)\}']:
    assert re.findall(pat, old) == re.findall(pat, new)

now = dt.datetime.now(dt.timezone.utc).isoformat()
review = 'records/S6_SERIES_PUBLISH_II_root_continuation2_batch63_review.json'
assert not (R / review).exists()
rd = dict(
    created_utc=now,
    checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, root, second continuation; reasoning effort not separately exposed',
    actual_reading='The entire frozen derivation was read before the original target. The full original nine-item proof and final nine-item proof, all three displays, entire item-by-item comparison, both complete program sources and outputs, all twenty-two guards, both event proposals, all chronology receipts, input/primary receipts and program scope were actually read. A single oversized attempted read was truncated and gave no reading credit; the original, final and comparison were then read in separate complete outputs. Guards 11-18 were reread separately after an aggregate-output truncation. Primary pages remain credited to the checker and earlier accepted readings; no new root opening of those primary works is claimed.',
    mathematical_review=[
        'The exact standing torus-fibration domain is resolved to P4.12. For the rational normal-crossing alternative, the normalization calculation in P4.6 gives e(S)=2 with coherent Euler characteristic one. Otherwise the full resolved conductor A and rational surface T are simply connected. The compact conductor pushout and its compatible triangulation identify pi1(C)->pi1(S) through the actual inclusion. The normalized components are rational and the incidence graph gives e(C)=c+1-b and pi1(C)=F_b. Virtual abelianness gives b<=1; e(S_reg)>=0 and e(S)=1 force c=b=1, exactly one two-branch point, and all other points unibranch.',
        'The normalization is finite and its normal two-dimensional local rings are Cohen-Macaulay. The actual conductor is Hom_OS(nu_*ON,OS), with evaluation at1 and inverse multiplication as the identification inside the total quotient ring. Finite canonical duality makes it a depth-two module; the conductor quotient is pure of dimension one. The transverse ordinary triple conductor is order two on each branch: the quadratic evaluation matrix has determinant -1 and the branch-idempotent first-jet test has trivial kernel. Thus J=P^(2), because their finite-length quotient embeds in the pure conductor scheme. The previously proved Euler characteristic is -1.',
        'Let M=P/P^(2), n:E->C and j=i n. The printed K is exactly the frozen V as the same kernel inside j^*Omega_Y. With F the image of n^*M, the exact sequence 0->n_*F/M->n_*V/M->n_*(V/F)->0 gives tau_p=q_p+ell_p and hence d_p=L_p, without an abstract rank-only identification. Degree of j^*Omega_Y is zero and deg Omega_P1=-2, giving deg K=2+deg R, chi(K)=4+deg R and chi(OY/P^(2))=5-sum d_p.',
        'For a plane curve P=(z,h), the differential identifies M with OC dz plus OC dh. Normalization adds length delta to each summand and the primitive-gradient multiplier adds sum v_i, so tau=2delta+sum v_i. Applying Hom(-,A) to A->B gives A/I=Ext1(B/A,A), while Ext1(B,A)=0 for the maximal Cohen-Macaulay B over the Gorenstein curve ring. Finite-length duality preserves length, yielding length(B/I)=2delta. The residue dx/h_y and the identity omega_B=I omega_A inside meromorphic differentials give c_i=v_i-r_i. Thus sum(v_i-r_i)=2delta and d=5delta.',
        'The stronger original nonplanar-unibranch estimate was verified after release, with that chronology explicit. For multiplicity2, the square-root parameter change gives x=t^2; unique even/odd decompositions and the triangular subtraction using the holomorphic ratio of the two odd coefficients give a smooth containing surface. Thus nonplanarity requires m>=3. The valuation filtration counts delta gaps and gives delta>=m-1, while gradient-minor colength and q>=0 give tau>=2m. Equality d=6 would force m3, delta2, tau6. Then elements of orders3,4,5 form ambient coordinates because their cotangent classes are independent modulo maximal-ideal square. The unique quadratic orders6 and7 force the x^2 and xy coefficients to vanish. Every order-three initial gradient lies in the z direction, so all two-by-two minors have order>=7. Higher terms have gradient order>=6 and cannot restore an order-six minor. This contradicts tau6.',
        'For two smooth branches a common immersive linear coordinate gives graph pairs (a_i(x),b_i(x)). Dividing their differences by their common x power produces the printed F with a unit y or z derivative. The explicit maps (x,y,z)->(x,y,F) or (x,F,z) are invertible and exhibit a smooth containing surface. Thus a nonplanar two-branch point has m1+m2>=3. The exact diagonal/difference normalization sequence gives delta=delta1+delta2+length OY/(P1+P2)>=m1+m2-1. Branchwise gradient minors yield tau>=2(m1+m2), and r=m1+m2-2, so d>=7.',
        'At the unique two-branch point the defect is5 for a plane node, at least10 for the other plane cases, or at least7 for the nonplanar case. Every additional singularity contributes at least5 or7 under the retained stronger proof. The sum is5 or at least7, never6; chi=-1 is therefore impossible. The frozen derivation used the sufficient weaker lower bound2 for additional unibranch points and has the same gap. The nonnegative fibre Euler sum is at most2 and the rational case is positive, so the final value is2. All nine original mathematical steps, three displays and85 original mathematical inline spans remain; no mathematical error or proof substitution was found.'
    ],
    chronology='Complete derivation frozen at07:05:49.819961 UTC and proof released at07:05:57.212629 UTC. Supporting proof exposure is disclosed. The stronger original unibranch estimate and the second program are postrelease comparisons and are not backdated. Exactly one targeted check and one full comparative reread share one evidence group; root review adds no event.',
    original_proof_items_preserved=9,
    original_displays_preserved=3,
    original_inline_expressions_preserved=85,
    mathematical_errors_found=[],
    publication_page_reading_credit=0,
    pending_global_typesetting='All permanent labels and hypertargets survive. The paper-wide visible small tag and section-numbering pass remains open, together with the other global defect classes.',
    evidence=[bind(ap), a['comparison'], a['program_scope'], a['display_preservation'], a['input_receipt'], a['primary_sources'], a['postrelease_comparison_receipt']]
)
(R / review).write_text(json.dumps(rd, indent=2) + '\n')
with (R.parent / 'S6_SERIES_GRIND_tags.tsv').open() as f:
    pages = {x['tag']: x['page'] for x in csv.DictReader(f, delimiter='\t')}
target = dict(owner=at['statement_owner'], tag=at['tag'], old_page=pages[at['tag']], original=at['full_original_block'], proposed=at['proposed_full_block'], freeze=at['freeze_receipt'], release=at['release_receipt'], events=a['event_proposals'], guards=guards, who=rd['checker'], scope='Exclusion of Euler number one for an irreducible support with rationally resolved normalization and a generic ordinary triple curve, followed by the exact value two under the mixed fibre hypothesis.', event_note='Root complete frozen/original/final comparison at ' + now + '. Exact quotient sequence identifies tau=ell+q and d=L; the stronger retained nonplanar-unibranch estimate was verified after release. No root independent credit.')
s = (R / 'S6_SERIES_PUBLISH_II.tex').read_text()
start = s.index('\\section*{Programs}')
end = s.index('\\end{longtable}', start)
last = s[s.rfind('\n', start, end - 1) + 1:end]
assert last.strip()
rows = (R / a['program_rows']['path']).read_text()
extra = [dict(old=last, new=last + rows, type='D09,D18', owner='Programs', location='Programs', reason='Cite each bounded new computation once for the printed conductor Euler identities and the stronger original gradient-minor bounds.')]
scope = read(a['program_scope']['path'])
copies = [dict(**{'from': x['output']}, to='code/' + Path(x['output']['path']).name) for x in scope['new_computations']]
cfg = dict(batch=63, root_review_complete=True, source_before_sha256=bind('S6_SERIES_PUBLISH_II.tex')['sha256'], ledger_before_sha256=bind('CHECK_EVENTS.tsv')['sha256'], review_evidence=[bind(review), bind(ap), a['comparison'], a['proposal'], a['program_scope'], a['display_preservation'], a['input_receipt'], a['primary_sources'], a['postrelease_comparison_receipt'], a['derivation']], targets=[target], additional_source_edits=extra, code_copies=copies, mathematical_repairs=[], scope='02X7 admitted following the full prerelease derivation and complete original/final comparison. All nine proof items, three displays and85 original inline mathematical spans retained. Twenty-two reversible target guards and two bounded program references; two events in one evidence group. Exact conductor, conormal quotient and local coordinate maps verified. No global defect or page-reading closure.')
assert cfg['source_before_sha256'] == 'c967e8b2c8738deec39e4e47f3109ea8a4008c692f3e1167b9e4147cf506f03e'
assert cfg['ledger_before_sha256'] == '14a469ba78f99b0a140f58173f3dc6caacb11f69106708736f7ebd04d8ee3b30'
out = 'records/S6_SERIES_PUBLISH_II_continuation2_batch63_config.json'
assert not (R / out).exists()
(R / out).write_text(json.dumps(cfg, indent=2) + '\n')
print(json.dumps(bind(out)))
