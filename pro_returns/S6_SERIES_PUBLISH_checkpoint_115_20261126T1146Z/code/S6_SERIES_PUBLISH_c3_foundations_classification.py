from pathlib import Path
from collections import Counter
import csv
import datetime
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation3_foundations'
source = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
start = source.index(r'\section{Complete smooth-fibre classification and actual Hopf occurrence}')
stop = source.index(r'\section{Cotangent torsion, conductor and the printed endpoint error}', start)
original = source[start:stop]
x = original
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
fields = ['change_id', 'type', 'statement_id', 'old_location', 'old_page',
          'new_location', 'new_page', 'old_text', 'new_text', 'reason', 'review_status']
rows = []


def record(old, new, kinds, owner, location, reason):
    for kind in kinds.split(','):
        rows.append(dict(change_id=f'II-C3-CLASSIFICATION-{len(rows)+1:03}',
                         type=kind, statement_id=owner, old_location=location,
                         old_page='cp35; final page concordance pending',
                         new_location=location, new_page='integrated build pending',
                         old_text=old, new_text=new, reason=reason,
                         review_status='Complete original and receiving owner proof read and compared; exact hypothesis/conclusion transport recorded.'))


def edit(old, new, kinds, owner, location, reason):
    global x
    assert x.count(old) == 1, (owner, location, x.count(old))
    x = x.replace(old, new)
    record(old, new, kinds, owner, location, reason)


edit(r'\section{Complete smooth-fibre classification and actual Hopf occurrence}',
     r'\section{Smooth fibres and Hopf bundles}', 'D08,D14', 'sec:II:03',
     'Section heading',
     'Use a mathematical heading for the same material. The section label and permanent target remain; the complete classification has its single owner C.3.11 after its prerequisites.')

old_dependency = r'''\StatementRecord{cdp:st:C.3.1}{proved}{01F4}{\SeriesRef{cdp:st:C.3.7}, \SeriesRef{cdp:st:C.3.8}, \SeriesRef{cdp:st:C.3.9}, \SeriesRef{cdp:st:C.3.10}, \SeriesRef{cdp:st:C.3.6}, \SeriesRef{cdp:st:D.2.7}, \SeriesRef{cdp:st:C.3.12}; \cite[Theorem 3.1]{Peters1990}; \cite[p.~2]{Teleman2008}; \cite[Theorem 1]{BBK2019}}'''
new_dependency = r'''\StatementRecord{cdp:st:C.3.1}{proved}{01F4}{\cite[Theorem 3.1]{Peters1990}; \cite[p.~2]{Teleman2008}; \cite[Theorem 1]{BBK2019}}'''
edit(old_dependency, new_dependency, 'D12,D14', 'cdp:st:C.3.1',
     'Necessary-properties dependency declaration',
     'C.3.1 retains exactly its three-step proof of the base, Chern classes, minimality, very-general Kodaira bound and seven-type necessary list. Its duplicated final classification and occurrence clauses are assigned to C.3.11, whose existing dependency declaration retains all seven removed SeriesRef inputs. The hidden declaration now follows the actual proof and removes the old dependency cycle. Printed D10 formatting is unchanged.')

old_tail = r'''Every listed type has Euler characteristic zero. This is a
preliminary necessary list. Statement \ref{cdp:st:C.3.7} below excludes the
bielliptic entry, and \ref{cdp:st:C.3.8} makes the very general Hopf fibre have
algebraic dimension zero. \ref{cdp:st:C.3.9} and \ref{cdp:st:C.3.10} exclude both Kodaira
entries. Statement \ref{cdp:st:C.3.6} realizes both primary and secondary Hopf
entries, and \ref{cdp:st:D.2.7} realizes a fixed abelian surface as general
fibre. Statement \ref{cdp:st:C.3.12} excludes the Inoue entry. Thus the
final very general list consists exactly of two-tori and
primary or secondary Hopf surfaces of algebraic dimension zero.'''
edit(old_tail, 'Every listed type has Euler characteristic zero.',
     'D11,D12,D14', 'cdp:st:C.3.1', 'End of necessary-properties statement',
     'The final-list recap duplicates C.3.11 under exactly the same hypotheses, expressed there by its opening reference to C.3.1. C.3.11 remains the owner of the exhaustive very-general torus/primary-Hopf/secondary-Hopf list, the Hopf algebraic dimension and occurrence. Its receiving statement explicitly retains the fixed abelian-surface occurrence detail. Each individual exclusion remains in C.3.7–C.3.10 and C.3.12. No hypothesis or conclusion disappears from the paper. The full C.3.1 proof is byte-identical.')

