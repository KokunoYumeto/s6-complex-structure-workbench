"""Arithmetic periods: exact normalization and operative known-input proofs."""
from pathlib import Path
import json,hashlib,datetime
B=Path(__file__).parent
base=B/'S6_SERIES_PUBLISH_I_editorial_batch_e_preview.tex'
original=base.read_text();s=original;guards=[];removed=[]
def patch(old,new,reason,ids=()):
 global s
 assert s.count(old)==1,(reason,s.count(old),old[:150])
 guards.append(dict(id=f'IA-F-{len(guards)+1:02}',old=old,new=new,
 expected_count=1,reason=reason,statement_ids=list(ids)))
 s=s.replace(old,new,1)
def archive(name,text,why):
 removed.append(dict(name=name,reason=why,original=text,
 sha256=hashlib.sha256(text.encode()).hexdigest()))

patch(r'\section{Periods, compact subgroups, and the transcendence question}',
      r'\section{Arithmetic periods and compact subgroups}',
      'Separate the proved arithmetic material from the final open discussion.')
a=s.index(r'We use a Weierstrass equation over $\overline\Q$')
b=s.index(r'\begin{proposition}[sigma expression',a)
old=s[a:b]
new=r'''\begin{definition}[Algebraic period coordinates]
\hypertarget{tag-IA10}{}\label{I:algebraic-period-coordinates}
Use an algebraic Weierstrass equation and invariant differential
as in \cref{I:def:theta-height}. Write
$\Lambda=\mathbb Z\omega_1+\mathbb Z\omega_2$ with
$\Im(\omega_2/\omega_1)>0$,
$\zeta(z+\omega_j)=\zeta(z)+\eta_j$, and extend
$\eta:\Lambda\to\mathbb C$ real-linearly.
The discriminant is that of the equation in this differential.
For a homothety $\Lambda\mapsto c\Lambda$, $u\mapsto cu$,
\[
 \sigma_{c\Lambda}(cu)=c\sigma_\Lambda(u),\qquad
 \eta_{c\Lambda}(cu)=c^{-1}\eta_\Lambda(u),\qquad
 \Delta(c\Lambda)=c^{-12}\Delta(\Lambda).
\]
These formulas cancel the factors in \eqref{ari:eq:cp-klein},
so $N$ has the same value in the transported coordinates.
\end{definition}

'''
patch(old,new,'Number the general period setup and exhibit its exact homothety.',
      ('ari:C.7.1',))
old=r'''Changing an algebraic differential of the
third kind adds an algebraic multiple of $u$ and algebraic
endpoint terms.'''
new=r'''Changing the third-kind differential while retaining its simple
poles and residues adds an algebraic multiple of $u$.
Adding an exact algebraic differential to a relative-integral
representative adds algebraic endpoint differences when both
endpoints are regular.'''
patch(old,new,'Specify the fixed pole/residue scope of the differential change.',
      ('ari:C.7.1',))
needle=r'''This is the pullback of an algebraic differential with residues
$+1$ at $-P$ and $-1$ at $O$.'''
patch(needle,needle+r'''
Two algebraic differentials with precisely these simple poles
and residues differ by a holomorphic differential, hence by
$c\,dz$ with $c\in\overline{\mathbb Q}$.
Integration gives $cu$; integration of $df$ gives the stated
endpoint difference.''',
'Prove the exact differential-change assertion.',('ari:C.7.1',))
old=r'''\citet[Definitions 2.3--2.4 and
Section 6]{bertolin2022};'''
new=r'''\citet[Section~2.3, equations~(2.10)--(2.13), pp.~7--8;
Definitions~2.3--2.4, p.~8; Section~6.1, pp.~26--27,
arXiv v2]{bertolin2022};'''
patch(old,new,'Give the actually read generalized-logarithm and Serre-function locators.',
      ('ari:C.7.1',))

