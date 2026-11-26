from S6_SERIES_PUBLISH_c3_edit import *

s = SOURCE.read_text()
old = r'''The following proofs retain every Part~4 result of the night run. The final classification is Theorem~\ref{night:P4.58}; its exact normalization maps and its local exclusions are proved below.
'''
apply_edit(old, '', 'II-C3-IDENTITY-HISTORY', ['D01', 'D04', 'D07', 'D08'], '',
    'Opening of irreducible-support section',
    'Remove production history and a preview. The classification target and all its proving statements remain in their mathematical positions.')

old = r'''The ambient space is a smooth compact complex threefold $Y$ with $b_1(Y)=b_2(Y)=0$, and $f:Y\to B$ is proper and surjective with connected fibres and smooth general fibre a complex two-torus. Every statement below concerning an irreducible support uses its actual full fibre $mS$, normalization and resolution. The global assertions expressly retaining the hypothesis that every support is irreducible or has normal crossings are used with that hypothesis. Constructions and comparison examples with different Betti numbers state their own assumptions.'''
new = r'''The global torus-fibration setting consists of a smooth compact complex
threefold $Y$ with $b_1(Y)=b_2(Y)=0$ and a proper surjective holomorphic
map $f:Y\to B$ with connected fibres and smooth general fibre a complex
two-torus. For an irreducible support $S$, its full fibre is $mS$;
we use the normalization $\nu:N\to S$ and a resolution
$\sigma:T\to N$. In the irreducible-or-normal-crossings setting,
every reduced fibre support is irreducible or has normal crossings.
Local degenerations and comparison examples have the hypotheses
specified in their statements.'''
apply_edit(old, new, 'II-C3-IDENTITY-SETTING', ['D08', 'D11'],
    'def:II:standing-torus-fibration', 'Standing torus-fibration definition',
    'Express the same ambient hypotheses through the explicit maps f, nu and sigma and name the additional global support hypothesis once. Local examples keep their separately stated domains.')

s = SOURCE.read_text()
left = s.index('Throughout this part we orient complex spaces by their complex structures.')
right = s.index('\\begin{proposition}[An elliptic bundle degeneration]', left)
old = s[left:right]
new = r'''\begin{definition}[The square elliptic curve and its lattice]
\hypertarget{tag-P241}{}\label{def:II:identity-example-lattice}
\StatementRecord{def:II:identity-example-lattice}{proved}{P241}{}
For the compact example in this subsection, put
\[
 E=\C/(\Z+i\Z)=\C^*/q^\Z,\qquad q=e^{-2\pi},\qquad
 A=E^2,\qquad \Lambda=\Z e_1\oplus\Z e_2\oplus\Z e_3\oplus\Z e_4,
\]
where $(e_1,e_2,e_3,e_4)=((1,0),(i,0),(0,1),(0,i))$.
The map $z\mapsto e^{2\pi iz}$ identifies the two displayed presentations
of $E$. Homology in this subsection has coefficients in $\Z$.
A base meridian is counterclockwise in its holomorphic coordinate;
at infinity that coordinate is $1/t$.
\end{definition}

'''
apply_edit(old, new, 'II-C3-IDENTITY-LATTICE', ['D13', 'D20'],
    'def:II:identity-example-lattice', 'Initial data for the compact example',
    'Give the existing elliptic curve, exponential comparison, ordered lattice and meridian convention a numbered owner. The complex orientation is already in the common conventions. Every datum is unchanged.')

s = SOURCE.read_text()
left = s.index('The lattice matrices, with columns $(a_i,c_i,b_i,d_i)$ in the common basis,')
right = s.index('\\begin{proposition}[Fundamental group and first two homology groups]', left)
matrices = s[left:right]
anchor = r'''The threefold $Y$ has $H_1(Y;\Z)=H_2(Y;\Z)=0$ and $\pi_1(Y)=1$.
\end{proposition}
\begin{proof}
'''
new_anchor = r'''The threefold $Y$ of Proposition~\ref{night:P4.2} has
$H_1(Y;\Z)=H_2(Y;\Z)=0$ and $\pi_1(Y)=1$.
\end{proposition}
\begin{proof}
''' + matrices
apply_edit(anchor, new_anchor, 'II-C3-IDENTITY-MATRIX-OWNER', ['D13', 'D22'],
    'night:P4.4', 'Fundamental-group and homology proof: marking matrices',
    'Place the three marking matrices and the exact exterior-power quotient definitions inside the proof that uses them. The threefold is explicitly the object constructed in P4.2. The matrix data are copied exactly.')
