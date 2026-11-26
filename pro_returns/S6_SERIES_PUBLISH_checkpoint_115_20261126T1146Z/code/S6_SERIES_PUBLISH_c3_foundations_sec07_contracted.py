from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *

p = Package('contracted', 'subsec:II:contracted-ruled-boundaries')
source = (ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
owners = ['lem:II:contracted-section-duality', 'cdp:st:C.2.CR.1',
          'cdp:st:C.2.CR.2', 'cdp:st:C.2.CR.3', 'cdp:st:C.2.CR.5',
          'cdp:st:C.2.CR.6', 'cdp:st:C.2.UN.9', 'cdp:st:C.2.UN.10',
          'cdp:st:C.2.MH.3', 'night:P4R.6']
old = {k:block(source,k) for k in owners}

def statement(k):
    return old[k][:old[k].index(r'\begin{proof}')].strip()

def display(k, label):
    text = old[k]
    q = text.index(r'\label{'+label+'}')
    a = text.rfind(r'\[',0,q)
    b = text.index(r'\]',q)+2
    return text[a:b]

duality = old['lem:II:contracted-section-duality']
record_end = duality.index('\nLet $f:')
duality = duality[:record_end] + r'''
\hypertarget{tag-01BR}{}\label{cdp:st:C.2.CR.2}
\StatementRecord{cdp:st:C.2.CR.2}{proved}{01BR}{}
''' + duality[record_end:]
p.record('D12', 'cdp:st:C.2.CR.2', old['cdp:st:C.2.CR.2'], duality,
         'The complete CR2 statement and proof are the restriction of P293 to the global CR1 data, with the identical S,T,Z,C,V,p0 and q. Move its label and tag to that single stronger proved owner. CR3 below explicitly keeps every CR1 global hypothesis; the other body consumers are absorbed into UN10. No global conclusion is inferred from the broader alias alone.')

cr1s = statement('cdp:st:C.2.CR.1')
record = cr1s.splitlines()[1]
cr1s = p.edit(cr1s, record,
    r'\StatementRecord{cdp:st:C.2.CR.1}{proved}{01BQ}{\cref{lem:II:contracted-section-duality,lem:II:irrational-ruled-boundary,lem:II:canonical-boundary-blowup,lem:II:proper-conductor-pushout,lem:II:curve-normalization-graph,night:P4R.1,lem:II:proper-conductor-divisor,cdp:st:D.1.9,cdp:st:C.2.VII.2}}',
    'D12,D14', 'cdp:st:C.2.CR.1',
    'Record the exact earlier owners used by the receiving proof and remove UN7, whose later exclusion is a consequence rather than a premise of CR1.')
cr1s = p.edit(cr1s, 'Then the following are exact consequences of these hypotheses:',
              'One has', 'D08', 'cdp:st:C.2.CR.1',
              'State the conclusions directly.')
cr1s = p.edit(cr1s, 'all\nits intersections are ordinary double points.',
              'all\nits intersections are ordinary double points. Every component of\ncoefficient one is a leaf of this tree.',
              'D12', 'cdp:st:C.2.CR.1',
              'Transfer the full coefficient-one-leaf conclusion and its induction from the first step of CR3 to the common coefficient owner, at the same global scope.')
cr1s = p.edit(cr1s, 'Choose a specified sequence of ruling blowdowns to a bundle',
              'Choose a sequence of ruling blowdowns to a bundle', 'D08',
              'cdp:st:C.2.CR.1',
              'Keep the chosen blowdown sequence and its sequence-dependent N0, with direct mathematical wording.')
closing = '''These necessary equations are retained in the Euler
calculation. \\ref{cdp:st:C.2.UN.7} later excludes their simultaneous
geometric occurrence under the stated CDP hypotheses.
'''
cr1s = p.edit(cr1s, closing, '', 'D01,D08,D11,D14', 'cdp:st:C.2.CR.1',
              'The later global exclusion remains proved in UN7. Remove the production wording and the forward exclusion from this statement; it is not a premise of any CR1 calculation.')

cr1proof = r'''\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item Restrict $f$ over a small disc about $mS$ and apply
\cref{lem:II:contracted-section-duality} with the same
$S,T,Z,C,V$. It gives the three cohomology vanishings in
\eqref{cdp:eq:C.CR.1}, and $R^1\pi_*\OO_Z$ has length $g$
entirely at $p_0=\pi(C)$. Its Leray sequence is
\eqref{cdp:eq:C.CR.4}. The same numerical input
\cref{lem:II:torus-tube-numerical} gives $\omega_S$
torsion and $\chi(\OO_S)=0$. Its adjunction identity
$K_Z+D=h^*\omega_S$ makes this canonical-boundary
class numerically trivial.

\item Let $\beta:Z\to Z_0$ be the chosen ruling contraction,
and put $D_0=\beta_*D$. Apply the doubled-section case of
\cref{lem:II:irrational-ruled-boundary} with its $T=Z$,
$T_0=Z_0$, $H=C_0$ and this same divisor $D$.
It gives $D_0=2C_0+\sum_j a_jF_j$, the stated tree of
smooth curves, and the isomorphism induced by
$j:D_{\rm red}\hookrightarrow Z$ on fundamental groups.
Under the same blowdowns, this isomorphism is identified
with $\pi_1(C_0)\to\pi_1(Z_0)$ and with the inverse of
the ruling map to $\pi_1(B)$.

At each step $\sigma:W\to W'$, use
\cref{lem:II:canonical-boundary-blowup} with
$Z_1=W$, $Z_2=W'$, $D_1=D_W$, $D_2=\sigma_*D_W$ and
$m=d$, the multiplicity at its centre.
The coefficient $a$ is that of the same exceptional
curve in $D_W$. Formula~\eqref{cdp:eq:C.CR.5} gives
$a=d-1$.

\item Initially each edge of the boundary tree has
coefficients $(2,a_j)$, whose shifted coefficients are
coprime. A node blowup inserts coefficient $a+b-1$,
whose shift is $(a-1)+(b-1)$, so the two new edge gcds
equal the old one. A positive-coefficient blowup at a
smooth point of a coefficient-$a$ component creates
coefficient $a-1$; the new edge has shifted coefficients
$a-1,a-2$. This proves \eqref{cdp:eq:C.CR.2}.

Every coefficient-one component is initially a fibre
leaf. A smooth boundary blowup creates coefficient one
only from coefficient two, and creates a leaf. A node
blowup could create coefficient one only from an edge
$(1,1)$, excluded by \eqref{cdp:eq:C.CR.2}. A blowup
at the unique node of an existing coefficient-one
component subdivides its edge, while a blowup at a
smooth point of that component has exceptional coefficient
zero. Hence every coefficient-one component remains a leaf.

\item Apply \cref{lem:II:proper-conductor-divisor} to
$f$ restricted over the same disc, with
$N=T$, its resolution surface equal to $Z$,
$\nu=\eta$ and $\rho=h$. Its divisor is the same $D$:
both are defined by the orders of the pullback of a local
generator of $\omega_S$, and changing that generator by
a unit changes no order. The lemma identifies the
reduced singular locus of $S$ with its reduced conductor image,
gives
''' + display('cdp:st:C.2.CR.1', 'cdp:eq:C.CR.6') + r'''
It also makes $h$ an isomorphism off these closed sets.
In particular every exceptional configuration meets
the strict conductor and lies in $D_{\rm red}$.

\item Apply \cref{lem:II:proper-conductor-pushout} to
$h:Z\to S$, using $D_{\rm red}\subset Z$ and
$\Gamma_{\rm red}\subset S$ as its closed sets $A,C$,
respectively, with $j$ the inclusion and $k=h|_{D_{\rm red}}$.
The map is proper and surjective, the pairs have compatible
triangulations, and \eqref{cdp:eq:C.CR.6} gives its required
complement isomorphism. Thus
''' + display('cdp:st:C.2.CR.1', 'cdp:eq:C.CR.7') + r'''
Here $j_*$ is the isomorphism in the second step. The map
$k_*$ is zero, since the section $C\subset Z$ generates
$\pi_1(D_{\rm red})$ and $h(C)$ is a point.
The resulting isomorphism
$\pi_1(\Gamma_{\rm red})\to\pi_1(S)$ is induced by inclusion.
Every image-conductor component is dominated by a vertical
rational curve; its normalization is therefore $\PP^1$.
\cref{lem:II:curve-normalization-graph} makes
$\pi_1(\Gamma_{\rm red})$ a free group of rank
$b_1(\Gamma_{\rm red})$.

\item Apply \cref{night:P4R.1} to the same full fibre
$mS$ over the disc. It makes $\pi_1(S)$ virtually abelian.
The rational-component case of
\cref{lem:II:curve-normalization-graph} then bounds the
free rank in \eqref{cdp:eq:C.CR.7} by one.
The nonzero integral class on $S$ in \cref{cdp:st:D.1.9},
under the global hypotheses of the statement, excludes
rank zero. The same curve lemma gives
''' + display('cdp:st:C.2.CR.1', 'cdp:eq:C.CR.8') + r'''

\item Put $\epsilon=h^0(S,\omega_S)\in\{0,1\}$ and
$Q=\eta_*\OO_T/\OO_S$. Serre duality and
$\chi(\OO_S)=0$ give $h^1(\OO_S)=1+\epsilon$ and
$h^2(\OO_S)=\epsilon$. Since $S,T$ have the same
constant functions and $H^1(T,\OO_T)=H^2(T,\OO_T)=0$,
the normalization sequence identifies
$H^0(Q)=H^1(\OO_S)$ and $H^1(Q)=H^2(\OO_S)$.
The conductor-duality map of \cref{lem:II:conductor-duality}
is $Q=\omega_\Gamma\otimes\omega_S^{-1}|_\Gamma$.
The torsion twist has degree zero on each component,
so curve duality gives $\chi(\OO_\Gamma)=-\chi(Q)=-1$.
Consequently
''' + display('cdp:st:C.2.CR.1', 'cdp:eq:C.CR.9') + r'''
Apply the first assertion of \cref{cdp:st:C.2.VII.2}
to this compact irreducible hypersurface $S$, with its
torsion $\omega_S$ and $\chi(\OO_S)=0$. It gives
$\chi(\OO_{\Gamma_{\rm red}})\ge-1$.
All normalized image components are rational, so
$\chi(\OO_{\Gamma_{\rm red}})=n-\sum_x\delta_x$.
Equation~\eqref{cdp:eq:C.CR.8} and
$\delta_x\ge r_x-1$ give
$\chi(\OO_{\Gamma_{\rm red}})\le0$ and
$\sum_x(\delta_x-r_x+1)=-\chi(\OO_{\Gamma_{\rm red}})\le1$.

\item On the minimal bundle,
$e(Z_0)=4-4g$ and $e((D_0)_{\rm red})=2-2g+v$.
The complement formula of
\cref{lem:II:canonical-boundary-blowup}, applied to the
same successive divisors as in the second step, adds one
exactly at the $N_0$ centres of multiplicity one. Hence
\[
             e(Z\setminus D_{\rm red})=2-2g-v+N_0.
\]
The Euler formula in \cref{lem:II:proper-conductor-pushout},
for the same $h:Z\to S$, $D_{\rm red}$ and $\Gamma_{\rm red}$, and
$e(\Gamma_{\rm red})=n$ give \eqref{cdp:eq:C.CR.3}.
\end{enumerate}
\end{proof}
'''
cr1 = p.clean(cr1s+'\n'+cr1proof,'cdp:st:C.2.CR.1')

cr3s = statement('cdp:st:C.2.CR.3')
cr3s = p.edit(cr3s, cr3s.splitlines()[1],
    r'\StatementRecord{cdp:st:C.2.CR.3}{proved}{01BS}{\cref{cdp:st:C.2.CR.1,lem:II:contracted-section-duality,lem:II:conductor-two-branch-cycle}}',
    'D12,D14', 'cdp:st:C.2.CR.3',
    'Record the exact earlier owners for the graph and genus inputs.')
cr3s = p.edit(cr3s,
    r'In the genus-two situation of \ref{cdp:st:C.2.CR.2}, the component',
    r'Under all the hypotheses of \cref{cdp:st:C.2.CR.1}, with $g=2$, the component',
    'D12', 'cdp:st:C.2.CR.3',
    'State the inherited compact smooth Y, b1=b2=0, base P1 and full contracted-section data through CR1 explicitly before CR2 becomes an alias of the broader local P293 owner. The domain of CR3 is unchanged.')
cr3proof = r'''\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item Let $p=\pi(C)$, $q=\eta(p)$, and let $E_0$ be
the connected exceptional fibre containing $C$.
In the boundary tree of \cref{cdp:st:C.2.CR.1}, the
first nonexceptional vertex on every path from $C$
meets $E_0$. Its image in $T$ passes through $p$,
and its further image is a component of $\Gamma$ through
$q$. Apply \cref{lem:II:contracted-section-duality}
to these same data. Since $g=2$, $\Gamma$ is smooth
and reduced at $q$, so there is only one such component,
denoted $G$.

\item Suppose its generic transversal is a node.
Every strict conductor curve above $G$ has coefficient
one, and \cref{cdp:st:C.2.CR.1} makes it a leaf.
Thus each first nonexceptional vertex just found is
a leaf, and every strict conductor curve is such a leaf,
attached at one point to $E_0$. No additional exceptional
tail meets it, since this would raise its boundary
valence. The reduced conductor $D_T\subset T$ is
therefore a union of rational curves through $p$, each
smooth away from $p$ and with one branch at $p$.
Indeed $\pi$ is an isomorphism on each leaf away from
its single attachment point, and contracts the connected
$E_0$ to $p$. Its normalization-incidence graph is a star,
with cycle rank zero.

\item All these image curves pass through $q$, where
$\Gamma$ is smooth. Hence $\Gamma_{\rm red}=G$ is
irreducible. By \eqref{cdp:eq:C.CR.8},
$b_1(G)=1$ and $\sum_x(r_x-1)=1$.
Thus every multibranch point of $G$ has exactly two
branches, and lies away from the smooth point $q$.
For any such point apply
\cref{lem:II:conductor-two-branch-cycle} with
$N=T$, $\nu=\eta$, its curve $C=G$ and its inverse
conductor $D=D_T=(\pi D_{\rm red})_{\rm red}$.
Every component of $D_T$ dominates $G$ under the finite
map $\eta$, and no other image-conductor component
passes through the chosen point. The lemma gives
$\beta(D_T)\ge b_0(D_T)=1$, contradicting the star just
described. Therefore all germs of $G$ would be unibranch.

\item The normalization of $G$ is rational. If all its
germs are unibranch, its normalization is a continuous
bijection from the compact $\PP^1$ to the Hausdorff $G$,
hence a homeomorphism. This gives $\pi_1(G)=1$,
contrary to \eqref{cdp:eq:C.CR.1}.
The remaining generic transversal is a cusp.
Its transverse normalization is unibranch, with
conductor exponent two, so there is one strict
coefficient-two curve, of degree one over $G$.
\end{enumerate}
\end{proof}
'''
cr3 = p.clean(cr3s+'\n'+cr3proof,'cdp:st:C.2.CR.3')

un10 = r'''\begin{proposition}[Contracted irrational sections and their Euler number]\hypertarget{tag-01CN}{}\label{cdp:st:C.2.UN.10}
\StatementRecord{cdp:st:C.2.UN.10}{proved}{01CN}{\cref{lem:II:contracted-section-duality,cdp:st:C.2.UN.9,cdp:st:C.2.CR.4,cdp:st:C.2.CR.1,cdp:st:C.2.MH.2}}
\hypertarget{tag-01BU}{}\label{cdp:st:C.2.CR.5}
\StatementRecord{cdp:st:C.2.CR.5}{proved}{01BU}{}
\hypertarget{tag-01C6}{}\label{cdp:st:C.2.MH.3}
\StatementRecord{cdp:st:C.2.MH.3}{proved}{01C6}{}
Let $f:Y\to B_0$ be a proper holomorphic map from a
smooth complex threefold to a smooth curve, with connected
fibres and smooth general fibre a complex two-torus.
Let $mS$ be an irreducible nonnormal full fibre, and write
$h=\eta\pi:Z\to T\to S$ for the normalization and its
minimal resolution. Suppose that $p:Z\to B$ is a ruling
over a curve of positive genus, that its effective
adjunction divisor is $D=2C+V$, with $C$ a section and
$V$ vertical, and that $\pi$ contracts $C$. Then
''' + display('cdp:st:C.2.CR.5','cdp:eq:C.CR.19') + r'''
For a compact $Y$ with $b_1(Y)=b_2(Y)=0$ and
$B_0=\PP^1$, let $n,v,N_0$ have the meanings in
\cref{cdp:st:C.2.CR.1}. Then
\begin{equation}
\hypertarget{tag-00QG}{}\SsixEquationAliases{\label{cdp:eq:C.MH.15}}
             e(S)=n-v+N_0=0,\qquad n=v-N_0.
\hypertarget{tag-00D7}{}\label{cdp:eq:C.CR.20}
\end{equation}
\end{proposition}
\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item Put $g=g(B)$, $p_0=\pi(C)$ and $q=\eta(p_0)$.
Apply \cref{lem:II:contracted-section-duality} to the
map and full fibre in the statement, with the same
$S,T,Z,C,V$. It gives $g\in\{1,2\}$ and the residue
comparison \eqref{cdp:eq:C.UNCR.3}. For $g=2$, the
conductor ideal at $q$ is $(x,y)$, the point $p_0$
is the only normalization point over $q$, and the
smooth reduced conductor has generic transversal
a node or a cusp.

\item Consider a reduced local equation of $S$ at $q$.
Each positive-dimensional component of its critical
locus through $q$ has constant value zero, so lies in
its singular locus. A normal surface is regular in
codimension one, so every singular curve lies in the
nonnormal locus and hence in the conductor. After shrinking the germ,
the full reduced critical locus is the smooth conductor
curve above. In the node case
\cref{cdp:st:C.2.UN.9} gives the exact product
coordinates. Its normalization has two smooth points
over $q$, contradicting the unique $p_0$.
In the cusp case \cref{cdp:st:C.2.CR.4} gives the
product cusp $X^2+Y^3=0$ with normalization
\[
          (u,z)\longmapsto(X,Y,z)=(u^3,-u^2,z).
\]
This normalization is smooth. Its minimal resolution
is the identity near $p_0$, so cannot contract the
positive-genus section $C$ there. Both alternatives
exclude $g=2$, giving \eqref{cdp:eq:C.CR.19}.

\item Under the additional global hypotheses in the
statement, \cref{cdp:st:C.2.MH.2} applies to the
same irreducible full fibre and ruled normalization
resolution. It gives $e(S)=2-2g=0$.
Equation~\eqref{cdp:eq:C.CR.3}, for the same chosen
ruling blowdowns, gives $e(S)=n-v+N_0$ and hence
$n=v-N_0$. These are \eqref{cdp:eq:C.CR.20}.
\end{enumerate}
\end{proof}
'''
un10 = p.clean(un10,'cdp:st:C.2.UN.10')
p.equations.extend([
    dict(old_tag='C.CR.20',label='cdp:eq:C.CR.20',owner='cdp:st:C.2.UN.10'),
    dict(old_tag='C.MH.15',label='cdp:eq:C.MH.15',owner='cdp:st:C.2.UN.10')])

cr6s = statement('cdp:st:C.2.CR.6')
cr6s = p.edit(cr6s,cr6s.splitlines()[1],
    r'\StatementRecord{cdp:st:C.2.CR.6}{proved}{01BV}{\cref{cdp:st:C.2.CR.1,lem:II:contracted-section-duality,lem:II:conductor-duality,lem:II:plane-branch-conductor}; \cite[\S2.2.3, p.~60]{vanStraten1987}}',
    'D12,D18','cdp:st:C.2.CR.6',
    'Record the exact finite-duality and analytic vanishing inputs read at their current proofs and primary locus.')
cr6s = p.edit(cr6s,r'In the remaining case $g=1$ of \ref{cdp:st:C.2.CR.1}, let',
    r'In the case $g=1$ of \cref{cdp:st:C.2.CR.1}, let',
    'D04,D08','cdp:st:C.2.CR.6',
    'Keep the original global genus-one domain with a current numbered reference.')
cr6proof = r'''\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item Apply \cref{lem:II:contracted-section-duality}
with $g=1$ and these same $S,T,Z,C,V,p,q$.
Equations~\eqref{cdp:eq:C.CR.12} and
\eqref{cdp:eq:C.CR.13} give an element of the
conductor summand $I_p$ with nonzero ambient linear
part. Call it $x$ and extend it to coordinates
$(x,y,z)$ on the smooth threefold.

\item The full conductor ideal contains $x$, and
\cref{lem:II:conductor-duality} makes its quotient
pure one-dimensional Cohen--Macaulay. Its remaining
ideal in the regular ring $\C\{y,z\}$ is therefore
unmixed of height one. Its primary decomposition
is the intersection of its height-one primary
localizations, which are powers of the corresponding
principal primes in this factorial ring. Their
intersection is generated by their product.
This proves \eqref{cdp:eq:C.CR.21}, with all
multiplicities in $g$.

\item Let $D\subset W$ be a reduced plane curve germ,
let $\nu:\widetilde D\to D$ be its normalization,
and let $\rho:\widetilde W\to W$ be an embedded
resolution with smooth disjoint strict transform
$\widehat D$. Apply the finite-duality comparison
of \cref{lem:II:plane-branch-conductor} to its
equation $f_D$. It identifies
\[
           \mathfrak c_D\,\omega_D=\nu_*\omega_{\widetilde D}
\]
inside the meromorphic differentials on the normalized
branches. The residue sequence on $\widetilde W$ and
\cite[\S2.2.3, p.~60]{vanStraten1987}, applied to this
proper bimeromorphic $\rho$ with smooth source, give
a surjection
$\rho_*\omega_{\widetilde W}(\widehat D)\to
\nu_*\omega_{\widetilde D}$.

Thus for an ambient representative $a$ of a conductor
element, the residue of $a\,du\wedge dv/f_D$ lifts
to a meromorphic two-form on $\widetilde W$ with poles
only along $\widehat D$. Downstairs this lift and
$a\,du\wedge dv/f_D$ have the same residue, so differ
by a holomorphic two-form. Pullback of that difference
is holomorphic. The pullback of the displayed form
therefore has no exceptional pole. On the first
plane blowup, its order along the exceptional curve is
$\operatorname{ord}_0(a)+1-m$, where
$m=\operatorname{mult}_0D$. Hence
''' + display('cdp:st:C.2.CR.6','cdp:eq:C.CR.22') + r'''
Adding a multiple of $f_D$ preserves this bound
because $\operatorname{ord}_0(f_D)=m$.

\item At a general point of any conductor component
through $q$, the coordinate $x$ remains in the
conductor and has nonzero transverse linear part.
Indeed its smooth ambient zero plane contains the
curve. A transverse slice and \eqref{cdp:eq:C.CR.22}
give $m\le2$; the slice is singular, so $m=2$.
Weierstrass preparation gives a monic quadratic.
Complete its square and write its nonzero remaining
one-variable term as a unit times $v^{k+1}$.
Taking a $(k+1)$st root of that unit in the $v$
coordinate gives $u^2-v^{k+1}=0$. Each coordinate
change has nonzero derivative and inverse given by
the implicit function theorem.

\item For $k=2s-1$ the branches are $u=\pm v^s$.
They are smooth and have intersection multiplicity
$s$, so \cref{lem:II:plane-branch-conductor} gives
conductor $(v^s)$ on each. For $k=2s$, the
normalization is $v=t^2$, $u=t^{2s+1}$. Its value
semigroup $\langle2,2s+1\rangle$ contains every
integer at least $2s$ and omits $2s-1$, so its
conductor is $(t^{2s})$.
The generic transverse branch count of the finite
normalization equals the sum of its covering
degrees over the image component. These counts are
two and one in the respective cases.
\end{enumerate}
\end{proof}
'''
cr6 = p.clean(cr6s+'\n'+cr6proof,'cdp:st:C.2.CR.6')

header = r'\subsection{Contracted ruled boundaries}\label{subsec:II:contracted-ruled-boundaries}'
next_start = source.index(r'\begin{proposition}[The reduced horizontal case is a minimal elliptic ruled double-curve fibre]')
start = source.index(header)
old_unit = source[start:next_start]
next_header = r'''\subsection{Reduced horizontal boundaries}\label{subsec:II:reduced-horizontal-boundaries}
'''
new_unit = header+'\n\n'+'\n\n'.join(
    [duality.strip(),old['cdp:st:C.2.UN.9'].strip(),cr1.strip(),
     cr3.strip(),un10.strip(),cr6.strip()])+'\n\n'+next_header+'\n'
p.guard('complete contracted-boundary subsection',old_unit,new_unit,
        'Read and consolidate the entire contracted-boundary subsection. P293 absorbs CR2, UN9 is the earlier full-function node input, CR1 keeps all global topology and coefficient data, CR3 explicitly preserves its inherited global domain, UN10 absorbs CR5/MH3 at their exact local/global scopes, and CR6 keeps the complete conductor-order comparison. The next header bounds the actual finished subsection.')

alias_old = r'\hypertarget{tag-0080}{}\hypertarget{tag-0073}{}\hypertarget{tag-0093}{}\SsixEquationAliases{\label{cdp:eq:A.T.22}\label{cdp:eq:A.RT.11}\label{cdp:eq:C.22b}}'
alias_new = r'\hypertarget{tag-0080}{}\hypertarget{tag-0073}{}\hypertarget{tag-0093}{}\hypertarget{tag-00DC}{}\SsixEquationAliases{\label{cdp:eq:A.T.22}\label{cdp:eq:A.RT.11}\label{cdp:eq:C.22b}\label{cdp:eq:C.CR.5}}'
p.guard('canonical-boundary equation alias',alias_old,alias_new,
        'Transfer C.CR.5 to the single P232 Jacobian formula, with Z1=W,Z2=Wprime,m=d; preserve every receiving alias.')
p.equations.append(dict(old_tag='C.CR.5',label='cdp:eq:C.CR.5',owner='lem:II:canonical-boundary-blowup'))
p.record('D12,D19','cdp:eq:C.CR.5',
         display('cdp:st:C.2.CR.1','cdp:eq:C.CR.5'),alias_new,
         'The old formula is exactly P232 with Z1=W,Z2=Wprime and m=d. Its full proof and numerical coefficient conclusion are earlier. Move only the stable equation label and target into the existing alias hook; every C.CR.5 consumer still resolves to that same identity.')

p.guard('MH3 consolidated owner',old['cdp:st:C.2.MH.3'],'',
        'The whole MH3 statement, equation and proof are in the global clause of UN10 with both permanent identifiers preserved. Its final future global exclusion stays at the later UN7 owner.')

r6 = old['night:P4R.6']
a = r6.index('We exclude such a point directly.')
b = r6.index('Thus every exceptional block meets',a)
r6_old = r6[a:b]
r6_new = r'''At such a point choose a coordinate on the base vanishing
at the fibre. Its full local function is $f=u g^m$,
where $u$ is a unit and $g$ is the reduced local equation
of this normal isolated hypersurface singularity. The
critical-point germ of $g$ is isolated: each critical
component through the point has constant value zero,
so lies in the zero-dimensional singular locus of
$\{g=0\}$. The proper map restricted over a disc has
smooth nearby fibres complex two-tori, exactly the
hypotheses of \cref{cdp:st:A.5.15}. The isolated-critical-point
assertion of \cref{cdp:st:A.5.17} therefore applies
to this same $f,u,g,m$.

In that application its root is
$H=\exp((\log u)/m)g$, so $f=H^m$ exactly.
Its local-fibre inclusion is the identity on the chosen
coordinate neighbourhood,
\[
           K\cap H^{-1}(\delta)\hookrightarrow
                          f^{-1}(\delta^m).
\]
The proposition transports the compact Morse sphere
of square $-2$ into that local level and then into the
same torus fibre by this inclusion, which excludes
the isolated point.

'''
p300_proof = r6[r6.index(r'\begin{proof}'):].replace(r6_old,r6_new)
torsion_start = p300_proof.index(r'Finally, \cref{night:P4.12}')
torsion_end = p300_proof.index(r'\end{enumerate}',torsion_start)
p300_proof = p300_proof[:torsion_start]+p300_proof[torsion_end:]
finite_start = p300_proof.index(r'Write $\mathfrak c$')
finite_end = p300_proof.index('At a regular generic point',finite_start)
finite_old = p300_proof[finite_start:finite_end]
finite_new = r'''Write $\mathfrak c$ for the conductor on $N$.
Apply \cref{lem:II:conductor-duality} to $\nu:N\to S$.
Its evaluation-at-$1$ map identifies
$\operatorname{Hom}_{\OO_S}(\nu_*\OO_N,\OO_S)$ with
the conductor, by multiplication in the total quotient
ring. The same finite-duality map gives
\[
 \nu_*\omega_N
   =\mathcal Hom_{\mathcal O_S}(\nu_*\mathcal O_N,\omega_S),
 \qquad
 \omega_N\simeq\mathfrak c\otimes\nu^*\omega_S.
\]
'''
p300_proof = p300_proof[:finite_start]+finite_new+p300_proof[finite_end:]
unit_old = r'''A conductor curve through $p$ has strict transform meeting
$\pi^{-1}(p)$, by properness. Therefore a block disjoint from
$D_{\rm str}$ lies over a point where $\nu$ is an isomorphism.
Its image in $S$ would be a normal isolated hypersurface
singularity.'''
unit_new = r'''A conductor curve through $p$ has strict transform meeting
$\pi^{-1}(p)$, by properness. Thus a block disjoint from
$D_{\rm str}$ has unit conductor at $p$. To identify its
image, write the semilocal normalization over
$q=\nu(p)$ as $\prod_i B_i$ and its conductor as
$\bigoplus_i\mathfrak c_i\subset R=\OO_{S,q}$.
If $\mathfrak c_i=B_i$ at $p$, its element $1$ extended
by zero on the other factors is an idempotent of the
local ring $R$. Hence there is only one factor and the
conductor is all of $R$. The finite normalization is
an isomorphism near $q$. Since $p$ is singular on $N$,
the image $q$ would be a normal isolated hypersurface
singularity.'''
assert unit_old in p300_proof
p300_proof = p300_proof.replace(unit_old,unit_new)
p300_proof = p300_proof.replace(
    'The reduced support is a Cartier hypersurface in the smooth\nthreefold,',
    'The reduced surface is a Cartier hypersurface in the smooth\nthreefold,')
general_end = r'''It follows that $d_i\ge0$. A zero coefficient forces $b=0$
on the connected block. Each of its curves is then a smooth
rational $(-2)$-curve, and the block is disjoint from
$D_{\rm str}$.

\item We now prove that every exceptional block meets
$D_{\rm str}$.'''
general_new = r'''It follows that $d_i\ge0$. A zero coefficient forces $b=0$
on the connected block. Each of its curves is then a smooth
rational $(-2)$-curve, and the block is disjoint from
$D_{\rm str}$. Conversely, a block meeting $D_{\rm str}$
has some $b_i>0$, hence every $d_i>0$. The same conclusion
holds when a component $E_i$ has positive geometric
genus: then $p_a(E_i)\ge1$ and $E_i^2<0$, so
$K_T\cdot E_i>0$. This proves all assertions for an
arbitrary compact reduced hypersurface.

\item Now impose the proper torus-degeneration hypotheses
of the second assertion. We prove that every exceptional
block meets $D_{\rm str}$.'''
assert general_end in p300_proof
p300_proof = p300_proof.replace(general_end,general_new)
p300 = r'''\begin{lemma}[Conductor divisors on hypersurface resolutions]\hypertarget{tag-P300}{}\label{lem:II:proper-conductor-divisor}
\StatementRecord{lem:II:proper-conductor-divisor}{proved}{P300}{\cref{lem:II:conductor-duality,lem:II:exceptional-intersection,cdp:st:A.5.17}}
Let $S$ be a compact reduced hypersurface in a smooth
complex threefold $X$. Write $\nu:N\to S$ for its
normalization, $\pi:T\to N$ for the minimal resolution
and $\rho=\nu\pi$. The pullback of local generators of
$\omega_S$ defines an effective integral divisor $D$ with
\[
                  \omega_T(D)\simeq\rho^*\omega_S.
\]
Its strict-transform conductor coefficients are the
positive integral conductor exponents. The coefficients
on each connected exceptional configuration are all
strictly positive as soon as that configuration meets
the strict conductor or contains a curve of positive
geometric genus. A zero coefficient forces the entire
configuration to consist of rational $(-2)$-curves
disjoint from the strict conductor.

Now let $f:X\to\Delta$ be proper with connected fibres,
smooth over $\Delta^*$, with smooth fibres complex
two-tori and central fibre $mS$, where $S$ is irreducible.
Then every connected exceptional configuration meets
the strict conductor and has strictly positive coefficients,
the reduced singular locus of $S$ is its reduced
conductor image, and
\[
       D_{\rm red}=\rho^{-1}((\operatorname{Sing}S)_{\rm red}).
\]
The map $\rho$ is an isomorphism between the complements
of these two reduced closed sets.
\end{lemma}
''' + p300_proof
p300 = p.clean(p300,'lem:II:proper-conductor-divisor')
r6s = statement('night:P4R.6')
r6s = r6s.replace(r'\StatementRecord{night:P4R.6}{proved}{02YI}{\SeriesRef{night:P4.12}}',
    r'\StatementRecord{night:P4R.6}{proved}{02YI}{\cref{lem:II:proper-conductor-divisor,night:P4.12}}')
r6_receiving = r6s+r'''
\begin{proof}
Restrict $f$ to a sufficiently small disc about the
value of $mS$ and apply \cref{lem:II:proper-conductor-divisor}
to this restriction, with the same $S,N,T,\nu,\pi,\rho$.
Its divisor $D$ is defined by the orders of the pullback
of the same local generator of $\omega_S$. It gives the
line-bundle identity, effectiveness, support equality
and all assertions about conductor and exceptional
coefficients in the statement.

Under the global hypotheses here, \cref{night:P4.12}
gives $\omega_S^{\otimes m}\simeq\OO_S$. Therefore
\[
 (\omega_T(D))^{\otimes m}
   \simeq\rho^*(\omega_S^{\otimes m})\simeq\OO_T,
\]
which proves the torsion conclusion.
\end{proof}
'''
p.guard('P300 support owner and R6 global application',r6,p300+'\n'+r6_receiving,
        'Extract the divisor/effectiveness proof for any compact reduced hypersurface and the full support proof for the proper torus degeneration before R6. Keep R6’s full original global statement, stable labels and tag, with its exact P300 second-clause application and final P4.12 torsion conclusion.')
p.record('D12,D14','night:P4R.6',r6_old,r6_new,
         'Read all of R6 and all of A.5.17, including the first common-root proof, boundary transport and spherical intersection calculation, and compare A.5.15 hypotheses. In P300 the exact isolated-normal-point specialization is f=u g^m, H=u^(1/m)g and identity inclusion into f^(-1)(delta^m). This removes the repeated gradient/triangulation/Morse-sphere proof and its later P4.16 input. R6 applies that earlier owner with all original global hypotheses unchanged.')
p.record('D12','lem:II:proper-conductor-divisor',finite_old,finite_new,
         'Apply the complete earlier P222 evaluation/multiplication finite-duality proof on the identical finite normalization. The conductor isomorphism and every pole coefficient remain; no surface formula is substituted for a curve formula.')
p.record('D22','lem:II:proper-conductor-divisor',unit_old,unit_new,
         'Make the inherited unit-conductor-to-normality implication explicit using the branch-product normalization and the idempotent extended by zero. This proves that a unit conductor at the chosen normalization point forces one branch and an isomorphism at its image; no new geometric hypothesis or changed conclusion is introduced.')
p.record('D12,D14','lem:II:proper-conductor-divisor',r6,p300+'\n'+r6_receiving,
         'The first three proof steps use only a compact reduced hypersurface, its finite normalization and minimal resolution: degree zero follows because each exceptional curve maps to a point. They prove effectiveness, and a positive-geometric-genus component has K.E>0, hence strictly positive coefficients on its entire connected block by P243. The proper torus degeneration is imposed only for the fourth-step isolated-normal-point exclusion and the full support equality. The only original global input is the final P4.12 torsion assertion, which stays in the unchanged-scope R6 application. P300 is earlier than R6, CR1 and UN7 and introduces no forward P281/UN17 input.')
p.record('D12,D22','lem:II:proper-conductor-divisor',general_end,general_new,
         'Expose the exact proved generality of the first three steps before the proper-torus support assertion. The additional positive-genus sentence follows directly from p_a(E)>=1, E^2<0 and -M^{-1}>0. The complete proper-torus conclusion and every original R6/CR1/UN7 hypothesis remain. For P4.52, beta:Xprime->X is the ambient point blowup, Sprime is the compact strict transform, rho1:T1->Sprime is normalization followed by minimal resolution, and P300 first clause applies to (Sprime,Xprime,T1,rho1). Adjunction gives omega_Sprime=mu^*omega_S tensor O((2-d)E), so the same pulled-back generator gives D_old=D1+(d-2)rho1^*E. The coefficient on strict H is exactly 2=(d-2)n+a with a>=0; a>0 when H is exceptional because H has positive genus. No torus-fibre hypothesis is asserted for Sprime. The concrete P4.52 consumer replacement is in the next bounded package.')
p.rows[-1]['old_location']='receiving P300 generality comparison before admission; P4.52 strict-transform application'

un7 = block(source,'cdp:st:C.2.UN.7')
un7_old = r'''The proof of \eqref{cdp:eq:C.CR.6} uses only this
connectedness, minimality and the isolated
singularity exclusion. It gives'''
un7_new = r'''Apply \cref{lem:II:proper-conductor-divisor} to
$f|_U:U\to\Delta$, with its $N=T$, resolution surface
equal to $Z$, $\nu=\eta$ and $\rho=h$.
The divisor is the same $D$, defined by the pullback
of a local generator of $\omega_S$.
The torsion and numerical line in
\cref{lem:II:torus-tube-numerical} were proved separately
for this same tube and are the input to the boundary
blowdown comparison above. The support and complement
conclusions of \cref{lem:II:proper-conductor-divisor} give'''
assert un7_old in un7
p.guard('UN7 proper-disc support application',un7_old,un7_new,
        'Keep UN7’s original proper-disc domain. Apply P300 to its exact local maps and keep its P281 numerical input separate, so the rewritten CR1 global application is not used beyond its scope.')
p.record('D12,D14','cdp:st:C.2.UN.7',un7_old,un7_new,
         'Read the complete current UN7 proof, including its contracted case and the proper local numerical inputs. The former reference to the proof of C.CR.6 now points to the common P300 owner with X=U,N=T,T=Z,nu=eta,rho=h. The C.UI.14 formula and every later topology, parity, finite-character and global-exclusion step are unchanged.')
un7_record_old = un7.splitlines()[1]
un7_record_new = un7_record_old.replace(
    r'\SeriesRef{cdp:eq:C.CR.6}, \SeriesRef{cdp:st:C.2.CR.1}',
    r'\cref{lem:II:proper-conductor-divisor,lem:II:torus-tube-numerical}')
assert un7_record_new != un7_record_old
p.guard('UN7 exact local dependency record',un7_record_old,un7_record_new,
        'Replace only the inherited global proof dependency by its exact local owner and separately proved local numerical input.')

(OUT/'S6_SERIES_PUBLISH_II_sec07_contracted_P300.tex').write_text(p300,newline='\n')
(OUT/'S6_SERIES_PUBLISH_II_sec07_contracted_R6_receiving.tex').write_text(r6_receiving,newline='\n')

for k,new in [('cdp:st:C.2.CR.1',cr1),('cdp:st:C.2.CR.3',cr3),
              ('cdp:st:C.2.UN.10',un10),('cdp:st:C.2.CR.6',cr6)]:
    p.record('D12',k,old[k],new,
             'Complete original/current and receiving comparison: all statement hypotheses and conclusions are preserved through the explicit owner and map comparisons in the companion comparison file. Repeated arguments become exact earlier applications; the specific coefficient, graph, residue and local-coordinate calculations remain.')
p.record('D12','cdp:st:C.2.CR.5',old['cdp:st:C.2.CR.5'],un10,
         'The local UN10 conclusion proves genus one on the same full fibre, normalization, resolution and contracted section. The additional compactness, b1=b2=0 and base P1 are explicitly stated before the old CR5 Euler conclusion, and the chosen n,v,N0 are those of CR1.')
p.record('D12','cdp:st:C.2.MH.3',old['cdp:st:C.2.MH.3'],un10,
         'Merge the complete MH3 genus-one/e(S)=0/n=v−N0 conclusion into the global clause of UN10 using the identical MH2 specialization and CR1 blowdown data. C.MH.15 and C.CR.20 label one equation containing both full payloads; the later UN7 exclusion remains at its proved owner.')
p.record('D20','cdp:st:C.2.UN.10',
         'The map is f:Y→B, while the ruling base is unnamed and CR5 uses B for the ruling base.',
         'The map is f:Y→B0 and the ruling is p:Z→B, as in P293.',
         'Rename only the fibration target B to B0 and name the same ruling target B. The normalization, resolution and section are unchanged; g(B) in C.CR.19 is unambiguously the ruling genus.')
p.record('D14','subsec:II:contracted-ruled-boundaries',old_unit,new_unit,
         'The local order is P293, the already proved full-function UN9, CR1 coefficient/topology data, CR3 graph exclusion, the single UN10 genus/Euler owner, then CR6 local conductor structure. All premises precede their applications. The new next-subsection header bounds the finished unit; movement alone closes no defect or restructuring row.')
p.record('D17,D18','cdp:st:C.2.CR.6',
         'The residue sequence on the resolution and Grauert--Riemenschneider vanishing identify the right side with the residue of rho_* omega(hat D).',
         r'The residue sequence and \cite[\S2.2.3, p.~60]{vanStraten1987} give rho_* omega(hat D) → nu_* omega; the lift differs from a du∧dv/f_D by a holomorphic two-form, so the first exceptional order is ord(a)+1−m.',
         'Reopened the primary analytic theorem at its exact locus. Keep the short explicit residue/lift/first-blowup comparison because that theorem states vanishing, not this conductor-order formula. The one-dimensional finite-duality input is the complete P282 proof, not a surface-duality substitution.')

# Each removed source reference remains logged at the exact consolidated owner.
receiving = '\n'.join([duality,cr1,cr3,un10,cr6,p300,r6_receiving,un7_new])
for k in ['cdp:st:C.2.CR.1','cdp:st:C.2.CR.2','cdp:st:C.2.CR.3',
          'cdp:st:C.2.CR.5','cdp:st:C.2.CR.6','cdp:st:C.2.UN.10',
          'cdp:st:C.2.MH.3']:
    for match in re.finditer(r'\\SeriesRef\{([^{}]+)\}',old[k]):
        label = match.group(1)
        target = (r'\eqref{' if ':eq:' in label else r'\cref{')+label+'}'
        p.record('D04',k,match.group(0),target,
                 'Use the current statement/equation number. Where its repeated proof is consolidated, the comparison gives the exact receiving owner and application; no printed run identifier remains.')
    for match in re.finditer(r'\b(?:actual|retained|specified|supplied)\b',old[k]):
        context = old[k][max(0,match.start()-65):min(len(old[k]),match.end()+90)]
        p.record('D08',k,context,'The receiving proof names the same map, divisor or chosen blowdown sequence directly.',
                 'Remove production vocabulary in the complete receiving comparison; all associated mathematical data and multiplicities are preserved.')
    for match in re.finditer(r'\((C\.(?:CR|MH)\.\d+)\)',old[k]):
        oldtag=match.group(1)
        p.record('D04,D19',k,match.group(0),
                 r'\eqref{cdp:eq:'+oldtag+'}',
                 'Replace the literal earlier numbering by the current equation reference; its exact label, permanent target and payload survive at the mapped owner.')
    for literal,label in [('C.2.CR.1','cdp:st:C.2.CR.1'),
                          ('C.2.VII.2','cdp:st:C.2.VII.2'),
                          ('A.5.16','cdp:st:A.5.16')]:
        for match in re.finditer(r'(?<![:A-Za-z0-9])'+re.escape(literal),old[k]):
            p.record('D04',k,match.group(0),r'\cref{'+label+'}',
                     'Remove the printed compendium locator. The receiving proof uses the exact current owner; in the support comparison its stronger general P300 owner is applied directly instead of an out-of-scope rational special case.')
p.record('D02,D11','cdp:st:C.2.UN.10',
         'without ambient Betti assumptions; its proof ... requires no ambient Betti hypothesis or transgression class.',
         'The local proper-map hypotheses are stated positively; the global Euler clause separately states compactness, b1=b2=0 and base P1.',
         'State each domain once and preserve it exactly in the consolidated owner, removing repeated negative scope narration.')
p.record('D02,D08,D11','cdp:st:C.2.MH.3',
         'this reduction supplies no example of an actual CDP fibre.',
         'The later UN7 owner retains the global nonoccurrence result proved from its local e(S)≥2 and pi1(S)=1 calculation.',
         'Remove the defensive closing sentence and keep the mathematical exclusion at its single proved owner. The complete UN7 current and receiving proof has been reread.')
p.record('D17','cdp:st:C.2.CR.1',
         'Repeat the compact quotient, double mapping cylinder, van Kampen and blowup complement calculations inside CR1.',
         'Apply P294 to h:Z→S,A=D_red,C=Gamma_red,j the inclusion,k=h|D, and P232 to the same successive divisors with m=d.',
         'The exact primary cofibration/van Kampen loci were opened for P294, whose complete current proof was reread. The receiving text keeps the proper-map, inclusion inverse, coefficient and Euler data used here instead of repeating the general proofs.')
p.record('D23','cdp:st:C.2.CR.1',
         'The proposition identifies the singular support ... [equation ending with a period] and makes h ...',
         'The lemma identifies the reduced singular locus ... [equation ending with a period] It also makes h ...',
         'The final receiving comparison identifies P300 as a lemma and fixes sentence punctuation after C.CR.6.')
p.rows[-1]['old_location']='contracted receiving proposal / P300 application before final comparison'
p.record('D25','cdp:st:C.2.UN.10',
         'A reduced hypersurface is Cohen–Macaulay, and is normal at every regular codimension-one point; thus every singular curve is in the conductor locus.',
         'A normal surface is regular in codimension one, so every singular curve lies in the nonnormal locus and hence in the conductor.',
         'The receiving comparison caught the reversed explanatory implication in this draft sentence and replaced it by normal-implies-regular-in-codimension-one. The inherited original conclusion that every singular curve is nonnormal was correct and remains unchanged; no original statement is refuted or refined.')
p.rows[-1]['old_location']='contracted receiving proposal / UN10 critical-curve explanation before final comparison'

for equation in re.findall(r'\\begin\{equation\}([\s\S]*?)\\end\{equation\}',new_unit):
    assert not re.search(r'\n[ \t]*\n',equation)
for k in ['cdp:st:C.2.CR.2','cdp:st:C.2.CR.5','cdp:st:C.2.MH.3']:
    assert new_unit.count(r'\label{'+k+'}')==1
assert old['cdp:st:C.2.UN.9'] in new_unit
p.write(new_unit)
