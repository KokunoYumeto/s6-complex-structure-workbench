"""Final arithmetic consolidation and explicit open questions."""
from pathlib import Path
import json,hashlib,datetime,re
B=Path(__file__).parent
base=B/'S6_SERIES_PUBLISH_I_editorial_batch_f_preview.tex'
original=base.read_text();s=original;guards=[];removed=[]
def patch(old,new,reason,ids=()):
 global s
 assert s.count(old)==1,(reason,s.count(old),old[:150])
 guards.append(dict(id=f'IA-G-{len(guards)+1:02}',old=old,new=new,
 expected_count=1,reason=reason,statement_ids=list(ids)))
 s=s.replace(old,new,1)
def archive(name,text,why):
 removed.append(dict(name=name,reason=why,original=text,
 sha256=hashlib.sha256(text.encode()).hexdigest()))

# Preserve the complete former conditional implication as a check record.
# The body retains its unconditional full-period identities.
a=s.index(r'\begin{proposition}[The period-conjecture implication for the local norm]')
b=s.index(r'\end{proof}',a)+len(r'\end{proof}')
old=s[a:b];archive('C74_complete_original_implication',old,
 'Original proved(H) statement and full proof, moved to records; no conjectural lower bound is asserted in the paper.')
eq1=old[old.index(r'\begin{equation}\hypertarget{tag-003I}'):old.index(r'\end{equation}',old.index(r'\begin{equation}\hypertarget{tag-003I}'))+len(r'\end{equation}')]
eq2=old[old.index(r'\begin{equation}\hypertarget{tag-003J}'):old.index(r'\end{equation}',old.index(r'\begin{equation}\hypertarget{tag-003J}'))+len(r'\end{equation}')]
new=r'''\begin{lemma}[The full-period field and the compactness relation]
\hypertarget{tag-IA19}{}\label{I:compact-period-relation}
Let $E/\overline{\mathbb Q}$ and the nontorsion point $P$
have the coordinates of \cref{ari:C.7.1}.
Put $G=G_P\times G_{\bar P}$ and
$K_0=\overline{\mathbb Q}(\Omega_G)$, where $\Omega_G$
is the full de Rham--Betti period matrix, including the
second-kind periods of both factors.
Let $R_N=(P,r_N)$ be the actual compact point specified by
\cref{ari:C.7.2}, with
$r_N=|\wp'(u)|\,|\Delta|^{-1/6}N(P)^2$, and let $(u,v)$
be a logarithm in its algebraic coordinates.
Then $u,\zeta(u),\eta(u)$ and their conjugates belong to
$K_0$, and the compactness equation is
'''+eq2+r'''
This statement makes no assertion that $R_N$ is algebraic.
\end{lemma}
\begin{proof}
The full period matrix contains
$\kappa_j=\zeta(u)\omega_j-\eta_j u$.
The coefficient matrix for $(\zeta(u),u)$ is
$\left(\begin{smallmatrix}\omega_1&-\eta_1\\
\omega_2&-\eta_2\end{smallmatrix}\right)$.
Its determinant is the nonzero Legendre determinant, so
$u,\zeta(u)\in K_0$. The same calculation in the conjugate
factor gives their conjugates.
Writing $u=a\omega_1+b\omega_2$ with $a,b\in\mathbb R$
and solving together with the conjugate equation gives
'''+eq1+r'''
Its denominator is nonzero by real-linear independence.
Thus $\eta(u)$ and its conjugate are also in $K_0$.
Finally \cref{ari:C.7.2} gives
$\Re(v-u\zeta(u)+u\eta(u))=0$.
Adding this expression to its conjugate proves
\eqref{ari:eq:cp-relation}.
\end{proof}'''
patch(old,new,'Retain the unconditional field/compactness calculation and move the open lower-bound discussion to the end.',
      ('ari:C.7.4',))
patch(r'''% Compendium-only ari:C.7.5: apparatus: verification/diagnostic record retained with source computation''','',
      'Restore the open-question anchor at the actual open discussion below.')

old=r'''The first
assertion concerns the displayed holomorphic normalization;
it does not assert transcendence of either $N(P)$ or
$\theta(u)=\sigma(u)e^{-s_2u^2/2}$.'''
new=r'''The exact relation of these normalized values to $N(P)$
and $\theta(u)=\sigma(u)e^{-s_2u^2/2}$ is
\eqref{ari:eq:ct-Gaussian}.'''
patch(old,new,'Point to the proved morphism between the normalized quantities.',('ari:C.7.7',))

