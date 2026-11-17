# The starred cap and the finite generic source reduction

## P3K.21. Proved: the starred-fibre cap obstruction and the remaining generic pairs

In the established sphere orbit and root-line cap scope, a
nonzero-linearization \(I_s^*\) source fibre can occur only
with \(s=1\), a primitive quadratic cap, and
\[
                         a\equiv0\pmod2,
                         \qquad b\equiv2\pmod4.       \tag{P3K.21.1}
\]
The two \(I_3^*\) rank-one source configurations are excluded.
Combined with P3K.19–20 and the actual source table, the
remaining generic source coefficients are the 26 pairs in
the 16 profiles displayed below.  This is a proved finite
restriction on the generic source data; it does not declare
all remaining affine cap tuples to be sphere tuples without
their integral gluing calculation.

**Proof: the marked quadratic root.** The quadratic root of
\(I_s^*\) is the Tate \(I_{2s}\) fibre.  Its deck
acts on component labels by \(j\mapsto-j\), since
it is elliptic inversion and fixes the zero component.
The two invariant components are \(j=0,s\).  On each,
inversion has two fixed smooth points.  Near such a point
the two local coordinates have signs \((-1,-1)\), so
the quotient has equation \(v^2=uq\).  Resolving it
adds a multiplicity-one outer component.  The quotient
of the cycle is a path of \(s+1\) multiplicity-two
components, with two such outer leaves at each end.
This is the actual affine \(D_{s+4}\) graph.

The end \(j=0\) contains the zero section.  Remove
its corresponding outer leaf to obtain the finite
\(D_{s+4}\) intersection matrix.  Its inverse has
diagonal entry one at the other leaf of that end, and
\((s+4)/4\) at the two far-end leaves.  These entries
follow directly from the graph matrix; they are also the
local-height entries used in P3F.2.  The primitive
rank-one generator meets a spinor leaf, so its quadratic
root component is exactly \(s\), not zero.
The further degree-\(m/2\) root multiplies component
labels by \(m/2\).  Thus on an even \(m\)-root
the source fibre is \(I_{sm}\), the generator has
component \(sm/2\), and the canonical deck still
acts by reflection \(j\mapsto-j\).

An odd root leaves a starred fibre with unequal
multiplicities, excluded by the reduced-root conclusion
of P3K.19.  For an even root write the source component
action of the affine cap map as
\(A(j)=-j+\alpha\).  The suspension map acts as
\(B(j)=j+bsm/2\).  Its root fibre is singular, so
P3K.19 makes the pair \((m,n)\) primitive.  In
particular \(n\) is odd.  Since \(A^m\) is the
identity on components, the actual norm relation
\(A^m=B^n\) forces \(b\) even.  Then \(B\)
has trivial component action.  A reflection has orbits
of size at most two; transitivity forces \(sm\le2\).
Hence \(s=1,m=2\), and \(\alpha\) is odd.
The multidegree-zero root line has generic component
\(asm/2\); its component-Laplacian equation forces
\(a\) even, as in P3K.19.

There is one further unit constraint, which the component
labels alone would miss.  Write the quadratic Tate period
as \(Q_T=z^2u(z^2)\) and the generator as
\(Z_G=zv(z)\).  Its actual descent under inversion says
\(Z_G(-z)=Q_T/Z_G(z)\).  Thus
\(v(z)v(-z)=-u(z^2)\), and the identity-component
limit of \(2G\) is exactly \(-1\).  For the
affine reflection write
\(A(Z,z)=(R(z)/Z,-z)\), where
\(R=z^\alpha w(z)\).  Its square multiplies
\(Z\) by \(R(-z)/R(z)\), whose central value is
\((-1)^\alpha=-1\).  The central value of the
right-hand side \(B^n\) is
\((-1)^{bn/2}\).  Since \(n\) is odd, equality
forces \(b\equiv2\pmod4\).  This proves (P3K.21.1)
with both the component and unit parts of the norm retained.

