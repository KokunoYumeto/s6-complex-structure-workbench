# The actual source A3 charts and their relative tangent numbers

This calculation concerns the source quotient on the strict surface.
It supplies its tangent characteristic data. Its physical normal
extensions are the separate full-star calculation in the selected
infinity ledger.

On the central ordinary source the equation and residual action are
\[
 \bar Y^2=\bar X^3-2\chi^2\bar X^2+\bar X,
 \qquad
 \gamma(\chi,\bar X,\bar Y)=(i\chi,-\bar X,-i\bar Y).
\]
At O use the actual local coordinate \(\eta=-\bar X/\bar Y\).
At T use \(\eta=\bar Y\), with \(\bar X\) the implicit
holomorphic root; the derivative of the cubic in \(\bar X\)
is one at T. At both points the full source action is exactly
\((\chi,\eta)\mapsto(i\chi,-i\eta)\). Thus these two
source quotient germs have the invariant polynomial coordinates
\[
 x=\chi^4,\qquad y=\eta^4,\qquad z=\chi\eta,
 \qquad xy=z^4.
\]
These generate the invariant ring. In an invariant monomial the
two exponents have the same residue modulo four. Removing that
many factors of \(\chi\eta\) leaves powers of \(\chi^4\)
and \(\eta^4\). The sole displayed relation eliminates the
product of these last two generators, giving the same monomial
basis as the invariant ring.

## The actual proper source resolution

Use the quotient cocharacter lattice with basis
\(((1,-1)/4,e_\eta)\). Its two original boundary rays are
\((4,1)\) and \((0,1)\). The complete regular subdivision
has rays \((k,1)\), \(0\le k\le4\). In the ordered cone
\(((k+1,1),(k,1))\), \(0\le k\le3\), write the free
coordinates as \((a,b)\). The literal map to the original
quotient is
\[
 x=a^{k+1}b^k,\qquad
 y=a^{3-k}b^{4-k},\qquad z=ab.
\tag{ASa}
\]
All exponents are nonnegative integers, every ordered determinant
is one, and the cone supports fill the original cone with their
common edges. These maps glue through their invariant characters
and define the proper toric resolution. On \(x\ne0\), the
first chart has inverse \(a=x,b=z/x\). On \(y\ne0\), the
last chart has inverse \(b=y,a=z/y\). These opens cover the
quotient away from its origin, proving the exact boundary
identification. There are three exceptional projective lines,
with primitive wall relations
\((k-1,1)+(k+1,1)=2(k,1)\). Their integral intersection matrix is
\[
 I_{A_3}=\begin{pmatrix}-2&1&0\\1&-2&1\\0&1&-2\end{pmatrix}.
\tag{ASb}
\]
Its determinant is \(-4\), retaining the boundary order four.

The invariant source two-form has the exact expression
\[
 d\chi\wedge d\eta
 =\frac z4\,d\log x\wedge d\log z
 =\frac14\,da\wedge db
\tag{ASc}
\]
in all four oriented charts. It is nowhere zero there. Thus the
canonical frames on the resolution and orbifold source agree
under the actual punctured comparison, and their relative
first-Chern-square difference is zero.

## A common boundary vector field and the relative tangent integral

Use the original ball \(|\chi|^2+|\eta|^2\le r^2\). In
the invariant variables its boundary is
\(|x|^{1/2}+|y|^{1/2}=r^2\). Pulling this equation back through
ASa defines the same smooth outer boundary on the resolution.
The source vector field
\[
 \frac43\chi\frac{\partial}{\partial\chi}
 +\frac23\eta\frac{\partial}{\partial\eta}
\tag{ASd}
\]
is invariant and outward pointing there. Its logarithmic vector
in \((x,z)\) is \((16/3,2)\). Therefore its exact derivative
weights in the k-th chart of ASa are
\[
 \left(\frac{16}{3}-2k,\quad 2k-\frac{10}{3}\right),
 \qquad k=0,1,2,3.
\tag{ASe}
\]
Neither weight vanishes. The lifted field has one zero at each
of the four distinct toric chart origins and no other zero.
Every zero has real oriented index one: an invertible complex
derivative has positive real determinant equal to the squared
modulus of its complex determinant. The original orbifold
zero has stabilizer order four and index \(1/4\). Since these
are the same field on the identified boundary, the exact
relative second-Chern difference is \(4-1/4=15/4\). Formula
ASc and \(p_1=c_1^2-2c_2\) give
\[
 \Delta\!\int c_2=\frac{15}{4},\qquad
 \Delta\!\int p_1=-\frac{15}{2}
\tag{ASf}
\]
at each of the two actual O/T source germs.

The other two order-two source points \((\bar X,\bar Y)=(\pm i,0)\)
are exchanged by \(\gamma\). Their joint quotient therefore has
one A1 source point, with the exact boundary, determinant and
vector-field comparison already proved in the mu2 residue note.
Its changes are \(\Delta c_2=3/2\), \(\Delta p_1=-3\).
There are no other source stabilizers: on the central smooth
elliptic curve the fixed points of \(\gamma\) are O,T, and
the additional fixed points of \(\gamma^2\) are precisely
that exchanged pair. The two A3 and one A1 contributions sum to
\[
 \Delta c_2=9,\qquad \Delta p_1=-18.
\tag{ASg}
\]

## The complete source quotient characteristic numbers

The native source map on the \(\chi\)-unit open is
\[
 t_e=\chi^{-4},\qquad
 x_e=\chi^{-2}\bar X,\qquad y_e=\chi^{-3}\bar Y.
\]
It gives exactly \(y_e^2=x_e^3-2x_e^2+t_ex_e\), with
discriminant \(64t_e^2(1-t_e)\). The actual native resolutions
at zero and one have fibres I2 and I1, respectively. At infinity,
the reduced quotient of the good elliptic curve is a projective
line: the invariant function \(\bar X^2\) has degree four and
its fibres are the four-element residual-action orbits. The
three source resolutions above add chains of lengths three,
three and one, each attached at its recorded quotient point.
The reduced infinity fibre therefore has Euler number
\(2+3+3+1=9\). Thus the minimal source resolution has total
Euler number \(2+1+9=12\).

Its canonical frame on the finite chart is
\(dx_e\wedge dt_e/(2y_e)\). On the infinity Weierstrass
chart \(q=t_e^{-1}\), \(x'=q^2x_e\), \(y'=q^3y_e\),
the exact expression is
\[
 -q^{-1}\,\frac{dx'\wedge dq}{2y'}.
\]
The source resolutions preserve its canonical frame by the
explicit crepant comparisons. Hence the canonical divisor is
the negative of the full infinity fibre, whose square is zero.
It follows that the minimal source has \(p_1=-24\).
Subtracting the exact relative changes ASg gives the original
orbifold source values
\[
 \int_{\bar S}c_2=3,\qquad
 \int_{\bar S}p_1=-6,
\tag{ASh}
\]
with the specified complex orientation and the actual finite
orbifold chart factors. All normal-line and common-fan
refinement corrections remain in their separately typed
source/line maps. No physical surface or return value is
assigned by this source tangent calculation.
