"""Stage the single complete retained-angle proof with all original scopes."""
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r

rp = u.WORK / 'root/retained_angle.tex'
qp = u.WORK / 'root/quotient_maps.tex'
old = rp.read_text()
quotient = qp.read_text()
j7start = quotient.index(r'\begin{theorem}[The retained-angle homotopy class]')
j8start = quotient.index(r'\begin{theorem}[Null-homotopies after forgetting the angle]')
j7block = quotient[j7start:j8start]
j7statement = j7block[:j7block.index(r'\end{theorem}') + len(r'\end{theorem}')]
newquotient = quotient[:j7start] + quotient[j8start:]

diff_start = old.index(r'\paragraph{The full differential and its ordered normal framing}')
orientation_start = old.index(r'\begin{lemma}[Orientation of the cusp torus]')
contraction_start = old.index(r'\paragraph{An explicit contraction of the full frame}')
framing_start = old.index(r'\begin{proposition}[Stable framing of the cusp torus]')
spin_start = old.index(r'\paragraph{Nonzero framed bordism and the exact unstable class}')
main_start = old.index(r'\begin{proof}[Expanded proof of \cref{maps:src:B.3.1}]')
remark_start = old.index(r'\paragraph{Exact scope of the comparison with the angle-forgetting map.}')
cor_start = old.index(r'\begin{corollary}[Order-two quotient detected by the cusp map]')

coordinates = old[:diff_start]
data_start = coordinates.index(r'\paragraph{Original coordinates and the specified sphere-valued map}')
coordinates = r'''\subsection{The regular cusp torus}
\hypertarget{tag-03BF}{}\label{wb:h24:ret:section}

\begin{definition}[Retained-angle cusp data]
\hypertarget{tag-Q021}{}\label{mapsIII:def:retained-angle-cusp-data}
{\normalfont\scriptsize tag Q021}\par
Use the original sphere member or any defined admissible $|p|=1$
member in Definition~\ref{mapsIII:def:cusp-suspension-maps}, with the
fixed based sphere identification of Lemma~\ref{maps:src:B.1.1}
and its outward stable framing. The intrinsic cusp neighbourhood
$N_0$ and its marked quotient are the same in these members.
The overlap arrow is $G_0\circ T_\sigma$, where the prescribed
fibre translation has inverse $T_{-\sigma}$. These arrows preserve
the base parameter and the constant upper suspension value. The
identity on this intrinsic cusp, with itself as inverse, therefore
identifies every local map used below for all these members.

Write $t=q$ and $q=t$ for the two inverse names of the cusp
parameter, and $h_{\rm per}=h$ for the period function in that
definition, with inverse $h=h_{\rm per}$. The radial convention
has $B_0=J$ in the same ordered bases. In the real period
decomposition below, $u=u_{\rm long}$ and $k=v$ from that
definition, with inverse assignments $u_{\rm long}=u$ and $v=k$.
Use the original toric chart of \SeriesRef{mapsI:src:A.1.2}.

''' + coordinates[data_start:].replace(r'\paragraph{Original coordinates and the specified sphere-valued map}' + '\n\n', '', 1)
process = r'''\paragraph{The statement proved.} We give the complete expanded proof of \cref{maps:src:B.3.1}, including the full differential, the relative smoothing and the spin bordism calculation.


\paragraph{The entire regular inverse image lies in one original chart}

'''
assert coordinates.count(process) == 1
coordinates = coordinates.replace(process, '', 1)
chart_start = r'\begin{lemma}[A cusp torus in one coordinate chart]'
coordinates = coordinates.replace(chart_start, '\\end{definition}\n\n' + chart_start, 1)
coordinates = coordinates.replace(r'\hypertarget{tag-03AE}{}\label{wb:h24:ret:chart-lemma}',
    r'\hypertarget{tag-03AE}{}\label{wb:h24:ret:chart-lemma}' + '\n' + r'{\normalfont\scriptsize tag 03AE}\par', 1)
coordinates = coordinates.replace(r'\hypertarget{tag-03AP}{}\label{wb:h24:ret:eq:M}',
    r'\hypertarget{tag-03AP}{}\label{wb:h24:ret:eq:M}' + '\n ' + r'\hypertarget{tag-01V0}{}\label{maps:eq:B.3.2}', 1)

