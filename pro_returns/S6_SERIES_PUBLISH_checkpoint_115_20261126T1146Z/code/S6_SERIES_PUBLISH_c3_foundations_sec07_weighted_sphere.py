from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *

p=Package('weighted_sphere','local sphere constructions / before A.5.15')
source=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
a515=block(source,'cdp:st:A.5.15')
conic=block(source,'lem:II:conic-bundle-matching-sphere')

curve=r'''\begin{lemma}[Matching spheres from a curve and a monomial]\hypertarget{tag-P297}{}\label{lem:II:monomial-curve-matching-sphere}
\hypertarget{tag-P247}{}\label{lem:II:conic-bundle-matching-sphere}
\StatementRecord{lem:II:monomial-curve-matching-sphere}{proved}{P297}{}
\StatementRecord{lem:II:conic-bundle-matching-sphere}{proved}{P247}{}
Let $B\subset\C^2_{x,v}$ be a connected smooth complex curve such that $v|_B$ has two distinct simple zeros. Let $b',c'$ be relatively prime positive integers, and put
\[
 X_{B;b',c'}=\{(x,y,z)\in\C^3:(x,y^{b'}z^{c'})\in B\}.
\]
Choose an embedded arc $\gamma$ between two such zeros, avoiding every other zero. The smooth locus of $X_{B;b',c'}$ contains the compact spherical cycle \eqref{cdp:eq:A.J.33a}, whose class has square $-2b'c'$. For $b'=c'=1$, write $X_B=X_{B;1,1}$. The cycle is then a smoothly embedded sphere, its parametrization is \eqref{cdp:eq:A.BP.3}, and its square is $-2$.
\end{lemma}
\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item Over $v\ne0$, both $y,z$ are nonzero and the derivative of $y^{b'}z^{c'}$ is nonzero, so the projection to $B$ is locally a smooth one-dimensional fibration. At a simple zero of $v|_B$, write $x=\chi(v)$. Then
\[
 (y,z)\longmapsto\bigl(\chi(y^{b'}z^{c'}),y,z\bigr)
\]
is a holomorphic chart on the surface, with inverse projection to $(y,z)$. Thus it is smooth near the inverse image of the chosen arc.

\item Make the arc radial in the local $v$ coordinate at its endpoints $P,Q$. Choose smooth complex functions $A(t),B_0(t)$ on its interior such that
\[
 A(t)^{b'}B_0(t)^{c'}=v(\gamma(t)),\qquad
 |A(t)|=|v(\gamma(t))|^{1/(2b')},\quad
 |B_0(t)|=|v(\gamma(t))|^{1/(2c')}.
\]
They exist by choosing a continuous argument along the arc. The continuous map
\begin{equation}
 (t,\theta)\longmapsto
 \bigl(x(\gamma(t)),A(t)e^{\mathrm i c'\theta},
                 B_0(t)e^{-\mathrm i b'\theta}\bigr)
 \hypertarget{tag-0063}{}\label{cdp:eq:A.J.33a}
\end{equation}
from $[0,1]\times S^1$ collapses its two boundary circles to $P,Q$, giving an oriented spherical cycle $\sigma_\gamma:S^2\to X_{B;b',c'}$. Coprimality makes each interior circle embedded. The projection to $B$ recovers the arc, so the whole map is injective away from the collapsed ends.

\item Take a nearby arc $\gamma'$ with the same endpoints and disjoint interior, by an isotopy in a thin disc neighbourhood of $\gamma$ avoiding all other zeros. Choose the arguments in \eqref{cdp:eq:A.J.33a} continuously throughout the isotopy. The coordinates tend uniformly to zero at its endpoints, so this is a continuous homotopy of maps from $S^2$. The two cycles are homologous and meet only at $P,Q$.

In the holomorphic chart $(y,z)$ at either endpoint, arrange the arcs radial with distinct arguments in $v$. The links of the two cycles in a small three-sphere are parallel curves of slope $(c',-b')$ on a Clifford torus. Their oriented linking number is $-b'c'$: the torus framing of a $(p,q)$ curve has linking number $pq$ with its parallel copy, obtained by pushing the curves to opposite solid tori in the Heegaard splitting of $S^3$ and counting meridian discs. Replacing the two cones by transverse relative chains with those boundary links identifies their local intersection with this linking number. At the second endpoint both cycle orientations reverse relative to the outgoing radial coordinate, leaving the intersection sign unchanged. Consequently
\begin{equation}
 [\sigma_\gamma]^2
   =[\sigma_\gamma]\cdot[\sigma_{\gamma'}]
   =-2b'c'\ne0.
 \hypertarget{tag-0064}{}\label{cdp:eq:A.J.33b}
\end{equation}
The cycles and their homotopy all have compact support.

\item For $b'=c'=1$, the map over $v\ne0$ is explicitly
\[
 (b,y)\longmapsto(x(b),y,v(b)/y),\qquad
 (x,y,z)\longmapsto((x,yz),y)
\]
in the two directions. The sphere is
\begin{equation}
 (t,\theta)\longmapsto
   \bigl(x(\gamma(t)),A(t)e^{\mathrm i\theta},
                        B_0(t)e^{-\mathrm i\theta}\bigr).
 \hypertarget{tag-0051}{}\label{cdp:eq:A.BP.3}
\end{equation}
At an endpoint with $v=e^{\mathrm i\phi}|y|^2$, its disk is
\[
 y\longmapsto
 \bigl(\chi(e^{\mathrm i\phi}|y|^2),y,
                         e^{\mathrm i\phi}\overline y\bigr),
\]
with inverse disk coordinate given by projection to $y$. Together with the interior circle coordinate $y/A(t)$, these maps prove that the sphere is smoothly embedded. For a parallel arc, rotating $z$ puts the two oriented disks in the form $z=\overline y$ and $z=\eta\overline y$, with $\eta=a+\mathrm i b\ne1$. Their tangent-frame determinant in $(\Re y,\Im y,\Re z,\Im z)$ is
\[
                         -((a-1)^2+b^2)<0.
\]
Thus each endpoint intersection is $-1$, agreeing with the framing calculation above, and the square is $-2$.
\end{enumerate}
\end{proof}
'''

