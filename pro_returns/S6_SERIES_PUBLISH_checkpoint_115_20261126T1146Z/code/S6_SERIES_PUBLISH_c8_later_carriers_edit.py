#!/usr/bin/env python3
"""Publication edits with their exact defects rows; no central-file writer."""
from pathlib import Path
from collections import Counter
import csv
import re
import S6_SERIES_PUBLISH_c8_integrate_presentation as presentation

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / 'agents/continuation8_iii_integration/units/later'
OUT = ROOT / 'agents/continuation8_iii_later'
PATH = DIR / 'further_cusp_carriers.tex'
FIXED = DIR / 'fixed_target_metrics.tex'
LIMITS = DIR / 'limits_and_open_points.tex'
old = PATH.read_text()
fixed_old = FIXED.read_text()
limits_old = LIMITS.read_text()
assert len(old.splitlines()) == 3896
new, fixed, limits = old, fixed_old, limits_old
changes = []

def record(before, after, kind, sid, reason, pos, destination='same mathematical owner'):
    changes.append(dict(type=kind, statement_id=sid,
        old_location='further_cusp_carriers.tex sequential edit line ' + str(new[:pos].count('\n') + 1),
        old_page='pending final concordance', new_location=destination,
        new_page='pending final build', old_text=before, new_text=after,
        reason=reason, review_status='whole repaired source and admitted comparisons read; final readback pending'))

def edit(before, after, kind, sid, reason):
    global new
    assert new.count(before) == 1, (sid, before[:100], new.count(before))
    pos = new.index(before)
    record(before, after, kind, sid, reason, pos)
    new = new[:pos] + after + new[pos + len(before):]

def interval(first, last, after, kind, sid, reason, include_last=False):
    a = new.index(first)
    b = new.index(last, a) + (len(last) if include_last else 0)
    edit(new[a:b], after, kind, sid, reason)

def block(label, environment, proof=True):
    p = new.index(r'\label{' + label + '}')
    a = new.rfind(r'\begin{' + environment + '}', 0, p)
    ending = r'\end{proof}' if proof else r'\end{' + environment + '}'
    b = new.index(ending, p) + len(ending)
    return a, b, new[a:b]

# This complete corollary really uses the following fixed metric construction.
sid = 'wb:cusp-cone-sharp-global-R4-scope'
a, b, moved = block(sid, 'corollary')
record(moved, moved, 'D14', sid,
       'Move the entire already-read corollary and proof after its fixed-target metric prerequisite. The inverse relocation restores this exact block before the old final Scope paragraph. Its later publication rewrite remains pending.', a,
       'fixed_target_metrics.tex, after its existing material')
new = new[:a] + new[b:]
fixed = fixed.rstrip() + '\n\n' + r'\subsection{Euclidean cells, intrinsic limits and boundary fibres}' + '\n' + moved + '\n'

interval(r'\subsection{Cone-compactified sphere carriers for the native cusp quotient}',
         'Fix a closed coordinate disc',
         r'''\section{Cusp quotients and conical targets}
\hypertarget{tag-037I}{}\label{wb:cusp-cone-section}
\subsection{The marked quotient over the punctured cusp}

\begin{definition}[Cusp disc and quotient marking]
\hypertarget{tag-Q30P}{}\label{mapsIII:def:cone-cusp-data}
{\normalfont\scriptsize tag Q30P}\par
Use the original sphere fibration $f:X\to B$ of
\cref{maps:src:B.2.1}. Fix its cusp coordinate and a closed coordinate disc
''', 'D01/D02/D08/D13/D14/D16', 'wb:cusp-cone-native-descent',
         'Replace the production introduction by a numbered definition of its fixed mathematical data and a section/subsection boundary.')
edit('Fix a closed coordinate disc\n', '', 'D13', 'wb:cusp-cone-native-descent',
     'The numbered definition already introduces this exact disc.')
edit('The ordered basis of \\(\\overline\\Lambda\\) is the image of\n\\((\\widehat\\gamma,\\widehat u)\\).\n',
     r'''The ordered basis of \(\overline\Lambda\) is the image of
\((\widehat\gamma,\widehat u)\). In these sections,
\[
 B_R^Z(z)=\{w\in Z:d_Z(z,w)\leq R\}
\]
denotes the closed metric ball. The center and ambient space may be
suppressed when they are fixed by the displayed map.
\end{definition}
''', 'D13/D20', 'wb:cusp-cone-native-descent',
     'Complete the numbered cusp definition and place the inherited closed-ball convention before its first use.')

