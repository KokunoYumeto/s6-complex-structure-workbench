"""Prepare isolated editorial guards for eight fully read Paper II owners.

No canonical source, ledger, tag file, inventory, or full-paper candidate is written.
"""
from pathlib import Path
import collections
import csv
import datetime
import difflib
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_D09_D04_batch06_working'
P = 'S6_SERIES_PUBLISH_II_A2_D09_D04_batch06'
source = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
sha = lambda x: hashlib.sha256(x.encode() if isinstance(x, str) else x).hexdigest()
owners = {'01B9': 'cdp:st:A.5.19', '01BC': 'cdp:st:A.5.21', '02XD': 'night:P4.4',
          '01GE': 'cdp:st:D.2.7', '01D7': 'cdp:st:C.2.UN.29', '01DC': 'cdp:st:C.2.UN.33',
          '01DF': 'cdp:st:C.2.UN.36', '01DI': 'cdp:st:C.2.UN.39'}
before = {tag: (OUT / f'S6_SERIES_PUBLISH_II_A2_{tag}_before.tex').read_text() for tag in owners}
following = {tag: (OUT / f'S6_SERIES_PUBLISH_II_A2_{tag}_following_before.tex').read_text() for tag in owners}
after, following_after = dict(before), dict(following)
guards = []

def add(old, new, owner, tag, classes, reason, detail=None):
    assert old != new
    assert source.count(old) == 1, (tag, old[:100], source.count(old))
    a = source.index(old); b = a + len(old)
    g = dict(id=f'A2-ED06-{len(guards)+1:03d}', owner=owner, tag=tag,
             old=old, new=new, old_sha256=sha(old), new_sha256=sha(new), expected_count=1,
             defect_ids=classes, reason=reason, detail=detail or {},
             source_snapshot_sha256=sha(source), source_character_span=[a, b],
             source_byte_span=[len(source[:a].encode()), len(source[:b].encode())],
             source_line_span=[source.count('\n', 0, a)+1, source.count('\n', 0, b)+1])
    guards.append(g)

def edit(tag, old, new, classes, reason, detail=None):
    assert before[tag].count(old) == after[tag].count(old) == 1, (tag, old[:80])
    add(old, new, owners[tag], tag, classes, reason, detail)
    after[tag] = after[tag].replace(old, new)

tail = '\n\\end{enumerate}\n\\end{proof}'

def move_following(tag, content, remaining, classes, reason, detail=None):
    assert after[tag].endswith(tail)
    old = tail + following[tag]
    new = '\n\n' + content.strip() + '\n' + tail + remaining
    add(old, new, owners[tag], tag, classes, reason, detail)
    after[tag] = after[tag][:-len(tail)] + new[:-len(remaining)] if remaining else after[tag][:-len(tail)] + new
    following_after[tag] = remaining

# B9: retain the complete affine counterexample to a blanket spherical-cycle route.
f = following['01B9']
cut = f.index('Exact ideal, normal-coordinate and discriminant')
example = f[:cut].strip()
example = example.replace('The singular rational possibilities cannot be\nremoved by a blanket local spherical-cycle argument.\nFor example',
                          'A singular rational image can have an aspherical regular\naffine fibre. For example')
example = example.replace('This is a local model, not a compact\n$b_2=0$ example.',
                          'The ambient threefold of this local model is the\nnoncompact space $\\C^3$.')
move_following('01B9', example, '\n\n', ['D09', 'D13', 'D02', 'D08'],
               'Move the complete two-display nodal-image example and both inverse maps into the final proof item. Preserve its asphericity and boundary-comparison conclusion; replace the defensive opening and ambient-scope wording. Transfer only program narration to Programs/records.',
               dict(moved_equations=['cdp:eq:A.U.6', 'cdp:eq:A.U.7'], historical_programs=['E_triple_images.py', 'A_low_delta_cusp.py']))