**Proof: the finite generic factor list.** A simple whole
zero requires an \(I_1\) source value and \(ab=d\)
by P3K.20.  The three profiles with no \(I_1\) are
therefore removed.  P3K.19 imposes \(N\mid a\)
and \(\gcd(N,b)=1\) at every multiplicative fibre.
The preceding argument removes both \(I_3^*\) profiles
and imposes (P3K.21.1) at \(I_1^*\).  Enumerating the
positive divisors of each of the eight height denominators
now gives exactly the following list.

| OS row | Source fibre profile | Remaining \((a,b)\) |
|---|---|---|
|43|\(III^*+3I_1\)|\((1,2),(2,1)\)|
|43|\(III^*+II+I_1\)|\((1,2),(2,1)\)|
|45|\(I_8+4I_1\)|\((8,1)\)|
|45|\(I_8+II+2I_1\)|\((8,1)\)|
|47|\(I_7+I_2+3I_1\)|\((14,1)\)|
|47|\(I_7+I_2+II+I_1\)|\((14,1)\)|
|47|\(I_7+III+2I_1\)|\((7,2),(14,1)\)|
|49|\(IV^*+I_2+2I_1\)|\((2,3),(6,1)\)|
|49|\(IV^*+III+I_1\)|\((1,6),(2,3),(3,2),(6,1)\)|
|50|\(I_1^*+I_3+2I_1\)|\((6,2)\)|
|50|\(I_1^*+IV+I_1\)|\((2,6),(6,2)\)|
|55|\(I_5+I_4+3I_1\)|\((20,1)\)|
|55|\(I_5+I_4+II+I_1\)|\((20,1)\)|
|56|\(I_5+I_3+I_2+2I_1\)|\((30,1)\)|
|56|\(I_5+I_3+III+I_1\)|\((15,2),(30,1)\)|
|56|\(I_5+IV+I_2+I_1\)|\((10,3),(30,1)\)|

The script `code/part3_fourfold/source_reduction.py` starts
from all 21 source profiles of P3F.1, retains their marked
height denominators, and executes these exact tests.  It
also exports the affine \(D\) matrices and their inverse
entries, so the starred marking is independently checkable.

**Proof: the indispensable vertical correction in row 50.**
The list allows arbitrary vertical line divisors, as the
literal construction does.  For its two row-50 factors,
the necessary correction is explicit.  Label the affine
\(D_5\) fibre by central vertices \(C_0,C_1\),
identity outer leaf \(L_0\), its order-two mate \(L_1\),
and spinor leaves \(R_0,R_1\).  The two left leaves
meet \(C_0\), the two right leaves meet \(C_1\),
and \(C_0,C_1\) meet.  Translation by \(2G\) or
\(6G\) swaps \(L_0,L_1\) and \(R_0,R_1\),
while fixing the two central components.

For \(a=2\) or \(6\), the section \(aG\) meets
\(L_1\), so the bare section-line degree vector is
\(e_{L_1}-e_{L_0}\).  If \(B_D\) is the actual
affine intersection matrix, then
\[
 e_{L_1}-e_{L_0}-B_D e_{L_0}
                  =e_{L_0}+e_{L_1}-e_{C_0}.          \tag{P3K.21.2}
\]
The right-hand side is invariant under the stated
translation.  Thus the actual line
\(\mathcal O(aG-O-L_0)\), with \(L_0\) here a
vertical fibre component, has the required invariant
component degrees.  At the other reducible fibre the
displayed factor pairs likewise have invariant component
degrees: at \(I_3\) the line point is in the identity
component; at \(IV\), either the line point is in the
identity component or the translation preserves all
components.  The Hom ratio is generically trivial and
has degree zero on every fibre component.  Its vertical
divisor is therefore a sum of whole fibres, and P3K.14
gives its base degree one.  Choosing its section places
the simple zero at the selected \(I_1\).

This proves that these corrected source line data satisfy
the literal whole-fibre Hom condition.  It does not
replace the remaining integral cap/gluing verification
for their total threefolds.
**End of proof.**

The 26 pairs are a finite necessary source reduction in
the declared orbit and cap scope.  The full cap data still
include their exact cyclic norm, logarithmic site, integral
delta collar, Seifert determinant, and integral topology.
No unverified pair in this table is assigned a sphere or
a return index solely by this arithmetic list.