a=s.index(r'\citet[Construction~3.4, p.~12, Lemma~3.5, p.~13, and')
b=s.index(r'\begin{proposition}[the motivic groups',a)
old=s[a:b]
body=old[:old.index('The following calculation')]
new=r'''\begin{remark}[The motivic dimension formula]
\hypertarget{tag-IA11}{}\label{I:motivic-dimension-input}
'''+body+r'''The polarization calculation below identifies these groups
for the point and extension data in this paper.
\end{remark}

'''
patch(old,new,'Number the known dimension input and remove the forward conjectural-theorem description.')
old=r'''The holomorphic theta normalization proposed for the CM interpolation approach differs from the
norm occurring in the stated problem. We make that distinction explicit,
including the finite-character ambiguity in the multiplication law.'''
patch(old,r'''The multiplication law below retains the finite sign character.
Its exact relation to the metric norm is \eqref{ari:eq:ct-Gaussian}.''',
      'Introduce the exact relation without problem-history framing.')
old=r'''Thus the unsquared quotient is an algebraic function on $E$, but
it need not be a rational function on $E$.'''
new=r'''The unsquared quotient is a meromorphic function on the
cover of degree at most two with function field
$\overline{\mathbb Q}(E)(\sqrt{F_\alpha})$.
It descends to $E$ exactly when its residual sign character is trivial.'''
patch(old,new,'Give the exact finite-cover morphism behind the squared multiplication law.',
      ('ari:C.7.6',))
patch(r'''The additive group $\mathcal O u$ has
rank two, not more than four.''',
      r'''The additive group $\mathcal O u$ has rank two.''',
      'State the exact rank.',('ari:C.7.6',))

# Restore the checked Waldschmidt/analytic-subgroup applications.
a=s.index(r'The expanded source derivation is retained in the proof compendium, Paper~I, label \nolinkurl{ari:C.7.7}.')
b=s.index(r'\paragraph{The exact dependence',a)
old=s[a:b]
new=r'''\begin{proof}
The original French statement
\cite[unnumbered theorem, Section~3, p.~113; Corollary~1,
Section~4, pp.~113--114]{waldschmidt1979sigma}
applies to algebraic invariants, algebraic elliptic points
$\exp_Eu,\exp_Ev$, and $\beta\in\overline{\mathbb Q}$.
For nontorsion $\exp_Ev$ and $u,u+v\notin\Lambda$, it proves
transcendence of
\[
 \frac{\sigma(u+v)}{\sigma(u)\sigma(v)}
              e^{(\beta-\zeta(v))u}.
\]
Take $v=u$ and $\beta=0$. Since
$\sigma(2u)=-\wp'(u)\sigma(u)^4$, this value is
$-\wp'(u)\sigma(u)^2e^{-u\zeta(u)}$.
The nonzero factor $-\wp'(u)$ is algebraic, which proves
the first assertion.

For the second, use the algebraic universal vector extension
with analytic periods $(\omega,\eta(\omega))$.
On $E\setminus\{O\}$ an algebraic fibre coordinate is
$t=w-\zeta(z)$: the zeta addition formula makes its group
cocycle rational in the Weierstrass coordinates.
Near $O$, use
$t_O=t-\wp'(z)/(2\wp(z))=w+O(z^3)$.
The overlap change is rational, so $(z,w)$ are the tangent
coordinates of an algebraic chart at the identity.
If $b=\zeta(u)-s_2u$ were algebraic, the logarithm
$(u,\zeta(u)-b)$ would exponentiate to the algebraic point
with fibre coordinate $-b$ and would lie on the algebraic
line $w=s_2z$, since \cref{ari:C.7.6} gives
$s_2\in\overline{\mathbb Q}$.
The analytic subgroup theorem
\cite[Theorem~6.1, arXiv v8, p.~43]{huber2022}
would then give a one-dimensional algebraic subgroup projecting
nontrivially to $E$. Such a subgroup is an elliptic curve
mapping isogenously to $E$: a one-dimensional affine algebraic
group has no nonconstant group morphism to an elliptic curve.
Its inclusion would split the vector extension after that
isogeny. The extension class in $H^1(E,\mathcal O_E)$ is nonzero
and stays nonzero under isogeny, because trace divided by the
degree is a left inverse to pullback. Equivalently, its period
vectors cannot lie on one complex line, by Legendre's relation.
This contradiction proves the second assertion.
\end{proof}

'''
patch(old,new,'Restore the operative known-result proof with exact algebraic charts and primary locators.',
      ('ari:C.7.7',))

