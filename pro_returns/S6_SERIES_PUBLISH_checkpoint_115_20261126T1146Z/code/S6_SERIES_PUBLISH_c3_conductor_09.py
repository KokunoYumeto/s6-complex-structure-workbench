#!/usr/bin/env python3
"""Prepare shared compact-core transport and its two full applications. No central writes."""
from pathlib import Path
from collections import Counter
from datetime import datetime,timezone
import csv,re

root=Path(__file__).resolve().parents[1]
out=root/'agents/continuation3_conductor'
prefix='S6_SERIES_PUBLISH_c3_conductor_09'
old=(out/(prefix+'_input.tex')).read_text()
old36=(out/(prefix+'_UN36_input.tex')).read_text()
work=old
remote=old36
rows=[]
transfers=[]
ident='cdp:st:C.2.UN.28'

def log(kind,a,b,reason,owner=None):
    rows.append(dict(change_id=f'II-C3-UNRESTRICTED09-{len(rows)+1:04d}',type=kind,statement_id=owner or ident,old_location='UN.28 / UN.36; exact bounded source span',old_page='cp35 PDF omitted; exact source span supplied',new_location='compact-component-core or component-invariant-lattice subsection',new_page='pending integrated final PDF',old_text=a,new_text=b,reason=reason,review_status='Complete original and receiving statements/proofs read and compared; exposed editorial rereading; final PDF reading remains open.'))

def replace(a,b,kind,reason,which='main'):
    global work,remote
    text=work if which=='main' else remote
    assert text.count(a)==1,(which,a[:100],text.count(a))
    text=text.replace(a,b,1)
    if which=='main':work=text
    else:remote=text
    log(kind,a,b,reason)

def item(text,n):
    begin=text.index(r'\begin{enumerate}')
    starts=[m.start() for m in re.finditer(r'\\item\b',text[begin:])]
    starts=[begin+x for x in starts]
    end=starts[n] if n<len(starts) else text.index(r'\end{enumerate}',starts[n-1])
    return text[starts[n-1]:end]

