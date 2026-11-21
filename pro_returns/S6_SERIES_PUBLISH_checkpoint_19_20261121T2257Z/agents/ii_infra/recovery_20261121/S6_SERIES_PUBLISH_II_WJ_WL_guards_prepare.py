#!/usr/bin/env python3
"""New WJ/WL complete guard pairs after new independent freezes and releases."""
from pathlib import Path
import importlib.util
import hashlib
import json
import re
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[3]
AREA = ROOT / 'agents/ii_infra/recovery_20261121'
spec = importlib.util.spec_from_file_location('packets', ROOT/'code/S6_SERIES_PUBLISH_II_packets.py')
packets = importlib.util.module_from_spec(spec)
spec.loader.exec_module(packets)
src = packets.parse_source(ROOT/'S6_SERIES_PUBLISH_II.tex', 'II')
out = AREA/'WJ_WL_blocks'
out.mkdir(exist_ok=False)
def sha(value):
    return hashlib.sha256(value.encode() if isinstance(value, str) else value).hexdigest()
def getblock(label):
    row = src['statement_labels'][label]
    return src['text'][row['start']:max([row['end']]+[x['end'] for x in row['proofs']])]
def inline(text):
    return re.findall(r'(?<!\\)\$(?!\$)(.*?)(?<!\\)\$', text, re.S)
def displays(text):
    return re.findall(r'\\\[(.*?)\\\]', text, re.S)
def refs(text):
    return re.findall(r'\\(?:ref|eqref|cref|Cref|SeriesRef)\{[^}]*\}|\\CompendiumRef\{[^}]*\}\{[^}]*\}|\\cite(?:\[[^\]]*\])?\{[^}]*\}', text)

marker = r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]'
scope_old = 'In the standing torus-fibration setting of this section, let $f^{-1}(b)=mS$\nhave irreducible reduced support. Then'
scope_new = r'''Let $Y$ be a connected smooth compact complex threefold with
$b_1(Y)=b_2(Y)=0$, and let $f:Y\to B$ be a proper surjective
holomorphic map with connected fibres to a smooth compact curve.
Assume that the smooth general fibre is a complex two-torus, and let
$f^{-1}(b)=mS$ have irreducible reduced support. Then'''
formal_old = r'''For any effective exceptional cycle $Z$, the higher direct image
$R^2\pi_*I_Z$ vanishes because all fibres of $\pi$ have dimension
at most one. The exact sequence of $Z$ gives a surjection'''
formal_new = r'''For an effective exceptional cycle $Z$, put $\mathcal F=I_Z$.
Fix $s\in S$ and its maximal ideal $\mathfrak m_s$. Each coherent
quotient $\mathcal F/\mathfrak m_s^k\mathcal F$ is supported on a
compact infinitesimal fibre of dimension at most one. Its cohomology
vanishes in degrees at least two. To see this, filter by the nilradical
and reduce to coherent sheaves on the reduced compact curve. Removing
point-supported torsion and pulling back to its finite normalization
leaves vector bundles on compact Riemann surfaces, up to kernels and
cokernels supported at finitely many points. Their Dolbeault resolutions
have length one, while point-supported sheaves have no higher
cohomology. The finite filtration therefore gives the asserted vanishing
on every infinitesimal fibre.
Analytic formal functions and coherence
\cite[\S6, Haupts\"atze~I and~IIa, p.~59]{Grauert1960D} identify
the completed stalk of $R^2\pi_*\mathcal F$ with the inverse limit of
these zero groups. Nakayama's lemma gives $R^2\pi_*I_Z=0$.
The exact sequence of $Z$ gives a surjection'''
rr_old = r'''Riemann--Roch computation of P4.6, applied to $S$, gives'''
rr_new = r'''Riemann--Roch computation in \ref{night:P4.6}, applied to $S$, gives'''
classcite = r'\cite[Chapter~VI, Theorem~1.1, p.~243]{BHPV2004E}'
end_old = 'It follows that $\\kappa(T)=-\\infty$. The classification '+classcite+'\ngives precisely the stated alternatives for the minimal model.'
end_new = 'It follows that $\\kappa(T)=-\\infty$. Contraction of exceptional\ncurves of the first kind preserves the plurigenera, so the minimal\nmodel has the same Kodaira dimension.'
wl_old = r'''\item The program \texttt{code/part4/genus\_one\_conductor.py}
executes the exact jet restriction matrices through orders
$2,3,4,6,8$, computing the ranks and conductor exponents.
When these branches vary in a surface, their permutation may
assemble them into a single normalization curve covering the
image conductor with degree two or three. Consequently a
unique horizontal conductor component with multiplicity two
does not alone force a degree-one map or generically reduced
image conductor. An additional argument is needed at that
precise point of the general irreducible case.'''
wl_new = r'''\item Let $C_2$ and $C_3$ be the two cubics above. The normalization
of $C_2$ is the disjoint union of two copies of $\Pp^1$, identified
to first order at the preimages of the tacnode. Exchanging these
copies with the same parameter preserves their local ring
$\{(a,b):b-a\in(t^2)\}$ and descends to an involution $\sigma_2$
of $C_2$. In the local coordinates above it is
$(x,y)\mapsto(x,x^2-y)$. The projective automorphism
\[
 \sigma_3[X:Y:Z]=[-Y:X-Y:Z]
\]
has order three and cyclically permutes the components of $C_3$.
For $r=2,3$, take $E'=\C/(\Z+i\Z)$ and let $\tau_r$ be
translation by $1/r$. Its order is exactly $r$, and every nonidentity
power acts freely. Thus the diagonal action defines the compact
surface and its map to an elliptic curve
\[
 X_r=(C_r\times E')/\langle(\sigma_r,\tau_r)\rangle
       \longrightarrow E=E'/\langle\tau_r\rangle.
\]
The cyclic group acts transitively on the components of
$C_r\times E'$, so $X_r$ is irreducible. Its normalization is
$(\coprod_{j=1}^r\Pp^1\times E')/\langle(\sigma_r,\tau_r)\rangle$.
Restriction of this quotient map to one component is an isomorphism
from $\Pp^1\times E'$: each orbit meets that component exactly once.
The reduced inverse-image conductor is the single section
$\Gamma'=\{p\}\times E'$, its conductor divisor is $2\Gamma'$, and
its map to the singular curve $E$ is the finite unramified cover
$E'\to E$ of degree $r$. Analytically locally on $E$, the image
conductor has algebra $\OO_E[u]/(u^2)$ for $r=2$ and
$\OO_E[u,v]/(u,v)^2$ for $r=3$. These local algebras follow from
the normalization constraints in the first two steps and remain
nonreduced after the free quotient. The constructions give a single
horizontal conductor component of multiplicity two with generic
degree two or three over the image conductor.'''

