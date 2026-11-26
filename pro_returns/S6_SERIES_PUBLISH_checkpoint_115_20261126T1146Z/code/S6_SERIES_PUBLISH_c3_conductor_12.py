#!/usr/bin/env python3
"""Prepare UN64/65 and their precise common owners; no central writes."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv, re

root = Path(__file__).resolve().parents[1]
out = root / 'agents/continuation3_conductor'
prefix = 'S6_SERIES_PUBLISH_c3_conductor_12'
old = (out / (prefix + '_input.tex')).read_text()
cut = old.index(r'\begin{proposition}[Trivial local canonical')
old64 = old[old.index(r'\begin{proposition}'):cut]
tail = old[cut:]
litcut = tail.index(r'\par\medskip\noindent\textbf{Exact relation to the primary modification literature.}')
old65, oldlit = tail[:litcut], tail[litcut:]
rows = []
REVIEWED = True

def log(kind, a, b, reason, owner):
    rows.append(dict(change_id=f'II-C3-UNRESTRICTED12-{len(rows)+1:04d}', type=kind,
        statement_id=owner, old_location='UN64 / UN65 complete original subsection; exact span supplied',
        old_page='cp35 PDF omitted; exact source span supplied',
        new_location='terminal-ruled-contractions / anticanonical-hopf-boundaries / canonical-flat-fibres',
        new_page='pending integrated final PDF', old_text=a, new_text=b, reason=reason,
        review_status=('Complete original and receiving statements/proofs read and compared; exposed editorial rereading; final integrated PDF reading remains open.' if REVIEWED else 'Prepared from complete original reading; receiving proof comparison pending.')))

def edit(s, a, b, kind, reason, owner):
    assert s.count(a) == 1, (owner, a[:100], s.count(a))
    log(kind, a, b, reason, owner)
    return s.replace(a, b, 1)

def display(s, tag):
    found = [m.group() for m in re.finditer(r'\\\[.*?\\\]', s, re.S) if r'\tag{'+tag+'}' in m.group()]
    assert len(found)==1, tag
    return found[0]

hopf = r'''\subsection{Reduced anticanonical boundaries on Hopf surfaces}\label{subsec:II:anticanonical-hopf-boundaries}

\begin{lemma}[Reduced anticanonical Hopf boundaries]\hypertarget{tag-P325}{}\label{lem:II:reduced-anticanonical-hopf}
\StatementRecord{lem:II:reduced-anticanonical-hopf}{proved}{P325}{\cref{lem:II:hopf-curves}; \cite[arXiv v1, \S2.3.1, p.~8]{AbashevaDeev2024AB}; \cite[arXiv v2, normal forms (1), p.~3; Theorem~2.1 and Remark~2.2, p.~5]{Khaled2024Hopf}}
Let $H$ be a compact Hopf surface and let $D$ be a nonempty reduced divisor whose components are disjoint smooth elliptic curves. Suppose $K_H(D)\simeq\OO_H$. Then $(H,D)$ is a diagonal primary or secondary Hopf surface with its two axes individually marked. More precisely, there are coordinates on $W=\C^2\setminus\{0\}$ in which the full deck group of $W\to H$ is diagonal and the inverse image of $D$ is $\{zw=0\}\cap W$. The two axes have distinct images on $H$. The form $dz/z\wedge dw/w$ descends to a nowhere-zero section of $K_H(D)$.
\end{lemma}
\begin{proof}
Write $H=W/\Gamma$. The finite unramified primary-cover description in \cite[arXiv v1, \S2.3.1, p.~8]{AbashevaDeev2024AB} gives a cyclic contraction subgroup of finite index: for the cover $P_0\to H$, the covering injection $\pi_1(P_0)\hookrightarrow\pi_1(H)=\Gamma$ has index equal to its degree, and the primary normal form identifies its generator with a contraction. For primary $H$ use the identity cover. Intersecting the finitely many conjugates of this subgroup gives a normal cyclic subgroup $\langle F\rangle$ of finite index, with $F$ chosen contracting. Every deck map and its inverse extend across zero by Hartogs and fix zero. The character
$\gamma\mapsto\log|\det(d\gamma)_0|$ is conjugation-invariant and is nonzero on $F$. Thus conjugation on $\langle F\rangle$ cannot send $F$ to $F^{-1}$, and $F$ is central. The quotient
$P=W/\langle F\rangle\to H$ is a finite unramified primary cover. Its pulled-back boundary $D_P$ is reduced and satisfies $K_P(D_P)\simeq\OO_P$.

Use the complete primary normal-form list in \cite[arXiv v2, p.~3 and Theorem~2.1, p.~5]{Khaled2024Hopf}. In the nonlinear case, write
$F(z,w)=(\beta^a z+w^a,\beta w)$, $a\ge1$. The unique curve is the axis $C=\{w=0\}/\langle F\rangle$, by \cref{lem:II:hopf-curves} and its primary curve description. Since $\det dF=\beta^{a+1}$, the equivariant anticanonical section $w^{a+1}\partial_z\wedge\partial_w$ has divisor $(a+1)C$, so $K_P=-(a+1)C$. The line $\OO_P(C)$ has infinite order: a positive tensor power trivializing it would turn its canonical section into a nonconstant holomorphic function on the compact connected surface, with a nonempty zero divisor. But $D_P=C$, so $K_P(D_P)=-aC$ cannot be trivial. This excludes the nonlinear case, including $a=1$.

In diagonal coordinates $F(z,w)=(\alpha z,\beta w)$, an anticanonical section lifts to $g(z,w)\partial_z\wedge\partial_w$. Hartogs extends $g$ across zero, and equivariance gives
\[
                        g(\alpha z,\beta w)
                                      =\alpha\beta g(z,w).
\tag{C.CZ.11}\hypertarget{tag-00DP}{}\label{cdp:eq:C.CZ.11}
\]
If there is no positive multiplicative relation between $\alpha$ and $\beta$, the only possible monomial is $zw$. Otherwise a positive central power has multipliers $(\gamma^p,\gamma^q)$ with coprime positive integers $p,q$. Replace $F$ by this power; its primary cover is still finite unramified over $H$. The monomials of $g$ now have weight $p+q$. For $p,q>1$ the only one is $zw$. For $p>1,q=1$, one has $g=w(az+bw^p)$, and reducedness gives $a\ne0$. The coordinate change $z'=z+(b/a)w^p$, $w'=w$ commutes with the contraction and makes the boundary the two axes. The case $p=1,q>1$ uses the exchanged coordinates. For $p=q=1$, the reduced quadratic has two distinct linear factors; the invertible linear change given by those factors commutes with the scalar contraction and again makes the boundary the axes.

Every deck lift preserves their union and commutes with the central diagonal contraction. A lift preserving each axis has the form $(zU(z,w),wV(z,w))$ with $U,V$ holomorphic units. Commutation makes both units invariant under the contraction; iteration to zero makes them constant. A lift interchanging the axes has the form $(wU,zV)$. Comparison of the linear terms forces the two contraction multipliers to agree, and the same iteration makes $U,V$ constant. Thus it is a diagonal map followed by interchange. The logarithmic form $dz/z\wedge dw/w$ spans $H^0(P,K_P(D_P))$: it is nowhere zero, and $H^0(P,\OO_P)=\C$. Diagonal lifts fix it, whereas interchange negates it. The nonzero section pulled back from $K_H(D)$ is invariant, so every deck lift preserves the axes individually. The full group $\Gamma$ is therefore diagonal and the two images are distinct.

Finally a diagonal group containing an infinite cyclic subgroup with finite index is finitely generated abelian, hence $\Gamma=\langle f\rangle\oplus T$ with $T$ finite. Choose the sign of $f$ so that a positive power is a positive power of the contracting central element times an element of $T$; both multipliers of $f$ then have modulus less than one. The finite subgroup $T$ acts freely on $W$, so each of its two coordinate characters is injective. It is consequently cyclic, and
$H=(W/\langle f\rangle)/T$ is the asserted diagonal primary or secondary presentation with the marked axes. The invariant logarithmic form descends through this free quotient.
\end{proof}

'''

collar = r'''\subsection{Canonical-flat central fibres}\label{subsec:II:canonical-flat-fibres}

\begin{lemma}[Smooth normal-product collars]\hypertarget{tag-P326}{}\label{lem:II:normal-product-collars}
\StatementRecord{lem:II:normal-product-collars}{proved}{P326}{}
Let $f:X\to\Delta$ be a proper holomorphic map from a smooth complex threefold whose full central fibre $S$ is reduced and simple normal crossing, with no triple points. For a double curve $C=V_1\cap V_2$, the principal fibre gives an isomorphism
$N_{C/V_1}\otimes N_{C/V_2}\simeq\OO_C$.
A neighbourhood of $C$ is smoothly diffeomorphic over $\Delta$ to a neighbourhood of the zero section in
$N_{C/V_2}\oplus N_{C/V_1}$ with function $(x,y)\mapsto xy$. This map restricts to the identity on $C$ and identifies the two component branches and their normal lines.

These collars can be chosen simultaneously on all double curves. Compact component cores away from them transport to nearby fibres. The two attaching maps on each nearby neck induce the maps of the indicated normal circle bundles, with the reversal $y=t/x$. Hence fundamental-group calculations made with these cores and normal-product necks apply to the given smoothing.
\end{lemma}
\begin{proof}
Near $C$ write $L_i=\OO_X(V_i)$ and let $s_i$ be its canonical divisor section. Since the full fibre is reduced and no other component meets $C$, the function $f$ identifies $L_1\otimes L_2$ with the trivial line and carries $s_1s_2$ to $f$. Along $C$ one has
$L_1|_C=N_{C/V_2}$ and $L_2|_C=N_{C/V_1}$.
Choose a smooth retraction $r$ to $C$ and a smooth identification
$L_1\simeq r^*(L_1|_C)$ equal to the identity on $C$. Use the product trivialization to choose the second identification, so that their tensor product preserves $f$. The map
$\Psi=(r,s_1,s_2)$, with the sections expressed in these identifications, has identity derivative along $TC$. Its two normal derivatives are the transverse divisor differentials, which identify the normal bundle with $L_1|_C\oplus L_2|_C$. Its derivative is therefore invertible along $C$. Compactness and the inverse function theorem give the smooth tubular diffeomorphism after shrinking; by construction $f=xy$ and the branches are $x=0$ and $y=0$.

The finitely many double curves are disjoint, so their neighbourhoods may be chosen disjoint. Give the two normal lines dual Hermitian metrics. On $xy=t$, the projection to $x$ identifies a neck with an annulus bundle in $N_{C/V_2}^{\times}$; projection to $y$ is its dual map $y=t/x$. Radial retraction identifies either end with the corresponding normal circle bundle. This proves the asserted maps on fundamental groups, including normal reversal.

On a compact core in a component, $f$ is a submersion because that component has multiplicity one. Near its boundary the collar coordinates give horizontal lifts of the two real base-coordinate directions that keep the relevant nonzero normal coordinate fixed. Extend these lifts across the compact core with a partition of unity; the right-inverse condition for $df$ is affine and is preserved by this extension. Integrating along the radial segment from $0$ to a sufficiently small $t$ transports the core and agrees with the collar transport at its boundary. The inverse transport gives the inverse diffeomorphism. The attachments therefore use precisely the normal-product maps already described, and van Kampen uses those same homomorphisms for the given nearby fibre.
\end{proof}

'''

hopf=edit(hopf,r'\cref{lem:II:hopf-curves}; \cite[arXiv v1, \S2.3.1, p.~8]{AbashevaDeev2024AB}',r'\cite[arXiv v1, \S2.2.2, p.~4; \S2.3.1, p.~8]{AbashevaDeev2024AB}', 'D18','The P248 printed statement gives ellipticity/disjointness and square zero, but not the nonlinear unique-axis list. The P325 input record now names the exact freshly opened §2.2.2 p.4 and finite-primary-cover §2.3.1 p.8 sources actually used.','lem:II:reduced-anticanonical-hopf')
hopf=edit(hopf,r'by \cref{lem:II:hopf-curves} and its primary curve description',r'by \cite[arXiv v1, \S2.2.2, p.~4]{AbashevaDeev2024AB}', 'D18','Cites the precise nonlinear unique-axis statement rather than applying the narrower printed P248 statement. Section2.2.6 p.5 instead concerns the diagonal curve list and is not the locus of this nonlinear assertion.','lem:II:reduced-anticanonical-hopf')

owner64='cdp:st:C.2.UN.64'
new64=old64
a=next(x for x in old64.splitlines() if x.startswith(r'\StatementRecord'))
b=r'\StatementRecord{cdp:st:C.2.UN.64}{proved}{01EA}{\cref{cdp:st:C.2.UN.17}; \cite[Main Theorem, pp.~483--484]{Nakano1970}; \cite[\S2, Theorem~2\(^{\prime}\), pp.~640--642, and Proposition~9\(^{\prime}\), p.~642]{FujikiNakano1971}; \eqref{cdp:eq:C.PT.13}, \eqref{cdp:eq:C.PR.13}}'
new64=edit(new64,a,b,'D18','Names the existing canonical owner and the exact freshly opened ordinary analytic blowdown loci, including the supplement proving the normal condition alone. The two complete period constructions remain explicit dependencies.',owner64)
new64=edit(new64,'''These assertions classify the stated terminal pairs in actual
degenerations; they make no occurrence assertion for the
anticanonical alternatives.
''','', 'D11','The proper torus degeneration and terminal-pair hypotheses already state the numerical classification domain; the separate compact occurrence assertion remains exactly the two elliptic normal-extension cases.',owner64)
new64=edit(new64,'''The extension class belongs
to the actual one-dimensional space $H^1(B,K_B)$ and is retained,
with its endpoint identifications, by the contraction record.''', '''The extension class belongs to the one-dimensional space $H^1(B,K_B)$; the maps in the displayed exact sequence specify its endpoint identifications.''','D08','States the marked extension as mathematical data of the exact sequence, preserving its class and both endpoint maps.',owner64)
first=old64[old64.index(r'\item \par\medskip\noindent\textbf{The actual canonical'):old64.index(r'\item For a ruling fibre')]
firstnew=r'''\item Apply \cref{cdp:st:C.2.UN.17} to this full fibre, with every multiplicity $m_v=1$. For the smooth component $T$, its normalization and resolution maps are the identity and its intrinsic conductor divisor is zero. The intersection divisors with the other components sum to the single curve $C$ in $P$. The canonical evaluation generator of that proposition has divisor $\sum_v k_vT_v$. Its principal-fibre and adjunction maps, \eqref{cdp:eq:C.CA.3} and \eqref{cdp:eq:C.CA.4}, specialize to
'''+display(old64,'C.EL.6')+r'''
The adjunction map divides the evaluation section by a local equation of $T$ to order $k_T$, so it gives a meromorphic canonical section with the displayed divisor. Multiplication of the evaluation generator by a base power shifts every $k_v$ by the same integer and leaves this formula unchanged. At $C$, the reduced equation $xy=t$ trivializes $N_{C/T}\otimes N_{C/P}$.

'''
new64=edit(new64,first,firstnew,'D12','Uses UN17 on the identical proper-disc family, m_v=1, identity normalization/resolution, intrinsic conductor zero and the sole intersection C. The full EL6 line isomorphisms, canonical divisor and xy=t normal-dual map remain; the rank-one direct-image proof is not repeated.',owner64)
contraction=old64[old64.index(r'\par\medskip\noindent\textbf{The corrected analytic contraction'):old64.index(r'\item In the section case')]
contractionnew=r'''For the contractions, use the analytic blowdown theorem of \cite[Main Theorem, pp.~483--484]{Nakano1970} with the normal-line criterion proved in \cite[\S2, Theorem~2\(^{\prime}\) and proof, pp.~640--642; Proposition~9\(^{\prime}\) and proof, p.~642]{FujikiNakano1971}. A smooth divisor which is a holomorphic projective-space bundle and whose ambient normal line restricts to $\OO(-1)$ on each projective fibre is the exceptional divisor of an ordinary blowup of a smooth analytic centre. The local blowdown maps are the given bundle projections and glue through their isomorphisms off the divisor.

'''
new64=edit(new64,contraction,contractionnew,'D17','The precise known analytic theorem is cited after reading its full stated normal criterion and local ordinary-blowdown construction. The supplement removes the original additional canonical condition; the application retains the exact bundle projection and smooth centre.',owner64)
new64=edit(new64,r'''The contraction retains the matrices \eqref{cdp:eq:C.EL.9}, rather than
discarding this extension class.''',r'''The matrices \eqref{cdp:eq:C.EL.9} describe the normal bundle of the contracted centre with these endpoint frames.''','D02','Replaces the defensive contrast by the concrete bundle map and frames, preserving the extension class.',owner64)
program=old64[old64.index(r'\item The exact degree alternatives'):old64.index(r'\end{enumerate}')]
new64=edit(new64,program,'','D09','The complete degree, Jacobian, extension and Euler calculations are proved in the text. The program root_exceptional_leaves.py is mapped by the separately prepared appendix correction158 to its pinned CDP13 path and exact scope; no execution credit is claimed.',owner64)

oldel8=display(new64,'C.EL.8')
newel8=oldel8.replace(r'\longrightarrow K_C',r'\xrightarrow{\operatorname{res}}K_C')
newel8=newel8.replace(r'\label{cdp:eq:C.EL.8}',r'\label{cdp:eq:C.EL.8}'+'\n'+r'\hypertarget{tag-00DO}{}\SsixEquationAliases{\label{cdp:eq:C.CZ.10}}')
new64=edit(new64,oldel8,newel8,'D20','EL8 and CZ10 are the identical residue exact sequence under T=V and q=pi. The natural arrow is now explicitly named res, and CZ10 keeps its permanent target as a same-counter alias at this sole formula owner.', 'cdp:eq:C.EL.8 / cdp:eq:C.CZ.10')

owner65='cdp:st:C.2.UN.65'
new65=old65
a=next(x for x in old65.splitlines() if x.startswith(r'\StatementRecord'))
b=r'\StatementRecord{cdp:st:C.2.UN.65}{proved}{01EB}{\cref{cdp:st:C.2.UN.17,cdp:st:C.2.UN.5,lem:II:negative-kodaira-models,cdp:st:C.2.UN.19,cdp:st:C.2.UN.64,lem:II:reduced-anticanonical-hopf,lem:II:normal-product-collars,cdp:st:C.2.UN.57}; \cite[Lemmas~2.1--2.2, pp.~959--960]{Kulikov1977}; \cite[Theorem~1\(^{\prime}\), p.~340; Appendix, p.~342]{Kulikov1981}; \cite[Theorem~3.1, author preprint pp.~2--3]{KamenovaTori}}'
new65=edit(new65,a,b,'D18','Uses exact shared owners and the freshly opened English published Kulikov pages and complete Kamenova author-preprint theorem/proof. The later C3.1 classification pointer is replaced by the earlier precise negative-Kodaira owner.',owner65)
a=r'''Shrink the disc to remove every other critical value.
The rank-one canonical direct image has an evaluation
generator $\Omega$ whose divisor is supported on $S$.'''
b=r'''After shrinking the disc, apply \cref{cdp:st:C.2.UN.17} to the same family with every full-fibre multiplicity equal to one. Its evaluation generator $\Omega$ has divisor $\sum_i k_iV_i$.'''
new65=edit(new65,a,b,'D12','The canonical generator and its vertical divisor are supplied once by UN17 on exactly this full reduced fibre. The multiplication/division proof of equal orders iff trivial local K remains here.',owner65)
a='''statement by the displayed multiplication and division maps.
'''
b=r'''statement by these multiplication and division maps. The smooth-total reduced SNC hypotheses are Kulikov's good-degeneration hypotheses, \cite[pp.~957--958]{Kulikov1977}. In \cite[Theorem~1\(^{\prime}\), p.~340]{Kulikov1981}, existence of a good modification with trivial canonical line is characterized by the minimum-order condition on class VII components. Here the equal orders give that trivial line on the given neighbourhood itself through $\Omega/f^k$. The correction to the 1977 Enriques assertion is stated in the later paper's Appendix, p.~342; the principal-divisor and coherent-stratum comparisons used below are the 1977 Lemmas~2.1--2.2.
'''
new65=edit(new65,a,b,'D13','Moves the exact canonical-modification source comparison from the orphan paragraph into the proof of the equal-order/trivial-K equivalence. Its identity map on the given neighbourhood and the published Enriques correction remain explicit.',owner65)
new65=edit(new65,r'\cite[Lemma 2.1]{Kulikov1977}',r'\cite[Lemma~2.1, p.~959]{Kulikov1977}','D18','The primary rendered p.959 formula and its principal-divisor proof were opened; the receiving line-bundle refinement retains its complete local restriction maps.',owner65)
new65=edit(new65,r'\cite[Lemma 2.2]{Kulikov1977}',r'\cite[Lemma~2.2 and proof, pp.~959--960]{Kulikov1977}','D18','The complete coherent-stratum sequence and flat Euler argument were read in the published English layout; the precise SNC maps remain in the proof.',owner65)
new65=edit(new65,r'''These formulas require no K\"ahler assumption.
''','', 'D02','The proper complex-analytic hypotheses and compact-surface Riemann–Roch already state the domain. The explicit Kähler consequence is proved later in the same proof.',owner65)
new65=edit(new65,r'''Thus every component has Kodaira dimension
$-\infty$. The compact-surface classification
in \SeriesRef{cdp:st:C.3.1} makes its minimal model ruled or
of class VII.''',r'''Thus every component has Kodaira dimension $-\infty$. Apply \cref{lem:II:negative-kodaira-models} to its smooth compact minimal model. Its K\"ahler case is rational or a projective-line bundle, and its non-K\"ahler case is of class VII.''','D12','Maps the same compact minimal surface and negative Kodaira dimension to the already proved earlier classification, replacing the later general classification and keeping every alternative.',owner65)
a=old65[old65.index(r'\item A connected bisection'):old65.index(r'\item The two disjoint sections')]
b=r'''\item A connected bisection $C$ would be the entire boundary of $V$. Since the fibre is SNC without triple points, it lies in one other component. Apply \cref{cdp:st:C.2.UN.64} with $(T,C,q,B)=(V,C,\pi,E)$. Its degree-two alternative \eqref{cdp:eq:C.EL.2} forces $E\simeq\PP^1$, contradicting that $E$ is elliptic. Under this identity map, \eqref{cdp:eq:C.EL.8} is the residue sequence of $C\subset V$, and its Serre-dual restriction \eqref{cdp:eq:C.EL.7} is the same finite pullback $H^1(E,\OO_E)\to H^1(C,\OO_C)$ through the Leray isomorphism $\pi^*$. Thus the trace and residue exclusion applies to this very bisection.

'''
new65=edit(new65,a,b,'D12','Removes the second display/proof of the terminal elliptic bisection obstruction. The exact T=V, q=pi, B=E map and both Serre-dual cohomology maps are retained; CZ10 moves as an alias of EL8.',owner65)
a=old65[old65.index(r'\item The two disjoint sections'):old65.index(r'\par\medskip\noindent\textbf{The Hopf boundary')]
b=r'''\item Write the ruling as $V=\PP_E(W)$ with the lines convention. The two disjoint sections give line subbundles $L_0,L_\infty\subset W$. Their sum map $L_0\oplus L_\infty\to W$ is an isomorphism on each fibre, because the two lines are distinct, and hence is a bundle isomorphism. Tensoring it by $L_0^{-1}$ gives
$\PP_E(W)\simeq\PP_E(\OO_E\oplus L)$, where $L=L_\infty\otimes L_0^{-1}$, and sends the two marked sections to the coordinate lines. On the chart with nonzero first coordinate, the ratio of the second coordinate to the first lies in $L$. The remaining marked section is its zero section; removing it gives exactly $L^\times$. Its degree is determined below by the nearby fundamental group.

'''
new65=edit(new65,a,b,'D20','Uses the same lines-projectivization convention as UN64. The two marked sections yield line subbundles; their sum and the explicit tensoring map identify the bundle with O plus L. The ratio chart proves that the complement is this exact L^times, fixing the degree and normal convention used by CZ12.',owner65)
a=old65[old65.index(r'\par\medskip\noindent\textbf{The Hopf boundary'):old65.index(r'\par\medskip\noindent\textbf{The integral obstruction')]
b=r'''\item Let $H$ be a Hopf component and let $D$ be its double-curve boundary. It is nonempty, reduced and a disjoint union of smooth elliptic curves, as proved above; \eqref{cdp:eq:C.CZ.3} is exactly $K_H(D)\simeq\OO_H$. Apply \cref{lem:II:reduced-anticanonical-hopf} to this same pair $(H,D)$. It identifies $H$ with a diagonal primary or secondary quotient and $D$ with its two individually marked axes.

'''
new65=edit(new65,a,b,'D12','P325 is the complete owner of the general reduced-anticanonical Hopf calculation. This receiver explicitly proves nonempty/reduced/disjoint-elliptic and K_H(D)=O on the same H,D before applying it. The central-cover, nonlinear Jacobian, eigenmonomial, coordinate-change and deck-sign arguments are preserved at the owner.',owner65)
log('D25',a,hopf,'The former reference to UN43 occurred inside an all-Hopf boundary argument although UN43 is stated for algebraic dimension zero. P325 proves the general normal-core/central-contraction construction directly before invoking the full primary normal forms. It also proves the nonlinear canonical Jacobian and infinite-order divisor line, and the diagonal-unit/interchange calculation, on exactly its stated domain.','lem:II:reduced-anticanonical-hopf')
a=r'''The canonical
divisor sections and a small smooth
unit root give these product-preserving
tubular maps for the arbitrary
given smoothing, exactly as in
\ref{cdp:st:C.2.UN.46}. Flatness of $L$ is not used
for this topological comparison.'''
b=r'''Apply \cref{lem:II:normal-product-collars} to this reduced SNC fibre, which has no triple points by \eqref{cdp:eq:C.CZ.1}. Its map $\Psi$ uses the two divisor sections and the normal-dual identification along each of these same double curves. It transports the component cores and gives the attaching map $y=t/x$ on their normal circle bundles. For the ruled vertex, the Hermitian metric is on this same degree-$d$ line $L$; the collar construction applies for every integer $d$.'''
new65=edit(new65,a,b,'D25','Replaces the unsupported use of the restricted all-Hopf UN46 statement on degree-d ruled components by the proved general P326. The identical reduced SNC/no-triple family, divisor sections, normal lines, arbitrary-degree Hermitian retraction and attaching maps are named.',owner65)
ref46=(out/(prefix+'_UN46_reference.tex')).read_text()
oldcollar=ref46[ref46.index(r'\item For an arbitrary actual smoothing'):ref46.index(r'\item If the given $Y_t$')]
log('D12',oldcollar,collar,'P326 extracts precisely the smooth normal-product collar construction from the fully read UN46 proof, on its proved general reduced SNC/no-triple domain. The receiving proof retains the derivative, product function, simultaneous collars, horizontal core transport and exact normal-circle maps. The later UN46 bounded application will be prepared in the assigned section10 pass; no distant proof is edited here.','lem:II:normal-product-collars')
rows[-1]['old_location']='UN46 complete proof, arbitrary-smoothing item; exact reference snapshot supplied'
a='''no omitted unblown component
or boundary alternative.'''
b='''all components and their two boundary curves as proved above.'''
new65=edit(new65,a,b,'D02','States positively which marked objects enter the cycle criterion, with their complete classification already proved.',owner65)
a='''The smooth torus case
is its literal product family.
'''
b=r'''The smooth torus case is its product family.

For a K\"ahler total space, restriction of the K\"ahler form makes every component K\"ahler. A Hopf component has $H^2(H,\R)=0$ by \cref{lem:II:hopf-curves} and its bundle-cohomology proof, whereas a K\"ahler form would have positive square integral; exactness and Stokes give a contradiction. Thus the zero-Euler list in this case consists of a torus or a cycle of the elliptic ruled surfaces in \eqref{cdp:eq:C.CZ.2}. Kamenova's necessary list in \cite[Theorem~3.1 and proof, author preprint pp.~2--3]{KamenovaTori}, under the same smooth-total K\"ahler and trivial-canonical hypotheses, also permits elliptic ruled paths. A terminal vertex of such a path would have the connected bisection excluded above by the identical residue and finite-trace maps \eqref{cdp:eq:C.CZ.10} and \eqref{cdp:eq:C.EL.7}. The marked cycles here carry the compact realizations and volume forms just constructed.
'''
new65=edit(new65,a,b,'D13','Moves the substantive Kähler comparison into the complete zero-case proof. The Hopf exclusion uses the same compact surface and Stokes; the path exclusion names the exact terminal bisection/trace/residue map. The complete opened Kamenova theorem is necessary, and the receiving text identifies the additional proved restriction without attributing an occurrence assertion to that source.',owner65)
log('D13',oldlit,new65,'Both orphan paragraphs are incorporated at their mathematical uses in this complete receiving owner: canonical modification in its first proof item, Kähler classification in its last. Exact freshly opened published/preprint locators are given. No mathematical comparison or correction is dropped.',owner65)

# Give separate sequential proof steps to the mathematical blocks formerly divided by mini-headings.
for before,after in [
    ('For a curve contraction, the map is an isomorphism off $T$,',r'\item For a curve contraction, the map is an isomorphism off $T$,'),
    ('Fix the specified elliptic $B$, choose another elliptic curve',r'\item Fix the specified elliptic $B$, choose another elliptic curve')]:
    new64=edit(new64,before,after,'D14','Gives the Euler comparison and compact extension construction their own sequential proof steps, with all maps and calculations unchanged.',owner64)
for before,after in [
    ('Assume $e(S)=0$. Equations',r'\item Assume $e(S)=0$. Equations'),
    (r'Let $\pi:V\to E$ be one of the minimal ruled',r'\item Let $\pi:V\to E$ be one of the minimal ruled'),
    ('Every component now has exactly two',r'\item Every component now has exactly two'),
    ('For every such marked cycle,',r'\item For every such marked cycle,')]:
    new65=edit(new65,before,after,'D14','Separates the zero-case reduction, ruled boundary, integral cycle calculation and compact realization into consecutive mathematical proof steps.',owner65)

# Replace internal mini-headings and process adjectives one exposed paragraph at a time.
clean={}
for name,s,owner in [('hopf',hopf,'lem:II:reduced-anticanonical-hopf'),('collar',collar,'lem:II:normal-product-collars'),('new64',new64,owner64),('new65',new65,owner65)]:
    for m in list(re.finditer(r'\\par\\medskip\\noindent\\textbf\{[^}]+\}\n?',s))[::-1]:
        s=edit(s,m.group(),'', 'D13','The numbered statement and its sequential proof carry this material; removes the unnumbered mini-heading without removing any mathematical step.',owner)
    paras=s.split('\n\n')
    for i,p in enumerate(paras):
        q=p
        q=re.sub(r'\bactual\s+', '', q)
        q=q.replace('same corrected theorem','same analytic theorem')
        q=q.replace('a specified holomorphic', 'a holomorphic')
        q=q.replace('the specified ruling','the ruling').replace('the specified curve identification','this curve identification')
        q=q.replace('the actual one-dimensional','the one-dimensional')
        q=q.replace('For every specified elliptic curve','For every elliptic curve')
        q=q.replace('Fix the specified elliptic', 'Fix the elliptic')
        q=q.replace('recorded point contractions','point contractions').replace('recorded curve centres','curve centres')
        q=q.replace('The record consists of the','The inverse construction uses the')
        q=q.replace('Its exact normal\nbundle and Euler comparisons','Its normal\nbundle and Euler comparisons')
        q=q.replace('etale', r"\'etale").replace('Cech',r'\v{C}ech')
        q=re.sub(r'\b([Aa])n(\s+)(?=(?:proper|holomorphic|smooth|rank|circle|line|compact|finite|integral|meromorphic|literal|nowhere|bundle)\b)',r'\1\2',q)
        q=q.replace('terminates, retaining\nthe punctured torus family','terminates and leaves\nthe punctured torus family unchanged')
        if q!=p:
            log('D08' if any(x in p for x in ['actual','specified','record','corrected']) else 'D23',p,q,'Names the proved map, bundle, centre, quotient or cohomology calculation directly. Every construction and its marked mathematical data remain; articles and accents are adjusted in the receiving paragraph.',owner)
            paras[i]=q
    clean[name]='\n\n'.join(paras)
hopf,collar,new64,new65=(clean[x] for x in ['hopf','collar','new64','new65'])

with (root/'agents/continuation2_B/D19/S6_SERIES_PUBLISH_II_B2_D19_v1_equation_map.tsv').open() as f:
    established={r['old_tag']:r['target_label'] for r in csv.DictReader(f,delimiter='\t') if r['old_tag']}

def literal_refs(s,owner):
    for m in list(re.finditer(r'\((C\.[A-Za-z0-9.]+)\)',s))[::-1]:
        tag=m.group(1); assert tag in established,tag
        a=max(s.rfind('\n\n',0,m.start())+2,0);b=s.find('\n\n',m.end())
        if b<0:b=len(s)
        before=s[a:b];after=before[:m.start()-a]+r'\eqref{'+established[tag]+'}'+before[m.end()-a:]
        s=s[:a]+after+s[b:]
        log('D04',before,after,'Uses the permanent equation reader target from the established D19 mapping. The underlying compact period or primitive-cover construction remains an explicit forward dependency pending root placement.',owner)
    return s
new64=literal_refs(new64,owner64)
new65=literal_refs(new65,owner65)
old_displays={lab:m.group() for m in re.finditer(r'\\\[.*?\\\]',old,re.S) for lab in re.findall(r'\\label\{([^}]+)\}',m.group())}
eq=[]
def number(s,owner):
    def conv(m):
        a=m.group();tags=re.findall(r'\\tag\{([^}]+)\}',a)
        if not tags:return a
        assert len(tags)==1,tags
        lab=re.findall(r'\\label\{([^}]+)\}',a)[0]
        assert established[tags[0]]==lab
        b=a.replace(r'\[',r'\begin{equation}',1);b=b[:-2]+r'\end{equation}'
        b=b.replace(r'\tag{'+tags[0]+'}','')
        log('D19',old_displays[lab],b,'Uses the section equation counter and preserves all permanent targets. EL8/CZ10 have the proved identity T=V and the same residue map; CZ11 moves with its complete Hopf owner.',lab)
        eq.append(dict(old_tag=tags[0],target_label=lab,statement_id=owner));return b
    return re.sub(r'\\\[.*?\\\]',conv,s,flags=re.S)
new64=number(new64,owner64);hopf=number(hopf,'lem:II:reduced-anticanonical-hopf');new65=number(new65,owner65)
eq.append(dict(old_tag='C.CZ.10',target_label='cdp:eq:C.CZ.10',statement_id=owner64))
log('D19',old_displays['cdp:eq:C.CZ.10'],next(m.group() for m in re.finditer(r'\\begin\{equation\}.*?\\end\{equation\}',new64,re.S) if r'\label{cdp:eq:C.CZ.10}' in m.group()),'CZ10 keeps its tag00DO and label as the same-counter alias of EL8 under T=V. The two arrows are the natural residue map, now explicitly named at the sole owner.','cdp:eq:C.CZ.10')
heading=r'\subsection{Terminal ruled contractions}\label{subsec:II:terminal-ruled-contractions}'+'\n\n'
def spacing(s):return re.sub(r'\n{4,}','\n\n\n',s).rstrip()+'\n\n'
new64,hopf,collar,new65=map(spacing,[new64,hopf,collar,new65])
work=heading+new64+hopf+collar+new65
log('D14',old.split('\n\n',1)[0],heading+hopf.split('\n\n',1)[0]+'\n'+collar.split('\n\n',1)[0],'Splits the complete original subsection into its three mathematical units. P325 and P326 precede their UN65 consumers. UN64 remains before the terminal-bisection application. Root owns the later whole contiguous UN64–68 relocation after section10; that ordering remains open.', 'subsec:II:terminal-ruled-contractions')

for kind in ['label','hypertarget']:
    p=r'\\'+kind+r'\{([^}]+)\}'
    before=Counter(re.findall(p,old));after=Counter(re.findall(p,work))
    assert all(after[k]==v for k,v in before.items()),(kind,before-after)
    assert max(after.values())==1,(kind,[k for k,v in after.items() if v>1])
assert Counter(re.findall(r'\\begin\{([^}]+)\}',work))==Counter(re.findall(r'\\end\{([^}]+)\}',work))
assert not re.search(r'\\tag\{|night:P4R\.13|night:P4\.40|\r|\\path\{|\\textbf\{|\(C\.',work)
assert len(old_displays)==25,len(old_displays)
assert len(eq)==25,len(eq)
assert len(re.findall(r'\\begin\{equation\}',work))==24
def payload(s):
    s=re.sub(r'\\SsixEquationAliases\{(?:\\label\{[^}]+\})+\}','',s)
    s=re.sub(r'\\tag\{[^}]+\}|\\label\{[^}]+\}|\\hypertarget\{[^}]+\}\{\}','',s)
    for x in [r'\[',r'\]',r'\begin{equation}',r'\end{equation}']:s=s.replace(x,'')
    return re.sub(r'\s+','',s)
new_displays={lab:m.group() for m in re.finditer(r'\\begin\{equation\}.*?\\end\{equation\}',work,re.S) for lab in re.findall(r'\\label\{([^}]+)\}',m.group())}
for lab,d in old_displays.items():
    if lab not in {'cdp:eq:C.EL.8','cdp:eq:C.CZ.10'}:assert payload(d)==payload(new_displays[lab]),lab

def tsv(suffix,fields,data):
    with (out/(prefix+suffix)).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(data)

(out/(prefix+'_replacement.tex')).write_text(work,newline='\n')
(out/(prefix+'_P325.tex')).write_text(hopf[hopf.index(r'\begin{lemma}'):],newline='\n')
(out/(prefix+'_P326.tex')).write_text(collar[collar.index(r'\begin{lemma}'):],newline='\n')
with (root/'S6_SERIES_PUBLISH_defects_II.tsv').open() as f:fields=next(csv.reader(f,delimiter='\t'))
tsv('_defects.tsv',fields,rows)
tsv('_equations.tsv',['old_tag','target_label','statement_id'],eq)
transfers=[
dict(old_owner='UN64 / UN65 canonical-generator paragraphs',new_owner='UN17 / cdp:st:C.2.UN.17',conclusion='Rank-one canonical evaluation and principal-fibre/adjunction line maps',map='Same proper family; all m_v=1; each smooth component has identity normalization/resolution and intrinsic conductor zero. EL6 takes only E_TP=C. CZ3 uses the same generator divided by f^k and the existing NC6 residue map.'),
dict(old_owner='UN65 connected-bisection display/proof CZ10',new_owner='UN64 EL7/EL8 and CZ10 same-counter alias',conclusion='A terminal anticanonical elliptic bisection has rational ruling base',map='(T,C,q,B)=(V,C,pi,E); identical residue arrow and Serre-dual restriction; finite trace composed with degree-two pullback equals two; tag00DO retained at EL8.'),
dict(old_owner='UN65 full Hopf-boundary classification',new_owner='P325 / lem:II:reduced-anticanonical-hopf',conclusion='Reduced nonempty disjoint elliptic anticanonical boundary is the two individually marked diagonal Hopf axes',map='Central normal-core primary cover W/<F>→H is finite étale; nonlinear Jacobian w^(a+1); diagonal eigenfunction CZ11; weighted triangular/linear coordinate changes; contraction-unit deck lifts; logarithmic-form sign rules out swapping; full diagonal deck quotient.'),
dict(old_owner='UN46 arbitrary-smoothing tubular paragraph; UN65 broad collar consumer',new_owner='P326 / lem:II:normal-product-collars',conclusion='Smooth product-preserving double-curve collars and exact attaching group maps',map='L_i=O(V_i), divisor sections s_i, product f; r and compatible smooth line identifications; Psi=(r,s1,s2), invertible tangent/normal derivative; xy=f; Hermitian annuli and y=t/x; boundary-compatible horizontal core transport. UN65 has reduced SNC and t=0 triple count.'),
dict(old_owner='UN64 compact extension realization',new_owner='UN64 retained, with complete later period inputs',conclusion='Both elliptic normal-extension classes occur over P1 with one singular fibre',map='PT13 on A=B×E with R=1 or2; PR13 primitive cover p,t and gamma; EL11 normal derivative delta′0, tangent gamma′ term removed; Laurent constant obstruction; scalar a rescales exact endpoint-framed class; ordinary blowup ideal(p,t), t=xy.'),
dict(old_owner='UN65 zero-Euler occurrence',new_owner='UN57 exact marked-cycle construction plus retained UN65 volume proof',conclusion='Every marked dual-normal/M=I cycle has compact realization and trivial local canonical line',map='Same components, axes/sections, gluing maps and integral complement product. AD8 moving frames P_i(t), common vector coordinate eta, holomorphic translations; dt wedge kills base derivatives; xy=t gives CZ14; conjugate infinity filling is unchanged.')]
tsv('_owner_transfers.tsv',['old_owner','new_owner','conclusion','map'],transfers)
dependencies=[
dict(consumer='UN64 elliptic normal-extension realization',input='UN61 / PT13',map='Use its smooth compact torus period family on A=B×E, with R=1 or2; no pruning hypothesis enters the period invertibility/completion construction.',status='forward in current source; root-approved whole-block move after section10 pending'),
dict(consumer='UN64 primitive normal derivative',input='UN60 / PR12–PR13',map='Choose the primitive elliptic period basis in the fixed central B; the holomorphic basis change makes first period (0,2pi i) and second (delta(t),log gamma(t)), with delta order R. The normal quotient keeps p,t and discards tangent gamma′w.',status='forward in current source; exact construction read and map retained'),
dict(consumer='UN65 compact marked cycle',input='UN57 complete proof',map='All components are unblown diagonal Hopf or Pic0 elliptic ruled, two marked boundaries, same dual normals and M=I. Apply full local/compact moving-frame construction and verify volume by CZ13–14.',status='forward in current source; full UN57 read; root relocation pending'),
dict(consumer='UN65 arbitrary-smoothing collars',input='P326',map='The same reduced SNC central fibre has no triple points by CZ1; same divisor sections and arbitrary-degree ruled line. Exact x,y normal product and attaching maps.',status='local order completed'),
dict(consumer='UN65 Hopf boundary',input='P325',map='Same H,D; nonempty and reduced by connected reducible SNC support, smooth elliptic disjoint by CZ4 with t=0, K_H(D)=O by CZ3.',status='local order completed')]
tsv('_dependencies.tsv',['consumer','input','map','status'],dependencies)

if not REVIEWED:
    print('12 PREPARED:',len(rows),'defects;25 old equation identities;24 numbered equations;6 owner maps;5 dependency maps. Complete receiving read still required.')
    raise SystemExit

now=datetime.now(timezone.utc)
with (root/'CHECK_EVENTS.tsv').open() as f:event_fields=next(csv.reader(f,delimiter='\t'))
scopes=[
('cdp:st:C.2.UN.64','UN64','subsec:II:terminal-ruled-contractions','Read the complete original and receiving statement/proof. Compared the precise terminal ruled/plane hypotheses, canonical orders, EL1–11 and all numerical alternatives. UN17 specializes with full multiplicities one, identity normalization/resolution and intrinsic conductor zero. Retained the complete ruling-degree and finite trace/residue exclusion, the exact Nakano/Fujiki–Nakano normal criterion and ordinary smooth analytic blowdown, f descent/properness/submersion, Cartier restriction, lines-projectivization and endpoint-framed normal extension, Cech gauge and scalar orbit, plane blowdown, Euler and reverse-neighbourhood comparisons. The compact realization retains PT13/PR13 period maps, delta derivative, Laurent obstruction, exact rescaling by a, infinity frame and ordinary blowup. CZ10 is the identical residue sequence under T=V and is an alias at EL8. Program body path moves only to separately prepared appendix158; no execution.'),
('lem:II:reduced-anticanonical-hopf','P325','subsec:II:anticanonical-hopf-boundaries','Read the complete original UN65 boundary proof and the entire receiving lemma. Also read complete UN43 and P248 and the bounded UN59 contraction-unit argument. Compared the general Hopf domain, reduced nonempty disjoint smooth elliptic divisor and K_H(D)=O. The normal-core/central-contraction cover is proved before algebraic-dimension considerations; fresh Khaled v2 full normal-form list, Theorem2.1 and Remark2.2 supply the primary forms. The nonlinear determinant and anticanonical axis multiplicity, infinite-order effective line, complete eigenmonomial alternatives, explicit commuting triangular/linear maps, axis-preserving units, swapping multiplier comparison, logarithmic-form sign and diagonal finite quotient are proved. The receiving UN65 H,D satisfy every lemma hypothesis explicitly.'),
('lem:II:normal-product-collars','P326','subsec:II:canonical-flat-fibres','Read the complete original UN46 proof, its arbitrary-smoothing paragraph, and the full receiving P326 statement/proof. Compared the reduced full SNC fibre with no triple points, actual divisor lines and sections, product f, smooth retraction and compatible line identifications, invertible tangent/normal derivative, compact tubular shrinking, simultaneous disjoint collars, Hermitian annuli and y=t/x reversal. Boundary-matching horizontal lifts on compact cores are extended by the affine right-inverse condition and integrated over small radial base segments. The exact attaching group maps follow. This is a smooth comparison; the receiving statement asserts exactly that scope. UN65 applies it to the same zero-triple fibre and arbitrary-degree ruled lines. No distant UN46 edit or independent proof credit is claimed.'),
('cdp:st:C.2.UN.65','UN65','subsec:II:canonical-flat-fibres','Read the complete original and receiving statement/proof, including both original orphan literature paragraphs. Preserved equal-order iff local trivial canonical line through Omega/f^k, all CZ formulas/targets, residue sign trivializations, triple-point normal maps, K²/coherent/Euler counts and parity, all zero-case surface alternatives and minimality, exact terminal-bisection alias map, split ruled bundle, P325 Hopf application, degree-d circle-bundle presentation with injected infinite meridian, P326 collar and graph-of-groups injections, degree zero and M=I. The complete marked-cycle realization uses the same UN57 data; its full proof was read, and the common moving-frame volume extends by dt wedge dx/x wedge dz=dy wedge dx wedge dz. Both primary literature comparisons move into their mathematical proof loci, with full exact-source readings recorded. Forward compact-construction placement remains explicit and open.')]
events=[]
for lab,short,unit,scope in scopes:
    e={k:'' for k in event_fields};e.update(statement_id=lab,date=now.date().isoformat(),date_utc=now.isoformat(),who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 conductor agent',type='used and rechecked in this run',outcome=scope+' Exposed editorial rereading only. All25 old equation identities and all original permanent labels/targets remain;23 payloads are unchanged, EL8 names its residue arrow and CZ10 is its proved identity alias. No refined night:P4R.13 or night:P4.40 use occurs. Final whole-paper placement and integrated PDF reading remain open.',event_id='publish:c3:conductor12:'+short,phase='publication editorial comparison',source_file='agents/continuation3_conductor/'+prefix+'_replacement.tex',source_event_type='used and rechecked in this run',evidence_group='publish:c3:conductor12:ruled-canonical-flat',where=unit);events.append(e)
tsv('_CHECK_EVENTS.tsv',event_fields,events)
units=[('subsec:II:terminal-ruled-contractions','Terminal ruled contractions','UN64'),('subsec:II:anticanonical-hopf-boundaries','Reduced anticanonical boundaries on Hopf surfaces','P325'),('subsec:II:canonical-flat-fibres','Canonical-flat central fibres','P326 / UN65')]
status=[]
for unit,title,scope in units:
    for n in range(1,26):
        state='done';reason='Complete original and receiving '+scope+' statements/proofs compared; each local instance found is recorded with exact maps. This row concerns this actual subsection only.'
        if n in [10,16]:reason='Prior done status preserved: hidden records and all permanent labels/tags remain, and every numbered statement has a mathematical title.'
        if n==12:
            reason='The canonical generator and terminal bisection have one earlier proved owner with exact applications; complete specialized extension constructions remain.'
            if scope=='P325':state='open';reason='The complete reduced-boundary proof has one local owner and an exact UN65 application. Its general central-primary-cover paragraph also occurs in UN43; root owns a separate earlier general owner and the two exact receiving applications. This known D12 transfer stays open until that integration.'
            if scope=='P326 / UN65':state='open';reason='UN65 applies the exact proved P325/P326 owners. P326 extracts the general smooth collar argument; its later UN46/UN57 receiving applications belong to the assigned section10 pass and remain open. The P325 general central-cover transfer to root’s earlier owner also remains open.'
        if n==14:state='open';reason='Local owner order is complete. PT13/PR13 and UN57 remain forward compact-construction inputs; root owns the approved contiguous UN64–68 relocation after section10. Exact dependency maps supplied.'
        if n==17:reason='The analytic normal-line blowdown theorem and all cited primary loci were freshly opened. Full new-domain Hopf, collar, line/residue, extension and compact-volume arguments remain proved.'
        if n==18:state='open';reason='Edited exact primary locators and source versions are recorded. Bibliography-wide review remains separate; the two program additions are owned by appendix correction158.'
        if n==19:reason='25 inherited equation identities use the section counter; EL8/CZ10 have one residue owner and both permanent targets with the explicit T=V map.'
        if n==23:state='open';reason='Source articles and accents corrected; final integrated page reading remains open.'
        if n==24:reason='No unmatched front-matter promise is introduced in this bounded body unit. Final organization text is root-owned after the whole-block move.'
        if n==25:reason='Every original and receiving inference was compared, including the broad Hopf cover and arbitrary-degree ruled collar scope repairs. Full statements and constructive conclusions remain unconditional on their stated hypotheses.'
        status.append(dict(unit=unit,title=title,criterion=f'D{n:02d}',status=state,reason=reason))
    status.append(dict(unit=unit,title=title,criterion='structure',status='open',reason='Local unit separation and one-owner proof order complete; approved whole-block relocation after section10 and final paper proportion remain pending.'))
tsv('_unit_status.tsv',['unit','title','criterion','status','reason'],status)
sources=[]
def source(key,url,version,locus,sha,size,content,file):
    sources.append(dict(source_id=key+':conductor12',url=url,version=version,exact_locus=locus,sha256=sha,bytes=str(size),own_paraphrase=content,reader='continuation3 conductor; exact stated locus freshly opened and read; no independent proof/execution credit',date_utc=now.isoformat(),storage='/tmp/S6_SERIES_PUBLISH_c3_conductor_primary/'+file+'; outside checkpoint.'))
source('Nakano1970','https://ems.press/content/serial-article-files/41677','Published PRIMS6(3),1970/71,483–502','Introduction and complete Main Theorem pp.483–484','ec60be2235c29e43943641ec03472867c457206170a1b2e5a0485802d03fc37a',1840349,'The ordinary analytic blowdown theorem includes the normal O(-1) condition and an additional canonical condition. The receiving text explicitly uses the later supplement for the normal condition alone.','Nakano1970.pdf')
source('FujikiNakano1971','https://ems.press/content/serial-article-files/41704','Published PRIMS7(3),1971/72,637–644','Introduction p.637; complete §2 Theorem2′ and proof pp.640–642; Proposition9′ and proof p.642; complete §3 pp.643–644','2c2d2f6c8445f26437cdf64398745215b6448debc86f72829a7159fec8e6b72c',637148,'The normal O(-1) condition alone yields the smooth ordinary blowdown; Proposition9′ identifies the local map with the projective-bundle projection and smooth centre. Section1 was not completely read and no full-source proof claim is made.','FujikiNakano1971.pdf')
source('Khaled2024Hopf','https://arxiv.org/pdf/2310.05265v2','arXiv2310.05265v2,4December2023','Complete normal-form list(1),p.3; complete Theorem2.1 and Remark2.2,p.5; intervening p.4 read','7ec7b5917163b8d11ca97866b76a67aa81d3db5e3b1876b3abf9d4cbdb210383',377475,'The primary normal forms include scalar, resonant diagonal, nonlinear exponents a≥2, nonlinear Jordan a=1 and nonresonant diagonal. The complete centralizer table and equal-modulus correction are stated there. The paper recalls the classification theorem; no primary classification-proof reading is claimed.','Khaled2024_v2.pdf')
source('AbashevaDeev2024AB','https://arxiv.org/pdf/2303.10764v1','arXiv2303.10764v1,19March2023','Title/versionp.1; complete §2.3.1p.8; §2.2.1–2.2.9pp.4–5; §2.4.1p.8','506d60ef501997ba8e773dd1610a4d2c721dff120e6c5009d55a0e52245a410d',265648,'The exact used §2.3.1 statement gives a free finite quotient of a primary Hopf surface for every secondary Hopf surface. Its covering injection gives the finite-index cyclic contraction subgroup. Section2.2.2 identifies the unique nonlinear axis; the full automorphism and resonant normal-form input is taken from Khaled Theorem2.1, not the general automorphism sentence in §2.2.5. Section2.4.1 confirms the explicit v↦[1:v] lines-projectivization chart.','AbashevaDeev2023_v1.pdf')
source('Kulikov1977','https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=1877&what=fullteng','Published English MathUSSR-Izv11(5),1977,957–989','Complete introduction/good-degeneration definition pp.957–958; Lemmas2.1–2.2 and complete proofs pp.959–960; rendered p.959 formulas inspected','9e96a503588dbcd732bfaf7246c3e1de616db2c039b8be512541669a90af81cd',1737695,'Principal-fibre restriction gives the sum of the two normal degrees minus the triple count; the coherent strata sequence gives the Euler relation. UN65 retains the stronger explicit line maps and its residue/Euler application. The published translator correction was read; no complete main classification-proof claim.','Kulikov1977_eng.pdf')
source('Kulikov1981','https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=1953&what=fullteng','Published English MathUSSR-Izv17(2),1981,339–342','All four published pages339–342, including Theorem1′p.340, its full argument and Appendixp.342','c1264d449a39c81ae86e1ad5dcb2fd675c525b616bf2268344f8285f91b1a8b2',280655,'The minimum canonical-order condition on classVII components characterizes good modifications with trivial canonical line. UN65 equal orders give that line directly via Omega/f^k. The Appendix corrects the 1977 Enriques modification assertion.','Kulikov1981_eng.pdf')
source('KamenovaTori','https://www.math.stonybrook.edu/~kamenova/homepage_files/degen.pdf','Undated four-page author preprint','All four pages; full Theorem3.1 and proof pp.2–3, with proper Kähler setup p.1','8cd2ddcef5c77b97f6d1b648a73191734696dceb1c9281c09342413596cfbd0b',90441,'The necessary smooth-total Kähler/trivial-K torus-degeneration list includes elliptic ruled paths/cycles and a rational dual-torus case. The receiving zero-case proof names the exact trace/residue obstruction to its terminal bisection and proves the Hopf exclusion by Stokes.','KamenovaTori.pdf')
tsv('_sources.tsv',['source_id','url','version','exact_locus','sha256','bytes','own_paraphrase','reader','date_utc','storage'],sources)
print('12 READY:',len(rows),'defects;4 exposed events;25 old equation identities;24 numbered equations;6 owner maps;5 dependency maps;78 unit-status rows;7 source rows.')
print('New tags P325/P326. No central writes; complete original guard; all old labels/targets preserved; LF. Whole-block placement and final rendering remain open.')
