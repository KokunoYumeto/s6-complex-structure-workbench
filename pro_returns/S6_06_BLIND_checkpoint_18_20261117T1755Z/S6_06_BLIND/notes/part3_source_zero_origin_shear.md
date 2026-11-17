# The actual ordinary-origin shear and its fan refinements

Working local fan calculation for K39. Put \(c=nk\ne0\) and
\(N=km\), with the signed norm n retained. Subtracting the actual
ordinary origin \(nk\log(v)\log(q_1)/(2\pi i)^2\) gives, on positive
q1 continuation at fixed old coordinate,
\[
               (Z,V,v,q_1)\longmapsto(Z,v^{-c}V,v,q_1).
\]
The inverse gluing has the opposite exponent. This note records the
displayed forward-coordinate arrow. It does not replace the full
source/Cartier cap continuation by this scalar factor.

## OSH.1. Its exact lattice map and protected boundary

In the original lattice order \((x_Z,x_V,r,s)\), let
\(\delta=(0,1)\). The v-orders of the actual base rays give
\[
 S_I=S_W:(x,r,s)\longmapsto(x-cs\delta,r,s),\qquad
 S_E:(x,r,s)\longmapsto(x-c(r+s)\delta,r,s).
\]
Each is integral and unimodular. Since each fixes r,s and adds a
linear function of them to x, it commutes literally with every
period map \(T_j(x,r,s)=(x+(rP_0+sH)j,r,s)\).

The protected I and W boundary subfans have s=0 and are fixed
pointwise. The primitive E chain is carried by
\((0,j,1,0)\mapsto(0,j-c,1,0)\), hence is preserved as its
entire prescribed fan. On the common H face r=0 all three maps
agree. In E there is the additional exact identity
\[
 S_E=T_\nu,\qquad
 \nu=\left(\frac{bc}{2N},-\frac cN\right)
     =\left(\frac{bn}{2m},-\frac nm\right).
\]
This is a rational inspection period, not an integral deck map.
Its \(2m\)-th power is the actual integral period
\(T_{(bn,-2n)}\).

## OSH.2. A finite common protected refinement

For the finite-orbit fan Sigma already constructed, the intersection
fan \(\Sigma\wedge S\Sigma\) gives an actual common refinement.
It preserves the prescribed I/W/E boundary, because those boundary
fans agree exactly before intersection, and it has the same common
H faces in every sector. We give the finite-orbit check, including
the rank-one boundaries.

Choose finitely many cone representatives. On their compact
cross-sections r+s=1, x is bounded. In I the matrices rI+sH
have a uniform positive lower singular-value bound, so an
intersection between one chosen cone and a period translate of
an S-image cone bounds the period vector j. Thus only finitely
many translates contribute.

In W the functional \(\ell(x)=a x_Z+x_V\) vanishes on the
entire bottom boundary. For each finite cone representative,
\(|\ell(x)|\le C s\): sum its nonbottom ray coefficients and
use their positive s-heights. The shear changes this bound by
only \(|c|s\). Consequently an intersection at s>0 bounds
\[
             L=a j_1+(N+1)j_2.
\]
Write \(j=(t-bh,h)\). The first coordinate of its period shift is
\[
 r t+s(2t-bh)
   =\left(r+\frac{2N}{N-1}s\right)t
                       -\frac b{N-1}sL.
\]
The coefficient of t is bounded below by a positive constant
on r+s=1. The bounded x-coordinates therefore bound t, and
then h is bounded by \(L=at+(N-1)h\). This proves the required
finite list of translates for every positive-s intersection.
At s=0, arbitrarily many kernel periods can fix the same
protected face, but produce only that same face; their primitive
stabilizer was already recorded.

In E the functional x_Z vanishes on the entire bottom chain,
so the identical ray-coefficient argument gives \(|x_Z|\le Cs\).
The shear does not change x_Z. An intersection at s>0 therefore
bounds \(L=2j_1+bj_2\). The second coordinate of its period is
\[
 -asj_1+(Nr+(N-1)s)j_2
       =N(r+s)j_2-\frac a2sL.
\]
Since r+s=1, the bounded x_V coordinate bounds j2, and then j1.
The s=0 kernel again only repeats the same protected face.

Thus the intersection fan has finitely many period orbits. Its
rational polyhedral cones have common faces by the elementary
intersection-fan construction. Relative coning and ER.1–4 give
a period-equivariant regular refinement preserving the same
three boundary fans. This establishes a finite common protected
refinement of the two actual fans, without declaring it invariant
under further powers of S.

## OSH.3. No finite-orbit invariant I fan for this scalar shear

In fact the scalar shear alone has no invariant full-dimensional
polyhedral fan with finitely many period orbits in the I sector.
Suppose such a fan were invariant. Since S commutes with periods,
some positive power sends a full cone C to an integral translate:
\(S^L C=T_jC\). The integral map \(T_{-j}S^L\) permutes the
finitely many primitive extreme rays of C. A further positive
power p fixes each ray and therefore the full four-dimensional
span. Hence
\[
                         S^{Lp}=T_{pj}
\]
as linear maps, not merely as a permutation of cones. Comparing
their r-coefficients in I gives pj=0. Comparing their
s-coefficients then gives Lpc=0, contradicting c≠0.

The same conclusion holds in W: its r-coefficient first forces
\(j=h(-b,1)\); the first coordinate of Hj is then -bh, so the
s-coefficient forces h=0, and again c=0. E has no such obstruction
because of the rational-period identity in OSH.1.

Consequently one common refinement does not supply a closed
repeated-deck atlas for the scalar shear alone. This is an exact
obstruction to that specified finite-orbit invariant-fan attempt.
It is not an obstruction to every possible analytic completion.

## OSH.4. The source part still required by the cap

The actual finite cap carries A0 as well as the scalar factor.
On its chain A shifts the component index by kn and rotates the
m-root. Its mth power is the literal B^n. In contrast, the
currently constructed raw collision E boundary has component
index j modulo N and its displayed T-annulus units have v-order
zero, so that raw annular monodromy fixes each such index.
Fourfold's direct fixed-component calculation retains this
difference.

The next map must therefore continue the actual root/source/
Cartier A0 through the annulus. Combining that source map with
the scalar factor can give the full A^{-1} continuation, whose
mth power is B^{-n} on the quotient. The calculations above do
not replace that map by the scalar S. Neither the common
refinement nor its finite E period establishes the missing
collision-to-cap identification.