# The source now has two exact copies; remove the one before the proposition.
s = SOURCE.read_text()
full = matrices + '\\begin{proposition}[Fundamental group and first two homology groups]'
apply_edit(full, '\\begin{proposition}[Fundamental group and first two homology groups]',
    'II-C3-IDENTITY-MATRIX-MOVE', ['D13'], 'night:P4.4',
    'Paragraph before the fundamental-group and homology proposition',
    'The exact matrices and quotient maps now stand at the beginning of their owning proof; remove the former orphan copy.')

old = r'''This proves surjectivity of $F_2$ over $\Z$ and excludes torsion. The
executed independent Smith calculation gives fifteen unit factors for
$F_1$ and twenty-nine unit factors for $F_2$, and computes $\det F_1=-1$.'''
new = r'''Thus $F_2$ is surjective over $\Z$. In the specified ordered bases,
$\det F_1=-1$, and the Smith normal forms of $F_1$ and $F_2$
have fifteen and twenty-nine unit invariant factors, respectively.'''
apply_edit(old, new, 'II-C3-IDENTITY-SMITH', ['D07', 'D08', 'D09', 'D21'],
    'night:P4.4', 'Integral homology proof, fourth item',
    'State the exact matrix conclusions. Integral elimination in the preceding lines proves them; the exposed entrywise comparison also confirms both Smith forms and det F1. Remove the history of the calculation.')

s = SOURCE.read_text()
left = s.index('The program \\texttt{code/part4/example\\_mayer\\_vietoris.py}')
right = s.index('\\begin{proposition}[Invariants of the compact torus fibration]', left)
apply_edit(s[left:right], '', 'II-C3-IDENTITY-ARRAY-DUPLICATES', ['D09', 'D12', 'D13'],
    'night:P4.3;night:P4.4', 'Matrix appendix following the homology proof',
    'Every one of the 18 arrays is reproduced exactly by the retained marking matrices, exterior-power quotient maps, cellular differentials and Mayer--Vietoris blocks. code/S6_SERIES_PUBLISH_c3_example_matrices.py checks every entry, differential composite, determinant and Smith factor. The full arrays duplicate those definitions. Their historical program is retained once in the Programs table; no mathematical map or invariant is removed.')

s = SOURCE.read_text()
left = s.index('\\item We also have $H^2(Y;\\Z)=0$.', s.index('\\begin{proposition}[Invariants of the compact torus fibration]'))
right = s.index('\n\\end{enumerate}', left)
old = s[left:right]
new = r'''\item Proposition~\ref{night:P4.4} gives $H^2(Y;\Z)=0$.
The regular fibre $A=E^2$ is K\"ahler, and
Proposition~\ref{night:P4.2} gives a proper surjection with connected
fibres. Proposition~\ref{cdp:st:E1}, applied to this map $f$, therefore
identifies the meromorphic function fields through
$f^*:\C(\Pp^1)\xrightarrow{\sim}\C(Y)$ and gives $a(Y)=1$.
'''
apply_edit(old, new, 'II-C3-IDENTITY-VERTICAL-APPLICATION', ['D12'],
    'night:P4.5', 'Invariants proof, second item',
    'The earlier E1 proves exactly the divisor and meromorphic-descent argument repeated here. The replacement checks its domain, H2 vanishing, connected-fibre surjection and Kahler-fibre hypothesis, and names the same pullback field isomorphism. The complete original E1 and both P4.5 proofs were read.')
print('Identity-monodromy example revised; comparison events and unit closure follow the receiving-text reading.')
