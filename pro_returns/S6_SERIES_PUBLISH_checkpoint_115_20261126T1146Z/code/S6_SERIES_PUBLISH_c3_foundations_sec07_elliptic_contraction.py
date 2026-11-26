from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *

s=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
p=Package('elliptic_contraction','night:P4.54')

# Expose the local assertion already proved in A.5.17, then its torus application.
old517=block(s,'cdp:st:A.5.17')
new517=old517.replace(
 r'\begin{proposition}[Isolated singularities are excluded and suspension germs are transverse products]',
 r'\begin{proposition}[Local vanishing spheres and transverse suspension products]')
new517=new517.replace(r'Let $f:Y\to C_0$ have the hypotheses of \ref{cdp:st:A.5.15}.',r'''Let $H:(\C^3,0)\to(\C,0)$ be a holomorphic germ with
an isolated critical point at the origin. Every sufficiently
small local Milnor fibre of $H$ contains a compact embedded
two-sphere of self-intersection $-2$.

Let $f:Y\to C_0$ have the hypotheses of \ref{cdp:st:A.5.15}.''')
a=new517.index(r'\item Replace $h$')
b=new517.index(r'\item Choose a small closed ball',a)
root=new517[a:b].replace(r'\item Replace $h$',r'\item For the torus assertion, replace $h$')
new517=new517[:a]+new517[b:]
new517=new517.replace(r'\item Choose a small closed ball $K\subset\C^3$ such that',r'''\item We first use the germ $H$ in the local assertion.
Choose a small closed ball $K\subset\C^3$ such that''',1)
oldembed=r'''into $K\cap H^{-1}(\epsilon_0)$ for a nonzero small
$\epsilon_0$, which is a submanifold of the
global torus $Y_{\epsilon_0^m}$.'''
newembed=r'''into $K\cap H^{-1}(\epsilon_0)$ for a nonzero small
$\epsilon_0$. Varying $\epsilon_0$ in the punctured
Milnor disc transports the same sphere to every
sufficiently small nonzero local level.'''
assert oldembed in new517;new517=new517.replace(oldembed,newembed,1)
oldend=r'''The transported sphere has the same square in the
torus, whose $\pi_2$ is zero, a contradiction.

\item Factor the analytic plane function as'''
newend=r'''The oriented transport preserves its self-intersection,
proving the local assertion.

'''+root+r'''The local sphere just constructed lies in
$K\cap H^{-1}(\epsilon_0)$. The identity inclusion of
this coordinate neighbourhood maps it into the same
global fibre $Y_{\epsilon_0^m}$, because $f=H^m$.
Its square is still $-2$. The torus has $\pi_2=0$,
so the sphere is null-homotopic and has square zero,
a contradiction.

\item Factor the analytic plane function as'''
assert oldend in new517;new517=new517.replace(oldend,newend,1)
p.record('D12,D14,D16,D20,D25','cdp:st:A.5.17',old517,new517,
 'Expose the general isolated-germ sphere assertion already proved by the complete boundary/gradient/discriminant/Morse argument. Preserve its proof, every equation/tag, the exact f=u h^m root, and all suspension/Hessian statements; the torus application now follows the local assertion through its identity inclusion.')
p.guard('A517-local-sphere-owner',old517,new517,'Full owner comparison; no existing assertion or proof step is removed, and the stronger local scope is explicitly stated before its consumers.')