owner=r'''\begin{lemma}[Compact cycles in smooth component loci]\hypertarget{tag-P305}{}\label{lem:II:compact-component-transport}
\StatementRecord{lem:II:compact-component-transport}{proved}{P305}{\cref{lem:II:cyclic-component-cover}; \cite[Theorem~3.44, pp.~254--255]{Hatcher2002}}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item Let $E$ be a smooth compact complex surface and $D\subset E$ a reduced compact analytic set of dimension at most one. Under Poincar\'e--Alexander duality, the map
$H_2(E,\Z)\to H_2(E,E\setminus D;\Z)\simeq H^2(D,\Z)$
is the vector of intersection numbers with the curve components of $D$. The target is free, with one generator for each such curve, and the kernel is the image of $H_2(E\setminus D,\Z)$. With real coefficients the same maps give
\[
 H_2(E\setminus D,\mathbb R)\longrightarrow
 H_2(E,\mathbb R)\xrightarrow{\ I_D\ }
 H_2(E,E\setminus D;\mathbb R)
       \simeq H^2(D,\mathbb R).
                                                               \tag{C.PG.6}\hypertarget{tag-00V4}{}\label{cdp:eq:C.PG.6}
\]
The holomorphic two-forms determine
\[
 P_E=\{[\operatorname{Re}\alpha]:
                       \alpha\in H^0(E,K_E)\}
       \subset H^2(E,\mathbb R),
 \qquad \dim_{\mathbb R}P_E=2p_g(E).
                                                               \tag{C.PG.7}\hypertarget{tag-00V5}{}\label{cdp:eq:C.PG.7}
\]
This subspace is positive definite for the intersection form. Its Poincar\'e-dual homology classes lie in $\ker I_D$.

\item Let $f:U\to\Delta_t$ be proper and holomorphic, with $U$ a smooth complex threefold and with connected smooth two-torus fibres over $\Delta_t^*$. Write $f^{-1}(0)=\sum_i m_iS_i$ and $S=\bigcup_iS_i$. For a positive integer $N$ divisible by every $m_i$, normalize the base change $t=s^N$ and resolve its total space and central support. The resulting proper map
\[
                         g:\widetilde U\to\Delta_s
                                                               \tag{C.PG.2}\hypertarget{tag-00V0}{}\label{cdp:eq:C.PG.2}
\]
can be chosen unchanged over the punctured disc and over the normalized inverse image of every $S_i\setminus\operatorname{Sing}S$. Its nearby fibre is $f^{-1}(s^N)$. The strict components above $S_i$ have multiplicity one, and their union restricts over $S_i\setminus\operatorname{Sing}S$ to a finite \'etale cover of total degree $m_i$, possibly disconnected.

\item On any smooth resolved finite-base-change model of this family, choose finitely many compact finite smooth singular two-cycles in the smooth single-component loci of multiplicity-one components. Include compact transverse perturbations used to compute their intersection numbers. After shrinking the base disc, there are simultaneous smooth embeddings of neighbourhoods of these compact sets into each fibre, preserving the complex orientation and all these intersection numbers. Neighbourhoods belonging to different components have disjoint images. The transported cycles form continuous families over the whole small disc, and their classes on a nearby fibre are invariant under its monodromy.
\end{enumerate}
\end{lemma}
\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item The compact analytic set $D$ is triangulable and locally contractible. Apply \cite[Theorem~3.44, pp.~254--255]{Hatcher2002} with $M=E$, $K=D$ and real dimension four. The source theorem identifies relative homology with cohomology of $D$ by cap product with the orientation class. In its naturality diagram, $H_2(E,\Z)\to H_2(E,E\setminus D;\Z)$ corresponds to restriction of $H^2(E,\Z)$ to $D$. Normalization of the curve part changes only identifications at finitely many points, which leave degree-two cohomology unchanged; isolated points have degree-two cohomology zero. Evaluation on the fundamental class of each normalized curve therefore identifies this restriction with the asserted intersection vector. The relative homology sequence gives its kernel. Tensoring this sequence with $\mathbb R$ gives \eqref{cdp:eq:C.PG.6}.

Every holomorphic two-form $\alpha$ on $E$ is closed: its $(3,0)$ derivative vanishes by dimension and its antiholomorphic derivative vanishes by holomorphicity. With the complex orientation,
\[
 \int_E(\operatorname{Re}\alpha)^2
       =\tfrac12\int_E\alpha\wedge\overline\alpha>0
                      \quad (\alpha\ne0).
                                                               \tag{C.PG.8}\hypertarget{tag-00V6}{}\label{cdp:eq:C.PG.8}
\]
This proves positivity and injectivity of the real-part map on the underlying real vector space of $H^0(E,K_E)$, hence the dimension in \eqref{cdp:eq:C.PG.7}. The pullback of $\alpha$ to the normalization of any curve in $D$ vanishes by dimension. Its real part therefore pairs trivially with each boundary curve, so its Poincar\'e-dual class lifts to the open complement.

\item At a point of $S_i\setminus\operatorname{Sing}S$, write $t=u x^{m_i}$ with $u$ a unit. Factor $t=s^N$ through $t=r^{m_i}$ by $r=s^{N/m_i}$. Substituting this map into the normalized chart \eqref{cdp:eq:C.SC.2} of \cref{lem:II:cyclic-component-cover}, with its coordinate $z$ renamed $x$, gives
\[
       w^{m_i}=u,\qquad x=s^{N/m_i}/w.
                                                               \tag{C.PG.3}\hypertarget{tag-00V1}{}\label{cdp:eq:C.PG.3}
 \hypertarget{tag-00C7}{}\SsixEquationAliases{\label{cdp:eq:C.CL.8}}
\]
At $s=0$ this equation has exactly $m_i$ local unit roots, and its derivative with respect to $w$ is nonzero. Thus the normalized space is smooth there, $s$ is a normal parameter, and the central cover over the indicated open surface is \'etale of total degree $m_i$. Resolve the total space and central support while preserving these smooth normal-crossing open sets and the punctured tube, using the resolution construction of \cref{lem:II:cyclic-component-cover}. The coordinate $s$ continues to have order one on every strict component. The map to the original fibre over $s\ne0$ is the fibre-product projection, identifying it with $f^{-1}(s^N)$.

\item Let $K_j$ contain the finitely many chosen cycles and transverse perturbations in one smooth single-component locus. The map $g$ is a submersion near $K_j$: its local equation is a unit times a defining coordinate of the multiplicity-one component. Choose smooth horizontal lifts of the two real coordinate vector fields on the base. A partition of unity preserves their prescribed images under $dg$. Multiply by a cutoff outside a slightly larger compact neighbourhood and flow successively for the real and imaginary parts of $s$. For all sufficiently small $s$, these trajectories stay where the horizontal equations hold. The composition maps a neighbourhood of $K_j$ in the central component diffeomorphically onto an open subset of $g^{-1}(s)$; the two equations for $dg$ identify this exact fibre. Continuity from $s=0$ preserves the complex orientation.

The finitely many compact sets in distinct components are disjoint and avoid all intersections of central components. Choose disjoint ambient neighbourhoods for them and one small disc on which all the flows are defined and remain in those neighbourhoods. The images stay disjoint. The local diffeomorphisms preserve the signed transverse intersection numbers of the cycles in each component, and cycles from different components have intersection zero.

These two flows define each parametrized finite cycle over the whole small $s$-disc. Along a circle about zero the family returns to the identical parametrized cycle. In a local differentiable trivialization of the proper smooth family over $s\ne0$, its homology class is locally constant. It is therefore fixed by Gauss--Manin transport around that circle. The construction applies to integral chains and, by real linearity, to real cycles.
\end{enumerate}
\end{proof}

'''

