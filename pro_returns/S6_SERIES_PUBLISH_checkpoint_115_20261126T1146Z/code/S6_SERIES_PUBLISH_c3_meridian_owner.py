"""Consolidate the two existing full-fibre fundamental-group proofs."""
from S6_SERIES_PUBLISH_c3_edit import *

text = SOURCE.read_text()
start1 = text.index(r'\subsection{The specialization fundamental group}')
end1 = text.index(r'\subsection{', start1 + 15)
old1 = text[start1:end1]
start4 = text.index(r'\subsection{The full-fibre meridian presentation}')
end4 = text.index(r'\subsection{', start4 + 15)
old4 = text[start4:end4]

new1 = r'''\subsection{The specialization fundamental group}

\begin{proposition}[Fundamental group of an irreducible fibre]\hypertarget{tag-02Y2}{}\label{night:P4R.1}\label{stmt:P4R.1}
\StatementRecord{night:P4R.1}{proved}{02Y2}{the definitions and constructions stated in the proof}
Let $f:X\to\Delta$ be a proper holomorphic degeneration of complex
two-tori with smooth total threefold and central fibre $mS$, where
$S$ is irreducible and reduced. Choose a positive small-loop
monodromy $A$ on $\Lambda=H_1(T^4;\mathbb Z)$ and a lift $t$ of
the positive base generator, with $tvt^{-1}=A(v)$ for
$v\in\Lambda$. A positive meridian of $S$ has the form
$\mu=\lambda t^m$ for some $\lambda\in\Lambda$. The inclusion
of $S$ in a sufficiently small full tube induces an isomorphism
on fundamental groups, and the regular-fibre inclusion gives
\[
 \pi_1(S)\simeq
 (\Lambda\rtimes_A\langle t\rangle)/\langle\!\langle\mu\rangle\!\rangle,
 \qquad
 \pi_1(S)/\operatorname{im}\Lambda\simeq\mathbb Z/m,
 \qquad
 b_1(S)=\dim_{\mathbb Q}\ker(A-I).
\]
In particular $\operatorname{im}\Lambda$ is an abelian normal
subgroup with finite cyclic quotient, so $\pi_1(S)$ is virtually
abelian.
\end{proposition}
\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item The neighbourhood-retraction statement immediately after
Definition~1 of \cite[p.~85]{BobadillaKollar2012} applies to this
proper holomorphic map of complex spaces. It gives an open base
neighbourhood $V_0$ of zero such that $W_0=f^{-1}(V_0)$ deformation
retracts onto $S$. Choose a round disc $\Delta_0\subset V_0$ and
put $U_0=f^{-1}(\Delta_0)$. The restriction $U_0\to\Delta_0$ is
again proper, so the same statement gives $V_1\subset\Delta_0$
with $W_1=f^{-1}(V_1)$ deformation retracting onto $S$. Choose a
round disc $\Delta_1\subset V_1$ and put $U_1=f^{-1}(\Delta_1)$.
Thus
\[
 S\subset U_1\subset W_1\subset U_0\subset W_0.
\]
Write $r_j:W_j\to S$ for the two retractions. Their restrictions
to $S$ are the identity.

\item Put $U_i^*=U_i\setminus S$. The proper smooth fibrations
$U_i^*\to\Delta_i^*$ have fibre $T^4$. Their homotopy sequences
and $\pi_2(\Delta_i^*)=0$ give
\[
 \pi_1(U_i^*)=\Lambda\rtimes_A\langle t\rangle.
\]
The splitting is obtained by choosing $t$ over the positive
generator of the infinite cyclic base group. Every element is
uniquely $\lambda t^n$. Use the same base point over $\Delta_1^*$
for both fibrations. The inclusion of punctured discs induces
an isomorphism on their fundamental groups and the fibre map
is the identity. The two exact sequences therefore identify
$\pi_1(U_1^*)\to\pi_1(U_0^*)$ with an isomorphism preserving
the lattice and the positive base generator.

The inclusion $U_i^*\to U_i$ is surjective on fundamental groups.
A loop can be perturbed off the real-codimension-two smooth
stratum of $S$ and off its higher-codimension singular strata.
A null-homotopy disc avoids the singular strata and meets
$S_{\rm reg}$ in finitely many transverse points. Deleting
small discs about those intersections expresses the kernel
as the normal closure of smooth-support meridians. The smooth
locus of the irreducible $S$ is connected. A path in it and a
trivialization of the complex normal line give an annulus of
positive meridians, proving that they are conjugate. The same
meridian can be chosen in $U_1^*$, so the isomorphism of the two
punctured-tube groups identifies these normal closures. It
follows that $\pi_1(U_1)\to\pi_1(U_0)$ is an isomorphism.

\item This isomorphism factors through $\pi_1(W_1)$. The inclusion
$S\to W_1$ is inverse to $(r_1)_*$ on fundamental groups, so the
inclusion $S\to U_0$ is surjective on fundamental groups.
The restriction $r_0|_{U_0}$ is a left inverse to that inclusion,
which proves injectivity. These two maps identify
$\pi_1(U_0)$ with $\pi_1(S)$, including the regular-fibre map.

At a smooth point of $S$, write $f=vz^m$ with $v$ a holomorphic
unit. On a small coordinate neighbourhood,
$z'=z\exp((\log v)/m)$ is a holomorphic normal coordinate and
$f=(z')^m$. The positive circle $z'=a\exp(2\pi i\theta)$,
$0\le\theta\le1$, maps to $a^m\exp(2\pi im\theta)$.
Its image in the base group is therefore $m$, and its class is
$\mu=\lambda t^m$. The kernel calculation proves the asserted
normal-closure presentation.

\item The image of $\Lambda$ is abelian and normal. Dividing
by it leaves exactly the presentation $\langle t\mid t^m=1\rangle$,
which gives the stated cyclic quotient. Rational abelianization
of the full presentation is
\[
 \frac{(\Lambda/(A-I)\Lambda)\otimes\mathbb Q\ \oplus\ \mathbb Qt}
      {\mathbb Q(\overline\lambda+mt)}.
\]
Put $V=(\Lambda/(A-I)\Lambda)\otimes\mathbb Q$. The map
$(v,c)\mapsto v-c\overline\lambda/m$ induces an isomorphism of
this quotient with $V$, whose inverse is $v\mapsto[(v,0)]$.
Rank-nullity for $A-I$ identifies the dimension of its
cokernel with the dimension of its kernel. This proves the
formula for $b_1(S)$.
\end{enumerate}
\end{proof}

'''
new4 = r'''\subsection{Rational incidence trees}

\begin{proposition}[Euler number for a rational incidence tree]\hypertarget{tag-02YG}{}\label{night:P4R.4}\label{stmt:P4R.4}
\StatementRecord{night:P4R.4}{proved}{02YG}{\SeriesRef{night:P4.13}, \SeriesRef{night:P4R.1}, \SeriesRef{night:P4R.3}}
For the support in \SeriesRef{night:P4R.3}, a singular-locus
incidence graph that is a tree of rational normalization
components gives $e(S)\ge3$.
\end{proposition}
\begin{proof}
Put $C=\operatorname{Sing}(S)_{\rm red}$ and let $c\ge1$ be
its number of irreducible components. The normalization
pushout and incidence-graph calculation in
\SeriesRef{night:P4R.3}, with all normalization genera zero
and graph cycle rank zero, give
\[
 \pi_1(S)\simeq\pi_1(C)=1,\qquad e(C)=c+1\ge2.
\]
The cyclic quotient in \SeriesRef{night:P4R.1} forces $m=1$.
Its formula for $b_1(S)$ gives $\det(I-A)\ne0$ for the positive
monodromy $A$. By \SeriesRef{night:P4.13},
$e(S_{\rm reg})=\det(I-A)\ge0$. This nonzero integer is at least
one, and additivity gives $e(S)=e(S_{\rm reg})+e(C)\ge3$.
\end{proof}

'''
apply_edit(old1,new1,'II-C3-MERIDIAN-OWNER',['D12','D14'],'night:P4R.1',
    'specialization fundamental group',
    'Transfer the existing full meridian presentation and rational abelianization from P4R.4, whose hypotheses are exactly those of P4R.1. Preserve the original virtual-abelian conclusion. Two applications of the opened proper-map neighbourhood theorem supply the nested retractions; compare the actual inclusions and normal closures.')
