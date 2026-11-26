#!/usr/bin/env python3
"""Stage LP's complete comparison, two exact guards and typed check records.

Canonical and frozen mathematical inputs are read-only. The proof guard
contains both original proof environments, including their separator.
This program performs source checks and writes local proposals only.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import csv
import re

ROOT = Path(__file__).resolve().parent.parent
STAGE = ROOT / 'agents/continuation7_iii_weighted_cups_receiving'
OLD = ROOT / 'agents/continuation7_iii_weighted_cups_root'
P = 'S6_SERIES_PUBLISH_III_02LP'
ID = 'maps:src:D.2.48'
NOW = datetime.now(timezone.utc).isoformat()
FRESH = '2026-11-25T04:06:19+00:00'
RELEASE = '2026-11-25T04:09:11.877635+00:00'
WHO = ('GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical reasoning '
       'effort not separately exposed; continuation seven LP receiving check')


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
    with (STAGE / name).open('w', encoding='utf8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter='\t',
                           lineterminator='\n')
        w.writeheader()
        w.writerows(rows)


canonical_path = ROOT / 'S6_SERIES_PUBLISH_III.tex'
canonical_bytes = canonical_path.read_bytes()
assert digest(canonical_bytes) == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
canonical = canonical_bytes.decode()
os = env((OLD / f'{P}_released_statement.tex').read_text(), 'theorem')
released_proof = (OLD / f'{P}_released_proof.tex').read_text()
op = released_proof[released_proof.index(r'\begin{proof}'):].rstrip('\n')
assert digest(op) == '576e201fe7ec50fc93f3a9844c7e48d8a7dee5ff4c15b1f15911a8af33b0a5b8'
assert len(op.splitlines()) == 556
assert len(re.findall(r'\\begin\{proof\}', op)) == op.count(r'\end{proof}') == 2
assert len(re.findall(r'^\\item\b', op, re.M)) == 29
receiver = STAGE / f'{P}_receiving.tex'
new = receiver.read_text()
assert digest(new) == 'db7f0665769fd04524de31d85001d1098f737c4d07de3074adae2e3cf6462c19'
ns, np = env(new, 'theorem'), env(new, 'proof')
assert new.count(r'\begin{proof}') == new.count(r'\end{proof}') == 1
old = os + '\n\n' + op
comparison = (STAGE / f'{P}_comparison.md').read_text()
for head, tail, count in [
    ('## 3. Every item in the first original proof',
     '## 4. Every item in the second original proof', 11),
    ('## 4. Every item in the second original proof',
     '## 5. Independent refined-class check', 18),
]:
    table = comparison.split(head, 1)[1].split(tail, 1)[0]
    assert re.findall(r'^\| (\d+) \|', table, re.M) == list(map(str, range(1, count+1)))
assert 'No D25 or D27' in comparison
assert 'untagged' in comparison and 'one-proof' in comparison

guards = []
shadow = canonical
for kind, before, after in [('statement', os, ns), ('proof', op, np)]:
    assert canonical.count(before) == 1, kind
    position = canonical.index(before)
    start = canonical[:position].count('\n') + 1
    end = start + before.count('\n')
    if kind == 'proof':
        assert (start, end) == (19605, 20160)
    guards.append((kind, before, after, start, end))
    shadow = shadow.replace(before, after, 1)
for _, before, after, _, _ in reversed(guards):
    assert shadow.count(after) == 1
    shadow = shadow.replace(after, before, 1)
assert shadow.encode() == canonical_bytes

for command, count in [('label', 31), ('hypertarget', 31), ('tag', 30)]:
    pattern = r'\\' + command + r'\{([^}]+)\}'
    a, b = re.findall(pattern, old), re.findall(pattern, new)
    assert len(a) == len(b) == len(set(b)) == count
    assert sorted(a) == sorted(b), command
triples = r'\\tag\{([^}]+)\}\s*\\hypertarget\{([^}]+)\}\{\}\s*\\label\{([^}]+)\}'
assert sorted(re.findall(triples, old)) == sorted(re.findall(triples, new))
assert len(re.findall(triples, new)) == 30

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
assert cites == {'manZhubr75', 'manCartan1955EML', 'ffThomas56',
                 'ffZhubr13', 'mapsKaplan79'}
assert cites <= keys
for bad in (r'\StatementRecord', r'\path{', r'\subsubsection*', 'code/',
            'records/', '.json', 'SHA256', 'fresh', 'historical'):
    assert bad not in new, bad
assert r'\emph{The characteristic circle bordism.}' not in new

frozen = {
    'agents/continuation7_iii_weighted_cups_root/' + P + '_fresh_derivation.md':
        '9554965e32768a0258adc3175bf9b2dc35522f20c60ca31fab0cd548ce91370d',
    'agents/continuation7_iii_weighted_cups_root/' + P + '_circle_characteristic_bordism.md':
        '08267a0aefbe6dacf227c87010daa4b305e7b68363715b93da27f5921b8f7910',
    'agents/continuation7_iii_weighted_cups_root/' + P + '_refined_spin_primary.md':
        '968a116e88c51c0400c66905eac3cd4881e200422e240d108dff32ab3081c484',
    'agents/continuation7_iii_weighted_cups_root/' + P + '_finite_character_obstruction.md':
        'd67a22c66cb4fa9427ddc27e365dae7d083562fda58949d4fdbc4a26a3a2dc39',
    'agents/continuation7_iii_primary_powers/' + P + '_post_exposure_auxiliary_review.md':
        '2326f9165875400355fb9562b7636009c8f4d991c359a4bb77c42c2a0812977e',
    'agents/continuation7_iii_primary_powers/S6_SERIES_PUBLISH_III_divided_power_primary_reading.md':
        '6d0b7082a3582a25af2109f06391983374eaefacdf17f2d2e30ad29c220ebce1',
    'code/S6_SERIES_PUBLISH_c7_lp_fresh_geometry.py':
        'db633dbd42b9b8eebc8c1e503ee31cf466a2ca421ede47ce0bf79dbdc9642381',
    'code/S6_SERIES_PUBLISH_c7_lp_fresh_geometry.out':
        '580ec2c96f714d539bf258733d58fde4fbdbad4719652903e13fae526b1c227c',
    'code/S6_SERIES_PUBLISH_c7_lp_circle_bordism.py':
        'a80090239bc2e1918bdc92db74c6642f0bc19d6006765e327884c4987fb4a498',
    'code/S6_SERIES_PUBLISH_c7_lp_circle_bordism.out':
        '56fe9b05f22fb8836858624f0c83149afb8f6e97b00a561a0ce4f36886517e04',
    'code/S6_SERIES_PUBLISH_c7_lp_finite_character.py':
        '0f063869abbfa4d4d6d710b4e5492e37743d5b7f91004a6d36b9091592c2fe8d',
    'code/S6_SERIES_PUBLISH_c7_lp_finite_character.out':
        'b5d768f273f9a50b82eacea55353e4066f93a35f0b6e44a34e4bc99b9c5d0152',
    'code/S6_SERIES_PUBLISH_c7_lp_aux_comparison_v002.py':
        'd794440b96e09aef6e91b4411c8b1f4be6ee90a357e079960ffc11f5b74a9776',
    'code/S6_SERIES_PUBLISH_c7_lp_aux_comparison_v002.out':
        '1dedfaa066cc6ab3e45b5a9c1e162b4f271a4a17233c63fbe50d464faa2153cd',
    'code/S6_SERIES_PUBLISH_c7_lp_historical_thomas.py':
        '8e080c4fb00575274b8032e38037dbf8c13bd2d56394e4ef9117f8f9fd46ec2f',
    'code/S6_SERIES_PUBLISH_c7_lp_historical_thomas_new_run.out':
        '525be082a94921525339e618614c5e5ea7f229080da25c213f4bf975b273c38d',
    'agents/continuation7_iii_primary_powers/' + P + '_historical_thomas_new_run.json':
        '0285f408f85c335f31513cce8971ba32c189c15a0a7406dee2456da407ae265d',
}
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
    defects.append(dict(change_id=f'c7-III-02LP-{suffix}', type=kind,
        statement_id=ID, old_location=f'S6_SERIES_PUBLISH_III.tex:{line}',
        old_page='', new_location=str(receiver.relative_to(ROOT)),
        new_page='pending final typeset page concordance', old_text=before,
        new_text=after, reason=reason,
        review_status='staged; root admission, source application and final page review pending'))


defect('D22', 'marked-integral-quotients',
    part(op, 'The determinant condition implies', 'It is primitive because adjoining its relation gives $H_1(X)=0$.'),
    part(np, 'The quotient map sends', 'Thus the cusp meridian $x\'_0+x\'_1$ has primitive value $P$.'),
    'Retain the true primitive group assertion with the exact exterior functional, integral inverse and determinant-one basis. The receiver also supplies all four normal-column preimages and the primitive cusp augmentation. These are justification repairs, not a refutation of the original groups.')
defect('D22', 'actual-ruling-period-map',
    part(op, 'The common ruling in the $d$-period cusp', 'There is no division by $d$ or saturation at this step.'),
    part(np, 'The notation in the statement is', 'and applies in every\n$\\gamma$ component of the degree-$d$ period cover.'),
    'Give the exact exceptional-label permutation, KI period substitution and inverse, current-unit annulus/cylinder chains and actual quotient marking. The ruling equality is in the specialization quotient, with positive xi-value one; it is not declared to be an equality of distinct free dP6 curve classes.')
defect('D22', 'complete-differential-kernel',
    part(op, 'The abstract rank-two\nkernel $V$', 'at a triple point they are $(x,-y,0)$ and $(x,0,-z)$.'),
    part(np, "Indeed $yzA+xzB+xyC=0$", 'is the same divisibility argument.'),
    'Retain both displayed local bases and prove their full analytic generation by divisibility. Explain the nonzero abstract scalar section at the critical strata and the actual smooth frame construction. No original kernel claim is refuted.')
defect('D22', 'global-line-full-gauge',
    part(op, 'At weight one the regular bundle $V_1$', 'fibre part and zero on every graph generator.'),
    part(np, 'For the actual core monodromies', 'This constructs the integral\ncore class at every weight.'),
    'Construct the global line from the preserved quadratic refinement, real lattice cocycle, connection, scalar-one monodromy lifts and origin sections. This proves all five swept values and their full boundary marking rather than assigning them from a fibre functional alone.')
defect('D20,D22', 'support-gauge-and-units',
    display(op, 'D.WI17'),
    part(np, r'\psi(r,s)=-\frac{r(r-1)}2+3s(s-1)=\phi(r,s)-3s.',
         'and collar, including every period unit.'),
    'Preserve the original support through the explicit map zeta_psi=z2^{-3}zeta_phi and inverse z2^3. The multiplier changes by q^{-3 lambda_s} times the actual unit^{-3}; regular Cartier frames coincide. This proves the exact conversion from the fresh Gaussian support without changing the original numerical line degrees.')
defect('D22', 'finite-class-uniqueness',
    part(op, 'The circle\nGysin sequence therefore supplies an extension', 'class $u\\in H^2(X;\\mathbb Z/d)$.'),
    part(np, 'For an exact global extension map,', 'identifies this functional with the same glued class $u$.'),
    'Retain the full Gysin/root-loop extension and supply its exact relative H2 argument: the Seifert inverse makes H2(W) to H2(X) onto and every kernel class is the actual normal Thom image. Thus the chosen line determines the precise finite class and free/cyclic marking.')
defect('D22', 'finite-equivariant-line',
    part(op, 'The difference of any two equivariant lifts', 'read from any toric equivariant lift of \\eqref{maps:eq:D.TP1}.'),
    part(np, 'Here the same $h$ occurs on every component.', 'formula as well.'),
    'Prove the finite magnetic lift for N dividing6d and compare it with the Borel coefficient class by the actual Z^2 times C_N fundamental group and its fixed sections. This supplies the common-character conclusion across the whole fixed locus with all affine multiplicities.')
defect('D22', 'complete-coefficient-localization',
    part(op, 'Apply equivariant localization with coefficients', 'a unit after inverting $t$.'),
    part(np, 'Restrict to $C_N$ with $N=3d$', 'self-intersection formula on each fixed curve.'),
    'Use the proved actual finite lift and its full coefficient ring. The free complement, normal Euler units and explicit Thom inverse justify localization, including all nonidentity powers and the coefficient injection on constants.')
defect('D22', 'integral-cyclic-target',
    part(op, "For degree six, Zhubr's epimorphism", '$[\\mathbb {CP}^3]$ for every $d$.'),
    part(np, "In Cartan's integral model", 'The Chinese\nremainder isomorphism gives \\eqref{maps:eq:D.WI22} for all $d$.'),
    'Prove the full integral low-degree target from the primary elementary complexes, including the p=2 extra pair, and the positive divided generator. Retain the CP3 upper/lower bounds and complete mixed detector inverse. The same group conclusion stands; no theorem refutation is alleged.')
defect('D22', 'finite-detector-inverse',
    part(op, 'A primitive generator has the root-loop exponent inverse to', 'The normal three-frame is $\\delta$ followed by the two real\ndirections of $L$.'),
    part(np, 'Choose $A,K$ with $Am_1+Kn_1=1$', 'so it identifies the two stated framings.'),
    'Supply the primitive base generator and inverse, both actual monodromies, integral Smith changes/inverses and the exact projection S to TN with its inverse. This preserves the original group and parity scope for every affine cap parameter.')
defect('D22', 'actual-tangent-parity',
    part(op, 'For an actual parallelization of a closed oriented', '\\eqref{maps:eq:D.WI9} therefore gives reference parity'),
    part(np, r'\emph{The actual tangent-parallelization parity.}',
         'For \\eqref{maps:eq:D.WI9} that dimension is two, so'),
    'Give the prescribed-spin Kaplan filling and the complete Spin(4) degree calculation, Euler parity and even mod-two intersection rank. The original value 1+b1(F2), hence epsilon1, is proved rather than inferred from an unspecified framing statement.')
defect('D22', 'ambient-sphere-and-transgression',
    part(op, "Indeed, choose Zhubr's admissible three-frame", 'unproved general change-of-frame conjecture.'),
    part(np, 'An odd multiple of $N$', 'initial detector.'),
    'Retain and prove all original auxiliary steps: exact odd multiple, ambient spin two-handle discs, first-normal extension, actual admissible quaternion frame, factor-two normal-framing morphism, and integer transgression before division. The general unproved variation formula is not used.')
defect('D20', 'duality-convention',
    '$2P_{\\rm ref}=\\lambda=0$',
    '$2P_{\\rm ref}=\\operatorname{PD}\\lambda=0$',
    'Make the homology/cohomology Poincare-duality map explicit. The receiver also states that linking against the displayed degree-four dual class means linking with its dual two-cycle. The refined class and its value do not change.')
defect('D22', 'marked-classification-source-scope',
    part(op, "These are exactly the four invariants in", '\\cite[Theorem 1]{manZhubr75}.'),
    part(np, "Zhubr's Theorem 5", 'have the stipulated images in both directions.'),
    'Apply the exact marked bordism injection and Theorem3 with Section4.1 zero-free-H3 recognition; display the group marking and inverse. The primary pp793–794 literally print H2, while p809 supplies the proof-level H3 scope. This repairs the attribution without changing the theorem or alleging that classification theory is false.')
defect('D09', 'historical-program-paragraph',
    part(op, 'The universal integer identities, support slope,', 'comes from \\eqref{maps:eq:D.TP7}, not that finite range.'),
    part(np, 'For arbitrary integers $d>0,\\lambda_0$', 'The mixed coordinates retain the full modulus $D_2$ proved above.'),
    'Move the historical path and bounded execution bookkeeping to the comparison/source record and later program table. The receiver contains the exact all-integer polynomial proof. The pinned historical source was actually rerun once after release, with every source/output/JSON field read; the 4920 cases remain supplementary.')
defect('D10', 'machine-header',
    next(s for s in os.splitlines() if s.startswith(r'\StatementRecord')),
    r'\textnormal{\small tag 02LP.}',
    'Print the small tag and preserve all permanent labels and targets. Dependencies and primary citations occur at the mathematical steps; machine check navigation stays in check files.')
defect('D14', 'one-complete-proof',
    r'\begin{proof}[Proof of the complete invariant and classification]',
    r'\begin{proof}',
    'Merge both original proof environments into one ordered proof with every old auxiliary. Root also identified that assemblyv02 duplicated the refined-P proof; v03 removes its untagged108-line independent circle-bordism block. The complete frozen circle/refined proof remains independent check evidence. All30 equation triples and every original detector/framing assertion remain; classification follows its single refined-P proof.')
defect('D14', 'repeated-pure-cube-heading',
    r'\subsubsection*{The full Pontryagin cube of the weighted Engel torsion class}',
    r'\emph{The finite lift and the common fixed-point characters.}',
    'Consolidate the inserted subsection and repeated support lead-in into the proof sequence. Preserve D.TP1 with the exact gauge/component restriction and retain every later pure-cube identity.')
defect('D23', 'etale-accent',
    'degree-$d$ etale period cover',
    r"degree-$d$ \'etale period cover",
    'Restore the accent without changing the covering, its degree or its permitted graph/cusp domain.')
defect('D02', 'classification-defence',
    'by an applied complete classification, rather than by\nordinary cohomology or an asserted connected-sum model.',
    'Thus every adjusted free generator and the positive cyclic generator\nhave the stipulated images in both directions.',
    'State the actual marked classification and induced inverse maps positively, retaining all invariant data and existence statements.')
assert not any('D25' in d['type'] or 'D27' in d['type'] for d in defects)

events = []
event_name = f'{P}_CHECK_EVENTS.tsv'


def event(kind, suffix, phase, source, group, outcome, when=NOW):
    row = len(events) + 2
    events.append(dict(statement_id=ID, date=when[:10], who=WHO, type=kind,
        outcome=outcome, event_id=f'publish:c7:III:02LP:{suffix}', phase=phase,
        source_file=source, source_row='1', source_event_type=kind,
        evidence_group=f'publish:c7:III:02LP:{group}',
        publish_input_file=str((STAGE / event_name).relative_to(ROOT)),
        publish_input_row=str(row), date_utc=when,
        where=str((STAGE / f'{P}_comparison.md').relative_to(ROOT))))


event('targeted proof check', 'root-fresh-complete', 'before root original exposure',
    'agents/continuation7_iii_weighted_cups_root/' + P + '_fresh_derivation.md; '
    'agents/continuation7_iii_weighted_cups_root/' + P + '_circle_characteristic_bordism.md',
    'root-fresh',
    'Root derived the complete all-weight and all-good-parameter theorem from the exact claim-only packet and disclosed admitted/primary inputs. Explicit integral quotient maps, primitive ruling, global unit-retaining line, finite lifts, all coefficient detectors, actual circle characteristic bordism, Gamma-to-P morphism and marked zero-free-H3 recognition are proved with inverses. The earlier finite-character obstruction assigns no manifold P value. Root fully read the final586+323+196 lines and all retained programs/streams before individual release; source boundaries and bounded peer inputs are recorded in the root fresh review.', FRESH)
event('computation or formal certificate', 'root-fresh-symbolic-maps',
    'before root original exposure',
    'code/S6_SERIES_PUBLISH_c7_lp_fresh_geometry.py; code/S6_SERIES_PUBLISH_c7_lp_circle_bordism.py; code/S6_SERIES_PUBLISH_c7_lp_finite_character.py',
    'root-fresh',
    'Root authored and read all new source and output. Exact geometry/inverse identities,1386 supplementary filling cases, full fan degrees and universal cube divisibility are checked. The circle program proves the exact ring/Gamma identity and160 supplementary coefficient cases. The separate24-case character exploration retains its obstruction-only scope. Both earlier failed geometry attempts, partial stdout and tracebacks are retained and read; Boolean parity and exact Rational coefficients repair them. All successful separate stderr streams exist and are empty. Unbounded geometry is supplied by the written proofs.', FRESH)
event('used and rechecked in this run', 'bounded-pre-release-peer-review',
    'post-derivation and before original exposure',
    'agents/continuation7_iii_primary_powers/' + P + '_bounded_peer_review.md; '
    'agents/continuation7_iii_residual_two_primary/' + P + '_bounded_bordism_review.md',
    'bounded-peer',
    'The disclosed peer reviews check the root global-line/fixed-locus argument and every quotient, orientation, coefficient and tangent map of the circle bordism. The d1 endpoint and explicit Hermitian Riesz map were incorporated before freeze. These are bounded post-derivation reviews, not another independent fresh derivation or historical-program check.', FRESH)
event('used and rechecked in this run', 'complete-original-auxiliary-derivation',
    'after individual original release',
    'agents/continuation7_iii_primary_powers/' + P + '_post_exposure_auxiliary_review.md',
    'post-exposure-auxiliaries',
    'KS compared all11+18 original proof items and every auxiliary. The exact phi-to-psi gauge/current units, KI period substitution, differential generation/Bott residue, both finite-IV Smith maps, prescribed-spin Kaplan parity, actual Thom linking, embedded torsion sphere, admissible frame and relative transgression are proved. The whole663-line note was read by author, root and receiving checker. Every original mathematical conclusion stands; no refutation is claimed.')
event('computation or formal certificate', 'historical-thomas-new-run-and-auxiliary-maps',
    'after individual original release',
    'code/S6_SERIES_PUBLISH_c7_lp_historical_thomas.py; code/S6_SERIES_PUBLISH_c7_lp_aux_comparison_v002.py',
    'post-exposure-auxiliaries',
    'One actual isolated run of the exact pinned54-line historical source returned0 and produced the retained new stdout, empty stderr and full JSON. Both universal identities and4920 supplementary checks were read. The first auxiliary harness failed only after that successful run at structural symbolic equality; source/stdout/traceback remain. Version002 checks expanded differences, all Thom/Smith inverse and support-factor identities without repeating the historical run. Receiving checker read all source versions, every stream and every JSON field; no fresh-algorithm credit is assigned.')
event('used and rechecked in this run', 'bounded-primary-source-scope',
    'primary consultations before and after original release',
    str((STAGE / f'{P}_source_checks.md').relative_to(ROOT)),
    'primary-scopes',
    'Record exact primary URLs, versions, SHA256s and actual reading scopes for Cartan Exposes7/11, Thomas267–268, Kaplan239–240/243–246, Zhubr1975 and2013. Gamma2010 remains the inherited-axiom indexed-text input of the independent check; no PDF hash or visual credit is invented. Literal H2 printing on793–794 is distinguished from Section4.1 zero-free-H3 recognition. Empty Kaplan retrieval and all other limitations are retained. The receiving checker read the complete primary consultation and auxiliary note; visual readings are attributed to their actual readers.')
event('used and rechecked in this run', 'whole-original-receiver-and-guards',
    'after complete original comparison',
    str((STAGE / f'{P}_comparison.md').relative_to(ROOT)),
    'complete-original-comparison',
    f'After release{RELEASE}, read the entire statement and556-line combined proof, all29 items, every auxiliary and historical assertion. The full same-conclusion receiver preserves31labels,31targets and30exact equation triples. The complete original detector is proved once; root-requested removal of the untagged independent circle proof leaves its frozen check evidence intact. Exact separate guards and source checks pass, with frozen mathematical inputs unchanged. All successful assembly versions/outputs and the pre-mutation comparison-write syntax failure are retained. This event makes no canonical edit, TeX-build, page-review or global-admission claim.')

tsv(f'{P}_replacements.tsv', ['statement_id', 'old_text', 'new_text'],
    [dict(statement_id=ID, old_text=b, new_text=a) for _, b, a, _, _ in guards])
tsv(f'{P}_guards.tsv', ['statement_id', 'kind', 'start_line', 'end_line', 'old_sha256', 'new_sha256'],
    [dict(statement_id=ID, kind=k, start_line=s, end_line=e,
          old_sha256=digest(b), new_sha256=digest(a)) for k, b, a, s, e in guards])
tsv(f'{P}_defects.tsv', ['change_id', 'type', 'statement_id', 'old_location',
    'old_page', 'new_location', 'new_page', 'old_text', 'new_text', 'reason', 'review_status'], defects)
tsv(event_name, ['statement_id', 'date', 'who', 'type', 'outcome', 'event_id',
    'phase', 'source_file', 'source_row', 'source_event_type', 'evidence_group',
    'publish_input_file', 'publish_input_row', 'date_utc', 'where'], events)
assert canonical_path.read_bytes() == canonical_bytes
print('STAGED_AT', NOW)
for k, b, a, s, e in guards:
    print('GUARD', k, f'{s}--{e}', 'old_sha256', digest(b), 'new_sha256', digest(a))
print('IDENTITIES 31 labels;31 hypertargets;30 equation tags;all exact triples preserved')
print('ORIGINAL whole statement;556 combined proof lines;11+18 items;every auxiliary compared')
print('CHECKS unique reversible guards;braces/environments/math;references/citations;17 frozen hashes')
print('ONE_PROOF original detector retained;independent circle proof retained in frozen checks')
print('SCOPE staged source checks;no TeX build,canonical edit,global admission or final page review')
print('DEFECTS', len(defects), 'EVENTS', len(events), 'REFUTATIONS', 0)
for d in defects:
    print('DEFECT', d['type'], d['change_id'], d['old_location'])
for e in events:
    print('EVENT', e['event_id'], e['type'])
files = [receiver, STAGE / f'{P}_comparison.md', STAGE / f'{P}_source_checks.md',
         STAGE / f'{P}_staged_bibliography.bib', STAGE / f'{P}_replacements.tsv',
         STAGE / f'{P}_guards.tsv', STAGE / f'{P}_defects.tsv',
         STAGE / event_name, Path(__file__)]
for f in files:
    print('FILE', f.relative_to(ROOT), f.stat().st_size, digest(f.read_bytes()))
print('CANONICAL_UNCHANGED', digest(canonical_bytes))
