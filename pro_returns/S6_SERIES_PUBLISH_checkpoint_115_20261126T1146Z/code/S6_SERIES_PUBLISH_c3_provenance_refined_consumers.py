#!/usr/bin/env python3
"""Prepare bounded Paper II consumer proposals; never write the shared source.

The input is the exposed snapshot taken before this consumer reading.  The
reviewed flag records a complete old/receiving comparison, not independence.
"""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import argparse
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
TMP = ROOT.parents[1] / 'tmp'
OUT = ROOT / 'agents/continuation3_provenance/refined_consumers'
OUT.mkdir(parents=True, exist_ok=True)
SNAPSHOT = TMP / 'c3_provenance_refined_consumers_base.tex'
source = SNAPSHOT.read_text()
owner_re = re.compile(r'\\begin\{(proposition|lemma|theorem|corollary|definition|remark|example|cited)\}')


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def tsv(path, rows):
    with path.open('w', newline='') as f:
        writer = csv.DictWriter(f, list(rows[0]), delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def owner(text, label):
    p = text.index(r'\label{' + label + '}')
    begins = list(owner_re.finditer(text, 0, p))
    begin = begins[-1]
    env = begin.group(1)
    end = text.index(r'\end{' + env + '}', p) + len(r'\end{' + env + '}')
    proof = text.find(r'\begin{proof}', end)
    following = owner_re.search(text, end)
    if proof >= 0 and (not following or proof < following.start()):
        end = text.index(r'\end{proof}', proof) + len(r'\end{proof}')
    return text[begin.start():end]


labels = ['night:P4R.13', 'night:P4.51', 'night:P4.40', 'night:P4.43',
          'night:P4.42', 'night:P4R.18', 'night:P4.55', 'night:P4.58']
old = {label: owner(source, label) for label in labels}
units = old.copy()
rows = []


def record(label, before, after, types, reason, location='statement and proof'):
    rows.append(dict(change_id=f'II-C3-REFINED-{len(rows)+1:03d}', type=types,
        statement_id=label, old_location=location,
        old_page='cp35 continuation3 snapshot; final concordance pending',
        new_location=location, new_page='integrated build pending',
        old_text=before, new_text=after, reason=reason,
        review_status='Complete receiving comparison pending --reviewed.'))


def edit(label, before, after, types, reason, all_matches=False):
    count = units[label].count(before)
    assert count == 1 or (all_matches and count > 0), (label, count, before[:120])
    for i in range(count if all_matches else 1):
        record(label, before, after, types, reason,
               f'statement and proof; occurrence {i+1}' if count > 1 else 'statement and proof')
    units[label] = units[label].replace(before, after) if all_matches else units[label].replace(before, after, 1)


def interval(label, first, following):
    text = units[label]
    a = text.index(first)
    b = text.index(following, a)
    return text[a:b]


PRIMARY = 'lem:II:horizontal-primary-conductor'
primary = r'''\begin{lemma}[Restriction to the horizontal primary conductor]
\hypertarget{tag-P313}{}\label{lem:II:horizontal-primary-conductor}
\StatementRecord{lem:II:horizontal-primary-conductor}{proved}{P313}{\cref{night:P4R.6,night:P4.33}; \cite[Remark~2.1, p.~415]{Greb2011}}
In the standing torus-fibration setting of
\cref{def:II:standing-torus-fibration}, let $mS$ have irreducible,
reduced, singular support. Write $\nu:N\to S$ for normalization,
$\sigma:T\to N$ for its minimal resolution and $\rho=\nu\sigma$.
Suppose that $T$ is obtained by point blowups of a minimal ruled
surface over a curve of genus $g\ge1$ and that the pole divisor
$D$ of \cref{night:P4R.6} has horizontal part $2H$ for the induced
ruling, where the section $H$ is not contracted by $\sigma$.
Let $C_H=\rho(H)$ and let $C_{H,\rm sch}$ be the primary component
of the image conductor scheme $C_{\rm sch}$ supported on $C_H$.
For the conductor ideal $I_N\subset\mathcal O_N$, the residue and
restriction maps give injections of coherent $\mathcal O_S$-algebras
\begin{equation}
 \mathcal O_{C_{\rm sch}}\longrightarrow
 \nu_*(\mathcal O_N/I_N)\longrightarrow\rho_*\mathcal O_D.
 \label{eq:II:elliptic-conductor-algebra-injection}
\end{equation}
Under each point blowup $\beta:T'\to T''$ in the contraction to a
minimal ruled model, with successive pole divisors $D',D''$, one has
\begin{equation}
 \beta_*\mathcal O_{D'}=\mathcal O_{D''},
 \qquad R^1\beta_*\mathcal O_{D'}=0.
 \label{eq:II:elliptic-conductor-blowup-pushforward}
\end{equation}
The primary restriction is injective on $H^0$ and surjective on
$H^1$. In particular,
\begin{equation}
 g-1=\chi(\mathcal O_{C_{\rm sch}})
 \le\chi(\mathcal O_{C_{H,\rm sch}}).
 \label{eq:II:elliptic-primary-Euler-comparison}
\end{equation}
\end{lemma}
\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item Apply \cref{lem:II:irrational-ruled-boundary} to this ruling,
blowup sequence and divisor $D$. Its double-section case gives
the rational vertical trees required by \cref{night:P4.33}.
The noncontracted section therefore gives rational singularities
of $N$ and $h^1(N,\mathcal O_N)=g$. Put
$L_N=\nu^*\omega_S$. Finite duality in that proposition identifies
$I_N=\omega_N\otimes L_N^{-1}$. The proper resolution $\sigma$
has $R^1\sigma_*\mathcal O_T=0$ and fibres of dimension at most
one; $N$ is a normal Cohen--Macaulay surface. Apply
\cite[Remark~2.1, p.~415]{Greb2011} to this $N$ and $\sigma$.
Its canonical-sheaf equality is the trace isomorphism
$\sigma_*\omega_T=\omega_N$. The pole identity and projection
formula give
\[
 \sigma_*\mathcal O_T(-D)
 =\sigma_*(\omega_T\otimes\sigma^*L_N^{-1})
 =I_N.
\]
These are the same ideal subsheaves of $\mathcal O_N$: the pole
identity uses the pullback of the residue section defining finite
duality, and the trace is its identity on the birational
isomorphism locus. This agreement determines the maps between
the torsion-free sheaves. The divisor ideal sequence gives
$\mathcal O_N/I_N\hookrightarrow\sigma_*\mathcal O_D$; composing
with the injection from the finite conductor square gives
\eqref{eq:II:elliptic-conductor-algebra-injection}.

\item At a point blowup the canonical-boundary identity is
$D'=\beta^*D''-E_\beta$. Its structure-sheaf direct images are
$\beta_*\mathcal O=\mathcal O$ and $R^1\beta_*\mathcal O=0$.
Moreover,
\[
 \beta_*\mathcal O(E_\beta)=\mathcal O,
 \qquad R^1\beta_*\mathcal O(E_\beta)=0.
\]
For the first equality, a meromorphic function with a pole only
on $E_\beta$ descends off the centre and extends across it by
Hartogs. The exact sequence
$0\to\mathcal O\to\mathcal O(E_\beta)
\to\mathcal O_{E_\beta}(-1)\to0$, together with
$H^0(\mathbb P^1,\mathcal O(-1))=
H^1(\mathbb P^1,\mathcal O(-1))=0$, gives the second equality.
The structure-sheaf calculation follows on the two blowup charts,
or from the exceptional filtration with successive
$\mathcal O_{\mathbb P^1}(j)$, $j\ge0$. Projection by
$\mathcal O(-D'')$ and the two divisor ideal sequences now give
\eqref{eq:II:elliptic-conductor-blowup-pushforward}, with its
algebra map induced by pullback and quotient. Higher direct
images in degree two vanish because the fibres have dimension
at most one.

\item Thus $H^0(D,\mathcal O_D)=H^0(D_0,\mathcal O_{D_0})$,
where on the minimal ruled surface
$D_0=2H_0+V_0$ and $V_0=\sum_j a_jF_j$.
The kernel of restriction to $2H_0$ is
$\mathcal O_{V_0}(-2H_0)$. Its filtration on each thick fibre
$a_jF_j$ has successive layers $\mathcal O_{\mathbb P^1}(-2)$,
since $F_j^2=0$ and $H_0F_j=1$. It has no global section.
The Cartier curve $2H_0$ is Cohen--Macaulay and has no
zero-dimensional associated point. A global function on $D$
which vanishes at the generic doubled section is therefore zero.

\item Proposition~\ref{night:P4.33} makes the image conductor
Cohen--Macaulay of pure dimension one. For
$R=\mathcal O_{S,p}$ and its conductor ideal $I$, take every
minimal prime $\mathfrak p_i$ over $I$ corresponding to a local branch
of the global component $C_H$. Its component ideal is
\[
 J_H=\bigcap_i\bigl(IR_{\mathfrak p_i}\cap R\bigr).
\]
The isolated primary components are uniquely determined, so
these intersections agree on overlaps and define
$C_{H,\rm sch}$, including its multibranch points.
Restriction gives a
surjection $\mathcal O_{C_{\rm sch}}\to
\mathcal O_{C_{H,\rm sch}}$. A global section of its kernel maps
by \eqref{eq:II:elliptic-conductor-algebra-injection} to a function
on $D$ vanishing at the generic doubled section, so is zero by
the preceding item. The kernel sheaf has support of dimension
at most one and hence has zero second cohomology. The restriction
is therefore injective on $H^0$ and surjective on $H^1$.
Its Euler inequality, together with
$\chi(\mathcal O_{C_{\rm sch}})=g-1$ from
\cref{night:P4.33}, proves
\eqref{eq:II:elliptic-primary-Euler-comparison}.
\end{enumerate}
\end{proof}'''

GRAPH = 'lem:II:positive-ruled-conductor-graph'
graph = r'''\begin{lemma}[The conductor graph at positive Euler number]
\hypertarget{tag-P314}{}\label{lem:II:positive-ruled-conductor-graph}
\StatementRecord{lem:II:positive-ruled-conductor-graph}{proved}{P314}{\cref{night:P4.26,night:P4.35,night:P4R.13}}
In the irreducible-or-normal-crossings torus-fibration setting of
\cref{def:II:standing-torus-fibration}, let $mS$ have irreducible
reduced support with $e(S)>0$, and suppose that its normalization
has a resolution ruled over a curve of positive genus.
For the minimal resolved normalization $\rho:T\to S$, the pole
divisor $D$ has horizontal part $2H$, and its reduced support
$A$ is the section $H$ with rational trees attached.
The reduced conductor image
$C=\operatorname{Sing}(S)_{\rm red}$ has exactly two rational
normalized components and one point-identification cycle.
The inclusion $C\hookrightarrow S$ induces an isomorphism
$\pi_1(C)\simeq\pi_1(S)\simeq\mathbb Z$.
\end{lemma}
\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item Apply \cref{night:P4.26} to the given full fibration.
Its nonnegative fibre Euler numbers sum to $c_3(Y)\le2$, so
$0<e(S)\le2$. The support is singular: a smooth ruled support
would have torsion canonical bundle by \cref{night:P4.12},
whereas its canonical degree on a general ruling fibre is $-2$.
Write $\rho=\nu\sigma$ for the normalization and its minimal
resolution, and let $D$ be the pole divisor of
\cref{night:P4R.6}. Apply
\cref{lem:II:irrational-ruled-boundary} to the same $T,D$ and
minimal ruling. Its reduced-horizontal case is excluded by
\cref{night:P4R.7}, which gives $e(S)=0$ in that case.
Thus $D$ has horizontal part $2H$, with rational trees in its
remaining support $A=D_{\rm red}$.

\item The boundary lemma gives an isomorphism
$j_*:\pi_1(A)\to\pi_1(T)$ for the inclusion $j:A\hookrightarrow T$.
The support equality in \cref{night:P4R.6} is
$A=\rho^{-1}(C)_{\rm red}$, including every exceptional component.
Apply the conductor pushout \cref{lem:II:proper-conductor-pushout}
with $(X,Y,A,C,h)=(T,S,A,C,\rho)$, using a compatible analytic
triangulation. It gives the isomorphism induced by $C\hookrightarrow S$;
its inverse is the identity on $\pi_1(C)$ and
$(\rho|_A)_*j_*^{-1}$ on the image of $\pi_1(T)$.
Proposition~\ref{night:P4R.1}, applied to a small full tube of
this same $mS$, makes the resulting group virtually abelian.

\item Let $c$ be the number of normalized components of $C$,
let their genera be $g_i$, and let $b$ be its incidence-graph
cycle rank. The connected curve and maps just obtained satisfy
\cref{lem:II:curve-normalization-graph}. Any elliptic normalized
component would satisfy every hypothesis of \cref{night:P4R.13}
for this $f,Y,B,mS$ and ruled normalization resolution, giving
$e(S)=0$. Thus the curve-group alternatives leave all $g_i=0$
and $b\le1$. In particular
\[
 \pi_1(S)\simeq F_b,\qquad e(C)=c+1-b.
\]

\item If $b=0$, the cyclic quotient of \cref{night:P4R.1}
makes $m=1$. Its formula for $b_1(S)$ gives
$\det(I-A_{\rm mon})\ne0$ for the positive small-loop
monodromy. Proposition~\ref{night:P4.13}, with this same $m=1$,
then gives the positive integer
$e(S_{\rm reg})=\det(I-A_{\rm mon})\ge1$.
But $e(C)=c+1\ge2$, so $e(S)\ge3$, a contradiction.
Therefore $b=1$ and $\pi_1(C)\simeq\mathbb Z$.
Now $e(C)=c$, and the nonnegative smooth-locus Euler number in
\cref{night:P4.13} gives $c\le e(S)\le2$.

\item The resolved pole support is the section with rational trees
from the first item. The final ruled application in the proof of
\cref{night:P4.35} contracts precisely the connected exceptional
subtrees of $\sigma$ and shows that the reduced conductor in $N$
has no graph cycles. The same proposition therefore excludes
$c=1$, since $b=1$. Hence $c=2$, proving all the assertions.
\end{enumerate}
\end{proof}'''

# Structural edits follow below.  Both extracted proofs use the original
# maps and full global scope, and add no transverse-type restriction.

o = 'night:P4R.13'
primary_old = interval(o, r'\item We first construct a map', r'\item We evaluate the primary quotient')
record(PRIMARY, primary_old, primary, 'D12;D14;D18;D19;D25',
       'Extract the complete existing primary-restriction construction before its genus specialization. The noncontracted doubled section, rational singularities, residue/trace identification, every blowup direct-image map, generic determination and primary H0/H1 restriction are explicit. At a multibranch point take the intersection at every local minimal prime of the same global image component. The three equation labels move with their mathematical owner.')
units[PRIMARY] = primary
edit(o, primary_old, r'''\item Apply \cref{lem:II:horizontal-primary-conductor} with
$\sigma=\rho_N$, the pole divisor $D$ above, and $C_H=C_E$.
The preceding item makes $H$ noncontracted; the ruling has
positive genus and horizontal pole part $2H$. Thus this is the
same conductor ideal $I_N$ and the same primary quotient
$C_{E,\rm sch}=C_{H,\rm sch}$. The restriction map gives
\eqref{eq:II:elliptic-primary-Euler-comparison}.

''', 'D12;D14;D25',
     'Apply the extracted restriction owner to precisely the elliptic component C_E and the same normalization resolution; retain the entire conductor scheme on the left of the Euler comparison.')
reduced_old = interval(o, r'\item Suppose the horizontal part of $D_0$ is reduced.',
                       'The coefficient-one conductor gives generic transverse nodes,')
edit(o, reduced_old, r'''\item Suppose the horizontal part of $D_0$ is reduced.
Apply \cref{lem:II:irrational-ruled-boundary} to the same
minimal ruled model $T_0$, blowdown $\beta$ and divisor $D$.
It gives genus one, one elliptic bisection or two disjoint
elliptic sections, all with coefficient one, and no vertical
pole component. Proposition~\ref{night:P4R.7}, with this
normalization resolution, gives $N=T$ smooth and minimal
and $e(S)=0$.

''', 'D12',
     'Use the complete earlier ruled-boundary and reduced-horizontal owners for the identical T0,beta,D and normalization resolution; the following immersion/conductor-square calculation is retained in full.')
edit(o, r'''The residue formula of \cref{night:P4.34} expresses a branch's
conductor exponent as its intrinsic conductor exponent plus
its intersection multiplicities with the other branches.
An intrinsically singular branch has exponent at least two.
Exponent one on every sheet therefore gives two smooth
transverse branches generically, and $\deg\eta=2$.''', r'''Apply \cref{lem:II:plane-branch-conductor} to the reduced
generic transverse plane equation of $S$. Exponent one on
every sheet gives two smooth transverse branches, so
$\deg\eta=2$.''', 'D12',
     'Use the earlier residue/conductor owner with the identical reduced transverse equation; its exponent-one clause gives the two smooth transverse sheets and hence the degree.')
edit(o, r'''The intrinsic conductor exponent of a singular
plane branch is at least two, and each additional branch
increases it by its positive intersection multiplicity.
The possibilities are therefore a single ordinary cusp,
two smooth branches with intersection multiplicity two, or
three smooth branches with pairwise intersection multiplicity
one.''', r'''The formula in \cref{lem:II:plane-branch-conductor}, applied
to this reduced transverse equation, leaves a single branch
with $\delta=1$, two smooth branches with intersection
multiplicity two, or three smooth branches with pairwise
intersection multiplicity one. The first ring is
$\mathbb C\{t^2,t^3\}$ by the exponent-two enumeration in
the proof of \cref{night:P4.32}.''', 'D12;D25',
     'Retain the complete cusp/tacnode/triple enumeration through its earlier exact conductor formula and the same exponent-two branch-ring calculation.')

o = 'night:P4.51'
graph_old = interval(o, r'\item We prove the stated ruled application with its full', r'\end{enumerate}')
record(GRAPH, graph_old, graph, 'D12;D14;D25',
       'Give the repeated positive-ruled reduction one owner before its consumers. Transfer the full Euler, doubled-section, pushout, genus, meridian and graph calculation; complete the already used one-component exclusion by P4.35. State the full irreducible-or-normal-crossings global scope.')
units[GRAPH] = graph
edit(o, graph_old, r'''\item For the ruled application, the hypotheses of
\cref{lem:II:positive-ruled-conductor-graph} hold for this
$f:Y\to B$ and this full fibre $mS$: all reduced supports
are irreducible or normal crossing, $e(S)>0$, and its
normalization resolution is ruled over a positive-genus
curve. The lemma identifies $\pi_1(S)$ with $\mathbb Z$
through the conductor inclusion. Hence $b_1(S)=1$, and
the preceding four items apply to every reduced local
equation of this same $S$.

''', 'D12;D14;D25',
     'Apply the shared graph owner without changing either clause of P4.51; the complete local-fibre embedding, unit flow, covering lift and intersection-form proof remain.')

o = 'night:P4.40'
proof_old = units[o][units[o].index(r'\begin{proof}'):]
proof_new = r'''\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item Suppose such a support exists. Apply
\cref{lem:II:positive-ruled-conductor-graph} with the given
$f:Y\to B$, its full fibre $mS$ and its minimal normalization
resolution $\rho:T\to S$. The global support hypothesis,
$e(S)>0$ and the positive ruling genus are exactly its
hypotheses. The pole divisor has a doubled horizontal
section $H$ with rational trees attached, and the image
conductor $C$ has two rational normalized components and
one point-identification cycle.

The section $H$ is contracted by the normalization resolution:
otherwise its generic conductor exponent would be two by
\cref{night:P4R.6}, whereas the reduced transverse node has
exponent one on each branch by
\cref{lem:II:plane-branch-conductor}. Apply the contracted-section
clause of \cref{night:P4.33} to this same divisor and resolution.
It gives $\chi(\mathcal O_{C_{\rm sch}})=-1$.
The image conductor is Cohen--Macaulay of dimension one and
generically reduced in type $A_1$. Its nilradical would have
finite support, so depth one makes it zero. Thus
$C_{\rm sch}=C$ and $\chi(\mathcal O_C)=-1$.

\item Write $r_p$ for the number of normalized preimages of
$p\in C$ and $\delta_p$ for its normalization-quotient length.
The two rational components give
$\chi(\mathcal O_C)=2-\sum_p\delta_p$.
The one-cycle incidence graph gives
$\sum_p(r_p-1)=2-1+1=2$. Therefore
\[
 \sum_p\delta_p=3,\qquad
 \sum_p(r_p-1)=2,\qquad
 \sum_p\bigl(\delta_p-(r_p-1)\bigr)=1.
\]
Each last summand is nonnegative: taking independent
branch values modulo the common value embeds a vector space
of dimension $r_p-1$ into the normalization quotient.
Hence exactly one point has excess one, and $r_p\le3$
at every point. Apply \cref{ii:excess-one-curve-germs} to
that reduced curve germ in the smooth threefold $Y$.
Its analytic isomorphisms give a singular plane curve,
a plane cusp with a transverse smooth branch, or a plane
tacnode with a transverse smooth branch. Each is excluded
by \cref{night:P4.38}, applied to the same reduced
hypersurface germ and its assumed generic transverse
type $A_1$ on every critical-curve component. This is
the required contradiction.
\end{enumerate}
\end{proof}'''
edit(o, proof_old, proof_new, 'D12;D14;D25',
     'Preserve the refined statement byte-for-byte. Apply the complete shared positive-ruled graph reduction in its full global scope, then retain the contracted-section conductor Euler value, purity/reduction, exact excess-one counts and local exclusion map.')

o = 'night:P4.43'
statement_old = interval(o, 'In the requested full-fibration classes,', r'\end{proposition}')
edit(o, statement_old, r'''In the irreducible-or-normal-crossings torus-fibration setting
of \cref{def:II:standing-torus-fibration}, an irreducible
reduced fibre support whose normalization has a resolution
ruled over a positive-genus curve cannot have $e(S)>0$ and
generic transverse type $A_2$ on every component of its
critical curve.
''', 'D05;D25',
     'Replace the undefined requested classes by the previously intended full global setting; specify the same irreducible support, normalization resolution, positive Euler number and uniform cusp hypothesis.')
last_old = interval(o, r'\item On the other hand, the proved positive ruled reduction,', r'\end{enumerate}')
edit(o, last_old, r'''\item The normalization homeomorphism from the first item
therefore identifies $\pi_1(N)$ with $\mathbb Z$.
This contradicts the preceding resolution quotients:
their abelianizations have ranks zero or $2g$, whereas
the abelianization of $\mathbb Z$ has rank one.

''', 'D04;D12;D25',
     'Replace the unnamed broad reduction by the exact graph owner and identify its group map with the normalization homeomorphism already proved; retain the surface-group and contracted-section alternatives.')
edit(o, r'''\item Let $B$ be the base curve of the minimal ruled surface,
of genus $g\ge1$, and let $H$ be the horizontal section
of coefficient two in the total pole divisor.''', r'''\item Apply \cref{lem:II:positive-ruled-conductor-graph}
to this $f:Y\to B$ and full fibre $mS$. The statement gives
its global support hypothesis, $e(S)>0$ and the positive
ruling genus. It gives the doubled horizontal section $H$
and identifies $\pi_1(S)$ with $\mathbb Z$ through
$C\hookrightarrow S$. Let $B_0$ be the base curve of the
minimal ruled surface, of genus $g\ge1$.''', 'D12;D14;D20;D25',
     'Obtain the doubled section before using it. Keep the fibration base B distinct from the ruling base B0, so the global-hypothesis substitution is the original f:Y→B.')
edit(o, r'\pi_1(B)', r'\pi_1(B_0)', 'D20',
     'Use the same ruling base B0 in both resolution-group identifications.', all_matches=True)
edit(o, 'These quotients are the actual\ntopological contractions',
     'These quotients are the topological contractions', 'D08',
     'Keep the quotient-to-resolution identification without process emphasis.')

o = 'night:P4.42'
statement_old = interval(o, 'In the requested global support classes,', r'\end{proposition}')
edit(o, statement_old, r'''In the irreducible-or-normal-crossings torus-fibration setting
of \cref{def:II:standing-torus-fibration}, let $S$ be an
irreducible reduced fibre support whose normalization has
a resolution ruled over a positive-genus curve. Suppose
that its critical curve has generic transverse type $A_3$
on every component. Its point-identification cycle cannot
consist of two two-branch points, including nonordinary
points and additional unibranch singular points of the
critical curve.
''', 'D05;D25',
     'State the complete global setting and uniform A3 hypothesis explicitly, preserving the original absence of an Euler-positivity assumption and all nonordinary/additional-unibranch clauses.')
first_old = interval(o, r'\item After P4R.13,', r'\item At a planar curve point,')
edit(o, first_old, r'''\item Proposition~\ref{night:P4.26} gives $e(S)\ge0$.
At $e(S)=0$, the uniform $A_3$ case of
\cref{night:P4.32} has a smooth elliptic conductor image.
Its normalization is the identity and has no distinct
branch points to identify. Thus the asserted two-point
configuration has $e(S)>0$. Apply
\cref{lem:II:positive-ruled-conductor-graph} to this
$f:Y\to B$ and $mS$. The conductor then has two rational
normalized components and one graph cycle. In the stated
configuration that cycle consists of two two-branch
points. We compute their local Hessian defects.

''', 'D04;D12;D25',
     'Preserve the entire old statement scope: rule out its cycle at Euler zero through P4.32 and the identity normalization map, then apply the positive graph owner with every hypothesis checked.')
edit(o, r'''\item Apply the rank-one Hessian calculation
of P4R.10 to the two normalized projective lines. On each
line the rank-two conormal kernel has degree $2+\deg R$.''', r'''\item Apply the rank-one Hessian calculation of
\cref{night:P4R.10} to the two normalization maps
$j_i:\mathbb P^1\to C\hookrightarrow Y$ and the nilradical
of the full conductor scheme, pulled back to each normalized
component. Here
$K_i=\ker(j_i^*\Omega_Y\to\Omega_{\mathbb P^1}(-R_i))$
is the normalized derivative kernel. Since
$c_1(\Omega_Y)\cdot C_i=0$, it has degree
$2+\deg R_i$.''', 'D04;D25',
     'Specify the two rational-component substitutions, the differentiated-conormal map and the degree calculation used in the full-conductor Hessian formula.')
edit(o, r'''The rank-one quotient has Euler characteristic
$3+\deg R-\deg L$.''', r'''The quotient $K_i/L_i$ has Euler characteristic
$3+\deg R_i-\deg L_i$.''', 'D20;D25',
     'Keep the same component indices for the derivative kernel, ramification divisor and saturated Hessian line; the descent defects still belong to the full conductor nilradical.')

o = 'night:P4R.18'
statement_old = interval(o, 'In the remaining positive-Euler ruled case', r'\end{proposition}')
edit(o, statement_old, r'''In the irreducible-or-normal-crossings torus-fibration setting
of \cref{def:II:standing-torus-fibration}, let $mS$ have
irreducible reduced support with $e(S)>0$ and normalization
resolution ruled over a positive-genus curve. A noncontracted
horizontal pole section maps with degree two or three to a
rational normalized conductor component whose generic
transverse germ is $D_4$.
The conclusion applies to every transverse type and
conductor-exponent pattern on the other image component.
''', 'D02;D05;D25',
     'Replace the remaining-case reference by its full global assumptions; impose no condition on the other conductor component, preserving its complete transverse-type and exponent scope.')
first_old = interval(o, r'The ruled application in \cref{night:P4.51}', 'The nonconstant map')
edit(o, first_old, r'''Apply \cref{lem:II:positive-ruled-conductor-graph} to this
$f:Y\to B$ and this full fibre $mS$. Its global support,
positive-Euler and ruling-genus hypotheses are precisely
those in the statement. Thus $C$ has two rational
normalized components and one point-identification cycle.
''', 'D12;D25',
     'Replace the repeated Euler/graph/acyclicity derivation by its full shared owner with the identical fibration and support.')
third_old = interval(o, r'\item Assume that the transverse germ along $C_H$ is $A_3$.',
                     r'\item We evaluate the right side on $C_H^\nu=\mathbb P^1$.')
edit(o, third_old, r'''\item Assume that the transverse germ along $C_H$ is $A_3$.
Let $C_{H,\rm sch}$ be the primary component of the image
conductor supported on $C_H$. Apply
\cref{lem:II:horizontal-primary-conductor} with this
$\nu,\sigma,D,H$ and $C_H$. The section is noncontracted
by hypothesis, its pole coefficient is two, and the
positive-genus ruling and its rational vertical trees
are the ones just obtained. The same primary restriction
map therefore gives
\begin{equation}
 g-1=\chi(\mathcal O_{C_{\rm sch}})
 \le\chi(\mathcal O_{C_{H,\rm sch}}).
 \label{eq:horizontal-primary-euler}
\end{equation}

''', 'D02;D12;D18;D19;D25',
     'Use the primary-restriction owner at the rational component C_H, not the elliptic conclusion of P4R.13. Retain the full conductor on the left and the original equation target; its general algebra proof now stands once.')
edit(o, r'''Use the actual differentiated conormal, the saturated Hessian
line and the rank-one nilradical in the proof of \cref{night:P4R.10}. The kernel $K$
of the normalized derivative has degree $2+\deg R$, since
$c_1(Y)\cdot C_H=0$.''', r'''For the normalization map $j:\mathbb P^1\to C_H\hookrightarrow Y$,
use the differentiated conormal, saturated Hessian line
and rank-one nilradical of the primary conductor as in
\cref{night:P4R.10}. The map is
$j^*\Omega_Y\to\Omega_{\mathbb P^1}(-R)$, so its kernel
$K$ has degree $2+\deg R$, since $c_1(Y)\cdot C_H=0$.''', 'D08;D25',
     'Identify the rational normalization, derivative image and primary conductor module used by the Hessian calculation; no elliptic genus hypothesis is imported.')
edit(o, r'''At a planar point the ideal is
$(u,h)$, its symbolic square equals its ordinary square,
and the actual equation belongs to that square.''', r'''At a planar point the ideal of $C_H$ is
$(u,h)$, its symbolic square equals its ordinary square,
and the reduced equation of $S$ belongs to that square.''', 'D08;D20;D25',
     'Name the primary curve ideal and the same reduced surface equation in the local symmetric-square estimate.')
edit(o, r'\item For its branches $B_i$ the exact conductor formula is',
     r'\item Apply \cref{lem:II:plane-branch-conductor} to the reduced transverse equation and its branches $B_i$:',
     'D12;D25', 'Identify the exact earlier branch-conductor owner for the same reduced transverse equation before enumerating its exponent-two branches.')

o = 'night:P4.55'
edit(o, r'''In the remaining positive ruled case of \cref{sec:II:night-sign}, the image $A$ of the
horizontal pole section is a smooth rational curve.''', r'''In the irreducible-or-normal-crossings torus-fibration setting
of \cref{def:II:standing-torus-fibration}, let $mS$ have
irreducible reduced support with $e(S)>0$ and normalization
resolution ruled over a positive-genus curve. The image $A$
of its horizontal pole section $H$ is a smooth rational curve.''', 'D05;D20;D25',
     'State the full fibration and support hypotheses at the degree-two conclusion, preserving the unrestricted other transverse type and both self-identification exclusions.')
edit(o, r'''The primary
restriction maps in \cref{night:P4R.13,night:P4R.18} give''', r'''Apply \cref{lem:II:horizontal-primary-conductor} with the
normalization $N\to S$, its minimal resolution $T\to N$,
the noncontracted section $H$ and its image $C_H=A$.
Use the pole divisor $D_T$ of \cref{night:P4R.6} on $T$.
The preceding items give its horizontal part $2H$, rational
vertical trees and positive ruling genus. Thus the lemma's
divisor is $D_T$, while $D\subset N$ above is the reduced
normalization conductor. The primary restriction gives''', 'D12;D20;D25',
     'Apply the genus-independent primary conductor owner to A through the exact N,T,H maps; do not invoke the elliptic conclusion for a rational component.')
edit(o, r'''Adjunction gives the exact arithmetic genus''', r'''The intersection product is
$(3\xi-bF)(\xi+(e-2-b)F)=6e-6-4b$.
Adjunction therefore gives the arithmetic genus''', 'D12;D22',
     'Move the later repeated intersection computation to the point where it explains the spectral arithmetic-genus formula.')
last_old = interval(o, r'\item The intersection product is', r'\end{enumerate}')
edit(o, last_old, '', 'D12;D13',
     'The intersection identity now accompanies the earlier adjunction formula. Each strict graph-budget inequality is already proved in the respective singleton, nonsingleton and two-junction cases; remove their repeated closing proof item.')

o = 'night:P4.58'
edit(o, r'''Let $f:Y\to B$ be the fibration of Part~4.2, with
$b_1(Y)=b_2(Y)=0$, connected fibres and general fibre a
complex two-torus.''', r'''Let $f:Y\to B$ satisfy the standing torus-fibration
hypotheses of \cref{def:II:standing-torus-fibration}.''', 'D04;D05',
     'Use the numbered definition giving the same smooth compact Y, Betti vanishings, proper connected fibration and general two-torus.')
edit(o, r'''\item We finish the positive-genus ruled alternative without
a transverse-type assumption on its vertical conductor
branches. P4R.13 and the preceding reductions show that
a positive-Euler ruled support would have a doubled
horizontal pole section and an image conductor with two
rational normalized components and one graph cycle.''', r'''\item For a positive-Euler support with positive-genus ruled
normalization resolution, apply
\cref{lem:II:positive-ruled-conductor-graph} to this
$f:Y\to B$ and full fibre $mS$. Every reduced support
is irreducible or normal crossing by hypothesis. The lemma
gives a doubled horizontal pole section, two rational
normalized conductor components and one graph cycle.''', 'D02;D04;D12;D25',
     'Use the shared reduction at precisely the global hypotheses of the classification; no transverse condition is added on either conductor component.')
last_old = interval(o, r'\item The hypothesis checks are the explicit constructions', r'\end{enumerate}')
edit(o, last_old, '', 'D08;D12',
     'The same dependence on b2=0 and on torus fibres is already explicitly stated and proved in P4.10 and P4.11, including the covering-group obstruction and the stronger numerical normal-crossing sign. Remove the repeated closing summary from this classification proof.')

# Keep the section on T and its embedded image in N linked by the ruling map.
edit('night:P4.55', r'''\item We write $T\to N\to S$ for the minimal normalization
resolution.''', r'''\item Write $\nu:N\to S$ for normalization and
$\sigma:T\to N$ for its minimal resolution.''', 'D20;D25',
     'Name the two morphisms used in the embedded-section comparison, primary restriction and local branch-count substitutions.')
edit('night:P4.55', r'''\item The reduced normalization conductor $D$ has a tree as its
point-identification graph.''', r'''\item The ruled application in the proof of
\cref{night:P4.35}, with this $\sigma$ and its doubled-section
pole divisor, makes the reduced normalization conductor
$D\subset N$ a tree in its point-identification graph.''', 'D12;D25',
     'Identify the earlier owner and the same resolution map proving the tree property used in the conductor counts.')
edit('night:P4.55', r'''Its positive-genus component
$H$ is smoothly embedded: the ruling descends to $N$, and
restriction of that ruling is an inverse to $H\to N$.
In particular no two points of $H$ are identified by the
normalization resolution.''', r'''By \cref{night:P4.33}, the ruling $a:T\to E$ and its
section $h:E\simeq H\hookrightarrow T$ descend to
$q:N\to E$ and $s=\sigma\circ h:E\to N$, with
$q\circ\sigma=a$ and $q\circ s=\operatorname{id}_E$.
Thus $s$ is an embedding, and
$\sigma|_H=s\circ(a|_H)$ identifies the section $H$
with its smoothly embedded image in $N$.''', 'D12;D20;D25',
     'Apply P4.33 to the same noncontracted section and resolution; its exact q,s,a,h maps identify the two occurrences of H and provide the embedded component used in the later graph counts.')
separated_old = interval('night:P4.55', r'\paragraph{Separated self-identifications.}',
                         r'\paragraph{The actual primary conductor and smoothness of $A$.}')
edit('night:P4.55', separated_old, r'''\paragraph{Separated self-identifications.}
Suppose $p\in B\setminus A$ has two analytic branches.
Let $D_B$ be the union of conductor components mapping
to $B$, with $c_B$ normalized components and $s_B\ge1$
connected components. Its graph is a forest. Apply the
branch count in the proof of \cref{night:P4.35} with
$(D,C,p,c,k)=(D_B,B,p,c_B,s_B)$: every normalized component
maps finitely and surjectively to $B^\nu$, and at $p\notin A$
the local hypersurface branches have exactly the two
possible image branches used in that count. Their supports
pairwise intersect by the preceding item. Let
$\kappa:D_B^\nu\to D_B$ and $\eta:B^\nu\to B$ be normalization,
and let $\phi:D_B^\nu\to B^\nu$ satisfy
$\eta\phi=(\nu|_{D_B})\kappa$.
Label $p_+,p_-\in\eta^{-1}(p)$ so that the common
support branch in the cited count is the plus branch, and put
$r_\pm=|\phi^{-1}(p_\pm)|$ and
$r_q=|\kappa^{-1}(q)|$. Writing $n$ for
the number of normalization points over $p$, the count
therefore gives $r_+\ge n$, $r_-\ge c_B$, and
\[
 \sum_{q\in\nu^{-1}(p)}(r_q-1)=r_++r_--n\ge c_B.
\]
The whole forest has contribution $c_B-s_B<c_B$, a
contradiction. The identical substitution with $A$ and all
components mapping to it excludes a self-identification
of $A$ away from $B$. Thus the image cycle consists of
two distinct intersections of $A$ and $B$, or one
three-branch point belonging to both components.

''', 'D12;D25',
     'Apply the fully read P4.35 local branch count to D_B→B at p outside A, then D_A→A at p outside B. Finite surjectivity, the forest and exactly two local image branches give the same r-plus/r-minus maps and inequality; the full hypersurface intersection premise is checked before the substitution.')

# Scope is stated positively, once, with the relevant schemes and maps named.
edit('night:P4.55', r'''The other image component retains its unrestricted transverse
type.''', r'''The transverse type on the other image component is arbitrary.''', 'D02;D08;D11',
     'Preserve the full unrestricted other-component clause in positive mathematical language.')
edit('night:P4.55', r'''These are the actual conductor
curves; vertical components and their identifications are
retained throughout the argument.''', r'''Here $D$ includes the vertical conductor components and
all their point identifications.''', 'D02;D08',
     'Identify the whole reduced normalization conductor used by the forest calculation, including the vertical components and every identification.')
edit('night:P4R.13', r'''The presence of other conductor components
changes none of those maps.''', r'''At intersections with the other conductor components,
these maps are the restrictions of the same differentiation
map, saturated Hessian line and quotient projection.''', 'D02;D25',
     'Name the exact primary-quotient maps at intersections, preserving the established unrestricted other-component scope.')
for before, after in [
    ('The actual primary conductor and smoothness of $A$', 'The primary conductor and smoothness of $A$'),
    ('the actual pole divisor', 'the pole divisor'),
    ('the actual equation', 'the reduced equation'),
    ('The actual reduced equation', 'The reduced equation'),
    ('an actual global section', 'a global section'),
    ('the actual map', 'the map'),
    ('The actual cubic', 'The cubic'),
    ('The actual function', 'The reduced function'),
    ('the actual\npole divisor', 'the pole divisor'),
    ('the\nactual image conductor', 'the image conductor'),
    ('an\nactual global section', 'a global section'),
    ('the\nactual map', 'the map'),
    ('The actual\nfunction', 'The reduced function'),
    ('the\nactual weighted normalization', 'the weighted normalization'),
    ('its actual normalization', 'its normalization'),
    ('is supplied by one rational', 'lies on one rational'),
    ('the actual weighted', 'the weighted'),
    ('actual topological contractions', 'topological contractions'),
    ('The actual primary', 'The primary'),
    ('the actual image conductor', 'the image conductor'),
    ('the actual conductor', 'the conductor'),
    ('the actual differentiated', 'the differentiated'),
    ('the actual reduced equation', 'the reduced equation'),
    ('with the identifications retained', 'with all point identifications'),
    ('We specify the spectral morphisms. At a generic point', 'At a generic point'),
]:
    for label in list(units):
        if before in units[label]:
            edit(label, before, after, 'D08',
                 'Remove process emphasis from the fully read sentence while retaining its mathematical object, map and scope.', all_matches=True)

# Resolve all printed internal references through existing statement labels.
for before, after in [
    ('P4.6--P4.8', r'\cref{night:P4.6,night:P4.7,night:P4.8}'),
    ('P4.36--P4.37', r'\cref{night:P4.36,night:P4.37}'),
]:
    for label in list(units):
        if before in units[label]:
            edit(label, before, after, 'D04', 'Resolve the statement range through its existing numbered owners.', all_matches=True)
bare = re.compile(r'(?<![\w:{\\])P4R?\.\d+(?!\d|\.\d)')
for label in list(units):
    for token in dict.fromkeys(bare.findall(units[label])):
        # Replace only the printed tokens, never label or StatementRecord keys.
        pattern = re.compile(r'(?<![\w:{\\])' + re.escape(token) + r'(?!\d|\.\d)')
        for match in reversed(list(pattern.finditer(units[label]))):
            record(label, token, r'\cref{night:' + token + '}', 'D04',
                   'Resolve this printed run number through the existing statement label.',
                   'printed reference at receiving offset ' + str(match.start()))
            units[label] = units[label][:match.start()] + r'\cref{night:' + token + '}' + units[label][match.end():]
for label in list(units):
    for match in reversed(list(re.finditer(r'(\\item |\.\s+)\\cref\{', units[label]))):
        before = match.group()
        after = before.replace(r'\cref{', r'\Cref{')
        record(label, before, after, 'D23', 'Capitalize the generated statement reference at the start of its sentence.')
        units[label] = units[label][:match.start()] + after + units[label][match.end():]

# Every manual equation receives its final section counter.  Handle complete
# display blocks, so a TeX linebreak followed by [2pt] is never an opener.
equations = {}
manual = re.compile(r'(?<!\\)\\\[((?:(?!(?<!\\)\\\]).)*?)\\tag\{([^}]+)\}((?:(?!(?<!\\)\\\]).)*?)(?<!\\)\\\]', re.S)
for label in list(units):
    while True:
        match = manual.search(units[label])
        if not match:
            break
        before = match.group()
        left, number, right = match.groups()
        eq_labels = re.findall(r'\\label\{([^}]+)\}', left + right)
        eq_label = eq_labels[0] if eq_labels else 'eq:II:refined-' + re.sub(r'[^A-Za-z0-9]+', '-', number).strip('-')
        equations[number] = eq_label
        suffix = '' if eq_labels else r'\label{' + eq_label + '}'
        after = '\\begin{equation}' + left + right + suffix + '\\end{equation}'
        after = re.sub(r'\n[ \t]*\n', '\n', after)
        edit(label, before, after, 'D19',
             'Use section equation numbering while preserving every old mathematical label and target; remove paragraph breaks inside display math.')
for label in list(units):
    for number, eq_label in equations.items():
        if '(' + number + ')' in units[label]:
            edit(label, '(' + number + ')', r'\eqref{' + eq_label + '}', 'D04;D19',
                 'Point the printed equation reference to its preserved or new automatic equation label.', all_matches=True)

headings = [
    (r'\subsection{Restriction to an elliptic conductor component}',
     r'\subsection{Primary restriction and elliptic conductor components}', 'night:P4R.13',
     'Name the general primary restriction before its elliptic specialization.'),
    (r'\subsection{The completed irreducible classification and sign theorem}',
     r'\subsection{The irreducible classification and sign theorem}', 'night:P4.58',
     'Use the mathematical section title without a completion marker.'),
]
for before, after, label, reason in headings:
    assert source.count(before) == 1
    record(label, before, after, 'D08;D14', reason, 'immediately preceding subsection title')

placements = [
    ('elliptic', 'night:P4R.13', [PRIMARY, 'night:P4R.13']),
    ('intersection', 'night:P4.51', [GRAPH, 'night:P4.51']),
    ('ordinary_double', 'night:P4.40', ['night:P4.40']),
    ('cuspidal', 'night:P4.43', ['night:P4.43']),
    ('tacnodal', 'night:P4.42', ['night:P4.42']),
    ('horizontal_type', 'night:P4R.18', ['night:P4R.18']),
    ('horizontal_cover', 'night:P4.55', ['night:P4.55']),
    ('classification', 'night:P4.58', ['night:P4.58']),
]
guards = []
pieces = []
proposed_source = source
for key, anchor, owners in placements:
    fragment = '\n\n'.join(units[label] for label in owners)
    filename = 'S6_SERIES_PUBLISH_refined_' + key + '_proposed.tex'
    (OUT / filename).write_text(fragment + '\n', newline='\n')
    pieces.append(fragment)
    assert proposed_source.count(old[anchor]) == 1
    proposed_source = proposed_source.replace(old[anchor], fragment, 1)
    guards.append(dict(change_id='II-C3-REFINED-GUARD-' + key, statement_id=anchor,
        source_file='S6_SERIES_PUBLISH_II.tex', old_sha256=digest(old[anchor]),
        new_sha256=digest(fragment), old_text=old[anchor], new_text=fragment,
        proposed_file=str((OUT / filename).relative_to(ROOT))))
for index, (before, after, label, reason) in enumerate(headings, 1):
    proposed_source = proposed_source.replace(before, after, 1)
    guards.append(dict(change_id=f'II-C3-REFINED-GUARD-heading-{index}', statement_id=label,
        source_file='S6_SERIES_PUBLISH_II.tex', old_sha256=digest(before),
        new_sha256=digest(after), old_text=before, new_text=after, proposed_file=''))
receiving = '\n\n'.join(pieces) + '\n'
(OUT / 'S6_SERIES_PUBLISH_refined_receiving_all.tex').write_text(receiving, newline='\n')

# Direct comparison guards, not a paper inventory or census refresh.
for pattern in [r'\\label\{([^}]+)\}', r'\\hypertarget\{(tag-[^}]+)\}']:
    before = Counter(re.findall(pattern, source))
    after = Counter(re.findall(pattern, proposed_source))
    assert not before - after, (pattern, before - after)
    for key in before:
        assert before[key] == after[key], (key, before[key], after[key])
assert r'\CompendiumRef' not in receiving
assert r'\tag{' not in receiving
assert not bare.search(receiving)
for label in units:
    assert receiving.count(r'\label{' + label + '}') == 1
for label in ['night:P4R.13', 'night:P4.40', 'night:P4.51']:
    env = owner_re.match(old[label]).group(1)
    marker = r'\end{' + env + '}'
    old_statement = old[label].split(marker, 1)[0] + marker
    new_statement = units[label].split(marker, 1)[0] + marker
    assert old_statement == new_statement, ('protected refined statement', label)
protected = {}
for label in ['push:src:E.5.2', 'push:src:E.5.3']:
    before = owner(source, label)
    after = owner(proposed_source, label)
    env = owner_re.match(before).group(1)
    marker = r'\end{' + env + '}'
    before = before.split(marker, 1)[0] + marker
    after = after.split(marker, 1)[0] + marker
    assert before == after
    protected[label] = digest(before)
stack = []
for match in re.finditer(r'\\(begin|end)\{([^}]+)\}', receiving):
    action, env = match.groups()
    if action == 'begin':
        stack.append(env)
    else:
        assert stack and stack[-1] == env, (match.start(), env, stack[-3:])
        stack.pop()
assert not stack
for match in re.finditer(r'\\begin\{(equation\*?|align\*?|gather\*?|multline\*?)\}(.*?)\\end\{\1\}', receiving, re.S):
    assert not re.search(r'\n[ \t]*\n', match.group(2)), ('blank display paragraph', match.start())
refs = re.findall(r'\\(?:[cC]ref|[eE]qref|ref|SeriesRef)\*?\{([^}]+)\}', receiving)
all_labels = set(re.findall(r'\\label\{([^}]+)\}', proposed_source))
series_keys = set(re.findall(r'csname SRef@([^\\]+)\\endcsname', proposed_source))
missing = sorted({key.strip() for group in refs for key in group.split(',')
                  if key.strip() not in all_labels | series_keys})
assert not missing, missing

parser = argparse.ArgumentParser()
parser.add_argument('--reviewed', action='store_true')
args = parser.parse_args()
if args.reviewed:
    for row in rows:
        row['review_status'] = 'Complete old/receiving owner and application-map comparison read; exposed used-and-rechecked evidence.'
tsv(OUT / 'S6_SERIES_PUBLISH_refined_defects.tsv', rows)
tsv(OUT / 'S6_SERIES_PUBLISH_refined_guards.tsv', guards)
status = dict(scope='Every Paper II direct and equation-label consumer of night:P4R.13 and night:P4.40; eight existing owners and two extracted owners.',
    source_snapshot=str(SNAPSHOT), shared_writes=False, source_admission=False,
    complete_old_reading=True, complete_receiving_reading=args.reviewed,
    placements=placements, protected_statement_sha256=protected,
    preserved_refined_statements=['night:P4R.13', 'night:P4.40', 'night:P4.51'],
    unused_reserved_tag='P280',
    prerequisite_gates=['Foundations: factor-preserving full-multiplicity deformations in night:P4.41 and night:P4.45 remain open; night:P4R.14 is admitted and night:P4R.15 is covered by admitted P298. These owners are unchanged here.',
        'Root has admitted the zero-Euler and Hessian consolidations at P253, night:P4.29, night:P4.30, night:P4.31, night:P4R.10, night:P4R.11, night:P4.32 and night:P4.33. The receiving P4.33 statement and full proof were reread for P313 and P4.55.'],
    final_gates='Integrated build, page concordance and final provenance/count refresh remain with root.')
(OUT / 'S6_SERIES_PUBLISH_refined_status.json').write_text(json.dumps(status, indent=2, ensure_ascii=False) + '\n', newline='\n')
print(f'Prepared {len(rows)} exact defect rows and {len(guards)} bounded guards; receiving reviewed={args.reviewed}; shared source unchanged.')