edit(r'\begin{proposition}[Full-fibre cohomology and direct images]',
     r'\begin{proposition}[Complete classification and full-fibre cohomology]',
     'D14', 'cdp:st:C.3.11', 'Final-classification title',
     'Name both the classification already asserted here and its full-fibre cohomology conclusion. The title is mathematical and preserves the completed D16 scope.')

old_opening = r'''Under the hypotheses of \ref{cdp:st:C.3.1}, a very general smooth fibre
is a two-torus or a primary or secondary Hopf surface of
algebraic dimension zero. The Inoue exclusion is \ref{cdp:st:C.3.12}.
Both Hopf
entries and the torus entry occur, by \ref{cdp:st:C.3.6} and \ref{cdp:st:D.2.7}.'''
new_opening = r'''Under the hypotheses of \ref{cdp:st:C.3.1}, a very general smooth fibre
is a two-torus or a primary or secondary Hopf surface of
algebraic dimension zero. Both Hopf types occur, and the torus case
occurs with a fixed abelian surface as general fibre.'''
edit(old_opening, new_opening, 'D11,D12,D14', 'cdp:st:C.3.11',
     'Final classification and occurrence clauses',
     'C.3.11 uniquely owns the same exhaustive list and occurrence assertion formerly repeated in C.3.1. The fixed abelian surface is the precise extra occurrence detail transported from that duplicate; its owner D.2.7 and proof are unchanged. Remove the separate Inoue recap because the proof immediately invokes C.3.12 with the other exclusions. The whole-smooth-locus alternatives, full scheme-theoretic cohomology, base change, global cohomology and Picard line remain untouched.')

old_proof = r'''Kodaira and Inoue types from \ref{cdp:st:C.3.1}; \ref{cdp:st:C.3.8} gives the Hopf algebraic
dimension. All smooth fibres are diffeomorphic over the'''
new_proof = r'''Kodaira and Inoue types from \ref{cdp:st:C.3.1}; \ref{cdp:st:C.3.8} gives the Hopf algebraic
dimension. The constructions in \cref{cdp:st:C.3.6,cdp:st:D.2.7}
give the two Hopf types and the fixed abelian-surface occurrence.
All smooth fibres are diffeomorphic over the'''
edit(old_proof, new_proof, 'D12,D14', 'cdp:st:C.3.11',
     'Final classification proof: occurrence maps',
     'Move the occurrence citations from the statement to their proof step. C.3.6 is the explicit free holomorphic C quotient and finite central quotient; D.2.7 supplies the fixed abelian-surface fibration. Both references already occurred in the original statement. All cohomological proof steps remain unchanged.')

old_orphan = r'''These two explicit finite-cover maps locate two additional failures
in the surface-level exclusions used in the proof of CDP20,
Lemma 4.3. They do not construct these surfaces as fibres of a
threefold satisfying the standing hypotheses. Such a realization or
a separate exclusion remains part of C.3.'''
remark = r'''\begin{remark}[First homology of secondary surfaces]
\hypertarget{tag-P212}{}\label{rem:II:secondary-surface-homology}
\StatementRecord{rem:II:secondary-surface-homology}{proved}{P212}{}
The finite \'etale quotients in \cref{cdp:st:C.3.2,cdp:st:C.3.3}
contradict the two assertions in \cite[Lemma~4.3, proof, p.~685]{CDP2020}
that secondary Kodaira and secondary Hopf surfaces always have
nonzero torsion in their first integral homology. Their first homology
groups are computed by abelianizing the displayed deck groups.
\end{remark}'''
edit(old_orphan, remark, 'D02,D06,D11,D13,D18',
     'rem:II:secondary-surface-homology', 'Comparison after the two secondary-surface examples',
     'The publisher PDF was opened at Lemma4.3 and its entire proof, printed pp.684–685; the two homology claims occur on p.685. State their correction once in a numbered mathematical remark and name the actual quotient/abelianization maps proved in C.3.2 and C.3.3. Remove the draft-facing non-realization disclaimer and the obsolete C.3 shorthand. Actual fibre occurrence and exclusion retain their separate exact hypotheses in C.3.6, C.3.9 and C.3.11.')

