#!/usr/bin/env python3
"""Edit one wholly read later unit; local records only, no central writes."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import csv
import difflib
import re
import S6_SERIES_PUBLISH_c8_integrate_presentation as presentation
import S6_SERIES_PUBLISH_c8_integrate_units as units

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'agents/continuation8_iii_integration/units/later/elliptic_additive_profiles.tex'
OUT = ROOT / 'agents/continuation8_iii_later'
OLD_HASH = 'fefb559d49826513822cf10043f2ee00b4a05fc9237165b07ac79602f5734a49'
old = PATH.read_text()
assert sha256(old.encode()).hexdigest() == OLD_HASH
now = datetime.now(timezone.utc).isoformat()
new = old
edits = []

# Compare the complete extracted proofs to their admitted receivers. The
# only three extraction differences are these explicit blank-line maps;
# each displayed map is inverted and checked, rather than normalized away.
folders = {'02KR': 'continuation7_iii_kr', '02KS': 'continuation7_iii_ks',
           '02KV': 'continuation7_iii_original_caps', '02KW': 'continuation7_iii_original_caps'}
for tag, folder in folders.items():
    p = ROOT / 'agents' / folder / ('S6_SERIES_PUBLISH_III_' + tag + '_receiving.tex')
    expected = p.read_text().strip() + '\n'
    a = old.index(r'\hypertarget{tag-' + tag + '}')
    a = old.rfind(r'\begin{', 0, a)
    b = old.index(r'\end{proof}', a) + len(r'\end{proof}')
    actual = old[a:b] + '\n'
    x, y = r'\end{theorem}' + '\n\n' + r'\begin{proof}', r'\end{theorem}' + '\n\n\n' + r'\begin{proof}'
    if tag in {'02KS', '02KV'}:
        assert expected.count(x) == 1
        transported = expected.replace(x, y, 1)
        assert transported.replace(y, x, 1) == expected
    elif tag == '02KW':
        y = r'\end{theorem}' + '\n' + r'\begin{proof}'
        assert expected.count(x) == 1
        transported = expected.replace(x, y, 1)
        assert transported.replace(y, x, 1) == expected
    else:
        transported = expected
    assert actual == transported, tag
    print('WHOLE_ADMITTED_RECEIVER_MAP', tag, len(actual.splitlines()), sha256(p.read_bytes()).hexdigest())


def owner(text, position):
    candidates = list(re.finditer(r'\\begin\{(?:corollary|theorem|definition)\}.*?\\label\{([^}]+)\}', text[:position + 1], re.S))
    return candidates[-1][1] if candidates else 'maps:src:D.2.17'


def change(before, after, kind, reason, count=1, sid=None):
    global new
    assert new.count(before) == count, (before, new.count(before), count)
    positions = [m.start() for m in re.finditer(re.escape(before), new)]
    for pos in positions:
        edits.append(dict(change_id='c8-III-additive-' + str(len(edits) + 1).zfill(3),
                          type=kind, statement_id=sid or owner(new, pos),
                          old_location='elliptic_additive_profiles.tex, sequential edit line ' + str(new[:pos].count('\n') + 1),
                          old_page='pending final page concordance',
                          new_location='elliptic_additive_profiles.tex, corresponding retained statement',
                          new_page='pending final build', old_text=before, new_text=after,
                          reason=reason,
                          review_status='whole repaired input and admitted comparisons read; final source readback and root unit admission pending'))
    new = new.replace(before, after)


change(r'\begin{corollary}[Two further original additive profiles]',
       r'\subsection{Original additive profiles}' + '\n' +
       r'\subsubsection{Two additive profiles}' + '\n' +
       r'\begin{corollary}[Original profiles of types II and IV]', 'D14',
       'Give this complete unit its mathematical subsection and place the two-profile corollary first; remove the relative further title.')
change(r'\hypertarget{tag-02KR}{}\label{maps:src:D.2.17}',
       r'\hypertarget{tag-02KR}{}\label{maps:src:D.2.17}' + '\n' +
       r'{\normalfont\scriptsize tag 02KR}\par', 'D10', 'Print the existing small tag with its preserved permanent identity.')
for tag in ['02KS', '02KV', '02KW']:
    before = r'\textnormal{\small tag02KS.}' if tag == '02KS' else r'\textup{\small(tag ' + tag + ')}'
    change(before, r'{\normalfont\scriptsize tag ' + tag + r'}\par', 'D10',
           'Use the common small-tag form while preserving the permanent label and target.')

definition = r'''\subsubsection{The three-component cusp}
\begin{definition}[The complex flag threefold]\hypertarget{tag-Q300}{}\label{maps:def:complex-flag-threefold}
{\normalfont\scriptsize tag Q300}\par
The complex flag threefold is the incidence variety
\[
 \operatorname{Fl}(\mathbb C^3)=
 \{(L,P)\in\mathbb P^2\times(\mathbb P^2)^*:L\subset P\},
\]
where $L$ is a line and $P$ is a plane in $\mathbb C^3$.
We give it its complex orientation.
\end{definition}

'''
change(r'\begin{theorem}[Three-component cusp with original additive fillings]',
       definition + r'\begin{theorem}[Three-component cusp with original additive fillings]',
       'D13', 'Move the incidence-variety definition before its first theorem use and number it. Its ring, characteristic and recognition proofs remain inside the sole KS proof.', sid='maps:src:D.2.18')
change(r'''Define the comparison manifold concretely as

\[
 F=\{(L,P)\in\mathbb P^2\times(\mathbb P^2)^*:L\subset P\}.
\]
''', r'''Put $F=\operatorname{Fl}(\mathbb C^3)$ as in
Definition~\ref{maps:def:complex-flag-threefold}.
''', 'D13', 'Use the preceding numbered definition; the object and complex orientation are identical, and no proof step is removed.')
change(r'\begin{theorem}[Six original additive families]',
       r'\subsubsection{Six primitive original families}' + '\n' + r'\begin{theorem}[Six original additive families]',
       'D14', 'Separate the P=G, Q=dG families after the original-cusp refinement; preserve all component line data and both zero/nonzero normal cases.')
change(r'\begin{theorem}[One original additive fibre and one finite logarithm]',
       r'\subsubsection{A mixed original and logarithmic pair}' + '\n' + r'\begin{theorem}[One original additive fibre and one finite logarithm]',
       'D14', 'Place the mixed finite-cap theorem immediately after the original-cap theorem supplying its maps.')

# Each phrase was read in its complete proof. These are explicit local
# prose edits, not a vocabulary substitution pass over unexamined text.
phrases = [
 (r'\emph{The actual marking and the line.}', r'\emph{The marking and the line.}'),
 ('apply to these actual contractions.', 'apply to these contractions.'),
 ('its actual ten-coordinate cap source.', 'its ten-coordinate cap source.'),
 (r'the actual loop $\gamma$ in the reverse direction.', r'the loop $\gamma$ in the reverse direction.'),
 ('coordinate, and every $H_2$ torsion coordinate now coincide with', 'coordinate, and every $H_2$ torsion coordinate coincide with'),
 ('The Euler class is now zero on the whole punctured $Q$, because it', 'The Euler class is zero on the whole punctured $Q$, because it'),
 (r'Thus it gives the actual map $X\to\widetilde\Sigma_0Q$.', r'Thus it gives the map $X\to\widetilde\Sigma_0Q$.'),
 ('image. Exactness and the normal boundary map now give the integral splitting', 'image. Exactness and the normal boundary map give the integral splitting'),
 ('For the star, let us construct its mapping-torus model over the\noriginal neighbourhood.', 'For the star, use the mapping-torus construction over its\noriginal neighbourhood.'),
 (r'norm. The argument of \(a_*\) is retained in the angular', r'norm. The argument of \(a_*\) enters the angular'),
 ('For clarity, the degree-one eliminations in this assertion include', 'The degree-one eliminations in this assertion include'),
 (r'now give, for \(n\ne0\),', r'give, for \(n\ne0\),'),
 ('with all period units retained.', 'with the period units in the multiplier.'),
 (r'and its inverse now give \(S^2\times D^4\) with scalar action.', r'and its inverse give \(S^2\times D^4\) with scalar action.'),
 ('construction used in the type-II product model now gives an explicit trivialization of', 'construction used in the type-II product model gives an explicit trivialization of'),
 ('fixed normal pieces restored. Its boundary is now parametrized as', 'fixed normal pieces restored. Its boundary is parametrized as'),
 ('the inverse correction. The maps now glue on full collars to an', 'the inverse correction. The maps glue on full collars to an'),
 ('and has a smooth increasing inverse. Together with the corrected\nangular isotopy', 'and has a smooth increasing inverse. Together with the\nangular isotopy with its endpoint adjustment'),
 ('For completeness, every component coefficient is an invariant', 'Every component coefficient is an invariant'),
 (r'The actual outer rim $\mu\times x$ has connecting coordinates', r'The outer rim $\mu\times x$ has connecting coordinates'),
 ('three actual rims denoted', 'three rims denoted'),
 ('actual rims and chosen lifts', 'rims and chosen lifts'),
 ('with the actual rims;', 'with the rims;'),
 ('Integral duality and universal coefficients now give', 'Integral duality and universal coefficients give'),
 ('independent of a line frame and invariant under the actual\ncontracting lift:', 'independent of a line frame and invariant under the\ncontracting lift:'),
 (r'Now $H_2(Q)=\mathbb Z^7\oplus(\mathbb Z/m)^2$.', r'We have $H_2(Q)=\mathbb Z^7\oplus(\mathbb Z/m)^2$.'),
 ('the exterior order $(12,13,14,23,24,34)$, and the actual period', 'the exterior order $(12,13,14,23,24,34)$, and the period'),
 ('The original line and translation on the retained additive', 'The original line and translation on the original additive'),
 ('boundary connected sum of the retained original disc and the', 'boundary connected sum of the original disc and the'),
 (r'The last column gives the actual $\ell$ rim', r'The last column gives the $\ell$ rim'),
 (r'Choose the actual rim $w$, including its component-chain part,', r'Choose the rim $w$, including its component-chain part,'),
 ('actual lifts, and read the remaining component coordinates.', 'lifts, and read the remaining component coordinates.'),
 ('the actual rim. Thus this calculation retains precisely the\ncyclic class eliminated above.', 'the rim and its component-chain part. These inverse subdivision maps\nidentify the cyclic relation in the two presentations.'),
 ('quotient and extends across the retained caps by the node and', 'quotient and extends across the original caps by the node and'),
 ('The actual cusp divisor is the self-identified whole fibre:', 'The cusp divisor is the self-identified whole fibre:'),
 (r'Now $Q$ is simply connected and spin with $H_2(Q)=\mathbb Z^b$.', r'The quotient $Q$ is simply connected and spin with $H_2(Q)=\mathbb Z^b$.'),
]
for before, after in phrases:
    change(before, after, 'D08', 'State the displayed mathematical map or consequence directly; its domain, formula, inverse and parameter scope remain unchanged.')

change('The maps are alternating inclusions of the strata. To specify them\nwithout a lattice substitution, take vertex representatives',
       'The maps are alternating inclusions of the strata. Take vertex representatives', 'D02',
       'Specify the signed conductor maps directly; all vertex, edge and triangle prescriptions remain.')
change('Reverse radial transport is its inverse. Thus no missing cap\ngenerator enters van Kampen, and the quotient and inverse are',
       'Reverse radial transport is its inverse. The boundary images generate\neach cap group, so the quotient and inverse are', 'D02',
       'State the proved boundary-generation property used in van Kampen positively.')
change(r'There is no additional torsion in the kernel of \(\Theta\). The subgroup',
       'The kernel is determined integrally as follows. The subgroup', 'D02',
       'Keep the full two-generator/direct-summand argument and its zero graph homomorphism, which explicitly determines the kernel and every torsion coordinate.')
change(r'fixed \(V\). There is no other degree-two functional there.',
       r'fixed \(V\). The outside degree-two group is generated by the functional dual to \(V\).', 'D02',
       'Use the previously proved outside H2 group and its integral dual to state the extension criterion positively.')
change('The normalization has the stated conductor identifications; its\nintrinsic canonical square does not replace this divisor calculation.',
       'The conductor identifications and the whole-fibre Cartier map\ndetermine these divisor products.', 'D02',
       'Retain the complete Cartier/Thom computation of the self-identified whole fibre and remove the defensive normalization comparison.')
change('The positive base meridian has zero contracting coordinate:\nchoose a constant fractional roof coordinate on the base circle.\nNo contracting iterate is made after one turn. It is therefore',
       'The positive base meridian has zero contracting coordinate:\nchoose a constant fractional roof coordinate on the base circle.\nThat coordinate returns to its starting value after one turn, so the meridian is', 'D02',
       'Express the returning roof coordinate directly; its zero contracting class and swept-disc proof remain.')
change('projects to zero in $H_2(E_i)$. Hence there is no additional\ncomponent coefficient, and the displayed formula is the full\nintegral map.',
       'projects to zero in $H_2(E_i)$. These two evaluations determine\nevery component coefficient, giving the full integral map.', 'D02',
       'Use the proved two-dimensional invariant row space to state completeness of the component map directly.')
change('One can express the same integral elimination on the full\nregular-base graph.',
       'On the full regular-base graph, the integral elimination has the\nfollowing coordinates.', 'D08',
       'Present the required graph transfer coordinates as part of the same proof; retain every finite/original cap map and the explicit inverse subdivision relating the presentations.')

# Orthography and the already admitted source locator, occurrence by occurrence.
change('Cech', r'\v{C}ech', 'D23', 'Typeset the standard name consistently with its diacritic.', count=5)
change('Poincare', r"Poincar\'e", 'D23', 'Typeset the standard name consistently with its diacritic.', count=2)
change(r'\cite[\S2.4, equation (2.2)]{manUU21}',
       r'\cite[\S2.4, equation (2.2), p.~6]{manUU21}', 'D18',
       'Supply the exact page already opened and recorded in the admitted KR/KS/KV-KW primary-reading scopes; no new primary reading is claimed.', count=2)

# The bounded helper returns exact D19 operations on displays already read.
numbered, numbering, issues, aliases = presentation.remove_manual_equation_tags(new)
assert not issues, issues
for edit in numbering:
    edits.append(dict(change_id='c8-III-additive-' + str(len(edits) + 1).zfill(3),
                      type=edit.kind, statement_id=owner(new, edit.start),
                      old_location='elliptic_additive_profiles.tex, numbering stage line ' + str(new[:edit.start].count('\n') + 1),
                      old_page='pending final page concordance',
                      new_location='same retained equation label', new_page='pending final build',
                      old_text=edit.old, new_text=edit.new, reason=edit.reason,
                      review_status='bounded D19 display conversion after whole proof reading; global counters and rendered review pending'))
new = numbered
literal_issues = presentation.unresolved_literal_equation_references(new, aliases)
assert not literal_issues, literal_issues
units.check_permanent_identifiers(old, new,
    ['maps:def:complex-flag-threefold'], ['tag-Q300'])
assert new.count(r'\begin{proof}') == new.count(r'\end{proof}') == 4
assert new.count(r'\begin{definition}') == new.count(r'\end{definition}') == 1
assert new.count(r'\begin{theorem}') == 3 and new.count(r'\begin{corollary}') == 1
assert '\r' not in new
OUT.mkdir(exist_ok=True)
defect_path = OUT / 'S6_SERIES_PUBLISH_III_additive_publication_defects.tsv'
with defect_path.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, list(edits[0]), delimiter='\t', lineterminator='\n')
    writer.writeheader(); writer.writerows(edits)
diff = ''.join(difflib.unified_diff(old.splitlines(True), new.splitlines(True),
                                  fromfile='admitted_additive_profiles', tofile='publication_additive_profiles'))
(OUT / 'S6_SERIES_PUBLISH_III_additive_publication.diff').write_text(diff, newline='\n')
PATH.write_text(new, newline='\n')
print('UTC', now)
print('INPUT', len(old.splitlines()), OLD_HASH)
print('OUTPUT', len(new.splitlines()), sha256(new.encode()).hexdigest())
print('EXACT_LOCAL_DEFECT_ROWS', len(edits), 'D19_DISPLAY_EDITS', len(numbering))
print('NEW_ID', 'Q300', 'maps:def:complex-flag-threefold')
print('PERMANENT_IDENTIFIERS_PRESERVED', True, 'FOUR_SOLE_PROOFS', True)
print('UNRESOLVED_LITERAL_REFERENCES', len(literal_issues))
print('NO_CANONICAL_OR_CENTRAL_WRITES; NO_MECHANICAL_CRITERION_CREDIT')
