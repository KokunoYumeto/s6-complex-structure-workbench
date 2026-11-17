# Further exact cap restrictions in the established orbit model

## P3K.18. Proved: no multiple elliptic fibre over a cap-core knot

In the actual whole-fibre \(I_1\) orbit projection of P3K.16,
every sphere member has primitive source-fibre multiplicities
at every logarithmic cap.  In particular no cap whose smooth
source quotient has a genuinely multiple central fibre occurs
in such a sphere member.

**Proof.** The signed meridian matrix in P3K.16 has determinant
\(\pm1\); its explicit genus-one Heegaard map identifies
the target \(B\) with \(S^3\).  Let \(K\subset B\)
be one oriented cap-core knot.  Suppose that the source
fibre multiplicities on that core have a common divisor
\(\nu>1\).  The linking-number class of this single knot is
\[
            \eta\in H^1(S^3\setminus K;\mathbb Z/\nu),
\]
with value one on its positive meridian.  It is represented,
for example, by intersection with an oriented Seifert surface
for \(K\), reduced modulo \(\nu\).  Pull it back to
\(Y\setminus p^{-1}K\).

The relevant local normal exponent is that of the actual
three-dimensional target, not the old branched base coordinate.
In a cap chart of P3K.16 it is
\[
        \xi=e^{2\pi i rt/m'}u,
        \qquad u=z^g,
\]
the transverse disc coordinate of its target solid torus.
At a smooth point of a source component of multiplicity
\(\nu a_j\), choose a complex normal coordinate \(w\).
Then \(u=w^{\nu a_j}v\), where \(v\) is a nonvanishing
holomorphic unit.  Consequently a small positive component
meridian has linking number \(\nu a_j\) under \(p\).
The pulled-back class kills every such meridian modulo
\(\nu\).

The remaining singular strata of the central source fibre,
crossed with the suspension direction, have real codimension
at least four in the smooth five-manifold \(Y\).  A loop
or a homotopy disc can be perturbed off these strata; after
this perturbation, van Kampen says that filling the smooth
divisorial pieces only kills their normal meridians.  Thus
the pulled-back class extends to a homomorphism
\[
                         \pi_1(Y)\longrightarrow\mathbb Z/\nu.
\]
It is nonzero.  Indeed a meridian loop of \(K\) can first
be perturbed off all the other critical and cap-core circles.
Lift it through the connected regular elliptic fibres by the
horizontal-path construction of P3K.16, and close the lifted
path inside its starting fibre.  The resulting loop lies in
\(Y\setminus p^{-1}K\) and evaluates to one.  This
contradicts \(\pi_1(Y)=0\).  Therefore the common divisor
is one at every cap.
**End of proof.**

## P3K.19. Proved: reduction of the finite kernel and multiplicative-fibre constraints

For the actual affine root-line caps of P3K.15 in the sphere
orbit scope of P3K.16, the root fibre is reduced.  A singular
root fibre has no nontrivial finite zero-gamma kernel.  At a
smooth elliptic root fibre that kernel is an actual normal
root change, and the invariant source coordinates and line
frames cancel it exactly.  Thus the cap has a primitive
effective pair without an unrecorded source or line quotient.

At an original multiplicative fibre \(I_N\), a sphere cap
retains the following necessary restrictions on the original
source data \(M=\mathcal O(aG-O+D)\), \(Q=bG\):
\[
              \gcd(N,b[G])=1,
              \qquad a[G]=0\quad\text{in }\mathbb Z/N.       \tag{P3K.19.1}
\]
For the explicit generator markings in P3F.2 these are
\(\gcd(N,b)=1\) and \(N\mid a\).  These restrictions
hold at logarithmically replaced multiplicative fibres as
well as at retained ones.

**Proof: the actual component maps and their multiplicities.**
Use \(A,B,C,H\) from P3K.15, with
\(g=\gcd(m,n)\), \(C=A^{m/g}B^{-n/g}\).
The components of the finite source quotient are precisely
the \(C\)-orbits of root components.  The residual
\(H\)-action is transitive on those quotient components
by P3K.15.  Since \(C,H\) generate the same group as
\(A,B\), the latter group is transitive on all root
components.  Both maps preserve the multiplicities of
the root fibre \(\operatorname{div}(z)\).  The root
source retains the pulled-back section of the original
elliptic surface, so these multiplicities have greatest
common divisor one: intersecting the fibre with that
section gives one.  Transitivity makes every multiplicity
equal, and hence all are one.

Let \(H_j\subset C\) be the stabilizer of a general
point on root component \(C_j\).  It is the subgroup
acting pointwise on that component.  Since \(C\) is
central and \(A,B\) are transitive, all these subgroups
are the same subgroup \(H_0\), of order \(h\).
At a general point its action on the normal parameter has
order exactly \(h\), because the root-base character is
faithful.  The finite quotient is therefore ramified to
order \(h\) along each root component.  The quotient
base coordinate is \(u=z^g\).  If \(\bar C\) is an
image component, comparing divisors in
\(\pi^*u=z^g\) gives its multiplicity exactly
\[
                              g/h.                         \tag{P3K.19.2}
\]
This computation includes component permutations and the
degree of the component map; it uses the generic normal
ramification index, not a declaration that the quotient is
unramified.  P3K.18 forces \(g/h=1\).  Hence \(C\)
fixes every root component pointwise.

At a singular point of a reduced root fibre, a nontrivial
finite-order surface automorphism cannot fix that fibre
germ pointwise.  Average a local coordinate map over the
finite group to linearize the action, with derivative the
identity at the base point of the averaging map.  The fixed
germ of a nonidentity linear map in two complex dimensions
is either a point or a smooth line.  Neither can contain
the reduced singular fibre germ.  The derivative must
therefore be the identity; the linearization then makes
the automorphism the identity in a neighbourhood, and
analytic continuation makes it the identity on the root
source.  This contradicts its faithful root-base character.
Thus \(g=1\) at a singular reduced root fibre.

At a smooth elliptic root fibre, the group fixes that curve
pointwise.  Near each of its points average a tangent
coordinate to obtain an invariant coordinate \(e\), and
keep the given normal base coordinate \(z\).  These are
coordinates by the inverse function theorem, and the
generator acts exactly by
\[
                         (e,z)\longmapsto(e,\zeta_g z).
\]
The actual quotient coordinates are \((e,u=z^g)\).
They identify the root source with the pullback of its
smooth quotient along \(u=z^g\).  The invariant local
line frames of P3K.15 identify the root line with the
pullback quotient line as well; no fibre character remains
because every point stabilizer acts trivially on the line.
These local maps agree on overlaps by their quotient
construction and give the required global map after
shrinking the source disc.  On the quotient,
\[
  \bar A=\bar H^{n/g},\qquad
  \bar B=\bar H^{m/g},\qquad
  q=u^{m/g}.
\]
Thus the root order and gamma numerator reduce to the
primitive pair \((m/g,n/g)\) by an exact source-and-line
quotient.  The marked meridians and any remaining integral
delta collar factor are still those transported in P3K.15.

**Proof: the multiplicative root and its integral component action.**
On the minimal \(m\)-root of an \(I_N\) neighbourhood,
the Tate period is \(z^{Nm}\), and the components of
the \(I_{Nm}\) fibre are labelled by
\(\operatorname{ord}_z Z\pmod{Nm}\).  The canonical
root deck sends \(z\) to \(\zeta_m z\) and preserves
these labels.  A translation by a Tate point of valuation
\(\alpha\) adds \(\alpha\) to them.  If the original
point \(Q\) has component \(c\in\mathbb Z/N\), its
root lift has component \(mc\).  The actual affine
root map \(A\) therefore acts by addition of some
integer \(\alpha\), and \(B\) by addition of \(mc\).
The norm identity \(A^m=B^n\) gives
\[
       m\alpha\equiv nmc\pmod{Nm},\qquad
                   \alpha\equiv nc\pmod N.          \tag{P3K.19.3}
\]
This is the actual source-component action of the root
deck and its translation.  An additional inversion would
change the marked linear monodromy from trace two to
trace minus two and is not the outer monodromy of this
\(I_N\) source cap.

Every component orbit is a coset of the subgroup generated
by \(\alpha,mc\) in \(\mathbb Z/(Nm)\).  Its number
is \(\gcd(Nm,\alpha,mc)\).  By (P3K.19.3) every
common divisor of \(N,c\) divides this number.  The
proved transitivity thus forces \(\gcd(N,c)=1\).

The root line is the pullback of the quotient line of
P3K.15 and consequently has degree zero on every root
component.  Its generic Picard point is the pulled-back
point \(aG\), whose component is \(ma[G]\pmod{Nm}\).
Its extension differs from the section line by an integral
vertical divisor, by the coherent-direct-image argument
of P3K.15.  The component-degree equations are therefore
\[
                  e_{ma[G]}-e_0+B_{Nm}d=0.
\]
Multiply by the cyclic component labels and sum.  The
sum of labels times \(B_{Nm}d\) is divisible by \(Nm\),
by the exact cyclic difference calculation of P3K.14.
It follows that \(ma[G]=0\pmod{Nm}\), or equivalently
\(a[G]=0\pmod N\).  This proves (P3K.19.1).

The argument applies to the minimal root source used in
the actual Tate cap.  A superfluous equivariant blowup
cannot evade the transitivity statement: blowing up a
node introduces a component of different multiplicity,
and a rational vertical minus-one component in a reduced
transitive fibre would make every component a rational
minus-one curve.  The fibre intersection equations would
then give each vertex weighted valency one, so the
connected fibre would consist of two rational curves
with one transverse intersection.  Its arithmetic genus
would be zero, contradicting the elliptic fibre genus
one.  Thus the transitive root is relatively minimal.
**End of proof.**

These conclusions concern the actual root-line caps and the
global projection explicitly constructed in P3K.15–16.  They
do not assert a replacement of an arbitrary periodic cusp fan
by that fixed-sphere orbit model.  At such a fan the requisite
orbit comparison remains a separate part of the exhaustive
scope question.