old_group = r'''Multiplication of the listed coordinates is closed in $\Q(\sqrt5)^4$,
and the commutator map on this finite group is surjective.
Every element is therefore a commutator, and $G^{\rm ab}=0$.'''
new_group = r'''Representing each coordinate as $a+b\sqrt5$ with $a,b\in\Q$,
Hamilton multiplication and $g^{-1}=\overline g$ compute both the
products and the commutators $gh\overline g\,\overline h$ exactly.
Enumerating the ordered pairs of the displayed elements gives
products in the same set and a commutator image equal to that set.
Thus every element is a commutator and $G^{\rm ab}=0$.
The program is listed in \cref{tab:II:programs}.'''
edit(old_group, new_group, 'D09', 'cdp:st:C.3.3',
     'Secondary Hopf example: finite group calculation',
     'State the exact input, rational-pair arithmetic, inverse, exhaustive ordered-pair method and result already used in the proof. The existing program table contains its pinned repository/file citation. The complete stored target routine and existing exact output were read: the commutator image is the whole displayed group. This edit adds no computation run or independent check, and preserves the surjective-commutator conclusion.')

edit('where positive multiplicities are retained in the last integral.',
     'where $E$ carries its positive divisor multiplicities.',
     'D08', 'cdp:st:C.3.4', 'Kahler-resolution obstruction: intersection integral',
     'The effective divisor and its positive multiplicities are identical; state their mathematical role directly.')

edit(r'''For every threefold and fibration in \ref{cdp:st:C.3.1}, including every type on
its necessary list, the Euler-number identity is''',
     r'''For every threefold and fibration in \ref{cdp:st:C.3.1}, the Euler-number identity is''',
     'D11', 'cdp:st:C.3.5', 'Euler-number statement',
     'The unchanged universal quantifier over the exact C.3.1 hypotheses already includes every type on its necessary list. The proof still explicitly uses zero Euler number for all those types. Delete only the repeated scope clause.')

edit(r'''surface. Together with \ref{cdp:st:C.3.9} this excludes both Kodaira
types using only rational Betti-number vanishing.''', 'surface.',
     'D11,D12', 'cdp:st:C.3.10', 'End of primary Kodaira exclusion statement',
     'The hypotheses b1=b2=0 remain in both C.3.9 and C.3.10. Their two exclusion conclusions and their union in C.3.11 remain, so the closing recap carries no separate scope or result.')
edit('It is holomorphic, by the actual relative\nPicard quotient',
     'It is holomorphic, by the relative\nPicard quotient',
     'D08', 'cdp:st:C.3.10', 'Primary Kodaira proof: Picard quotient',
     'The same relative quotient Q_c, oriented coordinate q_c and coefficient map prove holomorphicity. Remove the process adjective only.')
edit(r'''applies to this resolution with all its fibre multiplicities
and without a K\"ahler hypothesis.''',
     r'''applies to this analytic resolution with all its fibre multiplicities.''',
     'D02', 'cdp:st:C.3.10', 'Primary Kodaira proof: analytic comparison scope',
     'Retain the exact analytic resolution and all full-fibre multiplicities. The ambient assumptions remain the stated smooth compact complex threefold hypotheses and D.2.3 supplies the analytic comparison at that scope; the affirmative wording removes only the defensive clause.')
edit('all the maps and sections used in their definition are\nthe actual global ones.',
     'all the maps and sections used in their definition are\nglobally defined.',
     'D08', 'cdp:st:C.3.10', 'Primary Kodaira proof: gluing the scalar',
     'The maps beta wedge -, lambda and the section s are unchanged, so their overlap equality and the resulting scalar kappa are unchanged.')

old_inoue = r'''a compact connected complex manifold to a compact Riemann surface,
whose fibres over the complement of a finite set are Inoue surfaces,
has a class in $H^1(Y;\mathbb R)$ restricting nontrivially to each
such fibre. Thus these families cannot have $b_1(Y)=0$.
This assertion permits arbitrary multiplicities and arbitrary
singularities of the omitted fibres.'''
new_inoue = r'''a compact connected complex manifold to a compact Riemann surface,
with arbitrary fibre multiplicities and singularities over a finite
set and Inoue surfaces over its complement, has a class in
$H^1(Y;\mathbb R)$ restricting nontrivially to each Inoue fibre.
Thus these families cannot have $b_1(Y)=0$.'''
edit(old_inoue, new_inoue, 'D11', 'cdp:st:C.3.12',
     'Inoue exclusion: full-fibre scope',
     'Move the existing arbitrary-multiplicity/arbitrary-singularity scope into the hypotheses of the general assertion. The finite exceptional set, all Inoue fibres over its complement, the nonzero restriction class and b1 conclusion are identical. The meridian-period proof is unchanged.')
