#!/usr/bin/env python3
"""Stage LL's records; v01's failed broad table check is retained.

The item-count check is restricted to the six-item comparison table.
Version01 failed before any record write. Canonical remains read-only.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import csv
import re

ROOT = Path(__file__).resolve().parent.parent
STAGE = ROOT / 'agents/continuation7_iii_residual_two_primary'
P = 'S6_SERIES_PUBLISH_III_02LL'
ID = 'maps:src:D.2.44'
NOW = datetime.now(timezone.utc).isoformat()
FRESH = '2026-11-25T03:43:08.512269+00:00'
RELEASE = '2026-11-25T03:46:56.073712+00:00'
WHO = ('GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical reasoning effort '
       'not separately exposed; seventh-continuation residual two-primary check')


def digest(x):
    return sha256(x if isinstance(x, bytes) else x.encode()).hexdigest()


def env(x, name):
    left = x.index('\\begin{' + name + '}')
    right = x.index('\\end{' + name + '}', left) + len('\\end{' + name + '}')
    return x[left:right]


def part(x, start, end):
    a = x.index(start)
    return x[a:x.index(end, a) + len(end)]


def display(x, tag):
    k = x.index('\\tag{' + tag + '}')
    a = x.rfind(r'\[', 0, k)
    b = x.index(r'\]', k) + 2
    return x[a:b]


def tsv(name, fields, rows):
    with (STAGE / name).open('w', encoding='utf8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter='\t', lineterminator='\n')
        w.writeheader()
        w.writerows(rows)


canonical_path = ROOT / 'S6_SERIES_PUBLISH_III.tex'
canonical_bytes = canonical_path.read_bytes()
assert digest(canonical_bytes) == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
canonical = canonical_bytes.decode()
os = env((STAGE / f'{P}_released_statement.tex').read_text(), 'theorem')
op = env((STAGE / f'{P}_released_proof.tex').read_text(), 'proof')
assert digest(op) == '86ae31a580fc45af23ec83425162e2876342ed3662731b0440490060ed57a725'
assert len(op.splitlines()) == 411
receiver = STAGE / f'{P}_receiving.tex'
new = receiver.read_text()
assert digest(new) == 'ce1272e21501270546e5987963dba21ebbc8e720e75b56fa12a00efa473e4d58'
ns, np = env(new, 'theorem'), env(new, 'proof')
old = os + '\n\n' + op
comparison = (STAGE / f'{P}_comparison.md').read_text()
item_table = comparison.split('## 2. Every original proof item and auxiliary', 1)[1].split('## 3.', 1)[0]
assert re.findall(r'^\| (\d+) \|', item_table, re.M) == list(map(str, range(1, 7)))
assert 'zero-based' in comparison and 'numbered from zero' in ns

guards = []
shadow = canonical
for kind, before, after in [('statement', os, ns), ('proof', op, np)]:
    assert canonical.count(before) == 1
    position = canonical.index(before)
    start = canonical[:position].count('\n') + 1
    end = start + before.count('\n')
    if kind == 'proof':
        assert (start, end) == (17908, 18318)
    guards.append((kind, before, after, start, end))
    shadow = shadow.replace(before, after, 1)
for _, before, after, _, _ in reversed(guards):
    assert shadow.count(after) == 1
    shadow = shadow.replace(after, before, 1)
assert shadow.encode() == canonical_bytes

for command, count in [('label', 17), ('hypertarget', 17), ('tag', 16)]:
    pattern = r'\\' + command + r'\{([^}]+)\}'
    a, b = re.findall(pattern, old), re.findall(pattern, new)
    assert len(a) == len(b) == count and len(set(b)) == count
    assert sorted(a) == sorted(b), command
triples = r'\\tag\{([^}]+)\}\s*\\hypertarget\{([^}]+)\}\{\}\s*\\label\{([^}]+)\}'
assert sorted(re.findall(triples, old)) == sorted(re.findall(triples, new))
assert len(re.findall(triples, new)) == 16

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
    if (i - j - 1) % 2:
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
cites = {k.strip() for g in re.findall(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}', new)
         for k in g.split(',')}
assert cites == {'manZhubr75', 'manZhubr2010Gamma', 'AtiyahSinger1968IIIE',
                 'ffBrown72', 'ffZhubr13', 'mapsKaplan79'}
assert cites <= keys
for bad in (r'\StatementRecord', 'code/', 'records/', '.json', 'SHA256',
            'fresh', 'historical', 'corrected', 'both0', 'zero2'):
    assert bad not in new, bad

frozen = {
    f'agents/continuation7_iii_residual_two_primary/{P}_fresh_derivation.md':
        'a003274556cb03eb646f68271c5e80c7c456b193e589b1d5c3f649cbd1877362',
    f'agents/continuation7_iii_residual_two_primary/{P}_characteristic_trace_and_index.md':
        '79525994f8ad16aa6c0dd6dc9ae7f64fc954d862cefc9cb041503490ba89306a',
    'code/S6_SERIES_PUBLISH_c7_ll_spin_localization.py':
        'e611699fb572d05ad1e3adcba3c265440fa4fb8ec0a86a4420d4ae0de3974459',
    'code/S6_SERIES_PUBLISH_c7_ll_spin_localization.out':
        '10b6592d108957ae31c9845fa48f8ed599dda81cd0bd8a3cecc7a9bdeb20f709',
    f'agents/continuation7_iii_residual_two_primary/{P}_fresh_localization_data.json':
        'c0d7c507d1faf05366107d3fb5da98e1c54c2a0ad0ff81e11065ee3607c624cd',
    'code/S6_SERIES_PUBLISH_c7_ll_gamma_character.py':
        'eb7ff190faa745851fb98874f4855cd588c2fec8f6fc1b6db207ad22b24be23b',
    'code/S6_SERIES_PUBLISH_c7_ll_gamma_character.out':
        'afc3488815afba560c85d7913aa239826edbb916376add3db416ad5ebca417d5',
    f'agents/continuation7_iii_residual_two_primary/{P}_fresh_gamma_data.json':
        '68b98dff5483cae40c33a0dba4a3c87f340b332d665c147c1445afc3fee3a0fb'}
for filename, expected in frozen.items():
    assert digest((ROOT / filename).read_bytes()) == expected, filename

defects = []


def defect(kind, suffix, before, after, reason):
    blocks = [(block, start, end) for _, block, _, start, end in guards if before in block]
    assert len(blocks) == 1, (suffix, 'old guarded block', before[:80])
    assert not after or after in new, (suffix, 'new text', after[:80])
    block, start, end = blocks[0]
    line = start + block[:block.index(before)].count('\n')
    assert start <= line <= end
    defects.append(dict(change_id=f'c7-III-02LL-{suffix}', type=kind,
        statement_id=ID, old_location=f'S6_SERIES_PUBLISH_III.tex:{line}',
        old_page='', new_location=str(receiver.relative_to(ROOT)),
        new_page='pending final typeset page concordance', old_text=before,
        new_text=after, reason=reason,
        review_status='staged; root admission, source application and final page review pending'))


defect('D27', 'four-smooth-identifications',
    part(os, 'In particular all three OS55 manifolds', 'with the following concrete surgery models.'),
    part(ns, 'The rows with $P=0$', 'the following spin surgeries with their unique normal framings.'),
    'The prescribed fan gives P=0 for OS55 zeros2,4 and P=4 for OS45 zeros2,3. Every oriented diffeomorphism acts on Z/c by an odd unit and transports P by that unit; it fixes 0 and c/2 separately. These four old identifications are refuted. The full marked construction of both models and their complete invariants proves the refined classification at the same permanent identity, for both ordinary signs.')
defect('D25', 'four-refined-values', display(os, 'D44.1'), display(ns, 'D44.1'),
    'Record the false numerical occurrences separately from the D27 smooth locus. Both the pre-exposure characteristic trace/index and the post-exposure actual critical-cycle framing give the four changed values. All groups, lambda, mu and the other three assignments stand.')
defect('D25', 'uniform-relative-character',
    part(op, 'The symmetric auxiliary line', 'degree coprime to $c$ on $C$.'),
    part(np, r'r_C=\frac c2', r'D_C=\deg\mathcal L|_{C_0}=K_{11}-K_{12}=a(1-c\kappa).'),
    'The exact Gaussian half-phase and prescribed-fan Cartier slope give r_C=(c/2)[a*kappa*(c*kappa-1)-1], which is zero in the four affected rows. The elliptic character remains zero. A common Borel character shift changes both equally and cannot repair their difference. The exact degree is a(1-c*kappa), congruent1 modulo c.')
defect('D25', 'fixed-restriction-occurrence', display(op, 'D44.0a'), display(np, 'D44.0a'),
    'Retain the same fixed curves and normal Euler classes, but replace the uniform cusp coefficient by r_C. The elliptic degree is -1 modulo c with its possible integral-origin mixed term. Full cyclic cube and lambda remain zero; this is another occurrence of the same relative-character error.')
defect('D25', 'prescribed-cusp-fan',
    part(op, 'At the unique rank-two cusp', 'so $Nb_j=a_j$.'),
    part(np, 'The short basis of the prescribed fan', 'integer inverse.'),
    'The period change x=Cj with inverse C^{-1} identifies the two monodromy descriptions only together with transport of every triangle. The stipulated unit fan is in SC with long basis B. The old unit fan in S with long basis BC^{-1} gives different actual curve classes. The exact support pullback, duality and integral character are proved in the auxiliary note. D44.10 is retained with H=-kappa, n=nu; D44.12 is transported into the actual fan.')
defect('D25', 'critical-linking-table', display(op, 'D44.13'), display(np, 'D44.13'),
    'The exact relation inverse RQ=K0 and ordinary Thom boundary -ce*s give link=-Omega(v)/(ce). For e=1 the actual OS55 values are -18,7,-18 and OS45 values4,-3,-3,4. The opposite sign reverses every integer. All relation/choice independence and the unit-generator assertion are proved with actual chains.')
defect('D25', 'critical-example-vector', display(op, 'D44.14'), display(np, 'D44.14'),
    'At OS55 zero2 the third vector must be (5,-24,-8,0,4,-19), of Omega degree101, instead of (-19,-23,-10,0,5,6), of degree-119. Their difference has degree220, so cannot lie in the actual cap kernel. The other four vectors are retained.')
defect('D25', 'critical-example-boundary',
    'Their sum has an integral bounding relation with clutch loop\n$(0,0,37,0)$.',
    'Their $\\Omega$ values are $-20,-1,101,-4,-4$, summing to $72$,\nso their bounding ordinary loop has $\\delta$ coefficient $-18$.',
    'This is the separately printed numerical consequence of the changed critical vector. The complete outside-disc chain and ordinary normal map give -18 exactly, not merely its parity.')
defect('D22,D09', 'global-line-and-descent',
    part(op, 'The full integral support-function', 'localization steps.'),
    part(np, 'We construct one line on $W$', 'including zero swept values.'),
    'Replace the historical code assertion by the complete real lattice cocycle, preserved quadratic refinement, exact finite lift, scalar-one monodromy gluing, Gaussian gauge and inverse, actual unit-retaining period factors and regular Cartier maps. This supplies the needed geometric map rather than crediting the historical algorithm with a new run.')
defect('D22', 'complete-cusp-specialization',
    part(op, 'The latter is the degree-two class of the dual torus', 'fourth homology component is being suppressed.'),
    part(np, 'The complete integral fibre specialization', 'its fourth coordinate is zero.'),
    'Supply the actual primitive kernel and inverse four-coordinate quotient, with the Cartier lines and dual long-period torus projection. Every double curve projects to an edge, determining the fourth coordinate. No independent false-matrix allegation is made: D44.11 is retained via dual supports and the explicit first-two-column interchange.')
defect('D22', 'normal-framing-factor',
    'The homomorphism\n$\\pi_3SO(3)\\to\\pi_3SO(6)$ has image $2\\mathbb Z$.',
    part(np, 'The homomorphism\n$\\pi_3SO(3)', 'reduction modulo two.'),
    'Retain the true original auxiliary and give its exact p1 morphism: adjoint SU2 has p1=-4c2 and real rank4 generator p1=-2c2. This proves the factor two and parity quotient, rather than treating a missing calculation as a refutation.')
defect('D22', 'kernel-generation',
    'chart $f=xyz$ it has basis\n$x\\partial_x-y\\partial_y,y\\partial_y-z\\partial_z$.',
    part(np, 'For the first assertion, a relation', 'including at the critical strata.'),
    'The original fields and annihilation identity stand. Add the divisibility proof that they generate the complete analytic differential kernel at xy and xyz; no false claim about the displayed basis is asserted.')
defect('D20', 'comparison-class-symbol',
    '$a$ whose local residue on every smooth double curve is one,',
    '$\\mathfrak a$ whose local residue on every smooth double curve is one,',
    'Distinguish the degree-three comparison class from the already fixed integer a. The exact same class and pairing occur in D44.7; no normalization changes.')
defect('D09', 'historical-execution-paragraph',
    part(op, 'The executable\n', r'\path{records/fourfolds_D2_frame_certificate.json}.'),
    part(np, 'Since $K=C^t', 'generator assertion used in the framing argument.'),
    'Move all source/output paths and execution history to the comparison and later programs table. The manuscript gives the actual inputs, local specialization, explicit integer relation inverse, full table and generator maps. Historical programs and selected outputs were fully read after release but not executed; their arithmetical equalities do not establish the faulty fan input.')
defect('D10', 'machine-header',
    next(s for s in os.splitlines() if s.startswith(r'\StatementRecord')),
    r'\textnormal{\small tag 02LL.}',
    'Print only the small tag, with every permanent label, hypertarget and equation tag preserved. Dependencies and source citations occur where used.')
defect('D11', 'repeated-scope',
    'This theorem makes no assertion about\nthe remaining additive profiles or additional regular logarithms.', '',
    'The exact seven-row hypotheses, both ordinary signs and absence of additional regular logs are stated once positively. No parameter range is changed.')
defect('D14', 'complete-proof-organization',
    r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=0pt,labelsep=.5em]',
    r'\begin{enumerate}[leftmargin=*]',
    'Organize one complete proof by marked homology and global line, finite fixed data, characteristic trace/index, all retained framing auxiliaries, actual critical cycles and concrete oriented recognition. Every old item and permanent display is compared; the moved valuation display retains its tag. Whole-paper restructuring and final page concordance remain later gates.')
defect('D02', 'framing-scope-defence',
    'This is a Pontryagin--Thom argument about the specified\nnormal framing; no compression of an arbitrary framed torus to a\nsphere is being assumed.',
    'gives \\eqref{maps:eq:D44.2} for the specified normal framing.',
    'State the exact proved framing scope positively, and retain the separate explicit Kaplan ambient-surgery construction.')
defect('D02', 'classification-defence',
    'No conclusion\nhere rests on ordinary homology alone.',
    part(np, 'The marked classification in the zero-free-third-homology scope', r'\cite[Theorem 3 and Section 4.1]{manZhubr75}.'),
    'State the full marked invariants and exact zero-free-H3 classification scope positively. Both concrete models and all coefficient maps are proved.')

events = []
event_name = f'{P}_CHECK_EVENTS.tsv'


def event(kind, suffix, phase, source, group, outcome, when=NOW):
    row = len(events) + 2
    events.append(dict(statement_id=ID, date=when[:10], who=WHO, type=kind,
        outcome=outcome, event_id=f'publish:c7:III:02LL:{suffix}', phase=phase,
        source_file=source, source_row='1', source_event_type=kind,
        evidence_group=f'publish:c7:III:02LL:{group}',
        publish_input_file=str((STAGE / event_name).relative_to(ROOT)),
        publish_input_row=str(row), date_utc=when,
        where=str((STAGE / f'{P}_comparison.md').relative_to(ROOT))))


event('targeted proof check', 'fresh-complete-derivation', 'before LL original exposure',
    str((STAGE / f'{P}_fresh_derivation.md').relative_to(ROOT)), 'fresh-derivation',
    'Derived all seven prescribed-fan cases and both ordinary signs before original exposure, with the disclosed LB/LC auxiliary-line method inputs. Exact lattice factors, unit-retaining Gaussian/Cartier inverses, all finite powers, full mu and lambda, characteristic round-handle trace, composite characteristic MV correction and Gamma-to-P morphism determine the full refined P. Concrete spin surgeries and marked zero-free-H3 recognition finish the oriented classification. Both final proofs, all programs, all output and every data field were fully read by author and root before release. This is a targeted derivation, not a claim to a wholly different underlying line method.', FRESH)
event('computation or formal certificate', 'fresh-finite-symbols', 'before LL original exposure',
    'code/S6_SERIES_PUBLISH_c7_ll_spin_localization.py; code/S6_SERIES_PUBLISH_c7_ll_gamma_character.py',
    'fresh-derivation',
    'Two new programs verify the literal seven-row period/fan maps, complete fixed data, all nonidentity finite powers, full cyclic cube/lambda and exact Green inverse integral virtual characters. The outputs have18 and25 lines; both complete programs and full JSONs were read. Combined stdout/stderr successful runs returned0. These cover every fresh mathematical execution identified in the retained record; no failed mathematical run is known there, but compaction did not retain a verbatim command ledger and no stronger absence claim is made.', FRESH)
event('computation or formal certificate', 'post-exposure-critical-maps', 'after LL original exposure',
    'code/S6_SERIES_PUBLISH_c7_ll_critical_cycles_v01.py', 'post-exposure-auxiliaries',
    'The distinct post-release program derives every rank-one Bezout basis/inverse, actual cusp wall matrix and fourth coordinate, physical critical vector, Omega degree and explicit integral R-bounding coefficient, for all seven rows and both signs. It checks the support-convention map and unit torsion-generator coefficient. The complete source, successful combined stdout and complete JSON were read; no old algorithm was run.')
event("refuted, with the refined statement's id", 'four-refined-smooth-assignments',
    'after complete LL original comparison', str(receiver.relative_to(ROOT)), 'main-refinement',
    'Refined identities remain maps:src:D.2.44 and maps:eq:D44.1. OS55 zeros2,4 have P0 and model Z4,0; OS45 zeros2,3 have P4 and model Z8,1. The other three rows and all homology/lambda/mu claims stand. Every odd-unit automorphism fixes0 and c/2 separately, so naturality of P contradicts the four old smooth identifications. D27 records that theorem locus; D25 records its numerical occurrences. The full replacement and both exact model maps are proved for e=±1.')
event("refuted, with the refined statement's id", 'relative-character-auxiliary',
    'after complete LL original comparison', str((STAGE / f'{P}_post_exposure_auxiliaries.md').relative_to(ROOT)),
    'post-exposure-auxiliaries',
    'Refine the local character assertion and maps:eq:D44.0a within maps:src:D.2.44 to r_C=(c/2)[a*kappa*(c*kappa-1)-1]. The exact finite lift and prescribed-fan Cartier map give r_C0 in four rows, instead of c/2; the elliptic character is0. A common character shift cannot change the difference. Full mu=lambda0 conclusions remain proved; no generic localization theorem is refuted.')
event("refuted, with the refined statement's id", 'critical-cycle-auxiliary',
    'after complete LL original comparison', str((STAGE / f'{P}_post_exposure_auxiliaries.md').relative_to(ROOT)),
    'post-exposure-auxiliaries',
    'Refine the actual fan assertion and maps:eq:D44.12--D44.14 within the same theorem. The old S,BC^{-1} Jordan description kept an untransported unit fan; the actual cap uses SC,B. At OS55zero2 the actual vector has Omega101 versus-119, difference220 excluding a cap-kernel identification. The exact linking tables become OS55(-18,7,-18), OS45(4,-3,-3,4) for e1 and their negatives for e-1. Every fourth-coordinate, chain, relation-freedom and generator assertion is proved. The old D44.11 matrix is retained via the exact dual-support/curve-order map, not separately declared false.')
event('used and rechecked in this run', 'whole-original-and-primary-comparison',
    'after LL original exposure', str((STAGE / f'{P}_comparison.md').relative_to(ROOT)),
    'complete-original-comparison',
    f'After release{RELEASE}, read the entire statement and411 proof lines, all six outer items and nested auxiliaries, all17 identities and every historical assertion. Rechecked Brown369–372 visually, Kaplan239–240/243–246 as indexed primary text, ASIII562–567 visually and the exact Zhubr loci/attributed readings recorded in the source note. Settled full Brown parity, sphere framing, Kaplan ambient surgeries, differential-kernel generation, Bott residue, integral linking and all model claims. Read all three old scripts and every selected LL output field without executing those algorithms or opening non-LL output rows. Exact separate guards, all labels/targets/tags and frozen hashes pass. Assembly failure v01 and repair v02 are retained. Source checks only; no TeX build, canonical edit, final page review or global admission is claimed.')

tsv(f'{P}_replacements.tsv', ['statement_id', 'old_text', 'new_text'],
    [dict(statement_id=ID, old_text=b, new_text=a) for _, b, a, _, _ in guards])
tsv(f'{P}_guards.tsv', ['statement_id', 'kind', 'start_line', 'end_line', 'old_sha256', 'new_sha256'],
    [dict(statement_id=ID, kind=k, start_line=s, end_line=e, old_sha256=digest(b), new_sha256=digest(a))
     for k, b, a, s, e in guards])
tsv(f'{P}_defects.tsv', ['change_id', 'type', 'statement_id', 'old_location',
    'old_page', 'new_location', 'new_page', 'old_text', 'new_text', 'reason', 'review_status'], defects)
tsv(event_name, ['statement_id', 'date', 'who', 'type', 'outcome', 'event_id',
    'phase', 'source_file', 'source_row', 'source_event_type', 'evidence_group',
    'publish_input_file', 'publish_input_row', 'date_utc', 'where'], events)
assert canonical_path.read_bytes() == canonical_bytes
print('STAGED_AT', NOW)
for k, b, a, s, e in guards:
    print('GUARD', k, f'{s}--{e}', 'old_sha256', digest(b), 'new_sha256', digest(a))
print('IDENTITIES 17 labels; 17 hypertargets; 16 equation tags; all exact triples preserved')
print('ORIGINAL whole statement;411 proof lines;6 outer items and every nested auxiliary compared')
print('CHECKS unique reversible guards; braces/environments/math; references/citations;8 frozen hashes')
print('SCOPE staged source checks; no TeX build, canonical edit, global admission or final page review')
print('DEFECTS', len(defects), 'EVENTS', len(events))
for d in defects:
    print('DEFECT', d['type'], d['change_id'], d['old_location'])
for e in events:
    print('EVENT', e['event_id'], e['type'])
for f in [receiver, STAGE / f'{P}_comparison.md', STAGE / f'{P}_post_exposure_auxiliaries.md',
          STAGE / f'{P}_source_checks.md', STAGE / f'{P}_staged_bibliography.bib',
          STAGE / f'{P}_replacements.tsv', STAGE / f'{P}_guards.tsv',
          STAGE / f'{P}_defects.tsv', STAGE / event_name, Path(__file__)]:
    print('FILE', f.relative_to(ROOT), f.stat().st_size, digest(f.read_bytes()))
print('CANONICAL_UNCHANGED', digest(canonical_bytes))
