#!/usr/bin/env python3
"""Exact publication edits and local defects; no canonical or shared writes."""
from pathlib import Path
from collections import Counter
import csv
import re
import S6_SERIES_PUBLISH_c8_integrate_presentation as presentation

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'agents/continuation8_iii_integration/units/later/fixed_target_metrics.tex'
OUT = ROOT / 'agents/continuation8_iii_later'
old = PATH.read_text()
assert len(old.splitlines()) == 2081
new = old
changes = []

def edit(before, after, kind, sid, reason):
    global new
    assert new.count(before) == 1, (sid, before[:90], new.count(before))
    pos = new.index(before)
    changes.append(dict(type=kind, statement_id=sid,
        old_location='fixed_target_metrics.tex sequential edit line ' + str(new[:pos].count('\n') + 1),
        old_page='pending final concordance', new_location='fixed_target_metrics.tex, same mathematical scope unless specified',
        new_page='pending final build', old_text=before, new_text=after, reason=reason,
        review_status='whole repaired source and all admitted comparisons read; final readback pending'))
    new = new[:pos] + after + new[pos + len(before):]

def interval(first, last, after, kind, sid, reason):
    a = new.index(first)
    b = new.index(last, a)
    edit(new[a:b], after, kind, sid, reason)

interval(r'\subsection{Fixed-target metric realization and its sharp dimensional scope}',
         r'\begin{theorem}[Topology-forced collapse',
         r'''\section{Metrics on the conical targets}
\hypertarget{tag-03D9}{}\label{wb:sphere-metric-limit-note}
\subsection{Fixed targets and radial collapse}

\begin{definition}[Radial metric data]
\hypertarget{tag-Q30W}{}\label{mapsIII:def:fixed-target-metric-data}
{\normalfont\scriptsize tag Q30W}\par
Use the based quotient maps and their target carriers
\[
 q_2^{\wedge2}:X^{\wedge2}\longrightarrow
 Z_{12}:=\mathcal A^{\wedge2},\qquad
 q_{1,\mathrm{cusp}}^{\wedge4}:X^{\wedge4}\longrightarrow
 Z_{24}^{\mathcal B}:=\mathcal B^{\wedge4},\qquad
 q_1^{\wedge4}:X^{\wedge4}\longrightarrow
 Z_{24}^{\mathcal C}:=\mathcal C^{\wedge4}.
\]
The based source identifications are the maps $\mu_{6,2}$ and
$\mu_{6,4}$ of \cref{wb:cusp-cone-sphere-map-homotopy-status}.
Write
\[
 r_T=e^{-2\pi T},\qquad
 J=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
 Y_T=TJ+E(r_T),\qquad
 T(r)=-\frac{\log r}{2\pi}.
\]
Fix $T_0>0$ in the native cusp range so that $r_0=e^{-2\pi T_0}<\epsilon$,
$Y_T$ is invertible and $\ell_T>0$ for every $T\geq T_0$.
The residual matrix $E$ is the matrix of the radial cusp expansion;
write $C_E=\sup_{0\leq t\leq r_0}\|E(t)\|$.
On $\overline T^2=(\overline\Lambda\otimes\mathbb R)/\overline\Lambda$ set
\[
 h_T=\iota_T^*g_{Q_T}=dx^{\mathsf T}Y_T^{\mathsf T}Y_Tdx,
 \qquad\iota_T[a]=[Y_Ta],\quad\vartheta_T[\theta]=[\ell_T\theta].
\]
The inverse markings are $[y]\mapsto[Y_T^{-1}y]$ and
$[c]\mapsto[c/\ell_T]$. The period-one base and character coordinates
$u,\theta\in\mathbb R/\mathbb Z$ represent the circle values
$e^{2\pi iu},e^{2\pi i\theta}$; the inverse sends a circle value to
its argument divided by $2\pi$ modulo $\mathbb Z$.
Use the slice embeddings $j_T,k_T^{\mathcal B},k_T^{\mathcal C}$ of
\cref{wb:cusp-cone-target-slice-embeddings}. Thus $u=0$ represents
the positive radial angle $1\in S^1$.
\end{definition}

''', 'D01/D02/D08/D13/D14/D16/D20', 'wb:sphere-metric-limit-note',
         'Replace the production introduction by the numbered metric data, with exact source, marking and angular maps. Move 03DA to its proved construction owner below.')