# BC: all scalar-zero models, covering maps, conductor divisors and sphere arguments stay.
f = following['01BC']; section_at = f.index('\\section{')
content = f[:section_at].strip()
content = content.replace('The weighted scaling,\nsimple-zero and endpoint-square identities are\nchecked in \\path{code/E_binary_products.py}.', '')
content = content.replace('The identities and the two finite-cover\nformulas are checked in \\path{code/E_cubic_double.py}.', '')
content = content.replace('These are actual coordinates with $y$', 'These are coordinates with $y$')
content = content.replace('The following different scalar-zero model records\nthe limit of that argument:',
                          'A scalar-zero model with aspherical regular affine fibre is')
content = content.replace('by these actual covering\nmaps.', 'by these covering\nmaps.')
content = content.replace('This is an exact local\nmodel, not a construction of a compact $b_2=0$\nfibre. It shows why a vanishing cubic coefficient\nalone does not justify a local spherical-cycle\nexclusion.',
                          'The ambient threefold of this local model is the noncompact\nspace $\\C^3$; its regular affine fibre is aspherical despite\nthe vanishing cubic coefficient.')
move_following('01BC', content, '\n\n'+f[section_at:], ['D09', 'D13', 'D02', 'D08'],
               'Move the complete hypothesis comparison, both scalar-zero models, exact coordinate inverses, compact sphere and finite covering maps into the final proof item. Preserve the five displays and all conductor divisors. Remove the two program sentences and process phrasing. Leave the raw A.U.6 reference for root D19.',
               dict(moved_equations=['cdp:eq:A.BP.9', 'cdp:eq:A.BP.10', 'cdp:eq:A.BP.11', 'cdp:eq:A.BP.12'], historical_programs=['E_binary_products.py', 'E_cubic_double.py']))

# XD: replace the matrix-output dump by exact generating maps, retaining all values.
old = r'''\item We use the ordered basis $(e_1,e_2,e_3,e_4,s_1,s_2)$ for $H_1(W)$ and
append the three bases $(c_i,b_i,d_i)$ for the local groups.'''
new = r'''\item The coordinate changes in Proposition~\ref{night:P4.2} give the
ordered local lattice bases $(a_i,c_i,b_i,d_i)$ as the columns
\[
 \begin{aligned}
 S_1&=(e_3,e_4,e_1,e_2),\\
 S_2&=(e_2+e_4,-e_1-e_3,e_3,e_4),\\
 S_3&=(e_1+e_4,e_2-e_3,e_3,e_4).
 \end{aligned}
\]
Let $q_1$ delete the $a$ coordinate and let $q_2$ delete the
$a\wedge c$ coordinate from the lexicographically ordered wedge basis
of $(a,c,b,d)$. Proposition~\ref{night:P4.3} gives the local maps
\[
 R_{1,i}=q_1S_i^{-1},\qquad
 R_{2,i}=q_2\bigwedge\nolimits^2(S_i^{-1}).
\]
In the cellular model of that proposition, the chain groups in degrees
zero through four have ranks $(1,4,7,6,2)$: the torus exterior cells
come first, followed by $r$ in degree two, $rc,h$ in degree three,
and $hc$ in degree four. The only nonzero boundary values are
$\partial r=a$ and $\partial(rc)=a\wedge c$; all other cell boundaries
vanish. These specify the four integral differentials.

We use the ordered basis $(e_1,e_2,e_3,e_4,s_1,s_2)$ for $H_1(W)$ and
append the three bases $(c_i,b_i,d_i)$ for the local groups.'''
edit('02XD', old, new, ['D09'], 'Give exact ordered input bases, inverse/projection maps and sparse cellular boundary formulas that reproduce all eighteen former output arrays. The original Mayer–Vietoris construction and elimination remain unchanged.',
     dict(matrix_count=18, exact_comparison_program='code/S6_SERIES_PUBLISH_II_A2_D09_batch06_matrix_maps.py'))
edit('02XD', 'The\nexecuted independent Smith calculation gives fifteen unit factors for\n$F_1$ and twenty-nine unit factors for $F_2$, and computes $\\det F_1=-1$.',
     'Thus the Smith forms have fifteen unit factors for\n$F_1$ and twenty-nine unit factors for $F_2$; expansion of the\ndegree-one block matrix gives $\\det F_1=-1$.', ['D09', 'D08'],
     'Keep both complete Smith-form conclusions and the exact determinant while replacing execution/independence narration with the integral elimination and block determinant method.')