weighted=r'''\begin{proposition}[Two monomial-separated branches with arbitrary multiplicities]\hypertarget{tag-P296}{}\label{prop:II:weighted-two-branch-sphere}
\StatementRecord{prop:II:weighted-two-branch-sphere}{proved}{P296}{\cref{lem:II:monomial-curve-matching-sphere}}
Let $a,b,k,l$ be positive integers and put
\[
 G(X,Y,Z)=(X-Y^kZ^l)^a(X+Y^kZ^l)^b,\qquad e=\gcd(k,l).
\]
The affine fibre $G=1$ contains a compact spherical class of square $-2(k/e)(l/e)$. Weighted homothety puts that class, together with its intersection comparison, into arbitrarily small nonzero fibres near the origin. Consequently a map from a smooth complex threefold to a smooth curve with nearby smooth fibres complex two-tori cannot have local full-fibre equation $uG$, where $u$ is a holomorphic unit. This conclusion retains the original multiplicities $a,b$.
\end{proposition}
\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item Put $d=\gcd(a,b)$, $a=da_0$, $b=db_0$ and $N=a_0+b_0\ge2$. On the part of $G=1$ where
\[
 (X-Y^kZ^l)^{a_0}(X+Y^kZ^l)^{b_0}=1,
\]
both factors are nonzero. The maps
\[
 X-Y^kZ^l=s^{b_0},\qquad X+Y^kZ^l=s^{-a_0}
\]
identify this part with
\[
 \mathcal X=\{(s,Y,Z)\in\C^*\times\C^2:
              Y^kZ^l=\psi(s)\},\qquad
 \psi(s)=\frac{s^{-a_0}-s^{b_0}}2.
\]
The map from $\mathcal X$ to the original fibre is
\[
 \Theta(s,Y,Z)=\left(\frac{s^{b_0}+s^{-a_0}}2,Y,Z\right).
\]
For integers $r,t$ with $b_0r-a_0t=1$, its holomorphic inverse is
\[
 (X,Y,Z)\longmapsto
 \bigl((X-Y^kZ^l)^r(X+Y^kZ^l)^t,Y,Z\bigr).
\]
The relation between the two factors and the B\'ezout identity verify both inverse identities, including points with $Y=Z=0$.

\item Write $k=ek'$, $l=el'$ with $\gcd(k',l')=1$, and form the curve
\[
 B'=\{(s,v)\in\C^*\times\C:v^e=\psi(s)\}.
\]
The zeros of $\psi$ are the $N$ roots of $s^N=1$, and at each of them
\[
                    \psi'(s)=-\frac N2s^{-a_0-1}\ne0.
\]
The curve is smooth: away from $v=0$ its derivative in $v$ is nonzero, and at $v=0$ its derivative in $s$ is nonzero. It is connected. Over the punctured $s$-line with the zeros removed it is the cyclic $e$-sheeted covering obtained by taking an $e$th root of $\psi$; a loop around any simple zero cyclically permutes all $e$ sheets. This monodromy is transitive, and adjoining the points over the zeros preserves connectedness. The assertion is immediate also for $e=1$.

At each zero, $v$ is a local coordinate on $B'$, so $v|_{B'}$ has exactly $N$ distinct simple zeros. The identity map on $(s,Y,Z)$ identifies $\mathcal X$ with $X_{B';k',l'}$ of \cref{lem:II:monomial-curve-matching-sphere}, since
\[
                 (Y^{k'}Z^{l'})^e=Y^kZ^l=\psi(s).
\]
Apply that lemma to any arc between two of these zeros. Its cycle has square $-2k'l'$. The biholomorphism $\Theta$ and its displayed inverse carry the cycle, its parallel-arc comparison and both endpoints into the original full $G$-fibre. Thus their compact intersection number is unchanged.

\item The polynomial $G$ has weights $(k+l,1,1)$ and degree $D=(k+l)(a+b)$. The homothety
\[
 \delta_\lambda(X,Y,Z)
       =(\lambda^{k+l}X,\lambda Y,\lambda Z)
\]
maps $G=1$ biholomorphically to $G=\lambda^D$, with inverse $\delta_{1/\lambda}$, and shrinks all the compact supports to the origin as $\lambda\to0$.

Choose a local logarithm of $u$ and set
\[
 \Phi(X,Y,Z)
   =\bigl(u^{1/(a+b)}X,u^{1/D}Y,u^{1/D}Z\bigr).
\]
Its derivative at the origin is invertible and weighted homogeneity gives $G\circ\Phi=uG$. For an explicit inverse, choose $v=u^{1/D}$ and solve
\[
 \tau^D=u(\tau^{-(k+l)}X',\tau^{-1}Y',\tau^{-1}Z'),
 \qquad \tau(0)=v(0).
\]
Its derivative in $\tau$ at the origin is $D v(0)^{D-1}\ne0$. The inverse is
\[
 \Psi(X',Y',Z')
       =(\tau^{-(k+l)}X',\tau^{-1}Y',\tau^{-1}Z'),
\]
because uniqueness of the chosen root gives $v\circ\Psi=\tau$ and $\tau\circ\Phi=v$. The map $\Psi\circ\delta_\lambda\circ\Theta$ therefore embeds a neighbourhood of the constructed compact cycles in the local full fibre $uG=\lambda^D$, with the original exponents $a,b$.

Choose $\lambda$ sufficiently small so that the corresponding nearby global fibre is a smooth two-torus. The inclusion preserves the compact intersection number, while the composite sphere map lifts to the contractible universal cover of that torus and has zero homology class. Its square would then be both zero and $-2k'l'$, a contradiction.
\end{enumerate}
\end{proof}
'''