edits = {
    '02WJ': ('night:P4.12', [
        ('title', '[P4.12]', '[Irreducible fibres of torus fibrations]', 'D04/D16', 'Replace the internal run title by the mathematical subject.'),
        ('standing_scope', scope_old, scope_new, 'D04/D06', 'Write the exact inherited standing hypotheses supplied by the root v2 packet; all target conclusions are retained at that same scope.'),
        ('outer_wrapper_start', marker+'\n\\item \n', '', 'D04/D14', 'Remove the single production-labelled wrapper; retain the four substantive Step headings.'),
        ('outer_wrapper_end', '\n\\end{enumerate}', '', 'D04/D14', 'Close removal of the redundant single-item wrapper.'),
        ('rr_locator', rr_old, rr_new, 'D04', 'Resolve the internal P4.6 token to its printed statement number.'),
        ('local_proof_intro', 'We recall the local analytic proof.\n', 'Indeed,\n', 'D08', 'Introduce the actual argument directly.'),
        ('matrix_input_recap', 'The displayed local holomorphic function and exceptional blocks give\nall its inputs for these analytic germs.\n', '', 'D11', 'The retained local function, intersection inequalities and connectedness supply these inputs explicitly.'),
        ('formal_functions', formal_old, formal_new, 'D18/D22', 'Justify the analytic higher-direct-image vanishing for arbitrary coherent ideals on nonreduced infinitesimal fibres, with an exact primary locator.'),
        ('classification_locator', 'Then $K_T$ is torsion and the\nclassification gives Kodaira dimension zero', 'Then $K_T$ is torsion and the\nclassification '+classcite+' gives Kodaira dimension zero', 'D06', 'Move the existing classification citation to its operative use in the normal case.'),
        ('normal_recap', 'This exhausts the normal case.\n', '', 'D08', 'Remove the closing proof recap after all cases have been derived.'),
        ('normalization_intro', 'For completeness,\npull back a local generator', 'Pull back a local generator', 'D08', 'Begin directly with the local generator construction.'),
        ('disputed_scope_tail', '; its local proof does\nnot use the disputed global restriction conclusion.', '.', 'D02', 'Retain the precise conductor-formula citation and remove the retrospective defensive clause.'),
        ('minimal_model', end_old, end_new, 'D06/D08', 'The classification citation is retained at its earlier operative use; state the exact birational transport to the minimal model.'),
    ]),
    '02WL': ('night:P4.14', [
        ('title', '[P4.14]', '[Genus-one curves with nonreduced conductor]', 'D04/D16', 'Replace the internal run title by the mathematical objects.'),
        ('scope_tail', 'classification at that step; they are not counterexamples to\nthe threefold sign assertion.', 'classification at that step.', 'D11', 'The statement already specifies precisely the published curve inference addressed by the two examples.'),
        ('iteration_marker', marker, r'\begin{enumerate}[leftmargin=*]', 'D04', 'Remove the production iteration label and retain the three mathematical proof steps.'),
        ('compact_families', wl_old, wl_new, 'D09/D22', 'Replace program narration and an unsupported possibility with the explicit compact cyclic-quotient constructions, including the exact cover and local conductor maps.'),
    ]),
}

