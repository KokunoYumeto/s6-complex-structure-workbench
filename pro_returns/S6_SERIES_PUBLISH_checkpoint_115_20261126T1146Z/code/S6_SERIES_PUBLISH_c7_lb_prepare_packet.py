#!/usr/bin/env python3
"""Stage LB's complete guarded replacement and review records.

The canonical source, global records, bibliography and all frozen fresh
evidence are read-only. This program performs source checks, not a TeX build.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import csv
import re

ROOT = Path(__file__).resolve().parent.parent
STAGE = ROOT / 'agents/continuation7_iii_conic'
P = 'S6_SERIES_PUBLISH_III_02LB'
ID = 'maps:src:D.2.35'
NOW = datetime.now(timezone.utc).isoformat()
FRESH_TIME = '2026-11-25T01:01:49.520207+00:00'
RELEASE = '2026-11-25T01:23:55.653773+00:00'
WHO = ('GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical reasoning effort '
       'not separately exposed; seventh-continuation conic-pattern check')


def digest(value):
    return sha256(value if isinstance(value, bytes) else value.encode()).hexdigest()


def environment(text, kind):
    start = text.index(r'\begin{' + kind + '}')
    end = text.index(r'\end{' + kind + '}', start) + len(r'\end{' + kind + '}')
    return text[start:end]


def part(text, start, end):
    left = text.index(start)
    right = text.index(end, left) + len(end)
    return text[left:right]


def write_tsv(name, fields, rows):
    with (STAGE / name).open('w', encoding='utf8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t',
                                lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


canonical_path = ROOT / 'S6_SERIES_PUBLISH_III.tex'
canonical_bytes = canonical_path.read_bytes()
assert digest(canonical_bytes) == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
canonical = canonical_bytes.decode()
old_statement = environment((STAGE / f'{P}_released_statement.tex').read_text(), 'theorem')
old_proof = environment((STAGE / f'{P}_released_proof.tex').read_text(), 'proof')
assert digest(old_proof) == 'eb3e7605efb83ea6fd1892dad1f0f6d6b56dae5e5dafb2e222d1507e8afcb8a5'
assert old_proof.count(r'\item ') == 14
assert len(old_proof.splitlines()) == 333
receiver = STAGE / f'{P}_receiving.tex'
new = receiver.read_text()
new_statement = environment(new, 'theorem')
new_proof = environment(new, 'proof')
old = old_statement + '\n\n' + old_proof
comparison = (STAGE / f'{P}_comparison.md').read_text()
assert re.findall(r'^\|\s*(\d+)\s*\|', comparison, re.M) == list(map(str, range(1, 15)))
assert 'zero-based' in comparison and 'zero-based' in new

guards = []
shadow = canonical
for kind, before, after in [('statement', old_statement, new_statement),
                             ('proof', old_proof, new_proof)]:
    assert canonical.count(before) == 1, (kind, 'old uniqueness')
    position = canonical.index(before)
    start = canonical[:position].count('\n') + 1
    end = start + before.count('\n')
    if kind == 'proof':
        assert (start, end) == (15178, 15510)
    guards.append((kind, before, after, start, end))
    shadow = shadow.replace(before, after, 1)
for kind, before, after, _, _ in reversed(guards):
    assert shadow.count(after) == 1, (kind, 'new uniqueness')
    shadow = shadow.replace(after, before, 1)
assert shadow.encode() == canonical_bytes


def identities(text):
    return {key: re.findall(pattern, text) for key, pattern in {
        'labels': r'\\label\{([^}]+)\}',
        'hypertargets': r'\\hypertarget\{([^}]+)\}',
        'equation_tags': r'\\tag\{([^}]+)\}'}.items()}


assert identities(old) == identities(new)
assert identities(new)['labels'] == [ID] + [f'maps:eq:D.C2{i}' for i in range(1, 17)]
assert identities(new)['hypertargets'] == [
    'tag-02LB', 'tag-01Y7', 'tag-01YF', 'tag-01YG', 'tag-01YH',
    'tag-01YI', 'tag-01YJ', 'tag-01YK', 'tag-01YL', 'tag-01YM',
    'tag-01Y8', 'tag-01Y9', 'tag-01YA', 'tag-01YB', 'tag-01YC',
    'tag-01YD', 'tag-01YE']
assert identities(new)['equation_tags'] == [f'D.C2{i}' for i in range(1, 17)]

# These are literal source checks; compilation and page reading remain later gates.
stack = []
for match in re.finditer(r'\\(begin|end)\{([^}]+)\}', new):
    side, env = match.groups()
    if side == 'begin':
        stack.append(env)
    else:
        assert stack and stack.pop() == env, (side, env)
assert not stack
depth = 0
for index, char in enumerate(new):
    if char not in '{}':
        continue
    slashes, cursor = 0, index - 1
    while cursor >= 0 and new[cursor] == '\\':
        slashes += 1
        cursor -= 1
    if slashes % 2:
        continue
    depth += 1 if char == '{' else -1
    assert depth >= 0, index
assert depth == 0
math = []
for token in re.findall(r'\\[()\[\]]', new):
    if token in (r'\(', r'\['):
        math.append(token)
    else:
        assert math and math.pop() == {r'\)': r'\(', r'\]': r'\['}[token]
assert not math
assert len(re.findall(r'(?<!\\)\$', new)) % 2 == 0
assert not any(ord(char) < 32 and char not in '\n\t' for char in new)
assert not re.search(r'(?<![A-Za-z\\])(?:qquad|quad)\b', new)
refs = re.findall(r'\\(?:eqref|ref|SeriesRef|cref|Cref)\{([^}]+)\}', new)
labels = set(re.findall(r'\\label\{([^}]+)\}', canonical))
assert set(refs) <= labels, set(refs) - labels
bib = (ROOT / 'S6_SERIES_PUBLISH_references.bib').read_text()
staged_bib = (STAGE / f'{P}_staged_bibliography.bib').read_text()
keys = set(re.findall(r'@\w+\s*\{\s*([^,\s]+)', bib + '\n' + staged_bib))
cites = {key.strip() for group in re.findall(
    r'\\cite(?:\[[^]]*\])?\{([^}]+)\}', new) for key in group.split(',')}
assert cites == {'manAndrus77', 'manZhubr75'}
assert cites <= keys, cites - keys
for bad in (r'\StatementRecord', 'records/', 'code/', '.json', 'certificate',
            'fresh', 'historical', 'root review', 'SHA256', 'Bezout', 'Poincare'):
    assert bad not in new, bad
assert new.count(r'\begin{theorem}') == new.count(r'\end{theorem}') == 1
assert new.count(r'\begin{proof}') == new.count(r'\end{proof}') == 1

frozen = {
    STAGE / f'{P}_fresh_derivation.md': 'ab211ef6eec54636b2f7078f5e711b0aba7a59689ee3b1513d829fd395efe5d7',
    STAGE / f'{P}_inputs_and_primary_reading.md': '61ac92b78d32f4f3a36157ce3aa1f5ab5e925db1c2e1d0644f10c32f96254524',
    STAGE / f'{P}_fresh_data.json': '1e0731677fdbad18c93963bd6eda7f44659556ba660e14d6e61f2b8add60bca1',
    STAGE / f'{P}_fresh_patterns.tsv': 'cec55ff05c37aae7b70e2d3b3eb43b50eb7411cb0115f91bd9c6d9629fc1a0f7',
    ROOT / 'code/S6_SERIES_PUBLISH_c7_lb_conic.py': '8831024fba167c754d06730baa0ac9c3ad83c7ad2fe7340adf6a2ca0637f6663',
    ROOT / 'code/S6_SERIES_PUBLISH_c7_lb_conic.out': '985072d30eb6b7cdae6ad11998d0edc3b00f01da173ccccd81a4e4a8a5b74f25',
    ROOT / 'agents/continuation7_iii_graph/S6_SERIES_PUBLISH_III_02LB_fresh_bounded_review.md':
        '8baf36cc480ae331629dbd6315a559c761d470cc2ed372d17727da8803554872',
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
    line = start + block[:block.index(before)].count('\n')
    assert start <= line <= end
    defects.append(dict(change_id=f'c7-III-02LB-{suffix}', type=kind, statement_id=ID,
        old_location=f'S6_SERIES_PUBLISH_III.tex:{line}', old_page='',
        new_location=str(receiver.relative_to(ROOT)),
        new_page='pending final typeset page concordance', old_text=before, new_text=after,
        reason=reason,
        review_status='staged; root admission, source application and final page review pending'))


defect('D27', 'two-smooth-models',
    part(old_statement, 'Every simply connected output, for every allowed finite',
         r'\qquad \langle\alpha^3,[X]_2\rangle=1.'),
    part(new_statement, r'Let $M_1=M_{\mathrm{conic}}$', r'\qquad X\cong M_\varepsilon'),
    'The exact stipulated Jordan fan gives cubic 1+kappa mod 2. The simply connected OS47/default example (a,b)=(7,2), zero 3, e=1 has cubic zero, whereas the conic has cubic one. A diffeomorphism must pull the unique nonzero degree-two mod-two class to the unique such class and preserve its cubic evaluation, so this example refutes the uniform smooth identification. Retain maps:src:D.2.35 and maps:eq:D.C21 with the complete two-model replacement. All fifteen patterns, all thirteen rows, all homology and every allowed parameter are retained; the framed M0 construction, complete augmented-ring maps and oriented recognition prove the replacement.')
defect('D25', 'cusp-character',
    part(old_proof, 'Its two nonconstant coefficients are even and its constant is odd,',
         'is therefore nontrivial.'),
    part(new_proof, 'The half-circle lift in the Jordan Gaussian coordinate has dense',
         r'=1+\kappa\pmod2.'),
    'The physical support-difference identity is correct, but its use as the character on the stipulated fan omitted the exact physical-to-Jordan lattice and line maps. The dense half-phase plus the Cartier slope gives c_C=1+kappa. In OS47/default (7,2), zero 3, their exponents are -1 and 7, so the character is zero. This is the local occurrence of the same cubic refinement, not a refutation of the physical polynomial.')
defect('D25', 'exact-wall-degree',
    part(old_proof, 'The degree along its adjacent toric wall is,',
         r'$-a\rho+abj$, which is odd.'),
    part(new_proof, 'The adjacent-cone relation gives the degree',
         r"$\zeta_{\sigma'}=w^{-(K_{11}-K_{12})}\zeta_\sigma$."),
    'This is a separate numerical auxiliary. The prescribed fan has degree K11-K12=a(nu-b*kappa). In OS47/default (7,2), zero 3, nu=kappa=1, j=-1 and rho=-13, the actual degree is -7 while the old expression is 77. Its possible orientation sign cannot repair the unequal absolute values. Both actual curve degrees remain odd, and the other diagonal changes this degree by the even number 2K12.')
defect('D25', 'full-circle-weights',
    part(old_proof, 'The zero has',
         r'$\mathcal O(-1)_{+1}\oplus\mathcal O(-1)_{-1}$ as in \ref{maps:src:D.2.14}.'),
    part(new_proof, 'At the cusp the physical circle has short coordinate',
         'fixes $C$ and acts negatively on both normal directions.'),
    'This separate auxiliary needs its full circle scope corrected. The physical circle is d=C^{-1}delta=(-b*kappa,nu) in the actual short lattice; its endpoint weights are (b*kappa-nu,nu,-b*kappa) and (-nu,nu-b*kappa,b*kappa). For OS47/default (7,2), zero 3, these are (1,1,-2) and (-1,-1,2), so the full circle moves the curve. The exact overlap retains the complex O(-1)^2 normal bundle; reduction modulo two retains the fixed curve and the two negative involution signs used in localization.')
defect('D25', 'global-fixed-weight',
    r'\widetilde\alpha|_C=\alpha|_C+\tau^2,',
    r'\widetilde\alpha|_C=\alpha|_C+(1+\kappa)\tau^2,',
    'Retain maps:eq:D.C216 and the one common equivariant adjustment. The actual cusp coefficient is 1+kappa, and the elliptic coefficient remains zero with the same possible mixed degree-one term. This is the global fixed-point occurrence of the main cubic correction, not an additional independent refutation.')
defect('D25', 'localization-cube',
    part(old_proof, r'\langle\alpha^3,[X]_2\rangle', r'=\int_C\alpha|_C=1.'),
    part(new_proof, r'\langle\alpha^3,[X]_2\rangle',
         r'&=(1+\kappa)\int_C\alpha|_C=1+\kappa.'),
    'Retain the exact Euler class tau^4, both negative normal signs and the zero elliptic contribution. Substituting the corrected character gives cubic 1+kappa on every prescribed fan and parameter. The explicit Thom/Gysin inverse and the full exterior-algebra calculation justify the formula; it is the final occurrence of the same uniform-cubic error.')
defect('D22', 'physical-cartier-pullback',
    part(old_proof, 'At the zero, assign the following integer values to the lattice',
         'vertices and interpolate linearly on the given unimodular fan:'),
    part(new_proof, r'The exact comparison with \eqref{maps:eq:D.C210} is',
         'extension and every inverse chart map, with all units retained.'),
    'Supply the missing fan and line-coordinate comparison at the point where the physical support is introduced. The exact map x=Cv with inverse C^{-1}, phi(Cv)=-psi(v)+L0*v and the reciprocal monomial gauges identify every regular Cartier coordinate. Both physical period identities remain correct. This row records a missing justification repaired by the explicit maps, not a separate false polynomial claim.')
defect('D22', 'global-line-comparison',
    part(old_proof, 'Both lines\nare symmetric and rigidified with alternating form',
         'controls the mixed values as well as the alternating fibre form.'),
    part(new_proof, r'In real short/long coordinates $x=S U+L B$',
         'the stated pure-fibre and zero-sweep Chern values on $V$.'),
    'Give the actual comparison and inverse instead of leaving the global ratio argument implicit. The Gaussian gauge retains all units; the integer character z^((a-1)/2) gives exactly the three original h,F,J factors and reciprocal inverse. Their global scalar-one period lifts, common connection, rigidifying origin and half-period lift prove both the fibre and mixed Chern values. No mathematical refutation of the symmetric rigidified line conclusion is asserted.')
defect('D09', 'statement-data-path',
    r'\path{records/root_remaining_smooth_profiles.json}',
    r'Take a marked pattern in \eqref{maps:eq:D.C22}.',
    'Put the complete fifteen-pattern finite input in the statement and derive it from the component equations and cap options. The zero positions stay explicitly zero-based. Historical target tables and programs were not opened; the new raw-only enumeration is recorded outside the mathematics.')
defect('D02,D09', 'angular-certificate',
    part(old_proof, 'Both assertions are checked',
         'certificate below.'),
    part(new_proof, 'For an explicit integral verification, order the columns as',
         r'of the images of all $T_i-I$ is also exactly $\Lambda_0$.'),
    'Replace historical certificate narration by the thirteen unit minors, their adjugate right inverses and exact preimages under the monodromy relations. This proves both integral image assertions without assigning a new execution to the unopened historical algorithm.')
defect('D09', 'quadratic-certificate',
    'The certificate\nchecks this on all sixteen vectors modulo two at every marked site.',
    part(new_proof, r'Its polar form is $\Omega\bmod2$.',
         'hence every actual monodromy preserves $Q$.'),
    'The unique odd quadratic form on the elliptic mod-two plane and the even gamma column give the invariance directly. The separate frozen raw-only program and full output support the displayed structural proof; no historical certificate is credited.')
defect('D09', 'stabilizer-certificate',
    'All other rank-one scalar stabilizers have odd order; this is checked\nfrom the actual vanishing vectors in the certificate.',
    part(new_proof, 'At a rank-one\nplace the surviving elliptic lattice is',
         'so gives no fixed point.'),
    'Give the primitive quotient map and exact criterion delta-l in 2 Lambda, followed by the complete unique-I2 determination from the marked vectors. The finite and original additive caps are handled separately by their actual maps for all multiplicities.')
defect('D10', 'machine-header',
    next(line for line in old_statement.splitlines() if line.startswith(r'\StatementRecord')),
    r'\textnormal{\small tag 02LB.}',
    'Print the small permanent tag and preserve every label and hypertarget. Dependencies and primary citations occur where used in the complete proof. The navigation and check apparatus belongs to the records.')
defect('D14', 'proof-organization',
    r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=0pt,labelsep=.5em]',
    r'\emph{The marked inputs and the common piece.}',
    'Organize the complete proof by the finite inputs and exterior, one global line, prescribed cap extensions, fixed curves, full attachment, equivariant comparison and two oriented models. All fourteen original item tokens, every auxiliary and all sixteen equation identities are compared. Whole-paper restructuring and final page concordance remain later gates.')
defect('D11', 'repeated-statement-scope',
    part(old_statement, 'The statement includes the original additive caps in this table;',
         'other caps, or include additional regular logarithmic transformations.'),
    '',
    'State the same construction scope once in the theorem hypotheses: the original additive choices, stipulated multiplicative fans and absence of extra regular logs are all retained. The repeated closing disclaimer is removed without changing the parameter domain.')
defect('D02', 'two-period-defence',
    'The two displayed period identities prove that both actual deck\nfactors descend this extension; it is not enough to match only one\nof them.',
    part(new_proof, 'Thus the regular Cartier coordinates agree after this gauge;',
         r'therefore glue to one equivariant line $\mathcal L$ on $W$.'),
    'State the two descent identities and their full inverse Gaussian/Cartier maps positively. The mathematical requirement that both deck factors descend remains proved.')
defect('D02', 'positivity-defence',
    'This uses an integral piecewise affine support function; no\npositivity of the auxiliary line is required.',
    'Interpolate on each prescribed unimodular triangle.',
    'The integral Cartier construction is written for the actual possibly indefinite symmetric matrix, with its regular coordinate maps. That construction already gives the precise scope of the line extension.')
defect('D02', 'transfer-defence',
    'This uses the full integral normal columns, not a transfer of even\ndegree.',
    'Thus the functional one on $s$ and zero on every sweep descends\n'
    r'to the specified $\alpha$.',
    'Give the full integral finite, original and ordinary normal maps and their elimination, including the inverse meridian shear, instead of the defensive transfer comparison.')
defect('D02', 'ext-defence',
    part(old_proof, r'The absence of an $\operatorname{Ext}(H_1(W),\mathbb F_2)$ term is',
         r'part of \eqref{maps:eq:D.C25}, not an implicit universal-coefficient choice.'),
    'The free $H_1(W)$ gives the exact universal-coefficient identification.',
    'State the UCT hypothesis and its consequence directly, retaining the complete free H1 proof and global class comparison.')
defect('D02', 'fixed-normalization-defence',
    'In particular two unrelated fixed-point normalizations have not been\nchosen.',
    'Both ordinary curve degrees are odd, so the sum of their\ndegree-weight contributions is unchanged by the common shift as well.',
    'The unique order-two group element and the one global tau-squared adjustment prove the common normalization. Its invariance in the final integral is stated positively.')
defect('D02', 'pontryagin-defence',
    'This retains the two-primary refined invariant, not just ordinary\nPontryagin classes.',
    part(new_proof, 'The full spin-bordism description gives the same classification',
         'conversion of the complete invariants.'),
    'Retain the full old auxiliary with its exact spin-bordism quotient, generator and inverse cubic detector. The primary proof scope on printed p809 preserves H2 and kills free H3. The augmented-ring maps, Pontryagin class and orientation identify the same two values; no ordinary-p1-only classification is used.')

write_tsv(f'{P}_defects.tsv', ['change_id', 'type', 'statement_id', 'old_location',
          'old_page', 'new_location', 'new_page', 'old_text', 'new_text', 'reason',
          'review_status'], defects)

event_file = f'{P}_CHECK_EVENTS.tsv'
events = []


def event(kind, suffix, phase, source, group, outcome, when=NOW):
    row = len(events) + 2
    events.append(dict(statement_id=ID, date=when[:10], who=WHO, type=kind,
        outcome=outcome, event_id=f'publish:c7:III:02LB:{suffix}', phase=phase,
        source_file=source, source_row='1', source_event_type=kind,
        evidence_group=f'publish:c7:III:02LB:{group}',
        publish_input_file=str((STAGE / event_file).relative_to(ROOT)),
        publish_input_row=str(row), date_utc=when,
        where=str((STAGE / f'{P}_comparison.md').relative_to(ROOT)) + '; ' +
              str(receiver.relative_to(ROOT))))


event('targeted proof check', 'fresh-complete-derivation', 'before whole original LB exposure',
    str((STAGE / f'{P}_fresh_derivation.md').relative_to(ROOT)), 'fresh-conic-derivation',
    'KS derived the complete fifteen-pattern, thirteen-row theorem from the statement and admitted inputs before original exposure. The full proof constructs the actual prescribed-fan global equivariant line, all inverse gauges and cap maps, full parameter attachment, common Borel normalization, cubic 1+kappa and both framed oriented models. The exact result is eight conic patterns on seven rows and seven cubic-zero patterns on six rows. The admitted LY method is explicitly disclosed; this is a targeted derivation, not a claim of a different geometric method. Root and the peer checker fully read all 771 proof lines, 339 code lines and 380 output lines before individual release.', FRESH_TIME)
event('computation or formal certificate', 'fresh-raw-marked-maps', 'before whole original LB exposure',
    'code/S6_SERIES_PUBLISH_c7_lb_conic.py', 'fresh-conic-derivation',
    'The new raw-only program reconstructs the natural input rows and minimal additive choices, obtains all fifteen patterns, retains every literal period basis and inverse, checks Gaussian gauges, both adjacent cusp charts and nodal maps, symbolic finite elimination and full exterior-algebra localization. Historical target catalogue, code and output remained closed. The author, peer and root read the complete 339-line program and all 380 final output lines. The finite calculation supports the written all-parameter proof; no new rerun of the frozen program is claimed in this packet.', FRESH_TIME)
event('computation or formal certificate', 'post-exposure-auxiliary-maps', 'after whole original LB exposure',
    'code/S6_SERIES_PUBLISH_c7_lb_auxiliary_maps.py', 'post-exposure-auxiliaries',
    'The new 216-line program proves all original h,F,J identities, exact Gaussian-to-original gauge and reciprocal inverse, both physical support differences and actual Cartier pullback, full circle weights and wall degrees, all thirteen angular unit minors and monodromy-image right inverses, and both rank-one period laws with integral supports at all 42 site occurrences. The OS47/default zero-3 example is evaluated literally. The full program and all 27 final output lines were read. Execution returned exit code zero with stdout and stderr combined in the .out by 2>&1; no separate stderr file and no historical execution are claimed.')
event("refuted, with the refined statement's id", 'cubic-and-two-model-refinement',
    'after complete whole original LB comparison',
    str((STAGE / f'{P}_fresh_derivation.md').relative_to(ROOT)), 'cubic-refinement',
    'Refined identities remain maps:src:D.2.35 and maps:eq:D.C21, with the cusp and Borel occurrences retained as maps:eq:D.C212 and maps:eq:D.C216. The exact stipulated fan gives cubic 1+kappa, so seven of the fifteen patterns have cubic zero and cannot be diffeomorphic to the cubic-one conic. OS47/default (a,b)=(7,2), zero 3, e=1 is an explicit simply connected example. The unique degree-two class and diffeomorphism pullback prove the obstruction. The complete replacement constructs M0 and proves oriented X=M_(1+kappa); all integral homology, rows and affine multiplicities are retained. This finding was derived before exposure and is formally recorded after full original comparison.')
event("refuted, with the refined statement's id", 'wall-degree-auxiliary-refinement',
    'after complete whole original LB comparison',
    str((STAGE / f'{P}_post_exposure_auxiliaries.md').relative_to(ROOT)), 'post-exposure-auxiliaries',
    'The separate exact-degree auxiliary at maps:eq:D.C212 within maps:src:D.2.35 is refined to a(nu-b*kappa)=K11-K12 on the prescribed fan. For OS47/default (7,2), zero 3, the actual degree is -7 whereas the old expression -a*rho+a*b*j is 77, so its allowed sign cannot repair it. The exact chart transition proves the new degree. Odd parity and the even difference between the two diagonal wall calculations remain valid.')
event("refuted, with the refined statement's id", 'circle-weight-auxiliary-refinement',
    'after complete whole original LB comparison',
    str((STAGE / f'{P}_post_exposure_auxiliaries.md').relative_to(ROOT)), 'post-exposure-auxiliaries',
    'The separate full-circle auxiliary in maps:src:D.2.35 is refined by the exact lattice map d=C^{-1}delta=(-b*kappa,nu) and its two chart actions. OS47/default (7,2), zero 3 has endpoint weights (1,1,-2) and (-1,-1,2), so the physical circle moves the rational curve. The exact chart overlap retains its complex O(-1)^2 normal bundle, and reduction modulo two retains the two negative involution signs and the full fixed set used in localization. The event refutes only the stronger circle-coordinate/weight assertion.')
event('used and rechecked in this run', 'whole-original-comparison',
    'after whole original LB exposure',
    str((STAGE / f'{P}_comparison.md').relative_to(ROOT)), 'complete-original-comparison',
    f'After release {RELEASE}, read the complete statement and all 333 proof lines, including all fourteen item tokens, all sixteen equation identities, every auxiliary and each historical certificate assertion. The receiver contains all exact old-factor gauges and inverses, actual fan/support transport, rank-one maps, global attachment and Borel comparison, both framed models and the complete Andrus/Zhubr invariant conversion. Andrus printed pp17,19-21,42 and Zhubr printed pp793-795,803,807,809 were actually rendered and read at the exact hashes in the source note. The English pp793/794 literally print H2; the zero-free-H3 scope comes from the proof in section4.1 p809, and the earlier inaccurate K9 source description is not repeated. No unopened old program or unrendered source page receives new credit. All seventeen ordered labels/targets and sixteen equation tags are preserved, separate unique guards are jointly reversible, and every defect location is inside its released target block. Source checks and frozen hashes pass; no TeX build, rendered-page review, canonical mutation or global admission is claimed.')
write_tsv(event_file, ['statement_id', 'date', 'who', 'type', 'outcome', 'event_id',
          'phase', 'source_file', 'source_row', 'source_event_type', 'evidence_group',
          'publish_input_file', 'publish_input_row', 'date_utc', 'where'], events)

assert canonical_path.read_bytes() == canonical_bytes
print('STAGED_AT', NOW)
for kind, before, after, start, end in guards:
    print('GUARD', kind, f'{start}--{end}', 'old_sha256', digest(before),
          'new_sha256', digest(after))
print('IDENTITIES 17 labels; 17 hypertargets; 16 equation tags; preserved exactly and uniquely')
print('ORIGINAL 333 proof lines; 14 item tokens; whole statement and every auxiliary compared')
print('SOURCE_CHECKS braces, environments, math delimiters, references, citations and frozen hashes passed')
print('SOURCE_SCOPE no TeX build, rendered-page review or whole-paper completion claimed')
print('GUARDS separate unique statement/proof substitutions; joint reverse returns identical canonical bytes')
print('DEFECTS', len(defects), 'EVENTS', len(events))
for row in defects:
    print('DEFECT', row['type'], row['change_id'], row['old_location'])
for row in events:
    print('EVENT', row['event_id'], row['type'])
for path in [receiver, STAGE / f'{P}_comparison.md',
             STAGE / f'{P}_post_exposure_auxiliaries.md',
             STAGE / f'{P}_post_exposure_maps.json',
             STAGE / f'{P}_replacements.tsv', STAGE / f'{P}_defects.tsv',
             STAGE / event_file, STAGE / f'{P}_staged_bibliography.bib',
             ROOT / 'code/S6_SERIES_PUBLISH_c7_lb_auxiliary_maps.py',
             ROOT / 'code/S6_SERIES_PUBLISH_c7_lb_auxiliary_maps.out',
             Path(__file__).resolve()]:
    print('SHA256', digest(path.read_bytes()), path.relative_to(ROOT))
print('CANONICAL_UNCHANGED', digest(canonical_bytes))
print('FRESH_AND_PEER_FILES_UNCHANGED', len(frozen))
