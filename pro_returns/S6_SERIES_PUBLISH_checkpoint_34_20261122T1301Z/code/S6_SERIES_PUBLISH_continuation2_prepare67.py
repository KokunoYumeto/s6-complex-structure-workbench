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
        for v in o.values():
            verify(v)
    elif isinstance(o, list):
        for v in o:
            verify(v)

pre = 'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_X9_v1_20261122/S6_SERIES_PUBLISH_II_A2_X9_'
ap = pre + 'admission_recommendation.json'
assert bind(ap)['sha256'] == '56f698a856d3584d91d8e079f58e379bdeaede805adee9bb41f3f193cfd29484'
a = read(ap)
verify(a)
at = a['targets'][0]
p = read(a['proposal']['path'])
guards = [dict(old=g['literal_old'], new=g['literal_new'], type=','.join(g['defect_types']), reason=g['reason']) for g in p['guards']]
assert len(guards) == 28
old = (R / at['full_original_block']['path']).read_text()
new = (R / at['proposed_full_block']['path']).read_text()
w = old
for g in guards:
    assert w.count(g['old']) == 1
    w = w.replace(g['old'], g['new'], 1)
assert w == new and old.count('\\item') == new.count('\\item') == 8
stripped = new
for label in p['new_equation_labels']:
    assert stripped.count('\\label{' + label + '}') == 1
    stripped = stripped.replace('\\label{' + label + '}', '')
assert re.findall(r'\\\[(.*?)\\\]', old, re.S) == re.findall(r'\\\[(.*?)\\\]', stripped, re.S)
assert len(re.findall(r'\\\[(.*?)\\\]', old, re.S)) == 9
for pat in [r'\\label\{([^}]+)\}', r'\\hypertarget\{([^}]+)\}', r'\\tag\{([^}]+)\}']:
    assert re.findall(pat, old) == re.findall(pat, stripped)