edit(r'\begin{theorem}[Topology-forced collapse for every fixed compatible metric]',
     r'\begin{corollary}[Collapse in fixed compatible metrics]', 'D12/D16',
     'wb:sphere-metric-uniform-collapse',
     'The compact-parameter collapse is already proved in 036W; retain the Hausdorff and GH consequences as one corollary.')
start = new.index(r'\label{wb:sphere-metric-uniform-collapse}')
end = new.index(r'\end{theorem}', start)
edit(new[start:end + len(r'\end{theorem}')], new[start:end] + r'\end{corollary}', 'D12',
     'wb:sphere-metric-uniform-collapse', 'Match the corollary environment.')
interval('Choose $0<r_0<\\epsilon$ and put $P=(\\mathbb R/\\mathbb Z)^4$.',
         'For the nonempty compact set $S_r=H(r,P)$,',
         r'''Use the continuous maps $H_{12},H_{24}^{\mathcal B},H_{24}^{\mathcal C}$
of \cref{wb:cusp-cone-metric-scope} on
$[0,r_0]\times P$, $P=(\mathbb R/\mathbb Z)^4$.
For the first map the identification of $P$ with
$(\overline T^2)^2$ concatenates the two ordered coordinate pairs,
with inverse splitting them; for the other maps it is the identity
on the four circle coordinates. The inverse markings in
\cref{mapsIII:def:fixed-target-metric-data} give exactly
$H_{12}(r_T,P)=j_T(Q_T^2)$ and
$H_{24}^{\mathcal D}(r_T,P)=k_T^{\mathcal D}(C_T^4)$.
That proposition proves, for each of these maps and every compatible $D$,
\[
 A(r):=\max_{a\in P}D(H(r,a),*)\longrightarrow0.
\]
''', 'D12/D20', 'wb:sphere-metric-uniform-collapse',
         'Use the identical compact-parameter maps and the earlier whole collapse proof through the explicit pair-concatenation map and inverse; retain the complete quantitative Hausdorff/GH argument.')
interval('The preceding theorem is unrescaled.',
         r'\begin{theorem}[One fixed cusp-adapted metric', '', 'D02/D14',
         'wb:sphere-metric-fixed-realization', 'Remove the orphan transition; the following numbered construction supplies the positive metric assertions.')