edit('Thus the $\\theta_V$ glue to an\nactual closed form $\\theta$ on $Y^\\circ$.',
     'Thus the $\\theta_V$ glue to a\nclosed form $\\theta$ on $Y^\\circ$.',
     'D08', 'cdp:st:C.3.12', 'Inoue proof: closed form on the total family',
     'The full-space exterior derivative, real affine transition identity and glued form are unchanged; remove the process adjective only.')

# Convert only the eight tagged bracket displays in this receiving unit.
equation_rows = []
prepared_map = {}
with (ROOT / 'agents/continuation2_B/D19/S6_SERIES_PUBLISH_II_B2_D19_v1_equation_map.tsv').open() as f:
    for row in csv.DictReader(f, delimiter='\t'):
        if row['old_tag']:
            prepared_map[row['old_tag']] = row['target_label']


def numbered(match):
    whole = match.group()
    tag_match = re.search(r'\\tag\{([^}]+)\}', whole)
    if not tag_match:
        return whole
    tag = tag_match.group(1)
    labels = re.findall(r'\\label\{([^}]+)\}', whole)
    assert prepared_map[tag] in labels
    replacement = whole.replace(r'\[', r'\begin{equation}', 1)
    replacement = replacement[:-2] + r'\end{equation}'
    replacement = replacement.replace(tag_match.group(), '')
    # Removing the wrapper and manual tag must leave the formula identical.
    assert whole[2:-2].replace(tag_match.group(), '') == replacement[len(r'\begin{equation}'):-len(r'\end{equation}')]
    owner = 'cdp:st:C.3.9' if tag.startswith('C.SK.') else ('cdp:st:C.3.11' if tag == 'C.PK.9' else 'cdp:st:C.3.6')
    record(whole, replacement, 'D19', owner, f'Equation {tag}',
           'Convert the bracket display to equation and remove only its manual printed tag. Formula payload, label and permanent hypertarget are identical. The existing D19 prepared map confirms the target label. The root-installed section equation counter numbers it in receiving order; no align row scope is involved.')
    equation_rows.append({'old_tag': tag, 'target_label': prepared_map[tag],
                          'owner': owner, 'old_environment': 'bracket',
                          'new_environment': 'equation',
                          'hypertarget': re.search(r'\\hypertarget\{([^}]+)\}', whole).group(1),
                          'formula_comparison': 'byte-identical after numbering wrappers and manual tag only'})
    return replacement


x = re.sub(r'\\\[.*?\\\]', numbered, x, flags=re.S)
assert len(equation_rows) == 8
assert r'\tag{' not in x

# Keep each complete owner and proof intact while changing their mathematical order.
blocks = {}
for match in re.finditer(r'\\begin\{proposition\}.*?\\end\{proof\}', x, re.S):
    block = match.group()
    label = re.search(r'\\label\{(cdp:st:C\.3\.\d+)\}', block).group(1)
    assert label not in blocks
    blocks[label] = block
assert len(blocks) == 12
groups = [
    ('Necessary properties and Euler numbers', 'sec:II:fibre-properties', ['C.3.1', 'C.3.5', 'C.3.4']),
    ('Secondary surfaces and integral cohomology', 'sec:II:secondary-surfaces', ['C.3.2', 'C.3.3']),
    ('Bielliptic and elliptic Hopf fibres', 'sec:II:elliptic-exclusions', ['C.3.7', 'C.3.8']),
    ('Kodaira fibres', 'sec:II:kodaira-exclusions', ['C.3.9', 'C.3.10']),
    ('Inoue fibres', 'sec:II:inoue-exclusion', ['C.3.12']),
    ('Hopf bundles and complete classification', 'sec:II:fibre-classification', ['C.3.6', 'C.3.11']),
]
header = x[:x.index(r'\begin{proposition}')].strip()
parts = [header]
for title, label, owners in groups:
    parts.append(r'\subsection{' + title + r'}\label{' + label + '}')
    parts.extend(blocks['cdp:st:' + owner] for owner in owners)
    if label == 'sec:II:secondary-surfaces':
        parts.append(remark)
result = '\n\n'.join(parts) + '\n\n'

for command in ('label', 'hypertarget'):
    old = Counter(re.findall(r'\\' + command + r'\{([^}]+)\}', original))
    new = Counter(re.findall(r'\\' + command + r'\{([^}]+)\}', result))
    assert all(new[key] == count for key, count in old.items()), command