xd_suffix = before['02XD'][before['02XD'].rindex('Both base generators'):]
add(xd_suffix+following['02XD'], xd_suffix+'\n\n', owners['02XD'], '02XD', ['D09', 'D13'],
    'Remove the generated eighteen-matrix dump and program/output narration after exact entrywise comparison against the generating maps in the revised proof, the original TeX arrays and historical JSON. Every array remains in the immutable original extract; no mathematical entry, labelled equation or dependency is lost.',
    dict(matrix_count=18, historical_program='example_mayer_vietoris.py'))
following_after['02XD'] = '\n\n'

# GE: preserve the +1 determinant in its distinct, now explicit quotient bases.
edit('01GE', 'Consequently the trivial-monodromy class in D.2 is\nnonempty, and equality in the unrestricted sign theorem',
     'Consequently the class of such torus fibrations with identity\nintegral monodromy is nonempty, and equality in the unrestricted sign theorem',
     ['D04'], 'Replace the internal D.2 scope label by the exact class already specified in the unchanged statement hypotheses.')
old = r'''The attached program constructs both full signed
Mayer--Vietoris matrices: their sizes are $15\times15$
and $29\times30$, the first has determinant $+1$, and
all nonzero Smith entries of both are $1$. It also checks
the six-dimensional relation matrix in \eqref{cdp:eq:D.32}.'''
new = r'''For explicit quotient coordinates, if $v$ has a coordinate equal to
$\pm1$, let $p$ be the first such coordinate and put
\[
 Q_v(x)=\bigl(x_j-(v_j/v_p)x_p\bigr)_{j\ne p},
\]
with the remaining coordinates in their original order.
Use $Q_{w_i}$ and $Q_{[C_i]}$ for the two local quotients in
\eqref{cdp:eq:D.25}. Order the global fibre basis by $(e_1,e_2,e_3,e_4)$,
its exterior square lexicographically, and the two exterior-base
generators by $(\mu_1,\mu_2)$. Concatenate the three boundary bases for
the source; append the three local target bases after the exterior
target, in increasing $i$.
In each boundary basis put the fibre generators before the meridian,
and the pure wedge generators before $(e_j\wedge\mu_i)_{j=1}^4$.
In the exterior degree-two target put the pure fibre generators first,
then the mixed generators ordered first by $\mu_1,\mu_2$ and then by $e_j$.
The signed maps given by \eqref{cdp:eq:D.29}--\eqref{cdp:eq:D.30} then have
sizes $15\times15$ and $29\times30$. Integer elimination as above gives
unit Smith entries in both degrees, and expansion of the degree-one
block matrix gives determinant $+1$. The six-dimensional quotient
relation matrix in \eqref{cdp:eq:D.32} has unit Smith entries as well.'''
edit('01GE', old, new, ['D09', 'D08'],
     'Preserve all matrix-size, determinant and Smith-form assertions in exact primitive-pivot quotient bases. Give the quotient formula, ordered inputs and signed-map method, replacing the attached-program narration. These bases are related to XD by the explicitly verified unimodular maps in the comparison record.')
f = following['01GE']
marker = 'They also show why extending the group family\nof \\ref{cdp:st:D.2.6}'
assert marker in f
content = r'''The construction uses principal elliptic bundles, one point blowup
in each quotient surface, and the integral clutchings above.
The extension of the Albanese group family in Proposition~\ref{cdp:st:D.2.6}
does not extend its marked Albanese map on this model: by
\eqref{cdp:eq:D.25}, a nonzero integral one-cycle of the smooth torus
is killed in each local filling. An extending map
$\alpha:U_i\to\mathcal A$ to the smooth group family would give
\[
 H_1(A;\Z)\longrightarrow H_1(U_i;\Z)
       \xrightarrow{\alpha_*}H_1(\mathcal A;\Z).
\]
The first arrow kills $w_i$, while the composite sends it to its
nonzero marked class: a smooth proper group family over a disc is
differentiably trivial, so inclusion of its fibre induces an
isomorphism on $H_1$. This is a contradiction.'''
move_following('01GE', content, '\n\n', ['D13', 'D01', 'D02'],
               'Move the complete mathematical group-family/marked-map distinction into the owning proof, with its exact killed-cycle obstruction. Preserve the original literature-search wording in records only; its historical search claim is not repeated or upgraded. The entire supporting D.2.6 proof was read.')