heading=r'\subsection{Compact component cores and geometric genus}\label{subsec:II:component-core-genus}'
assert work.count(heading)==1
work=work.replace(heading,heading+'\n\n'+owner,1)
log('D12',item(old,4)+item(old,5)+item(old,7)+item(old,8),owner,'Extracts the common integral complement map, positive two-form subspace, root-chart comparison and simultaneous compact-cycle transport into the proved owner P305. The integral and whole-disc portions also come from UN.36; all exact maps and coefficient domains are retained.','lem:II:compact-component-transport')
transfers.append(dict(old_owner='UN.28 items 1,4–8; UN.36 items 1–3,5,7',new_owner='P305 / lem:II:compact-component-transport',conclusion='Integral complement duality and real specialization; positive two-form subspace; common root chart; simultaneous compact-cycle transport and monodromy invariance',map='M=E,K=D,n=4; tensor with R; t=r^mi,r=s^(N/mi),z=x; local embeddings by the two real horizontal flows'))

replace(r'\StatementRecord{cdp:st:C.2.UN.28}{proved}{01D6}{\SeriesRef{cdp:eq:C.PG.2}, \SeriesRef{cdp:eq:C.PG.6}, \SeriesRef{cdp:eq:C.PG.5}}',r'\StatementRecord{cdp:st:C.2.UN.28}{proved}{01D6}{\cref{lem:II:compact-component-transport}; \eqref{cdp:eq:C.PG.5}}','D14','The nonprinting declaration names the earlier proved common owner and the retained generically finite comparison.')
replace(r'''The assertion has no K\"ahler, Betti-number, reducedness,
or normal-crossing hypothesis. In particular at most
one normalization component in a given fibre has a
nonzero holomorphic two-form, and that component has
geometric genus one.''',r'''At most one normalization component in a given fibre has a nonzero holomorphic two-form, and that component has geometric genus one.''','D02','The general proper analytic hypotheses already state the full scope; the numerical conclusion is retained.')
replace(r'''The same bound holds for any collection of multiplicity-one
components in a smooth resolved finite base change of
this family. The proof compares their compact homology
cores with one actual nearby torus, preserving their
intersection forms.''',r'''The same bound holds for any collection of multiplicity-one components in a smooth resolved finite base change of this family.''','D08','Retains the full second conclusion and removes a proof-plan sentence.')
replace(item(old,1),r'''\item Apply \cref{lem:II:compact-component-transport} to $f$ with a common multiple $N$ of the $m_i$. It gives the resolved map \eqref{cdp:eq:C.PG.2}, whose strict components above each $S_i$ have multiplicity one and whose nearby fibres are the original tori.

''','D12','The entire common-root construction is owned by P305. The application specifies the same f,N,strict components and nearby-fibre identification.')
replace(item(old,3)+item(old,4)+item(old,5)+item(old,6)+item(old,7)+item(old,8),r'''\item Let $D_i$ be the reduced intersection of $E_i$ with the other components of the resolved central support. It is a compact normal-crossing curve, or is empty. Apply the first part of \cref{lem:II:compact-component-transport} with $(E,D)=(E_i,D_i)$. Each Poincar\'e-dual class of $P_{E_i}$ lifts to $H_2(E_i\setminus D_i,\mathbb R)$. Choose a real basis and finite smooth singular representatives of these lifted classes, together with their transverse perturbations. The third part of that lemma embeds neighbourhoods of all these compact cycles into one nearby torus $F=g^{-1}(s)$, with disjoint images for distinct $i$ and with the same intersection pairings. Their images are mutually orthogonal positive subspaces of $H_2(F,\mathbb R)$, of dimensions $2p_g(E_i)$. Preservation of the positive form proves injectivity on their direct sum.

''','D12','The real coefficient, boundary and cycle choices are mapped explicitly to P305. The application keeps the positive-space injection and direct-sum pairing which are needed for the genus bound.')
replace(r'Resolve the actual rational comparison to $Z_i$:',r'Resolve the meromorphic comparison to $Z_i$:','D08','Names the graph comparison directly; both maps, the point blowups and the generically finite pullback proof remain.')
replace(r'''The sum is integral, so it is at most
one. Together with \eqref{cdp:eq:C.PG.5} this is
\eqref{cdp:eq:C.PG.1}. The compact-core argument
used only multiplicity one, and hence
also proves the stated assertion for
any collection of such components in
a smooth finite-base-change model.''',r'''The sum is an integer, so it is at most one. Together with \eqref{cdp:eq:C.PG.5} this gives \eqref{cdp:eq:C.PG.1}. For any collection of multiplicity-one components in a smooth resolved finite base change, apply the first and third parts of \cref{lem:II:compact-component-transport} directly to their complements of the other central components. Their positive subspaces again embed orthogonally in one nearby torus, giving the same inequality.''','D22','Gives the precise second application proving the full finite-base-change conclusion, with its own central components and boundary complements.')