old322=block(s,'lem:II:weighted-initial-monodromy')
new322=old322.replace(r'\cite[Theorem~2C.3, p.~179]{Hatcher2002}',r'\cite[proof of Theorem~2C.3, pp.~180--181]{Hatcher2002}; \cite[Theorem~1.2, p.~180]{ParkSuh1996}')
oldst=r'''the affine fibre $\{P=1\}$ and a compact local Milnor fibre
have the same homology and weighted scalar monodromy.
Suppose that the cyclic group $\mu_d$, acting with weights'''
newst=r'''the affine fibre $F=\{P=1\}$ and a compact local Milnor fibre
have the same homology and weighted scalar monodromy.
For every $\zeta\in\mu_d$, acting with weights $w$,
\[
 \sum_{j=0}^2(-1)^j\operatorname{tr}
       (\zeta\mid H_j(F;\Q))=\chi(F^\zeta).
\]
Suppose that the cyclic group $\mu_d$, acting with weights'''
assert oldst in new322;new322=new322.replace(oldst,newst)
oldchar=r'''Every nonidentity element of $\mu_d$ acts freely on
the invariant core. The Lefschetz theorem
\cite[Theorem~2C.3, p.~179]{Hatcher2002} gives zero
Lefschetz number for those elements. At the identity
the number is $\chi(P^{-1}(1))=d\chi(Q)$.'''
# The citation replacement above also affects this local paragraph.
oldchar=oldchar.replace(r'\cite[Theorem~2C.3, p.~179]{Hatcher2002}',r'\cite[proof of Theorem~2C.3, pp.~180--181]{Hatcher2002}; \cite[Theorem~1.2, p.~180]{ParkSuh1996}')
newchar=r'''To compute the character on this core $C=\{P=1,R_w\le R_0\}$,
choose $R_0$ above all critical values and regular also
on every fixed locus. Its algebraic double is
\[
 \widehat C=\{(z,t):P(z)=1,\ t\in\R,
                         t^2=R_0-R_w(z)\}.
\]
It is compact. The real algebraic action of
$\mu_d\times\{\pm1\}$ acts on $z$ by weighted scalars
and on $t$ by its sign. The equivariant triangulation
of \cite[Theorem~1.2, p.~180]{ParkSuh1996} respects
the isotropy strata. After barycentric subdivision,
the equator $t=0$, fixed by the second factor, is a
subcomplex, and each closed half is a subcomplex.
Projection $(z,t)\mapsto z$ identifies the half $t\ge0$
with $C$, with inverse $z\mapsto(z,\sqrt{R_0-R_w(z)})$.
Thus $C$ has a finite equivariant triangulation.
After one further barycentric subdivision, a simplex
preserved by an element is fixed pointwise. The alternating
cellular trace is therefore the Euler number of the fixed
subcomplex. The trace identity in
\cite[proof of Theorem~2C.3, p.~181]{Hatcher2002}
identifies it with the alternating trace on homology.
The invariant gradient collar restricts to each fixed
locus, so $C^\zeta\hookrightarrow F^\zeta$ is a
homotopy equivalence. This proves the displayed character
formula on $F$.

For a free action every nonidentity character value
is zero. At the identity the value is
$\chi(P^{-1}(1))=d\chi(Q)$.'''
assert oldchar in new322;new322=new322.replace(oldchar,newchar)
p.record('D12,D17,D18,D20,D25','lem:II:weighted-initial-monodromy',old322,new322,
 'Make the finite-order character formula used by P454 an explicit earlier clause. The compact algebraic double and its half-projection identify the exact core; Park–Suh Theorem1.2 p180 supplies equivariant triangulation, and opened Hatcher trace identity p181 supplies the cellular/homology comparison. All existing free-action/transport/variation statements remain.')
p.guard('P322-fixed-locus-character',old322,new322,'One shared compact-core/character owner, including the nonfree order-six action, with exact double/half maps.')

pos=s.index(r'\label{night:P4.54}')
start=s.rfind(r'\subsection',0,pos)
stop=s.index(r'\subsection',pos)
oldunit=s[start:stop]
new=oldunit
new=p.edit(new,'In the remaining positive ruled support of \\cref{sec:II:night-sign},',r'In the setting of \cref{lem:II:positive-ruled-conductor-graph},','D01,D08,D25','night:P4.54',
 'State the exact global irreducible-or-normal-crossings positive ruled setting, including the refined conductor-graph hypotheses; retain the complete conclusion.')
new=p.edit(new,'No transverse-type restriction is imposed on the other\nconductor component.','The transverse types on the other conductor component are arbitrary.','D02','night:P4.54',
 'State the existing unrestricted transverse-type scope positively once.')
new=new.replace(r'\StatementRecord{night:P4.54}{proved}{02XT}{}',r'\StatementRecord{night:P4.54}{proved}{02XT}{\cref{night:P4.53,night:P4R.18,lem:II:weighted-initial-monodromy,cdp:st:A.5.17}; \cite[Theorem~1.4.1, pp.~39--41]{Dolgachev1982}}')

weights=r'''We establish the following three coordinate
weights and leading degrees, retaining the actual $r$:
\[
 (1,1,1;3),\qquad(1,1,2;4),\qquad(1,2,3;6).
                                                        \tag{4.54w.1}
\]'''
assert weights in new
new=new.replace(weights,'')
p.record('D03,D14','night:P4.54',weights,'The same numbered weights/degree display stands after the leading-equation argument.',
 'Place the established weights and leading degrees at their proof, instead of announcing them before the formal-functions and coordinate maps.')

