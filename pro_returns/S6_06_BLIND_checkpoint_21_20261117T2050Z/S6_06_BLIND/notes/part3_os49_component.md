# P3F.26. The component-supported OS49 sphere construction

**Proved.** The rational elliptic surface
\[
 y^2=x^3-3t^3(t-1)x+2t^4(t-1)(t-\tfrac12)
                                                        \tag{P3F.26.1}
\]
has fibres \(IV^*,II,I_2\) at \(0,1,\infty\), and primitive
Mordell--Weil generator \(G=(t^2,t^2)\). Put
\(M=\mathcal O(G-O)\), and suspend translation by \(-Q=-3G\).
There is a linearization whose divisor is the identity component
\(C_0\) of the \(I_2\) fibre, with multiplicity one. Its primitive
rank-two toric filling at infinity, the original line-complement
quotient at \(II\), and the order-three free logarithmic cap at
\(IV^*\), with logarithmic vector \((1,-1,0,0)^t\), glue to a
smooth compact complex manifold diffeomorphic to \(S^6\). Its
integral topology is computed below, including every differential.
This is the component-supported target specified in the prompt;
we do not identify its linearization with a whole-fibre divisor.

## The source, section and component divisor

Write \(f=t^3(t-1)\), \(g=t^4(t-1)(t-1/2)\). Direct calculation gives
\[
 f^3-g^2=-\tfrac14t^8(t-1)^2,
 \qquad j/1728=4t(1-t).
\]
The vanishing orders at zero and one are respectively
\((3,4,8)\) and \((1,1,2)\) for \((f,g,\Delta)\).
At infinity the minimal coefficients are units and the discriminant
has order two. These give exactly the asserted Kodaira fibres.
Substitution verifies the displayed section. On the cubic root
\(t=s^3\), set \(x=s^4X,y=s^6Y\). The central good-reduction
curve is \(Y^2=X^3+1\), and \(G\) specializes to \((0,1)\), a
nonzero point of order three. At infinity, with \(q=1/t\), its
coordinates \((q^2x,q^3y)=(1,q)\) meet the Weierstrass node
\((1,0)\), and the first resolution gives component one of
\(I_2\). Its intersections with \(O\) are empty. The height is
\[
 2-\frac43-\frac12=\frac16.
\]
Shioda--Tate gives rank one. The verified Oguiso--Shioda Main
Theorem table used in P3F.1 has exactly one row with root lattice
\(E_6+A_1\), namely row49, with trivial torsion and primitive
height \(1/6\). Since multiplication of a section multiplies its
height by the square of that integer, the displayed \(G\) is a
primitive generator. This application has the required rationality:
the Weierstrass fundamental line has degree one, the base is
\(\mathbb P^1\), and the section excludes multiple fibres.

For translation by \(-Q\), the divisor of the line of
linearizations is
\[
 D=G-O-(-2G)+(-3G).
\]
At \(IV^*\), \(Q\) meets the identity component, so all
multidegrees cancel. At \(I_2\), its multidegrees on \((C_0,C_1)\)
are \((-2,2)\). They equal those of \(C_0\), since
\(C_0^2=-2\) and \(C_0C_1=2\). On a rational elliptic surface
the difference \(D-C_0\), having zero generic degree and zero
component multidegrees, is an integral fibre class. Its intersection
with \(O\) is zero: the height formula gives
\((-2G)O=(-3G)O=0\), and \(DO=1=C_0O\).
Thus \(D\sim C_0\). Choose its canonical section and multiply
it by a small nonzero scalar \(\lambda\). This specifies the
linearization and its exact zero divisor.

## Actual local fillings and their gluing

Near \(I_2\), use a Tate coordinate \(Z\) on the source and a
nonzero line coordinate \(V\). A logarithmic representative of
\(G\) has valuation one. Inverting \(G\) changes every associated
marking coherently; choose the sign giving that positive valuation.
The two commuting deck periods have valuations
\[
 h:(Z,V)\longmapsto(q^2aZ,qbV),\qquad
 g:(Z,V)\longmapsto(q^{-3}cZ,\lambda q^{-1}dV),       \tag{P3F.26.2}
\]
where the four coefficients are nonvanishing holomorphic units.
To check the second valuation without a guessed toric model,
translation by \(-Q\) exchanges \(C_0\) and \(C_1\).
The norm of the linearization has divisor
\(C_0+C_1=F\). Therefore \(h^3g^2\), whose first valuation
is zero, has second valuation one. This gives exactly the exponent
\(-1\) in (P3F.26.2).