ident='cdp:st:C.2.UN.36'
record=remote.splitlines()[1]
newrecord=r'\StatementRecord{cdp:st:C.2.UN.36}{proved}{01DF}{\cref{lem:II:compact-component-transport,cdp:st:C.2.UN.33,cdp:st:C.2.UN.11}; \cite[\S3.G, p.~321]{Hatcher2002}; \cite[author draft, Chapter~1, Proposition~3.5, p.~17]{HuybrechtsK3Draft}; \cite[Chapter~1, \S1, pp.~5--6; \S2, p.~8; \S3, p.~9]{Peters1990}}'
replace(record,newrecord,'D18','The local input declaration names the common owner and the exact opened source versions/loci. Hatcher duality is now declared by P305; integral transfer remains here.','remote')
replace(r'''Let $U_1$ be the monodromy on the integral first
homology of the actual nearby torus after this
base change.''',r'''Let $F$ be a nearby torus after this base change and let $U_1$ be its monodromy on $H_1(F,\Z)$.''','D22','Names the nearby torus F before defining the invariant target and makes the integral monodromy module explicit.','remote')
replace('The existing monodromy theorem gives',r'\Cref{cdp:st:C.2.UN.11} gives','D04','Names the exact earlier monodromy statement at the point of use.','remote')
replace(r'''normalization component. All these assertions
apply to arbitrary actual central fibres, with
no normal-crossing, reducedness or K\"ahler
hypothesis on the original fibre.''',r'''normalization component.''','D02','The complete proper analytic scope is already given by the hypotheses; the rank-one conclusion remains.','remote')
replace(item(old36,1)+item(old36,2),r'''\item The open set $Z_i^\circ=Z_i\setminus D_i$ maps isomorphically to $S_i\setminus\operatorname{Sing}S$, where the reduced support is one smooth embedded surface. Apply the integral part of \cref{lem:II:compact-component-transport} with $E=Z_i$ and $D=D_i$. Its relative homology map is
\[
 H_2(Z_i^\circ,\Z)\longrightarrow H_2(Z_i,\Z)
 \longrightarrow H_2(Z_i,Z_i^\circ;\Z)
       \simeq H^2(D_i,\Z).                          \tag{C.CL.7}\hypertarget{tag-00C6}{}\label{cdp:eq:C.CL.7}
\]
The target is free on the curve components of $D_i$, and the second arrow gives the vector of intersections with them. Torsion maps to zero. Every element of $K_i$ therefore has an integral lift represented by a compact finite cycle in $Z_i^\circ$. Choose such lifts for an integral basis of each $K_i$, with compact transverse smooth chain representatives and the perturbations needed to compute all their intersections.

''','D12','Replaces the repeated duality and boundary-cohomology proof by the exact integral E=Zi,D=Di application. CL7 remains its integral displayed specialization; it is not aliased to the real-coefficient PG6 sequence.','remote')
replace(item(old36,3),r'''\item Apply the root construction of \cref{lem:II:compact-component-transport} to the stated common multiple $N$. Through the isomorphism $Z_i^\circ\simeq S_i\setminus\operatorname{Sing}S$, its central cover becomes
\[
        \pi_i:\widetilde Z_i^\circ
                       \longrightarrow Z_i^\circ
                  \quad\text{of total degree }m_i.  \tag{C.CL.9}\hypertarget{tag-00C8}{}\label{cdp:eq:C.CL.9}
\]
The cover may be disconnected. In the chart \eqref{cdp:eq:C.PG.3}, the parameter $s$ has order one on every strict component, and the resolution is an isomorphism over this open cover. Thus these cycles lie in smooth single-component loci of multiplicity-one central components.

''','D12','Transfers the identical root chart CL8 to the same owner/display as PG3, retaining both permanent targets and labels there. The central cover CL9, total degree mi, possible disconnectedness and precise preserved open set remain explicit.','remote')
replace(item(old36,5),r'''\item Apply the third part of \cref{lem:II:compact-component-transport} to the transferred cycles and their compact transverse perturbations in these multiplicity-one loci. It gives simultaneous orientation-preserving embeddings into one nearby torus $F=g^{-1}(s)$, preserving intersections within a component and giving disjoint images for distinct strict components.

''','D12','The transferred integral cycles and preserved open root charts satisfy the shared transport hypotheses exactly. The full two-real-flow construction remains once in P305.','remote')
replace(r'''The choice
of lifts is part of this construction;
no canonical splitting of \eqref{cdp:eq:C.CL.7} is
needed.''',r'''The choices of integral lifts and their transferred basis cycles determine this homomorphism.''','D02','States the actual dependence on choices positively, retaining the full integral homomorphism construction.','remote')
replace(item(old36,7),r'''\item The whole-disc cycle families in \cref{lem:II:compact-component-transport} show that every transported basis class is fixed by monodromy on $H_2(F,\Z)$. The natural exterior-algebra identification $H_2(F,\Z)\simeq\Lambda^2H_1(F,\Z)$ intertwines monodromy. Therefore $\Psi$ takes values in the invariant group of \eqref{cdp:eq:C.CL.2}.

''','D12','Retains the natural exterior-algebra map and exact invariant target; the full return-to-identical-cycle proof is owned by the preceding common lemma.','remote')
replace(r'''proved in (C.PG.7)--(C.PG.8). Their
integrals on every boundary curve
vanish by type; their dual homology
classes therefore belong to
$K_i\otimes\mathbb R$ by \eqref{cdp:eq:C.CL.7}.''',r'''of \cref{lem:II:compact-component-transport}, applied with $E=Z_i$ and $D=D_i$. Its Poincar\'e-dual classes pair trivially with every curve component of $D_i$, and hence belong to $K_i\otimes\mathbb R$.''','D04','Replaces inherited literal formula references by the exact positive-space owner and the explicit E=Zi,D=Di map.','remote')
replace(r'\cite[Chapter~1, Proposition~3.5, p.~17]{HuybrechtsK3Draft}',r'\cite[author draft, Chapter~1, Proposition~3.5, p.~17]{HuybrechtsK3Draft}','D18','The complete proposition and proof were opened in the 449-page author draft; the cited layout is named.','remote')
replace(r'''For rank one the invariant space
has basis $(e_{12},e_{13},e_{14},e_{34})$;
its form is one hyperbolic plane
and a two-dimensional radical.
For \eqref{cdp:eq:C.CL.10} an invariant basis is''',r'''In rank one, the only nonzero images under $\Lambda^2U_1-I$ are $e_{23}\mapsto e_{13}$ and $e_{24}\mapsto e_{14}$. Its kernel therefore has basis $(e_{12},e_{13},e_{14},e_{34})$, with one hyperbolic plane and a two-dimensional radical. For \eqref{cdp:eq:C.CL.10}, the nonzero images are
$e_{14}\mapsto\epsilon e_{13}$,
$e_{23}\mapsto e_{13}$ and
$e_{24}\mapsto e_{14}+\epsilon e_{23}+\epsilon e_{13}$.
Thus a vector is invariant precisely when its $e_{24}$ coefficient is zero and its $e_{23}$ coefficient is $-\epsilon$ times its $e_{14}$ coefficient. An invariant basis is''','D22','Makes the exterior-square calculation reproducible directly from U1=I+N0, including the quadratic cross term in the e24 image. The original bases and all Gram entries remain unchanged.','remote')
bookkeeping=r'''The four exterior-square kernels and their restricted forms
are computed over the rationals by
\path{code/current_audits/audit_sign/code/independent_sign_checks.py};
the bases and Gram matrices are recorded in
\path{code/current_audits/audit_sign/independent_sign_checks.json}.
For the rank-two rows the recorded basis is
$(e_{12},e_{13},-\epsilon e_{14}+e_{23},e_{34})$.
Reordering its columns as $(1,4,2,3)$ and multiplying the last
column by $-\epsilon$ gives exactly the basis in
\eqref{cdp:eq:C.CL.12}, and congruence gives
\eqref{cdp:eq:C.CL.13}. The four inertias are respectively
$(3,3,0)$, $(1,1,2)$, $(1,2,1)$ and $(2,1,1)$. Finally
the rank-one row has $p_U=1$,
so \eqref{cdp:eq:C.CL.5} forces every
$p_g(Z_i)$ to vanish, as claimed.'''
replace(bookkeeping,r'''The rank-one row has $p_U=1$, so \eqref{cdp:eq:C.CL.5} forces every $p_g(Z_i)$ to vanish.''','D09','The displayed normal forms, exterior-square actions, bases, Gram matrix and resulting inertias give the complete calculation in the proof. Program/output paths and comparison to saved matrix columns are recorded through provenance program154: S6_SERIES_PUBLISH_c3_provenance_program_rows154.tex and S6_SERIES_PUBLISH_records_II_additions154.tsv. The removed recorded-basis conversion is retained in this exact defect span and the exposed event; no new computational certification is claimed.','remote')