all_guards = []
blocks = []
for tag, (label, rows) in edits.items():
    before = getblock(label)
    after = before
    guards = []
    for suffix, old, new, typ, reason in rows:
        assert before.count(old) == 1, (tag, suffix, 'original', before.count(old))
        assert after.count(old) == 1, (tag, suffix, 'sequence', after.count(old))
        after = after.replace(old, new, 1)
        guards.append({'id': 'II-infra-recovery-'+tag+'-'+suffix,
                       'statement_id': label, 'tag': tag,
                       'source_sha256': src['sha256'],
                       'before': old, 'after': new, 'type': typ, 'reason': reason,
                       'literal_math_map': {'inline_before': inline(old), 'inline_after': inline(new),
                                            'display_before': displays(old), 'display_after': displays(new)},
                       'literal_reference_map': {'before': refs(old), 'after': refs(new)},
                       'comparison_record': 'agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_WJ_WL_comparison.json'})
    paths = {}
    for side, content in [('before', before), ('after', after)]:
        path = out/f'S6_SERIES_PUBLISH_II_{tag}_{side}.tex'
        path.write_text(content)
        key = 'original_full_block' if side == 'before' else 'proposed_full_block'
        paths[key] = str(path.relative_to(ROOT)); paths[key+'_sha256'] = sha(content)
    for guard in guards:
        guard.update(paths)
    all_guards += guards
    blocks.append({'tag': tag, 'statement_id': label, **paths,
                   'guard_ids': [guard['id'] for guard in guards],
                   'displayed_target_statement_conclusions_identical': True,
                   'global_math_reference_sequence_identity_claimed': False,
                   'reason': 'Explicit inherited hypotheses and justified proof expansions/locator transports are recorded guard by guard.'})
    print('COMPLETE PROPOSED BLOCK '+tag+'\n'+after)

s = src['text']
a = re.search(r'\\section\*?\{Programs\}', s).start()
b = s.index(r'\begin{thebibliography}', a)
before = s[a:b]
row = r'''Exact rational jet restrictions at orders $2,3,4,6,8$ and conductor ideals of the two genus-one plane cubics (\cref{night:P4.14}) & \href{https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\SsixRepositoryCommit/pro_returns/S6_06_BLIND_checkpoint_15_20261117T1457Z/S6_06_BLIND/code/part4/genus_one_conductor.py}{\nolinkurl{genus_one_conductor.py}} \\[3pt]
'''
assert row not in before
assert before.count(r'\end{longtable}}') == 1
after = before.replace(r'\end{longtable}}', row+r'\end{longtable}}')
paths = {}
for side, content in [('before', before), ('after', after)]:
    path = out/f'S6_SERIES_PUBLISH_II_WL_program_table_{side}.tex'
    path.write_text(content)
    key = 'original_full_block' if side == 'before' else 'proposed_full_block'
    paths[key] = str(path.relative_to(ROOT)); paths[key+'_sha256'] = sha(content)
all_guards.append({'id': 'II-infra-recovery-02WL-program-table',
                   'statement_id': 'tab:II:programs', 'tag': 'program_table',
                   'source_sha256': src['sha256'], 'before': before, 'after': after,
                   'type': 'D09', 'reason': 'Move the single pinned program citation and exact jet-order scope from the proof into the existing end table; every previous row is byte-preserved.',
                   'transported_inline_math': r'$2,3,4,6,8$',
                   'added_reference': r'\cref{night:P4.14}',
                   'program_receipt': 'records/S6_SERIES_PUBLISH_II_opened_programs_recovery_01/receipt.json',
                   'program_sha256': '5b228e81babc0ff65fd653dcf06ff562afa1a2f0b675a7870e5da180f1ba0155', **paths})
print('COMPLETE PROPOSED PROGRAM SECTION\n'+after)

record = {'created_utc': datetime.now(timezone.utc).isoformat(),
          'source_sha256': src['sha256'], 'status': 'UNAPPLIED; complete pair rereading and root review required',
          'recovery': 'New proposals after two new prereading freezes; no lost old guard bytes or historical timestamps are reconstructed.',
          'guards': all_guards, 'blocks': blocks, 'program_table': paths,
          'mathematical_events_added': 0, 'canonical_files_modified': False,
          'owner_count': 2, 'guard_count': len(all_guards)}
path = AREA/'S6_SERIES_PUBLISH_II_WJ_WL_guards.json'
with path.open('x') as stream:
    json.dump(record, stream, indent=2); stream.write('\n')
print('GUARD_FILE', path.relative_to(ROOT), sha(path.read_bytes()), len(all_guards))
