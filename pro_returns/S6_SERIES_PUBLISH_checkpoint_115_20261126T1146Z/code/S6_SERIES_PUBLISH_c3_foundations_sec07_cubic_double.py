from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *

s=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
p=Package('cubic_double','night:P4.53')

old222=block(s,'lem:II:conductor-duality')
new222=old222.replace('For compact $S$, these maps induce',r'''The ideal $\mathfrak c_T$ is reflexive. At a point
$q\in T$ with $(\mathfrak c_T)_q=\OO_{T,q}$, the
normalization is an isomorphism over a neighbourhood
of $\eta(q)$, including every local branch of $S$ there.
For compact $S$, these maps induce''')
new222=new222.replace('Finally $\\mathcal Ext^1_S',r'''The canonical sheaf on the normal surface $T$ is reflexive,
so \eqref{cdp:eq:A.RT.5} gives the asserted reflexivity.
For the local isomorphism, put $R=\OO_{S,\eta(q)}$, let
$B$ be its finite semilocal normalization, and write
$\mathfrak q\subset B$ for the maximal ideal of $q$.
The equality $\mathfrak c B_{\mathfrak q}=B_{\mathfrak q}$
gives $c\in\mathfrak c\setminus\mathfrak q$.
Since $c\in R$ and $\mathfrak q\cap R=\mathfrak m_R$,
the element $c$ is a unit of $R$. The defining inclusion
$cB\subset R$ then gives $B=R$. The finite coherent
quotient $\eta_*\OO_T/\OO_S$ vanishes at $\eta(q)$,
and hence on a neighbourhood of that point.

Finally $\mathcal Ext^1_S''')
assert new222!=old222
p.record('D12,D17,D20','lem:II:conductor-duality',old222,new222,
 'Consolidate the exact unit-conductor criterion from P300/P453 at finite duality. Freshly opened Reid1994 Proposition2.3 and full proof p703, Theorem2.6 and full proof pp704–705; preserve all existing duality and compact-section maps. The additional proof explicitly treats every branch of the finite semilocal normalization.')
p.guard('P222-unit-conductor',old222,new222,'Single earlier owner for reflexive conductor and whole-germ normality; all old assertions and identifiers retained.')

old300=block(s,'lem:II:proper-conductor-divisor')
a=old300.index('To identify its\nimage,')
b=old300.index('Since $p$ is singular on $N$,',a)
oldpara=old300[a:b]
newpara=r'''Put $q=\nu(p)$. Apply the unit-conductor assertion of
\cref{lem:II:conductor-duality} to $\nu:N\to S$, at this
same $p$ above $q$. Its local rings are
$R=\OO_{S,q}$ and the finite semilocal normalization
$B=(\nu_*\OO_N)_q$. The unit conductor at $p$ gives
$B=R$, so $\nu$ is an isomorphism near $q$.
'''
p.record('D12,D20','lem:II:proper-conductor-divisor',oldpara,newpara,
 'Apply the complete local-ring criterion at P222 on the identical finite normalization; replace the repeated semilocal-factor/idempotent argument, keeping all proper-torus and full-function/root hypotheses and conclusions.')
p.guard('P300-unit-conductor-application',oldpara,newpara,'Bounded paragraph only; the admitted A.5.3 application and full proper-torus support proof remain.')
new300=old300.replace(oldpara,newpara)

start=s.index(r'\subsection{The cubic double line and its weighted leading fibre}')
stop=s.index(r'\subsection',start+12)
oldunit=s[start:stop]
old=block(oldunit,'night:P4.53')
head,body=old.split(r'\begin{proof}',1)
pieces=body.split(r'\item ')[1:]
assert len(pieces)==14
pieces[-1]=pieces[-1].split(r'\end{enumerate}',1)[0]
head=head.replace(r'\StatementRecord{night:P4.53}{proved}{02XS}{}',r'\StatementRecord{night:P4.53}{proved}{02XS}{\cref{night:P4.52,lem:II:weighted-initial-monodromy,lem:II:conductor-duality,lem:II:plane-branch-conductor,cdp:st:A.5.3}}')
head=head.replace(r'''In the remaining positive ruled support of \cref{sec:II:night-sign},
blow up the
multiplicity-three image of the contracted horizontal
section $H$, normalize the strict transform $S_1$, and
take its minimal resolution $T_1$.''',r'''In the setting of \cref{night:P4.52}, blow up the
multiplicity-three image of the contracted horizontal
section $H$, normalize the strict transform $S_1$, and
take its minimal resolution $T_1$.''')
head=head.replace('No generic\ntransverse type is imposed on the original critical curve.','The generic transverse types along the original critical\ncurve are arbitrary.')
p.record('D01,D02,D08,D14,D25','night:P4.53',old.split(r'\begin{proof}')[0],head,
 'Resolve the inherited remaining-support phrase to the full preceding P452/P314 global setting; state arbitrary transverse-type scope positively. No domain or conclusion changes.')

