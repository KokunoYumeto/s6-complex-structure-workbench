# Reduced additive roots and the exact affine norm restriction

This draft refines the necessary source list of P3K.21.  It keeps
smooth good roots separate from the reduced additive roots by their
actual Weierstrass maps.  No total-space sphere or return invariant
is assigned here.

## 1. Actual root maps

Write the original minimal equation as \(y^2=x^3+f(q)x+g(q)\),
put \(q=z^m\), and substitute \(x=z^{2k}X,y=z^{3k}Y\).
The minimal value of \(k\), and the roots that remain reduced,
are as follows.  The leading coefficients in the indicated minimal
equations are units.

| Original type | Minimal exponent k | Smooth root | Other reduced root |
|---|---|---|---|
| II | floor(m/6) | m=0 mod6 | II for m=1 mod6; IV for m=2 mod6 |
| III | floor(m/4) | m=0 mod4 | III for m=1 mod4 |
| IV | floor(m/3) | m=0 mod3 | IV for m=1 mod3 |
| III* | floor(3m/4) | m=0 mod4 | III for m=3 mod4 |
| IV* | floor(2m/3) | m=0 mod3 | IV for m=2 mod3 |

For example, the III* equation has
\(f=q^3a(q),g=q^5b(q)\); the substitution gives valuations
\(3m-4k,5m-6k,9m-12k\) for \(f,g,\Delta\).
The residue \(3m\bmod4\) therefore gives smooth, III,
\(I_0^*\), or III* respectively.  The other rows follow from
the same displayed substitution, using discriminant valuations
2,3,4,8 for II,III,IV,IV*.  The omitted nonreduced roots are
excluded by P3K.19, with their actual component multiplicities.

The deck on the minimal equation is
\[
 D(X,Y,z)=(\zeta_m^{-2k}X,\zeta_m^{-3k}Y,\zeta_m z).
                                                               \tag{ACap.1}
\]
It extends to the minimal smooth surface by the corresponding
resolved charts.  For III the two component labels have no nontrivial
group automorphism.  For a reduced IV root, use the blowup chart
\(X=zX_1,Y=zY_1\).  Its two nonidentity branches are distinguished
by \(Y_1=\pm\sqrt{b(0)}\).  For an original IV and
\(m=3l+1,k=l\), the factor on \(Y_1\) is
\(\zeta_m^{-(3l+1)}=1\).  For an original IV* and
\(m=3l+2,k=2l+1\), it is
\(\zeta_m^{-(6l+4)}=1\).  Thus the canonical deck fixes all
three component labels in both cases.

For an original II and \(m=6l+2,k=l\), the same factor is
\(\zeta_m^{-(3l+1)}=-1\).  The deck fixes the identity component
and interchanges the two other IV components.  The original section
group has trivial component group, and its sections remain in the
identity component after this root: composing with the degree-three
good root gives the order-six automorphism, whose only fixed point is
the origin.  Equivalently this follows in the displayed blowup chart
from the original section and its deck invariance.  The suspension
therefore has trivial component action, while the affine deck has a
reflection action on three labels.  Its orbits have at most two
elements.  This IV root cannot be transitive and is excluded.

## 2. Generator limits with their exact source coordinate

For III and III*, the minimal good root has order four and central
curve \(Y^2=X^3+a_0X\), \(a_0\ne0\).  Its order-four
automorphism has precisely the fixed points \(O\) and \((0,0)\).
The latter is the nonzero two-torsion point.  For IV and IV*, the
minimal good root has order three and central curve
\(Y^2=X^3+b_0\), \(b_0\ne0\).  The fixed points are
\(O,(0,\sqrt{b_0}),(0,-\sqrt{b_0})\).  At either finite point
the tangent line has triple intersection, so these are the nonzero
three-torsion points by the cubic group law.

