# Whole-fibre zero sites and source reduction

## P3K.20. Proved: the Euler contribution of a whole-fibre zero

For a semistable multiplicative source fibre \(I_N\), a
whole-fibre zero of order \(e\) has period determinant
\(Ne\) and central Mumford fibre Euler number \(2Ne\),
for every periodic unimodular triangulation.  At an
\(I_s^*\) zero, \(s>0\), the smooth quadratic
semistable Mumford root, followed by its actual monomial
involution quotient and toric quotient resolutions, has
Euler contribution at least \(4se\).  Potentially good
zero sites are excluded from sphere members by P3K.12.

In this actual smooth-root toric construction, a sphere
member therefore has exactly one whole-fibre zero: a
simple \(I_1\) zero.  For a rational rank-one source,
writing its generic line point and translation as
\(aG\) and \(bG\), respectively, the height denominator
\(d=1/h(G)\) satisfies \(ab=d\) after choosing the
contracting generator and the sign of \(G\).

**Proof: the actual line-frame determinant.** On the infinite
Tate chain let the source period and suspension period have
valuation vectors
\[
                    h=(N,\alpha),\qquad g=(-c,\beta).
\]
Write the fibre-coordinate graph of the actual line extension
as heights \(h_j\), so \(h_{j+N}=h_j+\alpha\).
An arbitrary vertical line divisor changes these heights
integrally; it is not omitted.  The line lift has the same
zero order \(e\) on every component precisely when its
actual fibre-coordinate transition has defect
\[
                      h_j+\beta-h_{j-c}=e.             \tag{P3K.20.1}
\]
Put \(r=\gcd(N,c)\), and iterate this identity \(N/r\)
times.  The period relation on the left gives
\[
      -\frac c r\alpha=\frac N r(\beta-e),
      \qquad
      \det(h,g)=N\beta+c\alpha=Ne.                    \tag{P3K.20.2}
\]
This is an identity of the actual component line frames.
It proves cancellation of the off-diagonal valuation terms
without changing or normalizing the vertical line divisor.

A fundamental polygon of this period lattice has area
\(Ne\).  Every unimodular triangle has area \(1/2\),
so it contains exactly \(2Ne\) triangles, counted with
their periodic boundary identifications.  In the central
Mumford fibre each triangle gives one zero-dimensional
torus orbit.  All other orbit strata are positive-dimensional
complex tori and have Euler number zero.  Additivity of
Euler number over the finite orbit stratification gives
\(2Ne\).  No vertical edge or semifree property of the
chosen delta circle is assumed in this calculation.

**Proof: the starred multiplicative quotient.** The quadratic
semistable root of an \(I_s^*\) fibre is \(I_{2s}\),
and the pulled-back whole-fibre zero has order \(2e\).
The determinant just proved is \(4se\).  The smooth
root Mumford fibre therefore has \(8se\) zero-dimensional
torus strata and Euler number \(8se\).

The quadratic deck is monomial on the central strata.
Indeed on the source nodal identity torus it is
\(Z\mapsto uZ^{-1}\), with a nonzero central unit
\(u\).  It commutes with the scalar circle on the line,
so in a line frame it sends \(V\mapsto f(Z)V\).
The source, line and their linearization are algebraic,
and this central torus map is regular and invertible.
Thus \(f\) is a unit of \(\mathbb C[Z,Z^{-1}]\),
so \(f(Z)=vZ^{\ell}\).  The induced maps on preserved
boundary torus strata are the restrictions of this same
integral monomial map.  Nonpreserved strata are permuted.
An invariant refinement can be used for descent; every
subdivision increases the number of maximal cones and
does not lower the preceding root Euler count.