The integral change of deck generators
\[
 H=h^{-1}g^{-1},\qquad K=h^3g^2
\]
has determinant one, and its valuation columns are respectively
\((1,0)^t,(0,1)^t\). Thus the precise local filling is the
unit-square Mumford model triangulated by its diagonal, with units
retained in the deck maps. For a triangle with lattice vertices
\((i,j),(i+1,j),(i,j+1)\), the cone on the three height-one rays
has determinant one; its affine chart is \(\mathbb C^3\), with
\(q\) the product of the three toric coordinates. The other
triangle has the analogous chart. Adjacent charts glue by the
integral monomials determined by their common rays. Translations
by \(H,K\) preserve the fan and multiply those monomials by
holomorphic units. Modulo this full period lattice there are one
vertex, three edges and two triangles. The usual annular moduli
fundamental domain in \((\log|Z|,\log|V|)\), together with these
boundary charts, is compact over a closed sufficiently small disc.
It proves properness and the Hausdorff property. The unimodular
charts prove smoothness. The central normalization is the standard
hexagonal toric surface, with opposite boundary curves identified
by the retained unit periods. Its Euler number is two.

At the type \(II\) fibre the linearization is invertible. Use
the actual smooth total line complement \(M^\times\) over the
original elliptic neighbourhood, divided by the contracting lift
of \(-Q\). A Hermitian norm and a sufficiently small scalar
make that lift strictly decrease the norm, uniformly on this compact
neighbourhood. Its iterates therefore act freely and properly
discontinuously, with a compact annular fundamental domain. The
quotient is smooth, proper over the base disc, and agrees with the
regular torus family on the punctured disc. No replacement of this
additive source fibre is made.

At \(IV^*\), cubic good reduction gives a smooth elliptic family.
The point \(Q=3G\) specializes to zero. The degree-zero line and
the nonvanishing linearization consequently give a smooth two-torus
family on the root chart. The linear homology deck matrix is
\(\widehat T_A=(T_A^{-1})^t\), displayed below. The vector
\(\ell=(1,-1,0,0)^t\) is invariant. The affine cyclic action is
translation by \(\ell/3\) followed by \(\widehat T_A\).
The invariant gamma covector evaluates to one on \(\ell\),
so its nonidentity powers have gamma displacement \(1/3\) and
\(2/3\), and are free. Its quotient is the smooth finite cap.
Its punctured gluing is the holomorphic logarithmic translation
\[
 (z,s)\longmapsto
 \left(z+\frac{\log s}{2\pi i}\Pi(s)\ell,s\right),
 \qquad t=s^3.
\]
Changing the branch of the logarithm adds an integral period;
the cubic deck changes it by the displayed affine translation.
This verifies descent and gives its inverse by subtraction.

Glue these models to the regular family over the three-punctured
sphere by these logarithmic and toric chart identifications.
On every compact parameter subannulus the discs can be shrunk once
to give uniform compact fundamental domains. Their union with a
compact regular-base part proves compactness of each threefold and
properness of the holomorphic family over that subannulus. Exhaust
the punctured parameter disc by such subannuli; the constructions
agree on their common ordinary locus and by the same toric charts,
so they glue to the family on the whole punctured disc. This does
not impose a parameter-independent cusp radius at \(\lambda=0\).
Smoothness, holomorphy and the Hausdorff property follow from the
explicit local charts and their annular overlap maps.

## Marked monodromy and its completeness

The elliptic cohomology matrices can be marked
\[
 A=\begin{pmatrix}-2&-3\\1&1\end{pmatrix},\quad
 B=\begin{pmatrix}1&1\\-1&0\end{pmatrix},\quad
 C=\begin{pmatrix}1&2\\0&1\end{pmatrix},\qquad ABC=I.
\]
This is a marking of the displayed surface. Its exact degree-two
map \(j/1728=4t(1-t)\) has permutations \(S=(12)\) over one,
\(R=1\) over zero, and cusp permutation \((12)\). The associated
index-two modular cover therefore has two order-three elliptic
points and one cusp of width two. Taking the local lifts of types
\(IV^*\) and \(II\) gives the displayed order-three and order-six
matrices, with the positive cusp transvection \(C\). There is
no additional quadratic twist: an odd valuation changes one of
these fixed local types, and a rational function on \(\mathbb P^1\)
with all valuations even is a square.

