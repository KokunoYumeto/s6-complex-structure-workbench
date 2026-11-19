#!/usr/bin/env python3
"""Build a guarded atlas integration proposal; never mutate receiving files."""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
WORK = HERE.parents[1]
BODY = WORK / 'parts/I.body.linked.tex'
FRONT = WORK / 'audit_paper_i/frontmatter_I.tex'
ASSEMBLER = WORK / 'code/assemble_series.py'
INDEX = WORK / 'audit_paper_i/main_index_I.json'

def sha(s):
    return hashlib.sha256(s.encode()).hexdigest()

def unique_replace(s, old, new):
    count = s.count(old)
    assert count == 1, (count, old[:120])
    return s.replace(old, new)

atlas_path = HERE / 'coefficient_atlas_theorem.tex'
atlas = atlas_path.read_text()
atlas = atlas.replace(r'\sigma=h\Pi v_j,qquad', r'\sigma=h\Pi v_j,\qquad')
atlas = atlas.replace(r'd\log g_{ba}quad', r'd\log g_{ba}\quad')
atlas = atlas.replace(r'A_{F_j,(a,b)}quad', r'A_{F_j,(a,b)}\quad')
atlas = atlas.replace(r'm_{i+v_1,j+v_2}^{,t}', r'm_{i+v_1,j+v_2}^{t}')
short_start = 'For comparison, fix a Hermitian metric and an orthonormal basis'
if short_start in atlas:
    a = atlas.index(short_start)
    b = atlas.index(r'\begin{proposition}', a)
    atlas = atlas[:a] + atlas[b:]

body = BODY.read_text()
old_operator_start = 'The invariant computations and all the metric types named above are'
oa = body.index(old_operator_start, body.index(r'\label{inv:C3.8}'))
ob = body.index('These two formulas fix global smooth representatives', oa)
operator_statement = body[oa:ob]
operator_statement = operator_statement.replace(
    'The invariant computations and all the metric types named above are\nsettled for $X$.  The real restriction map',
    'The real restriction map')
operator_statement = operator_statement.replace('construction of $Q$ as well.', 'construction of $Q_H$ as well.')
operator_statement = operator_statement.replace('\nQ=\\frac', '\nQ_H=\\frac')
pa = body.index(r'\begin{proof}', ob)
pb = body.index(r'\end{proof}', pa) + len(r'\end{proof}')
operator_proof = body[pa:pb]
operator_proof = unique_replace(operator_proof,
    r'\item We verify the settled operator assertions in this open question.',
    r'\item The operator formulas have the following normalization.')
operator_proof = operator_proof.replace('Thus $Q$ is independent', 'Thus $Q_H$ is independent')
operator_proof = operator_proof.replace(r'$\ell(Q)=1$', r'$\ell(Q_H)=1$')
operator_proof = unique_replace(operator_proof,
    'These computations establish the operator\nrepresentatives and their restrictions. They leave the stated\nevaluation of their coefficient functions on a common global\natlas unevaluated.',
    'These computations establish the operator\nrepresentatives and their restrictions. The evaluated coefficient\nconstruction above provides another representative with the same\nfibre normalization.')
operator = r'''
\subsection{Comparison with the Green and harmonic representatives}
\label{inv:C3.8:operator-comparison}

''' + operator_statement + operator_proof + r'''

The exact comparison on cohomology is
\[
 [G]=[G_0]/12=g_\gamma,\qquad
 [Q_H]-[Q]\in\C d_1g.
\]
The second inclusion follows from the restriction kernel in
\cref{inv:A3.2}.  Thus the two formulas choose lifts of the same fibre
class; their difference is the specified one-dimensional Leray
ambiguity.  The harmonic normalization remains basis independent for
the fixed metric and regular fibre.

\Uses{\cref{inv:A3.2,inv:C3.1,inv:C3.2,inv:C3.7};
the Green formula \eqref{inv:eq:C-G-Green}}
'''