# Number the functional graph calculation without retaining route narration.
a=s.index(r'\paragraph{What functional transcendence gives in this construction.}')
b=s.index(r'\subsection{A CM-stable enlargement',a)
old=s[a:b];archive('C79_functional_comparison_original',old,'Full original functional-theorem comparison.')
body=old[old.index('Indeed consider'):old.index('This is a statement over')]
body=body.replace('Indeed consider','Consider',1)
new=r'''\begin{remark}[The Zariski closure of the compact-slope graph]
\hypertarget{tag-IA15}{}\label{I:compact-slope-graph}
'''+body+r'''The graph therefore has Zariski closure
$G_Q\times\ell_c$. This equality is the functional statement
used here; the algebraicity of the particular value
$R_N=\exp_{G_Q}(u,cu)$ remains the question in
\cref{ari:C.7.5}.
\end{remark}

'''
patch(old,new,'Keep the operative nondegeneracy/graph-dimension proof in a numbered remark.',
      ('ari:C.7.9',))

a=s.index(r'The fixed-extension calculation in \ref{ari:C.7.9} does not prevent')
b=s.index(r'\begin{proposition}[The CM action',a)
old=s[a:b]
new=r'''\begin{definition}[The CM enlargement coordinates]
\hypertarget{tag-IA16}{}\label{I:CM-enlargement-coordinates}
Retain the curve, point $Q=2P$, and real logarithm $u$ of
\cref{ari:C.7.9}. Put
$\beta=\sqrt{-19}=i\sqrt{19}$, $d=19$,
$D=\zeta(u)-s_2u$, and $k=\pi/A$.
All endomorphisms and extensions below are defined over
$\overline{\mathbb Q}$.
\end{definition}

'''
patch(old,new,'Number the exact CM enlargement setup.')
patch(r'''This also gives a direct, fully normalized construction of
the antisymmetric compact lift; no unrestricted theta
criterion is being used.''',
r'''This computes the antisymmetric compact lift with the stated normalization.''',
'State the established construction directly.',('ari:C.7.10',))
patch(r'''For completeness, the matrix $dB$ can be recovered without
choosing a transcendental change of coordinates.''',
r'''The following period comparison determines $dB$ in the algebraic coordinates.''',
'Describe the exact coordinate calculation.',('ari:C.7.10',))
patch(r'''We give polynomial certificates for these values, so they
do not depend on recognition from numerical approximations.''',
r'''The following polynomial identities determine these values.''',
'Introduce the exact certificate directly.',('ari:C.7.10',))
a=s.index(r'\item The exact polynomial identities, the complete kernels, the')
b=s.index(r'\end{enumerate}',a)
old=s[a:b];archive('C710_polynomial_and_analytic_output',old,
 'Exact proof is already displayed; program/check counts and high-precision corroboration moved to records.')
patch(old,'','End the witness proof after its exact algebraic evaluations.',('ari:C.7.10',))
needle=r'\subsection{Complexifying the Gaussian: values, jets, and the rank criterion}'
new=r'''\begin{remark}[A real period basis for the CM witness]
\hypertarget{tag-IA17}{}\label{I:CM-real-period-basis}
Put $\tau_0=(1+i\sqrt{19})/2$. The integral basis change
$(1,\tau_0)\mapsto(1-2\tau_0,1-\tau_0)$ has determinant one.
Applied to the rotated basis $i(1,\tau_0)$, it gives the ratio
\[
 \tau=\frac{1+i/\sqrt{19}}2,\qquad
 \omega_1=\left(\frac{g_2(\tau)}{152}\right)^{1/4}>0.
\]
The logarithm $u$ is selected by
$0<u<\omega_1/2$, $\wp(u)=4$, and $\wp'(u)=-3$.
This fixes the analytic branch of the algebraic witness in
\cref{ari:C.7.10}.
\end{remark}

'''+needle
patch(needle,new,'Preserve the unique integral basis/branch map after archiving numerical corroboration.',
      ('ari:C.7.10',))