There is also no unverified integral choice of the section cocycle.
Since \(B-I\) is unimodular, choose the unique Abel--Jacobi lift
which makes its \(B\)-cocycle zero. The \(I_2\) component implies
the remaining cocycle is \((r,0)\), with \(r\) odd. The product
relation gives the \(A\)-cocycle \((-r,0)\). For an elliptic
matrix \(E=(\begin{smallmatrix}a&b\\c&d\end{smallmatrix})\),
cocycle \((j,h)\), and scalar entry \(z\), the line/suspension
weights \((1,3)\) give
\[
 T(E,(j,h),z)=
 \begin{pmatrix}
 1&3(cj-ah)&3(dj-bh)&z\\
 0&a&b&j\\0&c&d&h\\0&0&0&1
 \end{pmatrix}.
\]
The order-three condition gives \(z_A=-r^2\).
The norm calculation above gives
\(z_C=(3r^2-1)/2\). The central entry of the global product is
\((r^2-1)/2\). Its only integral zeros are \(r=\pm1\),
interchanged by \(G\mapsto-G\). Hence, in the positive marking,
the actual cohomological tuple is
\[
 T_A=\begin{pmatrix}1&-3&-3&-1\\0&-2&-3&-1\\0&1&1&0\\0&0&0&1\end{pmatrix},
 \qquad
 T_B=\begin{pmatrix}1&0&0&0\\0&1&1&0\\0&-1&0&0\\0&0&0&1\end{pmatrix},
\]
\[
 T_C=\begin{pmatrix}1&0&3&1\\0&1&2&1\\0&0&1&0\\0&0&0&1\end{pmatrix}.
                                                        \tag{P3F.26.3}
\]
Their product and \(T_A^3\) are the identity. These and the
normal-function normalization equation are executed exactly in
`code/part3/os49_component.py`.

## Integral topology

The local type \(II\) neighbourhood retracts onto its cuspidal
rational curve, which is homeomorphic to \(S^2\): its normalization
is a continuous bijection from a compact space to a Hausdorff space.
The restriction of \(M\) has degree zero and is topologically
trivial. A local logarithm of \(Q\) gives a translation isotopy
through its identity-component group; on the central cuspidal
curve this is its additive translation, fixing the cusp. Its
suspension, including the line, thus retracts onto
\(S^2\times T^2\). The collapse from a smooth fibre kills the
two elliptic one-cycles and has degree one on its oriented two-cell.
It follows integrally that its specialization image is the complete
invariant lattice of \(\bigwedge^qT_B\) in every degree. At
the rank-two cusp the unimodular fan calculation is exactly the
normalization/double-curve complex of E26 Lemma7.4: the checked
period basis has index one, so its specialization also has full
integral invariant image. Its two vanishing circles are primitive.

In van Kampen, these two nonfinite fillings kill the section
meridians and the images of \(\widehat T_B-I,\widehat T_C-I\).
The eight-column relation matrix has Smith factors \((1,1,1)\);
its quotient is generated by the invariant gamma direction.
The base relation kills the remaining finite meridian, and its
cube relation kills \(\ell\). Adding that column gives Smith
factors \((1,1,1,1)\). The boundary maps are surjective onto the
local filled fundamental groups, by the indicated collapse and
finite quotient presentations. Since the original torus group is
abelian, these are all van Kampen generators and relations; hence
\(\pi_1(X)=1\).

For completeness the section used here is obtained from a meromorphic
frame of \(M|_O\), whose degree is one, with divisor at the cusp.
On the rank-two chart its valuation is an integral period vector
and is subtracted by that deck period. It therefore extends to the
cusp. It is invertible at \(II\). At \(IV^*\) take it as the
punctured origin before the specified logarithmic translation.
Thus no unrecorded affine clutch is present in these relations.

Use the parabolic complex, with the full matrices (P3F.26.3),
\[
 L_q\xrightarrow{d^0}\bigoplus_{i=A,B,C}(E_i-I)L_q
       \xrightarrow{d^1}L_q,
 \qquad E_i=\bigwedge^qT_i,
\]
\[
 d^0v=((E_i-I)v)_i,
 \qquad d^1(y_A,y_B,y_C)=y_A+E_Ay_B+E_AE_By_C.
\]
The executed program prints the integral Hermite bases and every
entry of both maps. In degrees one, two and three the local image
ranks are respectively \((2,2,2),(4,4,2),(2,2,2)\), and both
differentials have ranks three, five and three. Their ambient
stacked and cokernel Smith forms have only unit nonzero entries.
Thus the parabolic middle cohomology is zero integrally, and the
last cokernels are free of rank one.