differential = old[diff_start:orientation_start]
differential = differential.replace(r'\paragraph{The full differential and its ordered normal framing}', r'''\subsection{Differential and orientation of the cusp torus}

\begin{lemma}[The differential normal framing]
\hypertarget{tag-Q022}{}\label{mapsIII:lem:retained-angle-differential}
{\normalfont\scriptsize tag Q022}\par
For the torus of Lemma~\ref{wb:h24:ret:chart-lemma}, the map $H$
is a submersion along its full inverse image. Its target-coordinate
normal framing is given by the vectors in
\eqref{wb:h24:ret:eq:normal-first} and
\eqref{wb:h24:ret:eq:normal-u}. The literal four-cell framing and
this framing are joined by the positive diagonal path below, and
\eqref{wb:h24:ret:eq:A-homotopy} gives a normal-frame homotopy
on the same embedded torus for every parameter $0\leq v\leq1$.
\end{lemma}

\begin{proof}''', 1)
differential = differential.replace(r'\hypertarget{tag-03AT}{}\label{wb:h24:ret:eq:derivative-on-M}',
    r'\hypertarget{tag-03AT}{}\label{wb:h24:ret:eq:derivative-on-M}' + '\n ' + r'\hypertarget{tag-01V1}{}\label{maps:eq:B.3.3}', 1)
differential = differential.replace(r'\hypertarget{tag-03B3}{}\label{wb:h24:ret:eq:normal-u}',
    r'\hypertarget{tag-03B3}{}\label{wb:h24:ret:eq:normal-u}' + '\n ' + r'\hypertarget{tag-01V2}{}\label{maps:eq:B.3.4}', 1)
differential = differential.replace('This explicitly accounts for all derivatives of the original bounded\nperiod terms; none are omitted or estimated away.',
    'The equality follows from the vanishing factor $v-\\ell p_0$\nin the full derivative, including the entire $dA(t)$ term.')
differential = differential.replace('Orthogonal representatives are not required for\nthis quotient-bundle definition; projecting the displayed lifts along',
    'Projecting the displayed lifts along')
differential = differential.replace('For completeness, the original period matrix admits the following\nexplicit homotopy of this normal framing.',
    'The period matrix gives an explicit homotopy of this normal framing.')
differential = differential.replace('This is a homotopy of\nthe computed frame on the same embedded torus, not a replacement of\nthe original degeneration by a different one.',
    'At every time the embedding, the period germ and the target map\nremain the specified ones; only the displayed normal-frame matrix varies.')
differential += '\\end{proof}\n\n'
orientation = old[orientation_start:contraction_start]
orientation = orientation.replace(r'\hypertarget{tag-03BD}{}\label{wb:h24:ret:orientation-lemma}',
    r'\hypertarget{tag-03BD}{}\label{wb:h24:ret:orientation-lemma}' + '\n' + r'{\normalfont\scriptsize tag 03BD}\par', 1)

contraction = old[contraction_start:framing_start]
contraction = contraction.replace(r'\paragraph{An explicit contraction of the full frame}' + '\n\n', '', 1)
contraction = contraction.replace('Thus neither an unspecified phase nor a position-dependent\nreal-linear matrix remains.', 'This gives the complete phase dependence through the displayed\n$D(a,b)$ and the fixed positive matrix $G_0$.')
framing = old[framing_start:spin_start]
framing = framing.replace(r'\hypertarget{tag-03BC}{}\label{wb:h24:ret:framing-proposition}',
    r'\hypertarget{tag-03BC}{}\label{wb:h24:ret:framing-proposition}' + '\n' + r'{\normalfont\scriptsize tag 03BC}\par', 1)
framing = framing.replace('\\begin{proof}\n', '\\begin{proof}\n' + contraction, 1)
circle_contraction = r'''
The same periodic matrices give the following explicit circle-loop
identity. For the real-linear involution
$\mathcal J(z_1,z_2)=(z_1,\overline z_2)$, with inverse $\mathcal J$,
\[
 \mathcal J\operatorname{diag}(e^{ia},e^{ia})\mathcal J
 =\operatorname{diag}(e^{ia},e^{-ia})=K_1(-a).
\]
Thus $\mathcal J K_v(-a)\mathcal J$ joins the identity to
$\operatorname{diag}(e^{ia},e^{ia})$ and its reversed parameter
contracts that loop. All matrices are periodic in $a$ and all
inverse products are defined on the same real four-dimensional space.
'''
assert framing.count('\\end{proof}') == 1
framing = framing.replace('\\end{proof}', circle_contraction + '\\end{proof}', 1)
framing = '\\subsection{Stable framing and the spin invariant}\n\n' + framing