# Split the old native theorem only after matching every construction and limit clause.
a = new.index(r'\begin{theorem}[One fixed cusp-adapted metric')
b = new.index(r'\end{proof}', a) + len(r'\end{proof}')
native_old = new[a:b]
construction_statement = native_old[native_old.index('There are fixed compatible length metrics'):native_old.index('Consequently,')]
native_statement = native_old[native_old.index('Consequently,'):native_old.index(r'\end{theorem}')]
construction_proof = native_old[native_old.index(r'\begin{proof}'):native_old.index('For a fixed \\(R\\), the period bounds')]
construction_proof = construction_proof.replace(
    'In particular \\(T^{-2}h_T\\) has coefficient matrix\n\\((J+E(r_T)/T)^{\\mathsf T}(J+E(r_T)/T)\\), which tends to \\(I\\).',
    r'''In particular $T^{-2}h_T$ has coefficient matrix
$(J+E(r_T)/T)^{\mathsf T}(J+E(r_T)/T)$, which tends to $I$.
These coefficients are constant in the fixed torus coordinates, so
the convergence holds in every $C^k$ norm.''')
strict = native_old[native_old.index(r'\medskip\noindent' + '\n' + r'\emph{Intrinsic and ambient paths on the slices.}'):native_old.index('On every bounded physical slice-coordinate set,')]
construction_proof += strict + r'\end{proof}'
construction = r'''\subsection{Compatible length metrics and slice forms}
\begin{lemma}[Conical metrics and their induced slice forms]
\hypertarget{tag-Q30X}{}\label{mapsIII:lem:fixed-conical-metrics}
{\normalfont\scriptsize tag Q30X}\par
In the data of \cref{mapsIII:def:fixed-target-metric-data},
\begin{equation}
 T^{-2}h_T\longrightarrow h_\infty=dx^{\mathsf T}dx
 \hypertarget{tag-03DA}{}\label{wb:sphere-metric-normalized-Q-limit}
\end{equation}
in every $C^k$ norm in the fixed flat coordinates.
''' + construction_statement + r'\end{lemma}' + '\n\n' + construction_proof
native = r'''\subsection{Native and unit-volume scaling}
\begin{corollary}[Native Euclidean slice and ambient limits]
\hypertarget{tag-03D6}{}\label{wb:sphere-metric-fixed-realization}
For the metrics, slices and marked points of
\cref{mapsIII:lem:fixed-conical-metrics},
''' + native_statement.replace('Consequently,\n', '') + r'''\end{corollary}

\begin{proof}
In \cref{wb:sphere-metric-scaling-trichotomy}, set
\[
 \lambda_T=T/r_T,\quad\beta_T=T\quad\text{on }Z_{12},
 \qquad
 \lambda_T=\ell_T/r_T,\quad\beta_T=\ell_T
       \quad\text{on }Z_{24}^{\mathcal D}.
\]
These substitutions have inverse $\lambda_T=\beta_T/r_T$.
Both parameters tend to infinity, since $\ell_T\geq T-C_E$.
The exact forms \eqref{wb:sphere-metric-A-slice-exact} and
\eqref{wb:sphere-metric-BC-slice-exact} identify the resulting
intrinsic metrics with $g_{Q_T}^{\oplus2}$ and $g_{C_T}^{\oplus4}$.
The whole-ball isometries and ambient convergence in that theorem
therefore give both displayed limits in their stated categories.

More explicitly, its factor coordinate maps become
\[
 (a,b,\xi)\longmapsto
 [r_T(1+a/T),e^{2\pi ib/T},[Y_T^{-1}\xi]]
\]
on $\mathcal A$, with inverse
$(r,u,x)\mapsto(T(r/r_T-1),Tu,Y_Tx)$ on the specified lift window.
On $\mathcal B$ and $\mathcal C$ they become
\[
 (a,b,\xi)\longmapsto
 [r_T(1+a/\ell_T),e^{2\pi ib/\ell_T},[\xi/\ell_T]],
\]
using the cone's paired representative in $\mathcal C$.
Their inverse is $(r,u,\theta)\mapsto
(\ell_T(r/r_T-1),\ell_Tu,\ell_T\theta)$ on that window.
Both inverse compositions are identities. The products of two or
four factors are exactly the general theorem's maps after the
displayed substitutions, so its all-order estimates and whole-ball
exhaustion apply without a further rate assumption.
The slice in each factor has $a=b=0$. Its four physical coordinates
therefore give the asserted coordinate four-plane, including the
ambient-restricted slice limit proved there.
\end{proof}

'''
edit(native_old, construction, 'D12/D13/D14/D16/D20',
     'wb:sphere-metric-fixed-realization',
     'Assign every global metric, local quotient, exact form and strict-shortcut assertion to Q30X; retain the native limit statement under 03D6 after 03DC with its explicit scale and coordinate inverse maps. The arbitrary-rate proof is the single limit-proof owner. Every original equation anchor is retained once.')