The global invariant generators are
\[
 1,\quad\psi,\quad\omega=uw+3\psi\delta,
 \quad\phi=\psi uw,\quad\nu=\psi uw\delta.
\]
The coinvariant generators are
\[
 1,\quad[\delta],\quad\eta,\quad[uw\delta],\quad[\nu],
 \qquad[\psi\delta]=\eta,\quad[uw]=3\eta.
\]
All other exterior basis classes map to zero.

At the finite cap the five-generator affine relation matrix
\((\begin{smallmatrix}\widehat T_A-I&-\ell\\0&3\end{smallmatrix})\)
has Smith factors \((1,1,1)\). Thus its reduced bielliptic surface
has \(H_1=\mathbb Z^2\), and Poincaré duality makes its integral
cohomology torsion-free. Its degree-two intersection form is
unimodular. The invariant first-cohomology basis upstairs is
\(\psi,h=-w+3\delta\), and its descending lattice is
\(\mathbb Z(3\psi)\oplus\mathbb Zh\).
The full invariant degree-two basis is
\[
 u_2=-\psi w+3\psi\delta,\qquad v_2=\psi w+uw,
\]
with intersection matrix
\((\begin{smallmatrix}0&3\\3&0\end{smallmatrix})\), and
\(\omega=u_2+v_2\). The degree-three covering multiplies
intersection numbers by three, so its downstairs unimodular
degree-two lattice has pullback determinant nine. This is already
the determinant of the full invariant lattice; hence every invariant
degree-two class descends. Perfect pairing with degree one gives
degree-three index one, and degree four has index three. The
global specialization indices are exactly \((3,1,1,3)\).
The global invariant generators reach both nontrivial local
cokernels, so the corresponding skyscraper corrections create
no additional first-cohomology groups.

The integral Leray page consequently has only columns zero and two.
Its zeroth column is generated by
\(1,3\psi,\omega,\phi,3\nu\), and its second column by the
five coinvariant generators above times the positive base class
\(H_B\). To verify that no intrinsic differential is omitted,
replace the affine order-three cap by the coarse quotient of the
same root torus family under its linear action. This auxiliary
compact topological filling has rational fibre cohomology equal
to the invariant cohomology of the root torus: take an equivariant
barycentric subdivision and average cochains. Inversion about the
global origin extends over that linear quotient and the centrally
symmetric toric fan; at \(II\) it is the group inversion and
dual line map. It acts by \((-1)^q\) on the rational direct
images, so its rational \(d_2\) is zero. The actual affine
boundary differs by the explicit translation path
\(z\mapsto z+t\ell/3\); three lifted prisms make the integral
prism for \(\ell\). Rational transfer gives one third of its
contraction. The already computed actual source and target groups
are free, so this determines the integral differential uniquely.
The logarithmic translation prism consequently gives
\[
 d_2(a)=\frac{H_B}{3}[\iota_\ell a].
\]
On \(\psi,\omega,\phi,\nu\) the contractions in coinvariants
are respectively
\(1,3[\delta],3\eta,[uw\delta]\). After the indicated source
indices, all four integral differentials are multiplication by one.
No higher differential is possible. Thus the only cohomology groups
are \(H^0=H^6=\mathbb Z\), with no torsion or extension ambiguity.
Simple connectivity, Hurewicz and Whitehead give a homotopy sphere,
and \(\Theta_6=0\) identifies it with the standard smooth sphere.

The unit-circle action is semifree. The \(II\) line-complement
quotient is free by strict norm contraction; the finite cap is free
by its nonintegral gamma displacement; and the cusp has the
standard primitive vertical-wall fan, so its only fixed set is one
\(\mathbb P^1\) of normal bundle
\(\mathcal O(-1)\oplus\mathcal O(-1)\), with weights
\((-1,+1)\). All of these checks concern the actual component
divisor filling. **End of proof.**

# P3F.27. The OS49 cusp circle and its marked page comparison

**Proved.** In the above component-supported construction, the
primitive circle which extends as the rotation of the second nodal
factor is \(K=3u+2\gamma\). It is not the original suspension
cycle \(\gamma\). The change of its page boundary marking is
\[
 H=-u-\gamma,\qquad K=3u+2\gamma,
 \qquad u=2H+K,\qquad\gamma=-3H-K.               \tag{P3F.27.1}
\]
The boundary angle for a \(K\)-rotation evaluates to one on
\(u\) and to minus one on \(\gamma\), and vanishes on \(H,w\).
These statements follow by inversion of the displayed unimodular
matrix, and the program executes them exactly.

