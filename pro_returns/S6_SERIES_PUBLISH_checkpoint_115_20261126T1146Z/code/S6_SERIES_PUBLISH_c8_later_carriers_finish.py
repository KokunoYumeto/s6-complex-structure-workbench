#!/usr/bin/env python3
"""Apply bounded corrections found by whole final carrier reading."""
from pathlib import Path
from collections import Counter
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'agents/continuation8_iii_integration/units/later/further_cusp_carriers.tex'
DEFECTS = ROOT / 'agents/continuation8_iii_later/S6_SERIES_PUBLISH_III_carriers_publication_defects.tsv'
before = PATH.read_text()
assert len(before.splitlines()) == 3246
text = before
with DEFECTS.open(newline='') as stream:
    reader = csv.DictReader(stream, delimiter='\t')
    fields = reader.fieldnames
    rows = list(reader)
assert len(rows) == 59

def edit(old, new, kind, owner, reason):
    global text
    assert text.count(old) == 1, (owner, old[:100], text.count(old))
    pos = text.index(old)
    rows.append(dict(change_id='c8-III-carriers-' + str(len(rows) + 1).zfill(3),
        type=kind, statement_id=owner,
        old_location='further_cusp_carriers.tex final-readback line ' + str(text[:pos].count('\n') + 1),
        old_page='pending final concordance', new_location=owner,
        new_page='pending final build', old_text=old, new_text=new,
        reason=reason, review_status='changed text awaiting immediate whole readback'))
    text = text[:pos] + new + text[pos + len(old):]

edit(r'''Choose a diffeomorphism $X\to S^6$ from
Theorem~\ref{wb:cusp-spec-globalization-obstruction} and compose it
with a rotation sending the image of $x_0$ to infinity.
On the two nonbasepoint factors, stereographic coordinates give
$(\mathbb R^6)^2$.  The collapsed fat wedge is the point at infinity
of that open complement, so the resulting homeomorphism to
$(\mathbb R^{12})^+=S^{12}$ proves
\eqref{wb:cusp-cone-S12-source}.''',
r'''Take the diffeomorphism $h:X\to S^6$ from
\cref{wb:cusp-spec-globalization-obstruction} and a rotation $R$
with $Rh(x_0)=\infty$. Apply the ordered source homeomorphism of
\eqref{wb:cusp-spec-smash-spheres} to $h_0=Rh$.
On nonbasepoint factors it concatenates the stereographic coordinates
of $h_0$; its inverse splits the two blocks and applies inverse
stereographic projection followed by $h^{-1}R^{-1}$.
The basepoints correspond, giving \eqref{wb:cusp-cone-S12-source}.''',
'D12/D20', 'wb:cusp-cone-S12-route',
'Use the earlier sphere-smash proof, retaining the exact rotation needed for the cusp basepoint and both ordered coordinate maps.')

edit(r'''Choose a based diffeomorphism $X\to S^6$ using
Theorem~\ref{wb:cusp-spec-globalization-obstruction}.
Stereographic coordinates on the four nonbasepoint factors identify
the complement of the collapsed fat wedge with $(\mathbb R^6)^4$;
the collapsed point is its point at infinity.  This gives the based
homeomorphism $X^{\wedge4}\cong S^{24}$.''',
r'''Use the based diffeomorphism $h_0$ of
\cref{wb:cusp-cone-S12-route}. The four-block source homeomorphism
of \eqref{wb:cusp-spec-smash-spheres}, with its block-splitting
inverse followed by $h_0^{-1}$ in sphere coordinates, gives
$X^{\wedge4}\cong S^{24}$.''',
'D12/D20', 'wb:cusp-cone-S24-local-route',
'Cite the same earlier ordered sphere-smash proof for four factors, with the unchanged cusp basepoint and inverse.')

edit(r'''The based
stereographic construction in Proposition~\ref{wb:cusp-cone-S24-local-route}
gives \eqref{wb:cusp-cone-S24-source}.''',
r'''The based source homeomorphism in
Proposition~\ref{wb:cusp-cone-S24-local-route}
gives \eqref{wb:cusp-cone-S24-source}.''',
'D12', 'wb:cusp-cone-S24-route',
'Make the reference identify the earlier based homeomorphism, whose sole proof is cited there.')