# Return germs: the all-order calculation stays verbatim; remove only code narration.
edit('01D7', 'compact-curve time-form argument\nin C.2.UN.16:',
     'compact-curve time-form argument\nin Proposition~\\ref{cdp:st:C.2.UN.16}:', ['D04'],
     'Resolve the printed internal statement number to its exact existing permanent owner.')
edit('01D7', r'''The formal coefficient extraction is independently
certified in \path{code/A_return_germs.py}; its executed
output records the higher-coefficient cancellations.

\par\medskip\noindent\textbf{Global periods and the singular fibres.}''',
     r'''\par\medskip\noindent\textbf{Global periods and the singular fibres.}''', ['D09', 'D08'],
     'Move the program/independence narration to records and Programs. The preceding every-d coefficient-order proof and both identities are retained byte for byte.')
edit('01D7', 'quotient and graph comparisons in \\ref{cdp:st:C.2.UN.19}--20\ngive',
     'quotient and graph comparisons in \\ref{cdp:st:C.2.UN.19}--\\ref{cdp:st:C.2.UN.20}\ngive',
     ['D04'], 'Resolve both endpoints of the existing same-paper dependency range without changing its mathematical inputs.')
edit('01DC', '\\ref{cdp:st:C.2.UN.19}--20. Thus its relatively minimal elliptic model is',
     '\\ref{cdp:st:C.2.UN.19}--\\ref{cdp:st:C.2.UN.20}. Thus its relatively minimal elliptic model is',
     ['D04'], 'Resolve both endpoints of the existing same-paper dependency range without changing its mathematical inputs.')

# Finite character calculation: the complete character rules and eleven-row table stay.
edit('01DC', r'''The zero character gives no nonsmooth fibre.
These finite counts, the local reflection reductions,
and the Euler sums are independently executed in
\path{code/root_cyclic_elliptic_types.py} and its
saved output.
''', 'The zero character gives no nonsmooth fibre.\n', ['D09', 'D08'],
     'Move the finite-program narration to Programs and records. The reflection quotient, all characters, Euler rule and eleven configurations remain in the proof.')

# The alternate invariant basis is mathematical and must remain with its exact map.
edit('01DF', r'''The four exterior-square kernels and their restricted forms
are computed over the rationals by
\path{code/current_audits/audit_sign/code/independent_sign_checks.py};
the bases and Gram matrices are recorded in
\path{code/current_audits/audit_sign/independent_sign_checks.json}.
For the rank-two rows the recorded basis is''',
     'For the rank-two rows an alternative invariant basis is', ['D09', 'D08'],
     'Remove file/output narration while retaining the complete alternate basis, exact permutation/sign map and Gram congruence. Both epsilon values are verified in the post-reading matrix comparison.')

# Keep the exact determinant connection to actual, possibly nonsemisimple monodromy.
old = r'''The exact integer-matrix calculation in
\path{code/current_audits/audit_sign/code/UN24_UN39_exact_certificate_08.py}
computes every one-period determinant, the M\"obius coefficients,
all nineteen averages and their zero indices. Its complete output is
\path{code/current_audits/audit_sign/UN24_UN39_exact_certificate_08.json}.
For each characteristic polynomial the program uses a direct sum
of cyclotomic companion matrices.'''
new = r'''For each characteristic polynomial, let $B$ be the direct sum of the
companion matrices of its cyclotomic factors, retaining repetitions.
Compute $\det(I-B^k)$ through one period, take the rational average
\eqref{cdp:eq:C.ZC.2}, and apply M\"obius inversion to the divisor sum in
\eqref{cdp:eq:C.ZC.5}. This gives the nineteen averages and zero indices
in \eqref{cdp:eq:C.ZC.4}.'''
edit('01DI', old, new, ['D09'],
     'State the exact companion-matrix input, determinant/average/Mobius method and complete-table result in mathematical language. Keep the following eigenvalue-multiplicity identity that relates the computation to actual monodromy, including its unipotent part.')