On writing \(\lambda=r^3\), \(s=\log q/(2\pi i)\) and
\(v=\log r/(2\pi i)\), the leading period columns are
\[
 u=(2s,s)^t+U(q),\qquad
 \gamma=(-3s,-s+3v)^t+C(q),
\]
where \(U,C\) are holomorphic. In particular
\[
 H=(s,-3v)^t-U-C,\qquad
 K=(0,s+6v)^t+3U+2C.                             \tag{P3F.27.2}
\]
The positive closing deck on the ordinary locus is multiplication
of the line coordinate by \(t\). At the finite cap its logarithmic
translation is \(\log t\,\delta/(2\pi i)\), exactly the change
in that cap's gluing when \(c=\log\lambda/(2\pi i)\) increases
by three. At infinity it is multiplication by \(q^{-1}\); this
extends through the cusp by translation of the toric fan by its
integral second basis vector. At \(II\) it is a holomorphic unit.
Thus these maps close the actual holomorphic family over
\(\lambda=r^3\). Its cusp difference is \(-s\delta\).
The bounded extending origin cancels that difference by the
integral period \(K\), because
\(-s\delta+K=6v\delta+3U+2C\) is holomorphic at \(q=0\).
In full detail, put \(D=3U+2C\). The two origins on \(q=Q_0^6\)
are
\[
 \sigma(q,v)=vD(q)+3v(v-1)\delta,
 \qquad
 o(q,v)=-\frac{sD(q)}6-\frac{s^2}{12}\delta-sv\delta.
\]
The first is bounded at \(q=0\), and its characters extend by units
in the cusp charts. The second has parameter difference
\(-s\delta\), and subtracting it trivializes that deck. At fixed
\(q\ne0\), the suspension multiplier has order three in \(r\),
so the ordinary three-component rank-one parameter chain supplies
the extending zero origin. Their difference and deck identities are
\[
 F=\sigma-o=\frac{D(s+6v)}6+
       \left(\frac{(s+6v)^2}{12}-3v\right)\delta,
\]
\[
 \begin{aligned}
 F(s,v+\theta)-F(s,v)&=\theta K+3\theta(\theta-1)\delta,\\
 F(s+6,v)-F(s,v)&=K+3\delta.
 \end{aligned}
\]
The latter is an integral period. In particular the two origins
descend on the specified cyclic cover. The extra real delta gauge
has equal zero endpoint values, while its \(Q_0\)-deck winding
is six. This proves that the positive family loop has the stated
actual \(K\)-angular clutch, with its line gauge retained.

The existing regular-binding page of the original source has
boundary cycles \((u,w,\gamma)\). On the actual cusp product
\(E'_{I_1}\times S^1_K\), the source torus has cycles \((H,w)\).
The old gamma angle winds on \(H\). Consequently the phase
avoidance step used in P3K.6 for the original family does not apply
to this compression without modification: its projected compression
meets every old gamma phase. The graph map from the page to the
parameter disc still extends by a radial cutoff, for any boundary
angle, so that extension is not the obstruction. The unproved step
is the identification of the normal-section Euler line on that
graph with the old source line through a homotopy avoiding the
rotating compression.

This direct graph-line comparison was the unresolved route at the
first writing of P3F.27. P3F.31 subsequently constructed the actual
positive-fan page through its line-complement subfan. P3K.65 constructs the full native C2 return and the oriented Cox ruling arrow, giving negative-fan class \(-3\) while the positive fan has class zero. That proof retains the outer normal-line marking and does not use the incomplete direct negative-fan graph homotopy.

The old degree-three compact elliptic pullback has three \(II\)
and three \(I_2\) fibres, \(\chi=1\), signature \(-8\), height
\(1/2\), total component correction \(3/2\), and \(G\cdot O=0\).
These numbers are checked. Their actual positive-fan page identification is P3F.31. P3K.65 relates the actual two sphere returns by its native relative diffeomorphism and oriented Cox arrow; it does not identify the two integer indices. The earlier direct graph
homotopy remains an uncompleted auxiliary route. The boundary
marking and the obstruction to that particular homotopy recorded
above are retained exactly. **End of proof.**