code_note = r'''
\paragraph{Exact algebra checks.}
The programs and their same-stem \path{.output.json} files are in
\path{code/current_audits/audit_paper_i/open_atlas/}.
The program \path{exact_regular_atlas.py} records 25 exact checks of
the marking, lattice factors, curvature coefficients and regular
transition identities; \path{cusp_and_finite_exact.py} records 48
exact checks of the Cartier exponents, extending units, finite phases
and connection identities.  The separate first-jet implementation
\path{finite_collar_jet_verifier.py} records 106 checks of both affine
actions through their first twelve iterates, including the full base
component of the collar connection and the logarithmic gauge terms.
The universal identities in the proof establish descent on the stated
domains; the first-jet evaluations corroborate those identities at the
recorded exact inputs.
'''
if r'\paragraph{Exact algebra checks.}' not in atlas:
    a = atlas.index('\n\\Uses{')
    atlas = atlas[:a] + code_note + atlas[a:]
if r'\subsection{Comparison with the Green' not in atlas:
    atlas += operator
atlas_path.write_text(atlas)

gauges = r'''
\subsection{Changes of the specified coefficient gauge}

\paragraph{The representative and its fibre restriction.}
\label{wb:rem:bcpr-literal-gauge}
The formulas \eqref{inv:eq:atlas-final-forms} and
\eqref{inv:eq:atlas-final-coefficients} choose actual global smooth
forms through all three special fibres.  Their restriction statement
uses the pullback map followed by the Dolbeault quotient on a regular
fibre.  In particular, its translation-invariant value is the class
represented in \CompendiumRef{I}{wb:eq:bcpr-q-fibre-expanded}.
The specified coefficient form on that fibre can be related to the
invariant representative by a Dolbeault coboundary.  The cocycle and
weight formulas below describe the changes produced by these choices.

\Uses{\cref{inv:A3.2,inv:C3.8};
\CompendiumRef{I}{wb:eq:bcpr-q-fibre-expanded}}

\paragraph{The exact changes between coefficient gauges.}
\label{wb:rem:bcpr-global-gauge-boundary}
Use the same holomorphic cocycles $c_{ab},f_{ab}$ on a common
refinement, and two locally finite weight systems $w_n,w'_n$ with
sum one.  In a chart $a$ set
\[
 K_a=\sum_n\sum_u(w'_n-w_n)c_{a,n},\qquad
 U_a=\sum_n\sum_u(w'_n-w_n)f_{a,n}.
\]
The cocycle identities and $\sum(w'_n-w_n)=0$ give
$K_a-K_b=0$ and $U_a-U_b=0$.  They therefore define a global
smooth $(1,0)$ form $K$ and a global smooth function $U$, with
\[
 Q'-Q=\tfrac1{12}\bar\partial K,\qquad
 G'-G=\bar\partial U.
\]
For a holomorphic change of cocycles
$c'_{ab}=c_{ab}+r_a-r_b$ and
$f'_{ab}=f_{ab}+u_a-u_b$, where $r_a$ is a holomorphic one-form
and $u_a$ a holomorphic function, the same weights give
\[
 B'_a-B_a=r_a-\sum_n\sum_u w_n r_n,\qquad
 H'_a-H_a=u_a-\sum_n\sum_u w_n u_n.
\]
The two sums on the right are globally defined smooth forms of the
indicated degrees.  Consequently
\[
 Q'-Q=-\tfrac1{12}\bar\partial\!\sum_n\sum_u w_n r_n,
 \qquad
 G'-G=-\bar\partial\!\sum_n\sum_u w_n u_n.
\]
These formulas identify the actual Dolbeault coboundaries under the
specified gauge changes and preserve all class and product
calculations.  A change of coherent-Leray lift of the fibre class is
measured separately by $\C d_1g$, as in the operator comparison above.

\Uses{the cocycles and coefficients in \cref{inv:C3.8};
the restriction kernel in \cref{inv:A3.2};
the class and product calculations in \cref{inv:C3.3}}
'''

patches = []
def add_patch(path, old, new, reason):
    current = path.read_text()
    assert current.count(old) == 1, (str(path), current.count(old), old[:80])
    patches.append(dict(file=str(path), occurrences=1, old_sha256=sha(old),
                        old=old, new=new, reason=reason))