old=r'''The antiholomorphic Gaussian can be made holomorphic by introducing a
second variable. This gives more algebraic values under the hypothesis
in C.7(c), but the derivative and growth hypotheses of the resulting
transcendence arguments must still be checked. We do this on the
conductor-$361$ model, where all constants and conjugations are fixed.'''
new=r'''The following complexification uses the curve and conjugation of
\cref{I:CM-enlargement-coordinates}. Its diagonal values,
CM translates and normalized second derivatives are computed explicitly.'''
patch(old,new,'Introduce the proved complexification without an open hypothesis.')
patch(r'''Moreover the rank-four set does not satisfy the
explicit derivative-free finite-order criterion audited below.
These are obstructions to the stated applications of those
criteria; they do not decide the algebraicity of $N(Q)$.''',
r'''The rank-four sampling set and growth order give the numerical
comparison with \eqref{ari:eq:cc-rankcriterion} proved below.''',
'State the proved numerical comparison positively.',('ari:C.7.11',))
patch(r'''\item \textbf{The precise several-variable criteria that were checked.}''',
      r'''\item \textbf{Differential and growth criteria.}''',
      'Use a mathematical proof heading.',('ari:C.7.11',))
old=r'''\item For a criterion without differential equations we opened
\citet[Theorem 1, p.~24]{waldschmidt1975dimension}, including
its proof and a visual check of the displayed inequalities.
The source uses'''
new=r'''\item Theorem~1 of
\cite[p.~24]{waldschmidt1975dimension} uses'''
patch(old,new,'Remove source-review narration while preserving the exact criterion.',
      ('ari:C.7.11',))
patch(r'''We do not
silently discard these hypotheses.''','',
'Retain the hypotheses without review commentary.',('ari:C.7.11',))
old=r'''This
checks the particular published criterion rather than asserting
that every possible multivariable transcendence method fails.
The missing unconditional step in C.7(c) remains the exclusion
of an algebraic value on the diagonal compact leaf.'''
new=r'''Thus the stated rank and growth envelopes do not satisfy
\eqref{ari:eq:cc-rankcriterion}. The norm question is
recorded in \cref{ari:C.7.5}.'''
patch(old,new,'End with the exact tested inequality and its scope.',('ari:C.7.11',))

# Preserve the actual formal-tangent computation; reference the already
# proved vector-extension nonsplitting rather than repeat it.
old=r'''Its projection to $E$
is nonzero, so it is an elliptic curve isogenous to $E$ and
splits the vector extension after that isogeny. This is
impossible: its nonzero class in $H^1(E,\mathcal O_E)$ stays
nonzero under an isogeny, whose pullback has a left inverse
after dividing the trace by the degree. These are the same
algebraic logarithm coordinates and extension as in \ref{ari:C.7.7};
a fixed algebraic linear change of coordinates leaves the
argument unchanged.'''
new=r'''Its projection to $E$ is nonzero, so it splits the vector
extension after an isogeny. The nonsplitting argument in
\cref{ari:C.7.7} excludes this: the coordinates here are
exactly $(z,w)$ with periods $(\omega,\eta(\omega))$ and
algebraic charts $t=w-\zeta(z)$,
$t_O=t-\wp'(z)/(2\wp(z))$.'''
patch(old,new,'Consolidate the same vector-extension nonsplitting argument under its explicit coordinate identity.',
      ('ari:C.7.7','ari:C.7.11'))

patch(r'\subsection{Division values and a variable-degree interpolation test}',
      r'\subsection{Division values and interpolation bounds}',
      'Use a descriptive subsection title.')
patch(r'''The algebraicity of $N_0$ remains the open question
of \ref{ari:C.7.4}.''',
r'''The algebraicity of $N_0$ is the open question in
\cref{ari:C.7.5}.''',
'Point the unresolved value question to the final open discussion.',('ari:C.7.12',))
patch(r'''\item \emph{The exact numerical and tangent checks.}\par''',
      r'''\item \emph{Interpolation inequalities and algebraic tangents.}\par''',
      'Use a mathematical proof heading.',('ari:C.7.12',))