interval('Define\n\\begin{equation}\n \\mathcal A=',
         '\\begin{theorem}[Localized two-torus quotient with sphere source]',
         r'''\subsection{The two-torus suspension carrier}
\begin{definition}[The two-torus suspension carrier]
\hypertarget{tag-Q30Q}{}\label{mapsIII:def:two-torus-suspension}
{\normalfont\scriptsize tag Q30Q}\par
Set
\begin{equation}
 \mathcal A=
 \frac{[0,\epsilon]\times S^1\times\overline T^2}
 {\{0\}\times S^1\times\overline T^2\sim v_0,\quad
  \{\epsilon\}\times S^1\times\overline T^2\sim v_1}.
 \hypertarget{tag-0354}{}\label{wb:cusp-cone-A-definition}
\end{equation}
Write $\operatorname{Susp}$ for the unreduced suspension. The radial
coordinate maps $[r,z,a]\mapsto[r/\epsilon,z,a]$ and
$[s,z,a]\mapsto[\epsilon s,z,a]$ give
\begin{equation}
 \mathcal A\cong
 \operatorname{Susp}(S^1\times\overline T^2)
 \cong\operatorname{Susp}(T^3).
 \hypertarget{tag-0358}{}\label{wb:cusp-cone-A-suspension}
\end{equation}
The first circle is the angular coordinate of the punctured base.
\end{definition}

''', 'D08/D11/D13/D14/D20', 'wb:cusp-cone-S12-route',
         'Give the suspension its own numbered definition and explicit inverse radial maps. Angle forgetting is defined once by the later explicit quotient maps.')

edit('\\paragraph{The localized one-circle construction.}\nThe full-monodromy-invariant character also gives a smaller cusp-supported\ntarget.  Define\n',
     r'''\subsection{Circle suspensions and finite fillings}
\begin{definition}[The circle suspension carrier]
\hypertarget{tag-Q30R}{}\label{mapsIII:def:circle-suspension}
{\normalfont\scriptsize tag Q30R}\par
Define
''', 'D08/D13/D14', 'wb:cusp-cone-S24-local-route',
     'Replace the orphan introduction by the numbered circle-carrier definition.')
edit('where the two circle coordinates in an interior cross-section are the base\nangle and the value of \\(\\theta_\\gamma\\).\n',
     'where the two circle coordinates in an interior cross-section are the base\nangle and the value of \\(\\theta_\\gamma\\). The suspension coordinates are\nrelated by $[r,z,\\theta]\\mapsto[r/\\epsilon,z,\\theta]$, with inverse\n$[s,z,\\theta]\\mapsto[\\epsilon s,z,\\theta]$.\n\\end{definition}\n',
     'D13/D20', 'wb:cusp-cone-S24-local-route',
     'Close the definition and identify both radial coordinate directions.')
edit('The intrinsic target slices have the pointed Euclidean limit of\n\\eqref{wb:cusp-cone-S24-R4-limit}.  The integral homology groups of\n',
     'The intrinsic target slices converge to $\\mathbb R^4$ in pointed\nlocal-isometric, smooth and Gromov--Hausdorff topology, by\n\\eqref{wb:cusp-spec-four-circle-limit}. The integral homology groups of\n',
     'D04/D14', 'wb:cusp-cone-S24-local-route',
     'Replace the forward equation pointer by its earlier actual four-circle metric owner with identical lattice and metric.')
interval('By \\eqref{wb:cusp-spec-global-circle-circumference}, the quotient\ncircle has length',
         'Finally, the coordinate map',
         r'''The isometry $\vartheta_T$ identifies the character circle with
$C_T$; its inverse divides arclength by $\ell_T$. On four factors the
coordinate map $([u_i])_{i=1}^4\mapsto[(u_1,u_2,u_3,u_4)]$ and its
coordinatewise inverse identify the product isometrically with
$\mathbb R^4/\ell_T\mathbb Z^4$. This is exactly the metric and lattice
of \eqref{wb:cusp-spec-four-circle-fibre}. Its entire-ball isometries
and the three pointed limits are those of
\eqref{wb:cusp-spec-four-circle-limit}.

''', 'D12/D20', 'wb:cusp-cone-S24-local-route',
         'Use the earlier complete four-circle ball proof through the explicit product-coordinate isometry and inverse; preserve the same thresholds and all three limits.')

edit('\\paragraph{The full-base circle target before coning.}\n',
     r'''\begin{definition}[The finite-filled circle carrier]
\hypertarget{tag-Q30S}{}\label{mapsIII:def:finite-filled-circle-carrier}
{\normalfont\scriptsize tag Q30S}\par
''', 'D13', 'wb:cusp-cone-S24-route',
     'Give the core, both finite solid-torus fillings and the attached cone one numbered definition.')