# Add one source citation per historical file, reusing a matching existing row.
prefix = r'https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\SsixRepositoryCommit/'
cdp = 'pro_returns/S6_03_CDP_checkpoint_13_20261116T0136Z/S6_03_CDP/code/'
blind = 'pro_returns/S6_06_BLIND_checkpoint_15_20261117T1457Z/S6_06_BLIND/code/part4/'
grind = 'pro_returns/S6_SERIES_GRIND_checkpoint_10_20261120T0211Z/code/current_audits/audit_sign/code/'
table = source[source.index('\\section*{Programs}'):]
retrieval = json.loads((OUT / 'S6_SERIES_PUBLISH_II_A2_batch06_retrieval_attempts_01.json').read_text())
opened = {r['name']: r for r in retrieval['attempts'] if r.get('status') == 200}
rows = []

def link(name, directory):
    assert name in opened and opened[name]['url'].endswith(directory+name)
    assert '\\nolinkurl{'+name+'}' not in table, name
    return '\\href{'+prefix+directory+name+'}{\\nolinkurl{'+name+'}}'

matches = [line for line in table.splitlines(True) if '\\nolinkurl{S6_SERIES_PUBLISH_II_B2_B9_prereading_certificate.py}' in line]
assert len(matches) == 1
old = matches[0]
new = old[:-len(' \\\\[3pt]\n')] + '; ' + link('E_triple_images.py', cdp) + '; ' + link('A_low_delta_cusp.py', cdp) + ' \\\\[3pt]\n'
add(old, new, 'Programs', '', ['D09'], 'Append the two fully opened historical symbolic-cube programs once to the matching existing B9 row; retain the existing current verifier link.')
rows.append(new)
specs = [
    (r'Weighted binary-product identities and endpoint-square arithmetic (\cref{cdp:st:A.5.21})', 'E_binary_products.py', cdp),
    (r'Scalar-zero coordinate changes and finite-cover identities (\cref{cdp:st:A.5.21})', 'E_cubic_double.py', cdp),
    (r'Local chain maps and signed integral Mayer--Vietoris maps (\cref{night:P4.3,night:P4.4})', 'example_mayer_vietoris.py', blind),
    (r'Primitive quotient bases, integral clutchings and Smith forms (\cref{cdp:st:D.2.7})', 'D_trivial_monodromy.py', cdp),
    (r'Leading return-germ coefficients and their integration (\cref{cdp:st:C.2.UN.29})', 'A_return_germs.py', cdp),
    (r'Cyclic elliptic characters, reflection quotients and Euler sums (\cref{cdp:st:C.2.UN.33})', 'root_cyclic_elliptic_types.py', cdp),
    (r'Exterior-square invariant bases and intersection forms (\cref{cdp:st:C.2.UN.36})', 'independent_sign_checks.py', grind),
    (r'Cyclotomic determinants, M\"obius inversion and zero-Euler indices (\cref{cdp:st:C.2.UN.39})', 'UN24_UN39_exact_certificate_08.py', grind),
]
new_rows = ''.join(description+' & '+link(name, directory)+' \\\\[3pt]\n' for description, name, directory in specs)
anchor = '\\end{longtable}}\n\n\\begin{thebibliography}{99}'
add(anchor, new_rows+anchor, 'Programs', '', ['D09'], 'Add eight exact opened historical program links with the shared full-commit macro and their verified receiving scopes. No output file is cited as a second program source.')
rows.extend(new_rows.splitlines(True))
(OUT / (P+'_Programs_rows_after.tex')).write_text(''.join(rows))

# Verify exact disjoint application and inversion in memory only.
ordered = sorted(guards, key=lambda g: g['source_character_span'][0])
for a, b in zip(ordered, ordered[1:]):
    assert a['source_character_span'][1] <= b['source_character_span'][0], (a['id'], b['id'])
