"""Place the two later-section proof references after their exact owners."""
from S6_SERIES_PUBLISH_c3_edit import *

before = SOURCE.read_text()
after = before
rows = []

def record(key, kinds, ids, old, new, reason):
    for n, kind in enumerate(kinds, 1):
        rows.append(dict(change_id=f'{key}-{n:02}', type=kind,
            statement_id=ids, old_location='Current body before the global order pass',
            old_page='800-page working PDF', new_location='Exact dependency order in the body',
            new_page='next integrated build', old_text=old, new_text=new,
            reason=reason,
            review_status='Root read complete old and receiving statements and proofs and the exact identity applications. All labels and tags retain their multiplicities. No independent derivation or final-page credit.'))

start = before.index(r'\subsection{Hopf axes and canonical-order ratios}')
end = before.index(r'\subsection{Logarithmic period families}', start)
hopf = before[start:end]
anchor = r'\subsection{Diagonal Hopf components in compact torus fillings}'
assert after.count(hopf) == after.count(anchor) == 1
after = after.replace(hopf, '', 1).replace(anchor, hopf + anchor, 1)
labels = {m[1]:m.start() for m in re.finditer(r'\\label\{([^}]+)\}', after)}
start_hopf = after.index(hopf)
for ref in re.finditer(r'\\(?:[Cc]ref|[Ee]qref|ref|SeriesRef)\*?\{([^}]+)\}', hopf):
    for target in ref[1].split(','):
        target = target.strip()
        if target in labels:
            assert labels[target] < start_hopf + len(hopf), target
record('DII-C3-HOPF-AXES-BEFORE-OCCURRENCE', ['D14'],
    'cdp:st:C.2.UN.40', hopf, hopf,
    'Move the complete unchanged Hopf-axis subsection before the diagonal and nonlinear Hopf occurrence constructions. '
    'The UN42 canonical-order calculation now follows the exact UN40 divisor identity it cites. '
    'All premises of UN40 are earlier or internal. This is a byte-preserving move, with no unit subdivision or proof change.')

start = before.index(r'\begin{proposition}[Euler equality under trivial torus monodromy]')
end = before.index(r'\subsection{Extension of periods and coherent direct images}', start)
old = before[start:end]
new = r'''\begin{proposition}[Euler equality under trivial torus monodromy]
\hypertarget{tag-01G9}{}\label{cdp:st:D.2.2}
\StatementRecord{cdp:st:D.2.2}{proved}{01G9}{\cref{cdp:st:C.2.G.1,cdp:st:D.2.5,cdp:st:D.2.7}}
\hypertarget{tag-01GB}{}\label{cdp:st:D.2.4}
\StatementRecord{cdp:st:D.2.4}{proved}{01GB}{}
The class of smooth compact connected complex threefolds with $b_1=b_2=0$,
a proper surjective holomorphic map with connected fibres onto a smooth compact curve,
smooth two-torus general fibre, and trivial rational monodromy is nonempty.
Every member satisfies
\[
 c_3(Y)=0,\qquad b_3(Y)=2.
\]
Every individual reduced fibre support has Euler number zero and
the geometric description of \cref{cdp:st:C.2.G.1}.
Arbitrary singularities and full-fibre multiplicities are allowed.
There is an example with normal-crossing reduced supports,
integral $H_1(Y,\Z)=H_2(Y,\Z)=0$, and algebraic dimension one.
\end{proposition}
\begin{proof}
Apply \cref{cdp:st:C.2.G.1,cdp:st:D.2.5} to the same
threefold $Y$ and map $f$. The first theorem identifies the
base with $\PP^1$, as required by the second proposition.
Their lower and upper bounds give $c_3(Y)=0$.
Poincar\'e duality gives $b_3(Y)=2-c_3(Y)=2$.
The Euler sum and equality criterion of \cref{cdp:st:C.2.G.1}
apply to these same full fibres with their given multiplicities;
each nonnegative summand is zero and has the stated geometric form.
This applies in particular to every member with normal-crossing
reduced supports. The construction in \cref{cdp:st:D.2.7}
has such supports, the stated integral homology and algebraic
dimension, and identity integral monodromy. It therefore proves
nonemptiness of both the full class and this subclass.
\end{proof}

'''
preserve_identifiers(old, new)
assert after.count(old) == 1
after = after.replace(old, '', 1)
g1 = after.index(r'\begin{theorem}[The Euler sign for every degeneration and its equality criterion]')
g1_end = after.index(r'\end{proof}', g1) + len(r'\end{proof}')
after = after[:g1_end] + '\n\n' + new + after[g1_end:]
record('DII-C3-EULER-MONODROMY-SINGLE-OWNER', ['D12','D14'],
    'cdp:st:D.2.2;cdp:st:D.2.4', old, new,
    'The normal-crossing assertion D2.4 is the restriction of D2.2 along the identity maps on the identical Y and f, '
    'with unchanged full-fibre multiplicities. Merge both permanent identities into one proposition, preserving '
    'the normal-crossing example supplied by D2.7. Place its full proof after G1, whose lower bound and equality '
    'description are its premises. The proof now explicitly supplies the base-isomorphism premise of D2.5. '
    'No hypothesis or conclusion is discarded and this resolved duplication supplies no new progress credit.')

