from pathlib import Path
from collections import Counter
import csv
import datetime
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation3_foundations'
source = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
classification = (OUT / 'S6_SERIES_PUBLISH_II_smooth_fibres.tex').read_text()
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
fields = ['change_id', 'type', 'statement_id', 'old_location', 'old_page',
          'new_location', 'new_page', 'old_text', 'new_text', 'reason', 'review_status']
rows = []


def owner_block(label):
    loc = source.index(r'\label{' + label + '}')
    a = source.rfind(r'\begin{proposition}', 0, loc)
    b = source.index(r'\end{proof}', loc) + len(r'\end{proof}')
    return source[a:b]


def record(old, new, kinds, owner, location, reason):
    for kind in kinds.split(','):
        rows.append(dict(change_id=f'II-C3-PREMISES-{len(rows)+1:03}', type=kind,
                         statement_id=owner, old_location=location,
                         old_page='cp35; final page concordance pending', new_location=location,
                         new_page='integrated build pending', old_text=old, new_text=new,
                         reason=reason,
                         review_status='Full source and receiving owner proof read and compared; scoped dependency transport supplied.'))


def replace(text, old, new, kinds, owner, location, reason):
    assert text.count(old) == 1, (owner, location, text.count(old))
    record(old, new, kinds, owner, location, reason)
    return text.replace(old, new)


# C.3.10 uses the general published analytic comparison, not the conclusion
# of the later torus-obstruction proposition D.2.3.
classification = replace(classification,
    r'\SeriesRef{cdp:eq:C.PK.4}, \SeriesRef{cdp:st:D.2.3}, \SeriesRef{cdp:eq:C.PK.5}',
    r'\SeriesRef{cdp:eq:C.PK.4}, \SeriesRef{cdp:eq:C.PK.5}',
    'D14', 'cdp:st:C.3.10', 'Primary Kodaira dependency declaration',
    'The proof invokes Steenbrink directly at the precise general analytic scope. D.2.3 has a torus obstruction conclusion; its proof cited the same general comparison. Remove that indirect forward edge while keeping the existing Steenbrink citation and all true proof inputs.')
classification = replace(classification,
    r'''\item Resolve all exceptional
fibres by successive blowups with smooth centres contained
in those fibres, writing''',
    r'''\item Resolve the union of the exceptional-fibre supports to
normal crossings by successive blowups with smooth centres contained
in those fibres, writing''',
    'D22', 'cdp:st:C.3.10', 'Primary Kodaira proof: logarithmic resolution',
    'Make explicit the normal-crossings property of the embedded resolution already required by the following logarithmic complex. The same vertical smooth-centre blowups, maps rho and h, and unchanged smooth fibres are used; their structure-sheaf direct images and the isomorphism C.PK.5 are unchanged.')
classification = replace(classification,
    r'''positive degree. The exact analytic comparison of \ref{cdp:st:D.2.3},
namely \cite[Theorem~2.18 and \S\S2.19--2.21]{Steenbrink1976},
applies to this analytic resolution with all its fibre multiplicities. It gives the logarithmic
de Rham bundle''',
    r'''positive degree. The analytic comparison of
\cite[\S2.1, p.~234; Theorem~2.18, pp.~237--238;
\S2.19 and Proposition~2.20, pp.~238--239; Theorem~2.21, p.~239]{Steenbrink1976}
applies on each base disc: the total space is smooth, the map is
proper and smooth off the central value, and the full central fibre
has normal-crossings support with its positive multiplicities.
It gives the logarithmic de Rham bundle''',
    'D14,D18', 'cdp:st:C.3.10', 'Primary Kodaira proof: direct analytic comparison',
    'Original journal scans actually opened and read on pp.231,233,234,237–239. Section2.1 has the stated complex-manifold/proper-map/normal-crossings hypotheses, with no restriction to torus fibres. Theorem2.18 gives local freeness and canonical fibre base change; Section2.19 gives the connection, Proposition2.20 gives residue spectrum [0,1), and Theorem2.21 gives exp(-2pi i Res). The receiving complex is exactly the quotient defined in Section1.4. Its canonical projection to O[0], followed by the already proved R2 blowup identification, is unchanged. The noncanonical central topological identification mentioned in Section2.17 is not used to define this projection.')

