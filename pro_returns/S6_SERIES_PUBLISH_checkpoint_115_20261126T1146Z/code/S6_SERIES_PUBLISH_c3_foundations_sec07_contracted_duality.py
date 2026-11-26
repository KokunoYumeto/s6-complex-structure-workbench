from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *

p=Package('contracted_duality','subsec:II:contracted-ruled-boundaries / before CR.1')
source=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
owner='lem:II:contracted-section-duality'
fragment=r'''\begin{lemma}[Duality and ruling genus for a contracted section]\hypertarget{tag-P293}{}\label{lem:II:contracted-section-duality}
\StatementRecord{lem:II:contracted-section-duality}{proved}{P293}{\cref{lem:II:torus-tube-numerical,lem:II:conductor-duality,lem:II:blowup-topology,lem:II:delta-two-curve-rings,cdp:st:A.5.3}; \cite[\S\S2.2.2--2.2.5, pp.~60--61]{vanStraten1987}}
Let $f:Y\to B_0$ be a proper holomorphic map from a smooth complex threefold to a smooth curve, with connected fibres and smooth general fibre a complex two-torus. Let $mS$ be an irreducible nonnormal full fibre, let $\eta:T\to S$ be its normalization, and let $\pi:Z\to T$ be the minimal resolution. Put $h=\eta\pi$. Suppose that $p:Z\to B$ is an irrational ruling and that its effective adjunction divisor is $D=2C+V$, with $C$ a section and $V$ vertical. Suppose that $\pi$ contracts $C$, and put $g=g(B)$, $p_0=\pi(C)$ and $q=\eta(p_0)$.

Then
\[
 H^1(T;\mathbb R)=H^1(T,\OO_T)=H^2(T,\OO_T)=0.
\]
The sheaf $R^1\pi_*\OO_Z$ is supported only at $p_0$ and has length $g$. After fixing a local generator of $\omega_S$ at $q$, the conductor ideal $I_{p_0}$ of the normalization branch $(T,p_0)$ embeds as an ideal of $R=\OO_{S,q}$; with $J=(\pi_*\omega_Z)_{p_0}$, its residue comparison is \eqref{cdp:eq:C.CR.12} and it satisfies \eqref{cdp:eq:C.CR.13}. One has $g\in\{1,2\}$. For $g=2$, the point $p_0$ is the only point of $T$ over $q$, and the full conductor-image scheme $\Gamma$ is smooth and reduced at $q$. Its component through $q$ has generic transversal an ordinary node or an ordinary cusp.
\end{lemma}
\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item Restrict $f$ over a small disc about the given fibre. The same $S,T,Z,C,V$ occur in \cref{lem:II:torus-tube-numerical}; it gives $\omega_S$ torsion, $\chi(\OO_S)=0$, and $K_Z+D=h^*\omega_S$. By the finite-duality inclusion \eqref{cdp:eq:A.RT.5} of \cref{lem:II:conductor-duality}, a section of $\omega_T$ is a section of $\eta^*\omega_S$ vanishing on the nonempty conductor. A nonzero section of a torsion line bundle on the connected compact normal surface $T$ is nowhere zero: a trivializing tensor power is a nonzero constant. Thus $H^0(T,\omega_T)=0$, and Serre duality gives $H^2(T,\OO_T)=0$.

Since $h^1(Z,\OO_Z)=g$ and $h^2(Z,\OO_Z)=0$, the coherent Leray sequence is
\[
 0\longrightarrow H^1(T,\OO_T)\longrightarrow H^1(Z,\OO_Z)
 \longrightarrow H^0(T,R^1\pi_*\OO_Z)\longrightarrow0.
\tag{C.CR.4}\hypertarget{tag-00DB}{}\label{cdp:eq:C.CR.4}
\]
The higher direct image has finite support. At $p_0$, formal functions identifies its completed stalk with the inverse limit of the $H^1$ of the infinitesimal exceptional fibres. The transition maps on $H^1$ are surjective because their kernels have support of dimension at most one. Restriction from the scheme-theoretic exceptional fibre to $C$ is surjective on $H^1$ for the same reason. The finite-length stalk equals its completion, so its length is at least $h^1(C,\OO_C)=g$. Equation~\eqref{cdp:eq:C.CR.4} bounds the total length by $g$. Equality gives $H^1(T,\OO_T)=0$ and shows that $p_0$ supports the entire higher direct image.

\item Connectedness of resolution fibres makes the constant-sheaf Leray map $H^1(T;\mathbb R)\to H^1(Z;\mathbb R)$ injective. Factor the ruling through its minimal ruled bundle. Its simply connected fibres and the point-blowup isomorphisms in \cref{lem:II:blowup-topology} identify $H^1(Z;\mathbb R)$ with $H^1(B;\mathbb R)$ by pullback. Since $p|_C:C\to B$ is an isomorphism, restriction from $Z$ to $C$ is the inverse identification. Every class pulled back from $T$ restricts to zero on $C$, because $\pi(C)=p_0$. Hence $H^1(T;\mathbb R)=0$.

\item Fix a generator of $\omega_S$ on a small neighbourhood of $q$. The multiplication map in \cref{lem:II:conductor-duality} identifies the branch conductor with
\[
 I_{p_0}=\omega_{T,p_0}\subset\OO_{T,p_0}.
\]
The semilocal normalization over $q$ is the product of its branch rings. Its conductor is the direct sum of their conductor ideals, embedded in $R$ by multiplication; extending by zero on the other branches embeds $I_{p_0}$ itself as an ideal of $R$.

The normal surface $(T,p_0)$ is Cohen--Macaulay. Apply proper duality and Grauert--Riemenschneider vanishing to the resolution over this neighbourhood, in the analytic form of \cite[\S\S2.2.2--2.2.5, pp.~60--61]{vanStraten1987}. The defect of $\OO_T\to R\pi_*\OO_Z$ is $R^1\pi_*\OO_Z$ in degree one. Duality identifies its finite-length dual with $\omega_T/\pi_*\omega_Z$, since the positive direct images of $\omega_Z$ vanish. With $J=(\pi_*\omega_Z)_{p_0}$, this gives
\[
 \operatorname{length}(I_{p_0}/J)
  =\operatorname{length}(R^1\pi_*\OO_Z)_{p_0}=g.
 \tag{C.CR.10}\hypertarget{tag-00CW}{}\label{cdp:eq:C.CR.10}
\]

\item The residue sequence of the smooth exceptional section is
\[
 0\longrightarrow\omega_Z\longrightarrow\omega_Z(C)
   \longrightarrow\omega_C\longrightarrow0.
 \tag{C.CR.11}\hypertarget{tag-00CX}{}\label{cdp:eq:C.CR.11}
\]
The same vanishing makes its pushforward quotient at $p_0$ equal to $H^0(C,\omega_C)$, of dimension $g$. The sheaf $\pi_*\omega_Z(C)$ embeds in $\omega_T$: away from the exceptional set its sections are holomorphic two-forms, and the reflexive canonical module of a normal surface extends them across its isolated singularities. Comparing lengths with \eqref{cdp:eq:C.CR.10} proves
\[
\hypertarget{tag-015A}{}\SsixEquationAliases{\label{cdp:eq:C.UNCR.3}}
 I_{p_0}=(\pi_*\omega_Z(C))_{p_0},\qquad
 I_{p_0}/J\simeq H^0(C,\omega_C).
 \tag{C.CR.12}\hypertarget{tag-00CY}{}\label{cdp:eq:C.CR.12}
\]
Use the adjunction comparison of \cref{cdp:st:A.5.3} with the chosen generator of $\omega_S$. Its pulled-back meromorphic two-form has divisor $-D$, so the comparison identifies $\omega_Z$ with $\OO_Z(-2C-V)$ and $\omega_Z(C)$ with $\OO_Z(-C-V)$ as subsheaves in that trivialization. Thus the quotient in \eqref{cdp:eq:C.CR.12} records the coefficient of order one along $C$, retaining every vertical vanishing condition in $V$.

\item Write $\mathfrak m$ for the maximal ideal of $R$. An element of $\mathfrak m$ pulls back to a function vanishing on $C$, since $h(C)=q$. Every element of $\mathfrak m^2$ therefore vanishes there to order at least two. An element of $I_{p_0}$ already has the prescribed vanishing along $V$ by \eqref{cdp:eq:C.CR.12}; the additional order along $C$ therefore gives
\[
                 I_{p_0}\cap\mathfrak m^2\subset J.
 \tag{C.CR.13}\hypertarget{tag-00CZ}{}\label{cdp:eq:C.CR.13}
\]
The same comparison puts $I_{p_0}\subset\mathfrak m$. It also shows that $q\in\Gamma$: otherwise $S$ would be normal at $q$, its only branch conductor would be $R$, and its element $1$ would have to vanish along $C$.

Consequently
\[
 g=\dim(I_{p_0}/J)
 \le \dim\bigl(I_{p_0}/(I_{p_0}\cap\mathfrak m^2)\bigr)
 \le \dim(\mathfrak m/\mathfrak m^2)\le3.
 \tag{C.CR.14}\hypertarget{tag-00D0}{}\label{cdp:eq:C.CR.14}
\]
A middle dimension of three would make $I_{p_0}$ generate the whole cotangent space. Nakayama's lemma for $\mathfrak m/I_{p_0}$ would give $I_{p_0}=\mathfrak m$. The full conductor ideal contains this ideal and is proper, so it would also equal $\mathfrak m$. This contradicts the pure one-dimensional conductor image in \cref{lem:II:conductor-duality}. Thus the middle dimension is at most two, and $1\le g\le2$.

\item For $g=2$, choose $x,y\in I_{p_0}$ with independent linear parts and lift them to ambient coordinates $(x,y,z)$. The full conductor ideal contains $(x,y)$ in $R$. If $F$ is the defining equation of $S$, the one-dimensional conductor quotient forces $F\in(x,y)$; hence $R/(x,y)=\C\{z\}$. Any strictly larger proper ideal would have a zero-dimensional quotient, so purity makes the full conductor ideal exactly $(x,y)$. This proves that $\Gamma$ is smooth and reduced at $q$.

There is no other point of $T$ over $q$. The elements $x,y$ lie in the single branch summand $I_{p_0}$ and vanish identically on every other branch. Such a two-dimensional branch cannot lie in the one-dimensional ambient germ $\{x=y=0\}$.

Finally the conductor-duality isomorphism $\eta_*\OO_T/\OO_S\simeq\omega_\Gamma\otimes\omega_S^{-1}|_\Gamma$ makes this quotient a line bundle near $q$. The generic transverse normalization quotient therefore has length one. For a reduced plane curve with $r$ branches, the branch constants already give $\delta\ge r-1$, so here $r\le2$. The delta-one cases of \cref{lem:II:delta-two-curve-rings} are exactly the ordinary node and ordinary cusp.
\end{enumerate}
\end{proof}
'''
fragment=p.clean(fragment,owner)
p.record('D12,D14',owner,'CR.1 proof items1–2, the complete CR.2 proof and UN.10 proof items1–3 repeat the same finite-duality, formal-functions, residue and genus calculation.',fragment,'One earlier proved owner uses precisely the broader local UN.10 hypotheses. It retains all cohomology vanishings, support and length of R1piO, the exact branch-ideal embeddings, residue comparison, Nakayama bound and genus-two conductor conclusions. CR.1 and CR.2 apply it by the proper-map restriction with the identical S,T,Z,C,V; no ambient Betti hypothesis is imported into UN.10.')
p.record('D17,D18',owner,'CR.2 cites vanStraten1987 Sections2.2.2–2.2.5 without page locators and repeats the delta-one ring argument.','The exact analytic duality/vanishing source is Sections2.2.2–2.2.5, pp.60–61; the node/cusp ring conclusion applies the earlier full P228 classification after the branch bound delta≥r−1.','Freshly opened the primary Mainz PDF, rendered and read printed pp.60–61 (PDF pp.63–64), including the duality map2.2.2, analytic vanishing2.2.3 and the isolated-singularity canonical quotient2.2.5(5). The complete receiving local finite-length and residue comparison is retained; this does not claim to reprove the cited general duality or vanishing theorem.')
p.record('D25',owner,'CR.2 uses I_p inside the maximal ideal and a proper conductor ideal, after the earlier global CR.1 support argument.','At the broader local owner, the explicit identification I_p=pi_*O_Z(-C−V) proves I_p⊂m_q. If the conductor image avoided q, normality would make its only branch conductor R and force 1 to vanish along C; hence q lies in the conductor.','This makes the inherited proper-ideal premise explicit before Nakayama and preserves the original conclusion. It supplies the direct local correspondence needed when the same proof is extracted from UN.10; no singular-ambient extension or new global assumption is made.')