edit('and write \\(c_0\\) for the cone vertex.\nThis changes the codomain at the cusp: the whole boundary two-torus,\nincluding the target circle, is collapsed to \\(c_0\\).  It therefore does\nnot contradict the proved nonextension of the literal map\n\\(\\chi_\\gamma\\) to the fixed product target \\(B\\times S^1\\).\n',
     'and write \\(c_0\\) for the cone vertex. Its radius runs from zero to\n$\\epsilon$; the outer torus is attached to $\\partial\\mathcal M$ by the identity.\n\\end{definition}\n',
     'D02/D11/D13', 'wb:cusp-cone-S24-route',
     'State the cone attachment positively. The later explicit C/M-to-B map supplies its mathematical comparison.')

edit('\\begin{definition}[The three radial target-slice embeddings]',
     '\\subsection{Radial embeddings and intrinsic metrics}\n\\begin{definition}[Radial target-slice maps]',
     'D14/D16', 'wb:cusp-cone-target-slice-embeddings',
     'Create the actual embedding/metric subsection and distinguish the map definition from its proof.')
edit('choice of a real argument branch.  Each displayed map is a topological\nembedding in this exact parameter range.\n\n\\emph{Embedding verification.}\n',
     r'''choice of a real argument branch.
\end{definition}

\begin{lemma}[Radial embeddings and endpoint maps]
\hypertarget{tag-Q30T}{}\label{mapsIII:lem:radial-slice-embeddings}
{\normalfont\scriptsize tag Q30T}\par
The three maps of Definition~\ref{wb:cusp-cone-target-slice-embeddings}
are topological embeddings for $0<r_T<\epsilon$.
At radius zero all three are constant. At radius $\epsilon$ the
two suspension maps are constant, whereas the cone map remains an embedding.
\end{lemma}
\begin{proof}
''', 'D12/D13/D22', 'wb:cusp-cone-target-slice-embeddings',
     'Move the complete inline embedding argument into one numbered lemma and proof, retaining every map, endpoint and inverse.')
edit('It sends the prescribed slice to radius\n\\(r_T/\\epsilon\\); it introduces no extra condition \\(r_T<1\\).\n\\end{definition}',
     'The unit-coordinate slice therefore has radius $r_T/\\epsilon$.\n\\end{proof}',
     'D02/D13', 'wb:cusp-cone-target-slice-embeddings',
     'Close the separated proof and state the radial conversion directly.')
edit('\\begin{proposition}[Intrinsic expansion versus ambient collapse]',
     '\\begin{proposition}[Intrinsic and ambient slice metrics]', 'D16',
     'wb:cusp-cone-metric-scope', 'Use a mathematical title naming the two defined metrics.')
edit('By contrast, in the intrinsic quotient metrics,',
     'In the intrinsic quotient metrics,', 'D02', 'wb:cusp-cone-metric-scope',
     'The exact identity and diameter comparison already establish the metric relationship.')
edit('The obstruction to an almost-complex structure on \\(S^{12}\\),\nwith all three complete classical proofs, is given in\n\\CompendiumRef{III}{wb:cusp-cone-S12-almost-complex-obstruction}.\n\n\n',
     '', 'D06/D12/D13/D17', 'wb:cusp-cone-obstructions',
     'Remove the orphan pointer to multiple compendium proofs; the exact Borel--Serre result is already cited by the earlier global quotient theorem.')
edit('\\begin{theorem}[Global quotient and topology obstructions]',
     '\\section{Monodromy constraints and sphere maps}\n\\subsection{Finite-cover and extension obstructions}\n\\begin{theorem}[Global quotient and topology obstructions]',
     'D14', 'wb:cusp-cone-obstructions', 'Start the next actual section with its finite-cover and extension result.')

# Shared period and orbit calculations have their earlier owner at 039U.
interval('For a rank-zero quotient the conclusion is immediate.',
         'The left-deck matrices give',
         r'''The quotient is the same physical quotient used in
\cref{wb:cusp-spec-globalization-obstruction}: its real-coordinate
map is $[a]\mapsto[P_T^{\oplus r}a]$, with inverse induced by
$(P_T^{\oplus r})^{-1}$. Rank zero satisfies the bound immediately.
The bounded-period argument in that theorem uses only the displayed
length-one vectors and primitivity, before imposing any monodromy
condition. It therefore applies on every lifted radial ray and gives
\begin{equation}
 K_\Lambda^{\oplus r}\subset N.
 \hypertarget{tag-036U}{}\label{wb:cusp-cone-kernel-contained}
\end{equation}

''', 'D12/D20', 'wb:cusp-cone-obstructions',
         'Use the identical physical quotient and the earlier bounded-period argument; retain the old internal label and the additional finite-cover saturation proof.')
interval('The bound is attained by \\(N^\\sharp=',
         '\\emph{The local quotient and the base-cover obstruction.}',
         r'''For $N=L_\Lambda^{\oplus r}$ the quotient is the product of
the character circles of \cref{wb:cusp-spec-globalization-obstruction}.
The map $[P_Ta]\mapsto[\ell_Ta_g]$, with the angle/arclength inverse
$[u]\mapsto[u/\ell_T]$, is precisely that theorem's isometry.
Its product lattice is $\ell_T\mathbb Z^r$ and its systole tends to infinity.

''', 'D12/D20', 'wb:cusp-cone-obstructions',
         'Cite the complete earlier circle quotient and metric proof through its literal marked map, retaining sharpness for every r.')