apply_edit(old4,new4,'II-C3-MERIDIAN-TREE',['D12','D14'],'night:P4R.4',
    'rational incidence trees',
    'Keep the rational-tree Euler consequence here and use the earlier single meridian owner. Apply the already proved conductor graph model at g_i=0 and b=0, preserving its exact pi1 and Euler conclusions.')

# These complete consumer proofs were read before this reference-only edit.
for label in ['night:P4.51','night:P4.40']:
    text=SOURCE.read_text(); middle=text.index('\\label{'+label+'}')
    a=text.rfind(r'\begin{proposition}',0,middle)
    b=text.index(r'\end{proof}',middle)+len(r'\end{proof}')
    before=text[a:b]; after=before.replace('night:P4R.4','night:P4R.1')
    assert before!=after
    apply_edit(before,after,'II-C3-MERIDIAN-USE-'+label.split(':')[-1].replace('.','-'),
        ['D12','D14'],label,'complete proposition and proof',
        'The existing regular-fibre map, exact cyclic quotient, and b1 calculation now have their sole owner at P4R.1. The complete consumer statement and proof were read; only the owner reference changes. Later refined-conductor inputs remain subject to their separate full-use review.')
    add_event(label,'II-C3-ROOT-MERIDIAN-USE-'+label.split(':')[-1],
        'used and rechecked in this run',
        'Complete old and receiving proof read. Exact-meridian applications preserve f, mS, lattice, monodromy and maps; only P4R.4 owner references become P4R.1. This is an exposed comparison, not independent evidence; no completion claimed for other refined-conductor inputs.',
        'S6_SERIES_PUBLISH_II.tex',group='II-C3-MERIDIAN-OWNER')