old_begin = '\\clearpage\n\\part{Results not yet established}\n\\section{Limits and open points: the coefficient atlas}'
ba = body.index(old_begin)
bb = body.index(r'\section{Open arithmetic questions for the normalized norm}', ba)
old_block = body[ba:bb]
insert_atlas = atlas.replace(r'\label{inv:C3.8}',
    r'\label{inv:C3.8}' + '\n' +
    r'\StatementRecord{inv:C3.8}{proved}{}{\cref{inv:A2.1,inv:A3.2,inv:C3.1,inv:C3.2,inv:C3.7}}', 1)
replacement = r'''\clearpage
\section{Global coefficient representatives}
\label{inv:section:coefficient-atlas}

''' + insert_atlas + '\n' + gauges + r'''
\clearpage
\part{Results not yet established}
'''
add_patch(BODY, old_block, replacement,
          'Relocate the proved atlas before the final open part; preserve the full earlier operator and Aeppli assertions, their three-step proof, both gauge labels, and the remaining arithmetic section.')
(HERE / 'coefficient_atlas_insertion.tex').write_text(replacement)
(HERE / 'previous_coefficient_atlas_block.tex').write_text(old_block)

main_clause = r'''
There are specified global forms
$G\in\mathcal A^{0,1}(X)$ and $Q\in\mathcal A^{1,1}(X)$ satisfying
\[
 \bar\partial G=\bar\partial Q=0,\qquad
 [G]=g_\gamma,\qquad i_b^*[Q]=\eta,\qquad
 \exp(12[G])=f^*\mathcal O_{\mathbb P^1}(1).
\]
On the specified common refinement of the original atlas they are
$G=\bar\partial\sum w_nf_{a,n}$ and
$Q=\tfrac1{12}\bar\partial\sum w_nc_{a,n}$, with the locally finite
weights, holomorphic scalar cocycle and holomorphic one-form cocycle
of \eqref{inv:eq:atlas-final-forms}.  The elementary derivative
recursion specifies every coefficient through both multiple fibres
and every cusp stratum.  The form $Q$ is complex; a real
$\bar\partial$-closed form cannot have this fibre class.
'''
anchor = 'supported exactly on $S_1\\cup S_2$, while degree two also has\ntorsion along the cusp double locus.\n'
add_patch(FRONT, anchor, anchor + main_clause,
          'Include the exact standard-family global representative result and its normalization in main Theorem D.')
old = 'the exact quotient by $dt$ and its exterior powers.\n'
new = old + 'Twelfth-power theta lines, cusp Cartier frames and annular\nholomorphic connections give the cocycles for the coefficient\nconstruction; the specified locally finite weights evaluate them.\n'
add_patch(FRONT, old, new, 'Add the actual mechanism of the explicit coefficient result.')
old = 'degree.  The explicit smooth global coefficient atlas remains the\nquestion in \\ref{inv:C3.8}.\n'
new = 'degree.  The coefficient construction in \\ref{inv:C3.8} uses the\noriginal period, finite affine and toric charts; its source comparison\nand exact cocycle maps are given there.\n'
add_patch(FRONT, old, new, 'Replace the obsolete open-atlas description with the proved scope, without a priority claim.')
old = '\\ref{inv:C2.1}, \\ref{inv:C3.3}, \\ref{inv:A4.1},\n\\ref{inv:A4.2}.\n'
new = '\\ref{inv:C2.1}, \\ref{inv:C3.3}, \\ref{inv:A4.1},\n\\ref{inv:A4.2}, \\ref{inv:C3.8}.\n'
add_patch(FRONT, old, new, 'Link main Theorem D to the full new atlas statement.')
step = r'''\item\hypertarget{step-I-D-5}{} The theta factors with their original
finite affine phases and the extending cusp Cartier units define the
three local twelfth-power lines.  The exact determinant divisor makes
the displayed holomorphic connection inverse valid on every overlap
annulus.  Its one-form cocycle and the specified coordinate weights
give $Q$; the scalar cocycle gives the primitive $G$ and its factor
twelve normalization
(\hyperref[inv:C3.8]{\ref*{inv:C3.8}}).
'''
old = '\\end{enumerate}\n\\hyperlink{main-I-D}{Return to Theorem D}.'
add_patch(FRONT, old, step + old, 'Add a fifth proof-outline step with its actual dependency and normalization.')
old = '''% RungZero blocks 1 and 25 are deliberately assigned to the shared
% series overview and the final open-problems part, respectively.
% The literal coefficient-atlas question is inv:C3.8; the arithmetic
% question is the retained ari:C.7.1--ari:C.7.12 discussion, with the
% explicit unresolved relative-period gate at ari:C.7.4.
'''
new = '''% RungZero block 1 belongs to the shared series overview.
% The coefficient-atlas portion of block 25 is included in Theorem D;
% its arithmetic portion remains in the final open-problems part,
% with the explicit unresolved relative-period gate at ari:C.7.4.
'''
add_patch(FRONT, old, new, 'Retain the arithmetic open problem while recording the exact split of block 25.')