old_heading = r'\subsection{Euler equality and the normal-crossing subclass}'
new_heading = r'\subsection{The Euler upper bound under trivial monodromy}'
assert after.count(old_heading) == 1
after = after.replace(old_heading, new_heading, 1)
record('DII-C3-EULER-UPPER-BOUND-HEADING', ['D14','D24'],
    'cdp:st:D.2.5', old_heading, new_heading,
    'The unchanged D2.5 upper-bound proposition and its full proof remain in this subsection; '
    'its equality consequences now follow the general lower bound. Name the material that remains.')

old_item = r'\item \cref{cdp:st:D.2.4}\quad Euler number in the normal-crossings class.'
old_main = r'\item \cref{cdp:st:D.2.2}\quad Euler equality under trivial torus monodromy.'
new_item = r'\item \cref{cdp:st:D.2.2}\quad Euler equality under trivial torus monodromy, including normal-crossing supports.'
assert after.count(old_item) == after.count(old_main) == 1
after = after.replace(old_item + '\n', '', 1).replace(old_main, new_item, 1)
record('DII-C3-FURTHER-EULER-MONODROMY-OWNER', ['D12','D24'],
    'cdp:st:D.2.2;cdp:st:D.2.4', old_item + '\n' + old_main, new_item,
    'The two Further-results entries now point to one complete proposition through both preserved permanent identities. '
    'The one-line entry states both the full scope and the normal-crossing specialization.')

preserve_identifiers(before, after)
assert identifiers(before) == identifiers(after)
assert after.count(hopf) == 1
protected = ['push:src:E.5.2','push:src:E.5.3']
for label in protected:
    def statement(t):
        p = t.index(r'\label{' + label + '}')
        q = t.find(r'\end{', p)
        return t[p:q]
    assert statement(before) == statement(after)
SOURCE.write_text(after, newline='\n')
print('Defect rows:', append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv', rows, 'change_id'))
fields, progress = read_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
for row in progress:
    if row['paper']=='II' and row['unit_id']=='cdp:st:D.2.5':
        row['unit_title']='The Euler upper bound under trivial monodromy'
write_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv', fields, progress)
add_event('II', 'II-C3-FORWARD-DEPENDENCIES-PLACEMENT',
    'used and rechecked in this run',
    'A source-wide read-only proof-reference check found two later-section mathematical targets. '
    'Root fully read the UN40 Hopf-axis statement/proof and moved its exact unchanged subsection before its UN42 occurrence application; '
    'all its premises are earlier or internal. Root fully read D2.2 and D2.4 with both proofs, the D2.1 hypotheses, '
    'the complete D2.5 proof and D2.7 example statement, and the new combined receiving statement/proof. '
    'The D2.4 subclass is the identity restriction of D2.2 on the same Y,f and full fibres. Both permanent identities '
    'now belong to one proposition after G1, with the D2.7 normal-crossing example and the exact G1 base identification '
    'required by D2.5. Its old subsection is named for the unchanged upper-bound result. '
    'The duplicated Further-results lines are one entry. No required-check, independent derivation, original-row movement '
    'or final-page credit; final whole-paper order remains open while the final packages are being admitted.',
    'UN40, UN42, D2.1--D2.5, D2.7 and G1; code/S6_SERIES_PUBLISH_c3_order_review.py',
    source='code/S6_SERIES_PUBLISH_c3_forward_order.py')
print('Two statement dependencies placed after their owners; normal-crossing Euler specialization has one owner.')