interval('The cusp map is\n', 'For every \\(h>0\\),',
         r'''The local compactification is exactly $q_2$ of
\cref{wb:cusp-cone-S12-route}: its fibre component is
$\overline\pi_f$ and $\pi_T=\iota_T\overline\pi_T$.
That theorem's endpoint values and collar proof give the whole
continuous map, with restriction
$q_2^{\wedge2}|_{F_T^2}=j_T(\pi_T\times\pi_T)$.

''', 'D12/D20', 'wb:cusp-cone-obstructions',
         'Identify the repeated local compactification with its already proved map on all three strata, then cite its sole continuity proof.')
interval('Choose a based homeomorphism \\(X\\to S^6\\).  Factor inclusions',
         'Over the regular base, the synchronized product has coordinates',
         r'''Use the based diffeomorphism $h:X\to S^6$ and its ordered
product and smash maps from \cref{wb:cusp-spec-globalization-obstruction}.
Their inverses apply $h^{-1}$ to each coordinate and split the
Euclidean coordinate blocks, respectively. The K\"unneth groups and
the resulting homotopy obstructions there prove
\eqref{wb:cusp-cone-products-not-spheres} for these identical sources.

''', 'D12/D20', 'wb:cusp-cone-obstructions',
         'Use the earlier complete product/smash proof under the same based h and its inverse, retaining the new completed-fibre singularity calculation below.')
interval('The join map is\n', '\\emph{The global covers and their finite normal counterparts.}',
         r'''The join maps in \cref{wb:cusp-spec-globalization-obstruction}
send $[(\lambda_i,x_i)]$ to $(\sqrt{\lambda_i}\,h(x_i))_i$.
Their inverses use squared block norms and $h^{-1}$ on each nonzero
unit block; the join relation removes every zero-weight coordinate.
For two and four factors these are the homeomorphisms in
\eqref{wb:cusp-cone-join-dimensions}.

''', 'D12/D20', 'wb:cusp-cone-obstructions',
         'Retain the actual join maps and inverses while citing their earlier complete homeomorphism proof.')
edit('The Borel--Serre proposition and its following remark exclude an\nalmost-complex structure for every differentiable structure on\n\\(S^{2n}\\) when \\(n\\geq4\\)\n\\cite[\\S15, Proposition~15.1 and the following remark,\np.~434]{BorelSerre1953}.\n',
     'The arbitrary-smoothing assertion is the Borel--Serre application in\n\\cref{wb:cusp-spec-globalization-obstruction}, from\n\\cite[\\S15, Proposition~15.1 and the following remark,\np.~434]{BorelSerre1953}.\n', 'D12/D17', 'wb:cusp-cone-obstructions',
     'Use the earlier exact primary application, preserving the explicit chart and tangent-endomorphism transport to a homeomorphic smooth manifold.')

# Move the genuine open problem; retain the exact original passage in its defect row.
a = new.index(r'\paragraph{Canonicity and exact scope.}')
b = new.index(r'\begin{theorem}[Optimality within the native connected torus-quotient class]', a)
scope = new[a:b]
problem = r'''\begin{problem}[Smooth compactifications of finite cusp covers]
\hypertarget{tag-Q30U}{}\label{mapsIII:problem:finite-cusp-cover-compactification}
{\normalfont\scriptsize tag Q30U}\par
For an integer $M>1$, consider the local degree-$M^2$ fibre cover
with lattice $\Lambda_M$ and base change $t=s^M$ in
\cref{wb:cusp-cone-obstructions}. Determine whether it admits a smooth
compactification after a connected global base cover with additional
branch values away from $p_0$, and determine the topology of the
resulting total space, including whether it can be a sphere.
The construction must specify the global base cover, the normalization
and resolution of every pulled-back singular fibre, and the lifted
metric. Its restriction to the chosen cusp must be the stated local
cover with that metric.

The finite flat normal completion in \cref{maps:src:C.1.5} gives the
established global covering construction. The one-branch-value
obstruction and the identity endpoint $M=1$ are proved in
\cref{wb:cusp-cone-obstructions}; the question concerns the smooth
completion with the additional branch values just specified.
\end{problem}

'''
record(scope, problem, 'D01/D02/D11/D13/D14', 'mapsIII:problem:finite-cusp-cover-compactification',
       'Move the genuine auxiliary-cover smooth compactification question to one numbered final-part problem, preserving extra branching, every pulled-back fibre, the lifted metric and total-space topology. Existing q2/quotient/metric statements own the repeated conclusions; unrelated physics disclaimers are removed.', a,
       'limits_and_open_points.tex, immediately before Problem 02LG')