candidate = source
for g in guards:
    assert candidate.count(g['old']) == 1, g['id']
    candidate = candidate.replace(g['old'], g['new'])
inverse = []
for g in reversed(guards):
    assert candidate.count(g['new']) == 1, (g['id'], candidate.count(g['new']))
    inverse.append(dict(id=g['id']+'-inverse', old=g['new'], new=g['old'], expected_count=1))
    candidate = candidate.replace(g['new'], g['old'])
assert candidate == source

math = lambda x: re.findall(r'\\\[.*?\\\]|\\\(.*?\\\)|(?<!\\)\$(?!\$).*?(?<!\\)\$|\\begin\{(?:align\*?|equation\*?|gather\*?)\}.*?\\end\{(?:align\*?|equation\*?|gather\*?)\}', x, re.S)
anchors = lambda x: re.findall(r'\\(?:label|hypertarget|tag)\{[^}]*\}', x)
enums = lambda x: re.findall(r'\\begin\{enumerate\}(?:\[[^\n]*\])?', x)
eqrefs = lambda x: re.findall(r'\\eqref\{[^}]*\}', x)
preservation = []
for tag, body in before.items():
    nb, f, nf = after[tag], following[tag], following_after[tag]
    for suffix, text in [('after', nb), ('following_after', nf)]:
        (OUT / f'S6_SERIES_PUBLISH_II_A2_{tag}_{suffix}.tex').write_text(text)
    (OUT / f'S6_SERIES_PUBLISH_II_A2_{tag}_exact.diff').write_text(''.join(difflib.unified_diff(
        (body+f).splitlines(True), (nb+nf).splitlines(True), fromfile=tag+'_before', tofile=tag+'_after')))
    assert anchors(body+f) == anchors(nb+nf), tag
    assert enums(body) == enums(nb), tag
    assert body.count('\\item') == nb.count('\\item'), tag
    assert all(x in nb for x in re.findall(r'\\\[.*?\\\]', body, re.S)), tag
    old_refs, new_refs = collections.Counter(eqrefs(body+f)), collections.Counter(eqrefs(nb+nf))
    assert not (old_refs-new_refs), (tag, old_refs-new_refs)
    assert '\\path{code/' not in nb and '.json}' not in nb, tag
    preservation.append(dict(tag=tag, owner=owners[tag], before_sha256=sha(body), after_sha256=sha(nb),
                             before_bytes=len(body.encode()), after_bytes=len(nb.encode()),
                             item_tokens=body.count('\\item'), original_bracket_displays=len(re.findall(r'\\\[.*?\\\]', body, re.S)),
                             final_bracket_displays=len(re.findall(r'\\\[.*?\\\]', nb, re.S)),
                             all_original_proof_displays_retained=True,
                             all_labels_tags_and_enum_formats_retained=True,
                             all_original_equation_references_retained=True,
                             matrix_dump_represented_by_exact_generating_formulas=18 if tag=='02XD' else 0))

def dump(suffix, data):
    (OUT / (P+'_'+suffix+'.json')).write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n')

dump('guards', guards); dump('inverse_guards', inverse); dump('preservation', preservation)
with (OUT / (P+'_defects.tsv')).open('w', newline='') as stream:
    fields = ['id', 'type', 'owner', 'tag', 'guard_id', 'old_text', 'new_text', 'source_line', 'status']
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t'); writer.writeheader()
    for g in guards:
        for defect in g['defect_ids']:
            writer.writerow(dict(id=g['id']+'-'+defect, type=defect, owner=g['owner'], tag=g['tag'], guard_id=g['id'],
                                 old_text=g['old'], new_text=g['new'], source_line=g['source_line_span'][0], status='proposed; no canonical write'))
summary = dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), source_snapshot_sha256=sha(source),
               owners=preservation, exact_guards=len(guards), exact_inverse_guards=len(inverse),
               new_program_rows=8, amended_program_rows=1, new_historical_program_links=10,
               forward_inverse_exact=True, all_intervals_disjoint=True,
               canonical_mutations=0, new_independent_check_credit=0, required_row_movement=0)
dump('verification', summary)
print(json.dumps(summary, indent=2))