anchor='\n'.join(a515.splitlines()[:2])
p.guard('P297 before A515',anchor,curve+'\n'+anchor,'Place the reusable complete arc/framing proof before the binomial and weighted applications, retaining P247 as its embedded conic clause.')
p.record('D10,D12,D14,D16','lem:II:monomial-curve-matching-sphere','A.5.15 proof items3–5 and the entire P247 conic-sphere proof duplicate the same arc, collapsed circles and endpoint intersection construction.',curve,'One numbered curve-input owner retains the arbitrary coprime slope, continuous spherical cycle, compact homotopy, both endpoint signs and square −2b′c′. Its b′=c′=1 clause retains P247, the inverse maps, smoothly embedded sphere and explicit negative tangent determinant. All old equation labels and permanent targets remain.')

a=a515.index(r'\item Choose two of these zeros');b=a515.index('The weighted homothety',a)
old=a515[a:b]
new=r'''\item Apply \cref{lem:II:monomial-curve-matching-sphere} to the curve $B$ just constructed and the relatively prime integers $b'=b/d$, $c'=c/d$. The identity on $(x,y,z)$ identifies its surface $X_{B;b',c'}$ with $H$, because $(y^{b'}z^{c'})^d=y^bz^c$. The lemma gives the exact cycle \eqref{cdp:eq:A.J.33a}, its parallel-arc homotopy, and the square \eqref{cdp:eq:A.J.33b}. Their supports are compact.
'''
p.guard('A515 matching-sphere application',old,new,'Retain the complete specific binomial base curve, connectedness, all zeros, weighted homothety and original full-map embedding; transfer only the common arc/framing proof.')
p.record('D12','cdp:st:A.5.15',old,new,'The complete old/current A.5.15 proof was read. Its specific base curve x^a−v^d=1 has the required a≥2 simple zeros. The exact map to the receiving X_B is the identity on the ambient coordinates, with b′=b/d and c′=c/d. All subsequent homothety, full-multiplicity unit map, torus contradiction and mixed-normalization example remain.')
old_record=r'\StatementRecord{cdp:st:A.5.15}{proved}{01B5}{}'
new_record=r'\StatementRecord{cdp:st:A.5.15}{proved}{01B5}{\cref{lem:II:monomial-curve-matching-sphere}}'
p.guard('A515 explicit curve input',old_record,new_record,'Record the exact newly earlier input of the retained binomial proof.')
p.record('D10','cdp:st:A.5.15',old_record,new_record,'The statement remains unchanged and its proved status is retained; its dependency record now names the earlier complete curve construction applied in its proof.')
p.guard('Remove old conic owner',conic,'','P247 is retained as an alias at P297 with its whole embedded-sphere conclusion and endpoint determinant specialization.')
p.record('D12,D14','lem:II:conic-bundle-matching-sphere',conic,'The P247 tag and stable label occur at P297; its original surface X_B is explicitly the b′=c′=1 clause there.','Every old hypothesis, actual inverse, smooth endpoint disk, tangent determinant and square is retained. Complete A.5.21, P230 and P4.25 consumer proofs were read: each uses exactly b′=c′=1, with the same curve B and identity surface map. No consumer domain is changed.')