limits = limits.replace(r'\begin{problem}[Remaining filling and smooth classification]', problem + r'\begin{problem}[Remaining filling and smooth classification]', 1)
new = new[:a] + r'''\subsection{Minimum smash dimensions and compactification maps}
\hypertarget{tag-0376}{}\label{wb:cusp-cone-optimal-strengthening}

''' + new[b:]

edit('These minima concern precisely the specified native quotients; no\noptimality assertion is made for arbitrary continuous quotient maps\nor for metrics rescaled by a \\(T\\)-dependent factor.\n',
     '', 'D11', 'wb:cusp-cone-optimal-exponents',
     'The complete quotient class and unscaled metric are already explicit in the opening hypotheses; remove the repeated negative scope sentence.')

interval('\\emph{The cusp bound and its attainment.}',
         '\\emph{Attained minima and compact sphere maps.}',
         r'''\emph{Rank bounds and attaining quotients.}
The physical marking and primitive kernel are the ones in
\cref{wb:cusp-cone-obstructions}. The proof of
\eqref{wb:cusp-cone-kernel-contained} uses only the bounded short
periods on a radial ray, so it also applies over the punctured cusp.
It gives $K_\Lambda^{\oplus r}\subset N$ and hence rank at most $2r$.
For the full base and every connected finite cover, the same theorem
gives $L_\Lambda^{\oplus r}\subset N$ and rank at most $r$.
Its loop operators satisfy $G_*=A_2A_1=H_*=U^{-1}$, so its all-power
formula is exactly the one for this marking. The dual form is
\[
 (a_i,b_i,0,0)G_*^h=(a_i+6hb_i,b_i,hb_i,0);
\]
the integral double-annihilator identification above gives the same
kernel inclusion. The covering argument includes degree one and
nonnormal covers. A branched compact base cover restricts to that
class over $B^\circ$, with metric pulled back from
$T=-\log|t|/(2\pi)$.

For $N=K_\Lambda^{\oplus2}$, the quotient is the product of the
orthogonal quotients of \cref{wb:cusp-cone-native-descent}.
Its map and section are
\[
 [P_Ta]\longmapsto[Y_T(a_g,a_u)],\qquad
 [Y_T(a,b)]\longmapsto[P_T(a,b,0,0)].
\]
The quotient marking is $[a]\mapsto[Y_Ta]$, with inverse induced
by $Y_T^{-1}$. The product lattice and its exact systole are those
proved in \cref{wb:cusp-cone-S12-route}.

For $N=L_\Lambda^{\oplus4}$, use the circle quotient of
\cref{wb:cusp-spec-globalization-obstruction}. The lattice isomorphism
$\Lambda/L_\Lambda\to\mathbb Z$ is induced by
$\gamma=(1,0,0,0)$ and has inverse $n\mapsto[ng]$.
For every affine transition $a\mapsto Aa+b$ its coordinate is
$\gamma(Aa+b)=\gamma(a)+\gamma(b)$; this also gives its pullback
transition over any finite base cover. The metric map is
$[P_Ta]\mapsto[\ell_Ta_g]$ and the inverse arclength marking is
$[u]\mapsto[u/\ell_T]$.
The unit covector $\ell_TP_T^{-\mathsf T}\gamma^{\mathsf T}$ and
its least-norm lift $s\mapsto s\ell_TP_T^{-\mathsf T}\gamma^{\mathsf T}$
give the same quotient isometry as that theorem. Equivalently,
for $G=Y_T^{\mathsf T}Y_T$,
\[
 G_{11}-\frac{G_{12}^2}{G_{22}}
 =\frac{D_T^2}{L^2+m^2}=\ell_T^2.
\]
The four covectors have disjoint supports, giving exactly
$\ell_T\mathbb Z^4$ and systole $\ell_T$. With
$R_T=\sqrt{L^2+m^2}$, the earlier circumference expansion has the
explicit remainder
\[
 \ell_T-(L-B)=\frac{m^2}{R_T}
       \left(6-\frac{L-B}{R_T+L}\right).
\]
For bounded $m,H,B$ and $L=T+H>0$ this is $O(T^{-1})$;
at $m=0$ it is zero. This is the stated unscaled quotient metric.

''', 'D12/D20/D22', 'wb:cusp-cone-optimal-exponents',
         'Use the already proved rank and orbit calculation under the literal G*=H*=U inverse identification. Keep the full primitive character quotient, dual action, exact physical maps, least-norm lift, Schur complement, varying-coefficient remainder and m=0 endpoint.')