old_torus = owner_block('cdp:st:D.2.7')
torus = old_torus
torus = replace(torus,
    r'\StatementRecord{cdp:st:D.2.7}{proved}{01GE}{\SeriesRef{cdp:st:D.2.5},',
    r'\StatementRecord{cdp:st:D.2.7}{proved}{01GE}{\SeriesRef{cdp:st:E1},',
    'D12,D14', 'cdp:st:D.2.7', 'Torus construction: dependency declaration',
    'The sign theorem was mentioned only in a concluding comparison and is not an input to any construction or proof step. That comparison moves to D.2.5. The duplicated vertical-divisor/field proof is replaced below by its earlier owner E1 at the same smooth compact connected, H2(real)=0, Kahler-general-fibre scope.')
torus = replace(torus,
    r'''curve. Consequently the trivial-monodromy class in D.2 is
nonempty, and equality in the unrestricted sign theorem
\ref{cdp:st:D.2.5} is attained.''', 'curve.',
    'D05,D06,D11,D12,D14', 'cdp:st:D.2.7', 'End of compact torus construction statement',
    'The existence theorem itself states all defining data, identity integral monodromy and c3=0. The comparison with the sign bound becomes one explicit equality clause in D.2.5, whose hypotheses are met by this same constructed Y. Remove the obsolete D.2 shorthand and the duplicate nonemptiness recap; no existence, fibre-type, homology or Euler conclusion is removed.')
torus = replace(torus,
    'This proves precisely\nthe surjectivity and the kernel in \\eqref{cdp:eq:D.25}, without a torsion\nambiguity.',
    'This proves the integral surjectivity and kernel in \\eqref{cdp:eq:D.25}.',
    'D02', 'cdp:st:D.2.7', 'Local integral quotient maps',
    'The displayed integral quotients, primitive transgression and free graded terms remain. State their exact conclusion directly.')
torus = replace(torus,
    'nonzero, so these are actual bounding chains in the product',
    'nonzero, so these are bounding chains in the product',
    'D08', 'cdp:st:D.2.7', 'Boundary meridian chains',
    'The same discs and product chains in the same canonical-section trivialization prove the zero maps D.26; remove the process adjective.')

old_matrices = r'''The attached program constructs both full signed
Mayer--Vietoris matrices: their sizes are $15\times15$
and $29\times30$, the first has determinant $+1$, and
all nonzero Smith entries of both are $1$. It also checks
the six-dimensional relation matrix in \eqref{cdp:eq:D.32}.'''
prepared = (ROOT / 'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_D09_D04_batch06_final_v1/S6_SERIES_PUBLISH_II_A2_01GE_after.tex').read_text()
pm = re.search(r'For explicit quotient coordinates,.*?has unit Smith entries as well\.', prepared, re.S)
assert pm
new_matrices = pm.group() + '\nThe program is listed in \\cref{tab:II:programs}.'
torus = replace(torus, old_matrices, new_matrices, 'D09,D22', 'cdp:st:D.2.7',
    'Signed Mayer--Vietoris matrix coordinates',
    'Use the prepared continuation2_A exact quotient-coordinate and basis-order formula, which was read together with its explicit integral change-of-basis output. Q_v has kernel Zv and induces the displayed quotient isomorphism. This states the input maps, signed basis convention, integer elimination method and all original size/determinant/Smith conclusions. No new computation was run. The existing prepared pinned program-table row is supplied for root admission.')