new=p.edit(new,r'''using \(H^1(\mathbb P^2,\mathcal O(k))=0\), gives its whole''',r'''using \cite[Theorem~1.4.1(ii), p.~39]{Dolgachev1982}
with weights $(1,1,1)$, gives its whole''','D17,D18','night:P4.54',
 'The opened weighted-projective cohomology theorem includes precisely the ordinary-plane vanishing used for this restriction sequence.')
new=new.replace(r'where \(F_3=0\) is that smooth cubic.',r'''where \(F_3=0\) is that smooth cubic. For example,
$X^3+Y^3+Z^3=0$ is smooth in projective space because
its three gradient equations force $X=Y=Z=0$.''')
oldopt=r'''Its
weighted projective curve is the actual smooth \(H\).
The coordinate choice below does not require completing the
square or applying any of these optional graded simplifications.'''
newopt=r'''Its weighted projective curve is the smooth $H$.
The displayed Weierstrass generators describe this graded ring;
the analytic coordinates used below are constructed while fixing $r$.'''
new=p.edit(new,oldopt,newopt,'D02,D20','night:P4.54',
 'Distinguish the explicitly given graded-generator map from the analytic coordinate construction that keeps r; no graded change is applied to the ambient germ.')
oldrepeat=r'''\item This argument proves directly that the chosen analytic
coordinates have the prescribed orders and generate the
graded ring. The invertible linear and triangular coordinate changes retain the
fixed \(r\).

'''
assert oldrepeat in new;new=new.replace(oldrepeat,'')
oldlead=r'''\item Write the defining analytic equation in the coordinates just
constructed, with the weights in (4.54w.1). Its weighted initial
form is the single defining relation of the graded section
ring, up to a nonzero scalar. Here is an explicit proof of that
last assertion.

\item Let \(F_D\) be the graded relation from the section-ring calculation above, expressed
in the actual chosen initial generators.'''
newlead=r'''\item Use the coordinates $(r,s,v)$ just constructed, with
their computed valuations. Their initial sections generate
the graded ring. Let $F_D$ be its single graded relation,
expressed in these initial generators.'''
new=p.edit(new,oldlead,newlead,'D03,D12','night:P4.54',
 'Combine the repeated coordinate conclusion and prospective leading-equation announcement at the formal lifting step; retain its full completeness/principality proof.')
oldweightend=r'''This proves (4.54w.1) for the actual defining
equation, with all higher terms retained.'''
newweightend=r'''Thus the chosen analytic coordinates, with the fixed
exceptional parameter $r$, have weights and leading degrees
\[
 (1,1,1;3),\qquad(1,1,2;4),\qquad(1,2,3;6).
                                                        \tag{4.54w.1}
\]
All remaining terms of the analytic equation have strictly
larger weighted degree.'''
assert oldweightend in new;new=new.replace(oldweightend,newweightend)

oldchart=r'''\item In the chart with original coordinates
\(x=r u\), \(y=r v\), every change above has the form'''
newchart=r'''\item In a blowup chart, first centre $(u,v)$ at the point
below $H$. The corresponding original coordinate change is
$(x,y,z)\mapsto(x-u(p)z,y-v(p)z,z)$; its inverse adds
the same two linear terms. Thus $r=z$ is fixed.
In the centred chart $x=ru$, $y=rv$, every change above has the form'''
new=p.edit(new,oldchart,newchart,'D20,D22','night:P4.54',
 'Give the explicit original linear map and inverse that centre the selected exceptional point while keeping the required parameter r unchanged; retain the later descended triangular analytic map.')