interval('We give the compactification maps, retaining the full-base fillings.',
         'The product formula\n',
         r'''Set $c_{\mathcal A}=q_2$ and
$c_{\mathcal B}=q_{1,\mathrm{cusp}}$ from
\cref{wb:cusp-cone-S12-route,wb:cusp-cone-S24-local-route}.
Thus $v_\epsilon=v_1$ and $b_\epsilon=b_1$ denote their outer poles.
These are identities of the whole maps, including $W$, the outer
boundary and the exterior; their continuity and surjectivity were
proved there. Since $\varepsilon_\gamma=\operatorname{pr}_1p$,
the following map satisfies $c_{\mathcal B}=\kappa c_{\mathcal A}$.
''', 'D12/D20', 'wb:cusp-cone-optimal-exponents',
         'Identify the repeated A/B constructions on every stratum and cite their sole continuity proofs, retaining the new explicit compactification morphism.')
edit('property.  Put \\(c_{\\mathcal B}=\\kappa c_{\\mathcal A}\\).\n',
     'property. Its section is $[s,z,a_g]\\mapsto[s,z,(a_g,0)]$;\ncomposing with $\\kappa$ is the identity.\n',
     'D20', 'wb:cusp-cone-optimal-exponents',
     'State the actual section of the noninvertible coordinate-forgetting map, after its whole-map equality has been established.')
edit(' x\\longmapsto[|t|,(\\epsilon\\,t/|t|,\\chi_\\gamma(x))],\n',
     ' x\\longmapsto[|t|,(\\epsilon\\,t/|t|,\\theta_\\gamma(x))],\n',
     'D20', 'wb:cusp-cone-optimal-exponents',
     'Use the circle component theta_gamma=pr_circle chi_gamma in the cone coordinate; the family-valued chi_gamma has an additional base component.')
interval('Choose the established based diffeomorphism \\(h:X\\to S^6\\) used in',
         'The actual compact source maps are\n',
         r'''Let $h_r:X^{\wedge r}\to S^{6r}$ be the ordered smash
homeomorphism of \cref{wb:cusp-spec-globalization-obstruction},
using the same based $h:X\to S^6$. Its finite-coordinate map
concatenates the $r$ Euclidean blocks; its inverse splits those
blocks and applies $h^{-1}$, and the two basepoints correspond.
The compact source maps are
''', 'D12/D20', 'wb:cusp-cone-optimal-exponents',
         'Use the earlier sole smash-homeomorphism proof with its exact forward/inverse coordinates for the compactification diagrams.')
edit('The actual compact source maps are\n', '', 'D08', 'wb:cusp-cone-optimal-exponents',
     'The preceding identified maps already introduce this display.')

edit('\\begin{theorem}[Exact sphere-to-sphere carriers with moving four-spheres]',
     '\\subsection{Collapsed sphere targets and their intrinsic metrics}\n\\begin{theorem}[Sphere quotient maps with moving four-spheres]',
     'D14/D16', 'wb:cusp-cone-angle-forgotten-sphere-carriers',
     'Give the sphere-target construction and full metric proof its actual subsection.')

# The marking comparison is the prerequisite for the later null-homotopy application.
sid = 'wb:cusp-cone-sphere-map-homotopy-status'
a, b, moved = block(sid, 'remark', False)
record(moved, moved, 'D14', sid,
       'Move the complete exact period/skeleton/suspension comparison immediately after the sphere-target construction, before its repeated-smash application. The inverse relocation restores it after the moving-sphere lemma.', a,
       'further_cusp_carriers.tex, before remark 035Z')
new = new[:a] + new[b:]
at = new.index('\\begin{remark}[Squares of the rank-two sphere carrier]')
new = new[:at] + '\\subsection{Homotopy classes and suspension factorizations}\n' + moved + '\n\n' + new[at:]
edit('Consequently the long-period map \\(\\alpha\\) of\n\\cref{mapsIII:angle-forgotten-one-copy-null} satisfies\n',
     'Let $\\alpha$ denote the long-period map of\nDefinition~\\ref{mapsIII:def:cusp-suspension-maps}, viewed in its\nquotient lattice: a lift with coefficients $(a,b,c,d)$ has\n$\\alpha=[a\\widehat\\gamma+b\\widehat u]$. The displayed $\\beta$\nand $\\beta^{-1}$ give its coefficient coordinates. Consequently\n',
     'D04/D20', sid,
     'Refer to the published owner Q011 and explicitly define the quotient-lattice coordinate alpha with its coefficient isomorphism; current 02Q7 names no alpha.')