last_start = torus.index(r'\item Finally every effective divisor on $Y$ is vertical.')
last_end = torus.index(r'The universal coefficient theorem also gives', last_start)
old_last = torus[last_start:last_end]
new_last = r'''\item The constructed threefold is smooth, compact and connected,
and \eqref{cdp:eq:D.32} gives $H^2(Y;\R)=0$. Its smooth fibres are
the abelian surface $A$, hence are K\"ahler. The proper map $f$ has
connected fibres. Thus \cref{cdp:st:E1} makes every effective divisor
vertical and identifies the function fields by
$f^*:\mathcal M(\PP^1)\xrightarrow{\simeq}\mathcal M(Y)$.
Consequently $a(Y)=1$.
'''
torus = replace(torus, old_last, new_last, 'D12', 'cdp:st:D.2.7',
    'Last construction proof step: vertical divisors and function field',
    'Read E1 and this entire original proof. Apply E1 with n=3, g=f, C=P1 and the constructed Y. H2(Y;Z)=0 from D.32 gives its real-cohomology hypothesis; A=E×E is projective and hence Kahler; properness and connected fibres were established in step7. E1 gives exactly the original effective-divisor verticality and the pullback field isomorphism, including extension over special values. UCT and every displayed conclusion D.21 remain in the receiving step.')

prepared_map = {}
with (ROOT / 'agents/continuation2_B/D19/S6_SERIES_PUBLISH_II_B2_D19_v1_equation_map.tsv').open() as f:
    for row in csv.DictReader(f, delimiter='\t'):
        if row['old_tag']:
            prepared_map[row['old_tag']] = row['target_label']
equations = []


def convert(match):
    old = match.group()
    tag_match = re.search(r'\\tag\{([^}]+)\}', old)
    if not tag_match:
        return old
    tag = tag_match.group(1)
    label = prepared_map[tag]
    assert r'\label{' + label + '}' in old
    new = old.replace(r'\[', r'\begin{equation}', 1)
    new = new[:-2] + r'\end{equation}'
    new = new.replace(tag_match.group(), '')
    assert old[2:-2].replace(tag_match.group(), '') == new[len(r'\begin{equation}'):-len(r'\end{equation}')]
    record(old, new, 'D19', 'cdp:st:D.2.7', f'Equation {tag}',
           'Convert the tagged bracket display to equation, removing only its manual tag. Formula payload, existing label and permanent target are identical. Existing D19 prepared map confirms the label; root section counter determines the receiving number.')
    equations.append(dict(old_tag=tag, target_label=label, owner='cdp:st:D.2.7',
                          old_environment='bracket', new_environment='equation',
                          formula_comparison='byte-identical after numbering wrappers and manual tag only'))
    return new


torus = re.sub(r'\\\[.*?\\\]', convert, torus, flags=re.S)
assert len(equations) == 12
assert r'\tag{' not in torus
for command in ('label', 'hypertarget'):
    assert Counter(re.findall(r'\\' + command + r'\{([^}]+)\}', old_torus)) == Counter(re.findall(r'\\' + command + r'\{([^}]+)\}', torus))
(OUT / 'S6_SERIES_PUBLISH_II_torus_occurrence_early.tex').write_text(torus + '\n')

# A single later remark owns both substantive former scope paragraphs.
old_scope = r'''\paragraph{Scope of \ref{cdp:st:D.2.6}.}
For a fibration over $\PP^1$ with globally trivial marked
$H^1$ monodromy, the local constructions glue to a smooth
proper torus group family over $\PP^1$. The period map may
be nonconstant, as the explicit family in \ref{cdp:st:D.1.15} demonstrates.
The local filling in \ref{cdp:st:D.2.7} proves that the marked Albanese
map need not extend to the given model. Its inclusion of
a nearby fibre kills the nonzero cycle $w$ in (D.25).
An extension $U\to A\times\Delta$ of the marked fibre
isomorphisms would induce a map on $H_1$ whose composite
with that inclusion is the identity on $H_1(A;\Z)$,
which is impossible because it would send $w$ both to
zero and to $w$. This exact topological obstruction
explains why the extending group family does not imply
nonexistence in D.2.'''
new_scope = r'''\begin{remark}[Extended torus groups and Albanese maps]
\hypertarget{tag-P213}{}\label{rem:II:extended-torus-groups}
\StatementRecord{rem:II:extended-torus-groups}{proved}{P213}{}
Let $f:Y\to\PP^1$ be a proper holomorphic map from a smooth complex
threefold, with connected two-torus fibres over the complement of
a finite set and globally trivial marked $H^1(-;\Z)$ monodromy.
The local group extensions in \cref{cdp:st:D.2.6} glue to a smooth
proper torus group family over $\PP^1$. The marked
period extensions agree on overlaps because they agree on the
smooth locus; their quotients by the same constant lattice therefore
glue. The period map can be nonconstant, as in \cref{cdp:st:D.1.15}.

For the local filling $U\to\Delta$ in \cref{cdp:st:D.2.7}, this
group extension is $A\times\Delta$. An extension
$\alpha:U\to A\times\Delta$ of the marked fibre isomorphisms
would induce the composite
\[
 \Lambda=H_1(A;\Z)\longrightarrow H_1(U;\Z)
       \xrightarrow{\alpha_*}H_1(A\times\Delta;\Z)=\Lambda
\]
equal to the identity. The first arrow is the quotient
$\Lambda\to\Lambda/\Z w$ of \eqref{cdp:eq:D.25}, with $w\ne0$.
Its composite therefore kills $w$, a contradiction. Thus the
marked Albanese map on this filling does not extend to its smooth
group extension.
\end{remark}'''
assert source.count(old_scope) == 1
record(old_scope, new_scope, 'D05,D06,D11,D12,D13,D19',
       'rem:II:extended-torus-groups', 'After the marked torus-period extension',
       'Combine the two original scope discussions into one numbered remark after D.2.6. The global group-family extension and nonconstant-period example remain. The map obstruction is the same exact H1 composite: inclusion kills the primitive nonzero w by D.25, while an extending marked fibre isomorphism would induce identity. The repeated post-D.2.7 comparison is removed in favour of this owner. Replace literal D.25 by its existing equation label and remove obsolete D.2 question shorthand.')