cr1=block(source,'cdp:st:C.2.CR.1')
anchor='\n'.join(cr1.splitlines()[:2])
p.guard('P293 before CR1',anchor,fragment+'\n'+anchor,'Place the common local duality and genus proof before all three applications.')
a=cr1.index(r'\item The finite-duality calculation');b=cr1.index(r'\item We describe the actual divisor comparisons.',a)
old=cr1[a:b]
new=r'''\item Apply \cref{lem:II:contracted-section-duality} to the restriction of $f$ over a small disc about the fibre $mS$. The normalization, resolution, ruling section and effective divisor are the same $T,Z,C,D=2C+V$. That lemma gives the three cohomology vanishings in \eqref{cdp:eq:C.CR.1}, and says that $R^1\pi_*\OO_Z$ has length $g$ entirely at $\pi(C)$. Its Leray sequence is \eqref{cdp:eq:C.CR.4}.

'''
p.guard('CR1 duality application',old,new,'Apply the local owner to the identical normalization and contracted section; retain CR.1 full global statement and all topology/coefficient/Euler arguments.')
p.record('D12','cdp:st:C.2.CR.1',old,new,'The complete old/current CR.1 proof was read. Its first two items are now the exact P293 application, while C.CR.4 moves to that owner. Its stronger global topology, conductor curve and Euler conclusions remain at CR.1.')