apply_edit(r'\SeriesRef{night:P4R.4}\quad Meridian quotient and rational incidence trees.',
    r'\SeriesRef{night:P4R.4}\quad Euler number for a rational incidence tree.',
    'II-C3-MERIDIAN-LIST',['D12'],'night:P4R.4','further-results list',
    'Make the reader-facing list agree with the retained rational-tree conclusion.')
apply_edit(r'Meridian relation-space isomorphism, determinant sign and incidence-tree Euler count (\cref{night:P4R.4})',
    r'Meridian relation-space isomorphism, determinant sign and incidence-tree Euler count (\cref{night:P4R.1,night:P4R.4})',
    'II-C3-MERIDIAN-PROGRAM',['D12'],'night:P4R.1; night:P4R.4','programs table',
    'Retain the same program path and identify the two surviving mathematical owners.')
add_event('night:P4R.1; night:P4R.4','II-C3-ROOT-MERIDIAN-CONSOLIDATION',
    'used and rechecked in this run',
    'Read both complete prior proofs and both complete receiving proofs. Exact same degeneration hypotheses identify the quotient and b1 assertions; nested proper restrictions, fibre-group inclusions, corresponding positive meridians, retraction inverses, and rational quotient maps are explicit. The tree case applies the existing graph formula at genus and cycle rank zero. All labels and permanent targets preserved. Exposed comparison, no independent credit.',
    'S6_SERIES_PUBLISH_II.tex',group='II-C3-MERIDIAN-OWNER')
preserve_identifiers(text,SOURCE.read_text())
print('Existing meridian conclusions now have one earlier owner; three consumer references and the program association follow it.')