clarification = 'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_X9_v1_metadata_clarification.json'
assert bind(clarification)['sha256'] == '2ab985da0054026c421c3b99532deded5b981de84a4d9eae52046b4f66dc3abc'
verify(read(clarification))
now = dt.datetime.now(dt.timezone.utc).isoformat()
review = 'records/S6_SERIES_PUBLISH_II_root_continuation2_batch67_review.json'
assert not (R / review).exists()
rd = dict(
    created_utc=now,
    checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, root, second continuation; reasoning effort not separately exposed',
    actual_reading='Root read the entire frozen derivation before opening the target. All eight original and eight proposed proof items, all nine displays, the entire stepwise comparison, all twenty-eight guards, both complete program sources and outputs, Programs rows, both events, freeze/release/input/postrelease receipts, display preservation and the separate metadata clarification were read in bounded untruncated outputs. Reused WW primary-source receipts were read; no new opening of their primary texts is claimed.',
    mathematical_review=[
        'The exact maps are sigma:T->N, the minimal resolution; nu:N->S, the finite normalization; rho=(S inclusion Y) composed with nu composed with sigma; and pi:T->T0, the Hopf blowdown. The frozen proof calls sigma pi and the blowdown beta. A primary unramified cover q0:T0prime->T0 pulls back all point blowups, producing q:Tprime->T and exactly degree(q) times as many blowups. Its ambient map is rho composed with q, and its map to the original N is sigma composed with q. No covering map to a new singular normalization is constructed or needed.',
        'The nonsingular primary Hopf foliation is the disclosed completed WW input. Its local regular blowup generator u*d/du-v*d/dv and saddle generators b*u*d/du-(a+b)*v*d/dv and (a+b)*u*d/du-a*v*d/dv follow from the two actual coordinate Jacobians. The new saddles lie on the new exceptional curve and have ideal (u,v). The transverse-form exceptional order is epsilon=0 or 1, yielding Kprime=mu*K+E, Vprime=mu*V+epsilon E, c1(L)=-K+V, K squared=-k and KV=V squared. These are numerical identities with the same line bundles and pullbacks in both proofs.',
        'The original resolution may contract curves, so the effective common divisorial zero Z of L->rho*TY is retained. Dividing local coefficients defines Lprime=L(Z)->B. Absence of a common height-one factor makes its quotient Q torsionfree in the regular local surface ring. Q double-dual is locally free; c1(B)=c2(B)=0 rationally gives c2(Q double-dual)=(-K+V+Z) squared-z0, with z0 the nonnegative finite length. Saturation of the rank-two derivative image EB and torsionfreeness of B/EB place the divided line in EB. The extended rank-one saturation J in Q double-dual has c1=R-V-Z; its remaining ideal-sheaf quotient has c1=K-R and nonnegative length z1. This gives the exact original Chern equation.',
        'Expanding that equation with K squared=-k and KV=V squared gives B(R,Z)=R squared-KR-VR-ZR-KZ+2VZ+Z squared=k+z0+z1. This equals the frozen H(R,Z) by symmetry and bilinearity on the identical divisors, without changing the morphism. Under Rprime=mu*R+cE and Zprime=mu*Z+dE the universal intersection-matrix update yields -c squared+cd-d squared+(1+epsilon)c+(1-2epsilon)d. With a=c-1 and b=d-(1-epsilon), this is 1-(a squared+b squared-ab). Twice the quadratic form is a squared+b squared+(a-b) squared. Therefore all real, and hence all integral, coefficients are covered; equality is exactly c=1,d=1-epsilon. Summing from the Hopf surface forces z0=z1=0 and equality at every blowup.',
        'Original items six and seven prove the stronger all-exceptional positive-Z induction and are retained. Intermediate Z divisors are effective pushforwards of the final Z. A regular center adds one to a nonnegative multiplicity. Every saddle lies on a previously created exceptional curve, by the explicit chart induction beginning with a nonsingular foliation. At a saddle that positive existing coefficient contributes to the pulled-back multiplicity, and relative order d=0 still leaves the new coefficient positive. A noncontracted invariant curve has generically nonzero tangent derivative in characteristic zero, which would give zero Z coefficient. Thus every created exceptional curve is contracted by the covered ambient map and, using finiteness of nu, by sigma composed with q.',
        'Every downstairs exceptional curve is covered by such an upstairs curve, so the actual minimal resolution sigma contracts it. The last blowup exceptional curve is a smooth rational curve of square -1. Its contraction by sigma would let sigma descend continuously through the known last blowdown; local coordinate functions extend through the smooth blowdown point by Hartogs, giving a smaller proper resolution. Thus the original k is zero. The completed YI negative-definiteness input then excludes every further exceptional configuration on the minimal Hopf surface, whose curve self-intersections vanish. A proper quasi-finite birational map to normal N is finite and an isomorphism by integral closure. WW therefore applies to the resulting smooth minimal Hopf normalization and gives Euler number zero and its elliptic conductor description.',
        'The frozen route instead uses only a noncontracted last curve: its Z coefficient zero implies relative d=-multiplicity<=0, excluding the regular equality d=1. Saddle equality d=0 makes Z disjoint from the last exceptional curve, leaving its two saddle zeros; the local Ext calculation gives z0>=2, contradicting equality. A principal-divisor intersection then excludes a remaining Hopf contraction. This complete independent ending remains in check evidence. The stronger original induction was checked after release and is not substituted or backdated into that derivation.',
        'The first new program uses a universal symmetric intersection matrix and its rank-one blowup update, together with actual inverse chart Jacobians, to recompute the Chern expansion, complete quadratic equality forms and both saddle fields. The postrelease program computes the universal nonnegative slack-variable recurrences 1+w and 1+u+w for the retained induction and the covered blowup count. Their exact finite-length, saturation, foliation and mapping premises are proved in the derivation/comparison and are not inferred from the symbolic programs. Both outputs pass their stated assertions; no separate computation event is added.',
        'All nine original mathematical displays and their three printed equation tags remain byte-identical after deleting only the three new semantic labels. All eight original proof steps remain. The twenty-eight guards name the exact maps, resolve standing hypotheses and supporting references, make the effective-divisor and minimality premises explicit, and remove production prose. The separate immutable metadata clarification corrects only the descriptive new_map string from T to Tprime; the actual proposed map and guards already had Tprime. There is no mathematical error, proof replacement, or statement refutation.'
    ],
    chronology='Agent freeze 07:51:49.776093 UTC precedes release 07:53:23.967417 UTC. WW/Hopf supporting-proof exposure is explicit. The retained stronger induction, YI supporting-proof inspection and second program belong to the postrelease comparison. Root read the complete frozen derivation before the original. The two events share one evidence group and add one independently completed required owner.',
    original_proof_items_preserved=8,
    original_mathematical_displays_preserved=9,
    mathematical_errors_found=[],
    publication_page_reading_credit=0,
    evidence=[bind(ap), a['comparison'], a['program_scope'], a['display_preservation'], a['input_receipt'], a['postrelease_comparison_receipt'], a['frozen_derivation'], bind(clarification)] + a['primary_sources'],
)
(R / review).write_text(json.dumps(rd, indent=2) + '\n')
with (R.parent / 'S6_SERIES_GRIND_tags.tsv').open() as f:
    pages = {x['tag']: x['page'] for x in csv.DictReader(f, delimiter='\t')}