cr2=block(source,'cdp:st:C.2.CR.2')
old=cr2[cr2.index(r'\begin{proof}'):]
new=r'''\begin{proof}
Restrict the proper map of \cref{cdp:st:C.2.CR.1} to a disc about $mS$ and apply \cref{lem:II:contracted-section-duality} with the same $S,T,Z,C,V$ and $p_0=p$. It gives $g\in\{1,2\}$ and, for $g=2$, the unique normalization point over $q$, the smooth reduced conductor ideal $(x,y)$, and the node-or-cusp generic transversal. These are all the assertions of the present proposition; its stronger ambient hypotheses remain those of \cref{cdp:st:C.2.CR.1}.
\end{proof}'''
p.guard('CR2 complete duality application',old,new,'Transfer the full proof and C.CR.10–14 to P293; keep the original CR.2 statement as its scoped global application.')
p.record('D12,D14','cdp:st:C.2.CR.2',old,new,'Keeping the CR.2 statement in its inherited global scope preserves the exact hypotheses used by CR.3. Its proof becomes a direct application to the identical branch ideal, residue map and contracted section; no consumer domain is silently broadened.')
oldrecord=cr2.splitlines()[1]
newrecord=r'\StatementRecord{cdp:st:C.2.CR.2}{proved}{01BR}{\cref{cdp:st:C.2.CR.1,lem:II:contracted-section-duality}}'
p.guard('CR2 exact dependency record',oldrecord,newrecord,'Record the proved local owner and the inherited global hypothesis owner.')
p.record('D10','cdp:st:C.2.CR.2',oldrecord,newrecord,'The stable statement identifier and permanent tag remain; the hidden record now describes the receiving proof.')