a=s.index(r'\paragraph{The exact dependence of the theta expression on its lifts.}')
b=s.index(r'\paragraph{The archimedean term still requiring control.}',a)
old=s[a:b];archive('theta_lift_source_history',old,'Retrieval and historical correction narrative, with exact comparison retained below.')
new=r'''\begin{remark}[Lift transport for the theta expression]
\hypertarget{tag-IA12}{}\label{I:theta-lift-transport}
Put
$g(u,v)=\log(\sigma(u+v)/(\sigma(u)\sigma(v)))$ where the
three sigma factors are nonzero. Under $v\mapsto v+\omega$,
the change of $g(u,v)-s_2uv$, modulo $2\pi i\mathbb Z$, is
\[
 (\eta(\omega)-s_2\omega)u=\frac{\pi\bar\omega u}{A}.
\]
Both lifts represent the same elliptic point. Thus a relation
$N\exp_Ev=f(\exp_Eu)$ for a Rosati-antisymmetric endomorphism
retains its value, while the theta expression changes by this
explicit term. The pointwise criterion in
\cite[final slide, comment~(c)]{bertrand2017} uses compatible lifts.

For algebraic invariants and a CM elliptic curve,
\cite[p.~15-03]{waldschmidt1988theta} states, attributing the
result to Bertrand, that $\theta(u)=\sigma(u)e^{-s_2u^2/2}$
is transcendental at an algebraic nontorsion elliptic point.
The $s_2$ there is the regularized lattice sum. Its
quasiperiod identity is
$\eta(z)=s_2z+\pi\bar z/A$, the convention of \cref{ari:C.7.6}.
\end{remark}

'''
patch(old,new,'Retain the exact lift morphism and cited normalized value; remove retrieval chronology.')

a=s.index(r'\paragraph{The archimedean term still requiring control.}')
b=s.index(r'\subsection{The precise nonarchimedean comparison}',a)
old=s[a:b];archive('Gaussian_comparison_original',old,'Full original applications retained for exact comparison.')
new=old.replace(r'\paragraph{The archimedean term still requiring control.}',
r'''\begin{remark}[The Gaussian factor and arithmetic criteria]
\hypertarget{tag-IA13}{}\label{I:Gaussian-comparison}''',1)
new=new.replace(r'''The normalization proved transcendental in \ref{ari:C.7.7} instead
gives''',r'''The normalized value in \cref{ari:C.7.7} gives''')
new=new.replace(r'''Neither formula excludes algebraicity of $N(P)$: transcendence
of one complex factor does not control its absolute value or
its product with the remaining exponential.
The generic finite-order interpolation approach
supplies only the rank-two set $\mathcal O u$; it does not
meet the proposed rank-greater-than-four criterion. The
derivative approach would need the algebraicity of
$\theta'(u)/\theta(u)=\zeta(u)-s_2u$, which \ref{ari:C.7.7} excludes.
Replacing the norm by the holomorphic theta value would
therefore change the problem precisely by the factor in
\eqref{ari:eq:ct-Gaussian}.''',
r'''These identities specify the remaining exponential exactly.
The CM sampling group $\mathcal O u$ has rank two, and
$\theta'(u)/\theta(u)=\zeta(u)-s_2u$ is transcendental by
\cref{ari:C.7.7}. The arithmetic nature of the full product
in \eqref{ari:eq:ct-Gaussian} is the open question in
\cref{ari:C.7.5}.''')
new=new.replace(r'''For real $u$, hypothetical algebraicity of $N(P)$ makes
$s(u)$ algebraic, so the conclusion instead forces independence
of $e^{i\pi u/\omega_1}$ and
$\zeta(u)-\eta_1u/\omega_1$; it yields no contradiction.''',
r'''For real $u$, \eqref{ari:eq:cp-klein} gives
$N(P)=|\Delta|^{1/12}|s(u)|$.
This is the exact change of normalization for comparing that theorem
with the metric norm.''')
new=new.replace(r'''These
specific checked applications therefore do not decide the
metric norm; their source scopes and the larger CM
independence tuples are recorded separately.''','')
new=new.replace(r'''We also tested an additive-extension route.''',
r'''For vector extensions,''')
new=new.replace(r'''The theorem's hypotheses require an algebraic
point of the vector extension, equivalently an algebraic line
bundle with an algebraic connection having unitary monodromy.
\ref{ari:C.7.2} supplies only an algebraic point in one fibre of a
multiplicative extension. It does not supply that algebraic
connection. Differentiating a metric value at one algebraic
point cannot establish algebraicity of the connection there
or globally. This is the exact missing implication in that
attempt.''',
r'''Its input is an algebraic line bundle with an algebraic connection
having unitary monodromy. The compact-character construction in
\cref{ari:C.7.2} specifies a point in a multiplicative extension.
An application of the vector-extension theorem therefore requires
construction of the stated algebraic connection.''')
new=new.replace(r'''Another route uses the Latt\`es map''',
                r'''Let $f_E$ be the Latt\`es map, written''')