Here is the identification with the marked source components.  Near
\(O\), put \(w=-X/Y\).  The good-root map to the original
source has
\[
 -x/y=z^{-k}w,
 \qquad (r,k)=(4,1),(4,3),(3,1),(3,2)
\]
for III,III*,IV,IV* respectively.  Deck invariance makes a section
with root limit \(O\) have expansion
\(w(z)=z^k c(z^r)\).  The expressions
\(x=z^{2k}X(w),y=z^{3k}Y(w)\), with
\(X(w)=w^{-2}+\cdots,Y(w)=-w^{-3}+\cdots\), then give a
smooth point of the original identity component when \(c(0)\ne0\),
and the zero point when \(c(0)=0\).  Conversely a smooth
identity-component section gives this expansion.  Thus the source
component kernel is exactly the root fixed point \(O\).
The actual generator markings in P3F.2 are nonzero in the component
groups of order two or three, so their good-root limits have the
corresponding exact orders.  Composing any of the reduced additive
roots of Section 1 with its minimal good root gives the same marked
limit.  Its generator component is therefore again nonzero.

For II the order-six central automorphism fixes only \(O\): in
\(Y^2=X^3+b_0\), its two nontrivial coordinate characters would
force a finite fixed point to have \(X=Y=0\), which is impossible.

## 3. Good-root norm and reduced-additive component norm

After P3K.19 cancels the finite zero-gamma kernel, the cap has
\(\gcd(m,n)=1\).  On a smooth good central fibre write
\(A_0=T_R E\) and \(B_0=T_Q\), where \(E\) is the actual
finite linear monodromy of order \(r\mid m\).  It has no fixed
tangent vector.  Hence \(1+E+\cdots+E^{m-1}=0\) as an elliptic
endomorphism, and \(A_0^m=1\).  The actual norm
\(A^m=B^n\) gives \(nQ_0=0\).  Descent makes \(E Q_0=Q_0\).
By Section 2 its possible nontrivial order is \(p=2\) or 3,
which divides \(m\).  Coprimality forces \(Q_0=0\):
\[
 p\mid b\quad\text{at a smooth good root}.                         \tag{ACap.2}
\]

At one of the remaining III or IV roots, the canonical deck has
trivial component action and \(m\) is prime to the component order
\(p\).  If the affine translation has component \(r_0\), the
same actual norm gives
\[
 m r_0=n b[G]\quad\text{in }\mathbb Z/p.
\]
Thus the subgroup generated by \(r_0\) and \(b[G]\) is precisely
the subgroup generated by \(b[G]\).  Transitivity forces
\(p\nmid b\); the zero multidegrees of the root line force
\(p\mid a\) by its integral component-Laplacian equation.
Therefore
\[
 p\mid a,\quad p\nmid b\quad\text{at a reduced additive root}.
                                                               \tag{ACap.3}
\]
For every source denominator in P3K.21, the relevant prime occurs
exactly once in \(ab=d\).  Equations (ACap.2)--(ACap.3) select
complementary allowed root residues for the existing pairs; they do
not delete the complementary generic source pair.

## 4. An explicit surviving source affine norm

For III*, \((a,b)=(2,1)\) and \(m=3,n=1\), the actual root is
\[
 Y^2=X^3+z a(z^3)X+z^3b(z^3),
 \qquad D(X,Y,z)=(\zeta_3^2X,Y,\zeta_3 z).
\]
It is type III.  The marked \(Q=G\) has nonzero component and
the line point \(2G\) has zero component.  Multiplication by three
on the smooth local section group has derivative three on its
additive identity component and is a bijection on its two component
labels.  The analytic inverse-function theorem therefore gives the
unique local branch \(R\) with \(3R=Q\) and the prescribed
central point.  The deck preserves that branch, so \(D R=R\).
Consequently
\[
                     (T_R D)^3=T_Q.
\]
The root components are transitive under these actual source maps.
This explicitly verifies the source affine norm that the good-root
argument does not cover.  Extending its specified line lift and
checking the integral global gluing remain separate construction
steps; this example is not assigned sphere topology by its component
calculation alone.