old = '''deformation results in the source conventions. The unresolved literal
coefficient-atlas and period questions are stated with the established
reductions and their precise remaining steps.'''
new = r'''deformation results in the source conventions. A holomorphic \v Cech
cocycle and a specified locally finite coordinate partition give global
Dolbeault representatives through all three special fibres. The
arithmetic period question is stated with its established reductions
and precise remaining exclusion.'''
add_patch(ASSEMBLER, old, new, 'Update only the Paper I abstract to the proved coefficient scope and retained arithmetic question.')

index = json.loads(INDEX.read_text())
for main in index['main_theorems']:
    if main['letter'] == 'D':
        if 'inv:C3.8' not in main['body_labels']:
            main['body_labels'].append('inv:C3.8')
        main['rungzero_blocks'].append(25)
        main['rungzero_scope_note'] = 'Only the coefficient-atlas portion of block 25 is included; its arithmetic questions remain in the final open part.'
        main['steps'].append(dict(number=5, anchor='step-I-D-5',
             body_targets=['inv:C3.8'], claim_tex=step.split('{} ', 1)[1].rstrip()))
for outside in index['outside_main_theorems']:
    if outside['rungzero_block'] == 25:
        outside['body_labels'] = [x for x in outside['body_labels'] if x != 'inv:C3.8']
        outside['reason'] = 'The arithmetic portion retains its exact unresolved period-field exclusion; the coefficient-atlas portion is now included in main Theorem D.'
(HERE / 'main_index_I_with_atlas.json').write_text(json.dumps(index, indent=2) + '\n')

proposal = dict(
    author='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort; same model family',
    status='Guarded proposal only: receiving body, frontmatter, assembler, index and inventory are not changed by this program.',
    proof_file=str(atlas_path), insertion_file=str(HERE / 'coefficient_atlas_insertion.tex'),
    proposed_index_file=str(HERE / 'main_index_I_with_atlas.json'),
    receiving_file_sha256={str(p): sha(p.read_text()) for p in (BODY, FRONT, ASSEMBLER, INDEX)},
    inventory_note='The three inv:C3.8 inventory aliases have one canonical 01SL row. Root owns promotion and completion/layout checks after review and build.',
    patches=patches)
(HERE / 'integration_proposal.json').write_text(json.dumps(proposal, indent=2) + '\n')

for token in ('v_j,qquad', 'g_{ba}quad', 'A_{F_j,(a,b)}quad', '^{,t}', r'\label{inv:eq:atlas-cusp-domain}'):
    assert token not in atlas, token
assert operator_statement.count('real dimension\ntwo') == 1
assert operator_proof.count(r'\item') == 3
assert atlas.count(r'\label{inv:C3.8}') == 1
assert replacement.count(r'\part{Results not yet established}') == 1
print(json.dumps(dict(guarded_patches=len(patches), receiving_files_modified=False,
    proof_lines=len(atlas.splitlines()), preserved_operator_steps=3,
    insertion_sha256=sha(replacement), proposal_sha256=sha((HERE/'integration_proposal.json').read_text())), indent=2))