new=new.replace(r'''Let $f_E$ be the Latt\`es map, written $f_E$ defined by''',
                r'''Let $f_E$ be the Latt\`es map defined by''')
new=new.replace(r'''They do not apply to $f_E$. Indeed an elliptic''',
                r'''An elliptic''')
new=new.replace(r'''This checks
the failed hypothesis, rather than treating a theorem for
polynomials as a theorem for all rational maps.''','')
new=new.replace(r'''We also checked the arithmetic algebraicity criterion of''',
                r'''The arithmetic algebraicity criterion of''')
new=new.replace(r'''Besides sufficiently rapid height-normalized approximation by''',
                r'''requires sufficiently rapid height-normalized approximation by''')
new=new.replace(r'''points in a fixed number field, it requires the analytic germ
to be formally defined over that field.''',
                r'''points in a fixed number field and an analytic germ formally
defined over that field.''')
new=new.replace(r'''\citet[Theorems 1.3 and 2.3]{xie2024algebraicity}.
requires''',r'''\citet[Theorems 1.3 and 2.3]{xie2024algebraicity}
requires''')
new=new.replace(r'''The full hypothesis audit and the opened
preprint are retained in the records.''','')
new=new.rstrip()+r'''
\end{remark}

'''
patch(old,new,'Retain exact Gaussian, Lattes, formal-germ and degree comparisons as a numbered mathematical remark.')

patch(r'\subsection{The precise nonarchimedean comparison}',
      r'\subsection{Ordinary nonarchimedean heights}',
      'Use a descriptive subsection title.')
a=s.index(r'The expanded source derivation is retained in the proof compendium, Paper~I, label \nolinkurl{ari:C.7.8}.')
b=s.index(r'The comparison explains the missing step',a)
old=s[a:b]
new=r'''\begin{proof}
Use Theorem~A.1 and Lemma~A.2 in Rubin's appendix
\cite[Appendix~A, p.~1043]{agboola2006}, with its standing
CM, ordinary-prime and sign hypotheses. Theorem~A.1, attributed
there to Bertrand, gives nonzero $\mathfrak p$-adic height for
the nontorsion point over $K$.
The Galois-equivariance in
\cite[Section~2.9, pp.~587--588; Remark~2.2, p.~588]{MazurSteinTate2006}
makes the anticyclotomic height of a rational point zero:
complex conjugation fixes the point and acts by $-1$ on that
height space. Lemma~A.2 says that vanishing of two of the
cyclotomic, anticyclotomic and $\mathfrak p$ projections forces
the third to vanish. Hence the cyclotomic height is nonzero.

For the displayed curve, \cref{ari:C.6.R1,ari:C.6.R2} give
nontorsion and analytic rank one, hence sign $-1$.
The CM order has discriminant $-19$ and is maximal.
Its reduced positive binary forms have the single class
$(1,1,5)$, so the class number is one.
The minimal discriminant is $-19^3$.
There are seven points over $\mathbb F_5$, so $a_5=-1$,
proving good ordinary reduction. Equivalently, $-19$ is a
nonzero square modulo $5$. These verify every stated hypothesis.
\end{proof}

'''
patch(old,new,'Restore the operative Rubin/Mazur–Stein–Tate application with exact hypotheses and example.',
      ('ari:C.7.8',))
