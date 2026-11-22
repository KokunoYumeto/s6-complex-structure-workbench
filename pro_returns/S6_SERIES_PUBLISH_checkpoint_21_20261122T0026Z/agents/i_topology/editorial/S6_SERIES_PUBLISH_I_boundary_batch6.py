from pathlib import Path
from collections import Counter
import re,json,hashlib,datetime
P=Path(__file__).resolve().parent
initial=Path('work/S6_SERIES_PUBLISH_I.tex').read_text();s=initial;patches=[];archive=[]
orphans=json.loads(Path('work/records/S6_SERIES_PUBLISH_I_orphan_candidates.json').read_text())
def gap(prev):return next(x['text'] for x in orphans if x['previous']==prev)
def patch(old,new,reason,ids):
 global s
 ident='I-topology6-%02d'%(len(patches)+1);assert s.count(old)==1,(ident,s.count(old),old[:160])
 patches.append(dict(id=ident,old=old,new=new,reason=reason,statement_ids=ids));s=s.replace(old,new,1);archive.append(dict(id=ident,statement_ids=ids,old=old))
old=gap('push:B38')
new=r'''

\subsection{Normal-crossing limits and coherent cohomology}

\begin{remark}[The two logarithms in the finite connector]
\hypertarget{tag-PT09}{}\label{I:finite-connector-two-logarithms}
\StatementRecord{I:finite-connector-two-logarithms}{proved}{PT09}{\cref{fam:src:A.5.1,push:src:B.3.1,night:P2.7}}
The additive translation construction of Proposition~\ref{fam:src:A.5.1} has finite-chart connector
\[
 \frac{\log s_j}{2\pi i}\Pi_c v_j,
 \qquad c=-\frac{12}{2\pi i}\log r.
\]
The identity $\Pi_c v_j=\Pi_0v_j+c\gamma(v_j)e$ separates its vertical term as
\[
 \frac{\log s_j}{2\pi i}\Pi_0v_j
 -\frac{12\gamma(v_j)}{(2\pi i)^2}\log s_j\log r\,e.
\]
This is the exact overlap map on the punctured parameter charts. Proposition~\ref{push:src:B.3.1} computes its component transport, and Theorem~\ref{night:P2.7} gives the resulting obstruction for a proper filling over the full parameter disc.
\end{remark}

'''
patch(old,new,'Number the actual mixed-logarithm connector and state its exact dependence on the parameter; replace process prose and retitle the local Hodge section.',['I:finite-connector-two-logarithms'])
patch(gap('push:src:B.4.5'),'\n\n','Remove a search-history paragraph whose complete mathematical implication is already the preceding theorem and proof.',['push:src:B.4.5'])
old=gap('push:src:B.4.7')
new=r'''

\begin{remark}[Elliptic-bundle and Hopf degeneration inputs]
\hypertarget{tag-PT10}{}\label{I:elliptic-bundle-primary-comparisons}
\StatementRecord{I:elliptic-bundle-primary-comparisons}{proved}{PT10}{\citep[Definition~1.1 and Remark~1.4, pp.~85--86; Proposition~1.14 and Example~1.15, pp.~93--94]{Fujimoto1990AB}; \citet[Theorem~1.4, preprint p.~7, and Example~2.1, p.~13]{Nishiguchi1988IIRoot}; \citet[Propositions~3.1--3.4, preprint pp.~6--9]{SS00}}
The Cartier-divisor construction used in Proposition~\ref{push:src:B.4.7} is the construction of \citet[Definition~1.1, pp.~85--86]{Fujimoto1990AB}. His Remark~1.4 attributes non-K\"ahler torus degenerations to Ueno. His Proposition~1.14, p.~93, extends principal elliptic bundles across subsets of codimension at least three; Example~1.15, pp.~93--94, gives a principal-bundle extension failure in codimension two and leaves general relative compactification open in that example. Hopf components occur in the semistable degenerations of \citet[Theorem~1.4, preprint p.~7, and Example~2.1, p.~13]{Nishiguchi1988IIRoot}. The diagonal Hopf quotients, elliptic-conductor identifications and normal lines in \citet[Propositions~3.1--3.4, preprint pp.~6--9]{SS00} provide related explicit models. Proposition~\ref{push:src:B.4.7} proves its own proper family using the stated Cartier-divisor cocycle.
\end{remark}

\begin{remark}[Normal degrees along the exceptional ruling]
\hypertarget{tag-PT11}{}\label{I:normal-degree-triple-section}
\StatementRecord{I:normal-degree-triple-section}{proved}{PT11}{\cref{push:src:B.4.7,push:src:B.4.10}}
For the divisor $D=E\times\mathbb P^1$ in $H_i\times\mathbb P^1$, the normal line is pulled back from $E$ and has degree zero on every ruling fibre. For the exceptional divisor obtained by blowing up a smooth elliptic curve in a threefold, the tautological normal restricts to $\mathcal O_{\mathbb P^1}(-1)$ on that fibre. Restricting the normal-crossing identity
\[
 N_{D/A}\otimes N_{D/B}\otimes\mathcal O_D(T)\simeq\mathcal O_D
\]
to the ruling therefore gives $-1+0+\deg(T|_{\mathbb P^1})=0$. In particular an empty triple divisor has the wrong degree, whereas the section $T=E\times\{p\}$ contributes exactly $+1$. Proposition~\ref{push:src:B.4.10} computes the full line bundles, including their elliptic factors.
\end{remark}

\begin{proposition}[Generic simplicity and the distinguished orbit]
\hypertarget{tag-PT12}{}\label{I:generic-torus-simplicity}
\StatementRecord{I:generic-torus-simplicity}{proved}{PT12}{the marked period matrix and the nontorsion elliptic section of the construction}
Fix an ordinary base point at which $\mu\notin\mathbb Q\tau+\mathbb Q$. Such base points exist. Outside a countable set of admissible values of the parameter $\beta$, the corresponding two-dimensional complex torus is simple. For every admissible $\beta$ at this base point, the distinguished line $\mathbb C e$, with $e=\Pi\widehat\delta=(0,1)^t$, meets the period lattice in $\mathbb Z e$. The induced orbit map is the injective holomorphic group map
\[
 \iota:\mathbb C^*\longrightarrow\mathbb C^2/\Pi\Lambda,
 \qquad \iota(e^{2\pi iz})=[ze].
\]
Here $[z]\mapsto e^{2\pi iz}$ identifies $\mathbb C/\mathbb Z$ with the source.
\end{proposition}
\begin{proof}
On an ordinary uniformizing chart the equations $\mu=r\tau+s$, for $(r,s)\in\mathbb Q^2$, define countably many analytic loci. If they covered the chart, Baire's theorem would force one equation on an open set and hence identically. The marked elliptic section would then be torsion, contrary to the construction. Thus the required base point exists.

For integral vectors $v=(a,b,c,d)$ and $v'=(A,B,C,D)$,
\[
 \Pi v=(6a\mu+b\tau+c,\ a\beta+b\mu+d).
\]
The determinant $\det(\Pi v,\Pi v')$ is affine in $\beta$, with coefficient
\[
 (Ab-aB)\tau+(Ac-aC).
\]
If the coefficient vanishes and $a\ne0$, the nonreal number $\tau$ gives $B=Ab/a$ and $C=Ac/a$. The remaining determinant is
$(6a\mu+b\tau+c)(D-Ad/a)$.
Its first factor is nonzero by the rational independence of $1,\tau,\mu$, and its second factor vanishes only when $v,v'$ are rationally dependent. The case $a=0$, $A\ne0$ follows by exchanging the vectors. For $a=A=0$, the determinant is
\[
 (bD-Bd)\tau+(cB-Cb)\mu+(cD-Cd).
\]
Rational independence makes this zero only when all the two-by-two minors vanish, again giving dependence. Therefore an independent integral pair has zero determinant for at most one value of $\beta$. There are countably many such pairs.

A complex line defining an elliptic subtorus contains two real-linearly independent periods. Conversely, any such period pair spans a complex line with a rank-two lattice; admissibility makes the real period map an isomorphism. Avoiding the countable exceptional values therefore gives simplicity. The equation $6a\mu+b\tau+c=0$ forces $a=b=c=0$, which proves $\mathbb C e\cap\Pi\Lambda=\mathbb Z e$ and the claimed orbit map.

For comparison with an elliptic-bundle fibre, every holomorphic map from an elliptic curve to a complex torus lifts to a map $\mathbb C\to\mathbb C^2$ whose derivative is doubly periodic. Compactness makes that derivative constant. A nonconstant such map consequently has image a translate of an elliptic subtorus. Thus a simple torus obtained above has no elliptic-curve fibre of this kind.
\end{proof}

'''
patch(old,new,'Retain and number the primary comparisons, normal-degree identity and complete determinant proof of generic simplicity; make the orbit and elliptic-curve comparison maps explicit.',['I:elliptic-bundle-primary-comparisons','I:normal-degree-triple-section','I:generic-torus-simplicity'])
old=gap('push:src:B.4.8')
new=r'''

\begin{remark}[The individual mixed Chern class]
\hypertarget{tag-PT13}{}\label{I:individual-normal-winding}
\StatementRecord{I:individual-normal-winding}{proved}{PT13}{\cref{push:src:B.4.7,push:src:B.4.8}}
The evaluation isomorphism $\mathcal L_m\otimes\mathcal L_m^{-1}\simeq\mathcal O$ cancels the two mixed first Chern classes. Individually, Proposition~\ref{push:src:B.4.8} computes the nonzero covector $(0,mN)$ on the two swept tori after a parameter cover of order $N$. Both swept tori bound solid tori on an extending semistable good-reduction interface. Hence the restriction of the first Chern class of every extending line evaluates to zero on both, whereas $c_1(\mathcal L_m)$ does not. This is the explicit restriction map relating the individual obstruction to the tensor-product normal equation. In the constant elliptic family of Proposition~\ref{push:src:B.4.7}, the corresponding mixed class is zero.
\end{remark}

'''
patch(old,new,'Replace repair agenda by the exact evaluation isomorphism, integral Chern-class restriction and bounding-torus calculation.',['I:individual-normal-winding'])
# All normal products in this gap already occur with their complete maps in B4.12 Step6.
patch(gap('push:src:B.4.10'),'\n\n','Consolidate the repeated quadric/parabolic normal products with the full retained B4.12 proof, and place its unique Euler calculation after that construction.',['push:src:B.4.12'])
i=s.index('\\label{push:src:B.4.12}');end=s.index('\\end{proof}',i)+len('\\end{proof}')
old=s[end:end+2]
# Use a unique adjoining marker rather than a generic whitespace guard.
a=s.index('\\begin{proposition}',end);b=s.index('\n',a)
marker=s[a:b]
new=r'''\begin{remark}[Euler characteristics of the quadric--parabolic smoothing]
\hypertarget{tag-PT14}{}\label{I:quadric-parabolic-euler}
\StatementRecord{I:quadric-parabolic-euler}{proved}{PT14}{\cref{push:src:B.4.10,push:src:B.4.12}}
For the compact noncentral surface $V_t$ of Proposition~\ref{push:src:B.4.12},
\[
 \chi(V_t)=\chi(S_8)+\chi(Q)-2\chi(E)=8+4=12,
 \qquad \chi(V_t,\mathcal O_{V_t})=1.
\]
The first formula is the local $\xi z=t$ smoothing formula proved there. Mayer--Vietoris for the two spherical boundaries in the Kato construction identifies the middle homology and its intersection form with the eight negative exceptional classes. Thus $\chi(S_8)=8$ and the signature is $-8$, so $c_1(S_8)^2=2\chi(S_8)+3\sigma(S_8)=-8$ and analytic Riemann--Roch gives $\chi(S_8,\mathcal O_{S_8})=0$. Since $\chi(Q,\mathcal O_Q)=1$ and $\chi(E,\mathcal O_E)=0$, the normalization sequence for $S_8\cup_E Q$ and flatness give the second formula. The three pairwise normal-line products are the explicit identities in the proof of Proposition~\ref{push:src:B.4.12}. Its third space $\mathcal V$ maps surjectively to an open disc and is therefore noncompact.
\end{remark}

'''+marker
patch(marker,new,'Number the unique Euler characteristics after the smoothing they describe; retain normal-product results by their complete preceding proof.',['I:quadric-parabolic-euler'])
old=gap('push:src:B.4.13')
new=r'''

\begin{lemma}[The quotient of indexed cores]
\hypertarget{tag-PT15}{}\label{I:indexed-core-quotient}
\StatementRecord{I:indexed-core-quotient}{proved}{PT15}{the explicit quotient and closure maps in the proof}
Let $h$ be an automorphism of $H$, and let modifications $p_j:Y_j\to H$, indexed by $j\in\mathbb Z$, have isomorphisms $\widetilde h_j:Y_j\to Y_{j+1}$ satisfying $p_{j+1}\widetilde h_j=hp_j$. On an $h$-invariant open set $H^\circ$ over which every $p_j$ is an isomorphism, the shift quotient of the disjoint union of their cores is biholomorphic to $H^\circ$ by
\[
 [(j,y)]\longmapsto h^{-j}p_j(y).
\]
Under this isomorphism, its natural map to the orbit space $H^\circ/\langle h\rangle$ is the ordinary quotient map. Moreover, two embedded compact subspaces of a Hausdorff space that share a subset open and dense in both have the same image.
\end{lemma}
\begin{proof}
The displayed map is invariant under $(j,y)\mapsto(j+1,\widetilde h_jy)$ because $h^{-j-1}p_{j+1}\widetilde h_j=h^{-j}p_j$. Every shift orbit meets the zeroth core exactly once, so the inverse is $x\mapsto[(0,p_0^{-1}x)]$. These maps are holomorphic on the component charts. Composing with $H^\circ\to H^\circ/\langle h\rangle$ gives the asserted orbit-space map. For the last assertion, compact images in a Hausdorff space are closed; each of the two images is consequently the closure of their shared dense subset.
\end{proof}

'''
patch(old,new,'Replace the unfolding agenda by the proved exact quotient isomorphism and compact-closure lemma.',['I:indexed-core-quotient'])
old=gap('push:B415')
new=r'''

\begin{remark}[Pullback along a lifted ordinary arc]
\hypertarget{tag-PT16}{}\label{I:lifted-arc-central-cycle}
\StatementRecord{I:lifted-arc-central-cycle}{proved}{PT16}{\cref{push:src:B.4.15}}
Let $\beta:\widetilde B\to\Delta_z\times\Delta_r$ be the blow-up used in Proposition~\ref{push:src:B.4.15}, with exceptional curve $F$. An arc $\iota_k(r)=(kr,r)$ has strict lift $\widetilde\iota_k$ meeting $F$ at $[k:1]$. Choose this point away from the distinguished resolution centres. Pulling the constructed model over $\widetilde B$ back along $\widetilde\iota_k$ gives a central cycle of twelve ruled surfaces over $E_{q_0}$. Indeed the pullback of $\mathcal O_{\widetilde B}(F)$ is a line bundle on a disc and is trivial, and the arc misses the additional resolution centres. The new vertical threefolds of (\ref{push:src:B.4.15}.4) instead lie over the whole exceptional curve $F$ under the map to the original bidisc. The maps being compared are the strict-lift pullback and the composite with $\beta$, respectively.
\end{remark}

'''
patch(old,new,'Specify the strict-lift base-change map responsible for the ordinary central cycle, and its exact relation to the vertical threefold map.',['I:lifted-arc-central-cycle'])
old=gap('push:src:B.4.17')
new=r'''

\begin{remark}[The invariant-cycle equality in the Hopf degeneration]
\hypertarget{tag-PT17}{}\label{I:Hopf-invariant-cycle-comparison}
\StatementRecord{I:Hopf-invariant-cycle-comparison}{proved}{PT17}{\cref{push:src:B.4.17}; \citet[Theorem~1.1, p.~553; arXiv version~1, Theorems~1.2 and~3.2, pp.~1 and~8, equation~(3.9), p.~9, and Corollary~3.7, p.~11]{HondaViaclovsky2025D}}
The compact fibration of Proposition~\ref{push:src:B.4.17} has identity local monodromy $T$ on $H^1(F;\mathbb R)$, but $b_1(Y)=0$ and $b_1(F)=1$. It therefore refutes the converse equality clause in \citet[Theorem~1.1, p.~553]{HondaViaclovsky2025D}, also stated as Theorems~1.2 and~3.2 in arXiv version~1, pp.~1 and~8. The relative-homology and circle-bundle sequences in that proof give
\[
 b_1(Y)\leq\dim H^1(F;\mathbb R)^T\leq b_1(F)
\]
\citep[arXiv version~1, equation~(3.9), p.~9]{HondaViaclovsky2025D}. Identity of $T$ is equivalent to equality in the second inequality. In the present example the first inequality is $0<1$. Equality of the endpoint Betti numbers still forces $T$ to be the identity by this same chain of inequalities. For an irreducible central fibre, the top-dimensional homology in the displayed relative sequence has rank one, giving $b_1(Y)=\dim H^1(F;\mathbb R)^T$, as proved in \citet[arXiv version~1, Corollary~3.7, p.~11]{HondaViaclovsky2025D}. The example here has two central components, with the inclusion maps on $H_1(E)$ computed in Proposition~\ref{push:src:B.4.17}.
\end{remark}

\subsection{A cusp filling on the punctured bidisc}

'''
patch(old,new,'Retain the concrete published equality correction with exact actual primary locators, its two inclusion maps and surviving irreducible-fibre equality; remove audit/report wording.',['I:Hopf-invariant-cycle-comparison'])
old=gap('push:B418')
new=r'''

\begin{remark}[The two axial models and their overlap]
\hypertarget{tag-PT18}{}\label{I:two-axial-model-comparison}
\StatementRecord{I:two-axial-model-comparison}{proved}{PT18}{\cref{push:src:B.4.18,push:src:B.3.7,push:src:B.4.30,night:P2.7}}
Proposition~\ref{push:src:B.4.18} uses the rotating model $\mathcal R$ on $q\ne0$ and the reduced Mumford family on $r\ne0$. On their overlap the exact isomorphism is $\zeta\mapsto\zeta-\sigma+F$, with $F$ given by (\ref{push:src:B.4.18}.3). The larger rotating model has local equation $q=z^{12}$ at its $q$-boundary for $r\ne0$, so every $q$-vertical divisorial valuation there has order in $12\mathbb Z$. The actual reduced Mumford boundary has a divisor of $q$-order one. A common proper modification over $q$ would identify the function $q$ and the associated divisorial valuations; Proposition~\ref{push:src:B.3.7} gives the resulting contradiction. Thus the overlap isomorphism specifies precisely the two-open gluing on $B^\times$. Its noncompletion at the missing origin is Proposition~\ref{push:src:B.4.30}, and the obstruction for the full global family is Theorem~\ref{night:P2.7}.
\end{remark}

\subsection{The actual global family with one base point removed}

'''
patch(old,new,'Replace the scope essay by the explicit overlap isomorphism, the base-function valuation comparison and the already proved global obstruction.',['I:two-axial-model-comparison'])
old=gap('push:B425')
new=r'''

\begin{remark}[The toric ray and blow-up comparisons]
\hypertarget{tag-PT19}{}\label{I:Hopf-ray-blowup-comparisons}
\StatementRecord{I:Hopf-ray-blowup-comparisons}{proved}{PT19}{\citet[\S13, pp.~116--118]{Oda1978D}; \cref{push:src:B.4.10,push:src:B.4.25}}
For the toric ray datum of \citet[\S13, pp.~116--118]{Oda1978D}, put
\[
 v_1=n,\qquad v_2=-n+a n',\qquad a>0.
\]
The original period is $\lambda^{n'}$. The identity $a n'=v_1+v_2$ shows that the base change $\lambda=t^a$ acts in the universal-cover coordinates of $v_1,v_2$ by the two multipliers $(t,t)$, up to the fixed torus units of that construction. Their two vanishing orders are therefore $(1,1)$. The family in Proposition~\ref{push:src:B.4.25} instead has the explicitly specified orders $(m,0)$, with second multiplier tending to the nonzero contraction $\beta(0)$.

The generic fibres of Proposition~\ref{push:src:B.4.10} carry the actual modification $\pi:\widetilde H_q\to H_q$ formed by successive blow-ups at the marked axis points. At one blow-up, $K_{\widetilde H_q}^{-1}=\pi^*K_{H_q}^{-1}\otimes\mathcal O(-E_{\rm exc})$, so its sections correspond exactly to anticanonical sections on $H_q$ vanishing at that centre. Iterating gives the vanishing condition at each successive infinitely near centre. This is the precise map from the anticanonical spaces of the blown-up fibres to the spaces computed in (\ref{push:src:B.4.25}.5).
\end{remark}

\subsection{A necessary vertical fibre over the missing origin}

'''
patch(old,new,'Preserve the classical ray datum through its exact ramified base-change map and the anticanonical blow-up morphism; remove unsupported scope contrasts.',['I:Hopf-ray-blowup-comparisons'])
pat=r'\\(?:label|hypertarget)\{([^}]+)\}'
a=Counter(re.findall(pat,initial));b=Counter(re.findall(pat,s));lost={k:(v,b[k]) for k,v in a.items() if b[k]!=v};assert not lost,lost
r={'input_sha256':hashlib.sha256(initial.encode()).hexdigest(),'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'patches':patches,'anchor_check':{'old_anchor_count':sum(a.values()),'all_preserved':True,'new_anchors':sorted(set(b)-set(a))},'size_change_characters':len(s)-len(initial)}
(P/'S6_SERIES_PUBLISH_I_boundary_batch6_guarded.json').write_text(json.dumps(r,indent=2)+'\n');(P/'S6_SERIES_PUBLISH_I_boundary_batch6_preview.tex').write_text(s);(P/'S6_SERIES_PUBLISH_I_boundary_batch6_archived_proofs.json').write_text(json.dumps(archive,indent=2)+'\n');print('guards',len(patches),'size change',r['size_change_characters'],'new anchors',len(r['anchor_check']['new_anchors']))
