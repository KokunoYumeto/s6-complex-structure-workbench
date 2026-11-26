#!/usr/bin/env python3
"""Prepare complete component-cover and translation-field units; no central edits."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv,re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation3_conductor'
PRE='S6_SERIES_PUBLISH_c3_conductor_06'
source=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
rows=[]

def span(ident):
    p=source.index(r'\StatementRecord{'+ident+'}')
    a=list(re.finditer(r'^\\begin\{(?:proposition|lemma|theorem|corollary|example|remark|cited|definition)\}',source[:p],re.M))[-1].start()
    b=source.index(r'\end{proof}',p)+len(r'\end{proof}')
    return a,b
def block(ident):
    a,b=span(ident);return source[a:b]
def log(kind,owner,old,new,reason,newloc=None):
    p=source.find(old);line=source[:p].count('\n')+1 if p>=0 else ''
    rows.append(dict(change_id=f'II-C3-UNRESTRICTED06-{len(rows)+1:04d}',type=kind,statement_id=owner,
        old_location=f'pre-admission source line {line}; {owner}',old_page='cp35 PDF omitted; exact source span supplied',
        new_location=newloc or owner,new_page='pending integrated final PDF',old_text=old,new_text=new,reason=reason,
        review_status='Complete original and receiving proof read and compared; exposed editorial rereading; integrated PDF reading remains open.'))
def replace(text,old,new,kind,owner,reason):
    assert text.count(old)==1,(owner,old[:100],text.count(old))
    text=text.replace(old,new,1);log(kind,owner,old,new,reason);return text
def item(text,start,end):
    a=text.index(start);b=text.index(end,a);return text[a:b]

u15=block('cdp:st:C.2.UN.15');u16=block('cdp:st:C.2.UN.16')
u17=block('cdp:st:C.2.UN.17');u19=block('cdp:st:C.2.UN.19')
u20=block('cdp:st:C.2.UN.20')
heading_old=r'\subsection{Translation fields and component surfaces}\label{subsec:II:component-field-inputs}'
start=source.index(heading_old)
stop=source.index(r'\begin{proposition}[A component cover with a rank-two translation frame has coherent Euler characteristic zero]',start)
original=source[start:stop]
_,end17=span('cdp:st:C.2.UN.17');start19,_=span('cdp:st:C.2.UN.19')
orphan17=source[end17:start19].strip()

# The cyclic root equations, stabilizer quotient and minimal-model maps are
# prerequisites of both field ranks, not consequences of the class VII case.
cover=r'''\begin{lemma}[Cyclic covers of a fibre component]\hypertarget{tag-P240}{}\label{lem:II:cyclic-component-cover}
\StatementRecord{lem:II:cyclic-component-cover}{proved}{P240}{\cite[\S1, Universal and canonical desingularization, arXiv v2 p.~11]{BierstoneMilman1997}}
Let $f:U\to\Delta_t$ be a proper holomorphic map from a smooth complex threefold, with connected fibres and smooth complex two-tori over $\Delta_t^*$. Write $f^{-1}(0)=\sum_jm_jS_j$ and fix $S_i$. Normalize the fibre product for $t=s^{m_i}$. It has a resolution
$f':U'\to\Delta_s$ of its total space and central support, isomorphic over $\Delta_s^*$ and at the generic points above $S_i$. Every smooth strict component $E$ above $S_i$ has multiplicity one, and its proper generically finite map to $S_i$ factors through $S_i^\nu$. Its meromorphic function field is algebraic over the pullback of $\mathcal M(S_i^\nu)$, so $a(E)=a(S_i^\nu)$.

The resolution can be chosen equivariant for $\mu_{m_i}$. For such a choice, let $G\subset\mu_{m_i}$ be the stabilizer of $E$. The generic degree of $E\to S_i^\nu$ is $|G|$, and the induced map \eqref{cdp:eq:C.HQ.2} is proper and bimeromorphic. When $E$ has a nonruled minimal model $E_0$, its contraction $\rho:E\to E_0$ is equivariant and induces the proper bimeromorphic map \eqref{cdp:eq:C.HQ.3}. Resolving the graph of these two quotient maps compares a smooth resolution of $S_i^\nu$ with a resolution of $E_0/G$.
\end{lemma}
\begin{proof}
At a generic smooth point of $S_i$ away from the other components, write $t=uz^{m_i}$ with $u$ a holomorphic unit. The normalized root cover is given by
\[
 w^{m_i}=u,\qquad z=s/w.
 \tag{C.SC.2}\hypertarget{tag-010M}{}\label{cdp:eq:C.SC.2}
 \hypertarget{tag-00MQ}{}\SsixEquationAliases{\label{cdp:eq:C.HQ.1}}
\]
The map to $U$ keeps the other coordinates and sends $(s,w)$ to $z=s/w$; its deck action sends $(s,w)$ to $(\zeta s,\zeta w)$. Since $w$ is a unit and the root equation is \'{e}tale, the total space is smooth here and $s$ has order one on every component above $S_i$.

Resolve the normalized total space and then the central support, preserving the punctured tube and these generic smooth points. The canonical analytic resolution in \cite[\S1, Universal and canonical desingularization, arXiv v2 p.~11]{BierstoneMilman1997} lifts local isomorphisms through its successive blowups. Apply it to the space and then to the central divisor: the finite deck action preserves each centre and lifts to the resulting pair. Properness over the disc makes the central fibre compact; after shrinking the disc finitely many steps suffice. The nearby fibres are the original connected tori. In the Stein factorization of $f'$, the finite map to the normal disc has generic degree one and is therefore an isomorphism. Thus its full fibres are connected.

The strict component $E$ is compact and smooth. The universal property of normalization gives $E\to S_i^\nu\to S_i$. Its Stein factorization $E\to T'\to S_i^\nu$ has a birational first map and a finite second map. For a meromorphic function on $T'$, take the elementary symmetric functions of its values over the finite \'{e}tale locus. Near a point of the normal base, multiplication by a sufficiently high power of a local equation containing the finite image of its polar divisor makes that function holomorphic upstairs. The symmetric functions of this multiple are locally bounded, by finiteness, and extend holomorphically across the branch set by normality. Dividing the $k$th coefficient by the $k$th power of that base multiplier gives a meromorphic extension of the original coefficient. These global coefficients give a monic equation over $\mathcal M(S_i^\nu)$. Birational pullback identifies $\mathcal M(T')$ with $\mathcal M(E)$, proving the function-field and algebraic-dimension assertions.

For the equivariant choice, the reduced inverse image over the connected dense smooth open subset of $S_i$ in \eqref{cdp:eq:C.SC.2} is a $\mu_{m_i}$-torsor. The group permutes its connected components transitively, and the stabilizer of the component contained in $E$ acts freely and transitively on each of its fibres. Thus its degree is $|G|$. Taking the finite quotient and using the proper factorization through normalization gives
\[
 E/G\longrightarrow S_i^\nu,
 \tag{C.HQ.2}\hypertarget{tag-00MS}{}\label{cdp:eq:C.HQ.2}
\]
a degree-one proper map between irreducible normal surfaces, hence a bimeromorphic map. This uses the stabilizer of the selected component even when the root cover over $S_i$ is disconnected.

For a nonruled minimal model $E_0$, each $g\in G$ induces a bimeromorphic automorphism $g_0$ of $E_0$, which is holomorphic by uniqueness of the minimal model. The equality $\rho g=g_0\rho$ on the common open isomorphism extends everywhere. The contraction therefore descends to
\[
 E/G\longrightarrow E_0/G.
 \tag{C.HQ.3}\hypertarget{tag-00MT}{}\label{cdp:eq:C.HQ.3}
\]
It is proper and bimeromorphic since the contraction is so on the invariant open set. Passing to the effective quotient of the action on $E_0$ preserves the quotient space. The two proper quotient maps give the asserted graph comparison.
\end{proof}
'''
cover_old=item(u15,r'\item We first make the chosen component reduced',r'\item If $Z_i$ were')+item(u16,r'\item Write $f',r'\item Put $\mathcal O')+item(u19,r'\item We first identify the quotient',r'\item Write $Z_i$')
log('D12','lem:II:cyclic-component-cover',cover_old,cover,
    'The repeated root normalization, multiplicity-one, connectedness and stabilizer quotient are one prerequisite. The maps (s,w) to z=s/w and (s,w) to (zeta s,zeta w) identify the same covering and its exact quotient. Every resolution allowed in the original field construction is covered; equivariance is an available choice, not a new restriction on that construction.')
log('D12','lem:II:cyclic-component-cover',item(u16,r'\item Finally suppose $a(S_i^\nu)=0$',r'\item Apply the compact-surface'),cover,
    'The finite Stein-factor function-field proof is transferred in its exact generality. Its algebraic-dimension-zero specialization remains C.CF.9 in UN.16.')
log('D12','lem:II:cyclic-component-cover',item(u19,r'\item Every element of $G$',r'\item We exclude the torus'),cover,
    'The equivariant nonruled minimal contraction and its proper quotient graph are transferred intact and precede both rank branches. C.HQ.2 and C.HQ.3 keep their original statement and equation identities.')
log('D18','lem:II:cyclic-component-cover',r'\cite[\S1, universal and canonical desingularization]{BierstoneMilman1997}',r'\cite[\S1, Universal and canonical desingularization, arXiv v2 p.~11]{BierstoneMilman1997}',
    'Freshly opened the cited analytic, noncompact canonical-resolution paragraph in arXiv alg-geom/9508005v2, printed p.11; the finite group acts by the local isomorphisms that the source lifts.')

definition=r'''\begin{definition}[Semicomplete meromorphic vector fields]\hypertarget{tag-P238}{}\label{def:II:semicomplete-fields}
\StatementRecord{def:II:semicomplete-fields}{proved}{P238}{\cite[Definition~2.3, author preprint p.~7]{Guillot2024}; \cite[Definition~5, arXiv v2 p.~4]{Guillot2019}}
For a meromorphic vector field $V$ on a complex manifold $X$, let $X_V$ be its holomorphic locus. A solution $\phi:\Omega\to X_V$, with $\Omega\subset\C$ connected and open, is \emph{univalent maximal} when its graph map $t\mapsto(t,\phi(t))$ to $\C\times X_V$ is proper. The field is \emph{semicomplete} when every initial point in $X_V$ has such a solution. Equivalently, analytic continuations of a solution germ along two complex-time paths with the same endpoint agree wherever both are defined. We use this equivalence in the sense of \cite[Propositions~2.1--2.2, author preprint pp.~4--7]{Guillot2024}.
\end{definition}
'''
closed_old=item(u15,r'\item We use the precise closed-univalence theorem',r'\item Let $P$ be the polar')
log('D13','def:II:semicomplete-fields',closed_old,definition,
    'The univalent-maximal and semicomplete notions used by the component theorems receive one earlier numbered definition. The proper graph map gives the precise analytic meaning of single-valued maximality.')

transport=r'''\begin{lemma}[Restriction and specialization of semicomplete fields]\hypertarget{tag-P239}{}\label{lem:II:semicomplete-transport}
\StatementRecord{lem:II:semicomplete-transport}{proved}{P239}{\cref{def:II:semicomplete-fields}; \cite[Theorem~3.3, author preprint p.~9]{Guillot2024}; \cite[Lemma~6, arXiv v2 pp.~4--5]{Guillot2019}}
Semicompleteness is preserved by restriction to an open set and by transport through a bimeromorphic map between smooth manifolds, on the full holomorphic locus of the transported meromorphic field.

Let $f':U'\to\Delta_s$ be a proper holomorphic map from a smooth complex threefold with smooth compact two-torus fibres over $\Delta_s^*$. Let $v$ be a meromorphic vertical field, holomorphic over $\Delta_s^*$, and let $E$ be a smooth central component at whose generic point $v$ is holomorphic. Then $v$ is semicomplete on its holomorphic locus, and its meromorphic restriction $v_E$ is tangent to $E$ and semicomplete on its holomorphic locus.

A nonzero semicomplete meromorphic field on a smooth compact curve is holomorphic, and that curve has genus at most one.
\end{lemma}
\begin{proof}
Restriction preserves single-valued analytic continuation, or equivalently the fourth condition in \cite[Proposition~2.2 and the paragraph following Definition~2.3, author preprint pp.~6--7]{Guillot2024}. The uniformizability locus of a holomorphic field on any complex manifold is closed by \cite[Theorem~3.3, author preprint p.~9]{Guillot2024}. A field transported by a bimeromorphic map agrees with the old one under the biholomorphism of their dense common open sets. Apply restriction there, and then this closedness theorem on the full holomorphic locus of the transported field.

On every punctured fibre of $f'$, the field $v$ is a holomorphic translation field on a compact torus. In its presentation $\C^2/\Lambda$, the flow is $[z]\mapsto[z+\tau a]$ for the corresponding constant vector $a$, and is defined for every $\tau\in\C$. The union of these fibres is dense in the holomorphic locus $W$ of $v$. Closedness therefore makes $v|_W$ semicomplete.

The identity $v(s)=0$ preserves each component ideal of the central divisor wherever $v$ is holomorphic. Indeed, write $s=u\prod_jh_j^{n_j}$ in a smooth local ring. After dividing $v(s)=0$ by $h_j^{n_j-1}$ and reducing modulo $h_j$, the remaining nonzero factors give $v(h_j)=0\bmod h_j$. Thus $E\cap W$ is invariant, and its solutions inherit single-valued continuation under the inclusion into $W$. Its meromorphic field $v_E$ may extend holomorphically across further curves in $E$. Closedness on the holomorphic locus of $v_E$, applied to the dense open subset $E\cap W$, supplies the stated extension.

For a compact curve $C$ and a nonzero field $V$, apply \cite[Lemma~6, arXiv v2 pp.~4--5]{Guillot2019} to $V$ and a univalent maximal solution on $C_V$. The lemma proves that $V$ has no poles. Its nonzero holomorphic section of $T_C$ has an effective zero divisor of degree $\deg T_C=2-2g(C)$, proving $g(C)\le1$.
\end{proof}
'''
transport_old=item(u15,r'\item Let $P$ be the polar',r'\item We finish by proving')+item(u16,r'\item For completeness, semicompleteness',r'\item Take a complex basis')
log('D12','lem:II:semicomplete-transport',transport_old,transport,
    'The two ambient-to-component closedness arguments are one owner, with the factorization showing invariance of each component ideal and the second extension across removable restricted poles. The same birational-open restriction already used in UN.15/16 is included once.')
log('D17','lem:II:semicomplete-transport',closed_old,transport,
    'The known zero-time-path proof of closedness is replaced by Guillot Theorem 3.3 at its freshly opened complete proof, author-preprint p.9. The receiving proof supplies the ambient and restricted holomorphic loci to which that theorem is applied.')
curve_old=item(u15,r'\item Such a field on a compact curve',r'\item This also contradicts')+item(u16,r'\item A nonzero semicomplete meromorphic field on a smooth',r'\item Finally suppose')
log('D17','lem:II:semicomplete-transport',curve_old,transport,
    'Guillot2019 Lemma 6, arXiv v2 pp.4–5, was opened with its complete proof and states the exact no-poles assertion for a meromorphic curve field with a univalent maximal solution. The repeated inverse-time-form proof is removed; the compact tangent-line degree giving the genus bound remains.')

zero_surface=r'''\begin{lemma}[Two semicomplete fields in algebraic dimension zero]\hypertarget{tag-P301}{}\label{lem:II:zero-dimensional-field-surface}
\StatementRecord{lem:II:zero-dimensional-field-surface}{proved}{P301}{\cref{lem:II:semicomplete-transport}; \cite[Theorem~9.2, author preprint p.~28]{Guillot2024}; \cite[Theorem~0.3, pp.~641--642]{DOT2001}; \cite[p.~260]{DOT2000}; \cite[Proposition~2(ii), pp.~274--275; Proposition~3(ii), p.~277; Proposition~5, p.~280]{Inoue1974}}
Let $X$ be a smooth compact complex surface with $a(X)=0$ and a two-dimensional complex space of commuting meromorphic fields every member of which is semicomplete. Its minimal model is a complex two-torus or a Hopf surface.
\end{lemma}
\begin{proof}
Choose a complex basis $V_1,V_2$. Apply \cite[Theorem~9.2, author preprint p.~28]{Guillot2024} to each field. Its fibration alternative would give a nonconstant meromorphic function by pullback from its compact base curve. Since $a(X)=0$, each field instead becomes holomorphic on a smooth bimeromorphic model. Such a surface is nonruled: a ruling would again pull back a nonconstant function from its base, and a rational surface has algebraic dimension two. Its nonruled minimal model $X_0$ is unique, and each smooth bimeromorphic model maps to it by point blowdowns.

For such a blowdown $\pi$, the equality $\pi_*\OO=\OO$ descends the derivation $g\mapsto V(\pi^*g)$ to a holomorphic vector field on the base. On the common open isomorphism this is the original meromorphic field. Thus $V_1,V_2$ give two complex-linearly independent commuting holomorphic fields on the same $X_0$.

Apply the complete minimal-surface list in \cite[Theorem~0.3, pp.~641--642]{DOT2001}. Its ruled and elliptically fibred entries have nonconstant meromorphic functions by their indicated projections. The entries remaining in algebraic dimension zero are tori, Hopf surfaces, Inoue surfaces, and minimal class VII surfaces with positive second Betti number. The last have at most one holomorphic field by \cite[p.~260]{DOT2000}. For Inoue's three families the dimensions are respectively $0,1,0$, by \cite[Proposition~2(ii), pp.~274--275; Proposition~3(ii), p.~277; Proposition~5, p.~280]{Inoue1974}. The two independent descended fields therefore leave precisely the torus and Hopf entries.
\end{proof}
'''
zero_old=item(u16,r'\item Apply the compact-surface',r'\end{enumerate}')
log('D12','lem:II:zero-dimensional-field-surface',zero_old,zero_surface,
    'The original algebraic-dimension-zero argument uses only the stated two-dimensional semicomplete space. It is made a separate owner in that same scope, before both UN.16 and UN.22; the derivation descent and exact classification entries are preserved.')
log('D18','lem:II:zero-dimensional-field-surface',zero_old,zero_surface,
    'Freshly read Guillot9.2 author p.28, DOT2001 Theorem0.3 pp.641–642, DOT2000 p.260, and Inoue2(ii)/3(ii)/5 at printed pp.274–275/277/280. Exact published/author-version page locators replace the unpaginated citations; no full independent source-proof credit is claimed.')

algebraic=r'''\begin{lemma}[The fibration defined by algebraic solution leaves]\hypertarget{tag-P302}{}\label{lem:II:algebraic-leaf-fibration}
\StatementRecord{lem:II:algebraic-leaf-fibration}{proved}{P302}{\cref{lem:II:semicomplete-transport}}
Let $E$ be a smooth projective surface with a nonzero semicomplete meromorphic field $w_E$ whose regular solution leaves have algebraic closures. There are a proper birational morphism $\rho:E'\to E$ and a proper map
\[
 q:E'\longrightarrow C
 \tag{C.SC.6}\hypertarget{tag-010Q}{}\label{cdp:eq:C.SC.6}
\]
to a smooth compact curve with connected fibres, such that the lifted field is tangent to $q$ and its general fibre is rational or elliptic. In particular $\kappa(E)\le1$.
\end{lemma}
\begin{proof}
The irreducible algebraic closures of the regular leaves are invariant curves covering the regular foliation locus. Use the countably many Hilbert polynomials and flattening strata of their universal families to parametrize reduced irreducible curves. After clearing the polar divisor $P$ of $w_E$, tangency is the vanishing of the induced relative conormal map
\[
 \mathcal I/\mathcal I^2\longrightarrow\OO_{\mathcal C}(P),
 \qquad h\longmapsto w_E(h)\bmod\mathcal I
\]
on the universal curve $\mathcal C\subset E\times T$. Coherent presentations and flattening stratification make its fibrewise vanishing constructible. Thus the integral invariant curves have countably many irreducible locally closed parameter strata with constructible incidence images in $E$.

Some incidence image is dense. Otherwise their Zariski closures would be countably many proper closed analytic subsets covering the regular foliation locus, contrary to the Baire theorem. In a stratum with dominant incidence, exactly one generic curve passes through a regular point: two invariant irreducible curves through it contain the same local solution germ and coincide. The parameter stratum therefore has dimension one and its incidence map to $E$ is generically one-to-one. Compactify and normalize this parameter curve and close the incidence graph. Its birational projection to $E$, inverted and followed by projection to the parameter, gives a meromorphic first integral. Resolving its graph and taking the Stein factor gives \eqref{cdp:eq:C.SC.6}.

The meromorphic lift of $w_E$ is tangent to $q$, is nonzero on a general smooth fibre $G$, and is semicomplete on its holomorphic locus by \cref{lem:II:semicomplete-transport}. Restriction to the invariant fibre and the curve clause of that lemma give $g(G)\le1$.

Since $G$ is a smooth fibre, its normal line is trivial and adjunction gives $K_{E'}|_G=K_G$. A negative-degree line on a compact curve has no sections, and a degree-zero line has at most one independent section. Each pluricanonical map therefore contracts the general fibres of $q$. It cannot be generically finite, so $\kappa(E')\le1$; the proper birational map $\rho$ gives $\kappa(E)=\kappa(E')$.
\end{proof}
'''
algebraic_old=item(u15,r'\item Here is the other case',r'\item Such a field')+item(u15,r'\item This also contradicts',r'\item Both cases')
log('D12','lem:II:algebraic-leaf-fibration',algebraic_old,algebraic,
    'The complete projective incidence, graph and Stein-factor argument is one explicit construction before its UN.15 and UN.22 uses. The relative conormal morphism spells out the original normal-component map; the unique invariant curve through a regular point proves the dimension and degree assertions. The original adjunction/pluricanonical conclusion is retained.')

# The two-dimensional saturation now owns the relative tangent module and
# supplies the one-field application, in the direction required by the proofs.
u16_new=u16
old_intro=r'''Fix an irreducible central component $S_i$
of multiplicity $m_i$. Make the actual base change $t=s^{m_i}$,
normalize, and resolve as in \ref{cdp:st:C.2.UN.15}.'''
new_intro=r'''Fix an irreducible central component $S_i$
of multiplicity $m_i$. Make the base change $t=s^{m_i}$,
normalize, and resolve as in \cref{lem:II:cyclic-component-cover}.'''
u16_new=replace(u16_new,old_intro,new_intro,'D14','cdp:st:C.2.UN.16','The root-cover construction has an earlier owner, so the field theorem precedes the general-type exclusion that uses it.')
old_first=item(u16_new,r'\item Write $f',r'\item Put $\mathcal O')
new_first=r'''\item Let $f':U'\to\Delta_s$ and $E$ be the resolution and component of \cref{lem:II:cyclic-component-cover}. Its local map \eqref{cdp:eq:C.SC.2} gives multiplicity one, proper generic finiteness and the factorization through $S_i^\nu$. Define
\[
 \mathcal T_{U'/\Delta_s}
 =\ker\bigl[df':T_{U'}\longrightarrow f'^*T_{\Delta_s}\bigr].
 \tag{C.SC.4}\hypertarget{tag-010O}{}\label{cdp:eq:C.SC.4}
\]

'''
u16_new=replace(u16_new,old_first,new_first,'D12','cdp:st:C.2.UN.16','The exact local maps are applied, and the repeated relative tangent definition C.SC.4 transfers to the full rank-two construction.')
cf3=r'\tag{C.CF.3}\hypertarget{tag-00BP}{}\label{cdp:eq:C.CF.3}'
u16_new=replace(u16_new,cf3,cf3+'\n '+r'\hypertarget{tag-00K4}{}\SsixEquationAliases{\label{cdp:eq:C.FD.3}}','D12','cdp:eq:C.FD.3','C.FD.3 is the same pair of modules after the explicitly stated O=C{s}, K=Frac(O); its label and permanent tag become aliases of C.CF.3.')
old_semi=item(u16_new,r'\item For completeness, semicompleteness',r'\item Take a complex basis')
new_semi=r'''\item For $V\in\mathfrak a_E$, choose a representative $v\in L$. It is a meromorphic vertical field on $U'$, holomorphic over $\Delta_s^*$ and at the generic point of $E$. Apply \cref{lem:II:semicomplete-transport} with this $f'$, $v$ and $E$. It proves semicompleteness of $V=v|_E$ on its full holomorphic locus, for every member of $\mathfrak a_E$.

For a particular nonzero section $v\in M$, put $k=\operatorname{ord}_E(v)$ and
\[
 w=s^{-k}v.
 \tag{C.SC.5}\hypertarget{tag-010P}{}\label{cdp:eq:C.SC.5}
\]
In the vertical frame $(\partial_x,\partial_y)$, $k$ is the minimum of the two coefficient orders. Thus $w\in L$ has order zero and its class in $L/sL$ gives a nonzero field $w_E\in\mathfrak a_E$.

'''
u16_new=replace(u16_new,old_semi,new_semi,'D12','cdp:st:C.2.UN.16','The full semicompleteness statement applies the earlier owner to each lift in L. The old single-field formula C.SC.5 remains as the explicit nonzero element of this same saturated space.')
old_curve=item(u16_new,r'\item A nonzero semicomplete meromorphic field on a smooth',r'\item Finally suppose')
u16_new=replace(u16_new,old_curve,r'''\item On a general smooth fibre of \eqref{cdp:eq:C.CF.2}, the lifted field is nonzero, meromorphic and tangent. Its semicompleteness and the compact-curve clause of \cref{lem:II:semicomplete-transport} give a rational or elliptic fibre.

''','D12','cdp:st:C.2.UN.16','The repeated pole/time-form proof is replaced by the shared curve application, with its invariant-fibre restriction specified.')
old_last=item(u16_new,r'\item Finally suppose $a(S_i^\nu)=0$',r'\end{enumerate}')
new_last=r'''\item When $a(S_i^\nu)=0$, the finite Stein-factor comparison of \cref{lem:II:cyclic-component-cover} gives
\[
 a(E)=a(S_i^\nu)=0.
 \tag{C.CF.9}\hypertarget{tag-00BV}{}\label{cdp:eq:C.CF.9}
\]
The fields in \eqref{cdp:eq:C.CF.7} satisfy all hypotheses of \cref{lem:II:zero-dimensional-field-surface}. Its two descended holomorphic fields on the common minimal model give the stated torus or Hopf alternative.

'''
u16_new=replace(u16_new,old_last,new_last,'D12','cdp:st:C.2.UN.16','The finite-field equality and a=0 classification now have exact earlier owners; the original C.CF.9 specialization remains.')

u15_statement=u15[:u15.index(r'\begin{proof}')]
u15_new=u15_statement+r'''\begin{proof}
Fix $S_i$ and take the component cover $E\to S_i^\nu$ of \cref{lem:II:cyclic-component-cover}. If $Z_i$ had general type, resolve the graph of the generically finite meromorphic map $E\dashrightarrow Z_i$ to obtain
$a:\widehat E\to E$ birational and $b:\widehat E\to Z_i$ generically finite. The Jacobian pullback gives
\[
 K_{\widehat E}=b^*K_{Z_i}+R,\qquad R\ge0.
 \tag{C.SC.3}\hypertarget{tag-010N}{}\label{cdp:eq:C.SC.3}
\]
It injects pluricanonical sections. A generically finite pluricanonical map of $Z_i$, composed with $b$, remains generically finite; multiplication by the canonical section of $mR$ gives its subsystem in $|mK_{\widehat E}|$. Thus $K_{\widehat E}$ is big and $\kappa(E)=2$. A smooth compact surface of general type is projective.

Apply \cref{cdp:st:C.2.UN.16} to this same resolved base change. The field $w_E$ given by \eqref{cdp:eq:C.SC.5} is nonzero and semicomplete. A Zariski-dense maximal solution satisfies the hypotheses of \cite[Main Theorem and the following clarification, arXiv v2 p.~2; Proposition~22, p.~25]{Guillot2019}: the surface $E$ is projective, hence K\"ahler, and the solution is univalent maximal on the holomorphic locus of $w_E$ by \cref{def:II:semicomplete-fields}. The resulting birational model is Abelian or admits a rational or elliptic fibration. Its Kodaira dimension is at most one, contrary to $\kappa(E)=2$.

When every regular leaf has algebraic closure, apply \cref{lem:II:algebraic-leaf-fibration} to the projective surface $E$ and the same $w_E$. Its graph and Stein map \eqref{cdp:eq:C.SC.6} give $\kappa(E)\le1$, the same contradiction. These two cases exhaust the regular leaves, so \eqref{cdp:eq:C.SC.1} follows for the chosen component and hence for every $S_i$.
\end{proof}'''
log('D12','cdp:st:C.2.UN.15',u15[u15.index(r'\begin{proof}'):],u15_new[u15_new.index(r'\begin{proof}'):],
    'The original construction and complete contradiction proof are compared with their receiving form. Root-cover, relative tangent, saturation, semicompleteness and algebraic-leaf arguments have unique earlier owners. The generically finite Jacobian subsystem and exact projective/Kähler/univalent hypotheses of Guillot2019 remain in the general-type application.')

# Canonical support retains its full signed-divisor, null-block and character maps.
u17_new=u17
u17_new=replace(u17_new,r'''For each component let
$h_i:Z_i\to S_i$ be its normalization followed by minimal
resolution, and let $D_i\ge0$ be the intrinsic resolution
conductor of \SeriesRef{cdp:st:A.5.3}.''',
r'''For each component let $\eta_i:T_i\to S_i$ be its normalization,
$\pi_i:Z_i\to T_i$ its minimal resolution, and $h_i=\eta_i\pi_i$.
Let $D_i\ge0$ be the intrinsic resolution conductor of
\cref{cdp:st:A.5.3}, applied to the reduced hypersurface $S_i\subset U$.''',
'D20','cdp:st:C.2.UN.17','The normalization and resolution arrows are explicitly composed, and A.5.3 is applied to the individual reduced component, with no ambient Betti hypothesis used in its conductor identity.')
old_rank=r'''Its rank is one since every nearby
torus has a one-dimensional space of canonical forms.
Choose a frame and evaluate it on $U$. Over $\Delta^*$,
Grauert base change identifies its restriction with a
nonzero torus canonical form, which is nowhere zero.'''
new_rank=r'''On a smooth fibre $F_t$, adjunction identifies
$K_U|_{F_t}$ with $K_{F_t}\otimes T^*_{\Delta,t}$; the base form
$dt$ trivializes its second factor. Thus the direct image has
rank one because a two-torus has a one-dimensional space of
canonical forms. Choose a frame and evaluate it on $U$.
Grauert base change identifies its restriction over
$\Delta^*$, through this adjunction map, with a nonzero
torus canonical form tensored by $dt$, which is nowhere zero.'''
u17_new=replace(u17_new,old_rank,new_rank,'D22','cdp:st:C.2.UN.17','The threefold canonical line restricts as the fibre canonical line tensored with the base cotangent line. The explicit dt trivialization supplies the exact map behind the original rank-one evaluation.')
u17_new=replace(u17_new,r'''followed by the conductor comparison of \SeriesRef{cdp:st:A.5.3}, gives''',r'''followed by the conductor comparison of \cref{cdp:st:A.5.3}, gives''','D04','cdp:st:C.2.UN.17','The local conductor comparison is cited by its statement number in this paper.')
old_adj=r'''these standard class VII facts are stated with
their adjunction argument in \cite[\S1, pp.~4--5]{Dloussky2006}.
For completeness, adjunction gives
$K_M\cdot C=2p_a(C)-2-C^2$. A curve of arithmetic genus
zero is a smooth rational curve; minimality excludes
self-intersection $-1$, and self-intersection zero would
give zero real class and hence $K_M\cdot C=0$, contradicting
adjunction. Every other curve has arithmetic genus at
least one and $C^2\le0$, so also has nonnegative canonical
intersection.'''
new_adj=r'''these are the class VII facts in
\cite[\S1, arXiv v3 p.~4, and Theorem~1.8, p.~5]{Dloussky2006}.
The cited surface is our minimal $M$ with $b_1(M)=1$ and
$b_2(M)>0$, and its intersection pairing is the one used here.'''
u17_new=replace(u17_new,old_adj,new_adj,'D17','cdp:st:C.2.UN.17','Opened the exact class VII intersection and canonical-degree paragraph, arXiv v3 p.4, and Theorem1.8 p.5. The repeated adjunction proof is replaced by its citation; the distinct semidefinite block analysis below remains complete.')
for old,new,reason in [
 (r'\cite[Remark~2.7]{DlousskyTeleman2012}',r'\cite[Remark~2.7, arXiv v2 p.~9]{DlousskyTeleman2012}','The complete homologically trivial effective-divisor list was freshly opened at its version-specific page.'),
 (r'\cite[Theorem~0.2]{Dloussky2006}',r'\cite[Theorem~0.2, arXiv v3 p.~2; Definition~2.20, p.~14]{Dloussky2006}','Opened the theorem and its NAC definition; the receiving map takes the paper divisor A and flat line L to source D_m=A and F=L^{-1}.')
]:
    # One occurrence is in the nonprinting input declaration; the body occurrence
    # is separately logged and supplies the reader-facing exact locator.
    for _ in range(u17_new.count(old)):
        p=u17_new.index(old);u17_new=u17_new[:p]+new+u17_new[p+len(old):]
        log('D18','cdp:st:C.2.UN.17',old,new,reason)
u17_new=replace(u17_new,r'''These are exactly
the hypotheses of \cite[Theorem~0.2, arXiv v3 p.~2; Definition~2.20, p.~14]{Dloussky2006},
which proves existence of a global spherical shell.''',
r'''In \cite[Definition~2.20, arXiv v3 p.~14]{Dloussky2006},
take $m=n$, $D_m=A$ and the flat line $F=L^{-1}$.
Then $nK_M+F+[A]=0$ is precisely that source's
numerically anticanonical condition. Its
\cite[Theorem~0.2, arXiv v3 p.~2]{Dloussky2006}
therefore gives a global spherical shell.''',
'D22','cdp:st:C.2.UN.17','The exact sign and dual of the flat line in the published NAC convention are stated; the hypothesis comparison uses the constructed isomorphism rather than a terminology-only match.')
log('D13','cdp:st:C.2.UN.17',orphan17,'','The orphan paragraph repeated the later Hopf exclusion and described the role of an earlier reduction. UN.17 keeps its complete line-bundle/NAC conclusions, and UN.19 states the Hopf result once.')

# The Hopf theorem applies the earlier component-cover and field owners.
u19_new=u19
old_cover=item(u19_new,r'\item We first identify the quotient',r'\item Write $Z_i$')
new_cover=r'''\item Apply \cref{lem:II:cyclic-component-cover} to the chosen component $S_i$ of multiplicity $m_i$, using an equivariant resolution of $t=s^{m_i}$. Write $E$ for its strict component and $G$ for its stabilizer. The root map \eqref{cdp:eq:C.SC.2} and its proper quotient \eqref{cdp:eq:C.HQ.2} give the comparison with $S_i^\nu$.

'''
u19_new=replace(u19_new,old_cover,new_cover,'D12','cdp:st:C.2.UN.19','The complete earlier root-cover/stabilizer lemma replaces both repeated construction items; the original generic torsor and disconnected-cover scope are explicit there.')
old_min=item(u19_new,r'\item Every element of $G$',r'\item We exclude the torus')
new_min=r'''\item The torus and Hopf alternatives are nonruled. Apply the minimal-contraction clause of \cref{lem:II:cyclic-component-cover} to $\rho:E\to E_0$. The equivariant contraction gives \eqref{cdp:eq:C.HQ.3}; its graph with \eqref{cdp:eq:C.HQ.2} compares $Z_i$ with a resolution of $E_0/G$ by proper bimeromorphic maps.

'''
u19_new=replace(u19_new,old_min,new_min,'D12','cdp:st:C.2.UN.19','The same equivariant contraction/quotient graph is applied at the two nonruled minimal alternatives, with its hypotheses supplied by UN.16.')
u19_new=replace(u19_new,r'''The field comparison
in (C.CF.9) gives
$a(E)=0$, and \ref{cdp:st:C.2.UN.16} says''',
r'''The function-field comparison in
\cref{lem:II:cyclic-component-cover}, and birational pullback
through $Z_i$ and $M_i$, give $a(E)=a(M_i)=0$.
Now \cref{cdp:st:C.2.UN.16} says''',
'D22','cdp:st:C.2.UN.19','The equality a(E)=a(M_i) is explicitly composed from the finite component map and the two birational maps; it applies before the a=0 conclusion of the field theorem.')
u19_new=replace(u19_new,r'''Birational maps between smooth compact
surfaces preserve $H^1$, as follows from their
factorization into point blowups.''',
r'''The point-blowup maps in
\cref{lem:II:blowup-topology}, applied to a common
resolution of two smooth compact surfaces, preserve
$H^1$ under their bimeromorphic comparison.''',
'D12','cdp:st:C.2.UN.19','The already admitted integral blowup owner supplies the precise surface H1 comparison used after resolving the quotient.')
for old,new in [
 (r'\cite[Remark~2.7]{DlousskyTeleman2012}',r'\cite[Remark~2.7, arXiv v2 p.~9]{DlousskyTeleman2012}'),
 (r'\cite[\S1.1]{Nakamura2008VII}',r'\cite[\S1.1, p.~2]{Nakamura2008VII}'),
 (r'\cite[Theorem~2.1]{Khaled2024Hopf}',r'\cite[Theorem~2.1, arXiv v2 p.~5]{Khaled2024Hopf}')
]:
    for _ in range(u19_new.count(old)):
        p=u19_new.index(old);u19_new=u19_new[:p]+new+u19_new[p+len(old):]
        log('D18','cdp:st:C.2.UN.19',old,new,'Freshly opened the precise source locus. Nakamura gives the finite primary-cover description in the algebraic-dimension-zero case used here; Khaled gives the contraction normal forms, and the divisor classification identifies the final quotient.')

# The equivariant rank-one descent retains its entire field action and general
# quotient fibre, now referring directly to the shared root-cover maps.
u20_new=u20
old_modules=item(u20_new,r'\item Use a resolution equivariant',r'An element $g\in G$')
new_modules=r'''\item Choose the equivariant resolution of \cref{lem:II:cyclic-component-cover}. Its stabilizer $G$ preserves $E$. Use the modules $M$ and $L$ of \eqref{cdp:eq:C.CF.3}, identifying $\mathcal O$ with $\C\{s\}$ and its fraction field with $\C(\{s\})$.
'''
u20_new=replace(u20_new,old_modules,new_modules,'D12','cdp:st:C.2.UN.20','The repeated module display C.FD.3 has the identical ring and localization as C.CF.3; its preserved alias is placed there. The semilinear action, reduction modulo s and equivariant restriction remain here in full.')
u20_new=replace(u20_new,r'''The quotient comparisons (C.HQ.2)--(C.HQ.3), or directly
the generic $G$-torsor in (C.HQ.1), identify''',
r'''The proper quotient map \eqref{cdp:eq:C.HQ.2} of
\cref{lem:II:cyclic-component-cover}, composed with the
equivariant graph resolution $\widehat E\to E$, identifies''',
'D14','cdp:st:C.2.UN.20','The rank-one branch needs the general component quotient, not a minimal-model conclusion from the Hopf case; the explicit composition removes that accidental premise.')
old_uniruled=r'''More generally the rational fibration itself is a family
of rational curves covering the surface; it is precisely
an actual ruling on a proper birational model and is
excluded when the original component is not uniruled.'''
new_uniruled=r'''For the uniruledness conclusion, the relative anticanonical
evaluation maps a general rational fibre by its degree-two
linear system to a plane conic. The torsion-free direct
image on the compact base curve is a rank-three vector
bundle, and this evaluation gives a meromorphic map of
$Z'_i$ to its projective bundle, birational onto the
closure of the conic family. That projective bundle is
projective because the base is a compact curve. A general
hyperplane section of the conic surface has a component
finite over the base; normalize it to a compact curve
$C'$. On the resulting generic conic over $\mathcal M(C')$,
the diagonal point gives projection to $\PP^1$, a
birational parameterization. Composing its inverse with
the finite base-change projection and the preceding
birational map produces a dominant meromorphic map
$C'\times\PP^1\dashrightarrow Z'_i$.
\Cref{def:II:marked-torus-fillings} and its
birational-invariance proof therefore make the original
component uniruled. This proves the final assertion.'''
u20_new=replace(u20_new,old_uniruled,new_uniruled,'D22','cdp:st:C.2.UN.20','The rational-fibration implication is written through the exact relative conic model, finite multisection and projection from a rational point, giving the dominant product map in the established uniruledness definition. No statement or hypothesis changes.')

# Preserve mathematical conclusions while removing repeated scope/process prose.
edits={
 'u15_new':[
  (r'''No K\"ahler, projectivity, Betti-number or Euler-number
assumption is imposed on $U$ or its central fibre.''','', 'D02','The statement already specifies the complete proper analytic hypotheses.'),
 ],
 'u16_new':[
  (r'''in which case an actual resolution of a meromorphic first integral''',r'''in which case a resolution of a meromorphic first integral''','D08','The first-integral resolution is named directly, with the correct article.'),
  (r'''\item Here is a finite bound for the saturation in \eqref{cdp:eq:C.CF.3}.
Choose an $\mathcal O$-basis $v_1,v_2$ of $M$.''',r'''\item Choose an $\mathcal O$-basis $v_1,v_2$ of $M$.''','D08','The adjugate calculation begins directly with its basis and proves the stated saturation bound.'),
  (r'''When $V_1\wedge V_2$ is nonzero, it is the announced
meromorphic frame.''',r'''When $V_1\wedge V_2$ is nonzero, the map
$(a,b)\mapsto aV_1+bV_2$ identifies $\mathcal M_E^2$
with $T_E\otimes\mathcal M_E$, giving the meromorphic frame.''','D22','The nonzero wedge gives the explicit invertible meromorphic coefficient map for the pair of fields.'),
  (r'''This last conclusion concerns the
specified generically finite covering component; the maps giving
it are part of the assertion.''','', 'D11','The statement already identifies E and its proper map; the earlier cover owner supplies those same maps.'),
  (r'''Its semicompleteness passes through the birational
open isomorphism and then over its full holomorphic
locus by the same closedness theorem.''',r'''Apply the bimeromorphic transport in
\cref{lem:II:semicomplete-transport} to this graph resolution.
It preserves semicompleteness on the lifted field's
full holomorphic locus.''','D12','The exact earlier transport is applied to this graph resolution, with its domain identified.'),
 ],
 'u17_new':[
  (r'''Raise \eqref{cdp:eq:C.CA.4} to the $m_i$-th power and substitute
\eqref{cdp:eq:C.CA.3}. This proves \eqref{cdp:eq:C.CA.1}, with its signs and every
full-fibre multiplicity retained.''',r'''Raising \eqref{cdp:eq:C.CA.4} to the $m_i$-th power and substituting
\eqref{cdp:eq:C.CA.3} gives \eqref{cdp:eq:C.CA.1}.''','D08','The exact substitution proves the full formula directly, without an editorial statement about retaining its coefficients.'),
  (r'''We specify why this line is complex-flat. On a class VII
surface''',r'''On a class VII
surface''','D08','The full flat-character argument begins directly with its cohomological inputs.'),
  (r'''Consequently $M$ contains a global spherical shell by the
proved numerically anticanonical theorem. In particular,
the unrestricted normalization problem does not require
the classification of class VII surfaces without a
numerically anticanonical divisor. These are restrictions
on the components of the actual map $f$; no occurrence of
every surface with \eqref{cdp:eq:C.CA.2} is asserted.''',
   r'Consequently $M$ contains a global spherical shell.','D11','The NAC and shell conclusions remain; repeated comparison with a classification problem and an occurrence disclaimer are removed.'),
  (r'''This proves the first
alternative without an assertion about unknown class VII
surfaces.''','', 'D02','The exact divisor classification already proves the asserted Hopf alternative.'),
  (r'''\item We also treat every singular block, rather than assuming
linear independence of the curve classes. Choose a nonzero
kernel vector $u$.''',r'''\item For a singular block choose a nonzero kernel vector $u$.''','D02','The complete null-block proof remains, with its hypothesis stated directly.'),
  (r'''This proves \eqref{cdp:eq:C.CA.2} and the stated normalization
restriction. The argument also shows directly why a
positive-Betti class VII surface whose every curve class
is zero in real cohomology cannot be a minimal
normalization model here: \eqref{cdp:eq:C.CA.6} would contradict
$K_M^2=-b_2(M)$.''',r'''In particular \eqref{cdp:eq:C.CA.6} and
$K_M^2=-b_2(M)$ force at least one of the displayed
curve classes to be nonzero in real cohomology.''','D11','The mathematical nonzero-curve-class consequence remains in positive form; the closing recapitulation is removed.'),
 ],
 'u19_new':[
  (r'''This holds for
arbitrary multiplicities, arbitrary central singularities,
and arbitrary Euler number.''','', 'D11','The unrestricted degeneration statement already has those hypotheses; the specified cyclic cover handles every multiplicity.'),
  (r'''We give
the fixed-point and quotient argument explicitly.''','', 'D08','The proof proceeds directly to its covering presentation and character map.'),
  (r'''We have proved the
cyclic-quotient assertion by actual quotient
maps, including their branch points.''','', 'D11','The local invariant-ring display and smoothness conclusion already include every branch point.'),
  (r'''This
proves the assertion for every component
in the original, unaltered degeneration.''','', 'D11','The equality of the minimal model with the quotient already proves the assertion.'),
 ],
 'u20_new':[
  (r'''an actual proper fibration''',r'''a proper fibration''','D08','The proper fibration is named directly, with the correct article.'),
  (r'''The base in \eqref{cdp:eq:C.FD.2} is already the Stein base; in particular
there is no additional finite cover of $B/G$ implicit in this
description.''',r'''The finite map from the Stein base of \eqref{cdp:eq:C.FD.2}
to $B/G$ is an isomorphism.''','D02','The same claimed base identity is stated by its exact finite morphism.'),
  (r'''\item We spell out the general quotient fibre. Let''',r'''\item Let''','D08','The proof starts directly with the kernel group defining the generic quotient fibre.'),
  (r'''\item For clarity, the generic fibre remains unchanged when the
surface quotient is resolved.''',r'''\item The generic fibre remains unchanged when the
surface quotient is resolved.''','D08','Removed the editorial preface; the following local invariant-ring map proves the claim.'),
  (r'''Thus the fibration has been constructed
on the original birational component, through the specified
finite quotient, rather than inferred from images of a
covering family of curves.''','', 'D02','The immediately preceding proper quotient and resolved graph already give the construction and its precise domain.'),
 ]
}
for name,operations in edits.items():
    owner={'u15_new':'cdp:st:C.2.UN.15','u16_new':'cdp:st:C.2.UN.16','u17_new':'cdp:st:C.2.UN.17','u19_new':'cdp:st:C.2.UN.19','u20_new':'cdp:st:C.2.UN.20'}[name]
    text=globals()[name]
    for old,new,kind,reason in operations:
        text=replace(text,old,new,kind,owner,reason)
    globals()[name]=text

for name,owner in [('u15_new','cdp:st:C.2.UN.15'),('u16_new','cdp:st:C.2.UN.16'),('u17_new','cdp:st:C.2.UN.17'),('u19_new','cdp:st:C.2.UN.19'),('u20_new','cdp:st:C.2.UN.20')]:
    text=globals()[name]
    while True:
        m=re.search(r'\bactual\s+',text)
        if m is None:break
        a=max(text.rfind('\n\n',0,m.start())+2,0);b=text.find('\n\n',m.end())
        if b<0:b=len(text)
        old=text[a:b];new=old[:m.start()-a]+old[m.end()-a:]
        log('D08',owner,old,new,'Names the mathematical field, map, divisor, inclusion or fibration directly; all coordinates and domain hypotheses are retained.')
        text=text[:a]+new+text[b:]
    if 'the announced\nmeromorphic frame' in text:
        text=replace(text,'the announced\nmeromorphic frame','the meromorphic frame','D08',owner,'The wedge-product criterion identifies the meromorphic frame directly.')
    globals()[name]=text

# Targeted input declarations follow the mathematical owner transfer.
for name,oldid,newid in [
 ('u16_new','cdp:st:C.2.UN.15','lem:II:cyclic-component-cover'),
 ('u20_new','cdp:st:C.2.UN.19','lem:II:cyclic-component-cover')
]:
    text=globals()[name];a=text.index(r'\StatementRecord');b=text.index('\n',a)
    old=text[a:b];new=old.replace(r'\SeriesRef{'+oldid+'}',r'\cref{'+newid+'}')
    assert old!=new
    text=text[:a]+new+text[b:];globals()[name]=text
    log('D14',newid,old,new,'The nonprinting input declaration now names the exact earlier construction used by the receiving proof; no derived global inventory is refreshed.')

heading_cover=r'\subsection{Cyclic component covers}\label{subsec:II:component-field-inputs}'
heading_semicomplete=r'\subsection{Semicomplete fields and their restrictions}\label{subsec:II:semicomplete-field-inputs}'
heading_fields=r'\subsection{Translation fields on component covers}\label{subsec:II:component-translation-fields}'
heading_canonical=r'\subsection{Canonical divisors on component surfaces}\label{subsec:II:component-canonical-support}'
heading_descent=r'\subsection{Class VII quotients and fibration descent}\label{subsec:II:component-cover-descent}'
heading_next=r'\subsection{Rank-two frames and finite quotients}\label{subsec:II:rank-two-component-frames}'
working=heading_cover+'\n\n'+cover+'\n'+heading_semicomplete+'\n\n'+definition+'\n'+transport+'\n'+zero_surface+'\n'+algebraic+'\n'+heading_fields+'\n\n'+u16_new+'\n\n'+u15_new+'\n\n'+heading_canonical+'\n\n'+u17_new+'\n\n'+heading_descent+'\n\n'+u19_new+'\n\n'+u20_new+'\n\n'+heading_next+'\n\n'
log('D14','sec:II:06',original,working,
    'Five complete subsections replace the undivided component-field opening. The cyclic cover, semicompleteness, a=0 and algebraic-leaf owners precede the full two-field construction; UN.16 precedes its UN.15 application. Canonical support precedes the Hopf use, and both rank branches use the general quotient owner. A new following heading keeps UN.22 onward outside the completed units.')

# Literal equation references and manual numbers use the established D19 map.
with (ROOT/'agents/continuation2_B/D19/S6_SERIES_PUBLISH_II_B2_D19_v1_equation_map.tsv').open() as f:
    established={r['old_tag']:r['target_label'] for r in csv.DictReader(f,delimiter='\t') if r['old_tag']}
for old_tag,target in established.items():
    # A bare (M), (A), or (B) here is a mathematical argument, not an
    # equation citation. Only this component cluster's dotted C.* tags
    # are literal equation references in the complete receiving text.
    if not re.fullmatch(r'C\.[A-Za-z0-9.]+',old_tag):continue
    token='('+old_tag+')'
    while token in working:
        p=working.index(token);a=max(working.rfind('\n\n',0,p)+2,0);b=working.find('\n\n',p)
        if b<0:b=len(working)
        old=working[a:b];new=old.replace(token,r'\eqref{'+target+'}',1)
        prior=list(re.finditer(r'\\StatementRecord\{([^}]+)\}',working[:p]))
        owner=prior[-1].group(1)
        log('D04',owner,old,new,'The literal inherited equation number is replaced by the preserved label, which identifies the same displayed map.')
        working=working[:a]+new+working[b:]
working=re.sub(r'\n{4,}','\n\n\n',working)
original_displays={}
for m in re.finditer(r'\\\[.*?\\\]',original,re.S):
    for lab in re.findall(r'\\label\{([^}]+)\}',m.group()):original_displays[lab]=m.group()
equations=[]
def number(m):
    old=m.group();tags=re.findall(r'\\tag\{([^}]+)\}',old)
    if not tags:return old
    assert len(tags)==1
    lab=re.findall(r'\\label\{([^}]+)\}',old)[0];assert established[tags[0]]==lab,(tags[0],lab)
    new=old.replace(r'\[',r'\begin{equation}',1);new=new[:-2]+r'\end{equation}';new=new.replace(r'\tag{'+tags[0]+'}','')
    prior=list(re.finditer(r'\\StatementRecord\{([^}]+)\}',working[:m.start()]))
    owner=prior[-1].group(1)
    equations.append(dict(old_tag=tags[0],target_label=lab,statement_id=owner))
    log('D19',owner,original_displays.get(lab,old),new,'The same formula, stable label and permanent target now use the section equation counter. Transferred owners and exact aliases are identified separately.')
    return new
working=re.sub(r'\\\[.*?\\\]',number,working,flags=re.S)
for old_tag,label,owner in [
 ('C.HQ.1','cdp:eq:C.HQ.1','lem:II:cyclic-component-cover'),
 ('C.FD.3','cdp:eq:C.FD.3','cdp:st:C.2.UN.16')
]:
    assert established[old_tag]==label
    equations.append(dict(old_tag=old_tag,target_label=label,statement_id=owner))
    display=next(m.group() for m in re.finditer(r'\\begin\{equation\}.*?\\end\{equation\}',working,re.S) if r'\label{'+label+'}' in m.group())
    log('D19',owner,original_displays[label],display,'The repeated formula has one equation counter, with its original label and permanent target preserved by SsixEquationAliases after the exact ring/coordinate identification.')

for kind in ('label','hypertarget'):
    pat=r'\\'+kind+r'\{([^}]+)\}'
    before=set(re.findall(pat,original));after=re.findall(pat,working)
    assert before<=set(after),(kind,before-set(after))
    assert not [x for x,n in Counter(after).items() if n>1],(kind,'duplicate')
assert '\r' not in working
assert not re.search(r'\\tag\{|night:P4R\.13|night:P4\.40',working)
assert not re.search(r'\\eqref\{eq:II:manual:[A-Z]\}',working)
assert Counter(re.findall(r'\\begin\{([^}]+)\}',working))==Counter(re.findall(r'\\end\{([^}]+)\}',working))
def displayed_payload(text):
    text=re.sub(r'\\tag\{[^}]+\}|\\label\{[^}]+\}|\\hypertarget\{[^}]+\}\{\}','',text)
    for token in (r'\SsixEquationAliases{}',r'\[',r'\]',r'\begin{equation}',r'\end{equation}'):
        text=text.replace(token,'')
    return re.sub(r'\s+','',text).rstrip('.,')
receiving_displays={}
for m in re.finditer(r'\\begin\{equation\}.*?\\end\{equation\}',working,re.S):
    for lab in re.findall(r'\\label\{([^}]+)\}',m.group()):receiving_displays[lab]=m.group()
for lab,old in original_displays.items():
    new=displayed_payload(receiving_displays[lab])
    if lab=='cdp:eq:C.FD.3':
        new=new.replace(r'_{\mathcalO}K',r'_{\mathbbC\{s\}}\mathbbC(\{s\})')
    assert displayed_payload(old)==new,('changed formula payload',lab)

# A bounded, coordinated application in the later irreducible-fibre owner.
# Its remaining complete proof and equation-alias placement stay verbatim.
p281=block('lem:II:torus-tube-numerical')
a=p281.index(r'\begin{proof}')+len(r'\begin{proof}')
b=p281.index('\n\nThe map is flat',a)
p281_old=p281[a:b]
p281_new=r'''
Choose a coordinate $t$ vanishing at the chosen value on a disc containing no other critical value. Apply \cref{cdp:st:C.2.UN.17} to $f|_U:U\to\Delta$, whose full central fibre is the single component $mS$. Its canonical generator has divisor $kS$ with $k\ge0$, giving $K_U\simeq\OO_U(kS)$. The principal fibre equation $(t)=mS$ gives $\OO_U(mS)\simeq\OO_U$. Adjunction for the reduced hypersurface $S$ gives $\omega_S\simeq\OO_U((k+1)S)|_S$; its $m$th power is trivial by the same principal fibre equation. These are the identities in \eqref{cdp:eq:C.UI.2}.'''
p281_receiving=replace(p281,p281_old,p281_new,'D12','lem:II:torus-tube-numerical','The complete current P281 proof was read. Its first construction is the exact irreducible specialization of UN.17 with m_1=m and a_1=k; the principal fibre and adjunction maps are stated. Its remaining torsion filtration, radial fundamental chain, Chern classes, conductor and curve-degree arguments remain byte-for-byte, as do both equation aliases before split.')
meta_old=r'\cref{lem:II:compact-analytic-tube,lem:II:conductor-duality,cdp:st:A.5.3,cdp:st:C.2.UN.5}'
meta_new=r'\cref{cdp:st:C.2.UN.17,lem:II:compact-analytic-tube,lem:II:conductor-duality,cdp:st:A.5.3,cdp:st:C.2.UN.5}'
p281_receiving=replace(p281_receiving,meta_old,meta_new,'D14','lem:II:torus-tube-numerical','The targeted nonprinting input list adds the earlier canonical-generator owner used in its first proof paragraph.')
remote=[dict(statement_id='lem:II:torus-tube-numerical',old_text=p281,new_text=p281_receiving,reason='The first canonical-generator paragraph is the exact mS specialization of UN.17. All other mathematics and alias hooks stay unchanged; complete old and receiving proof comparison is recorded.')]

def tsv(suffix,fields,data):
    with (OUT/(PRE+suffix)).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(data)
def final_block(ident):
    p=working.index(r'\StatementRecord{'+ident+'}')
    a=list(re.finditer(r'^\\begin\{(?:proposition|lemma|definition)\}',working[:p],re.M))[-1].start()
    if ident=='def:II:semicomplete-fields':b=working.index(r'\end{definition}',p)+len(r'\end{definition}')
    else:b=working.index(r'\end{proof}',p)+len(r'\end{proof}')
    return working[a:b]+'\n'
(OUT/(PRE+'_replacement.tex')).write_text(working,newline='\n')
(OUT/(PRE+'_UN17_receiving.tex')).write_text(final_block('cdp:st:C.2.UN.17'),newline='\n')
(OUT/(PRE+'_shared_owners.tex')).write_text(working[working.index(r'\begin{lemma}[Cyclic covers'):working.index(heading_fields)],newline='\n')
(OUT/(PRE+'_P281_receiving.tex')).write_text(p281_receiving+'\n',newline='\n')
tsv('_remote_repairs.tsv',['statement_id','old_text','new_text','reason'],remote)
with (ROOT/'S6_SERIES_PUBLISH_defects_II.tsv').open() as f:df=next(csv.reader(f,delimiter='\t'))
tsv('_defects.tsv',df,rows)
tsv('_equations.tsv',['old_tag','target_label','statement_id'],equations)

owners=[
 ('lem:II:cyclic-component-cover','subsec:II:component-field-inputs'),
 ('def:II:semicomplete-fields','subsec:II:semicomplete-field-inputs'),
 ('lem:II:semicomplete-transport','subsec:II:semicomplete-field-inputs'),
 ('lem:II:zero-dimensional-field-surface','subsec:II:semicomplete-field-inputs'),
 ('lem:II:algebraic-leaf-fibration','subsec:II:semicomplete-field-inputs'),
 ('cdp:st:C.2.UN.16','subsec:II:component-translation-fields'),
 ('cdp:st:C.2.UN.15','subsec:II:component-translation-fields'),
 ('cdp:st:C.2.UN.17','subsec:II:component-canonical-support'),
 ('cdp:st:C.2.UN.19','subsec:II:component-cover-descent'),
 ('cdp:st:C.2.UN.20','subsec:II:component-cover-descent')]
with (ROOT/'CHECK_EVENTS.tsv').open() as f:ef=next(csv.reader(f,delimiter='\t'))
events=[];now=datetime.now(timezone.utc)
for ident,unit in owners:
    row={k:'' for k in ef}
    row.update(statement_id=ident,date=now.date().isoformat(),date_utc=now.isoformat(),who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 conductor agent',
        type='used and rechecked in this run',
        outcome='Read the complete original owning statements/proofs and all transferred paragraphs, then compared the full receiving owner. Checked the cyclic root and stabilizer maps, finite Stein factor, semicomplete holomorphic loci, DVR saturation, canonical/conductor line maps, singular intersection blocks, flat-character map, Hopf quotient and rank-one quotient fibres at their stated domains. Exact primary-source loci are documented in the accompanying comparison. Exposed editorial rereading; no independent reproof or computation credit; final integrated PDF reading remains open.',
        event_id='publish:c3:conductor06:'+ident,phase='publication editorial comparison',
        source_file='agents/continuation3_conductor/'+PRE+'_replacement.tex',source_event_type='used and rechecked in this run',evidence_group='publish:c3:conductor06:'+unit,where=unit)
    events.append(row)
row={k:'' for k in ef}
row.update(statement_id='cdp:st:A.5.3',date=now.date().isoformat(),date_utc=now.isoformat(),who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 conductor agent',
    type='used and rechecked in this run',outcome='Read the complete currently admitted A.5.3 statement/proof and mapped its compact reduced hypersurface S to each individual S_i in UN.17. Its normalization/minimal-resolution maps are eta_i, pi_i and h_i; its effective divisor identity uses no ambient H2 hypothesis. The extra numerical and ruled conclusions are not used here. A.5.3 is unchanged. Exposed input reading; no independent credit.',
    event_id='publish:c3:conductor06:A5.3-scope',phase='publication editorial comparison',source_file='S6_SERIES_PUBLISH_II.tex',source_event_type='used and rechecked in this run',evidence_group='publish:c3:conductor06:UN17-A5.3-map',where='subsec:II:component-canonical-support')
events.append(row);tsv('_CHECK_EVENTS.tsv',ef,events)
row={k:'' for k in ef}
row.update(statement_id='lem:II:torus-tube-numerical',date=now.date().isoformat(),date_utc=now.isoformat(),who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 conductor agent',
    type='used and rechecked in this run',outcome='Read the complete current P281 statement/proof, then the entire receiving proof. Applied UN.17 to the proper disc restriction with full fibre mS: its generator coefficient a_1 is k. The principal fibre (t)=mS and hypersurface adjunction give the same four canonical identities. The flat Cartier filtration, normalization/resolution Euler comparison, radial chain [F]-m[S], Chern classes, conductor and degree conclusions are unchanged. Both equation-alias hooks remain before split. Exposed editorial rereading; no independent credit.',
    event_id='publish:c3:conductor06:P281-canonical-specialization',phase='publication editorial comparison',source_file='agents/continuation3_conductor/'+PRE+'_P281_receiving.tex',source_event_type='used and rechecked in this run',evidence_group='publish:c3:conductor06:UN17-P281',where='lem:II:torus-tube-numerical')
events.append(row);tsv('_CHECK_EVENTS.tsv',ef,events)

units=[
 ('subsec:II:component-field-inputs','Cyclic component covers'),
 ('subsec:II:semicomplete-field-inputs','Semicomplete fields and their restrictions'),
 ('subsec:II:component-translation-fields','Translation fields on component covers'),
 ('subsec:II:component-canonical-support','Canonical divisors on component surfaces'),
 ('subsec:II:component-cover-descent','Class VII quotients and fibration descent')]
status=[]
for unit,title in units:
    for n in range(1,26):
        state='done';reason='Complete original and receiving unit read and compared; each local instance found is logged. D10 and D16 remain done.'
        if n==18:state='open';reason='Exact edited primary-source loci opened and local locators corrected; inherited bibliography-wide checking remains separate.'
        if n==23:state='open';reason='Integrated typesetting and every page of the final PDF remain to be read.'
        status.append(dict(unit=unit,title=title,criterion=f'D{n:02d}',status=state,reason=reason))
    status.append(dict(unit=unit,title=title,criterion='structure',status='done',reason='All required constructions have earlier owners in this receiving order. Full original statements and labels remain; complete old/current proof comparison recorded. Later UN.22 and higher-rank units remain open under their separate following heading.'))
tsv('_unit_status.tsv',['unit','title','criterion','status','reason'],status)
transfers=[
 ('cdp:st:C.2.UN.15 / C.2.UN.16 / C.2.UN.19','lem:II:cyclic-component-cover','Root maps C.SC.2 and exact alias C.HQ.1; connectedness, generic multiplicity one and stabilizer quotient C.HQ.2.'),
 ('cdp:st:C.2.UN.16','lem:II:cyclic-component-cover','Finite Stein-factor and algebraic function-field comparison; C.CF.9 retains the a=0 specialization in UN.16.'),
 ('cdp:st:C.2.UN.19','lem:II:cyclic-component-cover','Equivariant nonruled minimal contraction and proper quotient map C.HQ.3.'),
 ('cdp:st:C.2.UN.15','def:II:semicomplete-fields','Univalent maximality, holomorphic locus and semicompleteness, with proper graph and source equivalence.'),
 ('cdp:st:C.2.UN.15 / C.2.UN.16','lem:II:semicomplete-transport','Ambient closedness, invariant component restriction, removable restricted poles and birational transport; curve no-poles/genus clause.'),
 ('cdp:st:C.2.UN.16','lem:II:zero-dimensional-field-surface','Two holomorphic models descend to one nonruled minimal surface; exact field dimensions exclude the two class VII alternatives.'),
 ('cdp:st:C.2.UN.15','lem:II:algebraic-leaf-fibration','Projective integral-curve incidence, relative conormal invariance, graph and Stein map C.SC.6, compact-curve genus and pluricanonical contraction.'),
 ('cdp:st:C.2.UN.15','cdp:st:C.2.UN.16','Relative tangent kernel C.SC.4 and explicit nonzero element s^{-k}v in C.SC.5, within the full two-dimensional saturation.'),
 ('cdp:st:C.2.UN.20','cdp:st:C.2.UN.16','C.FD.3 exact alias of the M,L display C.CF.3 under O=C{s}, K=Frac(O); equivariant action C.FD.4 stays in its application.')]
transfers.append(('lem:II:torus-tube-numerical','cdp:st:C.2.UN.17','P281 canonical-generator paragraph becomes the exact irreducible full-fibre mS specialization, with k=a_1; the principal fibre and adjunction maps remain in the receiving application.'))
tsv('_owner_transfers.tsv',['original_owner','receiving_owner','content'],[dict(zip(['original_owner','receiving_owner','content'],r)) for r in transfers])
print('Main replacement:',len(original),'->',len(working),'characters; new tags P238–P240, P301–P302.')
print('Defect rows:',len(rows),'; exposed events:',len(events),'; equation identities:',len(equations),'; owner transfers:',len(transfers),'; status rows:',len(status))
print('Five completed subsection units; next open unit rank-two-component-frames begins UN.22.')
print('One bounded remote repair: P281 canonical-generator application; remaining proof and split aliases unchanged.')
print('All 42 original labelled display payloads agree; C.FD.3 uses the explicitly identified O and fraction field.')
print('All original labels/targets retained once, exact equation aliases preserved, environments balanced, LF. No central file changed.')