# The specific null-homotopies have one owner, 02Q7, via the preceding exact map.
sid = 'wb:cusp-cone-S24-sphere-map-null'
a, b, old_block = block(sid, 'corollary')
replacement = r'''\begin{remark}[Suspension factorization of the circle carrier]
\hypertarget{tag-036E}{}\label{wb:cusp-cone-S24-sphere-map-null}
Let $f=\widehat q_\gamma:S^6\to S^2$ in the based coordinates of
\cref{wb:cusp-cone-angle-forgotten-sphere-carriers}. The identification
in \cref{wb:cusp-cone-sphere-map-homotopy-status} applies
\cref{mapsIII:angle-forgotten-one-copy-null} to this entire map, giving
\begin{equation}
 [f^{\wedge r}]=0\quad\text{in }\pi_{6r}(S^{2r})\qquad(r\geq2),
 \hypertarget{tag-0367}{}\label{wb:cusp-cone-S24-null-maps}
\end{equation}
and in particular
\begin{equation}
 [\widehat q_\gamma^{\wedge2}]=0\in\pi_{12}(S^4),\qquad
 [\widehat q_\gamma^{\wedge4}]=0\in\pi_{24}(S^8).
 \hypertarget{tag-0368}{}\label{wb:cusp-cone-S24-null-special-cases}
\end{equation}
Here the sphere-coordinate map is
$F_r=\mu_{2,r}f^{\wedge r}\mu_{6,r}^{-1}$, with
$\mu_{n,1}=\operatorname{id}$ and $F_1=f$.
The coordinate concatenations $\mu$ and their block-splitting inverses
are those of \cref{wb:cusp-cone-angle-forgotten-sphere-carriers}.

The two-factor map has the factorization
\begin{equation}
 \begin{tikzcd}[column sep=large]
 S^6\wedge S^6\arrow[r,"f\wedge\operatorname{id}_{S^6}"]&
 S^2\wedge S^6\arrow[r,"\operatorname{id}_{S^2}\wedge f"]&
 S^2\wedge S^2.
 \end{tikzcd}
 \hypertarget{tag-036C}{}\label{wb:cusp-cone-S24-smash-square-factorization}
\end{equation}
Write $\beta_{p,q}$ for two-block concatenation and
$\tau_{p,q}[x,y]=[y,x]$, whose inverse is $\tau_{q,p}$. On every
representative, including the fat wedge,
\begin{equation}
 \begin{aligned}
 f\wedge\operatorname{id}_{S^6}
   &=\tau_{6,2}(\operatorname{id}_{S^6}\wedge f)\tau_{6,6},\\
 \beta_{6,2}(\operatorname{id}_{S^6}\wedge f)\beta_{6,6}^{-1}
   &=\Sigma^6f:S^{12}\longrightarrow S^8.
 \end{aligned}
 \hypertarget{tag-036B}{}\label{wb:cusp-cone-S24-sixfold-suspension}
\end{equation}
The first composite sends $[x,y]$ successively to $[y,x]$,
$[y,f(x)]$ and $[f(x),y]$. The intermediate homotopy group is
\phantomsection\hypertarget{tag-033R}{}\label{qa:III:layout:11}
\begin{equation}
 \pi_{12}(S^8)\cong\pi_4^{\mathrm S}=0,
 \hypertarget{tag-036R}{}\label{wb:cusp-cone-fourth-stable-stem}
\end{equation}
by \cite[Corollary~4.24, p.~360]{Hatcher2002} and
\cite[Corollary~1.3, p.~112, and Table~1, p.~113]{IsaksenWangXu2023}.
The suspension range holds since $12+j<2(8+j)-1$ for every $j\geq0$.

Let $H_4$ be the based homotopy supplied by
\cref{mapsIII:angle-forgotten-one-copy-null}, transported through the
specified source and target homeomorphisms. Its initial map is the
continuous surjective quotient $F_4$ of
\cref{wb:cusp-cone-angle-forgotten-sphere-carriers}. With $\kappa_T$
the native radial product inclusion followed by source coordinates,
\[
 H_4(\kappa_T(x),0)
   =i_T\rho_{24,T}\bigl(\pi_{\gamma,T}(x_1),\ldots,
                         \pi_{\gamma,T}(x_4)\bigr),
 \qquad \pi_{\gamma,T}=\vartheta_T\chi_{\gamma,T}.
\]
Here $i_T$ is the fourth smash of $[u]\mapsto[r_T,[u/\ell_T]]$
in the chosen target coordinates. The quotient metric, midpoint
$[\ell_T/2,\ldots,\ell_T/2]$, and entire-ball isometries for
$\ell_T>4R$ are exactly those of
\eqref{wb:cusp-cone-S24-onto-exact-ball}. Thus the radial
restrictions of this initial representative have the stated pointed
local-isometric and Gromov--Hausdorff limits.
\end{remark}'''
record(old_block, replacement, 'D12/D14/D17/D20', sid,
       'Use the sole already proved based null-homotopies after the complete marking identification. Retain all old equation anchors, exact factorization/twists and cited stable group, all r>=2, the initial representative and the literal radial metric map. The repeated independent stable-stem nullity proof and repeated ball proof stay in the admitted comparison records.', a)
new = new[:a] + replacement + new[b:]

