#!/usr/bin/env python3
"""Prepare the complete cyclic-component/K3 consolidation; no central writes."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv, re

root = Path(__file__).resolve().parents[1]
out = root / 'agents/continuation3_conductor'
prefix = 'S6_SERIES_PUBLISH_c3_conductor_11'
old = (out / (prefix + '_input.tex')).read_text()
oldk = (out / (prefix + '_K3_input.tex')).read_text()
cut = old.index(r'\begin{proposition}[A properly elliptic')
old31 = old[old.index(r'\begin{proposition}'):cut]
old33 = old[cut:]
k3 = oldk[oldk.index(r'\begin{proposition}'):]
rows = []

def log(kind, a, b, reason, owner):
    rows.append(dict(
        change_id=f'II-C3-UNRESTRICTED11-{len(rows)+1:04d}',
        type=kind, statement_id=owner,
        old_location='UN.31 / UN.33 / complete K3 subsection; exact source span',
        old_page='cp35 PDF omitted; exact source span supplied',
        new_location='cyclic-component-models / elliptic-configuration-list / k3-cyclic-components / nonnegative-component-covers',
        new_page='pending integrated final PDF', old_text=a, new_text=b,
        reason=reason,
        review_status='Complete original and receiving statements/proofs read and compared; exposed editorial rereading; final integrated PDF reading remains open.'))

def item(s, n):
    a = s.index(r'\begin{enumerate}')
    starts = [a + m.start() for m in re.finditer(r'\\item\b', s[a:])]
    b = starts[n] if n < len(starts) else s.index(r'\end{enumerate}', starts[n-1])
    return s[starts[n-1]:b]

def edit(s, a, b, kind, reason, owner):
    assert s.count(a) == 1, (owner, a[:100], s.count(a))
    log(kind, a, b, reason, owner)
    return s.replace(a, b, 1)

def display(s, tag):
    found = [m.group() for m in re.finditer(r'\\\[.*?\\\]', s, re.S)
             if r'\tag{' + tag + '}' in m.group()]
    assert len(found) == 1, tag
    return found[0]

owners = r'''\subsection{Cyclic quotients of smooth multiple elliptic fibres}\label{subsec:II:cyclic-component-models}

\begin{lemma}[Local cyclic quotients of elliptic fibrations]\hypertarget{tag-P317}{}\label{lem:II:local-cyclic-elliptic}
\StatementRecord{lem:II:local-cyclic-elliptic}{proved}{P317}{\cref{lem:II:identity-monodromy-elliptic}}
Let $q:E\to B$ be a relatively minimal proper holomorphic map from a smooth compact complex surface to a smooth compact connected curve, with connected elliptic general fibre and identity integral $H_1$ monodromy on its smooth base locus. Let a finite cyclic group $G$ act on $E$ and $B$ with $q$ equivariant. Suppose that the kernel $H$ of the action on $B$ acts by translations on the general elliptic fibre.

The quotient $E_1=E/H$ is smooth. Its map $q_1:E_1\to B$ has connected fibres, identity integral monodromy, one fixed elliptic curve as relative Jacobian, and only positive multiples of smooth elliptic fibres. The remaining group $Q=G/H$ acts faithfully on $B$.

At a base point with stabilizer of order $s$, write $\beta$ for the stabilizer generator's linear action on the fixed elliptic curve. A nonidentity $\beta$ forces the fibre of $q_1$ to have multiplicity one. After quotienting the subgroup acting trivially on the elliptic factor, the local quotient has the product action
\[
 (v,z)\longmapsto(\zeta_d^r v,\zeta_d z),
 \qquad d\in\{2,3,4,6\},\quad r\in\{1,d-1\}.
\]
For $\beta=1$, the quotient surface and the reduced fibre support are smooth. The full fibre remains a positive multiple of that elliptic support.
\end{lemma}
\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item By \cref{lem:II:identity-monodromy-elliptic}, the normalized base change $t=z^m$ at a full fibre $mF$ is a smooth elliptic family, finite \'etale over the original surface neighbourhood. Its marked fibrewise integration maps identify it with $F'\times\Delta_z$ for one elliptic curve $F'$. The deck generator has the form
$(v,z)\mapsto(v+\tau+a(z),\zeta_m z)$, where $a(0)=0$. Its free central action makes $\tau$ a point of exact order $m$.

Lift $a$ to a small holomorphic complex-valued function. The finite-order identity gives $\sum_{j=0}^{m-1}a(\zeta_m^jz)=0$: the sum is lattice-valued and vanishes at zero. Put
$b(z)=-m^{-1}\sum_{j=0}^{m-1}j\,a(\zeta_m^jz)$.
Shifting the index in the sum gives $b(\zeta_mz)-b(z)=-a(z)$, so the holomorphic coordinate change $v'=v+b(z)$ removes $a$. Thus the local quotient is
\[
 (F'\times\Delta_z)/\langle\delta\rangle,
 \qquad \delta(v,z)=(v+\tau,\zeta_m z),
 \qquad \operatorname{ord}(\tau)=m,
 \qquad t=z^m.
 \tag{C.EQ.3}\hypertarget{tag-00IG}{}\label{cdp:eq:C.EQ.3}
 \hypertarget{tag-00Q4}{}\SsixEquationAliases{\label{cdp:eq:C.KX.4}}
\]
We also use base-first coordinates $(u,w)$ on $\Delta_u\times F'$. The product permutation $(u,w)\mapsto(v=w,z=u)$ conjugates
$(u,w)\mapsto(\zeta_m u,w+\tau)$ to the displayed deck map and carries $t=u^m$ to $t=z^m$. In particular the base-first and fibre-first charts give the same finite \'etale root cover and the same quotient.

\item A base-fixing element of $H$ lifts functorially to the root chart. Its multiplier on $z$ is a power of $\zeta_m$; compose with the inverse power of $\delta$ to make the lift fix $z$. A power equal to the element's order is then a deck transformation fixing $z$, hence the identity. The lift acts on every smooth elliptic fibre by a translation of bounded finite order. Its translation parameter is holomorphic with values in a finite torsion subgroup, so is constant. The uniquely chosen $z$-fixing lifts therefore form a finite translation subgroup $T\subset F'$ and commute with $\delta$.

First take the quotient by $T$, and write $\bar F=F'/T$ and $m'=\operatorname{ord}(\bar\tau)$; thus $m'\mid m$. The remaining deck map is
$(\bar v,z)\mapsto(\bar v+\bar\tau,\zeta_mz)$.
Its $m'$th power generates the pure disc rotations of order $m/m'$. Quotienting them gives $w=z^{m/m'}$, with remaining action
\[
 (\bar v,w)\longmapsto(\bar v+\bar\tau,\zeta_{m'}w),
 \qquad t=w^{m'}.
 \tag{C.EQ.4}\hypertarget{tag-00IH}{}\label{cdp:eq:C.EQ.4}
\]
That action is free on the central fibre, so $E_1$ is smooth and the full fibre is
$m'(\bar F/\langle\bar\tau\rangle)$.
These charts also identify its general fibres with torsors under the fixed quotient elliptic curve and leave their integral monodromy equal to the identity. The quotient by $H$ is taken over $B$, so its fibres remain connected. The definition of $H$ makes $Q$ faithful on $B$.

\item Let $g\in Q$ generate the stabilizer of a base point, with order $s$. Linearize its base coordinate so that $g_B(t)=\lambda t$, where $\lambda$ is primitive of order $s$. The linear part $\beta$ on the marked elliptic fibres is constant, since it takes values in the discrete group of origin-preserving automorphisms. Suppose $\beta\ne1$, and let $m$ be the full fibre multiplicity.

In the base-first chart from the first item, name the elliptic coordinate $z$ and the root coordinate $u$. Choosing an $m$th root $\rho$ of $\lambda$ gives the functorial lift
\[
 \widetilde g(u,z)
       =(\rho u,\beta z+a(u)),\qquad
       \rho^m=\lambda .
 \tag{C.KX.9}\hypertarget{tag-00Q9}{}\label{cdp:eq:C.KX.9}
\]
Conjugation by this lift preserves the root deck group. Its action on $u$ preserves the multiplier $\zeta_m$, so it fixes the deck generator. Restriction to $u=0$ gives
\[
                         \beta\tau=\tau .
 \tag{C.KX.10}\hypertarget{tag-00PX}{}\label{cdp:eq:C.KX.10}
\]
The order of $\beta$ divides $s$. Since $\beta\ne1$, the elliptic endomorphism
$1+\beta+\cdots+\beta^{s-1}$ is zero. Applied to $\tau$, this says $s\tau=0$, so $m\mid s$.

The induced affine map on $F'/\langle\tau\rangle$ has a fixed point: the nonzero endomorphism $1-\beta$ of that elliptic curve is an isogeny and hence surjective. Choose a lift of a fixed point and compose $\widetilde g$ with a deck transformation so that it fixes the chosen lift. Its $s$th power is a deck transformation fixing a central point, hence is the identity by freeness. Therefore $\rho^s=1$. Since $\rho^m=\lambda$ has exact order $s$, the order of $\rho$ is $s$ and $\gcd(m,s)=1$. Together with $m\mid s$ this proves
\[
                 m=1\qquad(\beta\ne1).
 \tag{C.EQ.5}\hypertarget{tag-00II}{}\label{cdp:eq:C.EQ.5}
\]

\item For $\beta=1$, a point stabilizer acts on the reduced elliptic fibre by a translation fixing that point, hence fixes the whole fibre. Averaging local coordinates linearizes its finite action. In coordinates $(x,v)$ with $x$ normal to the fibre, it acts as $(x,v)\mapsto(\zeta_e x,v)$; an element with identity derivative is the identity in these averaged coordinates. The quotient coordinates $(x^e,v)$ prove that the quotient surface and reduced support are smooth. The full map is a power of the normal coordinate times a unit, so its fibre is a positive multiple of the elliptic support.

\item For $\beta\ne1$, the source fibre has multiplicity one by \eqref{cdp:eq:C.EQ.5}. In a marked product chart, after translating a fixed central point to the origin, the action is
$(v,z)\mapsto(\beta v+a(z),\zeta_s z)$ with $a(0)=0$.
Lift $a$ to a small holomorphic complex-valued function, and define
\[
 Pb(z)=\beta^{-1}b(\zeta_sz),\qquad c(z)=-\beta^{-1}a(z).
\]
Here $P^s=1$, and the finite-order identity gives $\sum_{k=0}^{s-1}P^kc=0$. Thus
$b=s^{-1}\sum_{k=0}^{s-1}kP^kc$ satisfies $(P-1)b=c$.
The holomorphic change $v'=v+b(z)$ makes
$a(z)+b(\zeta_sz)-\beta b(z)=0$ and conjugates the action to the product action.

Put $d=\operatorname{ord}(\beta)$. An origin-preserving elliptic automorphism acts on a rank-two integral lattice, with real trace $2\cos(2\pi r/d)$ an integer between $-2$ and $2$. Its nonidentity finite orders are therefore $2,3,4,6$, and the primitive exponents for these orders are $r=1,d-1$. The kernel on the elliptic factor is generated by the $d$th power of $g$ and acts by pure normal rotations. Its quotient coordinate is $z^{s/d}$. Naming that coordinate again $z$ gives
\[
             (v,z)\longmapsto(\zeta_d^r v,\zeta_d z),
             \qquad r\in\{1,d-1\}.
 \tag{C.EQ.6}\hypertarget{tag-00IJ}{}\label{cdp:eq:C.EQ.6}
\]
The quotients by $H$ keep the base function $t$. At a $Q$-stabilizer of order $s$, the quotient base coordinate is $T=t^s$.
\end{enumerate}
\end{proof}

\begin{lemma}[Elliptic fibrations on minimal surface models]\hypertarget{tag-P318}{}\label{lem:II:elliptic-minimal-descent}
\StatementRecord{lem:II:elliptic-minimal-descent}{proved}{P318}{\cite[Chapter~1, Proposition~2.1, p.~8]{Peters1990}}
Let $Z$ be a smooth compact minimal complex surface with $\kappa(Z)\ge0$, and let $\rho:X\to Z$ be a proper birational morphism from a smooth surface. Let $q:X\to C$ be a proper holomorphic map to a smooth compact connected curve, with connected fibres and elliptic general fibre. There is a unique holomorphic map $p:Z\to C$ with $q=p\circ\rho$. It has connected fibres, and pullback gives an injection
$H^1(C,\OO_C)\hookrightarrow H^1(Z,\OO_Z)$.
A smooth compact complex surface of nonnegative Kodaira dimension carrying a relatively minimal elliptic fibration is minimal.
\end{lemma}
\begin{proof}
The canonical class of a minimal surface with nonnegative Kodaira dimension is nef by \cite[Chapter~1, Proposition~2.1, p.~8]{Peters1990}. Factor $\rho$ into point blowups. The one-step Jacobian formula has coefficient one on the exceptional curve, and iteration gives
$K_X=\rho^*K_Z+\sum_j a_jE_j$ with $a_j>0$ on every $\rho$-exceptional prime. For a smooth general elliptic fibre $F$ of $q$, the normal line is trivial, so adjunction gives
\[
 0=K_X\cdot F
   =\rho^*K_Z\cdot F+\sum_j a_jE_j\cdot F,
                   \qquad a_j>0.
 \tag{C.CS.5}\hypertarget{tag-00DL}{}\label{cdp:eq:C.CS.5}
\]
Every term is nonnegative, hence every $E_j$ is vertical for $q$. The fibres of $\rho$ are connected, and each is therefore sent to one point. This defines $p$ set-theoretically. On a coordinate neighbourhood in $C$, the holomorphic coordinate of $q$ descends through $\rho_*\OO_X=\OO_Z$; these functions give the holomorphic map $p$ and prove uniqueness. Its fibres are the images under $\rho$ of the connected fibres of $q$, so are connected. Consequently $p_*\OO_Z=\OO_C$, and the coherent Leray sequence gives the asserted injection.

For the last assertion, take the minimal contraction $\rho:X\to Z$ of the relatively minimal elliptic surface $q:X\to C$. The argument just given makes every $\rho$-exceptional curve vertical. A nonidentity contraction has a first point blowdown, whose exceptional $(-1)$-curve would therefore lie in a fibre of $q$. Relative minimality excludes that curve. Hence $\rho$ is an isomorphism.
\end{proof}

\begin{lemma}[Canonical characters over an elliptic base]\hypertarget{tag-P319}{}\label{lem:II:elliptic-canonical-character}
\StatementRecord{lem:II:elliptic-canonical-character}{proved}{P319}{\cref{lem:II:identity-monodromy-elliptic,lem:II:local-cyclic-elliptic,cdp:st:C.2.UN.28}}
Let $q:E\to B$ satisfy \cref{lem:II:identity-monodromy-elliptic}, with $B$ an elliptic curve. Write its full fibres as $m_bC_b$. A nonzero base differential and the fibre differential with fixed normalized periods define a generator $\Omega$ of $H^0(E,K_E)$ whose divisor is
$\sum_b(m_b-1)C_b$.
For a finite group $G$ acting on $E$ and $B$ with $q$ equivariant, let $\lambda(g)$ be its character on the base differential and $\beta(g)$ its linear character on the fixed elliptic fibre. Then
$g^*\Omega=\lambda(g)\beta(g)\Omega$.
For every smooth surface $M$ properly birational to $E/G$, the quotient and graph maps give an injection
$H^0(M,K_M)\hookrightarrow H^0(E,K_E)^G$.
\end{lemma}
\begin{proof}
Choose a nonzero differential $\omega_B$ on $B$. On the smooth base locus the marked integration charts of \cref{lem:II:identity-monodromy-elliptic} have translation transition maps. Their fibre differentials differ by base differentials, so $\omega_B\wedge dz$ glues. At a full fibre $mC$, use the base-first root chart of \cref{lem:II:local-cyclic-elliptic}, with root coordinate $u$ and elliptic coordinate $z$. Writing $\omega_B=c(t)\,dt$ gives
\[
 \Omega=\omega_B\wedge dz
        =m\,c(u^m)u^{m-1}\,du\wedge dz ,
                  \qquad c(0)\ne0 .
 \tag{C.KX.7}\hypertarget{tag-00Q7}{}\label{cdp:eq:C.KX.7}
\]
This form is deck-invariant, since the deck map multiplies $u^{m-1}du$ by $\zeta_m^m=1$ and acts on $z$ by a translation. The root projection is \'etale, so descent preserves the zero order $m-1$ along the reduced central curve. These charts prove the asserted divisor. By \cref{lem:II:identity-monodromy-elliptic}, $p_g(E)=g(B)=1$, so $\Omega$ spans the canonical forms.

The fibre linear part of $g$ is constant because it is a holomorphic function with values in the discrete group of origin-preserving automorphisms of the marked elliptic curve. Its translation term adds a base differential to $dz$. Thus pullback multiplies the wedge by $\lambda(g)\beta(g)$ on the smooth locus, and the equality extends over $E$.

To obtain the last map, resolve the graph of the meromorphic map $E\dashrightarrow M$ induced by the finite quotient and the given birational comparison. In the resulting diagram $E\xleftarrow{\mu}W\xrightarrow{\pi}M$, the map $\mu$ is a sequence of point blowups and $\pi$ is generically finite. The generic Jacobian makes $\pi^*:H^0(M,K_M)\to H^0(W,K_W)$ injective. The point-blowup identification of canonical forms, equivalently Hartogs extension across the finite images of the exceptional curves, identifies the latter space with $H^0(E,K_E)$. This is the same pullback map as in \eqref{cdp:eq:C.PG.4}--\eqref{cdp:eq:C.PG.5}, with these specified $E,W,M$. It is $G$-invariant on the dense quotient locus and therefore everywhere.
\end{proof}

'''

log('D12', item(old33,2)+item(old33,3)+item(old33,4)+item(old33,5)+item(old33,6)+item(old33,7)+item(k3,8)+item(k3,10)+item(k3,13)+item(k3,14),
    owners[:owners.index(r'\begin{lemma}[Elliptic fibrations on minimal')],
    'P317 is the single proved owner of the root product, constant-translation gauge, fibrewise finite translation quotient, faithful base stabilizer obstruction, reflection quotient and product-action gauge. Its exact statement includes the fibre-translation hypothesis on the base kernel and the faithfulness of the remaining base action; its consumers prove those hypotheses.', 'lem:II:local-cyclic-elliptic')
log('D20',display(old33,'C.EQ.3')+'\n'+display(k3,'C.KX.4'),
    display(owners,'C.EQ.3'),
    'The product permutation (u,w)→(v=w,z=u) conjugates the base-first and fibre-first deck actions and preserves t. EQ3 is the single formula owner; KX4 retains its permanent target and same-counter alias. The receiving domain explicitly orders the coordinates, resolving the old KX4 F×disc versus (u,z) order.', 'cdp:eq:C.KX.4')
log('D22',item(old33,7),owners[owners.index(r'\item For $\beta\ne1$'):owners.index(r'\begin{lemma}[Elliptic fibrations on minimal')],
    'The translation-removal equation now names the exact twisted operator P b=beta^{-1} b(zeta_s z) and cocycle c=-beta^{-1}a. The weighted finite sum is checked by (P−1)b=c, and v↦v+b gives the explicit conjugacy. This supplies the operator omitted from the earlier averaging description.', 'lem:II:local-cyclic-elliptic')
log('D12',item(old31,6)+item(k3,6),
    owners[owners.index(r'\begin{lemma}[Elliptic fibrations on minimal'):owners.index(r'\begin{lemma}[Canonical characters')],
    'P318 owns the shared point-blowup canonical formula, nonnegative intersection argument, connected exceptional-fibre descent and coherent H1 injection. Its domain is a minimal compact complex surface with kappa≥0, using the freshly opened Peters Proposition2.1 p.8. CS5 moves with its exact formula and target; K3.5 remains the receiving diagram.', 'lem:II:elliptic-minimal-descent')
log('D12',item(k3,12)+item(old33,11),
    owners[owners.index(r'\begin{lemma}[Canonical characters'):],
    'P319 owns the elliptic-base canonical wedge, its exact multiple-root zero divisor, the lambda beta character and invariant-form pullback through a generically finite graph. KX7 moves intact; KX8 remains the K3 specialization. The base genus is explicitly one and the source is the full P306 smooth-multiple fibration.', 'lem:II:elliptic-canonical-character')

owner33='cdp:st:C.2.UN.33'
new33=old33
record=next(x for x in old33.splitlines() if x.startswith(r'\StatementRecord'))
new33=edit(new33,record,r'\StatementRecord{cdp:st:C.2.UN.33}{proved}{01DC}{\cref{lem:II:cyclic-component-cover,cdp:st:C.2.UN.15,cdp:st:C.2.UN.22,cdp:st:C.2.UN.29,lem:II:local-cyclic-elliptic,lem:II:elliptic-minimal-descent,lem:II:elliptic-canonical-character,cdp:st:C.2.UN.28}; \cite[\S2.1, arXiv v2 pp.~3--4; \S2.3, pp.~5--6]{UlmerUrzua2021}; \cite[Theorem~6.2, pp.~564--566; \S8(iv)(11), p.~585]{Kodaira1963II}; \cite[Chapter~1, \S1, pp.~5--6]{Peters1990}}',
    'D18','Names the common proved owners and the exact opened published and versioned loci. The former reference to the later K3 theorem is replaced by P317, whose local proof precedes both applications.',owner33)
new33=edit(new33,r'''In each row $p_g(M)=\chi(\OO_M)-1$. All additional
smooth multiple fibres are retained as part of the specified
surface; the table lists its nonsmooth reduced fibres.
This is a necessary classification of the displayed
invariant for actual components. The statement does not
assert occurrence of every abstract surface with these data.
The map $p$ is the elliptic map on the component surface;
the original threefold map has the degeneration disc as target.''',
    r'''In each row $p_g(M)=\chi(\OO_M)-1$. The table lists the nonsmooth reduced fibres; $p$ may also have smooth multiple fibres.''',
    'D11','The hypotheses already specify normalization components of torus degenerations and p is explicitly the component Iitaka map. Keeps the smooth-multiple-fibre qualification once, positively, and removes occurrence and target disclaimers.',owner33)
new33=edit(new33,item(old33,1),r'''\item Take the component cover $E'\to S^\nu$ and its cyclic stabilizer $G$ from \cref{lem:II:cyclic-component-cover}. Resolve its generically finite comparison with $M$ as $E'\leftarrow W\to M$. Injective pluricanonical pullback and the finite-base-change application of \cref{cdp:st:C.2.UN.15} give $\kappa(E')=1$. The relatively minimal elliptic model of \cref{cdp:st:C.2.UN.22,cdp:st:C.2.UN.29} is minimal by \cref{lem:II:elliptic-minimal-descent}; call it $E$. The birational map from $E'$ is its minimal contraction, so it is the same model in \eqref{cdp:eq:C.HQ.3}. It has the connected elliptic Iitaka map
'''+display(old33,'C.EQ.2')+r'''
Its smooth fibres have a fixed elliptic modulus and identity integral monodromy, and every full fibre is a smooth multiple. The action of $G$ descends to $E$ by \eqref{cdp:eq:C.HQ.3} and preserves $q$, because the connected-fibre Iitaka map is determined by the pluricanonical field. The same quotient comparison identifies $E/G$ properly birationally with $M$.

The quotient and Stein maps of \cref{cdp:st:C.2.UN.20} give a fibration over $B/G$ on a smooth birational model of $M$. Its general fibre is the quotient of a general fibre of $q$ by the kernel of the base action. A rational general fibre would force every positive pluricanonical section to vanish by adjunction, contradicting $\kappa(M)=1$. Thus that general fibre is elliptic. Apply \cref{lem:II:elliptic-minimal-descent} to a common smooth resolution over the minimal surface $M$; it descends the map to $p:M\to B/G$. Its smooth general fibre is unchanged. This is the connected-fibre Iitaka map, since the pluricanonical ratios factor through these elliptic fibres and their nonconstant image has dimension one. Set $B_0=B/G$; Riemann--Hurwitz gives $g(B_0)\le g(B)\le1$.

''','D22','Specifies the component-cover graph, minimal equivariant quotient, connected quotient fibre, rational-fibre adjunction exclusion and P318 descent before asserting p on the minimal M. EQ2 and all original hypotheses remain; the previous UN19–20 shorthand is replaced by the actual P240 HQ3 map and UN20.',owner33)
local_old=''.join(item(old33,n) for n in range(2,8))
local_new=r'''\item Let $H=\ker(G\to\operatorname{Aut}(B))$. Every element of $H$ acts on a general elliptic fibre by a translation. Indeed, an affine elliptic automorphism with nonidentity linear part has a fixed point, since its fixed-point equation is an isogeny equation. Riemann--Hurwitz then makes the quotient by any group containing it rational. The resulting general quotient fibre would contradict the preceding pluricanonical restriction argument. The translations have bounded finite order, so form a locally constant subgroup of the fixed elliptic curve.

Apply \cref{lem:II:local-cyclic-elliptic} to this map $q:E\to B$ and its cyclic group $G$. Its root chart \eqref{cdp:eq:C.EQ.3} and the quotient map \eqref{cdp:eq:C.EQ.4} construct the smooth surface $E_1=E/H$ over the same $B$, including every full multiple fibre. The remaining group $Q=G/H$ acts faithfully on $B$. At a point with stabilizer of order $s$, a nonidentity fibre character $\beta$ gives multiplicity one by \eqref{cdp:eq:C.EQ.5}; the primitive product action is \eqref{cdp:eq:C.EQ.6}. A trivial fibre character gives a smooth quotient surface and smooth elliptic reduced support. Those values have Euler contribution zero.

'''
new33=edit(new33,local_old,local_new,'D12',
    'The complete repeated local quotient proofs move to P317. The receiving application proves the translation hypothesis for the base kernel using the exact quotient general fibre and pluricanonical adjunction, then names the same q, G, H, E/H and faithful Q. All full multiplicities and the beta=1 branch remain.',owner33)
new33=edit(new33,r'''generate the quotient function field. They give
the following minimal Weierstrass equations:''',
    r'''generate the quotient function field. Indeed, adjoining $z$ to their field recovers $x=z^{-2r}X$ and $y=z^{-3r}Y$, and $z^d=T$. Thus the extension has degree at most $d$. The faithful cyclic action of order $d$ gives fixed-field degree $d$, so the invariant field is exactly the displayed one. They give the following minimal Weierstrass equations:''',
    'D22','Proves the precise invariant-field equality: the finite extension obtained by adjoining z has degree at most d and the faithful group has degree d. This identifies the birational quotient morphism rather than inferring it from the equations alone.',owner33)
new33=edit(new33,r'''The invariant meromorphic functions
''',r'''Over the meromorphic function field of the base, the invariant functions
''','D22','States the analytic base field for the quotient Weierstrass calculation; the finite extension over that field is generated by the root coordinate z.',owner33)
new33=edit(new33,r'''The equations are minimal, since their indicated
orders are below the Weierstrass rescaling threshold.
The primitive monodromy matrices and their characters distinguish the
unstarred and starred types; see \citet[Section~2.3, pp.~5--6]{UlmerUrzua2021}
and \citet[Theorem~6.2 and Section~8(iv)]{Kodaira1963II}.''',
    r'''The equations are minimal: for every row, the coefficient orders are below a simultaneous division by $T^4$ and $T^6$ in the Weierstrass rescaling. The positive $T$-loop lifts to $z\mapsto\zeta_d z$. In the quotient, its endpoint $(v,\zeta_d z)$ is identified with $(\zeta_d^{-r}v,z)$, so its action on the fixed fibre is multiplication by $\zeta_d^{-r}$. This is the inverse of the deck character in \eqref{cdp:eq:C.EQ.6}. In the convention of \cite[\S2.1, arXiv v2 pp.~3--4]{UlmerUrzua2021}, a fixed period $\tau$ and a matrix $\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$ send the row cycle $(m,n)$, representing $m\tau+n$, to a cycle representing $(c\tau+d)(m\tau+n)$; the uniformizing deck multiplier is $(c\tau+d)^{-1}$. Thus the displayed endpoint identification gives exactly the row-cycle monodromy in \cite[\S2.3, arXiv v2 pp.~5--6]{UlmerUrzua2021}. Its finite-order rows, together with the minimal Weierstrass equations, distinguish the starred and unstarred types in \eqref{cdp:eq:C.EQ.8}; Kodaira's fibre classification is \cite[Theorem~6.2, pp.~564--566]{Kodaira1963II}.''',
    'D22','Names the positive-loop endpoint identification (v,zeta_d z)~(zeta_d^{-r}v,z), so the local monodromy is the inverse deck character. The types and every coefficient of EQ8 remain unchanged; the freshly opened Ulmer–Urzúa uniformization pp.3–4 fixes the convention.',owner33)
new33=edit(new33,r'''This verifies the reduction to that table,
including the two different types of each primitive
order. Their Euler numbers are $12r/d$.

\par\medskip\noindent\textbf{All faithful cyclic base actions.}
On $B=\PP^1$''',
    r'''Their Euler numbers are $12r/d$.

\item On $B=\PP^1$''',
    'D13','The full quotient-to-relatively-minimal-model map and Euler numbers remain. Starts a numbered proof item for the rational-base action instead of an internal unnumbered heading and repeated verification sentence.',owner33)
new33=edit(new33,r'''For completeness, the number fixed by a nontrivial
power is''',r'''The number fixed by a nontrivial power is''',
    'D08','States the fixed-point calculation directly.',owner33)
new33=edit(new33,r'''Enumerating these actual characters gives''',
    r'''Enumerating these characters gives''','D08','The exact exponent reduction preceding the table already identifies the characters.',owner33)
new33=edit(new33,r'''These finite counts, the local reflection reductions,
and the Euler sums are independently executed in
\path{code/root_cyclic_elliptic_types.py} and its
saved output.''','',
    'D09','The finite branch indices, all character exponents, primitive reduction rule and Euler sums remain explicit. The program moves to provenance addition157 at its pinned CDP checkpoint13 path; the present pass claims no independent execution.',owner33)
new33=edit(new33,item(old33,11),r'''\item A free base orbit has a neighbourhood in the quotient isomorphic to the neighbourhood of one fibre in the orbit. Since the source fibres are smooth multiples, the preceding stabilizer list exhausts the nonsmooth reduced fibres. A free cyclic translation action on an elliptic base also leaves only smooth multiples. Positive Euler number therefore occurs over $B_0=\PP^1$ with nontrivial fibre linear character.

Apply \cref{lem:II:identity-monodromy-elliptic} to $q_1:E_1\to B$; it gives $p_g(E_1)=g(B)$. The quotient comparison $E_1/Q=E/G$ with $M$ gives the injective pullback of canonical forms through a resolved graph as in \eqref{cdp:eq:C.PG.4}--\eqref{cdp:eq:C.PG.5}. For $B=\PP^1$, it follows that $p_g(M)=0$.

For elliptic $B$, apply \cref{lem:II:elliptic-canonical-character} with $(E,q,G)=(E_1,q_1,Q)$. Choose the base generator with derivative $\zeta_n$ and write the fibre character as $\zeta_n^a$, as in \eqref{cdp:eq:C.EQ.11}. The canonical character is then $\zeta_n^{a+1}$. The lemma's exact graph pullback embeds $H^0(M,K_M)$ in its invariant subspace. Hence $p_g(M)=0$ when $a+1\not\equiv0\pmod n$. Every Euler-twelve row of \eqref{cdp:eq:C.EQ.11} has this nontrivial character.

''','D12','P306 supplies the full-base genera. P319 supplies the already proved multiple-root wedge and invariant-form map, with exact substitutions E=E1, q=q1, G=Q and characters lambda=zeta_n, beta=zeta_n^a. The argument still distinguishes Euler12 by its nontrivial character and retains the graph pullback.',owner33)
new33=edit(new33,r'''Analytic Riemann--Roch gives
$12\chi(\OO_M)=e(M)$.''',
    r'''Analytic Riemann--Roch \cite[Chapter~1, \S1, pp.~5--6]{Peters1990} gives $12\chi(\OO_M)=e(M)$.''',
    'D18','Adds the exact opened analytic surface Noether formula after the preserved vertical canonical divisor and adjunction proof of K_M²=0.',owner33)
new33=edit(new33,r'''This proves all assertions while preserving every
smooth multiple fibre and every actual quotient map.''','',
    'D11','Deletes the closing scope recapitulation. The statement and each quotient construction retain their full multiplicities.',owner33)
new33=r'\subsection{Elliptic fibre configurations of component surfaces}\label{subsec:II:elliptic-configuration-list}'+'\n\n'+new33

ownerk='cdp:st:C.2.UN.32'
newk=k3
newk=edit(newk,r'\StatementRecord{cdp:st:C.2.UN.32}{proved}{01DB}{}',
    r'\StatementRecord{cdp:st:C.2.UN.32}{proved}{01DB}{\cref{lem:II:cyclic-component-cover,cdp:st:C.2.UN.22,cdp:st:C.2.UN.29,cdp:st:C.2.UN.23,cdp:st:C.2.UN.28,lem:II:local-cyclic-elliptic,lem:II:elliptic-minimal-descent,lem:II:elliptic-canonical-character,cdp:st:C.2.UN.4}; \cite[Chapter~1, Theorem~3.1, p.~10]{Peters1990}; \cite[\S3.1, p.~7659; \S4.1, Theorem~27, p.~7663]{Roulleau2019GeneralizedKummer}; \cite[Theorem~II, Corollary~II, p.~201]{Lagrange1770}; \cite[\S3, Corollary~3, p.~560; \S6, Theorem~1(3) and its corollary, pp.~573--574]{PiatetskiShapiroShafarevich1971}}',
    'D18','The complete K3 owner declares its exact earlier internal dependencies and the freshly opened primary loci, including the precise four-square and isotropic-pencil pages.',ownerk)
newk=edit(newk,r'''For $a(M)>0$ there is an actual elliptic fibration''',
    r'''For $a(M)>0$ there is an elliptic fibration''','D08','The complete proof constructs the fibration on M; removes the workflow adjective.',ownerk)
newk=edit(newk,r'''and, after an actual translation of the origin,''',
    r'''and, after a translation of the origin,''','D08','The later equation (I−L)p=b gives the exact conjugating translation.',ownerk)
newk=edit(newk,r'''Use the actual normalized root base change and equivariant
resolution of \ref{cdp:st:C.2.UN.16}.''',
    r'''Use the normalized root base change and equivariant resolution of \cref{lem:II:cyclic-component-cover}.''',
    'D04','Names the proved component-cover owner with its exact normalization/resolution maps.',ownerk)
newk=edit(newk,r'''Also $a(E)=a(M)$. To check this equality through the
specified map, a meromorphic function on $E$ has elementary
symmetric functions along the finite generic sheets.
They descend meromorphically to $M$, so that the original
function satisfies a monic polynomial over $\mathcal M(M)$.
Thus the two meromorphic function fields have the same
transcendence degree.''',
    r'''The function-field clause of \cref{lem:II:cyclic-component-cover}, applied to the same generically finite map $E\to S_i^\nu$, gives $a(E)=a(S_i^\nu)=a(M)$. Its monic-polynomial map uses elementary symmetric functions along precisely these finite generic sheets; the last equality is the birational identification through \eqref{cdp:eq:C.K3.2}.''',
    'D12','Uses the complete P240 symmetric-function proof with the exact component-cover morphism and birational target map, preserving algebraic dimension in every branch.',ownerk)
newk=edit(newk,r'''\item The proper graph comparison of \ref{cdp:st:C.2.UN.19},
for this same component cover, also gives''',
    r'''\item Composing the proper birational quotient comparison in \eqref{cdp:eq:C.K3.2} with the birational map to the minimal surface gives''',
    'D12','KX1 is explicitly the composite of the already displayed proper graph maps, so its permanent target remains without a second quotient-construction proof or the former UN19 shorthand.',ownerk)
newk=edit(newk,r'''Pass to its unique smooth minimal model
$E_0$; the finite action descends through
the actual point blowdowns.''',
    r'''The compact-component theorem \cref{cdp:st:C.2.UN.15} applies to the resolved finite-base-change family and gives $\kappa(E)\le1$. Pass to its unique smooth minimal model $E_0$; \eqref{cdp:eq:C.HQ.3} of \cref{lem:II:cyclic-component-cover} descends the finite action through the point blowdowns and compares $E/G$ properly birationally with $E_0/G$.''',
    'D12','Uses the earlier full equivariant contraction owner with its exact E→E0 and quotient square, and states the finite-base-change kappa bound before the projective classification uses it.',ownerk)
newk=edit(newk,r'''Indeed every meromorphic function is algebraic over any
one nonconstant function on $B$ and hence constant on
the connected general fibres; the proper graph descends
it, as in (C.RF.9).''',
    r'''This is \eqref{cdp:eq:C.RF.9} for $X=E'$ and the connected-fibre map $q$: the finite-valued restriction to each connected general fibre and the proper graph in $B\times\PP^1$ identify the descended field with $\mathcal M(B)$.''',
    'D12','Applies the earlier complete algebraic-reduction field identity with exact source, Stein base and proper graph, retaining K3.4 as this component specialization.',ownerk)
newk=edit(newk,r'''In rank two, \eqref{cdp:eq:C.K3.3} and
$\chi(\mathcal O_{E_0})=0$, together with the compact
surface classification already used in \SeriesRef{cdp:st:C.3.1}
\cite[Chapter~1, Theorem~3.1, p.~10]{Peters1990}, leave the following
possibilities. The precise models in \ref{cdp:st:C.2.UN.22}
already give $\kappa(E_0)\le1$: on an elliptic general fibre
$F$ of its stated model, adjunction gives
$K|_F=K_F=\OO_F$, so every pluricanonical map is constant
on $F$ and has image of dimension at most one; a torus
has trivial canonical line.''',
    r'''In rank two, \eqref{cdp:eq:C.K3.3}, $\chi(\mathcal O_{E_0})=0$ and the preceding finite-base-change bound $\kappa(E_0)\le1$ give the following cases of the compact surface classification \cite[Chapter~1, Theorem~3.1, p.~10]{Peters1990}.''',
    'D12','The all-component kappa≤1 statement already proved in UN15 is applied to the resolved covering family; removes its repeated fibre-adjunction derivation and the unrelated C3.1 cross-reference, while preserving the complete classification cases.',ownerk)
newk=edit(newk,r'''Thus the only
remaining positive-dimensional case is a cyclic quotient
of a two-torus.''',
    r'''This gives the equivariant elliptic quotient map in the projective non-torus case.''',
    'D14','The former sentence announced the cyclic-torus conclusion before the non-torus principal-bundle argument. The preceding construction at this point gives the equivariant elliptic quotient map; the later complete Chern-vector and lattice proof establishes the torus quotient. The theorem statement is unchanged.',ownerk)
newk=edit(newk,item(k3,6),r'''\item On a common smooth resolution, the elliptic quotient map just obtained has the form
'''+display(k3,'C.K3.5')+r'''
with connected elliptic general fibre. Apply \cref{lem:II:elliptic-minimal-descent} with $Z=M$ and the displayed $\rho,q$. Since $M$ is minimal with $K_M=0$, the lemma descends it to a holomorphic map on $M$. Its injection
$H^1(B,\OO_B)\hookrightarrow H^1(M,\OO_M)=0$
gives $B\simeq\PP^1$.

''','D12','The full canonical-intersection and connected exceptional-fibre proof moves to P318. Its K3 application keeps the complete K3.5 common-resolution diagram and exact specialization Z=M, rho, q, K_M=0; the base conclusion remains.',ownerk)
newk=edit(newk,r'''The local invariant
direct-image calculation (C.RG.13)
applies and gives
$p_g(E_0)=g(B)$, so $B$ is elliptic.''',
    r'''Apply \cref{lem:II:identity-monodromy-elliptic} to the displayed $q:E_0\to B$. Its full-base direct-image and Leray calculation \eqref{cdp:eq:C.RG.13} gives $p_g(E_0)=g(B)$. Equation \eqref{cdp:eq:C.KX.2} makes $B$ elliptic.''',
    'D04','Replaces the literal RG13 locator with the complete P306 owner and its exact map q:E0→B, including the full-base multiple-fibre descent.',ownerk)
newk=edit(newk,r'''In algebraic dimension one its
connected-fibre function field is
intrinsic, by (C.RG.13) and
(C.K3.4).''',
    r'''In algebraic dimension one, the field identity \eqref{cdp:eq:C.K3.4} makes its connected-fibre base intrinsic.''',
    'D04','RG13 is a coherent cohomology identity and supplies the genus, while K3.4 is the exact meromorphic-field identity supplying equivariance. The receiving sentence uses the established field morphism for that step.',ownerk)
newk=edit(newk,item(k3,8),'','D12',
    'The entire normalized root, product trivialization and weighted averaging proof is now P317 before this theorem. EQ3/KX4 is its one chart with an explicit product-permutation map and both permanent targets. The receiving application below uses q:E0→B with the same full fibre.',ownerk)
newk=edit(newk,item(k3,10),r'''\item Apply \cref{lem:II:local-cyclic-elliptic} to $q:E_0\to B$, $G$ and the translation kernel $H$ just established. It constructs
'''+display(k3,'C.KX.5')+r'''
as a smooth surface over $B$, with fixed quotient elliptic curve and identity integral monodromy. At a full fibre $mC$, its exact root-quotient map is \eqref{cdp:eq:C.EQ.4}. With $e=m/m'$, the pure normal rotation quotient has local coordinate $x\mapsto x^e$, and the full fibre equation becomes $t=(x^e)^{m/e}$ with $e\mid m$. Thus the full reduced support is smooth elliptic and the multiplicity is the one supplied by that quotient map. The remaining group $Q$ acts faithfully on $B$.

''','D12','P317 supplies the repeated full smoothness/reflection/root calculation. The exact KX5 finite quotients and local multiplicity map x↦x^e, e=m/m′, are retained as this application; every full fibre is accounted for.',ownerk)
newk=edit(newk,r'''The same direct-image
calculation gives''',
    r'''The full-base calculation of \cref{lem:II:identity-monodromy-elliptic}, applied to $q_1:E_1\to B$ and $g(B)=1$, gives''',
    'D12','Applies P306 to the precise new translation quotient, preserving KX6 and all genera.',ownerk)
newk=edit(newk,r'''The
K3 descent argument
(C.K3.5) makes its
base $B/Q\simeq\PP^1$.''',
    r'''Applying \cref{lem:II:elliptic-minimal-descent} through \eqref{cdp:eq:C.K3.5} makes its base $B/Q\simeq\PP^1$.''',
    'D04','Names the prior proved common-resolution descent and exact diagram for the remaining quotient fibration.',ownerk)
newk=edit(newk,r'''After translating the
origin on $B$, its
generator is a linear
elliptic automorphism.''',
    r'''Write its generator as $b\mapsto Lb+c$ on $B$. Since $L\ne1$, the isogeny $1-L$ is surjective; choose $b_0$ with $(1-L)b_0=c$. Translation by $b_0$ conjugates the generator to $L$.''',
    'D22','Gives the exact translation conjugacy before identifying the faithful derivative character; no choice of origin is asserted without its morphism.',ownerk)
newk=edit(newk,item(k3,12),r'''\item Apply \cref{lem:II:elliptic-canonical-character} with $(E,q,G)=(E_1,q_1,Q)$. The base is elliptic, and \eqref{cdp:eq:C.KX.6} gives the unique canonical form. The lemma constructs it by \eqref{cdp:eq:C.KX.7}, with divisor $\sum_b(m_b-1)C_b$, and gives its character $\lambda(g)\beta(g)$.

The proper birational comparison $E_1/Q=E_0/G\dashrightarrow M$ gives the lemma's injective pullback of the nonzero K3 form into this one-dimensional canonical space. The image is invariant, so
'''+display(k3,'C.KX.8')+r'''
The faithful character $\lambda$ consequently makes $\beta$ faithful as well.

''','D12','The full canonical-root zero divisor and character proof moves to P319, with KX7. The application names E1, q1, Q and the same quotient graph, retains KX8 and its faithful-character consequence, and uses invariance of the pulled-back K3 form.',ownerk)
newk=edit(newk,item(k3,13)+item(k3,14),r'''\item Let a base point have stabilizer of order $s>1$. By \eqref{cdp:eq:C.KX.8} and the faithfulness of $\lambda$, its fibre character $\beta=\lambda^{-1}$ is nonidentity and has order $s$. Apply the stabilizer clause of \cref{lem:II:local-cyclic-elliptic} to $q_1:E_1\to B$. Its lift \eqref{cdp:eq:C.KX.9}, deck commutation \eqref{cdp:eq:C.KX.10} and multiplicity conclusion \eqref{cdp:eq:C.EQ.5} apply to this same full fibre and give
'''+display(k3,'C.KX.11')+r'''

''','D12','The two full repeated local obstruction items move to P317. The K3 specialization proves beta=lambda^{-1} nonidentity with exact stabilizer order before applying it, and keeps KX11 as this branch-value consequence. KX9/KX10 move intact to the shared owner.',ownerk)
newk=edit(newk,r'''\item We finish by an
explicit Chern-class
comparison, without
assuming that a
finite image or
preimage is
K\"ahler.
The smooth map''',
    r'''\item The smooth map''',
    'D02','The complete transition-cocycle Chern-vector proof follows directly. Deletes the framing and Kähler scope disclaimer without adding any Kähler assumption.',ownerk)
newk=edit(newk,r'''These cyclic configurations agree with the classical generalized-Kummer
list in \cite[\S3.1, p.~7659; \S4.1, Theorem~27, p.~7663]{Roulleau2019GeneralizedKummer},
which records the preceding cyclic-quotient work.
The exact integer matrices, every power's fixed-point count,
exact-stabilizer subtraction, quotient Euler average and resolution
Euler correction are computed in
\path{code/current_audits/audit_sign/code/UN24_UN39_exact_certificate_08.py};
the full four-row output and the formal identities
\eqref{cdp:eq:C.K3.8}--\eqref{cdp:eq:C.K3.9} are recorded in
\path{code/current_audits/audit_sign/UN24_UN39_exact_certificate_08.json}.''',
    r'''The configurations in \eqref{cdp:eq:C.K3.1} are the cyclic rows of the generalized Kummer classification \cite[\S3.1, p.~7659; \S4.1, Theorem~27, p.~7663]{Roulleau2019GeneralizedKummer}. The explicit fixed-point and quotient maps above give the singularity, exceptional-rank and quotient-Euler data for the component's cyclic action.''',
    'D09','Preserves all exact characteristic-polynomial, fixed-point, stabilizer-orbit, quotient-Euler and resolution calculations and their maps. Removes both program/JSON paths and agreement framing; provenance addition157 carries the pinned grind checkpoint10 program and its precise non-execution scope.',ownerk)
newk=edit(newk,r'\cite[Theorem~II, Corollary~II]{Lagrange1770}',
    r'\cite[Theorem~II, Corollary~II, p.~201]{Lagrange1770}',
    'D18','The freshly opened original 1868 text places the four-square consequence in the second corollary following TheoremII, printed p.201. The preceding theorem itself is a modular quadratic representation statement; the citation now identifies the required corollary.',ownerk)
newk=edit(newk,r'''\cite[\S3, Corollary~3, with the reflection
argument of \S6]{PiatetskiShapiroShafarevich1971}''',
    r'''\cite[\S3, Corollary~3, p.~560; \S6, Theorem~1(3) and its corollary, pp.~573--574]{PiatetskiShapiroShafarevich1971}''',
    'D18','Names the exact freshly opened English-translation pages. The projective K3 hypothesis and the nonzero integral isotropic divisor supplied by K3.8–9 match the source; its reflections take the class to a nef elliptic-pencil class.',ownerk)
newk=edit(newk,r'''Equality of the
Cech classes gives''',
    r'''Equality of the \v{C}ech classes gives''',
    'D23','Restores the accent in the exact torsor-to-lattice isomorphism proof.',ownerk)
newk=r'\subsection{K3 components and cyclic quotients}\label{subsec:II:k3-cyclic-components}'+'\n\n'+newk

owner31='cdp:st:C.2.UN.31'
new31=old31
record=next(x for x in old31.splitlines() if x.startswith(r'\StatementRecord'))
new31=edit(new31,record,
    r'\StatementRecord{cdp:st:C.2.UN.31}{proved}{01DA}{\cref{lem:II:cyclic-component-cover,cdp:st:C.2.UN.15,cdp:st:C.2.UN.22,cdp:st:C.2.UN.29,lem:II:identity-monodromy-elliptic,lem:II:elliptic-minimal-descent,cdp:st:C.2.UN.28,cdp:st:C.2.UN.23,cdp:st:C.2.UN.33,cdp:st:C.2.UN.32}; \cite[Chapter~1, \S3, pp.~9--10]{Peters1990}}',
    'D18','The classification now cites the preceding exact local, configuration and K3 owners, plus the opened surface-classification pages. The quotient and algebraic-dimension arguments use P240 instead of internal equation shorthand.',owner31)
new31=edit(new31,r'''A K3 component is either the cyclic torus quotient
of \ref{cdp:st:C.2.UN.24}, with the exact orders and configurations
listed there, or has an isotrivial elliptic fibration
over $\mathbb P^1$ through the non-torus-cover branch.
The singular and multiple fibres on these original
quotient surfaces are retained by the quotient maps;
the smooth-multiple assertion concerns the specified
cover $E_0$.''',
    r'''Every K3 component is a cyclic torus quotient as in \cref{cdp:st:C.2.UN.32}, with the orders and configurations stated there. In the non-torus-cover branch its comparison also gives an isotrivial elliptic fibration over $\PP^1$.''',
    'D12','Combines the original intermediate alternative with its already proved all-algebraic-dimensions conclusion formerly repeated in proof item10. The full UN24/UN32 owner now precedes this theorem. Preserves the additional isotrivial pencil in the non-torus-cover branch and removes repeated quotient-versus-cover scope narration.',owner31)
new31=edit(new31,r'''\item Take the actual component, cyclic stabilizer, and
proper birational quotient comparison in \ref{cdp:st:C.2.UN.16}
and (C.CQ.12).''',
    r'''\item Take the component cover $E\to S^\nu$, its cyclic stabilizer $G$ and the proper birational quotient map \eqref{cdp:eq:C.HQ.2} of \cref{lem:II:cyclic-component-cover}.''',
    'D04','Identifies the proper generic-finite component map and P240 quotient owner, replacing the literal CQ12 and informal source pointer.',owner31)
new31=edit(new31,item(old31,2),r'''\item Apply \cref{lem:II:identity-monodromy-elliptic} to the relatively minimal elliptic map $q:E_0\to B$ in either field-rank branch. It has the identity integral monodromy just obtained, so the lemma's full-base invariant calculation gives $R^1q_*\OO_{E_0}\simeq\OO_B$ and $p_g(E_0)=g(B)$. The component $E$ belongs to the smooth resolved finite-base-change torus family. The finite-base-change clause of \cref{cdp:st:C.2.UN.28} gives $p_g(E)=p_g(E_0)\le1$, hence $g(B)\le1$.

''','D12','P306 supplies the full multiple-root direct-image argument once, with the same q:E0→B; UN28 is applied through its exact finite-base-change scope. Removes the repeated calculation and independent-check adjective.',owner31)
new31=edit(new31,item(old31,3),r'''\item The minimal-model clause of \cref{lem:II:cyclic-component-cover} applies because $\kappa(E)\ge0$. It gives the descended holomorphic action and the proper quotient comparison
'''+display(old31,'C.CS.3')+r'''
Here the square is \eqref{cdp:eq:C.HQ.3} for this same cover, and its final birational map is the composite with the normalization and minimal model of the chosen component.

''','D12','The complete equivariant point-contraction proof already belongs to P240. Preserves the full CS3 square and final target map, and identifies it exactly with HQ3 and the chosen normalization/minimal-model composition.',owner31)
new31=edit(new31,item(old31,4)+item(old31,5),r'''\item Suppose $\kappa(Z)=1$. Equation \eqref{cdp:eq:C.CS.2} and \cref{cdp:st:C.2.UN.15} give $\kappa(E_0)=1$. Apply the original-component conclusion of \cref{cdp:st:C.2.UN.29} to this same component cover. Its construction uses $q:E_0\to B$, the action of $G$ on the pluricanonical field, an equivariant graph resolution $E'\to E_0$ and its connected-fibre Stein map. The quotient is
'''+display(old31,'C.CS.4')+r'''
The general fibre is $F/K$, where $K=\ker(G\to\operatorname{Aut}(B))$. In the proof of that result, the rational-quotient adjunction argument makes $K$ a finite translation subgroup of the fixed elliptic curve $A$, and its bounded-order translation parameters are locally constant. Thus the general quotient fibre is the fixed curve $A/K$. Its base has genus at most one by Riemann--Hurwitz, and this connected-fibre quotient is the Iitaka map on the smooth birational model of $Z$.

''','D12','Uses the complete original-component Iitaka/equivariant graph/Stein/fibre-translation proof already admitted in UN29. The receiving application specifies the identical cover, q, G, E′, base quotient, kernel K and fixed elliptic quotient A/K, retaining CS4 as the explicit map.',owner31)
new31=edit(new31,item(old31,6),r'''\item Resolve that quotient fibration and its birational comparison with $Z$ as
$Z\xleftarrow{\rho}X\xrightarrow{q}B/G$.
Apply \cref{lem:II:elliptic-minimal-descent} to this common resolution and the minimal surface $Z$ of Kodaira dimension one. Its canonical-intersection identity \eqref{cdp:eq:C.CS.5} makes every exceptional curve vertical and descends the map holomorphically to $Z$. The general fibres and their fixed elliptic modulus are unchanged, giving the asserted isotrivial Iitaka fibration.

''','D12','The shared complete CS5 canonical-intersection and graph descent now precedes the theorem as P318. Names its precise common resolution and kappa1 domain; retains the descended minimal-surface conclusion.',owner31)
new31=edit(new31,r'''Algebraic
dimension is preserved by the actual
generically finite component map, by
the symmetric-function field argument
in (C.K3.2)--(C.K3.3). Thus $E_0$ is
projective.''',
    r'''The function-field clause of \cref{lem:II:cyclic-component-cover} applied to $E\to S^\nu$ gives $a(E_0)=a(Z)=2$. Thus the smooth compact surface $E_0$ is projective.''',
    'D12','Applies the single P240 symmetric-function proof to the actual component-cover morphism and uses the birational normalization/minimal-model field identifications; removes the forward K3 formula reference.',owner31)
new31=edit(new31,r'''If it has
Kodaira dimension zero, the surface
classification and $\chi(\mathcal O_{E_0})=0$
make it Abelian or bielliptic.''',
    r'''In Kodaira dimension zero, the projective cases of the surface classification \cite[Chapter~1, \S3, pp.~9--10]{Peters1990} and $\chi(\mathcal O_{E_0})=0$ make it Abelian or bielliptic.''',
    'D18','Adds the exact opened classification locus for the projective zero-Kodaira cases. The complete bielliptic product and connected-automorphism-group construction remains.',owner31)
new31=edit(new31,item(old31,8),r'''\item Apply \cref{lem:II:elliptic-minimal-descent} to the resulting common resolution over the minimal Enriques surface $Z$. Its canonical class is torsion, so the $K_Z$ term of \eqref{cdp:eq:C.CS.5} is zero. The lemma descends the elliptic map to $Z$, and its injection into $H^1(Z,\OO_Z)=0$ makes the base $\PP^1$. This gives the asserted isotrivial Enriques fibration.

''','D12','The exact torsion-canonical specialization of P318 replaces the duplicate descent paragraph and keeps the Leray base calculation and isotrivial conclusion.',owner31)
new31=edit(new31,item(old31,9),r'''\item For a K3 target $Z$, apply \cref{cdp:st:C.2.UN.32} to the same degeneration and component normalization. It identifies $Z$ with the minimal resolution of the stated cyclic symplectic torus quotient in every algebraic dimension. Its proof gives the exact torus $A=E_0$ in the initial torus branch and $A=E_0/H$ in the non-torus branch, with remaining cyclic group $G/H$ and quotient equality
$(E_0/H)/(G/H)=E_0/G$.
In the latter branch, the invariant elliptic map descends through \eqref{cdp:eq:C.K3.5} to an isotrivial elliptic fibration on $Z$ over $\PP^1$. These are the same proper quotient and common-resolution maps as \eqref{cdp:eq:C.CS.3}.

''','D12','Applies the now preceding complete K3 owner instead of repeating its rank, algebraic-dimension, equivariant Iitaka and descent proof. The receiving map identifies both possible tori and the equality of the finite quotient, preserving the non-torus-cover intermediate elliptic pencil.',owner31)
new31=edit(new31,item(old31,10),r'''\item The compact-core bound \cref{cdp:st:C.2.UN.28} gives $p_g(Z)\le1$. The preceding cover bound also gives $0\le\kappa(Z)\le1$. In Kodaira dimension zero, the compact surface classification \cite[Chapter~1, \S3, pp.~9--10]{Peters1990} gives coherent Euler characteristic zero for tori, bielliptic and Kodaira surfaces, two for K3 surfaces and one for Enriques surfaces. In Kodaira dimension one, apply \cref{cdp:st:C.2.UN.33} with $M=Z$; its complete local quotient and Noether calculation gives $\chi(\OO_Z)\in\{0,1,2\}$. In particular $\chi(\OO_Z)\ge0$ in every case. On the other hand
'''+display(old31,'C.CS.6')+r'''
The integer $\chi(\OO_Z)$ therefore belongs to the set in \eqref{cdp:eq:C.CS.1}.

''','D12','The preceding full UN33 calculation supplies the kappa1 coherent Euler range, and the opened classification supplies the kappa0 values. Preserves CS6 and the compact-core bound. Removes the formerly later K3 theorem restatement because its complete owner now precedes the classification.',owner31)
new31=edit(new31,item(old31,11),'','D11',
    'Deletes the final repeated quotient-versus-cover disclaimer. The cover alternatives are confined to E0 in the statement and every original-component conclusion is obtained through its explicit quotient maps.',owner31)
new31=r'\subsection{Minimal models of cyclic component covers}\label{subsec:II:nonnegative-component-covers}'+'\n\n'+new31

new33=edit(new33,r'''\item Here is an explicit comparison with the Kodaira
types, including the direction of the character.
Write the fixed elliptic curve as''',
    r'''\item Write the fixed elliptic curve as''','D08','The full invariant-coordinate and loop-character comparisons follow immediately; removes the proof announcement.',owner33)
newk=edit(newk,r'''These are the same equivariant
graph and Stein comparisons
used there.''','',
    'D11','The rank-one, algebraic-reduction and Iitaka graph/Stein maps have each been specified in the preceding clauses; removes the closing repetition.',ownerk)
newk=edit(newk,r'''pencil on $M$. This proves the remaining projective
branch. If the quotient has algebraic dimension
one,''',
    r'''pencil on $M$.

\item For a quotient of algebraic dimension one,''',
    'D14','Separates the full projective isotropic-lattice construction from the algebraic-dimension-one pencil construction; both remain complete and in dependency order.',ownerk)
newk=edit(newk,r'''elliptic pencil on $M$. This completes the
assertion for $a(M)>0$.''',
    r'''elliptic pencil on $M$.''','D11','Deletes the closing recapitulation after the precise quotient and common-resolution pencil maps.',ownerk)
newk=edit(newk,r'''\item Finally we prove the occurrence assertion with its
specified compact comparison. Start with any torus
$A$ and one of the actual cyclic symplectic actions
above, of order $n$.''',
    r'''\item Start with any torus $A$ and a cyclic symplectic action of order $n$ in \eqref{cdp:eq:C.K3.1}.''',
    'D08','States the input of the full compact realization directly. Its finite quotient, both fibres, resolution, connectedness and Euler adjustments remain.',ownerk)
newk=edit(newk,r'''\item Finally $Q$ is''',r'''\item The group $Q$ is''',
    'D08','Introduces the proved torus quotient directly.',ownerk)
newk=edit(newk,r'''\item We next compute the cyclic quotient branch. By''',
    r'''\item By''','D08','The characteristic-polynomial and fixed-point calculations follow without a production-style announcement.',ownerk)
newk=edit(newk,r'''resolution with exactly that specified K3 minimal model.''',
    r'''resolution with that K3 minimal model.''','D08','The realization refers to the given cyclic quotient class.',ownerk)
newk=edit(newk,r'''specified torus quotient.''',r'''torus quotient.''',
    'D08','The explicit map from the strict component to A/<g> already identifies the quotient.',ownerk)
owners=owners.replace('with these specified $E,W,M$', 'with these $E,W,M$')

log('D22',item(old31,1)+item(old33,1)+item(k3,7),
    owners[owners.index(r'\begin{lemma}[Elliptic fibrations on minimal'):owners.index(r'\begin{lemma}[Canonical characters')],
    'The receiving comparison exposed an implicit identification of relatively minimal and absolute minimal elliptic models at nonnegative Kodaira dimension. The same CS5 intersection proof makes all curves of the minimal contraction vertical; relative minimality excludes its first exceptional (-1)-curve, so the contraction is an isomorphism. The exact identification is now proved once in P318 and used in each consumer.', 'lem:II:elliptic-minimal-descent')
new33=edit(new33,
    r'\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)',
    r'\left(\begin{smallmatrix}a_\gamma&b_\gamma\\c_\gamma&d_\gamma\end{smallmatrix}\right)',
    'D20','Keeps the monodromy-matrix entries distinct from the order d of the local cyclic stabilizer.',owner33)
new33=edit(new33,r'$(c\tau+d)(m\tau+n)$; the uniformizing deck multiplier is $(c\tau+d)^{-1}$',
    r'$(c_\gamma\tau+d_\gamma)(m\tau+n)$; the uniformizing deck multiplier is $(c_\gamma\tau+d_\gamma)^{-1}$',
    'D20','Carries the specified monodromy-matrix entry names through the period and deck maps.',owner33)
new33=edit(new33,r'''therefore these are the fibre types of the actual
quotient. Their Euler numbers are $12r/d$.''',
    r'''therefore these are the fibre types of the quotient.''',
    'D12','The discriminant and Euler calculation immediately above already gives 12r/d. Keeps the complete birational-graph and relatively minimal model comparison once.',owner33)
newk=edit(newk,r'''nontrivial symplectic automorphisms.
The generator has no eigenvalue one on the tangent space
and, after a translation of the origin,''',
    r'''nontrivial symplectic automorphisms whose generator has no eigenvalue one on the tangent space.
After a translation of the origin, the generator''',
    'D22','Places the existing no-eigenvalue-one requirement in the exact quotient criterion, retaining its full old conjunction. The proof supplies the conjugating translation through the isogeny I−L.',ownerk)
newk=edit(newk,r'''\item In the other cases, \ref{cdp:st:C.2.UN.22} and \ref{cdp:st:C.2.UN.29} give
an actual relatively minimal elliptic map''',
    r'''\item In the non-torus cases, \cref{cdp:st:C.2.UN.22,cdp:st:C.2.UN.29} give a relatively minimal elliptic model. Its Kodaira dimension is nonnegative by \eqref{cdp:eq:C.K3.3}, so \cref{lem:II:elliptic-minimal-descent} makes its minimal contraction an isomorphism. The birational comparison with the unique minimal model $E_0$ is therefore an isomorphism, giving the elliptic map''',
    'D22','Identifies the relatively minimal elliptic surface with E0 by the exact minimal-contraction consequence of P318, using the already proved nonnegative Kodaira bound. This supplies the morphism needed before carrying G and the canonical form to q:E0→B.',ownerk)
newk=edit(newk,r'''Algebraic dimension zero was
already the torus branch of \ref{cdp:st:C.2.UN.16}.''',
    r'''In algebraic dimension zero, the limiting field space on the covering component $E$ has generic rank two: two complex-linearly independent fields of generic rank one would satisfy $V_2=hV_1$ with a nonconstant meromorphic function $h$, contrary to $a(E)=0$. The algebraic-dimension-zero branch of \cref{cdp:st:C.2.UN.22} therefore makes its minimal model $E_0$ a torus.''',
    'D04','UN16 constructs the limiting fields; UN22 is the proved rank-two torus classification. The exact field-ratio argument supplies the required rank hypothesis before applying its algebraic-dimension-zero branch.',ownerk)
newk=edit(newk,r'''For a quotient of algebraic dimension one, then $a(A)=1$ as well.''',
    r'''For a quotient of algebraic dimension one, $a(A)=1$ as well.''',
    'D08','Removes the dangling connective introduced by the new proof-item boundary; the finite-quotient algebraic-dimension identity is unchanged.',ownerk)
new31=edit(new31,r'''give precisely the asserted torus or smooth-multiple
elliptic alternatives and coherent Euler characteristic
zero.''',
    r'''give the torus or relatively minimal smooth-multiple elliptic alternatives and coherent Euler characteristic zero. In the latter branch, \eqref{cdp:eq:C.CS.2} and \cref{lem:II:elliptic-minimal-descent} make the minimal contraction an isomorphism. Its birational comparison with the unique smooth minimal model $E_0$ is therefore an isomorphism, so the elliptic map is defined on this same $E_0$.''',
    'D22','Identifies the relatively minimal elliptic model of UN22/UN29 with E0 through the exact isomorphism proved in P318, before applying the full-base cohomology and equivariant minimal-model clauses.',owner31)

parts=[('owners',owners,'lem:II:local-cyclic-elliptic'),('new33',new33,owner33),('newk',newk,ownerk),('new31',new31,owner31)]
clean={}
for name,s,owner in parts:
    for m in list(re.finditer(r'\bactual\s+',s))[::-1]:
        a=max(s.rfind('\n\n',0,m.start())+2,0)
        b=s.find('\n\n',m.end())
        if b<0:b=len(s)
        before=s[a:b]
        after=before[:m.start()-a]+before[m.end()-a:]
        after=re.sub(r'\b([Aa])n(\s+)(?=(?:generically|rational|relatively|base-point-free|holomorphic|meromorphic)\b)',r'\1\2',after)
        s=s[:a]+after+s[b:]
        log('D08',before,after,'Names the graph, Jacobian, fibration, quotient, finite map or blowup directly; its complete mathematical construction and domain remain.',owner)
    clean[name]=s
owners,new33,newk,new31=(clean[x] for x in ['owners','new33','newk','new31'])

with (root/'agents/continuation2_B/D19/S6_SERIES_PUBLISH_II_B2_D19_v1_equation_map.tsv').open() as f:
    established={r['old_tag']:r['target_label'] for r in csv.DictReader(f,delimiter='\t') if r['old_tag']}

def literal_refs(s, owner):
    for m in list(re.finditer(r'\((C\.[A-Za-z0-9.]+)\)',s))[::-1]:
        tag=m.group(1)
        assert tag in established,tag
        a=max(s.rfind('\n\n',0,m.start())+2,0)
        b=s.find('\n\n',m.end())
        if b<0:b=len(s)
        before=s[a:b]
        after=before[:m.start()-a]+r'\eqref{'+established[tag]+'}'+before[m.end()-a:]
        s=s[:a]+after+s[b:]
        log('D04',before,after,'Replaces the inherited literal equation number with its preserved reader target from the established D19 map.',owner)
    return s
new33=literal_refs(new33,owner33)
newk=literal_refs(newk,ownerk)
new31=literal_refs(new31,owner31)

old_displays={lab:m.group() for m in re.finditer(r'\\\[.*?\\\]',old+oldk,re.S)
              for lab in re.findall(r'\\label\{([^}]+)\}',m.group())}
eq=[]
def number(s, owner):
    def convert(m):
        a=m.group()
        tags=re.findall(r'\\tag\{([^}]+)\}',a)
        if not tags:return a
        assert len(tags)==1,tags
        labs=re.findall(r'\\label\{([^}]+)\}',a)
        lab=labs[0]
        assert established[tags[0]]==lab,(tags,lab)
        b=a.replace(r'\[',r'\begin{equation}',1)
        b=b[:-2]+r'\end{equation}'
        b=b.replace(r'\tag{'+tags[0]+'}','')
        log('D19',old_displays[lab],b,'Uses the section equation counter while preserving the formula and every permanent target. KX4 is the explicitly conjugated same-counter root-chart alias when present.',lab)
        eq.append(dict(old_tag=tags[0],target_label=lab,statement_id=owner))
        return b
    return re.sub(r'\\\[.*?\\\]',convert,s,flags=re.S)
owners=number(owners,'P317 / P318 / P319')
new33=number(new33,owner33)
newk=number(newk,ownerk)
new31=number(new31,owner31)
eq.append(dict(old_tag='C.KX.4',target_label='cdp:eq:C.KX.4',statement_id='lem:II:local-cyclic-elliptic'))
log('D19',old_displays['cdp:eq:C.KX.4'],
    next(m.group() for m in re.finditer(r'\\begin\{equation\}.*?\\end\{equation\}',owners,re.S) if r'\label{cdp:eq:C.KX.4}' in m.group()),
    'KX4 keeps its permanent tag and label as an alias of EQ3. The text proves their product-permutation conjugacy, including t, the deck map and the finite étale projection; no second numbered formula or proof remains.', 'cdp:eq:C.KX.4')

def clean_spacing(s):
    return re.sub(r'\n{4,}','\n\n\n',s).rstrip()+'\n\n'
owners,new33,newk,new31=(clean_spacing(s) for s in [owners,new33,newk,new31])
work=owners+new33+newk+new31
log('D14',old.split('\n\n',1)[0],owners.split('\n\n',1)[0],
    'Preserves the stable cyclic-component-models heading identity and places the three proved common constructions before all consumers. UN33 receives the elliptic-configuration-list subsection; UN31 follows the full K3 result as nonnegative-component-covers.', 'subsec:II:cyclic-component-models')
log('D14',oldk,newk,
    'Moves the complete K3 subsection, with both statement identities UN24/UN32 and every formula target, from its later position to immediately before UN31. All proof transfers have exact owners P317–P319 or already admitted earlier results. The distant old section is removed only by its full exact guard; no material in the following ruled-leaves subsection is touched.', 'subsec:II:k3-cyclic-components')

def payload(s):
    s=re.sub(r'\\SsixEquationAliases\{(?:\\label\{[^}]+\})+\}','',s)
    s=re.sub(r'\\tag\{[^}]+\}|\\label\{[^}]+\}|\\hypertarget\{[^}]+\}\{\}','',s)
    for x in [r'\[',r'\]',r'\begin{equation}',r'\end{equation}']:s=s.replace(x,'')
    return re.sub(r'\s+','',s)
new_displays={lab:m.group() for m in re.finditer(r'\\\[.*?\\\]|\\begin\{equation\}.*?\\end\{equation\}',work,re.S)
              for lab in re.findall(r'\\label\{([^}]+)\}',m.group())}
allowed_changed={'cdp:eq:C.KX.4'}
for lab,d in old_displays.items():
    if lab not in allowed_changed:assert payload(d)==payload(new_displays[lab]),(lab,payload(d),payload(new_displays[lab]))
for kind in ['label','hypertarget']:
    pattern=r'\\'+kind+r'\{([^}]+)\}'
    before=Counter(re.findall(pattern,old+oldk))
    after=Counter(re.findall(pattern,work))
    assert all(after[k]==v for k,v in before.items()),(kind,before-after)
    assert max(after.values())==1,(kind,[k for k,v in after.items() if v>1])
for s in [owners,new33,newk,new31,work]:
    assert Counter(re.findall(r'\\begin\{([^}]+)\}',s))==Counter(re.findall(r'\\end\{([^}]+)\}',s))
    assert not re.search(r'\\tag\{|night:P4R\.13|night:P4\.40|\r|\\path\{|\\textbf\{|\(C\.',s)
assert len(old_displays)==41,len(old_displays)
assert len(eq)==41,len(eq)
assert len(re.findall(r'\\begin\{equation\}',work))==40
for lab in ['lem:II:local-cyclic-elliptic','lem:II:elliptic-minimal-descent','lem:II:elliptic-canonical-character']:
    assert work.index(r'\label{'+lab+'}') < work.index(r'\label{cdp:st:C.2.UN.33}')
assert work.index(r'\label{cdp:st:C.2.UN.33}') < work.index(r'\label{cdp:st:C.2.UN.32}') < work.index(r'\label{cdp:st:C.2.UN.31}')

def tsv(suffix,fields,data):
    with (out/(prefix+suffix)).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n')
        w.writeheader();w.writerows(data)

(out/(prefix+'_replacement.tex')).write_text(work,newline='\n')
(out/(prefix+'_shared_owners.tex')).write_text(owners,newline='\n')
(out/(prefix+'_UN33_replacement.tex')).write_text(new33,newline='\n')
(out/(prefix+'_K3_replacement.tex')).write_text(newk,newline='\n')
(out/(prefix+'_UN31_replacement.tex')).write_text(new31,newline='\n')
starts=[owners.index(r'\begin{lemma}')]
starts.extend(m.start() for m in re.finditer(r'\\begin\{lemma\}',owners) if m.start()!=starts[0])
for i,tag in enumerate(['P317','P318','P319']):
    end=starts[i+1] if i+1<len(starts) else len(owners)
    (out/(prefix+'_'+tag+'.tex')).write_text(owners[starts[i]:end],newline='\n')
with (root/'S6_SERIES_PUBLISH_defects_II.tsv').open() as f:fields=next(csv.reader(f,delimiter='\t'))
tsv('_defects.tsv',fields,rows)
tsv('_equations.tsv',['old_tag','target_label','statement_id'],eq)
tsv('_remote_repairs.tsv',['statement_id','old_text','new_text','reason'],[
    dict(statement_id='cdp:st:C.2.UN.24 / cdp:st:C.2.UN.32',
         old_text=oldk,new_text='',
         reason='Remove this complete exact old K3 subsection after inserting its complete receiving form in the main11 replacement, before UN31. Both statement labels/tags and all K3/KX equation identities are preserved there or at the exact common P317/P318/P319 owners. The following ruled-leaves subsection is outside this guard.')])

transfers=[
    dict(old_owner='UN33 items2–7; UN32 items8,10,13–14',new_owner='P317 / lem:II:local-cyclic-elliptic',
         conclusion='Root products, finite translation quotients with full multiplicities, faithful stabilizer multiplicity obstruction, beta=1 reflections and primitive product actions',
         map='t=z^m; v↦v+b(z) with weighted sum; (u,w)↦(v=w,z=u) conjugates KX4 and EQ3; F′→F′/T and w=z^(m/m′); gtilde root lift, beta tau=tau and fixed-point lift; Pb=beta^{-1}b(zeta_s z), c=−beta^{-1}a; Q base quotient T=t^s'),
    dict(old_owner='UN31 item6; UN32 item6',new_owner='P318 / lem:II:elliptic-minimal-descent',
         conclusion='An elliptic fibration on a smooth birational model descends to a minimal compact complex surface of kappa≥0, with coherent H1 base injection',
         map='Z←rho X→q C; CS5 nonnegative canonical intersection; connected rho fibres and rho_*O=O; q=p rho; p_*O=O'),
    dict(old_owner='UN32 item12; UN33 item11',new_owner='P319 / lem:II:elliptic-canonical-character',
         conclusion='Elliptic-base canonical generator, precise multiple-fibre zero divisor, lambda beta character and quotient-invariant pullback',
         map='omega_B∧dz=m c(u^m)u^(m−1)du∧dz under the étale root; E←mu W→pi M generic Jacobian and point-blowup/Hartogs map'),
    dict(old_owner='UN33',new_owner='UN33 before the K3 and global cover classifications',
         conclusion='All eleven positive coherent-Euler fibre configurations, zero-Euler smooth-multiple case and all stated genera',
         map='P240 E′→Snu and E/G→M; P318 minimal descent; P317(E,q,G) with H proved translation; invariant Weierstrass functions and degree-d fixed-field equality; positive-loop endpoint (v,zeta z)~(zeta^{-r}v,z); full cyclic base character tables; P319 on E1 and Noether'),
    dict(old_owner='UN24/UN32 complete later K3 subsection',new_owner='UN24/UN32 in k3-cyclic-components before UN31',
         conclusion='All-algebraic-dimensions cyclic symplectic torus quotient classification, exact cyclic configurations, positive-algebraic-dimension pencils and compact realizations',
         map='P240 E→Snu and E0/G→M; P306 q:E0→B; P317 E1=E0/H,Q=G/H; P319 lambda beta=1; P318 K3 descent; Chern-vector cocycle and explicit C² lattice; fixed-point isogenies, toric quotient charts, four-square isotropic class; (A×P1)/cyclic and UN4 vertical Euler adjustments'),
    dict(old_owner='UN31 items4–5',new_owner='UN29 final original-component proof; UN31 exact application',
         conclusion='Equivariant isotrivial Iitaka quotient with base genus≤1 and fixed general quotient elliptic curve',
         map='Same E0,q,G and equivariant graph E′; E′/G→B/G; K=ker base action, F/K and A/K; P318 to Z'),
    dict(old_owner='UN31 K3 items9–10',new_owner='UN24/UN32 complete earlier owner; UN31 application',
         conclusion='Every K3 component has the exact cyclic torus quotient classification; the non-torus-cover branch also has its isotrivial P1 pencil',
         map='A=E0 or E0/H; (E0/H)/(G/H)=E0/G; same CS3 quotient comparison and K3.5 descent'),
    dict(old_owner='Repeated symmetric-function and equivariant contraction paragraphs in UN31/UN32',
         new_owner='P240 / lem:II:cyclic-component-cover',
         conclusion='Preserved algebraic dimensions and descended finite cyclic actions on nonruled minimal models',
         map='Each application names E→Snu, its finite generic sheets, the birational target M or Z, and E/G→E0/G from HQ2–3')
]
tsv('_owner_transfers.tsv',['old_owner','new_owner','conclusion','map'],transfers)

with (root/'CHECK_EVENTS.tsv').open() as f: event_fields=next(csv.reader(f,delimiter='\t'))
now=datetime.now(timezone.utc)
scopes=[
('lem:II:local-cyclic-elliptic','P317','subsec:II:cyclic-component-models',
 'Read all original UN33 items2–7 and UN24/UN32 items8,10,13–14 within their complete proofs, and the complete receiving P317 statement/proof. Compared the proper compact analytic relatively minimal identity-H1 scope; finite cyclic equivariance; the proved translation hypothesis on the base kernel; normalized étale root charts; weighted translation gauge; explicit base-first/fibre-first product permutation; quotient by constant torsion translations and pure normal rotations; full fibre multiplicities; faithful base stabilizer; root lift and deck commutation; beta tau=tau, m|s and gcd(m,s)=1; beta=1 reflection coordinates; twisted averaging operator and primitive product character. Every local quotient map retains its base function. EQ3/KX4 share one counter only after the product-permutation conjugacy is proved.'),
('lem:II:elliptic-minimal-descent','P318','subsec:II:cyclic-component-models',
 'Read the complete original UN31 and UN24/UN32 proofs and receiving P318. Compared the minimal compact surface of nonnegative Kodaira dimension, the proper birational map rho and connected elliptic map q. Peters Proposition2.1 p.8 supplies nef K on precisely this domain. The full point-blowup Jacobian coefficients, nonnegative CS5 intersections, connected exceptional-fibre descent through rho_*O=O and coherent Leray injection remain. The same proof now explicitly identifies a relatively minimal elliptic surface of nonnegative Kodaira dimension with its minimal model: every contraction curve is vertical, so a first exceptional (-1)-curve contradicts relative minimality. The exact isomorphism is applied in UN33, UN24/UN32 and UN31.'),
('lem:II:elliptic-canonical-character','P319','subsec:II:cyclic-component-models',
 'Read the complete original canonical-form arguments in UN24/UN32 and UN33 and the receiving P319. Compared the elliptic-base restriction, normalized-period charts, gluing of omega_B wedge dz, the étale root zero order m−1 and its invariant descent, the one-dimensional canonical space from P306, the lambda beta group character and the injective quotient-graph Jacobian pullback. The group action on both E and B is expressly named. KX7 retains its original formula and permanent target.'),
('cdp:st:C.2.UN.33','UN33','subsec:II:elliptic-configuration-list',
 'Read the complete original and receiving statement/proof. Preserved all eleven configurations, full smooth-multiple qualifications, genus bounds and all EQ table payloads. The cover E′→Snu, G, minimal contraction, quotient graph and P318 descent are named. The base kernel is proved translation before P317 is applied to the same E,q,G. The invariant Weierstrass field is identified by adjoining z and comparing its degree with the faithful cyclic fixed-field degree. The positive-loop endpoint (v,zeta_d z)~(zeta_d^{-r}v,z) is compared with the opened Ulmer–Urzúa row-cycle/uniformizing-deck conventions. All rational and elliptic base actions, branch indices, primitive character reductions, Euler sums, P319 canonical character and the complete vertical canonical/adjunction/Noether calculation remain. The source reading covers the exact finite-monodromy table and the complete displayed quotient calculations, not an independently executed program.'),
('cdp:st:C.2.UN.32','UN32','subsec:II:k3-cyclic-components',
 'Read the complete original combined UN24/UN32 subsection and complete receiving combined statement/proof, including every rank and algebraic-dimension branch. Compared P240 finite fields and equivariant minimal contractions; graph canonical pullback; finite-base-change pg≤1; intrinsic algebraic-reduction/Iitaka maps; P318 minimal descent and relative-minimal isomorphism; P306 genus; P317 full root/translation quotient and stabilizer applications; P319 invariant K3 character; free-orbit multiplicity-one argument; complete Chern-vector cocycle and Dolbeault-to-lattice quotient; characteristic polynomial, fixed-point isogenies, exact stabilizer orbits, toric chains and Euler corrections; projective four-square isotropic class, precise published pencil criterion, algebraic-dimension-one current/pencil construction and all compact quotient/resolution/vertical-Euler realizations. The no-eigenvalue-one requirement remains part of the same original conjunction, now placed directly in the quotient criterion. Algebraic dimension zero uses the explicit ratio V2=hV1 on the covering component to establish rank two before UN22. No field is silently transported to E0. The complete subsection moves before UN31 under a full distant-removal guard.'),
('cdp:st:C.2.UN.24','UN24','subsec:II:k3-cyclic-components',
 'This permanent statement identity belongs to the same combined UN24/UN32 theorem and proof just completely compared. Its tag01D2, statement label, every conclusion and exact cyclic quotient/elliptic-pencil/compact-realization construction are preserved in that one owner. This event records the second existing statement identity for the single exposed full reading; it is not another independent proof or another separate proof reading.'),
('cdp:st:C.2.UN.31','UN31','subsec:II:nonnegative-component-covers',
 'Read the complete original and receiving statement/proof. Compared every cover and original-component conclusion. P240 supplies the same E→Snu, cyclic G and HQ2/HQ3 quotient square; pluricanonical pullback gives kappa(E)≥kappa(Z); UN15 and both field-rank branches give the complete alternatives. P318 proves the precise relatively-minimal-to-minimal isomorphism before P306 cohomology and UN28 finite-base-change genus. The kappa-one Iitaka quotient reuses the complete UN29 proof with the same E0,q,G,E′,K and fixed A/K. Preserved the complete bielliptic product, connected-automorphism orbit map and equivariance proof; even pluricanonical restriction excludes rational quotient fibres in the Enriques branch. P318 descends both elliptic maps. The earlier complete K3 owner supplies the exact A=E0 or E0/H and quotient equality, retaining the additional non-torus-branch P1 pencil. The kappa-zero classification and preceding UN33 give the same coherent Euler range. CS1–6 remain, with CS5 at its single common owner.')
]
events=[]
for lab,short,unit,scope in scopes:
    e={k:'' for k in event_fields}
    e.update(statement_id=lab,date=now.date().isoformat(),date_utc=now.isoformat(),
        who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 conductor agent',
        type='used and rechecked in this run',
        outcome=scope+' Exposed editorial rereading only; no independent proof or computational execution credit. All41 original equation identities and every original label/target are preserved; 40 formula payloads are unchanged and the remaining KX4 chart has its explicit product-permutation alias. No use of refined night:P4R.13 or night:P4.40 occurs in these fragments. Source-wide placement and final integrated PDF reading remain open.',
        event_id='publish:c3:conductor11:'+short,phase='publication editorial comparison',
        source_file='agents/continuation3_conductor/'+prefix+'_replacement.tex',
        source_event_type='used and rechecked in this run',evidence_group='publish:c3:conductor11:cyclic-component-models',where=unit)
    events.append(e)
tsv('_CHECK_EVENTS.tsv',event_fields,events)

units=[
('subsec:II:cyclic-component-models','Cyclic quotients of smooth multiple elliptic fibres','P317/P318/P319'),
('subsec:II:elliptic-configuration-list','Elliptic fibre configurations of component surfaces','UN33'),
('subsec:II:k3-cyclic-components','K3 components and cyclic quotients','UN24/UN32'),
('subsec:II:nonnegative-component-covers','Minimal models of cyclic component covers','UN31')]
status=[]
for unit,title,scope in units:
    for n in range(1,26):
        state='done'
        reason='Complete original and receiving '+scope+' statements/proofs read and compared; every local instance found is recorded. This row concerns the actual subsection, with its exact shared-owner and application maps.'
        if n in [10,16]:reason='The prior done status remains: hidden statement records and all permanent targets are preserved, and every numbered statement has its mathematical title.'
        if n==12:reason='Local repeated proofs have one earlier proved owner with exact maps and hypothesis comparisons; all complete specialized calculations and conclusions remain. Other unreviewed units are not given closure by this row.'
        if n==14:
            state='open';reason='Local dependency order completed: P317–P319, then UN33, complete UN24/UN32, then UN31. Final whole-paper placement and proportion remain open.'
        if n==17:reason='The precise classification, finite-monodromy and pencil loci were opened before citation. The local root, character, Chern-vector, lattice and compact-realization constructions retain proofs in the exact analytic domains required here.'
        if n==18:
            state='open';reason='Exact edited source loci and versions are recorded; no new bibliography metadata replacement is needed. The bibliography-wide pass remains separate, and program157 is a separate pending appendix guard.'
        if n==19:reason='All inherited equation identities use the section counter. EQ3/KX4 have one explicitly conjugated owner and both permanent reader targets; old-tag-to-label map supplied.'
        if n==23:
            state='open';reason='Source wording, articles and accents corrected. Final integrated typesetting and page reading remain open.'
        if n==24:reason='This body subsection makes no unmatched front-matter promise. The whole-paper organization description is outside this bounded replacement and remains part of final integration.'
        if n==25:reason='Every original and receiving inference was read in context, including the exact quotient, contraction and field-ratio maps. No theorem conclusion is weakened or left conditional; the added explanations prove the receiving identifications.'
        status.append(dict(unit=unit,title=title,criterion=f'D{n:02d}',status=state,reason=reason))
    status.append(dict(unit=unit,title=title,criterion='structure',status='open',reason='Local one-owner consolidation and dependency order completed for this actual subsection; final whole-paper placement remains open. The complete distant K3 source is removed only through its exact guard.'))
tsv('_unit_status.tsv',['unit','title','criterion','status','reason'],status)

sources=[
dict(source_id='Peters1990:conductor11',url='https://cpeters1.win.tue.nl/ConfsAndSchools/Canada/surface.pdf',version='35-page author notes; 1990 proceedings metadata and author-draft layout identified by admitted bibliography156',exact_locus='Chapter1 Proposition2.1 and complete proof p.8; §3 definitions p.9, Theorem3.1 and Corollary3.2 p.10; pp.5–6 Noether formula reused from09',sha256='51f9c99621b3819aa85894a8cdee4a528b0894364fc22b40a651f1bae55ceed3',bytes='255331',own_paraphrase='Nef canonical class on a compact minimal surface of nonnegative Kodaira dimension; the compact surface classes and the explicit finite product description of bielliptic surfaces. P318 proves the exact birational elliptic descent and relative-minimal isomorphism using that nef input. The complete p.9 product definition was reopened during the final receiving comparison.',reader='continuation3 conductor; exact pp.8–10 reopened in11; Noether locus read in09 and reused',date_utc=now.isoformat(),storage='/tmp/S6_SERIES_PUBLISH_c3_conductor_primary/Peters1990.pdf; outside checkpoint.'),
dict(source_id='UlmerUrzua2021:conductor11',url='https://arxiv.org/pdf/2002.01906v2',version='arXiv2002.01906v2; margin26May2020 and author Date27May2020; 24-page layout',exact_locus='§2.1 full uniformization pp.3–4; §2.2 p.5; §2.3 positive-loop convention and complete matrix/period/Hodge-generator table pp.5–6',sha256='a35bde9428a00cf693863648138a05a9176942d74a692bc8ee8cce6966ec9dd6',bytes='305467',own_paraphrase='The row-cycle matrix acts on m tau+n through c tau+d, whereas the uniformizing deck factor is its inverse. The receiving positive-loop endpoint comparison gives beta inverse and matches the starred and unstarred finite-order rows. Complete text reopened in11; the p.6 image reading belongs to10.',reader='continuation3 conductor; full exact text reopened in11; no new page-image or program execution claim',date_utc=now.isoformat(),storage='/tmp/S6_SERIES_PUBLISH_c3_conductor_primary/UlmerUrzua2021_arxiv_v2.pdf; outside checkpoint.'),
dict(source_id='Kodaira1963II:conductor11',url='https://www.jstor.org/stable/1970131',version='Annals of Mathematics77(3),1963,563–626; original published text',exact_locus='Theorem6.2 full statement pp.564–566, with proper analytic setup pp.563–564; exact source reading already recorded in10',sha256='',bytes='',own_paraphrase='The proper analytic relatively minimal elliptic classification supplies the fibre configurations used after the explicit invariant Weierstrass and positive-loop comparisons. The full classification proof was not read. The exact published-text source reading and scan-reproduction locator are recorded in10; this row records its bounded reuse.',reader='continuation3 conductor; reused exact published-statement reading from10',date_utc=now.isoformat(),storage='No copied published source in checkpoint; no successful primary PDF byte hash claimed.'),
dict(source_id='Roulleau2019GeneralizedKummer:conductor11',url='https://www.i2m.univ-amu.fr/perso/xavier.roulleau/Site_Pro_English/Publications_files/Roulleau%2C%20On%20generalized%20kummer%20surfaces%20and%20the%20orbifold%20Bogomolov-Miyaoka-Yau%20inequality.pdf',version='Published TransAMS371(11),2019,7651–7668; author-hosted published offprint; DOI10.1090/tran/7507',exact_locus='Front matter; full §3.1 pp.7657–7659 including translation-kernel Lemma14 and cyclic rows; full §4.1 Theorem27 p.7663',sha256='765e0498e7e477ae0ecb53341862e208f0668e86a12f37e2264af5f9c4e63150',bytes='287850',own_paraphrase='The generalized Kummer list includes the four cyclic configurations in K3.1, and the configuration criterion is stated on p.7663. The receiving proof retains its exact cyclic fixed-point isogenies, stabilizer counts, toric singularities and quotient Euler calculation for the component action.',reader='continuation3 conductor; exact complete loci freshly opened in11',date_utc=now.isoformat(),storage='/tmp/S6_SERIES_PUBLISH_c3_conductor_primary/Roulleau2019_published.pdf; outside checkpoint.'),
dict(source_id='Lagrange1770:conductor11',url='https://fr.wikisource.org/wiki/M%C3%A9moires_extraits_des_recueils_de_l%E2%80%99Acad%C3%A9mie_royale_de_Berlin/D%C3%A9monstration_d%E2%80%99un_Th%C3%A9or%C3%A8me_d%E2%80%99Arithm%C3%A9tique',version='Original public-domain text in ŒuvresIII,1868,pp.189–201; original-text transcription',exact_locus='Complete TheoremII argument and CorollariesI–II; four-square consequence in CorollaryII, printed p.201; original page-index202 mapping checked',sha256='',bytes='',own_paraphrase='CorollaryII concludes that every positive integer is a sum of four integer squares. Applying it to ab and dividing each square root by b gives the positive rational a/b representation used for H′²/2. The primary facsimile download was blocked; this reading is the original-text transcription, not a claimed facsimile-image reading.',reader='continuation3 conductor; full original transcription read in11',date_utc=now.isoformat(),storage='No downloaded PDF, page image or byte hash; no copied source in checkpoint. Page locator https://fr.wikisource.org/wiki/Page:Joseph_Louis_de_Lagrange_-_%C5%92uvres,_Tome_3.djvu/202 .'),
dict(source_id='PiatetskiShapiroShafarevich1971:conductor11',url='https://www.mathnet.ru/eng/im2021',version='Published English translation, MathUSSR-Izv5(3),1971,547–588; DOI10.1070/IM1971v005n03ABEH001075',exact_locus='§3 setup p.558; Theorem1 full proof pp.559–560; Corollaries1–3 and complete Corollary3 proof p.560; §6 Theorem1 statement and full reflection proof pp.573–574, especially item(3), and its corollary',sha256='',bytes='',own_paraphrase='A nonzero integral isotropic class on the projective K3 surface gives an elliptic pencil after reflection to the nef cone; the proof decreases intersection with a positive class until the nef representative is reached. The receiving H′ and four-square construction gives precisely the nonzero integral isotropic input. The read source was the primary MathNet English PDF text viewer; no page-image or downloaded-byte verification is claimed.',reader='continuation3 conductor; exact full primary text loci freshly opened in11',date_utc=now.isoformat(),storage='Primary PDF text locator https://www.mathnet.ru/links/711689cb08d7b4d4498cc58378ffc9ce/im2021_eng.pdf ; no copied source in checkpoint, no downloaded bytes or hash.')
]
tsv('_sources.tsv',['source_id','url','version','exact_locus','sha256','bytes','own_paraphrase','reader','date_utc','storage'],sources)

print('11 READY:',len(rows),'defects;7 exposed identity events for6 proved owners;41 old equation identities;40 numbered equations;40 unchanged old payloads and one proved product-permutation alias;8 owner maps;104 unit-status rows;6 source rows.')
print('P317–P319 only new tags. Full main replacement plus complete distant K3 removal guard; all old labels/targets preserved; LF; no central writes. Final whole-paper placement and rendering remain open.')