assert result.count(r'\hypertarget{tag-P212}') == 1
old_c31 = re.search(r'\\begin\{proposition\}\[Smooth fibres.*?\\end\{proof\}', original, re.S).group()
assert old_c31[old_c31.index(r'\begin{proof}'):] == blocks['cdp:st:C.3.1'][blocks['cdp:st:C.3.1'].index(r'\begin{proof}'):]

old_order = [re.search(r'\\label\{(cdp:st:C\.3\.\d+)\}', m.group()).group(1)
             for m in re.finditer(r'\\begin\{proposition\}.*?\\end\{proof\}', original, re.S)]
new_order = ['cdp:st:' + o for _, _, owners in groups for o in owners]
record(' -> '.join(old_order), ' -> '.join(new_order), 'D14', 'sec:II:03',
       'Complete owner and proof order',
       'Move the initial necessary properties and Euler consequence before all their consumers, group the two secondary-surface examples with their precise published comparison, and put Hopf construction before the final classification. All twelve full proposition/proof blocks and the new comparison remark have one receiving occurrence. C.3.10 still requires prior placement of D.2.3, and C.3.11 requires prior placement of D.2.7; those two outside-unit premise moves are explicitly pending root integration.')

fragment = 'agents/continuation3_foundations/S6_SERIES_PUBLISH_II_smooth_fibres.tex'
(ROOT / fragment).write_text(result)


def write_tsv(name, header, values):
    with (OUT / name).open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=header, delimiter='\t', lineterminator='\n')
        w.writeheader()
        w.writerows(values)


write_tsv('S6_SERIES_PUBLISH_classification_defects.tsv', fields, rows)
write_tsv('S6_SERIES_PUBLISH_classification_equation_map.tsv',
          list(equation_rows[0]), equation_rows)

event_fields = ['statement_id', 'date', 'who', 'type', 'outcome', 'event_id',
                'phase', 'source_file', 'source_row', 'source_event_type',
                'evidence_group', 'publish_input_file', 'publish_input_row',
                'date_utc', 'where']
events = []
# Every original proof was read, including the unchanged receiving owners.
for owner in new_order + ['rem:II:secondary-surface-homology']:
    reasons = list(dict.fromkeys(r['reason'] for r in rows if r['statement_id'] == owner))
    comparison = ' '.join(reasons) if reasons else 'Complete original and receiving proof read; the full proof is unchanged and moved intact to the receiving dependency order.'
    event_id = 'publish:c3:classification:' + owner
    events.append(dict(statement_id=owner, date=now[:10],
                       who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 foundations',
                       type='used and rechecked in this run',
                       outcome=comparison + ' This is an exposed full-proof editorial comparison, not an independent re-proof, computation rerun or final PDF reading.',
                       event_id=event_id, phase='publication text and proof comparison',
                       source_file='agents/continuation3_foundations/S6_SERIES_PUBLISH_classification_CHECK_EVENTS.tsv',
                       source_row='', source_event_type='used and rechecked in this run',
                       evidence_group=event_id, publish_input_file='', publish_input_row='',
                       date_utc=now, where='Smooth fibres: complete owner proof and exact C.3.1/C.3.11 conclusion transport'))
write_tsv('S6_SERIES_PUBLISH_classification_CHECK_EVENTS.tsv', event_fields, events)

progress = []
for _, unit, _ in groups:
    for number in range(1, 26):
        kind = f'D{number:02}'
        status = 'done'
        basis = 'Complete unit read against all 25 defect types; each changed instance is logged and no residual local instance found.'
        if number == 10:
            basis = 'Existing D10 closure preserved: StatementRecord still prints only its permanent tag; every original target remains.'
        elif number == 16:
            basis = 'Existing D16 closure preserved; all original owners and the added P212 remark have mathematical titles.'
        elif number == 17:
            basis = 'Complete proofs compared. Cited classifications and normal-form inputs remain cited at their existing loci. The explicit quotient, period, meridian and norm arguments establish the specialized receiving forms; no published proof was removed without an opened exact source.'
        elif number == 19:
            basis = 'Every manual tag in this unit is converted with unchanged formula payload and existing target label; old-tag/label map supplied for outside-unit citations. Final equation numbers and layout await root build.'
        elif number == 24:
            status = 'open'
            basis = 'Root owns the front matter and organization. The supplied conclusion-owner map identifies front Theorem B and its relation-to-literature citation as needing C.3.11 for the final list.'
        elif number == 14:
            if unit in {'sec:II:kodaira-exclusions', 'sec:II:fibre-classification'}:
                status = 'open'
                basis = 'Local whole-owner order completed. The actual forward premise D.2.3 (for C.3.10) or D.2.7 (for C.3.11) must be placed before its consumer; direct-input inspection and exact block proposal follow separately.'
            else:
                basis = 'Necessary properties precede their local consumers; related owners are grouped into descriptive subsections, with all complete proofs intact.'
        elif number == 25:
            basis = 'Every original and receiving proof read in full. Exact quotient, trace, coefficient, period and meridian maps followed; no new false intermediate assertion identified. The C.3.1/C.3.11 consolidation changes ownership only and retains all hypotheses and conclusions.'
        progress.append(dict(unit=unit, row=kind, status=status, basis=basis, fragment=fragment))
    progress.append(dict(unit=unit, row='restructuring', status='open',
                         basis='Local subsections and whole-proof order completed. Parent must admit the conclusion-owner map, settle D.2.3/D.2.7 forward-premise placement, and align the final paper structure and front matter.', fragment=fragment))