oldtransport=r'''\item Weighted scaling with these weights and the compact-cycle
flow in Proposition~\ref{night:P4.52} transports every pairing of the leading
Milnor fibre into an actual local Milnor fibre of the reduced support equation.
By Proposition~\ref{night:P4.51}, all these pairings vanish.
For a one-dimensional critical locus, the boundary Wang sequence and
$j_2(T-I)=\mathrm{VAR}^{\mathrm{II}}j$ give
$\operatorname{rank}(T-I)\le M$
\cite[\S\S5.3--5.4, pp.~457--458; \S\S6.2--6.5,
pp.~460--461; \S7.1, p.~462]{Siersma1991Variation}.
For an isolated critical point, $M=0$ and the identity
$\ker j=\ker(T-I)$ gives $T=I$
\cite[Proposition~3.4, p.~451]{Siersma1991Variation}.
We contradict these bounds in each of the three cases.'''
newtransport=r'''\item Write $g$ for the original reduced support equation
and $\Phi=u g^m$ for the full local fibration function.
As in \cref{night:P4.52}, $b_1(S)>0$ gives the first
clause of \cref{night:P4.51} on this same full fibre.
The root $g_u=\exp((\log u)/m)g$ and the identity
inclusion $g_u^{-1}(\delta)\hookrightarrow\Phi^{-1}(\delta^m)$
give zero intersection pairing on its local reduced levels.
For each pair $(w;D)$ just obtained, apply
\cref{lem:II:weighted-initial-monodromy} with
$D_\epsilon(x,y,z)=(\epsilon^{w_x}x,
\epsilon^{w_y}y,\epsilon^{w_z}z)$,
$G_\epsilon=\epsilon^{-D}g\circ D_\epsilon$ and $c=1$.
Every compact pairing on the leading fibre is preserved
by transport to $g=\epsilon^D$, and hence is zero.
Once its leading polynomial is shown reduced, the second
clause of that lemma gives
$\operatorname{rank}(T-I)\le M$, with $M=0$ for an
isolated critical point.'''
new=p.edit(new,oldtransport,newtransport,'D12,D14,D17,D20,D25','night:P4.54',
 'Apply P322 with the complete weighted/full-function maps; P451 uses the same b1(S)>0 first clause. No repeated Siersma argument or lost original multiplicity remains.')

oldcore=r'''We choose an invariant
semialgebraic compact core large enough for $F$
and $B$. The finite-order Lefschetz character of
$H_0-H_1+H_2$ is therefore $\chi(F)$ at the identity,
$\chi(B)$ at the cube, and zero elsewhere.'''
newcore=r'''The fixed-locus character formula of
\cref{lem:II:weighted-initial-monodromy} applies to
this same polynomial, with weights $(2,2,1)$ and degree
six. Thus the character of $H_0-H_1+H_2$ is
$\chi(F)$ at the identity, $\chi(B)$ at the cube,
and zero elsewhere.'''
new=p.edit(new,oldcore,newcore,'D12,D17,D20','night:P4.54',
 'Use the exact earlier nonfree finite-order character owner for the order-six action, with its fixed set B under the cube; the full double-cover Euler and eigenspace calculations remain.')

oldcech=r'''The three standard affine charts give its \v Cech
complex. The middle cohomology of every
$\mathcal O_{\mathbb P}(k)$ is zero. The top
cohomology of $\mathcal O_{\mathbb P}(-e)$ has
basis the Laurent monomials $u^{-i}v^{-j}w^{-k}$,
$i,j,k\ge1$, of weighted degree $-e$. Thus'''
newcech=r'''Apply \cite[Theorem~1.4.1(i)--(iii), pp.~39--41]{Dolgachev1982}
with $S=\C[u,v,w]$, weights $(a,b,c)$ and twist $-e$.
It gives $H^1(\mathbb P,\mathcal O(k))=0$ and identifies
the dimension of $H^2(\mathbb P,\mathcal O(-e))$ with
that of $S_{e-a-b-c}$. The long exact sequence therefore gives'''
new=p.edit(new,oldcech,newcech,'D12,D17,D18','night:P4.54',
 'Freshly opened full Dolgachev1.4.1 statement/proof pp39–41; the exact graded sheaf and long-exact-sequence map replace the repeated general Cech calculation, while its complete monomial count stays.')
new=new.replace('We record the two curve facts needed for the last\ncases, with their quotient comparisons. For','For')
new=new.replace('Consider weights $(1,2,3)$ and degree seven.',r'''For degree seven the coordinate permutation
$(x,y,z)\mapsto(z,x,y)$ identifies the weighted plane
with $\operatorname{Proj}\C[z,x,y]=\mathbb P(1,2,3)$;
its inverse restores $(x,y,z)$.''')
new=new.replace('For weights $(1,3,4)$, (4.54a) gives',r'''For degree nine the same permutation identifies the plane
with $\operatorname{Proj}\C[z,x,y]=\mathbb P(1,3,4)$.
Formula (4.54a) gives''')
p.record('D20','night:P4.54','Weights (2,3,1) and (3,4,1) later printed as (1,2,3) and (1,3,4).',
 'The explicit permutation (x,y,z)→(z,x,y), with its inverse, gives Proj C[z,x,y] in both cases; z remains the weight-one coordinate.',
 'Give the exact coordinate identification behind the two printed orderings; all quotient-vertex characters and z=0 components keep their original meanings.')