# The general theorem now depends on the preceding construction, not its corollary.
dc = new.index(r'\begin{theorem}[Complete intrinsic scalar-rescaling trichotomy]')
dc_end = new.index(r'\end{proof}', dc) + len(r'\end{proof}')
dc_text = new[dc:dc_end]
dc_new = dc_text.replace(r'\cref{wb:sphere-metric-fixed-realization}', r'\cref{mapsIII:lem:fixed-conical-metrics}')
edit(dc_text, r'\subsection{Arbitrary radial scaling}' + '\n' + dc_new,
     'D12/D14/D20', 'wb:sphere-metric-scaling-trichotomy',
     'Place the full arbitrary-rate theorem after its actual construction prerequisite; replace only construction citations by Q30X. Its full proof retains zero, finite positive and infinite beta regimes, all-order estimates and fixed-vertex packing.')
edit(r'\end{gathered}' + '\nThe actual target path is',
     r'\end{gathered}' + '\n' + r'\]' + '\nThe actual target path is',
     'D23', 'wb:sphere-metric-scaling-trichotomy',
     'Close the displayed gathered chord calculation before the ordinary prose. This exact omitted closer occurs in the admitted receiver and the repaired input; no formula changes.')
edit(r'\begin{corollary}[Unit-volume normalization does not give' + '\n' + r'\(\mathbb R^4\)]',
     native + r'\begin{corollary}[Unit-volume flat quotients]',
     'D12/D14/D16', 'wb:sphere-metric-unit-volume',
     'Insert the native specialization after its proof owner and give the unit-volume corollary a mathematical title.')

# Consolidate two construction repetitions against already established owners.
interval('To verify the triangle inequality, concatenate paths giving either',
         'Give \\(P=X^n\\) the product distance',
         r'''This is the closed-subset quotient metric proved in
\cref{wb:cusp-cone-angle-forgotten-sphere-carriers}, applied here
to the same identity quotient $x\mapsto[x]$ with inverse taking
the unique representative off $F$. That proof gives the metric,
length and compatible quotient-topology properties, and also
applies to each outer-torus collapse above.

''', 'D12/D20', 'mapsIII:lem:fixed-conical-metrics',
         'Use the earlier full general compact-length quotient proof by the same quotient map and inverse. Retain the distinct product-distance, fat-wedge and local-isometry calculations.')
interval('At each synchronized basepoint, the distance to the fat wedge is',
         r'\medskip\noindent' + '\n' + r'\emph{The slice forms.}',
         'At each synchronized slice point, every factor has inward distance\n$r_T$, so the distance to the fat wedge is exactly $r_T$.\n\n',
         'D12/D20', 'mapsIII:lem:fixed-conical-metrics',
         'Keep the exact all-T radial identity; the general beta proof below owns all rescaled whole-ball exclusions, with K=beta and lambda=beta/r_T.')
edit('as stated in that theorem.', 'as stated in that corollary.',
     'D14', 'wb:sphere-metric-tangent-scope', 'Update the native result kind after exact consolidation.')
edit(r'\begin{proposition}[Vertex links and compact metric limits]',
     r'\subsection{Vertex links and pointed limits}' + '\n' + r'\begin{proposition}[Vertex links and compact metric limits]',
     'D14', 'wb:sphere-metric-tangent-scope', 'Give the complete link, local homology and tangent proof its actual subsection.')

# Keep core notation aligned with the finite-filled carrier definition.
for before, after in [
    (r'\partial M=\partial D_0\times S^1', r'\partial\mathcal M=\partial D_0\times S^1'),
    (r'core \(M\)', r'core \(\mathcal M\)'),
    (r'rest of \(M\)', r'rest of \(\mathcal M\)'),
]:
    if before in new:
        edit(before, after, 'D11/D20', 'mapsIII:lem:fixed-conical-metrics',
             'Use the already defined finite-filled core symbol; the object and its collar map are unchanged.')