write_tsv('S6_SERIES_PUBLISH_classification_unit_progress.tsv',
          ['unit', 'row', 'status', 'basis', 'fragment'], progress)

ownership = [
    ('C.3.1 hypotheses', 'connected smooth compact complex threefold; b1=b2=0; a(Y)=1; holomorphic algebraic reduction', 'cdp:st:C.3.1', 'unchanged; C.3.11 explicitly inherits these exact hypotheses', 'C.3.8; C.3.11; C.3.12; C.3.5; theorem B'),
    ('C.3.1 base and Chern classes', 'C=P1; all smooth fibres c1(K) rationally zero, c2 integrally zero, chi(O)=0', 'cdp:st:C.3.1', 'unchanged; original three-step proof retained', 'C.3.11 all-smooth-fibre cohomology; theorem B'),
    ('C.3.1 minimality and necessary list', 'no exceptional first-kind curve; very general kappa<=0; all seven listed types; Euler number zero', 'cdp:st:C.3.1', 'unchanged; original proof retained and placed first', 'C.3.5; C.3.8; C.3.12; A.4.9; NC5; C4e'),
    ('C.3.1 repeated exclusions', 'bielliptic, secondary Kodaira, primary Kodaira, Inoue excluded; very general Hopf a=0', 'cdp:st:C.3.7; cdp:st:C.3.9; cdp:st:C.3.10; cdp:st:C.3.12; cdp:st:C.3.8', 'individual owners and complete proofs retained; used once in C.3.11 proof', 'C.3.11; C4e retains necessary-list plus individual-exclusion proof'),
    ('C.3.1 repeated exhaustive final list', 'very general two-torus or primary/secondary Hopf with a=0', 'cdp:st:C.3.11', 'same hypotheses and conclusion already in this owner; duplicate removed from C.3.1', 'theorem B final-list clause; front relation-to-literature classification citation'),
    ('C.3.1 repeated occurrence', 'primary and secondary Hopf occurrence; fixed abelian surface as general fibre', 'cdp:st:C.3.11', 'fixed-abelian detail explicitly retained in receiving statement; C.3.6 and D.2.7 cited in proof', 'theorem B occurrence clause'),
    ('C.3.11 all-smooth alternatives', 'all smooth fibres tori or b1=1,b2=0; table of cohomology and direct images', 'cdp:st:C.3.11', 'unchanged table except automatic equation numbering; does not assert that every special smooth fibre is Hopf', 'all existing direct-image and cohomology consumers'),
    ('C.3.11 full-fibre/global claims', 'full scheme-theoretic hq and both base changes; second-branch Hq(Y,O) and Pic0=C beta', 'cdp:st:C.3.11', 'unchanged statements and proof', 'all existing full-fibre and Picard consumers'),
]
ownership_rows = [dict(zip(['original_clause', 'exact_scope', 'receiving_owner', 'transport', 'consumers'], row)) for row in ownership]
write_tsv('S6_SERIES_PUBLISH_classification_conclusion_map.tsv',
          list(ownership_rows[0]), ownership_rows)

print(f'{len(rows)} defect rows; {len(events)} exposed full-proof readings; 6 subsections; 8 equation conversions; P212 newly numbered.')
print('All 12 original proposition/proof owners, every old label and every permanent target retained. C.3.1 proof byte-identical.')
print('D.2.3/D.2.7 placement and global front-matter concordance remain explicit integration tasks. Shared deliverables unchanged.')