new=new.replace(r'''Its hypersurface critical
point is isolated, so the isolated-point
Morse transport in Proposition~\ref{night:P4.52} gives a spherical
class of square $-2$ in its Milnor fibre.
This again contradicts the zero pairing
transported from the actual torus.''',r'''Its hypersurface critical point is isolated. Apply the
local clause of \cref{cdp:st:A.5.17} with $H=P_9$:
the resulting compact sphere has square $-2$ in a small
local $P_9$-level. The weighted scaling isomorphism
$D_\lambda:P_9^{-1}(1)\to P_9^{-1}(\lambda^9)$
places its inverse image in $P_9=1$ for a chosen ninth
root $\lambda$ of that level value. The preceding
$G_\epsilon$ transport then puts the same compact
intersection class in a local reduced $g$-level, whose
pairing is zero. This is a contradiction.''')
p.record('D12,D14,D20,D25','night:P4.54','Isolated-point Morse transport in Proposition P4.52 applied to P9.',
 'Apply the explicit general local clause of A.5.17 to H=P9, use D_lambda^{-1} to P9=1, then P322 to g=epsilon^9 and the unchanged full Phi=u g^m.',
 'The leading polynomial is a local isolated germ, so its sphere comes from the general clause, with every subsequent scaled-fibre and full-fibre map stated explicitly.')

oldclose=r'''\item All three possibilities for the sole
simple elliptic exceptional curve have
now been excluded. Together with Proposition~\ref{night:P4.53}
this proves that the horizontal pole
section cannot be contracted. Proposition~\ref{night:P4R.18}
then gives the asserted generic $D_4$
image and degree two or three. The
other conductor component retains its
unrestricted transverse type.

\item For weights $(1,2,3)$, the cohomology count in (4.54a)
is zero in degrees one through five and one in degrees six and seven.
For weights $(1,3,4)$ it is zero in degrees one through seven and one
in degrees eight and nine. The order-six rank gap is at least
$12-2=10$, and the degree-seven rank gaps are $18-0=18$ and $12-1=11$.
For the order-four action with characters $1,3$, the quadratic
characters are $0,2$. The cubic $X^3+Y^3+Z^3$ is smooth in projective
space because its three gradient equations force $X=Y=Z=0$.'''
newclose=r'''\item The section is therefore noncontracted. Apply
\cref{night:P4R.18} to the identical $f:Y\to B$, full
fibre $mS$, normalization resolution and section $H$.
Its global irreducible-or-normal-crossings, positive-Euler
and positive ruling-genus hypotheses are those of
\cref{lem:II:positive-ruled-conductor-graph} in the statement.
It gives the degree-two or degree-three map onto a rational
normalized conductor component with generic germ $D_4$.'''
new=p.edit(new,oldclose,newclose,'D03,D12,D22,D25','night:P4.54',
 'Keep the precise refined R18 application. Move the Fermat cubic and numerical gaps beside their calculations; the repeated monomial counts and quadratic characters are already stated in full at their unique owner inside this proof.')
new=new.replace('the nontrivial monodromy rank.','the nontrivial monodromy rank; the gap is at least $12-2=10$.',1)
new=new.replace('whose upper bound is zero or one.','whose upper bound is zero or one. The respective gaps are\n$18-0=18$ and $12-1=11$.',1)
# Establish the reduced-polynomial hypothesis before the character application.
crit_start=new.index(r'\item Every nonzero critical orbit of $P_6$')
crit_end=new.index(r'\paragraph{Weighted curve cohomology.}',crit_start)
crit=new[crit_start:crit_end]
cut=crit.index(' The variation inequality')
crit_input=crit[:cut]+'\n\n'
crit_conclusion=crit[cut:].lstrip()
new=new[:crit_start]+crit_conclusion+new[crit_end:]
char_start=new.index(r'\item Weighted monodromy has order six.')
new=new[:char_start]+crit_input+new[char_start:]
p.record('D14','night:P4.54',crit,
 'The complete critical-orbit, transverse Milnor and reducedness calculation now precedes the order-six character calculation; its contradiction and rank gap follow the lower bound.',
 'P322 requires the leading polynomial to be reduced. Put that proved premise before the exact fixed-locus-character application without changing any formula or local singularity map.')