old_literature = r'''\paragraph{Literature comparison.}
The construction uses explicit principal elliptic bundles,
one ordinary point blowup in each local quotient surface,
and the specified integral clutchings. Searches for
``complex threefold, Kodaira, Hopf, fibre, monodromy'',
``algebraic dimension, $S^3\times S^3$, torus'', and
``complex torus, blow-up, principal elliptic bundle,
degeneration'' did not identify this marked example in
the sources inspected. 
The complete construction and integral calculation above
are independent of a literature classification of such
fillings. They also show why extending the group family
of \ref{cdp:st:D.2.6} does not imply extension of its marked Albanese
map on the original model: in \eqref{cdp:eq:D.25} one integral
one-cycle of the smooth torus is killed although its
linear monodromy is the identity.'''
assert source.count(old_literature) == 1
record(old_literature, '', 'D01,D02,D08,D12,D13', 'cdp:st:D.2.7',
       'Literature-search paragraph after the torus construction',
       'Remove search queries, bounded negative-search narration and the proof-independence disclaimer from the mathematical body. The construction remains in full. The sole mathematical comparison, concerning extension of the Albanese map, is retained and proved once by the exact H1 composite in P213 after D.2.6.')

old_sign_tail = r'''The fibres may have arbitrary singularities and arbitrary
multiplicities. In particular this proves the sign assertion of
D.2 for a holomorphic algebraic reduction; no existence assertion
is required for the conclusion.'''
new_sign_tail = r'''The fibres may have arbitrary singularities and arbitrary
multiplicities. The construction in \cref{cdp:st:D.2.7} attains
$c_3(Y)=0$ and $b_3(Y)=2$.'''
assert source.count(old_sign_tail) == 1
record(old_sign_tail, new_sign_tail, 'D02,D05,D06,D11,D12,D14',
       'cdp:st:D.2.5', 'Sign theorem: equality occurrence',
       'This is the unique later owner of the comparison formerly repeated in D.2.7 and after the sign proof. The earlier construction has smooth compact connected Y, b1=b2=0, proper connected-fibre torus map and identity integral, hence rational, monodromy; its computed c3=0,b3=2 satisfy the two equalities. Arbitrary singularity and multiplicity scope remains. No use of the sign theorem enters the construction proof.')
old_sign_orphan = r'''The sign result uses the analytic logarithmic comparison of
Steenbrink. The explicit compact construction in \ref{cdp:st:D.2.7} proves
that the stated class is nonempty and attains $c_3=0$.
Together these results settle both the existence and the sign
questions in D.2.'''
assert source.count(old_sign_orphan) == 1
record(old_sign_orphan, '', 'D05,D06,D12,D13', 'cdp:st:D.2.5',
       'Paragraph after the sign proof',
       'The proof already cites the precise logarithmic input through D.2.3. The equality/occurrence comparison now appears once in the sign statement; remove the duplicate and obsolete question shorthand.')