interval(r'\paragraph{Consequences for the three sphere routes.}',
         r'\subsection{Euclidean cells, intrinsic limits and boundary fibres}',
         r'''\subsection{Source pullbacks and moving sphere metrics}
\begin{remark}[Quotient differentials and moving quotient metrics]
\hypertarget{tag-Q30Y}{}\label{mapsIII:rem:source-and-moving-metrics}
{\normalfont\scriptsize tag Q30Y}\par
On the regular cusp chart, write a fibre vector as $P_Ta$ in the
ordered basis $(\widehat\gamma,\widehat u,\widehat w,\widehat\delta)$.
The two-torus quotient sends it to $Y_T(a_\gamma,a_u)$, and the
circle quotient sends it to $\ell_Ta_\gamma$. Their differential
kernels are exactly
\[
 P_T\operatorname{span}_{\mathbb R}\{\widehat w,\widehat\delta\},
 \qquad
 P_T\operatorname{span}_{\mathbb R}
       \{\widehat u,\widehat w,\widehat\delta\},
\]
because $Y_T$ is invertible and $\ell_T>0$. The base coordinates
are retained, so these are also the kernels on the full regular
charts. The product maps have the direct sums of these kernels,
of dimensions four and twelve. The smash quotient is a local
diffeomorphism off its fat wedge. Thus for every such nonzero
kernel vector $v$ the pulled-back target form has
$q^*g(v,v)=g(dq(v),dq(v))=0$. A smooth Riemannian metric on the
source sphere has positive value on that same $v$. For an orthonormal
frame $(e_i)$, the tangent isometry to $\mathbb R^{12}$ or
$\mathbb R^{24}$ is $v\mapsto(\langle v,e_i\rangle)_i$, with
inverse $(c_i)\mapsto\sum_i c_ie_i$.

For the moving sphere carriers, the maps
\[
 \widehat p_2[r,z,a]=[r,c(a)],\qquad
 \widehat p_1[r,z,\theta]=[r,\theta]
\]
of \cref{wb:cusp-cone-angle-forgotten-sphere-carriers} relate the
conical carriers to the angle-forgotten sphere targets. Here $c$
collapses the marked one-skeleton in $\overline T^2$.
On the radial slices their products are exactly the quotient maps
from $Q_T^2$ and $C_T^4$ defining the metrics on
$\mathbb S_{12,T}^4$ and $\mathbb S_{24,T}^4$ in that theorem.
On those radial slices, the inverse off the collapsed sets takes
the unique marked tuple.
The origins $p_T$ map to the collapsed points. The marked midpoint
classes are
\[
 \zeta_{12,T}=[c(1/2,1/2),c(1/2,1/2)],\qquad
 \zeta_{24,T}=[\ell_T/2,\ell_T/2,\ell_T/2,\ell_T/2].
\]
Their quotient distances to the collapsed points are at least
$(T-C_E)/2$ and exactly $\ell_T/2$, respectively, by the
closed-set distance formula and the period estimates proved in
\cref{wb:cusp-cone-angle-forgotten-sphere-carriers}.
These distances tend to infinity. For any fixed compatible metric
on the compact ambient $S^6$ or $S^8$, the corresponding distances
are bounded by that sphere's diameter. The identity on each moving
sphere is therefore a homeomorphism between these two metric
topologies, and the displayed pair of points proves that it is
not an isometry for every sufficiently large $T$.
\end{remark}

''', 'D02/D11/D12/D13/D20', 'mapsIII:rem:source-and-moving-metrics',
         'Replace the orphan summary by its unique differential and moving-metric content, with exact kernel maps, quotient maps, inverse representatives and distance obstruction. Repeated beta and unrescaled-rank conclusions retain their sole owners 03DC and 0374/0375.')