spin = old[spin_start:main_start]
spin = spin.replace(r'\paragraph{Nonzero framed bordism and the exact unstable class}', r'''\begin{lemma}[The spin invariant of the Lie torus]
\hypertarget{tag-Q023}{}\label{mapsIII:lem:lie-torus-spin-invariant}
{\normalfont\scriptsize tag Q023}\par
For an oriented closed spin surface, the Arf sum of its spin quadratic
form is independent of the symplectic basis and invariant under spin
bordism. The Lie-framed two-torus has quadratic form
$q(xe+yf)=x+xy+y$ and Arf invariant one. Its stable framed class is
$\eta^2\ne0$ in $\pi_2^{\mathrm S}=\mathbb Z/2$; reversing one
Lie tangent vector changes its sign and hence preserves this class.
\end{lemma}

\begin{proof}''', 1)
spin = spin.replace('We give the nonvanishing test for the resulting torus explicitly.\n', '', 1)
hopf_start = spin.index('To identify the element, let')
product_start = spin.index('The product of two normally framed inverse images represents')
old_hopf = spin[hopf_start:product_start]
new_hopf = r'''Let $\eta\in\pi_1^{\mathrm S}$ be the stable complex Hopf class.
The circle-framing calculation in the proof of
Theorem~\ref{maps:src:B.1.2} applies in the same coordinates:
its map is $(z_1,z_2)\mapsto[z_1:z_2]$, its fibre is
$(e^{ia},0)$, and its ordered derivative normal vectors are
$(0,e^{ia})$ and $(0,ie^{ia})$ in the coordinate $z_2/z_1$.
The coordinate identification is the identity on $\mathbb C^2$,
with inverse itself, and the circle parameter map is $\theta=a$,
with inverse $a=\theta$. Thus its proved translation-framed
circle represents this same $\eta$. The additional explicit
$\mathcal J K_v(-a)\mathcal J$ contraction is proved in
Proposition~\ref{wb:h24:ret:framing-proposition}.

'''
spin = spin[:hopf_start] + new_hopf + spin[product_start:]
spin += '\\end{proof}\n\n'

main = old[main_start:remark_start]
main = main.replace(r'\begin{proof}[Expanded proof of \cref{maps:src:B.3.1}]', r'\begin{proof}', 1)
main = main.replace(r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]', r'\begin{enumerate}[label=\arabic*.,leftmargin=*]', 1)
first = main.index(r'\item The globally continuous quotient')
pt = main.index(r'\item Pontryagin--Thom therefore identifies')
old_smoothing = main[first:pt]
new_smoothing = r'''\item The full inverse image and submersion assertions are
Lemma~\ref{wb:h24:ret:chart-lemma} and
Lemma~\ref{mapsIII:lem:retained-angle-differential}. Apply
Lemma~\ref{mapsIII:based-regular-fibre-smoothing} with
\[
 f=H,\qquad N=M,\qquad x_0=x_{\rm base},\qquad y=y_0,
 \qquad n=4.
\]
The source and target maps are the identical ones defined above,
with inverse notation changes $H=f$, $M=N$ and $y_0=y$.
In the lemma's notation take its protected tube $T=U_1$;
its first chart $\kappa$ and bump $\beta$ make the map constant
near the basepoint before the positive gap
\[
 d_0=\min_{x\in X\setminus\operatorname{int}U_1}
                 d(H_b(x),y_0)>0
\]
is chosen. The lemma supplies the complete based smoothing and
short-geodesic homotopy, fixed on this same tube and near the
basepoint, with error less than $d_0/2$ on its complement.
Its endpoint has exactly the same full inverse image and
differential at $y_0$. The ordered target chart is
\eqref{wb:h24:ret:eq:four-cell}; transporting its frame by
the positive diagonal map in
Lemma~\ref{mapsIII:lem:retained-angle-differential}, with the
displayed reciprocal inverse, gives precisely the four normal
vectors used below.

'''
main = main[:first] + new_smoothing + main[pt:]
main = main.replace('with the harmless order-two orientation\nsign already computed.', 'with the computed order-two orientation sign.')
main = main.replace('Hence\n\\[\n E^\\infty[H]=\\eta^2\\ne0.\n\\]',
    'Lemma~\\ref{mapsIII:lem:lie-torus-spin-invariant} therefore gives\n\\[\n E^\\infty[H]=\\eta^2\\ne0.\n\\]\nThe same ordered stable product satisfies\n$\\eta\\eta^2=\\eta^3=12\\nu\\ne0$ by\nTheorem~\\ref{maps:src:B.1.2}; it uses the identical Hopf-circle\nclass just identified.')