edit(r'''A based diffeomorphism $X\cong S^6$ gives
the source homeomorphisms $X^{\wedge2}\cong S^{12}$ and
$X^{\wedge4}\cong S^{24}$ through one-point compactification of
the products of the Euclidean complements of the basepoints.''',
r'''The source homeomorphisms and their inverses are the ordered
two- and four-block maps of
\cref{wb:cusp-cone-S12-route,wb:cusp-cone-S24-local-route},
based at the same point of $W$.''',
'D12/D20', 'wb:cusp-cone-target-homotopy-types',
'Use the established source identifications in the homotopy-type theorem without repeating their proof.')

start = text.index(r'\begin{definition}[Radial target-slice maps]')
end = text.index(r'\end{proof}', start) + len(r'\end{proof}')
old = text[start:end]
new = old.replace(r'\partial M=', r'\partial\mathcal M=')
new = new.replace(r'\mathcal C=M\cup', r'\mathcal C=\mathcal M\cup')
new = new.replace(r'\(M\)', r'\(\mathcal M\)')
new = new.replace(r'\(M\to', r'\(\mathcal M\to')
new = new.replace(r'\subset M\)', r'\subset\mathcal M\)')
assert new != old
edit(old, new, 'D20', 'wb:cusp-cone-target-slice-embeddings; mapsIII:lem:radial-slice-embeddings',
     'Use the already defined symbol mathcal M throughout the definition and proof; the attached manifold and every inclusion remain the identical object.')

edit(r'''with the two maps of the cited proposition, through the displayed
target homeomorphisms. That proposition supplies their based
null-homotopies, fixing the chosen \(x_0\in W\), and the based
null-homotopy of every positive smash power.''',
r'''with the two maps of Definition~\ref{mapsIII:def:cusp-suspension-maps},
through the displayed target homeomorphisms.
Proposition~\ref{mapsIII:angle-forgotten-one-copy-null} supplies their
based null-homotopies, fixing the chosen \(x_0\in W\), and the based
null-homotopy of every positive smash power.''',
'D04/D20', 'wb:cusp-cone-sphere-map-homotopy-status',
'Name Q011 as the definition of the maps and 02Q7 as their null-homotopy theorem, eliminating the ambiguous antecedent after the explicit alpha/beta transport.')

for old, new, owner in [
    ('with its actual\ndomains and targets.', 'with these domains and targets.', 'wb:cusp-cone-S12-route'),
    ('related to the actual\ntorus', 'related to the boundary\ntorus', 'wb:cusp-cone-target-slice-embeddings'),
    ('The strict radial scope is necessary for the common assertion.  At', 'The endpoint maps are as follows. At', 'mapsIII:lem:radial-slice-embeddings'),
    ('These are actual singular loci of the two completed products.', 'These equations exhibit singular loci in both completed products.', 'wb:cusp-cone-obstructions'),
    ('gives the actual gluing\nto', 'gives the gluing\nto', 'wb:cusp-cone-optimal-exponents'),
    ('well defined on the actual period lattices,', 'well defined on these period lattices,', 'wb:cusp-cone-explicit-carriers'),
    ('is an actual boundary fibre of', 'is a boundary fibre of', 'wb:cusp-cone-exact-decompactification-space'),
]:
    edit(old, new, 'D08/D11', owner,
         'Replace an editorial qualifier by the mathematical object or map already displayed; no formula or scope changes.')

section = r'\section{Compact carriers and Euclidean boundary fibres}'
boundary_end = text.index(section)
boundary_start = text.rfind(r'\end{proof}', 0, boundary_end)
assert not text[boundary_start + len(r'\end{proof}'):boundary_end].strip()
edit(text[boundary_start:boundary_end + len(section)],
     '\\end{proof}\n\n\\section{Compact carriers and Euclidean boundary fibres}',
     'D23', 'wb:cusp-cone-moving-S4-null-homotopy',
     'Remove the blank-line residue of the complete 037K relocation; preserve the actual section boundary.')

def identities(s):
    return Counter(re.findall(r'\\(?:label|hypertarget)\{([^}]+)\}', s))
assert identities(before) == identities(text)
assert '\\partial M=' not in text[text.index(r'\begin{definition}[Radial target-slice maps]'):text.index(r'\begin{proposition}[Intrinsic and ambient slice metrics]')]
PATH.write_text(text)
with DEFECTS.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
print('Bounded final-readback edits:', len(rows) - 59)
print('Exact defects rows:', len(rows))
print('Every label and target multiplicity preserved; no shared file changed.')
print('Final source lines:', len(text.splitlines()))