# 037J retains its unique modulus and compactness arguments; cite full earlier maps.
j = new.index(r'\label{wb:cusp-cone-sharp-global-R4-scope}')
pa = new.index(r'\begin{proof}', j)
pb = new.index(r'\end{proof}', pa) + len(r'\end{proof}')
oldj = new[pa:pb]
tail = oldj[oldj.index('The whole sphere and conical spaces in these routes are compact'):]
cone_start = tail.index('The cone-vertex assertion has an independent local pair check.')
cone_end = tail.index('Finally let $D_0$', cone_start)
tail = tail[:cone_start] + r'''The local cone comparison is the map
$[r,a]\mapsto[r/r_0,c_\nu(a)]$, inverse
$[s,b]\mapsto[r_0s,c_\nu^{-1}(b)]$, of
\cref{wb:cusp-cone-explicit-carriers}. Its complete pair-homology
calculation in \eqref{wb:cusp-cone-carrier-local-homology} applies
to these same vertices, with the coned-cell boundary map as its
specified isomorphism. It gives the stated local chart obstruction.

''' + tail[cone_end:]
tail = tail.replace(r'\cref{wb:sphere-metric-fixed-realization}', r'\cref{mapsIII:lem:fixed-conical-metrics}')
newj = r'''\begin{proof}
For the first realization use the homeomorphisms in
\cref{wb:cusp-cone-literal-R4-open-cells}. Explicitly, set
\[
 u_T(a)=[Y_Ta],\quad v_T(a)=[\ell_Ta],\quad
 \eta(t)=\tfrac12(1+t/\sqrt{1+t^2}).
\]
The maps are $h_{12,T}(u_T\eta^2,u_T\eta^2)$ and
$h_{24,T}(v_T\eta,v_T\eta,v_T\eta,v_T\eta)$, with the arguments
split into the indicated ordered pairs or single coordinates.
Their inverse takes the unique uncollapsed tuple, applies the
representative maps $Y_T^{-1}$ or division by $\ell_T$ in $(0,1)$,
and applies $\eta^{-1}(a)=(2a-1)/(2\sqrt{a(1-a)})$.
The cited theorem proves both inverse identities, the exact
synchronized cube coordinates, and the open-in-the-moving-sphere
and nonclosed-in-the-ambient-sphere assertions for these maps.

For the second realization put
\[
 A_T^{(12)}=\operatorname{diag}(Y_T,Y_T),\qquad
 A_T^{(24)}=\ell_TI_4,\qquad
 P_{\nu,T}=\mathbb R^4/A_T^{(\nu)}\mathbb Z^4.
\]
The maps splitting two coordinate pairs or four coordinates
identify $P_{12,T}$ with $Q_T^2$ and $P_{24,T}$ with $C_T^4$;
their inverse concatenates the coordinates. They preserve the
quotient-distance formula
$d_T([x],[y])=\min_{n\in\mathbb Z^4}|x-y+A_T^{(\nu)}n|$.
The exact maps in \cref{wb:cusp-cone-explicit-carriers} are
\[
 k_{\nu,T}[x]=[r_T,c_\nu^{-1}([(A_T^{(\nu)})^{-1}x])],
 \qquad j_{\nu,T}=\delta_\nu k_{\nu,T}.
\]
Their inverse at positive height sends a lift $b$ of the marked
angle to $[A_T^{(\nu)}b]$; changing $b$ by an integer changes its
image by a period. The commutative sphere-fibre restrictions in
that theorem identify these maps with the actual target slices.
The complete whole-ball isometry proof in
\cref{wb:cusp-cone-S12-route,wb:cusp-cone-S24-route}, transported
by these maps and inverses, supplies the intrinsic Euclidean
limits. Their diameters diverge by
\cref{wb:cusp-cone-intrinsic-expansion}.
For the fixed metrics of \cref{mapsIII:lem:fixed-conical-metrics},
the exact first forms give
\[
 j_{12,T}^*d_T^{\mathrm{slice}}=(r_T/T)d_T,\qquad
 j_{24,T}^*d_T^{\mathrm{slice}}=(r_T/\ell_T)d_T.
\]
The corresponding unrescaled path-metric diameters are at most
$r_T(1+C_E/T)$ and $r_T$. Inclusion bounds the restricted ambient
distance by the intrinsic path distance.

For the third realization use $e_\nu(x)=[0,x]$ and its
unique-coordinate inverse from
\cref{wb:cusp-cone-exact-decompactification-space}.
That theorem proves that the zero fibre is a closed Euclidean
boundary fibre. Its exact comparison map is
\[
 \beta_\nu[s,x]=
 \begin{cases}
 [e^{-2\pi/s},c_\nu^{-1}([(A_{1/s}^{(\nu)})^{-1}x])],&s>0,\\
 d_\nu,&s=0.
 \end{cases}
\]
The positive-height inverse sends $(r,a)$ to
$[s,A_{1/s}^{(\nu)}b]$, where $s=-2\pi/\log r$ and $b$ is any
lift of $c_\nu(a)$. Both compositions, representative independence
and continuity at zero are proved there. Thus
$\delta_\nu\beta_\nu e_\nu$ is the constant vertex map, while
the positive-fibre restrictions are precisely the slices above.
The closed noncompact zero fibre also proves that
$\mathfrak E_\nu$ is noncompact.

''' + tail
edit(oldj, newj, 'D12/D14/D20', 'wb:cusp-cone-sharp-global-R4-scope',
     'Use each earlier complete open-cell, cone, entire-ball and boundary-fibre proof through its exact map and inverse. Retain every realization and the full unique compact-image, metric modulus, sphere diameter and finite-T isometric-embedding obstructions. The relocation now follows the metric construction it uses.')