classification = replace(classification,
    r'\subsection{Hopf bundles and complete classification}\label{sec:II:fibre-classification}',
    r'\subsection{Compact torus and Hopf fibrations}\label{sec:II:fibre-classification}' + '\n\n' + torus,
    'D14', 'sec:II:fibre-classification', 'Earlier occurrence-construction placement',
    'Place the complete explicit torus construction immediately before the complete Hopf construction, and both before C.3.11. All genuine inputs of D.2.7 are self-contained except the earlier E1 application. Its old later copy must be removed by the supplied exact guard.')
classification = replace(classification,
    r'\begin{proposition}[Complete classification and full-fibre cohomology]',
    r'\subsection{Complete classification and cohomology}\label{sec:II:complete-fibres}' + '\n\n' + r'\begin{proposition}[Complete classification and full-fibre cohomology]',
    'D14', 'cdp:st:C.3.11', 'Final classification subsection',
    'The final theorem follows all individual exclusions and both occurrence constructions. Its exact hypotheses, all-fibre cohomology and proof are unchanged.')
(OUT / 'S6_SERIES_PUBLISH_II_smooth_fibres_with_inputs.tex').write_text(classification)
(OUT / 'S6_SERIES_PUBLISH_II_extended_torus_groups_remark.tex').write_text(new_scope + '\n')

guards = [
    dict(owner='cdp:st:D.2.7', action='delete old later owner; receiving copy is in smooth_fibres_with_inputs', old=old_torus, new=''),
    dict(owner='cdp:st:D.2.7', action='delete old post-construction literature/scope paragraph', old=old_literature, new=''),
    dict(owner='rem:II:extended-torus-groups', action='replace scope paragraph after D.2.6', old=old_scope, new=new_scope),
    dict(owner='cdp:st:D.2.5', action='own the equality comparison in the sign statement', old=old_sign_tail, new=new_sign_tail),
    dict(owner='cdp:st:D.2.5', action='remove duplicate after-proof comparison', old=old_sign_orphan, new=''),
]
(OUT / 'S6_SERIES_PUBLISH_premise_placement_guards.json').write_text(json.dumps(guards, ensure_ascii=False, indent=2) + '\n')
program_rows = (ROOT / 'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_D09_D04_batch06_final_v1/S6_SERIES_PUBLISH_II_A2_D09_D04_batch06_Programs_rows_after.tex').read_text().splitlines()
program_row = next(row for row in program_rows if r'\cref{cdp:st:D.2.7}' in row)
(OUT / 'S6_SERIES_PUBLISH_torus_occurrence_program_row.tex').write_text(program_row + '\n')


def write_tsv(name, header, values):
    with (OUT / name).open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(values)


write_tsv('S6_SERIES_PUBLISH_premises_defects.tsv', fields, rows)
write_tsv('S6_SERIES_PUBLISH_premises_equation_map.tsv', list(equations[0]), equations)
event_fields = ['statement_id', 'date', 'who', 'type', 'outcome', 'event_id', 'phase',
                'source_file', 'source_row', 'source_event_type', 'evidence_group',
                'publish_input_file', 'publish_input_row', 'date_utc', 'where']
