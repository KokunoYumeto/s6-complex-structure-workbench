#!/usr/bin/env python3
"""Prepare identity-monodromy elliptic owner and full return-map application."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import csv,re

root=Path(__file__).resolve().parents[1]
out=root/'agents/continuation3_conductor'
prefix='S6_SERIES_PUBLISH_c3_conductor_10'
old=(out/(prefix+'_input.tex')).read_text()
old303=(out/(prefix+'_P303_input.tex')).read_text()
work=old
remote=old303
rows=[]
ident='cdp:st:C.2.UN.29'
def log(kind,a,b,reason,owner=None):
    rows.append(dict(change_id=f'II-C3-UNRESTRICTED10-{len(rows)+1:04d}',type=kind,statement_id=owner or ident,old_location='UN.29 / P303; exact bounded source span',old_page='cp35 PDF omitted; exact source span supplied',new_location='elliptic-return-maps subsection / earlier rank-two-component-frames subsection',new_page='pending integrated final PDF',old_text=a,new_text=b,reason=reason,review_status='Complete original and receiving statements/proofs read and compared; exposed editorial rereading; final integrated PDF reading remains open.'))
def replace(a,b,kind,reason,which='main'):
    global work,remote
    s=work if which=='main' else remote
    assert s.count(a)==1,(which,a[:120],s.count(a))
    s=s.replace(a,b,1)
    if which=='main':work=s
    else:remote=s
    log(kind,a,b,reason)
def item(text,n):
    begin=text.index(r'\begin{enumerate}')
    starts=[begin+m.start() for m in re.finditer(r'\\item\b',text[begin:])]
    end=starts[n] if n<len(starts) else text.index(r'\end{enumerate}',starts[n-1])
    return text[starts[n-1]:end]

owner=r'''\begin{lemma}[Elliptic fibrations with identity monodromy]\hypertarget{tag-P306}{}\label{lem:II:identity-monodromy-elliptic}
\StatementRecord{lem:II:identity-monodromy-elliptic}{proved}{P306}{\cite[Theorem~6.2, pp.~564--566; p.~567; \S8(iv)(11), p.~585]{Kodaira1963II}; \cite[\S2.3, arXiv v2 pp.~5--6]{UlmerUrzua2021}}
Let $q:E_0\to B$ be a proper holomorphic map from a smooth compact complex surface to a smooth compact connected curve, with connected fibres and elliptic general fibre. Suppose that $q$ is relatively minimal and that its integral $H_1$ monodromy on the smooth base locus is the identity. Every full fibre is a positive multiple of a smooth elliptic curve. The smooth fibres are torsors under one fixed elliptic curve, and
\[
 \begin{gathered}
 R^1q_*\OO_{E_0}\simeq\OO_B,\qquad
 p_g(E_0)=g(B),\qquad h^1(E_0,\OO_{E_0})=g(B)+1,\\
 \chi(\OO_{E_0})=e(E_0)=0.
 \end{gathered}
\]
At a fibre $mC$, the normalization of the base change $t=s^m$ over a small base disc is a smooth elliptic family and is finite \'etale over the original surface neighbourhood. Its cyclic action on the central elliptic fibre is by translations, and its action on the relative $H^1(\OO)$ line is trivial. The displayed direct-image isomorphism is obtained by taking invariants under this action at every multiple value.
\end{lemma}
\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item Let $B^\circ$ be the smooth base locus. Trivial integral monodromy gives a global oriented marking $(\gamma_1,\gamma_2)$ of the first homology local system. On a small disc in $B^\circ$, choose a local section and a nonzero holomorphic relative one-form. Its periods $\lambda_1,\lambda_2$ are holomorphic, and $\lambda_1$ is nowhere zero because a nonzero integral cycle on an elliptic curve has nonzero period. The ratio $\tau=\lambda_2/\lambda_1$ is independent of rescaling that form. The marking therefore makes it a single-valued holomorphic map $B^\circ\to\mathbb H$.

The Cayley transform $(\tau-\mathrm i)/(\tau+\mathrm i)$ is bounded. It extends across the finitely many omitted points and is constant on the compact curve $B$, so $\tau$ is constant. Set $A=\mathbb C/(\mathbb Z+\tau\mathbb Z)$. On each small smooth base disc, integration of the relative form normalized by its $\gamma_1$ period, from the chosen section to $x$, identifies the fibre with $A$. These fibrewise integration maps give a holomorphic product with $A$. An overlap preserves the integral marking, so its origin-preserving part is the identity; the overlap is a translation. This identifies the smooth fibres as $A$-torsors and gives a global constant generator of their $H^1(\OO)$ line.

\item Apply Kodaira's classification of relatively minimal proper analytic elliptic fibrations \cite[Theorem~6.2, pp.~564--566; p.~567]{Kodaira1963II}. Every multiplicity-one fibre in the list has a coefficient-one component. At a smooth point of that component away from the other components, the map is a submersion and has a local holomorphic section $\sigma$. On each nearby smooth fibre $F_b$, the map
$x\mapsto\OO_{F_b}(x-\sigma(b))$
identifies $F_b$ with $\operatorname{Pic}^0(F_b)$ and identifies their integral homology local systems. Thus the positive-loop monodromy is the one in \cite[\S2.3, arXiv v2 pp.~5--6]{UlmerUrzua2021}. Identity monodromy leaves only the smooth type $I_0$.

For a multiple fibre, the classification gives type $mI_b$. Locally its full equation is $t=u h^m$, where $h=0$ defines the reduced Cartier support and $u$ is a unit. In the normalized base change $t=s^m$, the charts are $w^m=u$, $s=wh$. The projection $\pi$ to the original smooth surface keeps its two surface coordinates and forgets the unit root $w$. It is finite \'etale, the central fibre is reduced, and its monodromy is the $m$th power of the original monodromy, hence the identity. The new proper family has connected fibres: its Stein factor has generic degree one over the normal $s$-disc and is therefore that disc.

Every central prime curve downstairs has canonical degree zero in Kodaira's list. The \'etale equality $K_{E'}=\pi^*K_{E_0}$ gives canonical degree zero on each central prime upstairs. An exceptional rational curve of square $-1$ would have canonical degree $-1$ by adjunction, so the root family is relatively minimal. Its reduced central fibre has coefficient-one components. The preceding section and Abel--Jacobi comparison therefore applies to it; identity monodromy makes that central fibre smooth of type $I_0$, as also in \cite[\S8(iv)(11), p.~585]{Kodaira1963II}. Shrinking the disc makes the root family smooth throughout. Since $\pi$ is \'etale, its reduced image $C$ is smooth elliptic.

\item Write $r:\Delta_s\to\Delta_t$ for $t=s^m$ and $q':E'\to\Delta_s$ for this smooth root family. Its marked integration maps identify it locally with the product by the same elliptic curve $A$. The cyclic deck action on its central fibre is free because $\pi$ is \'etale. To identify this action, write an automorphism of $A$ as $x\mapsto Lx+b$. For $L\ne1$, the nonzero endomorphism $1-L$ of $A$ is surjective, so $(1-L)x=b$ has a solution and the automorphism has a fixed point. Freeness therefore makes every deck automorphism on the central fibre a translation. Its origin-preserving part on neighbouring marked fibres varies in the discrete group $\operatorname{Aut}(A,0)$, so it remains the identity. It consequently acts trivially on the relative $H^1(\OO)$ generator.

The finite quotient map $\pi:E'\to q^{-1}(\Delta_t)$ gives $\OO_{q^{-1}(\Delta_t)}=(\pi_*\OO_{E'})^{\mu_m}$. Finite direct image has no higher coherent direct images, and averaging over $\mu_m$ makes invariants exact. The direct-image comparison is therefore
\[
 \begin{aligned}
 \left.R^1q_*\OO_{E_0}\right|_{\Delta_t}
 &\simeq\left(r_*R^1q'_*\OO_{E'}\right)^{\mu_m}\\
 &\simeq\left(r_*\OO_{\Delta_s}\right)^{\mu_m}
 \simeq\OO_{\Delta_t}.
 \end{aligned}
\]
The last map identifies a holomorphic function of $t$ with its pullback under $t=s^m$: a power series in $s$ invariant under $s\mapsto\zeta_m s$ has exactly the powers divisible by $m$. These local generators agree on punctured discs with the translation-invariant generator from the global marking. They thus give $R^1q_*\OO_{E_0}\simeq\OO_B$ over the full base, including every multiple value.

\item Connected fibres give $q_*\OO_{E_0}=\OO_B$. The coherent Leray sequence on the curve gives
\[
 H^2(E_0,\OO_{E_0})\simeq H^1(B,\OO_B),\qquad
 h^1(E_0,\OO_{E_0})=g(B)+1.
                                                               \tag{C.RG.13}\hypertarget{tag-00Z7}{}\label{cdp:eq:C.RG.13}
\]
Serre duality yields $p_g(E_0)=g(B)$, and hence $\chi(\OO_{E_0})=1-(g(B)+1)+g(B)=0$. Euler additivity over the smooth base locus and the finitely many remaining fibres gives $e(E_0)=0$, since each fibre support is an elliptic curve.
\end{enumerate}
\end{proof}

'''

record=work.splitlines()[3]
assert record.startswith(r'\StatementRecord')
newrecord=r'\StatementRecord{cdp:st:C.2.UN.29}{proved}{01D7}{\cref{cdp:st:C.2.UN.16,cdp:st:C.2.UN.22,lem:II:identity-monodromy-elliptic,lem:II:semicomplete-transport,cdp:st:C.2.UN.28,cdp:st:C.2.UN.20,cdp:st:C.2.UN.15,lem:II:cyclic-component-cover}; \cite[Chapter~1, Proposition~2.2, p.~8; \S1, pp.~5--6; \S3, p.~9]{Peters1990}}'
replace(record,newrecord,'D18','The declaration names the proved common owners and the exact opened birational and surface-invariant loci. Kodaira and the monodromy table are declared by the receiving P306 owner.')
replace(r'''The maps to $E_0$ are the specified point blowups resolving
the first integral followed by vertical exceptional-curve
contractions. No extension of that first integral to an
ambient neighbourhood is assumed.''',r'''The maps to $E_0$ are the point blowups resolving the first integral followed by vertical exceptional-curve contractions.''','D02','Retains the complete birational construction and removes the scope disclaimer. The proof constructs its return maps by local ambient flow charts.')
replace(r'''Its smooth general fibre
is still a complex two-torus.''',r'''Its smooth general fibres are complex two-tori.''','D08','States the general-fibre property directly for the root model.')
replace(r'''Together with \ref{cdp:st:C.2.UN.22}, this proves that every such root-cover
component of nonnegative Kodaira dimension has coherent
Euler characteristic zero. In particular its minimal model
is neither K3 nor Enriques. Every original component of
Kodaira dimension one has an isotrivial elliptic Iitaka
fibration over a curve of genus at most one; its possible
singular fibres are retained by the actual cyclic quotient
comparison, and are not asserted to be smooth.''',r'''Every root-cover component of nonnegative Kodaira dimension has coherent Euler characteristic zero; its minimal model is neither K3 nor Enriques. Every original component of Kodaira dimension one has an isotrivial elliptic Iitaka fibration over a curve of genus at most one, obtained through the cyclic quotient and resolution maps of \cref{lem:II:cyclic-component-cover,cdp:st:C.2.UN.20}.''','D11','The all-class and original-component conclusions remain positively stated. The proof keeps the quotient maps and all exceptional/singular fibres instead of adding a smoothness conclusion to the quotient.')
replace(r'''Perform the same point blowups in the smooth ambient
threefold. This gives the actual ambient extension of
these modifications, retains multiplicity one on the
strict transform of $E$, and lifts both fields
meromorphically.''',r'''Blow up the same points in the smooth ambient threefold. In local coordinates with $E$ a coordinate divisor, the blowup charts restrict to the point blowup of $E$. Its strict transform still has multiplicity one, since the map is an isomorphism at its generic point, and both fields lift meromorphically.''','D22','Names the exact ambient/surface blowup comparison and the reason the strict component keeps multiplicity one. The generic restrictions and bracket comparison following it remain.')
replace(r'''This is precisely the function and Stein map given by
the original ratio, rather than a chosen ambient extension
of it.''',r'''The function $H$ is the meromorphic function on the Stein base induced by the ratio. The bracket identity gives $V_1(q^*H)=0$, so $V_1|_E$ is tangent to the fibres of $q$.''','D22','Identifies the ratio descent and its first-integral property through the bracket before the compact-fibre restriction is used.')
replace(r'''assertion follows from the compact-curve time-form argument
in C.2.UN.16: a semicomplete meromorphic field on an
elliptic curve has no pole.''',r'''assertion follows by applying the threefold specialization and compact-curve clauses of \cref{lem:II:semicomplete-transport} to the ambient field $V_1$, the multiplicity-one component $E$ and its elliptic fibre: the induced field is semicomplete, and its restriction to that compact curve has no pole.''','D04','Repairs the internal printed C.2.UN.16 reference with the exact proved specialization and compact-curve owner, identifying every receiving domain.')
replace(r'''The local coordinate
$z$ is only used in this one flow box. It need not extend
around the compact elliptic fibre.''',r'''The coordinate $z$ in this construction is the local base coordinate in this flow box.''','D02','States the precise coordinate domain positively. The full return continuation around the fibre remains separate and does not use a global ambient first integral.')
replace(r'\par\medskip\noindent\textbf{Actual elliptic return maps.}'+'\n','','D13','The period construction continues in its proof item; removes the internal unnumbered proof header.')
replace(r'''This constructs a genuine holomorphic return
germ $\Phi_i$; it does not deform a compact elliptic
orbit or assert that such an orbit exists on a nearby
torus.''',r'''This constructs a holomorphic return germ $\Phi_i$ on an ambient neighbourhood of $p$.''','D02','The finite chain of flow charts and compact time path provide the return germ directly; the full construction is retained.')
replace(r'''These are identities of holomorphic germs on the actual
ambient threefold.

\par\medskip\noindent\textbf{The leading normal coefficients.}
The second identity''',r'''\item The second identity''','D13','The displayed identities already arose by pushing the fields through the return map. Gives their leading-coefficient calculation a numbered proof item.')
replace(r'''on the small disc. This uses only the two return germs
and one flow box. In particular it does not require
an ambient extension of $q$ or of $H$ around a fibre.
The formal coefficient extraction is independently
certified in \path{code/A_return_germs.py}; its executed
output records the higher-coefficient cancellations.''',r'''on the small disc.''','D09','All formal cancellations, the orders 2d and 2d+k, unit division, constants ki and di, and equations RG8–RG12 remain in full. The program path and independent-certification language move to the admitted program154 appendix/records: S6_SERIES_PUBLISH_c3_provenance_program_rows154.tex and S6_SERIES_PUBLISH_records_II_additions154.tsv. This editing pass claims no independent computation.')
replace(r'''\par\medskip\noindent\textbf{Global periods and the singular fibres.}
Let $B^\circ$''',r'''\item Let $B^\circ$''','D13','The complete analytic continuation and global period argument receives its own numbered proof item.')
replace(r'''unchanged forces every integral monodromy matrix to
be the identity.''',r'''unchanged forces every integral monodromy matrix to be the identity on $B^\circ$. The inclusion of $B^\circ$ into the full smooth base locus is surjective on fundamental groups, since it adds back only finitely many regular values. Thus the monodromy is the identity on the full smooth base locus as well.''','D22','Maps the period calculation on the smaller regular open set to the precise smooth-locus hypothesis of P306.')
shared=item(old,9)+item(old,10)+item(old,11)
replace(shared,r'''\item Contract the vertical exceptional curves to obtain \eqref{cdp:eq:C.RG.1}. The smooth fibres and their integral monodromy are unchanged. Apply \cref{lem:II:identity-monodromy-elliptic} to this relatively minimal map $q:E_0\to B$. It gives every smooth-multiple-fibre and fixed-elliptic-curve assertion, as well as the full-base direct-image isomorphism in \eqref{cdp:eq:C.RG.2}, with the normalized root and invariant-function descent at every multiple value.

By \eqref{cdp:eq:C.RG.13}, $p_g(E_0)=g(B)$ and $\chi(\OO_{E_0})=0$. The point blowups and blowdowns comparing $E$ and $E_0$ preserve the plurigenera and coherent Euler characteristic \cite[Chapter~1, Proposition~2.2, p.~8]{Peters1990}. Hence $p_g(E)=g(B)$ and $\chi(\OO_E)=0$. The component $E$ is a multiplicity-one component of a smooth resolved finite base change of the original torus family. The finite-base-change clause of \cref{cdp:st:C.2.UN.28} therefore gives $p_g(E)\le1$, and $g(B)\le1$.

''','D12','The complete constant-period, multiple-root, relative-minimality, direct-image descent and Leray arguments are transferred to P306 before P303. This application specifies q:E0→B, preserved smooth monodromy, exact birational maps and the separate UN28 genus-bound hypothesis. RG13 moves with its original formula and target to P306.')
replace(item(old,12),r'''\item A root-cover component of nonnegative Kodaira dimension has either generic rank two, covered by \cref{cdp:st:C.2.UN.22}, or rank one. In rank one, \cref{lem:II:semicomplete-transport} gives genus at most one for a connected general first-integral fibre. A rational fibre would give Kodaira dimension $-\infty$ by the adjunction argument of \cref{cdp:st:C.2.UN.20}; hence the general fibre is elliptic and the preceding argument applies. All such covers therefore have coherent Euler characteristic zero. A minimal K3 surface has $p_g=1,q=0$ and coherent Euler characteristic two; an Enriques surface has $p_g=q=0$ and coherent Euler characteristic one \cite[Chapter~1, \S1, pp.~5--6; \S3, p.~9]{Peters1990}. This proves both exclusions.

''','D22','Keeps the full rank-two/rank-one exhaustion and rational-fibre adjunction exclusion, names the compact-curve genus input, and states the exact coherent invariants excluding K3 and Enriques minimal models.')
replace(item(old,13),r'''\item Let an original component have Kodaira dimension one, and let $Z$ resolve its normalization. For its component cover $E$, resolve the meromorphic comparison as $E\leftarrow W\to Z$, with the first map a sequence of point blowups and the second generically finite. The nonzero generic Jacobian makes pullback of every pluricanonical section injective. Birational invariance of the plurigenera then gives $\kappa(E)\ge\kappa(Z)=1$, while \cref{cdp:st:C.2.UN.15} gives $\kappa(E)\le1$.

Use the elliptic fibration $q:E_0\to B$ from \cref{cdp:st:C.2.UN.22} in rank two and from the preceding argument in rank one; both have $g(B)\le1$. It is the connected-fibre Iitaka fibration. Indeed, the canonical line restricts trivially to a smooth elliptic fibre, so the ratios of pluricanonical sections factor through $q$. Each nonconstant pluricanonical map consequently factors through a finite map from $B$ to its normalized image. Since $q_*\OO_{E_0}=\OO_B$, the connected-fibre Stein factor of the pluricanonical map has base $B$. The cyclic stabilizer therefore acts on $q$ through its action on the pluricanonical field. Apply the proper quotient maps \eqref{cdp:eq:C.HQ.2}--\eqref{cdp:eq:C.HQ.3} of \cref{lem:II:cyclic-component-cover} and the fibration descent in \cref{cdp:st:C.2.UN.20}. Resolving their graphs gives the descended fibration on a smooth birational model of the original component. Its base is the quotient of $B$, so Riemann--Hurwitz gives genus at most one.

On a general fibre, the subgroup fixing a general base point acts by translations. Indeed, an automorphism with a nonidentity linear part has a fixed point by the equation $(1-L)x=b$ on the elliptic curve. A quotient by a group containing such an element is ramified, and Riemann--Hurwitz makes the quotient curve rational. On the resulting smooth general fibre, the normal line is trivial, so adjunction restricts every positive pluricanonical line to $\OO_{\mathbb P^1}(-2m)$. All pluricanonical sections would vanish on this dense family of fibres, contrary to Kodaira dimension one.

The translation subgroup in the fixed elliptic curve is locally constant: each of its holomorphic translation parameters has order dividing the finite group order and hence takes values in a finite torsion subgroup. The general quotient fibres are therefore torsors under the fixed quotient elliptic curve. These proper quotient and graph maps give the isotrivial Iitaka fibration on the original component's smooth model.

''','D22','Retains the complete original-component conclusion with the exact generically finite pluricanonical comparison, Iitaka/base identification, proper cyclic quotient maps, Riemann–Hurwitz base and fibre calculations, rational-fibre adjunction exclusion and finite-torsion constancy. Repairs the former UN19--20 shorthand by the actual P240 quotient maps and UN20 descent. Singular fibres of the quotient/resolution remain part of those maps.')

for m in list(re.finditer(r'\bactual\s+',work))[::-1]:
    a=max(work.rfind('\n\n',0,m.start())+2,0);b=work.find('\n\n',m.end())
    if b<0:b=len(work)
    fragment=work[a:b]
    new=fragment[:m.start()-a]+fragment[m.end()-a:]
    new=re.sub(r'\ban(\s+)(?=(?:multiplicity-one|single-valued)\b)',r'a\1',new)
    work=work[:a]+new+work[b:]
    log('D08',fragment,new,'Names the component, graph, root model, ambient polar divisor or single-valued meromorphic function directly; its full construction remains.')

ident='lem:II:elliptic-first-integral'
record303=remote.splitlines()[1]
replace(record303,r'\StatementRecord{lem:II:elliptic-first-integral}{proved}{P303}{\cref{lem:II:semicomplete-transport,lem:II:identity-monodromy-elliptic}; \cite[Chapter~1, Proposition~2.2, p.~8]{Peters1990}}','D18','The earlier common owner now supplies the full elliptic-fibration comparison. The nonprinting declaration keeps semicomplete transport and the exact birational-invariance source.','remote')
new6=r'''\item Contract the vertical exceptional curves of the first
kind to obtain the relatively minimal elliptic
map
\begin{equation}
 \widehat X\xrightarrow{\ \mu\ }X_0
       \xrightarrow{\ q_0\ }B.
 \hypertarget{tag-00YW}{}\label{cdp:eq:C.RF.3}
\end{equation}
These contractions preserve the smooth fibres and their integral monodromy representation. Apply \cref{lem:II:identity-monodromy-elliptic} with $(E_0,q)=(X_0,q_0)$ and the same base $B$. It gives the smooth multiple fibre supports and $e(X_0)=\chi(\OO_{X_0})=0$. Write $\Lambda=\lambda_1\mathbb Z+\lambda_2\mathbb Z$ in the period marking above. The fixed curve in that lemma, normalized to first period one, is identified with $\mathbb C/\Lambda$ by $[z]\mapsto[\lambda_1z]$; this is the rescaling of the integration map on the common smooth fibres.

'''
replace(item(old303,6),new6,'D12','The entire repeated Kodaira/section/Jacobian and multiple-root comparison moves to P306 immediately before P303. This application names its precise relatively minimal map and identifies its fixed elliptic curve through the preserved marked integration map.','remote')
replace(r'''The Euler characteristic
is zero by additivity over the smooth base stratum
and the finitely many special fibres.  To compute
the canonical square, choose''',r'''To compute the canonical square, choose''','D12','The common owner proves Euler additivity once; P303 retains its separate full contraction-defined canonical-form calculation.','remote')
replace(r'''The surface
Riemann--Roch formula gives
$\chi(\mathcal O_{X_0})=(K_{X_0}^2+e(X_0))/12=0$.
Proper birational invariance of the coherent
Euler characteristic under the displayed point
blowups and blowdowns yields
$\chi(\mathcal O_X)=0$.''',r'''Birational invariance under the displayed point blowups and blowdowns \cite[Chapter~1, Proposition~2.2, p.~8]{Peters1990} gives $\chi(\OO_X)=\chi(\OO_{X_0})=0$.''','D12','Uses the full-base coherent direct-image conclusion already proved in P306 and preserves the exact birational comparison to X. The RF4 contraction map, vertical canonical divisor and square-zero support calculation remain complete.','remote')
remote=owner+remote
log('D12',item(old303,6)+shared,owner,'P306 is the single owner of the constant-modulus, local-section/Jacobian, multiple-root, canonical-degree/relative-minimality and full-base direct-image/Leray arguments. Its domain is an arbitrary relatively minimal compact proper analytic elliptic fibration with identity integral monodromy; no bound on base genus is imposed.','lem:II:identity-monodromy-elliptic')
work=work.rstrip()+'\n\n'+r'\subsection{Cyclic component models and elliptic fibre configurations}\label{subsec:II:cyclic-component-models}'+'\n\n'
log('D14',old,work,'The full ambient return-germ construction, leading coefficients, global periods and component applications stand in dependency order in one complete subsection. The following UN31/UN33 material receives its own open subsection boundary. P306 is inserted earlier, before P303, through the complete remote guard.','subsec:II:elliptic-return-maps')

with (root/'agents/continuation2_B/D19/S6_SERIES_PUBLISH_II_B2_D19_v1_equation_map.tsv').open() as f:
    established={r['old_tag']:r['target_label'] for r in csv.DictReader(f,delimiter='\t') if r['old_tag']}
old_displays={lab:m.group() for m in re.finditer(r'\\\[.*?\\\]|\\begin\{equation\}.*?\\end\{equation\}',old+old303,re.S) for lab in re.findall(r'\\label\{([^}]+)\}',m.group())}
eq=[]
def number(m):
    a=m.group();tags=re.findall(r'\\tag\{([^}]+)\}',a)
    if not tags:return a
    assert len(tags)==1,tags
    label=re.findall(r'\\label\{([^}]+)\}',a)[0];assert established[tags[0]]==label
    b=a.replace(r'\[',r'\begin{equation}',1);b=b[:-2]+r'\end{equation}';b=b.replace(r'\tag{'+tags[0]+'}','')
    log('D19',old_displays[label],b,'The unchanged formula and permanent target use the section equation counter.',label)
    eq.append(dict(old_tag=tags[0],target_label=label,statement_id='lem:II:identity-monodromy-elliptic' if tags[0]=='C.RG.13' else 'cdp:st:C.2.UN.29'))
    return b
work=re.sub(r'\\\[.*?\\\]',number,work,flags=re.S)
remote=re.sub(r'\\\[.*?\\\]',number,remote,flags=re.S)
work=re.sub(r'\n{4,}','\n\n\n',work)
remote=re.sub(r'\n{4,}','\n\n\n',remote)
def payload(s):
    s=re.sub(r'\\tag\{[^}]+\}|\\label\{[^}]+\}|\\hypertarget\{[^}]+\}\{\}','',s)
    for x in [r'\[',r'\]',r'\begin{equation}',r'\end{equation}']:s=s.replace(x,'')
    return re.sub(r'\s+','',s)
new_displays={lab:m.group() for m in re.finditer(r'\\\[.*?\\\]|\\begin\{equation\}.*?\\end\{equation\}',work+remote,re.S) for lab in re.findall(r'\\label\{([^}]+)\}',m.group())}
for lab,d in old_displays.items():assert payload(d)==payload(new_displays[lab]),lab
for kind in ['label','hypertarget']:
    p=r'\\'+kind+r'\{([^}]+)\}'
    before=Counter(re.findall(p,old+old303));after=Counter(re.findall(p,work+remote))
    assert all(after[k]==v for k,v in before.items()),(kind,before-after)
    assert max(after.values())==1
for text in [work,remote]:
    assert Counter(re.findall(r'\\begin\{([^}]+)\}',text))==Counter(re.findall(r'\\end\{([^}]+)\}',text))
    assert not re.search(r'\\tag\{|night:P4R\.13|night:P4\.40|\r|\\path\{|\\textbf\{',text)
assert len(eq)==13 and len(old_displays)==17
def tsv(suffix,fields,data):
    with (out/(prefix+suffix)).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(data)
(out/(prefix+'_replacement.tex')).write_text(work,newline='\n')
(out/(prefix+'_P303_replacement.tex')).write_text(remote,newline='\n')
(out/(prefix+'_P306.tex')).write_text(remote[:remote.index(r'\begin{lemma}[Elliptic first integrals')],newline='\n')
with (root/'S6_SERIES_PUBLISH_defects_II.tsv').open() as f:fields=next(csv.reader(f,delimiter='\t'))
tsv('_defects.tsv',fields,rows)
tsv('_equations.tsv',['old_tag','target_label','statement_id'],eq)
tsv('_remote_repairs.tsv',['statement_id','old_text','new_text','reason'],[dict(statement_id='lem:II:elliptic-first-integral',old_text=old303,new_text=remote,reason='Full current P303 and complete receiving P306/P303 read and compared. Insert the common identity-monodromy elliptic owner immediately before P303, replace its repeated classification by the exact q0:X0→B application, preserve RF1–4 and the entire projected-field no-pole, period-injection and canonical-form constructions.')])
transfers=[
dict(old_owner='UN.29 items9–11; P303 item6 and Euler part of item7',new_owner='P306 / lem:II:identity-monodromy-elliptic',conclusion='Constant elliptic modulus, smooth multiple supports, étale local roots, full-base R1O=O, Leray genera and zero Euler characteristics',map='Global integral marking gives normalized period ratio; coefficient-one section gives x↦O(x−sigma) to Pic0; t=uh^m,t=s^m,w^m=u,s=wh; finite quotient invariants identify R1qO with (r_*R1q′O)^mu_m'),
dict(old_owner='UN.29',new_owner='UN.29',conclusion='Rank-one ambient translation limits have identity monodromy and base genus≤1; all nonnegative-Kodaira covers have chi=0; original kappa1 components have isotrivial elliptic Iitaka fibrations over genus≤1 bases',map='Entire return-germ and coefficient argument RG3–12; pi1(B°)→pi1(full smooth locus) surjective; P306 q:E0→B; point-blowup birational genera and UN28 finite-base-change clause; P240 quotient maps and UN20 fibration descent'),
dict(old_owner='P303',new_owner='P303 with P306 application',conclusion='Rank-two commuting fields with elliptic first integral have base genus≤1 and the original e=K²=chi=0 conclusions',map='Preserved full projected-Z inverse-time loop argument and period injection RF2; preserved vertical contraction RF3; P306(E0,q)=(X0,q0); preserved i_V Omega=q0*eta and vertical square-zero divisor RF4'),
dict(old_owner='C.RG.13 in UN.29',new_owner='C.RG.13 in P306',conclusion='H²(E0,O)=H¹(B,O), h¹(E0,O)=g(B)+1',map='Exact same q:E0→B and coefficient sheaves, obtained from full-base R1qO=O and q_*O=O; no genus bound is used in this identity')
]
tsv('_owner_transfers.tsv',['old_owner','new_owner','conclusion','map'],transfers)
with (root/'CHECK_EVENTS.tsv').open() as f:fields=next(csv.reader(f,delimiter='\t'))
now=datetime.now(timezone.utc);events=[]
scopes=[
('lem:II:identity-monodromy-elliptic','P306','Read the complete source UN.29 and P303 proofs and complete receiving P306. Compared the exact compact proper analytic/relatively minimal/identity integral monodromy scope, the marked period and Cayley argument, local section and Abel–Jacobi identification, root charts t=uh^m,t=s^m,w^m=u,s=wh, connected Stein factor, étale canonical pullback and adjunction, free deck translation and discrete linear-part comparison. The finite-direct-image/invariant comparison is written in full, including the invariant power-series map at multiple values and its gluing to the global generator. The complete coherent Leray and Euler calculations remain.'),
('cdp:st:C.2.UN.29','UN29','Read the complete original and receiving statement/proof. Preserved every full-fibre conclusion and RG1–13 payload. The entire ambient blowup/flow-box/time-path/return-germ construction, both pushforward identities, all orders d,2d,2d+k, constants ki and di, universal-cover continuation and period injection remain. Added the exact full-smooth-locus fundamental-group map before P306. Preserved the all-class exhaustion, birational plurigenera and proper quotient/Iitaka arguments with explicit maps. The admitted program154 row owns the path previously printed in the proof; no new independent computational credit is claimed.'),
('lem:II:elliptic-first-integral','P303','Read the full current original P303 and the entire receiving proof. Preserved all hypotheses, RF1–4, full semicomplete transport, horizontal-pole removal, proper projected-Z no-pole argument using inverse-time monodromy, compactness and holomorphic ODE continuation, and the period injection with regular-value extension. The exact new P306 application uses (E0,q)=(X0,q0), sameB, and the fixed curve is identified by the existing integration map. The complete i_V Omega=q0*eta calculation, vertical canonical divisor and K²=0 proof remain; coherent Euler zero is taken from the full-base direct-image owner.')
]
for lab,short,scope in scopes:
    e={k:'' for k in fields}
    e.update(statement_id=lab,date=now.date().isoformat(),date_utc=now.isoformat(),who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 conductor agent',type='used and rechecked in this run',outcome=scope+' Kodaira §6 proper analytic setup pp.563–564, full Theorem6.2 statement pp.564–566, canonical-degree calculation p.567 and §8(iv)(11) p.585 were reopened at their exact published-text loci; the full classification proof is not claimed as read. Ulmer–Urzúa arXiv2002.01906v2 §2.3 pp.5–6 and its complete matrix table were reopened, including a page-image reading. Peters p.8 and pp.5–6,9 use the complete source readings already recorded in09. Exposed editorial rereading only; no independent proof or computation credit. All17 labelled formula payloads agree; final whole-paper placement and final rendering remain open.',event_id='publish:c3:conductor10:'+short,phase='publication editorial comparison',source_file='agents/continuation3_conductor/'+prefix+('_replacement.tex' if short=='UN29' else '_P303_replacement.tex'),source_event_type='used and rechecked in this run',evidence_group='publish:c3:conductor10:elliptic-return-maps',where='subsec:II:elliptic-return-maps' if short=='UN29' else 'subsec:II:rank-two-component-frames')
    events.append(e)
tsv('_CHECK_EVENTS.tsv',fields,events)
status=[]
for n in range(1,26):
    state='done';reason='Complete original and receiving UN.29 unit read and compared; each local instance found is recorded. D10 and D16 remain done.'
    if n==14:state='open';reason='P306 precedes both full applications; the return-map construction is in local dependency order. Final whole-paper placement remains open.'
    if n==18:state='open';reason='Exact edited primary loci are opened and named, with version records; bibliography-wide pass remains separate.'
    if n==23:state='open';reason='Source edited; final integrated typesetting and page reading remain open.'
    status.append(dict(unit='subsec:II:elliptic-return-maps',title='Elliptic return maps and component genera',criterion=f'D{n:02d}',status=state,reason=reason))
status.append(dict(unit='subsec:II:elliptic-return-maps',title='Elliptic return maps and component genera',criterion='structure',status='open',reason='Complete local shared-owner and receiving-proof ordering; final whole-paper placement remains open. P303 remote is bounded within its previously reviewed subsection; the unchanged UN.22 is not given a fresh full-reading event.'))
tsv('_unit_status.tsv',['unit','title','criterion','status','reason'],status)
sources=[
dict(source_id='Kodaira1963II:conductor10',url='https://www.jstor.org/stable/1970131',version='Annals of Mathematics77(3),1963,563–626; original published text',exact_locus='§6 proper analytic setup pp.563–564; full Theorem6.2 statement pp.564–566; canonical-degree calculation p.567; §8(iv)(11) p.585',sha256='',bytes='',own_paraphrase='Proper analytic elliptic fibre spaces over open or compact Riemann surfaces, relative minimality, all multiple types mIb, coefficient-one components and canonical degrees; the identity local linear monodromy gives regular typeI0. Full classification proof not read. Published text reopened through the original JSTOR scan reproduction at https://it.scribd.com/document/480913137/kodaira1963-II; this is a reading locator only, not a replacement bibliography URL.',reader='continuation3 conductor; exact published-text loci reopened in this pass',date_utc=now.isoformat(),storage='No copied published source stored in checkpoint; no successful primary PDF download or hash claimed.'),
dict(source_id='UlmerUrzua2021:conductor10',url='https://arxiv.org/pdf/2002.01906v2',version='arXiv2002.01906v2; arXiv margin26May2020, author Date27May2020;24-page layout',exact_locus='§2.3 pp.5–6, with all local monodromy matrix rows on p.6; §2.2 p.5 also read',sha256='a35bde9428a00cf693863648138a05a9176942d74a692bc8ee8cce6966ec9dd6',bytes='305467',own_paraphrase='The positively oriented local monodromy table has identity only at I0. The proof identifies the local analytic fibration with its Jacobian through a coefficient-one local section before applying that table; multiple fibres use the normalized étale root first.',reader='continuation3 conductor; full exact local text and p.6 table image reopened in this pass',date_utc=now.isoformat(),storage='/tmp/S6_SERIES_PUBLISH_c3_conductor_primary/UlmerUrzua2021_arxiv_v2.pdf; outside checkpoint.')
]
tsv('_sources.tsv',['source_id','url','version','exact_locus','sha256','bytes','own_paraphrase','reader','date_utc','storage'],sources)
print('10:',len(rows),'defects;3 exposed events;13 old equation conversions;17 unchanged labelled payloads;4 owner maps;26 local unit-status rows;2 exact source rows.')
print('P306 only new tag. Full UN29 and P306/P303 receiving guards; all old labels/targets preserved; LF; no central writes.')