# The final discussion preserves the open assertion and every old anchor,
# with the full former implication retained in the archive.
a=s.index(r'\section{Open arithmetic questions for the normalized norm}')
b=s.index(r'\begin{thebibliography}',a)
old=s[a:b];archive('open_norm_original',old,'Original open discussion and full displayed decimal height.')
new=r'''\section{Open arithmetic questions for the normalized norm}
\hypertarget{tag-003T}{}\label{ari:open:norm}
\hypertarget{tag-001E}{}\label{ari:C.7.5}

The arithmetic nature of $N(P)$ remains open for algebraic
nontorsion points in this family. An explicit instance is
\[
 E:y^2=x^3-140x+784,\qquad P=(0,28),\qquad j=-3375,
 \qquad N(P)=2e^{-\widehat h_O(P)}.
\]
The point is primitive modulo rational two-torsion, and
$\widehat h_O(P)=0.46736568\ldots$.
The unresolved assertion is transcendence of
$2e^{-\widehat h_O(P)}$.
For the conductor-$361$ example
$y^2+y=x^3-38x+90$, $P=(0,9)$, the corresponding exact
formula is
\[
 N(P)=e^{-\widehat h_O(P)}
     =\exp\!\left(-\frac{L'(E,1)}{4\Omega_E}\right).
\]
Here every finite local contribution vanishes.
The compact-point equivalence in \cref{ari:C.7.2} and the
explicit constructions in \cref{ari:C.7.9,ari:C.7.10}
give precise group-theoretic forms of this same unresolved value.

The exact analytic leading quotients in
\cref{I:analytic-leading-quotients} also leave group-order
questions: the orders of the Tate--Shafarevich groups are
identified here for rows $3,5,7$ only.
In particular the analytic quotient of row eleven is exactly
$9$; its identification with
$\#\operatorname{Sha}(E_{11}/\mathbb Q)$, including its
$3$-primary part, remains open in the results of this paper.

\subsection{The unresolved relative-period bound}
\hypertarget{tag-001D}{}\label{ari:C.7.4}

The Relative Semi-abelian Conjecture
\cite[Conjecture~4.7, p.~18]{bertolin2022} proposes, for
algebraic lifts in the indicated semiabelian varieties, the bound
\[
 \operatorname{trdeg}_{\overline{\mathbb Q}(\Omega_G)}
 \overline{\mathbb Q}\bigl(\Omega_G,R,\bar R,
                   \widetilde{\log}_G(R,\bar R)\bigr)
 \geq 2\dim B_Q+\dim Z(1).
\]
The full matrix $\Omega_G$ includes the second-kind periods.
This lower bound remains open for the compact diagonal
configuration at issue here. Its relation to Grothendieck's
period conjecture for algebraic $1$-motives is given in
\cite[Proposition~4.12, pp.~19--20]{bertolin2022}.

The known calculations isolate the precise issue.
For the algebraic motives of \cref{ari:C.7.3}, projection
from the point-extension variety to the extension-coordinate
variety is an isogeny: the point coordinates agree with the
extension data under the stated polarizations.
Equivalently, $(P,\bar P)=(P,0)+(0,\bar P)$ in
$E\times\bar E$. Formula~(4.4), p.~19 of the same source
therefore gives $\dim B_Q=0$.
The remaining kernel of connected motivic groups is the
weight-$-2$ vector group $\operatorname{Lie}Z$.
After fixing the base periods its fibre is an affine torsor
of dimension $\dim Z$.

In positive Tate coordinates the central action changes
$(v,\bar v)$ by $2\pi i(c_1,c_2)$.
For an isogeny $\phi:\bar E\to E$ of degree $d$,
$\phi^{\mathsf t}J_E\phi=dJ_{\bar E}$.
Thus the dependent bracket line of \cref{ari:C.7.3}
has coordinates $(1,aa^\dagger/d)$ with positive second
coordinate; in the independent case the bracket spans both
central coordinates.
The functional $(c_1,c_2)\mapsto c_1+c_2$ is nonzero
on this central group, including when there is a further
quotient Tate direction.
Accordingly, the compactness equation
\eqref{ari:eq:cp-relation} cuts a proper affine hyperplane.
The unconditional period-field calculation is
\cref{I:compact-period-relation}; the proposed lower bound
needed to exclude an algebraic compact lift is the open step.
No conjectural lower bound is used in the preceding results.

\clearpage

'''
patch(old,new,'Place only actual open assertions in final prose; retain all original question and period anchors.',
      ('ari:C.7.4','ari:C.7.5'))

out=dict(source_path=str(base),source_sha256=hashlib.sha256(original.encode()).hexdigest(),
 generated_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
 requires_batch='S6_SERIES_PUBLISH_I_editorial_batch_f_guards.json',guards=guards)
(B/'S6_SERIES_PUBLISH_I_editorial_batch_g_guards.json').write_text(json.dumps(out,indent=2)+'\n')
(B/'S6_SERIES_PUBLISH_I_editorial_batch_g_removed.json').write_text(json.dumps(removed,indent=2)+'\n')
(B/'S6_SERIES_PUBLISH_I_editorial_batch_g_preview.tex').write_text(s)
print(json.dumps({'guards':len(guards),'removed_blocks':len(removed),
 'preview_sha256':hashlib.sha256(s.encode()).hexdigest()},indent=2))
