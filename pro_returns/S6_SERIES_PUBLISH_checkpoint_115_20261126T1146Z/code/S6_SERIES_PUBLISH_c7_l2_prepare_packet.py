#!/usr/bin/env python3
"""Stage L2's separate exact guards and review rows; no canonical writes.

The fresh proof, program, certificate and output are immutable inputs.
All global tables, the canonical source and bibliography are read-only.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import csv
import re

ROOT = Path(__file__).resolve().parent.parent
STAGE = ROOT/'agents/continuation7_iii_nonstar_specializations'
P = 'S6_SERIES_PUBLISH_III_02L2'
ID = 'maps:src:D.2.27'
NOW = datetime.now(timezone.utc).isoformat()
FRESH_TIME = '2026-11-25T00:06:06Z'
RELEASE = '2026-11-25T00:09:52.436610+00:00'
WHO = ('GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical reasoning effort '
       'not separately exposed; seventh-continuation I1-star check')


def digest(s):
    return sha256(s if isinstance(s, bytes) else s.encode()).hexdigest()


def environment(s, kind):
    start = s.index('\\begin{'+kind+'}')
    end = s.index('\\end{'+kind+'}', start)+len('\\end{'+kind+'}')
    return s[start:end]


def part(s, start, end):
    a = s.index(start)
    b = s.index(end, a)+len(end)
    return s[a:b]


def write_tsv(name, fields, rows):
    with (STAGE/name).open('w', encoding='utf8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t',
                                lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def record_prose(s):
    """Space prose counts; this never changes guarded old/new source text."""
    return re.sub(r'\b(all|All|entire|complete|exact|exactly|indices|ranks|order|value|of|and|position|is|gives|exit|by)(?=[0-9])',
                  r'\1 ', s).replace(' e0,', ' e=0,')


canonical_bytes = (ROOT/'S6_SERIES_PUBLISH_III.tex').read_bytes()
assert digest(canonical_bytes) == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
canonical = canonical_bytes.decode()
old_statement = environment((STAGE/f'{P}_released_statement.tex').read_text(), 'theorem')
old_proof = environment((STAGE/f'{P}_released_proof.tex').read_text(), 'proof')
assert digest(old_proof) == 'edae26c6644c47c52a3bb06511781a16277708c9f6e791d717064e67b498cce8'
assert old_proof.count('\\item ') == 16
receiver = STAGE/f'{P}_receiving.tex'
new = receiver.read_text()
new_statement = environment(new, 'theorem')
new_proof = environment(new, 'proof')
old = old_statement+'\n\n'+old_proof
comparison = (STAGE/f'{P}_comparison.md').read_text()
assert re.findall(r'^\|\s*(\d+)\s*\|', comparison, re.M) == list(map(str, range(1, 17)))
assert 'seventeen' not in comparison

guards = []
shadow = canonical
for kind, before, after in [('statement', old_statement, new_statement),
                             ('proof', old_proof, new_proof)]:
    assert canonical.count(before) == 1, (kind, 'old uniqueness')
    start = canonical[:canonical.index(before)].count('\n')+1
    end = start+before.count('\n')
    if kind == 'proof':
        assert (start, end) == (13052, 13364)
    guards.append((kind, before, after, start, end))
    shadow = shadow.replace(before, after, 1)
for kind, before, after, _, _ in reversed(guards):
    assert shadow.count(after) == 1, (kind, 'new uniqueness')
    shadow = shadow.replace(after, before, 1)
assert shadow.encode() == canonical_bytes


def identities(s):
    return {key: re.findall(pattern, s) for key, pattern in {
        'labels': r'\\label\{([^}]+)\}',
        'hypertargets': r'\\hypertarget\{([^}]+)\}',
        'equation_tags': r'\\tag\{([^}]+)\}'}.items()}


assert identities(old) == identities(new)
assert identities(new)['labels'] == [ID]+[f'maps:eq:D.ST{i}' for i in range(1, 13)]
assert identities(new)['hypertargets'] == ['tag-02L2', 'tag-024V']+[f'tag-025{i}' for i in range(8)]+['tag-024W', 'tag-024X', 'tag-024Y']
assert identities(new)['equation_tags'] == [f'D.ST{i}' for i in range(1, 13)]

# Source checks only: no TeX compilation or rendered-page claim.
stack = []
for match in re.finditer(r'\\(begin|end)\{([^}]+)\}', new):
    side, env = match.groups()
    if side == 'begin':
        stack.append(env)
    else:
        assert stack and stack.pop() == env, (side, env)
assert not stack
depth = 0
for i, ch in enumerate(new):
    if ch not in '{}':
        continue
    slash_count = 0
    j = i-1
    while j >= 0 and new[j] == '\\':
        slash_count += 1
        j -= 1
    if slash_count % 2:
        continue
    depth += 1 if ch == '{' else -1
    assert depth >= 0, i
assert depth == 0
math = []
for token in re.findall(r'\\[()\[\]]', new):
    if token in (r'\(', r'\['):
        math.append(token)
    else:
        assert math and math.pop() == {r'\)': r'\(', r'\]': r'\['}[token]
assert not math
assert not any(ord(ch) < 32 and ch not in '\n\t' for ch in new)
assert not re.search(r'(?<![A-Za-z\\])(?:qquad|quad)\b', new)
refs = re.findall(r'\\(?:eqref|ref|SeriesRef|cref|Cref)\{([^}]+)\}', new)
labels = set(re.findall(r'\\label\{([^}]+)\}', canonical))
assert set(refs) <= labels, set(refs)-labels
assert not re.findall(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}', new)
for bad in ('\\StatementRecord', 'records/', 'code/', '.json', 'certificate',
            'fresh', 'historical', 'root review', 'Bezout', 'Poincare'):
    assert bad not in new, bad
assert new.count('\\begin{theorem}') == new.count('\\end{theorem}') == 1
assert new.count('\\begin{proof}') == new.count('\\end{proof}') == 1

frozen = {
    STAGE/f'{P}_fresh_derivation.md': 'e83ace944c368b42acb9fc5a0c7fda24ce7eb5cf2da5ebf20cf000d69fe907ce',
    STAGE/f'{P}_fresh_lattice_maps.json': '39bf6546778b265530d2703332715e8c2485c53da3ff898b8d4078f1bd213cdf',
    ROOT/'code/S6_SERIES_PUBLISH_c7_l2_star_integral.py': 'd776087529ccd0d9cd788a9f1c58d8f6874a731d65080a4f0525869c12265389',
    ROOT/'code/S6_SERIES_PUBLISH_c7_l2_star_integral.out': '73651038f0835c40564a1469c6713a28b6414f83bfbb80a9c8733303ce0c20f4',
}
for path, expected in frozen.items():
    assert digest(path.read_bytes()) == expected, str(path)

write_tsv(f'{P}_replacements.tsv', ['statement_id', 'old_text', 'new_text'], [
    dict(statement_id=ID, old_text=before, new_text=after)
    for _, before, after, _, _ in guards])

defects = []


def defect(kind, suffix, before, after, reason):
    assert before in old, before[:120]
    assert not after or after in new, after[:120]
    blocks = [(block, start, end) for _, block, _, start, end in guards if before in block]
    assert len(blocks) == 1, (kind, suffix, 'guarded block ambiguity')
    block, start, end = blocks[0]
    line = start+block[:block.index(before)].count('\n')
    assert start <= line <= end
    defects.append(dict(change_id=f'c7-III-02L2-{suffix}', type=kind, statement_id=ID,
        old_location=f'S6_SERIES_PUBLISH_III.tex:{line}', old_page='',
        new_location=str(receiver.relative_to(ROOT)),
        new_page='pending final typeset page concordance', old_text=before, new_text=after,
        reason=record_prose(reason),
        review_status='staged; root admission, source application and final page review pending'))


defect('D25', 'additional-multiplicative-index',
    part(old_proof, 'For an unchanged minimal cap or an index-one multiplicative',
         r'sphere after the \ref{maps:src:D.2.22} rank obstruction.'),
    part(new_proof, 'The local indices are one for unchanged minimal additive and',
         'finite good-reduction cap; and $m_i^3$ for a regular root.'),
    'The index-one assertion is valid for unchanged primitive caps, but the asserted exhaustion omitted allowed free transitive rank-one root quotients. The actual root charts and inverse unit maps give those fillings. Their normalization/conductor, collapsed lattice and complete F/S/K/R boundary identities give normal projection m Fix(T), hence full index m^3. This is the missing case behind the same ST12 counterexample, not a refutation of the unchanged-cap index-one claim.')
defect('D25', 'full-order-product',
    'where $Q_o$ is the product of the indices $q_i$ of the other\nfinite caps and $R$ is the product of regular logarithmic\nmultiplicities.',
    part(new_proof, 'Let $Q_o$ be the product of the indices $q_i$ of the other finite',
         'regular roots and all additional transitive multiplicative roots.'),
    'The allowed OS50/default (a,b)=(3,4), selected I1 position3, star (m,n)=(2,-1), unselected I3 root (m,n)=(3,1), e=0 has explicit free chart action, trivial fundamental group, minimal rational ranks and full normal indices 1 and27. Its H2 order is18, whereas old ST12 with no regular site gives2. Retain maps:eq:D.ST12 with R the product of both regular and additional transitive rank-one orders. The full determinant and every local integral map prove the refinement; the theorem and its two-primary orders stand unchanged.')
defect('D09', 'initial-certificate-path',
    'The sixteen natural initial rows on these three profiles are\nlisted in the certificate\n\\path{records/manifolds_i1star_obstruction.json}.',
    part(new_proof, 'Here $\\langle G,G\\rangle=1/12$.',
         'Each pair is\ncoprime and exactly one entry is divisible by four.'),
    'Derive and list the complete natural inputs from the component equations in the proof. The historical certificate was not opened. The new pre-exposure program and its complete output are recorded outside the paper for the programs table.')
defect('D09', 'period-basis-certificate',
    'Here $\\alpha$ is primitive. The exact integral change of basis\nfor every marked row is in the certificate.',
    part(new_proof, 'The matrix $H=(\\alpha,\\beta,\\lambda,\\ell)$ is integral with',
         '$H^{-1}=\\operatorname{adj}H$.'),
    'Give the universal determinant-one star basis and its inverse, together with the exact OS50/II conjugacy, actual coordinate direction and transported units. The alternate old fixed vector has the explicit shear ell0=ell+hs delta with inverse subtraction, preserving all wedge and pairing formulas.')
defect('D09', 'symbolic-certificate-narration',
    'The certificate also verifies\nthis identity symbolically with arbitrary two-by-two normal\nprojection matrices and arbitrary longitudinal coefficients.',
    part(new_proof, 'Multiplication on the left by the block upper triangular matrix',
         '$(be+\\sum_i f_i(\\delta),0,\\ldots,0)$.'),
    'Prove the all-sites determinant by its explicit determinant-one block row map and inverse, for arbitrary normal ranks and full integral covolumes. The separate new symbolic program checks these displayed maps in ranks2,3,4. No old symbolic execution or certificate verification is claimed.')
defect('D22', 'conductor-integral-h1',
    part(old_proof, 'The star cap has the abelian presentation obtained from the',
         'relation\nis primitive because $\\gcd(m_*,n_*)=1$.'),
    part(new_proof, 'The conductor map\non $H_1$ is injective, since its map to $D$ is a covering.',
         'Thus $H_1(U_2)=\\mathbb Z^2$.'),
    'Fill the integral justification with the distinct normalization and double-curve lattices, their covering matrices and inverses, and the exact elimination of the primitive conductor relation. The order-four conductor and all other cap H1 calculations are also written in full at their proper scope. This is a missing-map justification, not a refuted freeness assertion.')
defect('D10', 'machine-header',
    next(line for line in old_statement.splitlines() if line.startswith(r'\StatementRecord')),
    r'\textnormal{\small tag 02L2.}',
    'Print the small permanent tag, retain every label and hypertarget, and cite mathematical dependencies at their precise proof locations. Navigation and check apparatus remain in the records.')
defect('D01', 'earlier-missed-effect',
    'This is precisely the\nintegral effect missed by the rational vertical coinvariant\nidentity $[\\delta]=4[\\beta]$.', '',
    'Remove the production-history comparison. The full torsion extension and the exact projected-kernel quotient prove the mathematical index four directly.')
defect('D02', 'defensive-determinant',
    'Multiplying the rational calculation by the\nintegral covolumes is an equality of integer determinants,\nnot a saturation assumption.',
    'The indices are those of the full integral kernels,\nincluding the order-two torsion of $U_4$.',
    'State the integral covolumes positively and give the exact row operation proving the determinant. Its inverse and the full local kernels make the integral assertion explicit.')
defect('D14', 'proof-organization',
    r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]',
    r'\emph{The marked inputs and the primitive star periods.}',
    'Organize one complete proof by periods, cap normalization, full normal maps, exterior determinant and global exhaustion. All16 original proof items and all12 equation identities are compared and retained at their settled scope. Unit restructuring and final typeset page review remain later gates.')
defect('D23', 'poincare-accent',
    'Under Poincare--Lefschetz\nduality',
    r"The pair sequence and Poincar\'e--Lefschetz duality give",
    'Restore the accent in the mathematical text; source check only, with rendered-page review pending.')

write_tsv(f'{P}_defects.tsv', ['change_id', 'type', 'statement_id', 'old_location',
          'old_page', 'new_location', 'new_page', 'old_text', 'new_text', 'reason',
          'review_status'], defects)

event_file = f'{P}_CHECK_EVENTS.tsv'
events = []


def event(kind, suffix, phase, source, group, outcome, when=NOW):
    row = len(events)+2
    events.append(dict(statement_id=ID, date=when[:10], who=WHO, type=kind,
        outcome=record_prose(outcome), event_id=f'publish:c7:III:02L2:{suffix}', phase=phase,
        source_file=source, source_row='1', source_event_type=kind,
        evidence_group=f'publish:c7:III:02L2:{group}',
        publish_input_file=str((STAGE/event_file).relative_to(ROOT)),
        publish_input_row=str(row), date_utc=when,
        where=str((STAGE/f'{P}_comparison.md').relative_to(ROOT))+'; '+str(receiver.relative_to(ROOT))))


event('targeted proof check', 'fresh-complete-derivation', 'before whole original L2 exposure',
    str((STAGE/f'{P}_fresh_derivation.md').relative_to(ROOT)), 'fresh-star-derivation',
    'Before original exposure, derived the complete16 natural rows and their exact period maps, primitive semistable cover/reflection, all original-star exclusions and even-return obstruction. Proved both actual normalization/conductor models, distinct covering lattices, odd ruling clutch, integral H1/H2/H3/H4, full boundary surjectivity and torsion-sensitive normal indices1/4. Constructed the delta-root prism, full integral graph/fibre maps and arbitrary-parameter two-local determinant, proving exactly one/two factors of2 and the full nonexistence theorem including all admissible odd additional roots and refinements. Root read all745 fresh lines, all218 code lines and all33 output lines before release.', FRESH_TIME)
event('computation or formal certificate', 'fresh-integral-maps', 'before whole original L2 exposure',
    'code/S6_SERIES_PUBLISH_c7_l2_star_integral.py', 'fresh-star-derivation',
    'New program with historical target algorithms and original closed: exact16 marked rows from raw defining tuples, universal odd/even bases, graph and primitive exterior maps, OS50/II inverse conjugacy, all10 covering lattice cases and all4 possible vertical torsion components. Full integer coordinate inverses and all33 successful output lines read. This finite computation supports the written universal all-order geometric proof, with no parameter bound substituted for it.', FRESH_TIME)
event('computation or formal certificate', 'post-exposure-integral-auxiliaries', 'after whole original L2 exposure',
    'code/S6_SERIES_PUBLISH_c7_l2_aux_integral.py', 'post-exposure-integral-auxiliaries',
    'New distinct literal-component/Hermite computation verifies the entire172-row exterior auxiliary, all29 retained OS50 boundary H1 groups, universal rank-one F/S/K/R inverse identities and index m^3, arbitrary normal-block determinant with ranks2/3/4 and every affine functional, and the exact marked order18 counterexample. Full program and all27 output lines read by checker and root. Stdout/stderr were combined by2>&1 in the .out; the process returned exit0. No separate .err capture or historical program execution is claimed.')
event("refuted, with the refined statement's id", 'full-order-refinement', 'after whole original L2 exposure',
    str((STAGE/f'{P}_post_exposure_auxiliaries.md').relative_to(ROOT)), 'post-exposure-integral-auxiliaries',
    'Refined auxiliary identity remains maps:eq:D.ST12 within maps:src:D.2.27. The full permitted affine scope includes a transitive rank-one root, whose explicit free chart action and complete integral boundary maps give kappa=m^3. For OS50/default (a,b)=(3,4), selected I1@3, star(2,-1), I3 root(3,1), e0, the group is trivial and |H2|=18, contradicting old ST12 value2. Enlarge R to include these multiplicative root orders. Both cap rows, indices1/4, the theorem, and its exact two-primary conclusion remain proved; the event refutes only the auxiliary exhaustion and full-order product.')
event('used and rechecked in this run', 'whole-original-comparison', 'after whole original L2 exposure',
    str((STAGE/f'{P}_comparison.md').relative_to(ROOT)), 'complete-original-comparison',
    f'After release {RELEASE}, read the complete statement and all313 proof lines, exactly16 item tokens, every auxiliary D.ST1--D.ST12 and every historical computation claim. The receiving proof includes the complete fresh derivation, exact old/new fixed-period shear, all conductor/H1 maps, positive-root prism, full arbitrary-normal determinant, every local index, extra rank-one root action and counterexample, and refinement maps. Extra cusp roots have positive local defect by the component/degree-one pair calculation, so the full-order minimal-rank scope is complete. Compared every original clause and preserved all13 labels/hypertargets and12 equation tags. No old algorithm or broad external citation receives new execution/reading credit. Separate unique statement/proof guards are jointly reversible; source structure, references and all frozen hashes pass. No TeX build, rendered-page review, canonical mutation or global completion is claimed.')
write_tsv(event_file, ['statement_id', 'date', 'who', 'type', 'outcome', 'event_id',
          'phase', 'source_file', 'source_row', 'source_event_type', 'evidence_group',
          'publish_input_file', 'publish_input_row', 'date_utc', 'where'], events)

assert (ROOT/'S6_SERIES_PUBLISH_III.tex').read_bytes() == canonical_bytes
print('STAGED_AT', NOW)
for kind, before, after, start, end in guards:
    print('GUARD', kind, f'{start}--{end}', 'old_sha256', digest(before),
          'new_sha256', digest(after))
print('IDENTITIES 13 labels; 13 hypertargets; 12 equation tags; preserved exactly and uniquely')
print('ORIGINAL 313 proof lines; exactly 16 enumerated items; whole statement/auxiliary comparison complete')
print('SOURCE_CHECKS braces, environments, math delimiters, references and frozen hashes passed; no TeX build or page review claimed')
print('GUARDS separate unique statement/proof substitutions; joint reverse returns identical canonical bytes')
print('DEFECTS', len(defects), 'EVENTS', len(events))
for row in defects:
    print('DEFECT', row['type'], row['change_id'], row['old_location'])
for row in events:
    print('EVENT', row['event_id'], row['type'])
for path in [receiver, STAGE/f'{P}_comparison.md', STAGE/f'{P}_post_exposure_auxiliaries.md',
             STAGE/f'{P}_replacements.tsv', STAGE/f'{P}_defects.tsv', STAGE/event_file,
             STAGE/f'{P}_staged_bibliography.bib',
             ROOT/'code/S6_SERIES_PUBLISH_c7_l2_aux_integral.py',
             ROOT/'code/S6_SERIES_PUBLISH_c7_l2_aux_integral.out', Path(__file__).resolve()]:
    print('SHA256', digest(path.read_bytes()), path.relative_to(ROOT))
print('CANONICAL_UNCHANGED', digest(canonical_bytes))
print('FRESH_FROZEN_FILES_UNCHANGED', len(frozen))
