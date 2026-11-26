#!/usr/bin/env python3
"""Stage LF's complete comparison, three exact guards and typed check records.

Canonical and frozen mathematical files remain read-only. The third
guard removes the fully compared following historical paragraph. One
numerical-source defect has an exact pinned external source location.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import csv
import json
import re

ROOT = Path(__file__).resolve().parent.parent
STAGE = ROOT / 'agents/continuation7_iii_three_primary_receiving'
OLD = ROOT / 'agents/continuation7_iii_three_primary'
P = 'S6_SERIES_PUBLISH_III_02LF'
ID = 'maps:src:D.2.39'
NOW = datetime.now(timezone.utc).isoformat()
FRESH = '2026-11-25T06:01:00+00:00'
PEER = '2026-11-25T06:25:22+00:00'
RELEASE = '2026-11-25T06:20:11.780324+00:00'
WHO = ('GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical reasoning '
       'effort not separately exposed; continuation seven LF receiving check')


def digest(x):
    return sha256(x if isinstance(x, bytes) else x.encode()).hexdigest()


def env(x, name):
    a = x.index('\\begin{' + name + '}')
    b = x.index('\\end{' + name + '}', a) + len('\\end{' + name + '}')
    return x[a:b]


def part(x, start, end):
    a = x.index(start)
    return x[a:x.index(end, a) + len(end)]


def display(x, tag):
    k = x.index('\\tag{' + tag + '}')
    a = x.rfind(r'\[', 0, k)
    b = x.index(r'\]', k) + 2
    return x[a:b]


def tsv(name, fields, rows):
    with (STAGE / name).open('x', encoding='utf8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter='\t',
                           lineterminator='\n')
        w.writeheader()
        w.writerows(rows)


canonical_path = ROOT / 'S6_SERIES_PUBLISH_III.tex'
canonical_bytes = canonical_path.read_bytes()
assert digest(canonical_bytes) == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
canonical = canonical_bytes.decode()
os = env((OLD / f'{P}_released_statement.tex').read_text(), 'theorem')
op = env((OLD / f'{P}_released_proof.tex').read_text(), 'proof')
assert digest(op) == '3ac0e5f177c3f6294f54113729f679e2068e051108c50cdc0c11b5c154f24ba3'
assert len(os.splitlines()) == 42 and len(op.splitlines()) == 198
assert len(re.findall(r'^\\item\b', op, re.M)) == 12
oa = '\n'.join(canonical.splitlines()[16747:16764])
assert len(oa.split('\n')) == 17
assert 'The program' in oa and 'finite mod-three test.' in oa
receiver = STAGE / f'{P}_receiving.tex'
new = receiver.read_text()
assert digest(new) == '92aea92d7f4a4eeb256896f4b4cdabcba167bb0284801054c9fc352057bd9fb3'
assert len(new.splitlines()) == 796
ns, np = env(new, 'theorem'), env(new, 'proof')
assert new.count(r'\begin{proof}') == new.count(r'\end{proof}') == 1
comparison = (STAGE / f'{P}_comparison.md').read_text()
table = comparison.split('## 3. Every original proof item', 1)[1].split(
    '## 4. All following historical and numerical auxiliaries', 1)[0]
assert re.findall(r'^\| (\d+) \|', table, re.M) == list(map(str, range(1, 13)))
assert 'three narrowly scoped' in comparison and 'No new D26' in comparison
assert 'No historical algorithm was run' in comparison
assert 'V003' in comparison and 'V004' in comparison

guards = []
for kind, before, after, expected in [
    ('statement', os, ns, (16506, 16547)),
    ('proof', op, np, (16550, 16747)),
    ('following_auxiliary', oa, '', (16748, 16764)),
]:
    assert canonical.count(before) == 1, kind
    position = canonical.index(before)
    start = canonical[:position].count('\n') + 1
    end = start + before.count('\n')
    assert (start, end) == expected, (kind, start, end)
    guards.append((kind, before, after, start, end, position))
segments = []
last = 0
delta = 0
inverse = []
for kind, before, after, start, end, position in guards:
    assert position >= last
    segments.extend((canonical[last:position], after))
    inverse.append((position + delta, after, before))
    delta += len(after) - len(before)
    last = position + len(before)
segments.append(canonical[last:])
shadow = ''.join(segments)
for position, after, before in reversed(inverse):
    assert shadow[position:position+len(after)] == after
    shadow = shadow[:position] + before + shadow[position+len(after):]
assert shadow.encode() == canonical_bytes

old = os + '\n\n' + op
for command, count in [('label', 10), ('hypertarget', 10), ('tag', 9)]:
    pattern = r'\\' + command + r'\{([^}]+)\}'
    a, b = re.findall(pattern, old), re.findall(pattern, new)
    assert len(a) == len(b) == len(set(b)) == count
    assert sorted(a) == sorted(b), command
triples = r'\\tag\{([^}]+)\}\s*\\hypertarget\{([^}]+)\}\{\}\s*\\label\{([^}]+)\}'
assert sorted(re.findall(triples, old)) == sorted(re.findall(triples, new))
assert len(re.findall(triples, new)) == 9
assert r'\textnormal{\small tag 02LF.}' in ns
stack = []
for side, name in re.findall(r'\\(begin|end)\{([^}]+)\}', new):
    if side == 'begin':
        stack.append(name)
    else:
        assert stack and stack.pop() == name, (side, name)
assert not stack
depth = 0
for i, ch in enumerate(new):
    if ch not in '{}':
        continue
    j = i - 1
    while j >= 0 and new[j] == '\\':
        j -= 1
    if (i-j-1) % 2:
        continue
    depth += 1 if ch == '{' else -1
    assert depth >= 0
assert depth == 0
math = []
for token in re.findall(r'\\[()\[\]]', new):
    if token in (r'\(', r'\['):
        math.append(token)
    else:
        assert math and math.pop() == {r'\)': r'\(', r'\]': r'\['}[token]
assert not math and len(re.findall(r'(?<!\\)\$', new)) % 2 == 0
assert not re.search(r'(?<![A-Za-z\\])(?:qquad|quad)\b', new)
assert not any(ord(c) < 32 and c not in '\n\t' for c in new)
refs = set(re.findall(r'\\(?:eqref|ref|SeriesRef)\{([^}]+)\}', new))
assert refs <= set(re.findall(r'\\label\{([^}]+)\}', canonical))
bib = (ROOT / 'S6_SERIES_PUBLISH_references.bib').read_text()
bib += (STAGE / f'{P}_staged_bibliography.bib').read_text()
keys = set(re.findall(r'@\w+\s*\{\s*([^,\s]+)', bib))
cites = {k.strip() for group in re.findall(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}', new)
         for k in group.split(',')}
assert cites == {'manZhubr75', 'manCartan1955EML', 'ffThomas56', 'ffThomas1959Suspension'}
assert cites <= keys
for bad in (r'\StatementRecord', r'\path{', 'code/', 'records/', '.json', 'SHA256'):
    assert bad not in new, bad
frozen = {
    OLD / f'{P}_fresh_derivation.md':
        'a882ffccd0d1daf7fa6c50f7e67924bec72e12bc1c60ec7acc9c9c9f246b5bb2',
    STAGE / f'{P}_bounded_peer_review.md':
        'b17925d873b06a221dab8c69540bab9e43961bf8d78a65126d3a5244a5c40de0',
    STAGE / f'{P}_auxiliary_maps_v001.json':
        '77972e2fd3fda0f18891c22d76cc9fd0d8a68e60e9436618cf393d92ed4edf5f',
}
for filename, expected in frozen.items():
    assert digest(filename.read_bytes()) == expected, filename

defects = []


def defect(kind, suffix, before, after, reason):
    matches = [(block, start, end) for _, block, _, start, end, _ in guards
               if before in block]
    assert len(matches) == 1, (suffix, 'old guarded block', before[:70])
    assert not after or after in new, (suffix, 'new text', after[:70])
    block, start, end = matches[0]
    line = start + block[:block.index(before)].count('\n')
    assert start <= line <= end
    defects.append(dict(change_id=f'c7-III-02LF-{suffix}', type=kind,
        statement_id=ID, old_location=f'S6_SERIES_PUBLISH_III.tex:{line}',
        old_page='', new_location=str(receiver.relative_to(ROOT)),
        new_page='pending final typeset page concordance', old_text=before,
        new_text=after, reason=reason,
        review_status='staged; root admission, source application and final page review pending'))


defect('D22', 'integral-group-and-cap-maps',
    part(op, r'\ref{maps:src:D.2.26} gives', 'Let\n$u\\in H^2(X;\\mathbb F_3)$ be the generator normalized below.'),
    'H_2(X;\\mathbb Z)=\\mathbb Z/3\\langle s\\rangle.',
    'Retain the groups with the explicit primitive wedge quotient and inverse, complete graph section, every integral cap section and all finite normal columns. The original group claim is true; this is a justification and map completion, not a refutation.')
defect('D22', 'original-gamma-two-cap',
    'its original additive coefficients are zero, and the\nordinary clutch coefficient is $be$.',
    'At original $III$ the\nsecond vector is $(-3,9,0,2)$.',
    'Prove the zero original-additive coefficients by the actual line-frame and roof maps, the primitive fibre section and the gamma-two fixed lift at original III. Finite III has gamma-one lift; the receiver does not identify them without their respective cap maps.')
defect('D22', 'all-finite-affine-maps',
    part(op, 'This includes the\nfinite logarithmic caps:', 'for every allowed order.'),
    'v=n\\ell+r\\delta,\\qquad m=dk,\\quad k\\in\\mathbb Z_{>0},\\quad r\\in\\mathbb Z,',
    'Supply the full Seifert determinant, all integer parameters, finite root boundary map and inverse, Bezout normal lattice and holomorphic disc conjugacy for every affine lift with the same integral power. Integral chi and gcd(m,n)=1 prove scalar freeness. No finite range is substituted for the quantified parameters.')
defect('D22', 'global-line-period-gauge',
    part(op, 'The doubled factors', 'produce the corresponding line on $W$.'),
    'G_0=\\exp\\{-2\\pi i(U^tD_0W+W^tD_0\\Omega_{\\rm ph}W)\\}',
    'Give the common period cocycle, connection, finite lift, reciprocal Gaussian gauges, monomial gauge and every retained holomorphic unit. The complete normal and graph maps prove its global cycle values. The true polynomial identities are transported to the literal prescribed fan.')
defect('D25', 'false-whole-circle-fixing',
    'the rational curve $C$ fixed by the whole circle,',
    'It fixes $C_0$ pointwise for $k=0$ and rotates it with tangent weight\n$-k$ for $k\\ne0$.',
    'The first allowed II row has k=-3 and chart weights(-5,2,3),(-2,5,-3), so C rotates with tangent weight3. Six marked rows have nonzero k. The corrected actual map preserves C3 fixing and all final conclusions; it refutes only the asserted whole-circle pointwise fixing.')
defect('D20,D22', 'tate-period-coordinate-map',
    part(op, 'The seven exact Tate markings', '$w,-w$, where $w=(aj)^{-1}=\\pm1$ in $\\mathbb F_3$.'),
    '\\delta=-\\sigma l+n_0p_0.',
    'The complete27-site comparison is H_old=H_new diag(epsilon,epsilon,1,1), with the same inverse, and r_old=-epsilon kappa. Primitive coordinate j changes by tau; its support differs by the recorded integral linear monomial gauge. The old normal weight is -epsilon sigma, giving the exact same unordered pair. These sign conventions are proved, not silently normalized.')
defect('D22', 'common-borel-character',
    part(op, 'The group-cohomology difference', 'including arbitrary finite twists.'),
    'Every finite isotropy section\nhas generator $(1,\\zeta_3)$, since its first component lies in a\ntorsion-free group.',
    'Prove the based product fundamental group, ordinary degree-two restriction, common base coefficient and mixed kernel terms. Subtract one whole-circle base class with its inverse. The complete finite normal columns and original gamma-two cap are retained in that comparison.')
defect('D25', 'false-ordinary-curve-pullback',
    'There is also no contribution on $C_{S^1}$: \\eqref{maps:eq:D.T34} is pulled back\nfrom the two-dimensional curve, whose degree-six cohomology is zero.',
    'Q_3(U)|_{(C_0)_{S^1}}=\\rho_9(A^3z^3)\n                         =\\rho_9(A^3k^2T^2z).',
    'For nonzero k, a map to the ordinary sphere with nonzero ordinary degree j would pull its integral generator to jz+hT in Z[T,z]/(z(z-kT)); square zero forces h=0 and j=0. The actual class has integral lift Az, and 9 divides k^2, so its full Z9 operation still vanishes. The false reason and true conclusion are distinguished.')
defect('D18,D22', 'coefficient-one-primary-operation',
    part(op, "Its value on the reduced hyperplane class", 'detects its entire\ngenerator, and hence the whole fundamental-class invariant.'),
    'Q_3(\\rho_3x)=\\rho_9(x^3).',
    'Retain full order-nine detection and specify the positive coefficient-one map with its inverse. Cartan gives H5=0 and the divided generator; Thomas267-268 gives the augmentation-one cochain carrier. The original CP1 times CP2 upper bound is proved separately in the auxiliary note; it is not treated as a spin-bordism representative.')
defect('D18', 'proved-odd-suspension-locus',
    '\\cite[equations (2.3), (2.5), (2.7), p.267]{ffThomas56}.',
    '\\cite[Theorem~I(ii), pp.~897--898; (3.1), p.~900; \\S5, pp.~904--905]{ffThomas1959Suspension}.',
    'Retain the correct odd-index operation and add the detailed proved suspension source. The receiver gives the signed smash quotient, left interval convention and inverse slant map. The cited1959 pages were actually visually read; no whole-paper reading is claimed.')
defect('D14', 'one-localization-proof-and-tags',
    display(op, 'D.T37') + '\n' + 'The dimension bound can be read from an orbifold triangulation,',
    display(np, 'D.T37'),
    'Use one coherent C9 excision/Thom proof, retaining D.T37 and D.T38 with their exact C9 maps. The complete original stronger S1 relative comparison and degree-six injection are proved in the auxiliary check, and are not classified as false. The independent ordinary-p1 check stays in that check file.')
defect('D22', 'marked-bordism-and-recognition',
    part(op, "Thus the resulting model has zero spin-bordism class", 'both have $b_3=0$.'),
    part(np, "Zhubr's marked recognition theorem", 'positive surgery generator to $s$.'),
    'Give both trace multiplication-by3 maps, the marked null-bordism and exact refined coefficient P(j zeta)=j mod3. Use Theorem5 injectivity and Theorem3 with Section4.1 zero-free-H3 construction/uniqueness. The literal H2 wording on793-794 is recorded accurately. No model or classification conclusion is refuted.')
defect('D01,D09,D13', 'following-historical-paragraph',
    oa, '',
    'Move the complete following program/execution paragraph to the comparison and source checks. Both historical sources and complete JSONs were retrieved and read at the pinned revision, but neither stdout was found and no historical algorithm was rerun. All counts, finite factors, period identities and numerical wall assertions were settled. The record does not invent a past execution date or exit code.')
defect('D10', 'machine-header',
    next(line for line in os.splitlines() if line.startswith(r'\StatementRecord')),
    r'\textnormal{\small tag 02LF.}',
    'Replace machine navigation with the small printed tag; preserve the theorem target and label. Mathematical dependencies and primary citations occur at their actual steps.')
defect('D02', 'defensive-comparison-clause',
    'The familiar nonvanishing phenomena for the Pontryagin square of\nsuspended classes are irrelevant here; the cited formulas explicitly\nassume an odd prime.',
    'The odd-prime proof uses the relative external-product\nidentity and the vanishing on the dimension-one factor.',
    'State the proved odd-index hypothesis and operation map positively. The full coefficient scope and suspension proof remain explicit.')

historical = Path('/tmp/S6_SERIES_PUBLISH_c7_LF_historical/S6_SERIES_PUBLISH_fourfolds_D2_c3_AH.py')
hb = historical.read_bytes()
assert digest(hb) == 'c349dd8943a94a36f2974dc75a9564ffafdcd34f9929b7621757e7cea3c5d3c6'
ht = hb.decode()
false_numeric = part(ht, '                value=lambda xx,yy:',
                         '                            doubled_curve_degree=int(degree),alpha_mod_p=alpha)')
line = ht[:ht.index(false_numeric)].count('\n') + 1
assert line == 106
defects.append(dict(change_id='c7-III-02LF-untransported-wall-numerical-auxiliary',
    type='D25', statement_id=ID,
    old_location='KokunoYumeto/s6-complex-structure-workbench@a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7:pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/S6_10_PAPERS/code/III/fourfolds_D2_c3_AH.py:106-114',
    old_page='', new_location=str((STAGE / f'{P}_post_exposure_auxiliaries.md').relative_to(ROOT)),
    new_page='not a printed-page change', old_text=false_numeric,
    new_text='F=R_epsilon C=P_old R_epsilon; F^{-1}=R_epsilon P_old^{-1}; deg(D|C0)=2a(nu-b kappa).',
    reason='The physical polynomial is evaluated on an untransported unit wall and then labelled as the prescribed curve degree. The explicit fan map, inverse and reciprocal frame sign give the seven corrections100->50,86->58,230->70,520->80,100->50,-20->20,520->80. Polynomial identities at the old arguments remain true. This is one numerical auxiliary occurrence cited by the following canonical paragraph, not a claim that the main cubic or smooth type is false. No historical source is edited.',
    review_status='staged; root admission and numerical-auxiliary occurrence review pending'))
assert len(defects) == 16
assert sum('D25' in d['type'] for d in defects) == 3
assert not any('D26' in d['type'] or 'D27' in d['type'] for d in defects)

events = []
event_name = f'{P}_CHECK_EVENTS.tsv'


def event(kind, suffix, phase, source, group, outcome, when=NOW):
    events.append(dict(statement_id=ID, date=when[:10], who=WHO, type=kind,
        outcome=outcome, event_id=f'publish:c7:III:02LF:{suffix}', phase=phase,
        source_file=source, source_row='1', source_event_type=kind,
        evidence_group=f'publish:c7:III:02LF:{group}',
        publish_input_file=str((STAGE / event_name).relative_to(ROOT)),
        publish_input_row=str(len(events)+2), date_utc=when,
        where=str((STAGE / f'{P}_comparison.md').relative_to(ROOT))))


event('targeted proof check', 'attributed-fresh-complete', 'before original exposure',
    str((OLD / f'{P}_fresh_derivation.md').relative_to(ROOT)), 'author-fresh',
    'The frozen1408-line fresh proof supplies every one of the eight patterns, all finite multiplicities and affine lifts, actual gamma-two original III, integral cap/graph inverses, unit-preserving line gauges, actual rotating prescribed-fan curve, global Borel class, full C9 detector and marked degree-three model. Root read all fresh source/streams and accepted its exact scope. This receiving checker read the whole proof/input/execution notes before peer freeze but does not claim authorship or an independent rerun of the three fresh programs.', FRESH)
event('used and rechecked in this run', 'bounded-fresh-only-peer', 'before this checker original exposure',
    str((STAGE / f'{P}_bounded_peer_review.md').relative_to(ROOT)), 'bounded-peer',
    'Read the complete fresh proof and both notes with original/history closed until this peer freeze, despite the earlier root release. Independently checked whole-circle class existence, common finite character, actual invariant-neighbourhood C9 Thom inverse, rotating-curve contribution, elliptic mixed suspension and coefficient-one detector. This is a bounded peer review, not another fresh derivation or fresh-program review.', PEER)
event('used and rechecked in this run', 'bounded-primary-readings', 'primary consultations before and after original exposure',
    str((STAGE / f'{P}_source_checks.md').relative_to(ROOT)), 'primary-scope',
    'Visually read Thomas1959 printed897,898,900-905 and Thomas1956 printed267-268 at the exact recorded PDF hashes and individual images. Read1959 end-page911 and journal contents as text for metadata. Use disclosed Cartan and corrected K9 primary inputs with their exact attributed reading scopes; preserve literal H2 printing and Section4.1 zero-free-H3 scope. Failed publisher web opens and the uncredited truncated image response are recorded. Clean bibliography records are staged separately.')
event('used and rechecked in this run', 'historical-source-retrieval-only', 'after original exposure',
    'code/S6_SERIES_PUBLISH_c7_lf_historical_retrieve_v001.py; code/S6_SERIES_PUBLISH_c7_lf_tate_retrieve_v001.py',
    'historical-comparison',
    'Two read-only retrievals obtained both exact pinned historical programs and both full JSONs; every line/field was read. Both cited stdout names were404 at tested locations, and the AH JSON was found in code/III after records404. Neither historical algorithm was executed. Source contents and archived counts are verified, without attesting an unavailable historical exit status/date.')
event('computation or formal certificate', 'post-exposure-period-and-fan-maps',
    'after original exposure', 'code/S6_SERIES_PUBLISH_c7_lf_auxiliary_maps_v001.py',
    'post-exposure-maps',
    'The only new post-exposure mathematical execution succeeded on its first run. Read the entire source, all36 combined output lines and every JSON field: all27 period maps/inverses, primitive-period signs and linear gauge differences, all seven prescribed-fan maps/inverses, actual wall degrees and full Z9 cusp values. Historical programs were not imported or rerun. The written auxiliary proof supplies all-parameter geometric scope.')
event('refuted', 'three-false-intermediate-occurrences', 'after complete original comparison',
    str((STAGE / f'{P}_post_exposure_auxiliaries.md').relative_to(ROOT)),
    'post-exposure-refutation',
    'Refute exactly three intermediate occurrences: whole-circle pointwise fixing of C (explicit tangent weight3 counterexample); ordinary-sphere pullback of its normalized Borel class for nonzero k (integral ring square obstruction); and the historical untransported wall degree identification (seven exact corrected values under F=R_epsilon C and reciprocal frame). The theorem, full cubic mu=0, smooth model, genus-one elliptic core, original stronger S1 relative comparison and injection all remain true. No D26 or D27 refutation is claimed.')
event('used and rechecked in this run', 'complete-original-auxiliaries', 'after original exposure',
    str((STAGE / f'{P}_post_exposure_auxiliaries.md').relative_to(ROOT)),
    'complete-original-comparison',
    'Settle every auxiliary in the42-line statement, all12 proof items and17 following lines: CP1xCP2 ordinary upper bound, exact spin quotient/P map, both original caps, all finite affine lifts, all archived local checks, stronger S1 vanishing/injection, ordinary p1 localization and the complete marked surgery model. Independent alternative proofs remain in the check file; one C9 proof appears in the receiver.')
event('targeted proof check', 'targeted', 'after complete original comparison',
    str((STAGE / f'{P}_comparison.md').relative_to(ROOT)), 'complete-original-comparison',
    f'After individual release{RELEASE} and peer freeze, read the complete original and all auxiliaries, then all796 final receiving lines. Preserve10labels,10targets and9 exact tag triples in one same-conclusion proof. Three separate guarded replacements, full roundtrip identity, finite parameter scope, all references and staged primary keys pass. Four successful assembly versions/streams and one notes-only context failure are retained; the unsaved pre-execution inline cleanup source is accurately qualified. No canonical mutation, TeX build, page review or global admission is claimed.')

tsv(f'{P}_replacements.tsv', ['statement_id', 'old_text', 'new_text'],
    [dict(statement_id=ID, old_text=b, new_text=a) for _, b, a, _, _, _ in guards])
tsv(f'{P}_guards.tsv', ['statement_id', 'kind', 'start_line', 'end_line', 'old_sha256', 'new_sha256'],
    [dict(statement_id=ID, kind=k, start_line=s, end_line=e,
          old_sha256=digest(b), new_sha256=digest(a)) for k, b, a, s, e, _ in guards])
tsv(f'{P}_defects.tsv', ['change_id', 'type', 'statement_id', 'old_location',
    'old_page', 'new_location', 'new_page', 'old_text', 'new_text', 'reason', 'review_status'], defects)
tsv(event_name, ['statement_id', 'date', 'who', 'type', 'outcome', 'event_id',
    'phase', 'source_file', 'source_row', 'source_event_type', 'evidence_group',
    'publish_input_file', 'publish_input_row', 'date_utc', 'where'], events)
assert canonical_path.read_bytes() == canonical_bytes
print('STAGED_AT', NOW)
print('GUARDS', len(guards), 'DEFECTS', len(defects), 'EVENTS', len(events))
print('IDENTITIES', '10labels 10targets 9triples; exact forward/inverse replacements')
for kind, before, after, start, end, _ in guards:
    print('GUARD', kind, start, end, digest(before), digest(after))
for d in defects:
    print('DEFECT', d['change_id'], d['type'], d['old_location'])
for e in events:
    print('EVENT', e['event_id'], e['type'])
files = sorted(STAGE.glob(f'{P}_*'))
manifest = dict(staged_at=NOW, statement_id=ID, canonical_sha256=digest(canonical_bytes),
    receiver_sha256=digest(new), original_release=RELEASE,
    records=dict(guards=len(guards), defects=len(defects), events=len(events)),
    files={str(p.relative_to(ROOT)):dict(sha256=digest(p.read_bytes()),bytes=p.stat().st_size)
           for p in files if p.is_file() and p.suffix in {'.md','.tex','.bib','.tsv','.json'}})
manifest_path = STAGE / f'{P}_packet_manifest_v001.json'
assert not manifest_path.exists()
manifest_path.write_text(json.dumps(manifest, indent=2)+'\n')
for path in files + [manifest_path]:
    print('FILE', path.relative_to(ROOT), 'SHA256', digest(path.read_bytes()))
print('CANONICAL_AND_FROZEN_BYTES_UNCHANGED; NO_BUILD_OR_PAGE_REVIEW_CLAIM')