# The weighted model comes after the shared construction and the binomial owner.
p.guard('P296 after A515',a515.splitlines()[-1]+'\n\n\\begin{proposition}[The homotopy and intersection form of an irreducible binomial Milnor fibre]',a515.splitlines()[-1]+'\n\n'+weighted+'\n\\begin{proposition}[The homotopy and intersection form of an irreducible binomial Milnor fibre]','Place the proved arbitrary-multiplicity model after the complete matching-sphere and binomial construction, before its later rigidity consumers.')
p.record('D10,D14,D16,D25','prop:II:weighted-two-branch-sphere','The broad rigidity consumers need a sphere in the actual full function with unequal component multiplicities; the common-power binomial statement does not itself supply that map.',weighted,'P296 proves the precise model (X−Y^kZ^l)^a(X+Y^kZ^l)^b with the original a,b. It gives a Bezout inverse for the full level, the smooth connected root curve B′, its simple zeros, the exact matching-sphere map, weighted shrinking and a unit-coordinate inverse. This closes the weighted model only, not the still-outstanding factor-preserving deformation into that model for P4R.14/P4R.15/P4.41/P4.45.')

for tag,label,owner in [('A.J.33a','cdp:eq:A.J.33a','lem:II:monomial-curve-matching-sphere'),('A.J.33b','cdp:eq:A.J.33b','lem:II:monomial-curve-matching-sphere'),('A.BP.3','cdp:eq:A.BP.3','lem:II:conic-bundle-matching-sphere')]:
    p.equations.append(dict(old_tag=tag,label=label,owner=owner))
p.record('D19','lem:II:monomial-curve-matching-sphere','A.J.33a/A.J.33b occur inside the binomial proof; A.BP.3 occurs in P247.','The same numbered formula payloads, labels and permanent targets occur once at P297, with A.BP.3 in its explicit b′=c′=1 clause.','No legacy equation is deleted or silently replaced by a different morphism. Existing section equation numbering is retained; each consumer identifies its input curve and exponents.')
for row in p.rows:row['old_location']=row['statement_id']+' / complete current statement and proof'
p.write(curve+'\n'+weighted)
