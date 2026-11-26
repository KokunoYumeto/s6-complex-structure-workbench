from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *

p = Package('quartic', 'subsec:II:quartic-tangent-obstruction')
source = (ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
a53 = block(source, 'cdp:st:A.5.3')
p300 = block(source, 'lem:II:proper-conductor-divisor')
p452 = block(source, 'night:P4.52')

a53_old = 'The nonexceptional part of $D_i$ is exactly the divisorial conductor, with its scheme-theoretic multiplicities.'
a53_new = a53_old + r''' On each connected exceptional configuration, all coefficients are strictly positive when the configuration meets the strict conductor or contains a curve of positive geometric genus. A zero coefficient forces that configuration to consist of smooth rational $(-2)$-curves disjoint from the strict conductor.'''
a53_receiving = p.edit(a53, a53_old, a53_new, 'D12', 'cdp:st:A.5.3',
    'Place the complete general compact-hypersurface divisor statement at its existing owner. The additional positive-block and positive-genus conclusions are the already proved P300 refinement on the identical normalization components and minimal resolutions.')
matrix_old = r'''By \cref{lem:II:exceptional-intersection}, $a=-M^{-1}v$ has nonnegative entries on each connected exceptional block. Thus $D_i=D_i^{\rm str}+\sum_j a_jE_j$ proves \eqref{cdp:eq:A.25}.'''
matrix_new = r'''By \cref{lem:II:exceptional-intersection}, every entry of $-M^{-1}$ is strictly positive on a connected exceptional block. Hence $a=-M^{-1}v$ has nonnegative entries, and all entries are positive when $v\ne0$. A meeting with $D_i^{\rm str}$ makes some $v_j>0$. A component of positive geometric genus also does so: $p_a(E_j)\ge1$ and $E_j^2<0$ give $K_{Z_i}\cdot E_j>0$. Conversely, a zero coefficient forces $v=0$ on its block. Then every $K_{Z_i}\cdot E_j=0$ and $D_i^{\rm str}\cdot E_j=0$; adjunction and minimality make every $E_j$ a smooth rational $(-2)$-curve. Thus $D_i=D_i^{\rm str}+\sum_j a_jE_j$ proves \eqref{cdp:eq:A.25} and all assertions about exceptional coefficients.'''
a53_receiving = p.edit(a53_receiving, matrix_old, matrix_new, 'D12,D22', 'cdp:st:A.5.3',
    'Retain the full original matrix/sign proof and add the exact strict-positivity and zero-coefficient consequences. Every ruled, Picard, numerical and scheme-conductor conclusion remains unchanged.')
a53_record = a53_receiving.splitlines()[1]
a53_record_new = r'\StatementRecord{cdp:st:A.5.3}{proved}{01BD}{\cref{lem:II:conductor-duality,lem:II:exceptional-intersection}; \cite[Lemma~1.1 and Corollary~1.4]{Furushima1993}}'
a53_receiving = p.edit(a53_receiving, a53_record, a53_record_new, 'D12,D14', 'cdp:st:A.5.3',
    'Record the exact earlier finite-duality and exceptional-matrix inputs used by the full proof.')
p.guard('A53 general conductor owner', a53, a53_receiving,
    'Keep the unique general compact-hypersurface divisor owner at A.5.3, with the complete positive-block refinement and all stronger original conclusions.')

p300_receiving = r'''\begin{lemma}[Conductor support in a proper torus degeneration]\hypertarget{tag-P300}{}\label{lem:II:proper-conductor-divisor}
\StatementRecord{lem:II:proper-conductor-divisor}{proved}{P300}{\cref{cdp:st:A.5.3,lem:II:conductor-duality,cdp:st:A.5.17}}
Let $f:X\to\Delta$ be a proper holomorphic map from a smooth
complex threefold to a disc, with connected fibres, smooth
over $\Delta^*$, whose smooth fibres are complex two-tori.
Let its central fibre be $mS$, with $S$ irreducible and reduced.
Write $\nu:N\to S$ for normalization, $\pi:T\to N$ for the
minimal resolution, and $\rho=\nu\pi$. Let $D$ be the canonical
effective divisor of \cref{cdp:st:A.5.3} for these maps.
Every connected exceptional configuration of $\pi$ meets
the strict conductor and has strictly positive coefficients
in $D$. The reduced singular locus of $S$ is its reduced
conductor image, and
\[
       D_{\rm red}=\rho^{-1}((\operatorname{Sing}S)_{\rm red}).
\]
The map $\rho$ is an isomorphism between the complements
of these two reduced closed sets.
\end{lemma}
\begin{proof}
Apply \cref{cdp:st:A.5.3} with its normalization component
$T_i=N$, resolution surface $Z_i=T$, $\eta=\nu$,
$\pi_i=\pi$ and $h_i=\rho$. Its divisor is defined by the
orders of the pullback of the same local generator of
$\omega_S$. It gives the conductor multiplicities and
all exceptional-coefficient assertions once every connected
exceptional configuration meets the strict conductor.
Write $D_{\rm str}$ for the strict-conductor part of $D$,
and let $p\in N$ be a singular point. Its connected
exceptional fibre is $\pi^{-1}(p)$.

'''
tail_start = p300.index('The identity in the first item makes')
tail_end = p300.index(r'\end{enumerate}', tail_start)
tail = p300[tail_start:tail_end]
tail = tail.replace('The identity in the first item makes',
    r'The finite-duality identity of \cref{lem:II:conductor-duality} makes')
tail = tail.replace(r'$\mathfrak c$ a rank-one reflexive ideal',
    r'the conductor $\mathfrak c$ a rank-one reflexive ideal')
old_final = '''Thus every exceptional block meets $D_{\\rm str}$, so its vector
$b$ in the third item is nonzero. All its coefficients $d_i$
are strictly positive.'''
new_final = r'''Thus every exceptional block meets $D_{\rm str}$, and
\cref{cdp:st:A.5.3} gives strictly positive coefficients
on the whole block.'''
assert old_final in tail
tail = tail.replace(old_final, new_final)
tail = tail.replace('This proves effectiveness and the support equality.',
    'This proves the support equality and the complement isomorphism.')
p300_receiving += tail + '\\end{proof}\n'
p.guard('P300 proper support application', p300, p300_receiving,
    'Introduce the identical canonical divisor through A.5.3 and retain the entire additional proper-torus support proof. Every removed general clause and proof step is at A.5.3; all stable identifiers and all old conclusions remain available there through the exact displayed map.')
p.record('D12,D14','lem:II:proper-conductor-divisor',p300,p300_receiving,
    'Read the whole original/current A.5.3 and P300 statements and proofs. Their first finite-duality and matrix arguments have identical maps: T_i=N, Z_i=T, eta=nu, pi_i=pi, h_i=rho, and the same pulled-back dualizing generator. General divisor/effectiveness/positive-block statements and proof now have one owner A.5.3. P300 states only the additional proper torus support result and keeps the complete reflexive-conductor, unit-conductor, exact-root isolated-point exclusion, and complement argument. R6, CR1 and UN7 retain every original hypothesis and use the identical D.')

p322 = r'''\begin{lemma}[Weighted initial forms and monodromy bounds]\hypertarget{tag-P322}{}\label{lem:II:weighted-initial-monodromy}
\StatementRecord{lem:II:weighted-initial-monodromy}{proved}{P322}{\cite[\S1.2, p.~445; \S\S3.4--3.6, pp.~451--452; \S5.3, p.~457; \S6.3, p.~461; \S7.1, p.~462]{Siersma1991Variation}; \cite[Theorem~2C.3, p.~179]{Hatcher2002}}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item Let $g:(\C^3,0)\to(\C,0)$ be a holomorphic germ
with weighted initial polynomial $P$ of positive degree $d$
for positive integer weights $w=(w_1,w_2,w_3)$. For
$c\ne0$, every finite collection of compact cycles and
intersection chains in $\{P=c\}$ transports, preserving
oriented intersections, into a local level
$\{g=c\epsilon^d\}$ for all sufficiently small positive
$\epsilon$.

\item Let $g$ be reduced and let $F$ be its compact local
Milnor fibre. Write $T$ for its monodromy on $H_2(F;\Q)$
and $M$ for the sum of the transverse plane-curve Milnor
numbers along the one-dimensional critical branches;
put $M=0$ for an isolated critical point. When the rational
intersection form of $F$ is zero,
\[
                         \operatorname{rank}(T-I)\le M.
                                                        \tag{4.52b}
\]

\item For a reduced weighted homogeneous polynomial $P$
of degree $d$ and positive integer weights $w$,
the affine fibre $\{P=1\}$ and a compact local Milnor fibre
have the same homology and weighted scalar monodromy.
Suppose that the cyclic group $\mu_d$, acting with weights
$w$, acts freely on this fibre, and put
$Q=\{P=1\}/\mu_d$. Its monodromy satisfies
\[
                  \operatorname{rank}(T-I)\ge(d-1)\chi(Q).
\]
\end{enumerate}
\end{lemma}
\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item Put $D_\epsilon(z)=(\epsilon^{w_1}z_1,
\epsilon^{w_2}z_2,\epsilon^{w_3}z_3)$ and
$G_\epsilon=\epsilon^{-d}g\circ D_\epsilon$.
These functions extend at $\epsilon=0$ with value $P$
and converge there with all derivatives on compact sets.
Weighted Euler identity gives $dP\ne0$ on $P=c$.
Choose nested compact neighbourhoods of the cycle and
intersection representatives on that level. The Hermitian
gradient divided by its squared norm solves
\[
            dG_\epsilon(V_\epsilon)=-\partial_\epsilon G_\epsilon
\]
on a neighbourhood of these chains. A cutoff equal to one
along the relevant short trajectories makes the flow
defined for small $\epsilon$. It sends the chains into
$G_\epsilon=c$. The holomorphic map $D_\epsilon$ then
puts them into $g=c\epsilon^d$ in any fixed original
coordinate ball. The flow starts with the identity, and
the scaling has its complex orientation, so all their
oriented intersection numbers are unchanged.

\item Let $\partial_2F$ be the boundary pieces over the
critical-link circles, and write
\[
 j:H_2(F;\Q)\to H_2(F,\partial F;\Q),\qquad
 j_2:H_2(F;\Q)\to H_2(F,\partial_2F;\Q).
\]
The chain-level identity of
\cite[\S3.6, pp.~451--452; \S7.1, p.~462]{Siersma1991Variation}
is
\[
                  j_2(T-I)=\operatorname{VAR}^{II}j.
                                                        \tag{4.52a}
\]
It holds in complex fibre dimension two with the displayed
unmodified maps. Poincar\'e--Lefschetz duality identifies
$j$ with the intersection pairing. Thus $j=0$ makes
$\operatorname{im}(T-I)$ lie in $\ker j_2$, the image of
$H_2(\partial_2F;\Q)$. Each boundary piece is the mapping
torus of a transverse plane-curve Milnor fibre $F_i$.
The dimension-two Wang sequence of
\cite[\S5.3, p.~457; \S6.3, p.~461]{Siersma1991Variation}
gives
\[
 H_2(\partial_2F;\Q)=\bigoplus_i\ker(A_i-I)
                   \subset\bigoplus_iH_1(F_i;\Q),
\]
where $A_i$ is vertical monodromy. This proves
\eqref{eq:II:manual:4.52b}. For an isolated critical
point the same conclusion follows from
$\ker j=\ker(T-I)$ in
\cite[Proposition~3.4, p.~451]{Siersma1991Variation}.

\item Choose an integer $L$ divisible by every $w_i$.
The weighted norm
\[
                  R_w(z)=\sum_i|z_i|^{2L/w_i}
\]
is proper and semialgebraic on $P=1$. Its critical values
form a finite set: they are semialgebraic and have measure
zero by Sard's theorem. Above the largest value, the
normalized gradient supplies a product end. A large
regular sublevel is therefore a compact core invariant
under weighted scalar monodromy. The identity
$R_w(D_\epsilon z)=|\epsilon|^{2L}R_w(z)$ shows that the
critical values on $P=t$ are $|t|^{2L/d}$ times those on
$P=1$. Weighted scaling and the same product collar
identify the core with a compact local Milnor fibre.
Reducedness gives a connected fibre and homology only
in degrees zero, one and two, by the Milnor-fibre
statements in \cite[\S1.2, p.~445; Remark~3.3, p.~451]{Siersma1991Variation}.

Every nonidentity element of $\mu_d$ acts freely on
the invariant core. The Lefschetz theorem
\cite[Theorem~2C.3, p.~179]{Hatcher2002} gives zero
Lefschetz number for those elements. At the identity
the number is $\chi(P^{-1}(1))=d\chi(Q)$.
The character formula consequently gives
\[
 H_0(F;\C)-H_1(F;\C)+H_2(F;\C)=\chi(Q)\C[\mu_d]
\]
as virtual representations. The group acts trivially
on $H_0$. Each nontrivial character therefore occurs
in $H_2$ at least $\chi(Q)$ times. Finite-order
monodromy is semisimple, proving the lower bound.
\end{enumerate}
\end{proof}
'''
p322 = p.clean(p322,'lem:II:weighted-initial-monodromy')
p.record('D12,D17','lem:II:weighted-initial-monodromy',p452,p322,
    'Extract the exact compact-cycle transport, weighted compact-core comparison, zero-pairing variation bound and free-cyclic character calculation shared by P452/P453/P454/R19. Part1 permits a nonreduced leading polynomial, since weighted Euler makes every nonzero level smooth; reducedness is required only in parts2/3. Opened Siersma1991 Sections1.2,3.4–3.6,5.3,6.2–6.5,7.1, with rendered diagrams at pp452/462, and Hatcher Theorem2C.3 p179. Retain the complete weighted-scaling/cycle-chain maps and the short dimension-two Wang/character specialization; no variation-map isomorphism in the exceptional dimension is invoked.')

statement_old = p452[:p452.index(r'\begin{proof}')]
statement_new = r'''\begin{proposition}[Multiplicity of contracted horizontal pole sections]\hypertarget{tag-02XR}{}\label{night:P4.52}\label{stmt:P4.52}
\StatementRecord{night:P4.52}{proved}{02XR}{\cref{lem:II:positive-ruled-conductor-graph,lem:II:weighted-initial-monodromy,night:P4.51,cdp:st:A.5.3,cdp:st:A.5.17,night:P4R.15}}
In the setting of \cref{lem:II:positive-ruled-conductor-graph},
let the horizontal pole section $H$ be contracted by the
minimal normalization resolution. Its image on $S$ has
ambient multiplicity exactly three. The generic transverse
types along the critical curve are arbitrary.
\end{proposition}
'''
p.record('D01,D02,D11,D14,D22','night:P4.52',statement_old,statement_new,
    'Replace the undefined workflow phrase remaining positive ruled support by its exact earlier numbered setting P314/P203, preserving the inherited irreducible-or-normal-crossings global domain, e(S)>0, irreducible mS and positive-genus ruling. The conclusion and arbitrary-transverse-type scope remain. The proof uses P451 first clause on the same irreducible full fibre and explicitly establishes its b1(S)>0 hypothesis.')

proof = r'''\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item Use $\nu:N\to S$, $\sigma:T\to N$ and
$\rho=\nu\sigma$ from
\cref{lem:II:positive-ruled-conductor-graph}.
The section $H$ has positive genus and pole coefficient two.
Connected fibres give $H^1(B;\Q)\hookrightarrow H^1(Y;\Q)=0$,
so $B\simeq\PP^1$. The nonzero integral fibre class in the
proof of \cref{cdp:st:D.1.9}, on the underlying space
$|mS|=S$, gives $b_1(S)>0$. Thus the first assertion of
\cref{night:P4.51} applies to this same full fibre $mS$.

At the contracted image write $g=g_d+g_{d+1}+\cdots$
for a reduced local equation. The full local fibration
function is $\Phi=u g^m$ with $u$ a unit. The map in
\cref{night:P4.51} transports a local $g$-level to the
same level of $h=\exp((\log u)/m)g$, and its inclusion
into the full fibre is
$h^{-1}(\delta)\hookrightarrow\Phi^{-1}(\delta^m)$.
It proves that every local $g$-fibre has zero rational
intersection form. Apply the first assertion of
\cref{lem:II:weighted-initial-monodromy} with weights
$(1,1,1)$ and $P=g_d$. The pairing on $\{g_d=1\}$
is consequently zero.

\item Suppose that the projective quartic
$C_4=\{g_4=0\}$ is reduced and has a normalization
component of positive genus. By degree, either it is
an irreducible quartic with normalization genus $g_0\ge1$,
or it is a smooth elliptic cubic and a line. In the first
case $\sum\delta_i=3-g_0\le2$, so the sum of transverse
Milnor numbers satisfies
$M=\sum_i(2\delta_i-r_i+1)\le4$.
In the second case B\'ezout gives total intersection
length three and at least one intersection point.
Thus $\sum\delta_i=3$ and $\sum(r_i-1)\ge1$, giving
$M\le5$.

The map $g_4^{-1}(1)\to\PP^2\setminus C_4$ is the
quotient by the free scalar action of $\mu_4$.
The curve normalization and genus formula give
\[
 \chi(g_4^{-1}(1))=4\chi(\PP^2\setminus C_4)=4(7-M).
\]
The last assertion of \cref{lem:II:weighted-initial-monodromy}
therefore gives
\[
             \operatorname{rank}(T-I)\ge3(7-M)\ge6>M.
                                                        \tag{4.52c}
\]
This contradicts \eqref{eq:II:manual:4.52b}; the difference
of the lower and upper bounds is $21-4M\ge1$.

\item Blow up $Y$ at the image point, with map
$\beta:Y_1\to Y$ and exceptional divisor $E$.
Let $S_1$ be the compact strict transform, put
$\mu=\beta|_{S_1}$, and write
$\rho_1:T_1\to S_1$ for its normalization followed by
minimal resolution. The proper map $\mu\rho_1:T_1\to S$
factors through $N$. Over each singular point of $N$,
minimal-resolution domination gives its factorization
through $T$; over the smooth locus the factorization is
the given map to $N=T$. They agree on their overlap,
giving a proper holomorphic modification $T_1\to T$.
It is a composition of point blowups by
\cite[Propositions~3.10 and~3.12, p.~20]{PopescuPampu2016}.
The strict transform of $H$ therefore has the same
genus and pole coefficient two.

Apply \cref{cdp:st:A.5.3} to the compact Cartier
hypersurface $S_1\subset Y_1$, with normalization
and minimal resolution $\rho_1$. Denote its canonical
effective divisor by $D_1$. In a point-blowup chart
$(r,u_1,u_2)\mapsto(r,ru_1,ru_2)$, the ambient
volume form acquires the factor $r^2$, while the reduced
equation acquires $r^d$. The residue comparison, with
the permuted charts on the other exceptional patches, gives
\[
 \omega_{S_1}=\mu^*\omega_S\otimes
                        \OO_{S_1}((2-d)E).
\]
Comparing pullbacks of the same original local generator
gives $D_{\rm old}=D_1+(d-2)\rho_1^*E$ on $T_1$.
Set $n=\operatorname{ord}_H(\rho_1^*E)>0$ and
$a=\operatorname{coeff}_H(D_1)\ge0$. Their coefficient
identity is
\[
                             2=(d-2)n+a.
                                                        \tag{4.52d}
\]
When $H$ is exceptional for $\rho_1$, its positive genus
and \cref{cdp:st:A.5.3} give $a>0$.

Thus $d\ge5$ is impossible. For $d=4$, the identity
forces $n=1,a=0$. The curve $H$ is neither exceptional
over the normalization of $S_1$ nor a strict conductor
component. At its generic point the normalization is
an isomorphism. Its image in $S_1\cap E$ has multiplicity
one, since the local exceptional parameter has order one,
and is birational to $H$. This positive-genus component
of the quartic has degree three or four, leaving at most
one linear factor. Hence the entire quartic is reduced,
and the previous item excludes it.

\item An isolated critical point of $g$ is excluded by
\cref{cdp:st:A.5.17}, applied to the same full function
$\Phi=u g^m$. Its root $h=\exp((\log u)/m)g$ and the
identity inclusion of its local level into
$\Phi^{-1}(\delta^m)$ are precisely the maps above;
the proposition carries the square-$-2$ Morse sphere
into that torus fibre.

At a nonisolated point with $d=2$, the Hessian is
nonzero. Apply \cref{night:P4R.15} to this same reduced
equation and full local fibration. It gives the product
equation $X^2+Y^k$. For even $k$, its two analytic
branches are smooth; for odd $k$, its normalization is
the smooth parametrization
$(Y,X,Z)=(v^2,\mathrm i v^k,Z)$.
Neither minimal normalization resolution has an
exceptional curve. A point with $d=1$ is smooth.
These cases cannot receive the contracted section $H$,
so the remaining multiplicity is three.
\end{enumerate}
\end{proof}
'''
p452_receiving = p.clean(statement_new+proof,'night:P4.52')
p.record('D12,D14','night:P4.52',p452,p452_receiving,
    'Transfer the common topological calculations to P322, the general divisor calculation to A.5.3, and the full isolated-point sphere argument to A.5.17. Preserve the entire quartic genus/Milnor/character obstruction, 4.52c/d payloads, exact ambient blowup adjunction and coefficient identity, and degree1/2 exclusions. The generic transverse types and all full-fibre multiplicities are unchanged. The analytic factorization citation applies directly to T1->T, with local minimal-resolution maps glued over N; no projectivity assumption is added.')
p.record('D08','night:P4.52','In the remaining positive ruled support of \\cref{sec:II:night-sign},',
    'In the setting of \\cref{lem:II:positive-ruled-conductor-graph},',
    'Replace the production-relative remainder name with the exact numbered mathematical setting, whose complete present statement and proof were read.')
p.record('D04,D19','night:P4.52','This contradicts (4.52b).',
    r'This contradicts \eqref{eq:II:manual:4.52b}.',
    'Use the prepared exact equation label for the same upper bound, now owned once by P322.')
p.record('D20','night:P4.52','projective quartic $D=\\{g_4=0\\}$',
    'projective quartic $C_4=\\{g_4=0\\}$',
    'Keep D for the canonical pole divisor of the same normalization resolution, and write C4 for the distinct projective tangent curve. The identity map defines the renamed quartic; every genus, Milnor number and complement remains unchanged.')
p.record('D22','night:P4.52','Adjunction gives exactly 2=(d-2)n+a.',
    'The blowup chart (r,u1,u2)->(r,ru1,ru2) multiplies the volume form by r^2 and the equation by r^d, yielding omega_S1=mu*omega_S tensor O((2-d)E) and the coefficient equation.',
    'Give the explicit Jacobian/residue map that supplies the constant two and the sign, at the point where the coefficient equation is used.')

header = r'\subsection{The quartic tangent obstruction}'
start = source.index(header)
end = source.index(r'\subsection{The cubic double line and its weighted leading fibre}',start)
old_unit = source[start:end]
new_unit = header+r'\label{subsec:II:quartic-tangent-obstruction}'+'\n\n'+p322+'\n'+p452_receiving+'\n'
p.guard('complete quartic tangent subsection',old_unit,new_unit,
    'Complete all-class subsection pass, with one earlier weighted comparison owner and its exact quartic/pole application. All previous equations and result identifiers are retained.')

p318_old = 'Factor $\\rho$ into point blowups.'
p318_new = r'Apply \cite[Proposition~3.12, p.~20]{PopescuPampu2016} to the proper holomorphic modification $\rho:X\to Z$ between the smooth complex surfaces in the statement, and factor it into point blowups.'
p.guard('P318 analytic factorization citation',p318_old,p318_new,
    'The freshly opened analytic factorization proposition applies to exactly rho:X->Z; the full canonical-intersection and elliptic descent proof remains unchanged.')
p.record('D17,D18','lem:II:elliptic-minimal-descent',p318_old,p318_new,
    'Read the complete current P318 statement/proof. Its rho is a proper birational morphism of smooth complex surfaces, exactly Popescu-Pampu2016 Proposition3.12 p20. Read that complete source statement and its surrounding analytic setup; it refers to algebraic proofs and their analytic adaptation, so no claim of reading a printed proof of Proposition3.12 is made. No nef, canonical, fibre or descent conclusion changes.')

bib_anchor = r'\bibitem[Ramis and Ruget(1970)]{RR70push}'
bib = r'''\bibitem[Popescu-Pampu(2016)]{PopescuPampu2016}
Patrick Popescu-Pampu.

\newblock Complex singularities and contact topology.

\newblock \emph{Winter Braids Lecture Notes}, 3, Course~III:1--74, 2016.

\newblock \doi{10.5802/wbln.14}.

\newblock \url{https://www.numdam.org/item/10.5802/wbln.14.pdf}.

'''
assert 'PopescuPampu2016}' not in source
p.guard('analytic surface source bibliography',bib_anchor,bib+bib_anchor,
    'Add the opened primary analytic source in author order, with journal/course/pages, DOI and open-archive URL.')
p.record('D18','night:P4.52 / lem:II:elliptic-minimal-descent','No analytic factorization citation or bibliography entry.',bib,
    'The primary Numdam edition is Popescu-Pampu2016, Winter Braids Lecture Notes3, CourseIII pp1–74. Propositions3.10 and3.12 are both on printed p20. The first states analytic minimal-resolution domination; the second states point-blowup factorization for proper holomorphic modifications of smooth complex surfaces. Complete source statements/setup opened; no unavailable printed proof or Laufer book opening is claimed.')

for name,fragment in [('A53',a53_receiving),('P300',p300_receiving),('P322',p322),('P452',p452_receiving)]:
    (OUT/f'S6_SERIES_PUBLISH_II_sec07_quartic_{name}.tex').write_text(fragment,newline='\n')
p.write(new_unit)