pieces[0]=r'''Use the comparison maps of \cref{night:P4.52}:
$\beta:Y_1\to Y$ is the point blowup, $S_1$ is the
compact strict transform, and $\rho_1:T_1\to S_1$ is
normalization followed by minimal resolution.
Apply \cref{cdp:st:A.5.3} to this same compact hypersurface
$S_1\subset Y_1$, and denote its canonical effective divisor
by $D_1$. With $E$ the ambient exceptional plane, put
$n=\operatorname{ord}_H(\rho_1^*E)>0$ and
$a=\operatorname{coeff}_H(D_1)$. The coefficient equation
\eqref{eq:II:manual:4.52d}, now with multiplicity three,
is $2=n+a$. Hence $(n,a)=(2,0)$ or $(1,1)$.

'''
p.record('D12,D20,D22','night:P4.53','Use the comparison maps ... The pole identity is $2=n+a$.',pieces[0],
 'Identify the compact strict transform, its ambient blowup and the precise A.5.3 divisor; retain the coefficient equation and its two integral solutions.')
pieces[3]=pieces[3].replace('The branch formula\n',r'The branch formula of \cref{lem:II:plane-branch-conductor}'+'\n')
p.record('D12,D17','night:P4.53',r'The branch formula $c_i=2\delta_i+\sum_{j\ne i}I_{ij}$.',pieces[3],
 'Apply the earlier full plane-conductor owner to these same normalized transverse branches, including intrinsic delta terms and all pairwise intersections.')
# Keep all discriminant cases and place their numerical partitions at the estimate.
pieces[7]=pieces[7].replace('The total transverse Milnor-number sum is thus\n$M\\le2$.',r'''The positive-genus multiplicity partitions of the sextic are
$(1,1,1,1,1,1)$, $(2,1,1,1,1)$ and $(3,1,1,1)$;
their transverse Milnor-number sums are respectively
$0,1,2$. Thus $M\le2$.''')
pieces[8]=pieces[8].replace('four distinct simple roots.',r'''four distinct simple roots, the partition
$(1,1,1,1)$.''')
p.record('D22','night:P4.53',pieces[13],pieces[7]+pieces[8],
 'Place the complete sextic/quartic multiplicity partitions beside the genus and Milnor estimates that use them; retain every numerical conclusion.')

transport=r'''The local reduced equation is the same $g$ as in
\cref{night:P4.52}; its full fibration function is
$\Phi=u g^m$. That proof applies the first clause of
\cref{night:P4.51}, using $b_1(S)>0$, to this full fibre.
Its root $g_u=\exp((\log u)/m)g$, the function denoted
$h$ there, and the inclusion
$g_u^{-1}(\delta)\hookrightarrow\Phi^{-1}(\delta^m)$
therefore give zero intersection pairing on local $g$-levels.
Apply the first clause of
\cref{lem:II:weighted-initial-monodromy} with
\[
 D_\epsilon(x,y,z)=(\epsilon x,\epsilon^2y,\epsilon z),
 \qquad G_\epsilon=\epsilon^{-5}g\circ D_\epsilon,
 \qquad c=1.
\]
Since $G_\epsilon\to P_5$ with all derivatives on compact
sets, every compact intersection calculation on $P_5=1$
maps to a local $g=\epsilon^5$ level. Its intersection
form is consequently zero.

'''
p.record('D12,D14,D20,D25','night:P4.53',pieces[11],transport,
 'Use P322 before the monodromy inequalities; preserve the exact weights, scaled function, original unit and full multiplicity, and the same local-fibre inclusion. P451 applies through the explicitly established b1(S)>0 of P452.')

monodromy=r'''The weighted action of $\mu_5$ on $F=\{P_5=1\}$ is
free, and its quotient is $\mathbb P(1,2,1)\setminus C_5$.
Indeed the only possible nontrivial stabilizer of the
weighted $\C^*$ action lies at the weighted vertex,
which belongs to $C_5$. Thus the quotient map is an
unramified fivefold cover. The third clause of
\cref{lem:II:weighted-initial-monodromy}, with
$w=(1,2,1)$ and $d=5$, identifies its weighted scalar
monodromy with local Milnor monodromy and gives
\[
 \operatorname{rank}(T-I)
 \ge4\chi\bigl(\mathbb P(1,2,1)\setminus C_5\bigr)
 \ge8.
\]
Here one may use the invariant proper semialgebraic norm
$R=|y|^2+(|x|^2+|z|^2)^2$: it satisfies
$R(D_\epsilon z)=|\epsilon|^4R(z)$, and the normalized
gradient construction of that lemma applies to it.
The two resulting compact cores both include into $F$
by homotopy equivalences; these inclusions identify their
homology, monodromy and compact intersection calculations.
The polynomial $P_5$ is reduced by the factorization above.
Its zero pairing therefore satisfies the second clause
of the lemma, with the transverse sum just computed:
$\operatorname{rank}(T-I)\le M\le3$.
This also includes an isolated critical point, for which
$M=0$. The bounds differ by at least $8-3=5$, excluding
every dominating $H$.

'''
p.record('D12,D17,D22','night:P4.53',pieces[10]+pieces[13],monodromy,
 'P322 owns the opened Siersma variation/Wang calculation and Hatcher free-action character proof. Keep the exact free mu5 quotient, explicit old weighted norm and its scaling, reducedness, all upper/lower bounds, isolated case and gap; no second proof remains.')