for which in ['main','remote']:
    text=work if which=='main' else remote
    while (m:=re.search(r'\bactual\s+',text)):
        a=max(text.rfind('\n\n',0,m.start())+2,0)
        b=text.find('\n\n',m.end())
        if b<0:b=len(text)
        fragment=text[a:b]
        new=fragment[:m.start()-a]+fragment[m.end()-a:]
        log('D08',fragment,new,'Names the mathematical nearby torus or morphism directly; its precise construction is retained.', 'cdp:st:C.2.UN.28' if which=='main' else 'cdp:st:C.2.UN.36')
        text=text[:a]+new+text[b:]
    if which=='main':work=text
    else:remote=text

work=work.rstrip()+'\n\n'+r'\subsection{Elliptic return maps and component genera}\label{subsec:II:elliptic-return-maps}'+'\n\n'
remote=r'\subsection{Integral component lattices and monodromy}\label{subsec:II:component-invariant-lattice}'+'\n\n'+remote.rstrip()+'\n\n'+r'\subsection{Hopf components and fibre boundaries}\label{subsec:II:hopf-component-boundaries}'
log('D14',old,work,'The compact-core subsection now contains one common lemma before its complete geometric-genus application. The following elliptic-return-map material receives its own open boundary. Whole-paper placement remains open.','subsec:II:component-core-genus')
log('D14',old36,remote,'The integral weighted-lattice theorem becomes a complete subsection. Its substantive nonlocal inputs UN.11 and UN.33 already precede it. The following Hopf-component material receives its own open boundary. Whole-paper placement remains open.','subsec:II:component-invariant-lattice')
transfers.extend([
dict(old_owner='UN.28',new_owner='UN.28',conclusion='Sum of normalization geometric genera at most one, and the same bound after any finite base change',map='Ei <-rho_i- Wi -v_i-> Zi; injective pullback of holomorphic two-forms, point-blowup Hartogs invariance; P305 with (E,D)=(Ei,Di); positive subspace into one 3H torus'),
dict(old_owner='UN.36',new_owner='UN.36',conclusion='Integral multiplicity-weighted invariant lattice, radical kernel, square determinant and all signature/boundary bounds',map='P305 with (E,D)=(Zi,Di), then finite central cover pi_i of total degree mi; integral transfer=sum of all lifts; two-flow embedding; H2(F,Z)=Lambda^2 H1(F,Z)'),
dict(old_owner='C.PG.3 and C.CL.8',new_owner='C.PG.3 with C.CL.8 alias in P305',conclusion='Identical normalized common-root chart',map='Both original formula payloads are w^mi=u, x=s^(N/mi)/w; the same component, coordinates, root and preserved open locus are used'),
])