# Bounded format helpers: every unresolved item remains an explicit stop.
for helper in [presentation.statement_records_to_small_tags, presentation.remove_manual_equation_tags]:
    result = helper(new)
    candidate, edits, unresolved = result[:3]
    assert not unresolved, unresolved
    for item in edits:
        changes.append(dict(type=item.kind, statement_id=item.statement_label or 'equation in fixed_target_metrics',
            old_location='fixed_target_metrics.tex helper input line ' + str(new[:item.start].count('\n') + 1),
            old_page='pending final concordance', new_location='same mathematical owner', new_page='pending final build',
            old_text=item.old, new_text=item.new, reason=item.reason,
            review_status='exact bounded helper edit; final whole readback pending'))
    new = candidate

# Formal statements retained from the receivers need their visible existing tags.
formal = re.compile(r'(\\begin\{(?:theorem|lemma|proposition|corollary|definition|remark)\}(?:\[[\s\S]*?\])?\s*\\hypertarget\{tag-([^}]+)\}\{\}\\label\{([^}]+)\})(?!\n\{\\normalfont)')
matches = list(formal.finditer(new))
for match in reversed(matches):
    following = new[match.end():match.end()+90]
    if following.lstrip().startswith(r'{\normalfont\scriptsize tag'):
        continue
    edit(match[1], match[1] + '\n' + r'{\normalfont\scriptsize tag ' + match[2] + r'}\par',
         'D10', match[3], 'Add the small visible permanent tag to this formal result; retain its label and hypertarget once.')

for pattern in [r'\\label\{([^}]+)\}', r'\\hypertarget\{([^}]+)\}']:
    previous, current = Counter(re.findall(pattern, old)), Counter(re.findall(pattern, new))
    assert all(current[k] == v for k, v in previous.items()), (pattern, previous - current, current - previous)
    assert all(v == 1 for k, v in current.items() if k not in previous)
assert new.count(r'\[') == new.count(r'\]')
assert r'\StatementRecord' not in new
PATH.write_text(new)
fields = ['type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
with (OUT / 'S6_SERIES_PUBLISH_III_metrics_publication_defects.tsv').open('w', newline='') as handle:
    writer = csv.DictWriter(handle, fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(changes)
print('Metric input lines', len(old.splitlines()), 'edited lines', len(new.splitlines()))
print('Exact local defect rows', len(changes))
print('New tags Q30W Q30X Q30Y; all pre-existing labels and targets retained once at their prior multiplicities.')
print('No canonical/shared writes; all proof and criterion credit awaits complete reading and root admission.')