normality=r'''Thus $H$ is exceptional over the normalization of $S_1$.
The positive-genus refinement in \cref{cdp:st:A.5.3}
gives strictly positive coefficients on its entire
connected exceptional block. In particular $a>0$, so
$n=a=1$. Adjunction on this smooth positive-genus curve
gives
\[
                    0=2g(H)-2+(D_1-H)\cdot H.
\]
Every term on the right is nonnegative. Hence $g(H)=1$
and $H$ meets no other component of $D_1$. The whole
exceptional block has positive coefficients and is connected,
so it consists of $H$ alone and is disjoint from the
strict conductor.

Let $q$ be the normalization point below $H$ and
$p_1$ its image in $S_1$. A conductor curve through $q$
would have strict transform meeting the proper exceptional
fibre $H$. Thus the conductor has no codimension-one
support near $q$. It is reflexive by
\cref{lem:II:conductor-duality}, so its stalk at $q$ is
the unit ideal. Apply that lemma to
$A=\OO_{S_1,p_1}$, its finite semilocal normalization $B$,
and this same $q$: it gives $B=A$ on the entire local
germ. There are consequently no additional local branches.
The strict-transform germ is normal and its minimal
resolution has the single smooth elliptic exceptional
curve $H$. This is an isolated simple elliptic singularity.

'''
p.record('D12,D17,D20,D25','night:P4.53',pieces[12],normality,
 'A.5.3 supplies positivity on the exact exceptional block, so adjunction leaves H alone. P222 supplies reflexivity and the complete local-ring isomorphism A=B, including all branches. Freshly opened Reid1994 exact duality proofs support the comparison; no assertion is weakened.')

# The projective curve C5 is the curve formerly denoted D; D1 stays the pole divisor.
for i in [6,7,8,9]:
    pieces[i]=re.sub(r'(?<![A-Za-z_])D(?![A-Za-z_0-9])','C_5',pieces[i])
p.record('D20','night:P4.53','D={P5=0} in P(1,2,1)',
 'C5={P5=0} in P(1,2,1); D1 is the canonical pole divisor',
 'The identity map on the same weighted projective zero set names it C5, avoiding collision with the pole-divisor notation; every occurrence and Euler expression follows that explicit identification.')

for i in [1,2,3]:
    pieces[i]=re.sub(r'(?<![A-Za-z_])m(?![A-Za-z_0-9])',lambda m:r'\mu_L',pieces[i])
p.record('D20','night:P4.53','m is the Weierstrass degree over L; later m is the full fibre multiplicity; h is both cover degree and unit root.',
 'The Weierstrass degree is mu_L, exactly the multiplicity of L in the cubic; m is the unchanged full fibre multiplicity. The unit root is g_u=exp(log(u)/m)g, equal to h in P452; h here remains the covering degree.',
 'Separate distinct quantities by their explicit definitions and identity map; the degree sum and every numerical bound are unchanged.')

ordered=pieces[:6]+[transport]+pieces[6:10]+[monodromy,normality]
new=head+r'\begin{proof}'+'\n'+r'\begin{enumerate}[label=\arabic*.,leftmargin=*]'+'\n'
new+=''.join(r'\item '+x for x in ordered)
new+=r'\end{enumerate}'+'\n'+r'\end{proof}'+'\n'
new=p.clean(new,'night:P4.53')
new=new.replace('Proposition~\\ref{','\\cref{')
newunit=(r'\subsection{The cubic double line and its weighted leading fibre}'
         r'\label{subsec:II:cubic-double-line}'+'\n\n'+new+'\n')
p.guard('P453-complete-subsection',oldunit,newunit,
 'Complete subsection replacement, keeping all mathematical conclusions, degree/discriminant cases and every old label/target; earlier common owners replace exact duplicate proofs.')
p.write(newunit)
for key,text in [('P222',new222),('P300',new300),('P453',new)]:
    (OUT/f'S6_SERIES_PUBLISH_II_sec07_cubic_double_{key}.tex').write_text(text+'\n',newline='\n')