event_notes = {
    'cdp:st:C.3.10': 'Complete original and receiving proof read; direct Steenbrink application checked against actual primary scans. Exact logarithmic quotient, normal-crossings modification, canonical projection, R2 blowup map and zero-residue implication retained. The torus-obstruction proposition is no longer an indirect forward premise.',
    'cdp:st:D.2.3': 'Complete twelve-step proof read. Its general analytic comparison inputs were opened on original journal pages 231,233,234,237–239 and matched to the normal-crossing quotient, canonical fibre base change, connection, residue spectrum and exponential formula. Its torus obstruction statement and proof are unchanged.',
    'cdp:st:D.2.7': 'Complete original and receiving twelve-step construction proofs read and compared. The free elliptic quotient, normal-crossing central fibres, marked local homology, translation clutchings and signed Mayer–Vietoris elimination are retained. Prepared exact quotient coordinates expose the former program claim. The final field argument is an exact application of the earlier E1. Every original label and target survives; the twelve equation payloads are unchanged after wrapper removal.',
    'cdp:st:E1': 'Complete E1 proof reread as the receiving owner for D.2.7: the constructed smooth compact connected threefold has H2(real)=0 and Kahler general fibre A; properness and connected fibres have already been proved. Its pullback field isomorphism supplies exactly the removed duplicate divisor/descent argument.',
    'cdp:st:D.2.5': 'Complete original sign statement and seven-step proof read. Only the comparison tail is edited: the already proved earlier D.2.7 example meets every sign hypothesis and attains both equalities. No input to its sign proof is moved or removed.',
    'cdp:st:D.2.6': 'Complete original five-step marked-period/group-family extension proof and its scope paragraph read. The global gluing, nonconstant-period example and exact H1 obstruction are transferred to one numbered remark; the extension proposition and proof are unchanged.',
    'rem:II:extended-torus-groups': 'Complete receiving remark read against both original scope paragraphs and D.2.6/D.2.7. Period extensions agree on overlaps and use the same constant lattice. In the local filling, the quotient Lambda to Lambda/Zw cannot have a left inverse sending the nonzero w to itself; this is the exact obstruction already proved in the old paragraph.',
}
events = []
for owner, note in event_notes.items():
    identifier = 'publish:c3:premises:' + owner
    events.append(dict(statement_id=owner, date=now[:10],
                       who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 foundations',
                       type='used and rechecked in this run',
                       outcome=note + ' Exposed editorial/source comparison only; no independent re-proof, computation rerun or final PDF credit.',
                       event_id=identifier, phase='publication premise placement and proof comparison',
                       source_file='agents/continuation3_foundations/S6_SERIES_PUBLISH_premises_CHECK_EVENTS.tsv',
                       source_row='', source_event_type='used and rechecked in this run', evidence_group=identifier,
                       publish_input_file='', publish_input_row='', date_utc=now,
                       where='Early logarithmic input and torus occurrence; later equality and Albanese comparison owners'))
write_tsv('S6_SERIES_PUBLISH_premises_CHECK_EVENTS.tsv', event_fields, events)

progress = []
for unit in ('cdp:st:D.2.7', 'rem:II:extended-torus-groups'):
    for n in range(1, 26):
        status = 'done'
        basis = 'Complete unit read against all 25 defect types; changes logged individually with exact maps and proof comparison.'
        if n in (10, 16):
            basis = 'Prior D10/D16 closures preserved; the new P213 owner has a mathematical title and prints only its permanent tag.'
        elif n == 17:
            basis = 'Explicit marked construction and primitive homology maps retained; the repeated vertical-divisor proof is assigned to E1, whose full proof and exact hypotheses were read.'
        elif n == 19:
            basis = 'All twelve old manual tags use their prepared existing labels with unchanged formula payloads; literal D.25 is transported to eqref. Root final numbering/build pending.'
        elif n in (14, 24):
            status = 'open'
            basis = 'Concrete receiving fragment and exact deletion/replacement guards supplied. Root must admit the single earlier D.2.7 owner, later P213 owner and front-matter concordance.'
        progress.append(dict(unit=unit, row=f'D{n:02}', status=status, basis=basis))
    progress.append(dict(unit=unit, row='restructuring', status='open',
                         basis='Exact early/later owner placement complete in the supplied fragment and guards; root integration remains.'))
write_tsv('S6_SERIES_PUBLISH_premises_unit_progress.tsv', ['unit', 'row', 'status', 'basis'], progress)

print(f'{len(rows)} defect rows; {len(events)} exposed readings; 12 equation conversions; P213 newly numbered.')
print('Use smooth_fibres_with_inputs in place of the earlier classification fragment, then apply the five exact later-source guards and admit the supplied program row.')
print('D.2.3 stays intact. C.3.10 cites the opened general analytic comparison directly; D.2.7 precedes C.3.11 with E1 as its only external Paper-II proof input.')