target = dict(owner=at['statement_owner'], tag=at['tag'], old_page=pages[at['tag']], original=at['full_original_block'], proposed=at['proposed_full_block'], freeze=at['freeze_receipt'], release=at['release_receipt'], events=a['event_proposals'], guards=guards, who=rd['checker'], scope='Complete Hopf-minimal-model normalization and Euler-zero theorem with the exact smooth covering maps and all original Chern/blowup and exceptional-order steps.', event_note='Root complete frozen/original/final eight-item comparison at ' + now + '. All nine original mathematical displays remain. The stronger original positive-order induction was checked after release and retained. No mathematical correction or proof substitution; no extra root evidence group or final-page credit.')
s = (R / 'S6_SERIES_PUBLISH_II.tex').read_text()
start = s.index('\\section*{Programs}')
end = s.index('\\end{longtable}', start)
last = s[s.rfind('\n', start, end - 1) + 1:end]
assert last.strip()
rows = (R / a['program_rows']['path']).read_text()
extra = [dict(old=last, new=last + rows, type='D09,D18', owner='Programs', location='Programs', reason='Cite both bounded new programs once for the printed Chern/blowup identities and positive exceptional-order recurrence.')]
scope = read(a['program_scope']['path'])
copies = [dict(**{'from': x['output']}, to='code/' + Path(x['output']['path']).name) for x in scope['new_computations']]
cfg = dict(batch=67, root_review_complete=True, source_before_sha256=bind('S6_SERIES_PUBLISH_II.tex')['sha256'], ledger_before_sha256=bind('CHECK_EVENTS.tsv')['sha256'], review_evidence=[bind(review)] + rd['evidence'] + [a['proposal'], a['derivation']], targets=[target], additional_source_edits=extra, code_copies=copies, mathematical_repairs=[], scope='02X9 admitted after complete independent derivation and full original/final eight-item comparison. All nine original mathematical displays remain, with three semantic labels added. The stronger original positive-Z induction is retained after a separate complete comparison; twenty-eight target guards and two bounded Programs rows; two events in one group. No mathematical change, global defect closure or page-reading credit.')
assert cfg['source_before_sha256'] == '853ba0a84db88b8dc5f27490e8c77ded6a3a143a0a3e48a31ecf88cfde87e5e0'
assert cfg['ledger_before_sha256'] == '1ac989a33c257f453a4e2ecb746776d3f927b54db31bc422ee8681d6eac0cff8'
out = 'records/S6_SERIES_PUBLISH_II_continuation2_batch67_config.json'
assert not (R / out).exists()
(R / out).write_text(json.dumps(cfg, indent=2) + '\n')
print(json.dumps(bind(out)))