with (root/'agents/continuation2_B/D19/S6_SERIES_PUBLISH_II_B2_D19_v1_equation_map.tsv').open() as f:
    established={r['old_tag']:r['target_label'] for r in csv.DictReader(f,delimiter='\t') if r['old_tag']}
original_displays={lab:m.group() for m in re.finditer(r'\\\[.*?\\\]',old+old36,re.S) for lab in re.findall(r'\\label\{([^}]+)\}',m.group())}
eq=[]
def number(m):
    a=m.group();tags=re.findall(r'\\tag\{([^}]+)\}',a)
    if not tags:return a
    assert len(tags)==1,tags
    label=re.findall(r'\\label\{([^}]+)\}',a)[0];assert established[tags[0]]==label
    b=a.replace(r'\[',r'\begin{equation}',1);b=b[:-2]+r'\end{equation}';b=b.replace(r'\tag{'+tags[0]+'}','')
    log('D19',original_displays[label],b,'The same mathematical formula and permanent target use the section equation counter.',label)
    eq.append(dict(old_tag=tags[0],target_label=label,statement_id='lem:II:compact-component-transport' if label in ['cdp:eq:C.PG.2','cdp:eq:C.PG.3','cdp:eq:C.PG.6','cdp:eq:C.PG.7','cdp:eq:C.PG.8'] else ('cdp:st:C.2.UN.28' if ':C.PG.' in label else 'cdp:st:C.2.UN.36')))
    return b
work=re.sub(r'\\\[.*?\\\]',number,work,flags=re.S)
remote=re.sub(r'\\\[.*?\\\]',number,remote,flags=re.S)
eq.append(dict(old_tag='C.CL.8',target_label='cdp:eq:C.CL.8',statement_id='lem:II:compact-component-transport'))
alias_display=next(m.group() for m in re.finditer(r'\\begin\{equation\}.*?\\end\{equation\}',work,re.S) if r'\label{cdp:eq:C.PG.3}' in m.group())
log('D19',original_displays['cdp:eq:C.CL.8'],alias_display,'The identical CL8 chart retains its own tag and label through the same-counter alias on PG3. All outside literal citations can resolve to the retained CL8 label.','cdp:eq:C.CL.8')

work=re.sub(r'\n{4,}','\n\n\n',work)
remote=re.sub(r'\n{4,}','\n\n\n',remote)

def payload(s):
    s=re.sub(r'\\SsixEquationAliases\{\\label\{[^}]+\}\}','',s)
    s=re.sub(r'\\tag\{[^}]+\}|\\label\{[^}]+\}|\\hypertarget\{[^}]+\}\{\}','',s)
    for x in [r'\[',r'\]',r'\begin{equation}',r'\end{equation}']:s=s.replace(x,'')
    return re.sub(r'\s+','',s)