un10=block(source,'cdp:st:C.2.UN.10')
a=un10.index(r'\item Apply \cref{lem:II:torus-tube-numerical}');b=un10.index(r'\item Every positive-dimensional critical component',a)
old=un10[a:b]
new=r'''\item Let $g$ be the ruling genus and put $p=\pi(C)$, $q=\eta(p)$. Apply \cref{lem:II:contracted-section-duality} to the map and full fibre in the statement, with the same normalization, minimal resolution and divisor $2C+V$. Its proof uses \cref{lem:II:torus-tube-numerical} on this proper fibre tube, so it requires no ambient Betti hypothesis or transgression class. It gives $g\le2$, the residue comparison \eqref{cdp:eq:C.UNCR.3}, and, for $g=2$, the conductor ideal $(x,y)$, the unique normalization point $p$ above $q$, and the smooth reduced conductor curve with generic node or cusp.

'''
p.guard('UN10 local duality application',old,new,'Apply the broader local owner without importing the ambient assumptions of CR.1 or CR.2; keep the complete later local node/cusp exclusions.')
p.record('D12,D14','cdp:st:C.2.UN.10',old,new,'The complete old/current UN.10 proof was read. Its first three items become the P293 application, while C.UNCR.3 aliases the identical residue identity C.CR.12 there. Every subsequent normalization and genus-one conclusion remains.')
p.equations.append(dict(old_tag='C.UNCR.3',label='cdp:eq:C.UNCR.3',owner=owner))
p.record('D19',owner,'C.CR.12 and C.UNCR.3 display the same branch residue isomorphism in two proofs.','C.CR.12 is the one receiving equation; C.UNCR.3 and its tag015A are retained as an equation alias immediately after begin{equation}.','Both expressions use the same branch p0, J=(pi_*omega_Z)_p0 and residue map to H0(C,omega_C). The alias changes no equation content or morphism; all permanent targets remain.')
for row in p.rows:
    if row['statement_id']!=owner:row['old_location']=row['statement_id']+' / complete current proof'
p.write(fragment)