j7statement = j7statement.replace('For the retained-angle map of Definition~\\ref{mapsIII:def:cusp-suspension-maps},',
    'For the original sphere member and every defined admissible $|p|=1$\nmember in Definition~\\ref{mapsIII:def:retained-angle-cusp-data},\nthe retained-angle map of Definition~\\ref{mapsIII:def:cusp-suspension-maps}\nsatisfies')
conclusion = '\\subsection{The retained-angle homotopy class}\n\n' + j7statement + '\n\n' + main
corollary = old[cor_start:]
corollary = corollary.replace(r'\hypertarget{tag-03BE}{}\label{wb:h24:ret:q2-detected-quotient}',
    r'\hypertarget{tag-03BE}{}\label{wb:h24:ret:q2-detected-quotient}' + '\n' + r'{\normalfont\scriptsize tag 03BE}\par', 1)
new = coordinates + differential + orientation + framing + spin + conclusion + corollary
u.check_permanent_identifiers(old + quotient, new + newquotient,
    {'mapsIII:def:retained-angle-cusp-data', 'mapsIII:lem:retained-angle-differential', 'mapsIII:lem:lie-torus-spin-invariant'},
    {'tag-Q021', 'tag-Q022', 'tag-Q023'})
assert new.count(r'\label{maps:src:B.3.1}') == 1
assert new.count(r'\begin{proof}') == new.count(r'\end{proof}') == 7
df, ds = r.table(r.DEFECTS)
for suffix, label, previous, following, reason in [
 ('RETAINED-SINGLE-PROOF', 'wb:h24:ret:section; maps:src:B.3.1', old, new,
  'Four actual subsections now contain numbered full-family input, complete chart/differential/orientation/framing/spin proofs, one J7 statement/proof and03BE. All local auxiliary calculations remain. The three old J7 formula aliases are placed at their identical complete formulas with phi0=pi. Q255 owns the identical full based-smoothing construction through the stated notation maps. The old angle-forgetting comparison is moved in full mathematical scope to later Q257 after both framing proofs. The Hopf-circle identification uses its exact earlier J5 owner and coordinate/parameter inverse; the complete explicit J-conjugation is retained in03BC.'),
 ('QUOTIENT-J7-MOVE', 'maps:src:B.3.1', quotient, newquotient,
  'Remove the earlier complete duplicate J7 statement/proof only after its entire family scope and all four equation identities have been carried to the retained-angle owner. Q011 and the complete J8/J9 proofs remain at their original dependency boundary. Earlier D12/structure completion requires this full overlap correction; no rekey alone supplies progress.')
]:
    ident = 'III-C8-ROOT-' + suffix
    assert not any(x['change_id'] == ident for x in ds)
    ds.append(dict(change_id=ident, type='D12/D13/D14/D22', statement_id=label,
        old_location='complete retained_angle and quotient_maps inputs before consolidation', old_page='pending page concordance',
        new_location='single retained-angle proof and earlier quotient-map definitions/applications', new_page='pending final PDF',
        old_text=previous, new_text=following, reason=reason,
        review_status='staged whole-fragment exact edit; complete readback, Q255/Q257 integration and canonical placement pending'))
rp.write_text(new, encoding='utf-8', newline='\n')
qp.write_text(newquotient, encoding='utf-8', newline='\n')
r.write_table(r.DEFECTS, df, ds)
print('UTC', datetime.now(timezone.utc).isoformat())
print('RETAINED_LINES', new.count('\n'), 'QUOTIENT_LINES', newquotient.count('\n'))
print('PROOFS', 7, 'ALL_OLD_IDENTITIES_PRESERVED; NEW_Q021_Q022_Q023')
print('EXACT_DEFECT_ROWS', 2, 'STAGED_ONLY; FULL_READBACK_AND_ACTUAL_ORDER_PENDING')