a=s.index(r'The comparison explains the missing step')
b=s.index(r'\subsection{The fixed semiabelian extension',a)
old=s[a:b];archive('ordinary_archimedean_comparison',old,'Original comparison and source-hypothesis narrative.')
new=r'''\begin{remark}[The compact subgroup and the CM correction]
\hypertarget{tag-IA14}{}\label{I:CM-compact-comparison}
The complex holomorphic CM correction is $\theta$ of
\cref{ari:C.7.6}; its exact relation to the real norm includes
$\exp(-\pi|u|^2/(2A))$ as in \eqref{ari:eq:ct-Gaussian}.
The height in \cref{ari:C.7.8} has the ordinary nonarchimedean
normalization specified in its cited appendix.

Theorem~2.1 of \cite{bertrand1995} constructs nontrivial
multiplicative extensions with nontorsion algebraic points in
their maximal real compact subgroup. Its data include a
Rosati-antisymmetric endomorphism and a related nontorsion
point over a real number field.
For the diagonal class here, $NP=f(P)$ with $N>0$ and
$f+f^\dagger=0$ forces torsion: the endomorphism $N-f$ is an
isogeny because
$(N-f)^\dagger(N-f)=N^2-f^2$ is positive.
The concrete antisymmetric and diagonal extensions are
compared by the maps in \cref{ari:C.7.10}.
The vector-extension statements
\cite[Theorem~3.1]{bertrand1995}\cite[Theorem~3.1.2]{bost2009}
use an algebraic connection, as described in
\cref{I:Gaussian-comparison}.
\end{remark}

'''
patch(old,new,'Retain the exact diagonal/antisymmetric calculation and theorem hypotheses without route narration.')

for oldtitle,newtitle in [
 ('sigma expression and the third-kind period','The sigma expression and third-kind period'),
 ('the compact-subgroup criterion and the real formula','The compact subgroup and real-axis formula'),
 ('the motivic groups needed on the diagonal','The motivic groups of the diagonal data'),
 ('the exact CM multiplication law','The CM multiplication law'),
 ('with derivation: two unconditional normalized values','Two normalized transcendental values'),
 ('with derivation: a nonzero ordinary height','Nonzero ordinary heights'),
 ('the endomorphism and slope obstructions','Endomorphisms and the compact slope'),
 ('the enlarged CM action does not isolate the Gaussian','The CM action and its Gaussian eigencoordinate'),
 ('the complexified route and its exact obstructions','The complexified norm and its second derivatives'),
 ('division ratios, scalar models and translated functions','Division ratios and translated functions')]:
 patch('['+oldtitle+']','['+newtitle+']','Use a mathematical title without status or route labels.')
patch(r'\subsection{The fixed semiabelian extension and the diagonal subgroup attempt}',
      r'\subsection{The fixed semiabelian extension and its compact slope}',
      'Use a descriptive subsection title.')

for sid,rec in [
 ('ari:C.7.7',r'''\StatementRecord{ari:C.7.7}{proved}{001G}{\cref{ari:C.7.6}; \cite[unnumbered theorem, Section~3, p.~113; Corollary~1, Section~4, pp.~113--114]{waldschmidt1979sigma}; \cite[Theorem~6.1, arXiv v8, p.~43]{huber2022}}'''),
 ('ari:C.7.8',r'''\StatementRecord{ari:C.7.8}{proved}{001H}{\cref{ari:C.6.R1,ari:C.6.R2}; \cite[Appendix~A, Theorem~A.1 and Lemma~A.2, p.~1043]{agboola2006}; \cite[Section~2.9, pp.~587--588; Remark~2.2, p.~588]{MazurSteinTate2006}}''')]:
 a=s.index(r'\StatementRecord{'+sid+'}')
 b=s.index('\n\n',a)
 patch(s[a:b],rec,'Record only operative inputs; remove conjectural and source-audit references.',(sid,))

out=dict(source_path=str(base),source_sha256=hashlib.sha256(original.encode()).hexdigest(),
 generated_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
 requires_batch='S6_SERIES_PUBLISH_I_editorial_batch_e_guards.json',guards=guards)
(B/'S6_SERIES_PUBLISH_I_editorial_batch_f_guards.json').write_text(json.dumps(out,indent=2)+'\n')
(B/'S6_SERIES_PUBLISH_I_editorial_batch_f_removed.json').write_text(json.dumps(removed,indent=2)+'\n')
(B/'S6_SERIES_PUBLISH_I_editorial_batch_f_preview.tex').write_text(s)
print(json.dumps({'guards':len(guards),'removed_blocks':len(removed),
 'preview_sha256':hashlib.sha256(s.encode()).hexdigest()},indent=2))