edit('\\begin{corollary}[Open four-cells in the sphere targets]',
     '\\subsection{Open four-cells and moving spheres}\n\\begin{corollary}[Open four-cells in the sphere targets]',
     'D14', 'wb:cusp-cone-literal-R4-open-cells', 'Place open-cell coordinates and moving-sphere contractions in one actual subsection.')
edit('\\begin{proposition}[The compact cone-on-\\(T^4\\) carriers]',
     '\\section{Compact carriers and Euclidean boundary fibres}\n\\subsection{Conical carriers and their homotopy types}\n\\begin{proposition}[Compact cones on the four-torus]',
     'D14/D16', 'wb:cusp-cone-explicit-carriers', 'Start the section on the complete compact carriers and their boundary comparison.')
edit('\\begin{theorem}[Point-set quotient maps and exact homotopy types]',
     '\\begin{theorem}[Homotopy types of the conical targets]', 'D16',
     'wb:cusp-cone-target-homotopy-types', 'Name the mathematical result without emphatic process qualifiers.')
edit('\\begin{theorem}[Exact decompactification spaces with boundary\n\\(\\mathbb R^4\\)]',
     '\\subsection{Decompactification spaces}\n\\begin{theorem}[Decompactification spaces with Euclidean boundary]',
     'D14/D16', 'wb:cusp-cone-exact-decompactification-space', 'Give the noncompact comparison space its actual final subsection.')

interval('\\paragraph{Scope.}', '\n', '', 'D01/D02/D11/D13',
         'wb:cusp-cone-exact-decompactification-space',
         'Remove the closing production heading; its exact substantive and negative scope text is handled in the following edit.', True)
tail = new[new.index('The constructions above use only the original, unscaled fibre metrics'):]
edit(tail, '', 'D02/D11/D13', 'wb:cusp-cone-exact-decompactification-space',
     'The individual definitions fix the cusp coordinate, ray, based sphere map and marked Euclidean metrics. Their proofs give every actual comparison. Remove the repeated recap and unrelated physics disclaimers.')

# Only the bounded helper is used; every semantic edit above is individually specified.
candidate, header_edits, unresolved = presentation.statement_records_to_small_tags(new)
assert not unresolved, unresolved
for item in header_edits:
    record(item.old, item.new, item.kind, item.statement_label, item.reason, item.start)
new = candidate
owners = re.findall(r'\\begin\{(?:theorem|lemma|proposition|corollary|remark|definition)\}(?:\[[\s\S]*?\])?\s*\\hypertarget\{tag-([^}]+)\}\{\}\\label\{([^}]+)\}', new)
for tag, sid in owners:
    anchor = r'\hypertarget{tag-' + tag + r'}{}\label{' + sid + '}'
    pos = new.index(anchor) + len(anchor)
    if re.match(r'\s*\{\\normalfont\\scriptsize tag ', new[pos:]):
        continue
    edit(anchor, anchor + '\n{\\normalfont\\scriptsize tag ' + tag + '}\\par',
         'D10', sid, 'Print the existing permanent tag once as a small statement tag, preserving its anchor and label.')

def identifiers(text):
    return Counter(re.findall(r'\\(?:label|hypertarget)\{([^}]+)\}', text))
before = identifiers(old + fixed_old + limits_old)
after = identifiers(new + fixed + limits)
assert all(after[key] == count for key, count in before.items())
added = sorted(key for key in after if key not in before)
assert all(after[key] == 1 for key in added)
assert set(added) == {
    'tag-Q30P', 'mapsIII:def:cone-cusp-data',
    'tag-Q30Q', 'mapsIII:def:two-torus-suspension',
    'tag-Q30R', 'mapsIII:def:circle-suspension',
    'tag-Q30S', 'mapsIII:def:finite-filled-circle-carrier',
    'tag-Q30T', 'mapsIII:lem:radial-slice-embeddings',
    'tag-Q30U', 'mapsIII:problem:finite-cusp-cover-compactification',
}, added

fields = ['change_id', 'type', 'statement_id', 'old_location', 'old_page',
          'new_location', 'new_page', 'old_text', 'new_text', 'reason', 'review_status']
for i, row in enumerate(changes, 1):
    row['change_id'] = 'c8-III-carriers-' + str(i).zfill(3)
with (OUT / 'S6_SERIES_PUBLISH_III_carriers_publication_defects.tsv').open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(changes)
PATH.write_text(new.rstrip() + '\n')
FIXED.write_text(fixed)
LIMITS.write_text(limits)
print('Exact edit rows written:', len(changes))
print('All existing labels and targets retained with exact multiplicities across the three assigned fragments.')
print('New formal identities:', ', '.join(tag for tag in added if tag.startswith('tag-')))
print('Final proof readback and all-criteria review remain pending; no central files or publication gate changed.')