There is also an explicit invariant unimodular height-one
choice, without a restriction to the rank-one generator
marking.  Write the actual monomial deck on valuations as
\(R(x,y)=(-x,y-jx)\), with \(j=-\ell\in\mathbb Z\).
It sends the source period \(h=(2s,\alpha)\) to
\(-h\); comparison of the second coordinate gives
\[
                         j=\alpha/s.
\]
Thus the integrality of this shear follows from the
actual deck morphism.  The whole-zero identity is now
\(2\beta+cj=4e\).  For odd \(j\), the integral
shear \(y'=y-(j-1)x/2\) gives
\(R(x,y')=(-x,y'-x)\).  The positive unit-square
triangulation is invariant, since its edge vectors
\(u,v,u+v\) go to \(-(u+v),v,-u\).
For even \(j\), use \(y'=y-jx/2\).  The reflection
is then \((-x,y')\) and the periods are
\((2s,0),(-c,2e)\).  Give the square with lower-left
corner \((v,k)\) its diagonal according to the parity
\[
                       v+c\left\lfloor k/(2e)\right\rfloor.
\]
Both periods preserve this parity.  Reflection sends the
square to \((-v-1,k)\), changes the parity, and exchanges
the two diagonals.  This is the required invariant
unimodular periodic triangulation.

In the marked rank-one case the generic point \(aG\)
has root Tate lift \(Z_G^a\), hence \(\alpha=as\),
\(c=bs\), and \(j=a\).  Changing that lift by a
Tate-period power \(Q_T^k\) is the actual line-frame
map \(V\mapsto Z^kV\).  Vertical component divisors
change the graph heights periodically and do not change
the quasiperiod.  These explicit maps recover the
rank-one spelling while the preceding deck argument
proves the starred-zero bound before that specialization.

The canonical-form normalization also identifies the
quotient-resolution comparison.  In Weierstrass coordinates
\(q=z^2,x=z^2X,y=z^3Y\), one has exactly
\[
                  (dx/y)\wedge dq=2(dX/Y)\wedge dz.
\]
After wedging the logarithmic line form, this is the
nowhere-zero Kulikov form
\(\Omega=d\log Z\wedge d\log V\wedge dz\).
The source inversion and \(z\mapsto-z\) give two
minus signs, while the additional \(Z^{\ell}\) in the line
map drops out of the wedge.  Thus the deck preserves
\(\Omega\).  Its nontrivial stabilizers on a smooth
root have eigenvalues \((-1,-1,+1)\), and their quotient
is a transverse \(A_1\) surface singularity along a fixed
curve.  In a resolution chart \(v=ut,w=ut^2\) for
\(v^2=uw\), the invariant two-form is
\(\tfrac12du\wedge dt\); it is nonvanishing.  This
is the actual crepant quotient resolution.

A divisor in this resolved model cannot be contracted to
a smooth model carrying the same nonvanishing form: the
Jacobian of a birational morphism vanishes along every
divisor mapped into codimension at least two, contradicting
the equality of those forms on their common open set.
Changes of the height-one Mumford triangulation are already
covered by the period-area count for each such fan.  In
particular a pure base-root contraction, whose pullback
canonical form has a ramification zero, is not being
silently used as a comparison of these normalized forms.

On an invariant torus stratum a fixed point equation is
\(x^{M-I}=a^{-1}\).  Its solution is empty or a coset
of the kernel of an integral torus homomorphism.  That
kernel is a finite union of complex tori.  Its Euler
number is nonnegative: positive-dimensional components
give zero and points give one.  Euler additivity therefore
gives \(\chi(X'^{\iota})\ge0\) on the root central fibre.
The finite-action orbit count, applied stratumwise, is
\[
 \chi(X'/\langle\iota\rangle)
       =\frac{\chi(X')+\chi(X'^{\iota})}{2}
       \ge4se.                                        \tag{P3K.20.3}
\]

For completeness, the quotient-resolution correction has
a definite sign in the stated toric construction.  Along
each fixed torus stratum the normal cyclic quotient has
constant diagonal characters.  Resolve it by a toric
subdivision.  A compact exceptional fibre has finitely
many torus orbits; its positive-dimensional orbits have
Euler number zero and it has at least one zero-dimensional
orbit.  Its Euler number is consequently at least one.
Euler additivity over the base fixed torus strata shows
that replacing a point-normal fibre by this exceptional
fibre adds a nonnegative quantity.  This proves the same
lower bound after the actual toric quotient resolutions.
Flips between unimodular height-one triangulations keep
the triangle count unchanged.

**Proof: the actual invariant-twist map at a semistable zero.**
The logarithmic modification in the supplied construction
\texttt{con-log} uses an extending root automorphism and
an invariant lattice translation, with punctured comparison
\(\sigma=(\log z)/(2\pi i)\,v\).  A whole-zero line
lift itself is not invertible on the zero fibre.  If the
same invariant-translation formula is interpreted on its
semistable Mumford torus, its quotient can nevertheless
be described exactly.  Full-rank unipotent monodromy has
invariant lattice equal to the primitive vanishing-torus
lattice.  Thus its twist has no gamma component.
On \(q=z^m\) write its deck as
\[
 (Z,V,z)\longmapsto
       (\zeta_m^r Z,\zeta_m^t V,\zeta_m z).
\]
The invariant coordinates are
\[
               Z'=Z/z^r,\qquad V'=V/z^t,\qquad q=z^m.
\]
They preserve every original period \(c(q)q^\Gamma\).
On cocharacters the quotient lattice and its exact
isomorphism are
\[
 \mathbb Z^3+\mathbb Z(r,t,1)/m
      \longrightarrow\mathbb Z^3,
 \qquad (x,y,s)\longmapsto(x-rs,y-ts,ms).
\]
The two horizontal basis vectors and \((r,t,1)/m\)
map to the three standard basis vectors.  Conjugating
the root period shear with translation \(m\Gamma\)
by this map gives the original shear \(\Gamma\).
Hence a smooth Kulikov target is again a Mumford fan
for the original period lattice and has the same Euler
count.  This gives the quotient directly, including
cases where resolving its root first would add curves.
No noninvariant affine operation at a zero germ has
been assumed beyond these actual published maps.

**Proof: the global zero count and height equation.** Away from
zero fibres, the line-complement construction has no fixed
point for the scalar circle, including its finite affine
quotients.  Its compact fibre Euler number is zero.
This also follows directly from the corresponding real
mapping-torus description.  On the smooth part of the
base the fibre is a complex torus and also has Euler
number zero.  Stratifying the base by its finitely many
special values therefore expresses the total Euler number
as the sum of the zero-site contributions above.

A smooth or potentially good zero site has the elliptic
fixed component excluded by P3K.12.  Every semistable
multiplicative zero contributes the positive even integer
\(2Ne\).  Every starred multiplicative zero in the
stated quotient-resolution construction contributes at
least four.  Since a six-sphere has Euler number two,
there is exactly one contribution, with \(N=e=1\).

The literal whole-fibre Hom relation and the telescoping
height calculation of P3K.14 give
\(\deg E=ab\,h(G)\).  Hence \(ab=d\).
For the pole version of the construction replace the
actual suspension generator \(B\) by \(B^{-1}\).
Their cyclic groups are identical, and the corresponding
period lattices are identical with the gamma generator
reversed.  Thus their toric quotient is identified by the
identity on its common charts; the inverse lift has zeros
in place of poles.  Finally replacing the name of the
generator \(G\) by \(-G\) makes the two coefficients
positive without changing the represented line point or
translation.  This gives the stated positive factorization.
**End of proof.**

The starred-fibre bound retains the normalized canonical form
and its actual monomial quotient/resolution maps.  The
invariant-twist paragraph supplies the direct quotient map
for the stated logarithmic formula; it does not assume an
additional noninvariant zero-germ operation.  The later
Seifert restrictions still require the orbit map of K16;
the present Euler count itself applies to every periodic
unimodular Mumford triangulation and does not impose a
vertical-edge or semifree delta condition.