new_displays={lab:m.group() for m in re.finditer(r'\\begin\{equation\}.*?\\end\{equation\}',work+remote,re.S) for lab in re.findall(r'\\label\{([^}]+)\}',m.group())}
for lab,display in original_displays.items():assert payload(display)==payload(new_displays[lab]),lab
for kind in ['label','hypertarget']:
    p=r'\\'+kind+r'\{([^}]+)\}'
    before=Counter(re.findall(p,old+old36));after=Counter(re.findall(p,work+remote))
    assert all(after[k]==v for k,v in before.items()),(kind,before-after)
    assert max(after.values())==1
for text in [work,remote]:
    assert Counter(re.findall(r'\\begin\{([^}]+)\}',text))==Counter(re.findall(r'\\end\{([^}]+)\}',text))
    assert not re.search(r'\\tag\{|night:P4R\.13|night:P4\.40|\r|\\path\{',text)
assert len(eq)==22

def tsv(suffix,fields,data):
    with (out/(prefix+suffix)).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(data)
(out/(prefix+'_replacement.tex')).write_text(work,newline='\n')
(out/(prefix+'_UN36_replacement.tex')).write_text(remote,newline='\n')
with (root/'S6_SERIES_PUBLISH_defects_II.tsv').open() as f:fields=next(csv.reader(f,delimiter='\t'))
tsv('_defects.tsv',fields,rows)
tsv('_equations.tsv',['old_tag','target_label','statement_id'],eq)
tsv('_owner_transfers.tsv',['old_owner','new_owner','conclusion','map'],transfers)
tsv('_remote_repairs.tsv',['statement_id','old_text','new_text','reason'],[dict(statement_id='cdp:st:C.2.UN.36',old_text=old36,new_text=remote,reason='Complete original and receiving theorem/proof compared; exact P305 applications replace the duplicated duality, common-root and compact-transport proofs. Integral transfer, multiplicity factors, all lattice conclusions and oriented exterior-square calculations remain complete. Adds bounded subsection identities.')])
with (root/'CHECK_EVENTS.tsv').open() as f:fields=next(csv.reader(f,delimiter='\t'))
now=datetime.now(timezone.utc)
events=[]
scopes=[
('lem:II:compact-component-transport','P305','Read the complete old UN.28 and UN.36 proofs and the full receiving lemma. Compared the integral and real complement maps, positive two-form argument, common-root substitution t=r^mi with r=s^(N/mi), exact central degree, smooth preserved locus, two-real-flow transport and whole-disc monodromy argument. Fresh Hatcher Theorem3.44 statement and complete proof pp.254–255, including the naturality diagram, were opened. The map M=E,K=D,n=4 and real tensor specialization are explicit.'),
('cdp:st:C.2.UN.28','UN28','Read the complete original and receiving statement/proof. The original generically finite graph comparison Ei<-Wi->Zi and injective holomorphic-form pullback remain; P305 is applied to (Ei,Di) and its real compact cycles, giving the same positive direct sum in a single nearby torus. The finite-base-change multiplicity-one specialization and integral genus bound remain complete.'),
('cdp:st:C.2.UN.36','UN36','Read the complete original and receiving statement/proof. Integral lifts, the degree-mi central cover, sum-of-lifts chain transfer, each signed point counted mi times, pairing, radical kernel, full-rank lattice index determinant, signature inequalities, all boundary ranks and oriented Jordan/Gram calculations remain. Added the explicit exterior-square images, including the e24 cross term. Freshly opened Hatcher §3.G p.321, Huybrechts 449-page author draft Chapter1 Proposition3.5 p.17 with full proof, and Peters author notes Chapter1 §1 pp.5–6, §2 p.8, §3 p.9. The removed recorded-basis comparison is: (e12,e13,-epsilon e14+e23,e34), columns reordered (1,4,2,3), last multiplied by -epsilon, gives CL12 and its congruent CL13. Program154 records only rational kernels/Gram forms/inertias, without integral saturation or Smith-form certification.'),
('lem:II:cyclic-component-cover','P240','Read the full current P240 statement/proof as the exposed receiving source for P305. The coordinate map is t=r^mi, r=s^(N/mi), P240 z=x; only its normalized smooth single-component chart and resolution preserving that locus are used. No assertion of an étale interface cover or application of its stabilizer statement to the higher N-root is made.')
]
for lab,short,scope in scopes:
    d={k:'' for k in fields}
    d.update(statement_id=lab,date=now.date().isoformat(),date_utc=now.isoformat(),who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 conductor agent',type='used and rechecked in this run',outcome=scope+' Exposed editorial rereading; no independent proof or computation credit. All 22 old labelled formula payloads and all old targets are preserved, with CL8 exactly aliased to PG3. Whole-paper placement and final PDF remain open.',event_id='publish:c3:conductor09:'+short,phase='publication editorial comparison',source_file='agents/continuation3_conductor/'+prefix+('_UN36_replacement.tex' if short=='UN36' else '_replacement.tex'),source_event_type='used and rechecked in this run',evidence_group='publish:c3:conductor09:compact-component-cores',where='subsec:II:component-invariant-lattice' if short=='UN36' else 'subsec:II:component-core-genus')
    events.append(d)
tsv('_CHECK_EVENTS.tsv',fields,events)
status=[]
for unit,title in [('subsec:II:component-core-genus','Compact component cores and geometric genus'),('subsec:II:component-invariant-lattice','Integral component lattices and monodromy')]:
    for n in range(1,26):
        state='done';reason='Complete local original and receiving statements/proofs read and compared; every local instance found is recorded. D10 and D16 remain done.'
        if n==14:state='open';reason='Local common owner precedes its applications; UN.11 and UN.33 precede the lattice application. Whole-paper final placement remains open.'
        if n==18:state='open';reason='Exact edited primary loci were opened and named; version-identification guard for Huybrechts is delegated to provenance; bibliography-wide pass remains separate.'
        if n==23:state='open';reason='Source is corrected; final integrated typesetting and page reading remain open.'
        status.append(dict(unit=unit,title=title,criterion=f'D{n:02d}',status=state,reason=reason))
    status.append(dict(unit=unit,title=title,criterion='structure',status='open',reason='Complete local ownership and proof order; final whole-paper placement remains open. Adjacent elliptic-return-map and Hopf-boundary units remain open.'))
tsv('_unit_status.tsv',['unit','title','criterion','status','reason'],status)
sources=[
dict(source_id='Hatcher2002:conductor09',url='https://pi.math.cornell.edu/~hatcher/AT/AT.pdf',version='Author-hosted 560-page Algebraic Topology PDF; printed p maps to one-based PDF p+9',exact_locus='Theorem3.44 statement p.254 and complete proof p.255 including cap-product naturality diagram; §3.G chain transfer p.321',sha256='bebb3032bf9021b956da3bd070eb6c67dc662cf849be9cdf6679f677560e5618',bytes='8121741',own_paraphrase='Relative integral homology identifies with cohomology of compact locally contractible D; naturality identifies intersection restriction; covering transfer sums all lifts of each subdivided simplex.',reader='continuation3 conductor; full exact loci read in this pass',date_utc=now.isoformat(),storage='Outside checkpoint: base/S6_PUBLISH_c3_foundations_sources/S6_SERIES_PUBLISH_Hatcher2002.pdf'),
dict(source_id='HuybrechtsK3Draft:conductor09',url='https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf',version='449-page author draft; PDF p.2 identifies pre-publication copy and copyright2015; metadata created4January2016 is not an edition date',exact_locus='Chapter1 Proposition3.5, p.17, statement and full proof',sha256='59da72d5807fd05d08ce28ceaf30a030cfc7e52b92e27778d824ac86cb1dd287',bytes='3256284',own_paraphrase='The complex K3 intersection lattice is two negative E8 blocks plus three hyperbolic planes; the full proof obtains signature(3,19) from b2=22 and the index formula.',reader='continuation3 conductor; full exact locus read in this pass',date_utc=now.isoformat(),storage='/tmp/S6_SERIES_PUBLISH_c3_conductor_primary/HuybrechtsK3Global.pdf'),
dict(source_id='Peters1990:conductor09',url='https://cpeters1.win.tue.nl/ConfsAndSchools/Canada/surface.pdf',version='35-page author notes; title identifies June1990 Canadian Mathematical Society proceedings; metadata creation16September2014 is not an edition date',exact_locus='Chapter1 §1 pp.5–6; §2 p.8; §3 p.9, complete pages read',sha256='51f9c99621b3819aa85894a8cdee4a528b0894364fc22b40a651f1bae55ceed3',bytes='255331',own_paraphrase='Surface index/Noether and Betti formulas, point-blowup connected-sum change and birational genera, and Enriques pg=b1=0 with torsion canonical class give the used signature and blowup bounds.',reader='continuation3 conductor; full exact loci read in this pass',date_utc=now.isoformat(),storage='/tmp/S6_SERIES_PUBLISH_c3_conductor_primary/Peters1990.pdf')
]
tsv('_sources.tsv',['source_id','url','version','exact_locus','sha256','bytes','own_paraphrase','reader','date_utc','storage'],sources)
print('09:',len(rows),'defects;',len(events),'exposed events;',len(eq),'old equation identities;',len(transfers),'owner/conclusion maps;52 status rows;3 exact source records.')
print('P305 only new tag. Complete main and UN36 guards; all old targets/payloads preserved; LF; no central writes.')
