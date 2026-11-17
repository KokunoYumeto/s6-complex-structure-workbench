# Further supplied constructions: exact loops and page data

This file records the Part 3.4 audit of all six supplied construction
sources. It uses their defining charts, sections and parameter spaces.
The original real-trace comparison is now proved in P3K.6--9 and
applied in P3F.25. The earlier complex-corner approach in P3F.13
is retained as an uncompleted auxiliary route. The actual OS49
returns are proved by P3F.31--32 and the charged Cox bordism P3K.17.

## P3F.16. The actual comb-smoothing loop has identity monodromy

**Proved.** Let \(s\) denote the smoothing parameter of the labelled comb
in Viaclovsky, arXiv:2610.10451, in the germ used to construct the compact
threefolds. The smooth family of these threefolds over a sufficiently
small punctured \(s\)-disc is a product. Its return diffeomorphism is
isotopic to the identity. For a sphere member its class in
\(\Theta _7\) is therefore zero.

Here the loop is the parameter of the comb smoothing appearing in the
source. No identification of that parameter with the scalar parameter
\(w=e^{-\pi i c}\) of another construction is used.

### Construction and proof

Write \(B'=B\setminus\Sigma\) for the base with its critical values
removed, and \(\Lambda\) for the fixed integral homology local system
in the source's Section “Global extension,” equations `Jac` and
`fixedreal`. Every admissible Hodge plane \(\mathcal F_s\) gives the
real-linear evaluation isomorphism
\[
 \Lambda_{\mathbb R,b}\longrightarrow\mathcal F_s(b)^*,
 \qquad v\longmapsto(\omega\longmapsto\omega(v)).
\]
Injectivity follows because a real vector annihilating \(\mathcal F_s\)
also annihilates its conjugate, whose direct sum is the whole
cohomology space. Both sides have dimension four. Thus evaluation
identifies the smooth family on \(B'\) with the fixed bundle
\(\mathscr M=\Lambda_{\mathbb R}/\Lambda\). This identification is
smooth jointly in \((b,s)\) for every \(s\ne0\), even near a comb tooth.
No limiting Hodge plane at that tooth is required.

Choose pairwise disjoint closed discs about the critical values and
put \(B^\circ=B\setminus\bigcup\operatorname{int}D_i\). All their
collars avoid the comb teeth. The local finite and toric fillings,
their periods and their gluing translations are holomorphic on these
collars for the entire parameter disc, including \(s=0\). This is the
construction in the source's Proposition `topology`: its gluing
translations are extended from \(s=0\) by the exact sequence
\(0\to\Lambda\to\mathcal L\to\mathcal T\to0\), the vanishing of
\(H^1(A_i\times\Delta,\mathcal L)\), and extension of a vector-bundle
section from the divisor \(s=0\). Consequently the actual attachments,
not merely their isotopy classes, extend smoothly across \(s=0\).

For precision, one can make all the trivializations single valued in
\(s\), as follows. Set \(W=\mathscr M|_{B^\circ}\). On each compact
filled piece \(\mathcal V_i\to\Delta\), choose smooth horizontal lifts
of the two real coordinate vector fields on the parameter disc. The
local defining equations have parameter-independent strata; the lifts
can be chosen to preserve the base coordinate and be tangent to every
boundary collar. On a finite quotient average the lifts over its
finite group. On a toric filling patch the lifts on the regular charts;
the units vary smoothly with the parameter. Integrate their combination
along the radial path \(\tau\mapsto\tau s\), \(0\leq\tau\leq1\).
Compactness and a smaller common disc give diffeomorphisms
\[
 a_{i,s}:V_{i,0}\longrightarrow V_{i,s},\qquad a_{i,0}=\mathrm{id},
\]
smooth jointly in \(s\). In the fixed source of these trivializations,
the actual attachments are smooth maps
\[
 \varphi_{i,s}:\partial V_{i,0}\longrightarrow\partial_iW,
 \qquad |s|<\epsilon.
\]
Their central value is the original attachment, by the prescribed
translation extension just described.

Put \(g_{i,\tau,s}=\varphi_{i,\tau s}\varphi_{i,0}^{-1}\). This is a
smooth family of isotopies beginning at the identity. Its generating
vector field is
\[
 Z_{i,\tau,s}=(\partial_\tau g_{i,\tau,s})\circ g_{i,\tau,s}^{-1}.
\]
Extend it constantly in the radial coordinate of a fixed collar of
\(\partial_iW\), multiply by a cutoff which is one at the boundary
and zero at the inner edge, and extend by zero on the rest of \(W\).
The collars are disjoint. Integrating their sum gives a smooth family
\(K_s\in\operatorname{Diff}(W)\), with
\[
 K_s|_{\partial_iW}=g_{i,1,s},\qquad K_0=\mathrm{id}.
\]
These maps glue to the \(a_{i,s}\), because
\(K_s\varphi_{i,0}=\varphi_{i,s}\) on each common boundary. We have
therefore constructed an actual smooth isomorphism of bundles
\[
 X_0\times\Delta^*\longrightarrow\mathcal X|_{\Delta^*}.
\]
Every step depends on the complex number \(s\), rather than a chosen
argument of \(s\). The isomorphism is single valued around the positive
parameter circle, so its return is the identity. Any other connection
on the same bundle has isotopic return: interpolating connections
produces a smooth isotopy of their holonomies. This proves the claim
with its actual parameter and without using the annular index formula.

## P3F.17. Page invariants for all coprime higher multiplicities

**Proved.** Put \(m=3k\), \(n=4l\), with \(\gcd(m,n)=1\), and use any
of the logarithmic data in Viaclovsky, arXiv:2610.39102, giving a sphere.
The regular-fibre page of the circle quotient has base genus
\((mn-m-n+1)/2\), degree \(d=mn=12kl\) over the original elliptic base,
and its sectioned elliptic completion has precisely \(d\) fibres of
type \(I_1\). Its invariants are
\[
 \chi(\mathcal O)=kl,\quad \sigma=-8kl,\quad
 h(P)=2kl,\quad (aP)\cdot O=kl(a^2-1)
\]
for every nonzero integer \(a\). For the actual circle line on a page
disjoint from the fixed sphere, with the boundary marking of P3F.10,
\[
 s_\delta=-2kl,\qquad p_{\rm rel}=-24kl.
\]
These equations compute the page data. The actual real trace
P3K.6--9 supplies the original return comparison and P3F.25 records
its higher-family application. The fully signed higher-parameter
comparison is developed in P3K.11 and is under audit at this checkpoint.

### Proof

The source retains the same rational elliptic surface, section
\(P\), line \(\mathcal O(P-O)\), and cusp as E26. Its finite caps are
the further root pullbacks of the degree-three and degree-four good
reductions. The generators act on the invariant real circle coordinate
\(\psi\) by \(n_i/m_i\), with \(\gcd(n_i,m_i)=1\); see the source's
equations `logdat`, `cyclic`, `glue`, and Proposition `logprop`.
Since \(\psi(\delta)=0\), no nonidentity finite deck element can be
cancelled by the \(\delta\)-circle. Thus the circle has no new
stabilizers in these caps. The cusp orbit is the same relative product
constructed in P3F.9.

After quotienting by this circle, the two base solid tori have Seifert
multiplicities \(m,n\). The source's sphere condition is the integral
equation \(m_1n_0+m_0n_1=\pm1\); its meridian relation matrix is
unimodular. The two solid tori therefore glue to \(S^3\), with the
weighted circle fibration of weights \(m,n\), with the sign of its
orientation fixed by that equation. A regular binding has a page
described by \(b^m-a^n=1\), using positive real radial rescaling with
weights \(m,n\), exactly as in P3F.10. Its map to the weighted base has
degree \(mn\), ramification indices \(m,n,mn\) at the two exceptional
values and the chosen regular binding value. Riemann--Hurwitz gives
\(2-2g=m+n-mn+1\).

Choose the binding away from all three critical values. The root
indices at the original \(IV^*\) and \(III\) fibres are multiples of
their good-reduction indices, so their relatively minimal pullbacks
are smooth. The original nodal fibre is unramified and has \(d\)
preimages. Thus the elliptic completion has \(d\) positive nodes and
no reducible fibres. Its Euler number is \(d\), its holomorphic Euler
characteristic is \(d/12=kl\), and its signature is \(-2d/3=-8kl\).
Height pulls back by \(d\), giving \(h(P)=d/6=2kl\). Shioda's formula,
with zero reducible-fibre corrections, gives
\(2kl a^2=2kl+2(aP)\cdot O\). In particular \(P\cdot O=0\).
The section line square is
\((P-O)^2=-2\chi-2P\cdot O=-2kl\).

The actual page may be chosen disjoint from the fixed sphere by the
same phase choice as P3F.10. Its affine elliptic torsor is smoothly
translation-trivial over the base with boundary. The normalized
fibrewise Picard point of the circle line is \(P\), and a change of
this trivialization changes its line by a base pullback; such a class
vanishes on this base. The boundary first Chern class is zero, so the
relative square is independent of its relative lift, by the displayed
boundary cup-product calculation in P3F.10. The relative tangent
framing comparison there, and signature additivity on capping the
regular elliptic boundary, give \(p_{\rm rel}=3\sigma=-24kl\).

## P3F.18. The two supplied one-logarithmic-transformation page covers

The following source data have been read directly in the supplied
construction sources, rather than inferred from their arXiv titles.

| Construction | Source fibres | Defining section and translation | Finite cap | Regular-binding elliptic page |
|---|---|---|---|---|
| Viaclovsky 2609.33785 | \(III^*,I_1,I_1,I_1\) | \(P=(0,1)\) on \(y^2=x^3+tx+1\), \(M=P-O\), translation \(2P\) | order four | degree four, base genus zero, twelve \(I_1\) |
| Liu--Rollenske 2609.33826 | \(III^*,II,I_1\) | \(P=(-t^2,it^3)\) on their displayed Weierstrass model, \(M=P-O\), translation \(2P\) | order four | degree four, base genus zero, four \(II\) and four \(I_1\) |

Both primitive sections have height \(1/2\) and are disjoint from
\(O\), as also follows from the E7 entry in P3F.2. The first source
chooses its scalar linearization to vanish at one nodal fibre; the
other two nodal fibres have rank-one torus fillings. The second source
chooses the linearization to vanish at its nodal fibre and leaves the
\(II\) fibre as the product cusp with an elliptic factor; its sole
logarithmic cap is the order-four cap at \(III^*\).

For either source, quotienting its finite cap by the \(\delta\)-circle
gives a Seifert solid torus of multiplicity four. The meridian of the
other solid torus has multiplicity one: the source twist has primitive
invariant circle coordinate equal to one. The resulting Seifert
\(S^3\) has weights \((1,4)\). Its regular-binding page is a disc. Its
compactification maps with degree four to the source base, branched
only at the order-four value and the regular binding. Thus \(III^*\)
has good reduction and the remaining source critical values have four
unramified preimages each. This proves the last column, including the
four cuspidal fibres in the Liu--Rollenske case.

The Euler number is twelve in both cases, since \(e(II)=2\) and
\(e(I_1)=1\). Consequently their sectioned page completions have
\(\chi(\mathcal O)=1\), \(\sigma=-8\), \(h(P)=2\), and no reducible
fibres. Therefore \(P\cdot O=0\), \((P-O)^2=-2\), and
\((aP)\cdot O=a^2-1\). These are exact page computations. The scalar
loop's comparison with its global equivariant return is not supplied
by these numbers.

## P3F.19. A direct obstruction to spheres in Yang's two families

**Proved.** Every Type B and Type C construction in the supplied Yang
source has a nontrivial cyclic quotient of its fundamental group:
\(\mathbb Z/2\) in Type B and \(\mathbb Z/3\) in Type C. This applies
to every index and every admissible twist in those two constructions.
In particular none is diffeomorphic, or homeomorphic, to \(S^6\).

Here is a direct quotient of the attaching presentation, sufficient
for the obstruction and independent of any assertion of the full
group. On the regular part, kill every fibre loop. Send the two finite
base meridians to \(1,-1\) in \(\mathbb Z/g\), where
\(g=\gcd(m_1,m_2)\), and the cusp meridian to zero. All semidirect
product relations hold because the fibre loops have been killed. In
the local finite quotient chart, the only relation after killing the
fibre loops is the \(m_i\)-th power of the corresponding base
meridian: the affine translation in that power is a fibre loop.
This relation holds in \(\mathbb Z/g\). The local cusp attachment
kills its base meridian up to a fibre loop and kills some fibre loops;
these relations also hold. The sphere relation holds because
\(1+(-1)+0=0\). The map thus extends over all three attachments and is
surjective, since a finite meridian maps to one.

The construction has \((m_1,m_2)=(4,6)\) in Type B and \((3,6)\) in
Type C, giving the displayed nontrivial quotients. The quotient maps
are explicit morphisms of the Van Kampen presentation; a hypothetical
homeomorphism to \(S^6\) would induce an isomorphism on fundamental
groups, whereas the latter sphere has trivial fundamental group.

For the canonical twists \((\ell_0,\ell_1,\ell_2)=(0,1,-1)\), the
source's invariant-closure calculation kills exactly the other three
fibre generators: its cusp kills \(w,\delta\), and its first finite
matrix sends \(w\) to \(u-\delta\) in Type B and to
\(u-w-\delta\) in Type C. The resulting presentation is abelian on
\((z,x,y)\), with relation matrix
\[
 \begin{pmatrix}-1&m_1&0\\1&0&m_2\\0&1&1\end{pmatrix}.
\]
Its Smith diagonal is \((1,1,2)\) or \((1,1,3)\), respectively.
The program `other_family_checks.py` recomputes these matrices.

## P3F.20. Wang's two-torsion and the resulting obstruction to a sphere

**Proved.** The supplied Wang construction is simply connected and has
\(H_2=H_3=\mathbb Z/2\), so it cannot be homeomorphic to \(S^6\).
The computation below retains the primitive \((2,1)\) rank-one
exponent at \(I_2\); the full integer matrices have been executed in
`code/part3/other_family_checks.py` and are saved in its JSON output.

The source configuration is \(IV^*,I_2,I_1,I_1\), with line \(P-O\),
translation \(-6P\), and one logarithmic cap of order three. At
\(I_2\) the Tate periods are
\[
 h(z,v)=(q^2c_1z,qc_2v),\qquad
 g(z,v)=(c_3z,\lambda c_4v),
\]
where \(g\) is obtained from the original lift by multiplying it by
\(h^3\). The monomial coordinates \(x=v,y=v^2/z\) send the exponent
\((2,1)\) to \((1,0)\); this is a unimodular coordinate change. The
zero-exponent period contracts the \(y\) coordinate by \(\lambda^2\)
times a unit. Thus the central rank-one fibre has one component and
the primitive pinching-circle specialization. The ordinary rank-one
\(I_1\) has the same pinching map. At the remaining \(I_1\) the scalar
zero gives the unimodular two-period toric model, with its standard
hexagonal component and integral specialization. These are the
displayed local charts in the supplied source's Lemma `fill:tate`
and Propositions `fill:rankone`, `fill:a2`; the exponent and primitive
collapse calculations above verify their use here.

The cohomological monodromies in basis \((\psi,u,w,\delta)\) are
\[
 T_* =\begin{pmatrix}1&0&-6&-2\\0&-1&-1&1\\0&1&0&-1\\0&0&0&1\end{pmatrix},\quad
 T_2=\begin{pmatrix}1&0&6&3\\0&1&2&1\\0&0&1&0\\0&0&0&1\end{pmatrix},
\]
\[
 T_+=\begin{pmatrix}1&0&0&0\\0&2&1&0\\0&-1&0&0\\0&0&0&1\end{pmatrix},\quad
 T_-=\begin{pmatrix}1&0&0&-1\\0&1&1&0\\0&0&1&0\\0&0&0&1\end{pmatrix}.
\]
Their ordered product is the identity, \(T_*^3=I\), and the invariant
homology vector of the logarithmic transformation is
\(\ell=(1,-2,-4,0)^t\). Its invariant circle coefficient is one, so
the order-three affine action is free. The three Mumford sections
extend, and their meridians are killed. Their homological monodromy
images kill \(\widehat w,\widehat\delta,\widehat u+\widehat w\),
leaving only \(\widehat\psi\). The remaining meridian is killed by
the base relation, and its cube relation kills \(\ell\), hence the
remaining generator. Every boundary map is onto its filled
fundamental group by the displayed primitive collapse or affine
quotient presentation. This proves simple connectivity.

For every exterior degree, use the same integral parabolic complex as
in P3F.21, with this ordered tuple. The ranks of its four local images
are \((2,1,1,2)\), \((4,2,2,2)\), and \((2,1,1,2)\) in degrees one,
two and three. Both differentials have ranks three, five and three.
The stacked first differential has only unit nonzero Smith factors.
Thus its middle cohomology is zero integrally. The invariant
generators are
\[
 1,\quad\psi,\quad\xi=uw+6\psi\delta,\quad\phi=\psi uw,\quad\nu=\psi uw\delta,
\]
and the free coinvariant generators are
\[
 1,\quad[\delta],\quad[\psi\delta],\quad[uw\delta],\quad[\nu],
 \qquad[uw]=6[\psi\delta].
\]
The complete local image bases and both integer differentials are
recorded in the program output, not just their ranks.

At the order-three fibre, the reduced quotient has torsion-free
cohomology: its affine abelianization is free of rank two, and
Poincaré duality applies. The invariant degree-one basis is
\(\psi,h=-2u+w-3\delta\), with \(h(\ell)=0\). Its pullback image is
\(\mathbb Z(3\psi)\oplus\mathbb Zh\). The invariant degree-two basis
\((\psi h,\xi)\) has intersection matrix
\[
 \begin{pmatrix}0&-3\\-3&12\end{pmatrix}.
\]
Its determinant has absolute value nine, exactly the determinant of
the degree-three pullback of the downstairs unimodular lattice, so
the degree-two image is the full invariant lattice. The perfect
pairing with degree one then gives degree-three index one. Top
degree has index three. The global specialization indices are
therefore \((3,1,1,3)\). The two nontrivial cokernels are reached by
the global generators \(\psi,\nu\), so all first-cohomology terms of
the direct images remain zero.

The Leray page consists of columns zero and two; its first column is
generated by \(1,3\psi,\xi,\phi,3\nu\). Its second column is generated
by the five displayed coinvariants times the positive base class
\(H\). The only affine clutch is the logarithmic translation, so its
cellular prism gives
\[
 d_2(a)=\frac H3[\iota_\ell a].
\]
The four contractions in coinvariants, before the indicated source
multiplicities, are \(1,6[\delta],6[\psi\delta],[uw\delta]\). Hence
the four integral differentials are multiplication by
\[
 (1,2,2,1).
\]
No higher differential is possible. Thus
\(H^3=H^4=\mathbb Z/2\), \(H^0=H^6=\mathbb Z\), and the other
cohomology groups vanish; Poincaré duality gives the stated homology.
A homeomorphism to \(S^6\) would induce an isomorphism on integral
homology, contradicting this explicit nonzero two-torsion.

The original line circle also illustrates a local feature relevant
to further comparisons: at the \(I_2\) pinching locus its direction
\((0,1)\) intersects the collapsing torus circle \((2,1)\) in a
subgroup of order two. Therefore its isotropy there is exactly
\(\mathbb Z/2\). This follows by solving \(2\theta\in\mathbb Z\)
in \(\mathbb R/\mathbb Z\), and must be retained in any circle-orbit
calculation for this construction.

### Further component-supported cases

For the component-supported OS49 target in the prompt with \(Q=3P\), the regular-binding degree-three
page has three \(II\) and three \(I_2\) fibres, hence
\(\chi(\mathcal O)=1\), \(\sigma=-8\), \(h(P)=1/2\), and total
reducible-fibre correction \(3/2\). The height formula gives
\(P\cdot O=0\). Its component-permuting translation is carried through the actual positive-fan page in P3F.31--32, giving positive-fan index zero. P3K.65 retains the full native C2 closing and Cox ruling arrow and gives negative-fan class \(-3\) for \(\lambda=r^3\), or \(-1\) for the actual shorter scalar loop \(\lambda=w\). No negative-fan integer index is assigned here.

The eight Mordell--Weil entries and twenty-one configurations are
enumerated in P3F.1. Enumerating those source configurations does not
yet enumerate every compact sphere filling produced from all choices
of translation, vertical linearization divisor and logarithmic data.
The bounded slice mentioned in the prompt has no specified numerical
bounds in the supplied claim. We have not silently supplied bounds or
converted its asserted count into a theorem.