# Avoid collision of the count of binary roots with the fixed exceptional r.
da=new.index(r'\paragraph{Degree six.}')
db=new.index(r'\paragraph{Weighted curve cohomology.}',da)
piece=new[da:db]
piece=re.sub(r'(?<![A-Za-z_])r(?![A-Za-z_0-9])',lambda m:'k_0',piece)
new=new[:da]+piece+new[db:]
p.record('D20','night:P4.54','r denotes both the fixed exceptional coordinate and the number of distinct binary-cubic roots.',
 'The root count is k_0∈{1,2,3}, equal to the former integer r; the exceptional coordinate remains r everywhere.',
 'Rename only the count in the degree-six calculation; chi(B)=3(2−k_0), chi(F)=12+3k_0, rank>=9+3k_0 and M=3−k_0 are unchanged identities.')
new=new.replace('Hauptsätze',r'Haupts\"atze')
new=new.replace(r'Proposition~\ref{',r'\cref{')
new=new.replace(r'\subsection{The simple elliptic contraction and its weighted normal forms}',r'\subsection{The simple elliptic contraction and its weighted normal forms}')
# Add a stable heading label to the existing actual subsection.
heading=new[:new.index('\n')]
new=new.replace(heading,heading+r'\label{subsec:II:elliptic-contraction}',1)
new=p.clean(new,'night:P4.54')
p.guard('P454-complete-subsection',oldunit,new,
 'Complete subsection with all fixed-r analytic coordinates, formal-functions maps, weighted polynomial cases and original conclusions retained; exact earlier owners replace repeated topology/cohomology.')

dol=r'''\bibitem[Dolgachev(1982)]{Dolgachev1982}
Igor Dolgachev.
\newblock Weighted projective varieties.
\newblock In James~B. Carrell, editor, \emph{Group Actions and Vector Fields},
Lecture Notes in Mathematics, volume~956, pages~34--71. Springer, Berlin, 1982.
\newblock \doi{10.1007/BFb0101508}.
\newblock URL \url{https://sites.lsa.umich.edu/idolga-new/wp-content/uploads/sites/1467/2024/08/weighted82.pdf}.

'''
anchor=r'\bibitem[Douady(1966)]{Douady1966}'
p.guard('Dolgachev1982-bibliography',anchor,dol+anchor,'Opened author PDF Theorem1.4.1 pp39–41 and publisher DOI metadata; insert in author order.')
p.record('D18','Dolgachev1982','No weighted-projective cohomology entry.',dol,
 'The primary author facsimile and Springer chapter identity have been opened; cite published pages and DOI.')
park=r'''\bibitem[Park and Suh(1996)]{ParkSuh1996}
Dae Heui Park and Dong Youp Suh.
\newblock Equivariant semi-algebraic triangulations of real algebraic
$G$-varieties.
\newblock \emph{Kyushu Journal of Mathematics}, 50(1):179--205, 1996.
\newblock \doi{10.2206/kyushujm.50.179}.
\newblock URL \url{https://www.jstage.jst.go.jp/article/kyushujm/50/1/50_1_179/_article}.

'''
anchors=re.findall(r'\\bibitem[^\n]+',s)
anchor=next(x for x in anchors if re.match(r'\\bibitem\[P[a-z]+',x) and 'Park' < re.search(r'\[([A-Za-z]+)',x).group(1))
p.guard('ParkSuh1996-bibliography',anchor,park+anchor,'Opened primary journal Theorem1.2 and setup pp179–180; insert in author order.')
p.record('D18','ParkSuh1996','No equivariant triangulation entry.',park,
 'The exact compact algebraic double fits the opened finite-group algebraic-variety theorem; published locator and DOI are retained.')

p.write(new)
for key,text in [('A517',new517),('P322',new322)]:
    (OUT/f'S6_SERIES_PUBLISH_II_sec07_elliptic_contraction_{key}.tex').write_text(text+'\n',newline='\n')
