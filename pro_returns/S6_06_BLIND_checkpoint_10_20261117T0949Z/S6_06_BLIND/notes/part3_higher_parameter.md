# P3K.11. Proved: the higher parameter and its two characteristic integers

Fix logarithmic orders \(3K,4L\), with
\(\gcd(3K,4L)=1\), and primitive logarithmic coefficients
\(n_0,n_1\), so \(\gcd(n_0,3K)=\gcd(n_1,4L)=1\).
For the sphere members impose
\(a=4L n_0+3K n_1=\pm1\), with zero additional cusp collar.
Use the period coordinate \(c\) and scalar \(u\) of the original
family.  The closed higher parameter is
\[
 w_h=\exp\!\left(-\frac{\pi i c}{KL}\right),
 \qquad u=\kappa w_h^{2KL},\qquad \kappa\ne0.
\]
In particular, the original expression \(w=\exp(-\pi i c)\)
does not give one closed higher loop when \(KL>1\).
The positive sixfold cover \(w_h=r^6\) gives the signed
gamma turn \(a\gamma\).  For the positive-gamma sphere marking
\(a=1\), with the descended rotating framing of P3K.9, the Jin
integers of the positive \(w_h\)-loop are
\[
                  (k,\ell)=(-KL,-4KL).
\]
The integer return index is zero for either sphere sign.
These statements identify
both the parameter and the framing in the supplied higher-order
formulas.

**Proof: the integral orbifold complex.** We use the marked
lattice and period convention of P5.6.  Its cohomological
monodromy matrices are
\[
 T_1=\begin{pmatrix}
 1&0&-6&2\\0&-1&1&1\\0&-1&0&1\\0&0&0&1
 \end{pmatrix},\qquad
 T_2=\begin{pmatrix}
 1&6&0&-3\\0&0&-1&1\\0&1&0&0\\0&0&0&1
 \end{pmatrix}.
\]
Put \(A_i=T_i^{-t}\), \(A_0=(A_1A_2)^{-1}\),
\(N_1=1+A_1+A_1^2\), and
\(N_2=1+A_2+A_2^2+A_2^3\).  The lattice local system
on the higher root base is the pullback of the original one.
Consequently its finite cyclic norm operators are exactly
\(K N_1\) and \(L N_2\).  This assertion retains the
ineffective stabilizers: the generator of the additional
order-\(K\) or order-\(L\) stabilizer acts as the identity
on the lattice, so the full cyclic sum repeats the original
sum precisely \(K\) or \(L\) times.

Here is a complete block specification of the integer complex
used in the computation.  Let
\[
 C^0=\Lambda\oplus\Lambda\oplus\Lambda\oplus\mathbb Z^2,
 \quad C^1=\Lambda^7,\quad C^2=\Lambda^5,
 \quad C^3=\Lambda^2,
 \qquad \Lambda=\mathbb Z^4,
\]
and let \(J:\mathbb Z^2\to\Lambda\) have columns
\(e_3,e_4\).  In the displayed ordered summands, the three
differentials are
\[
\begin{split}
 d^0(a,b,c,z)={}&\bigl((A_1-1)a,(A_2-1)a,
 (A_1-1)b,(A_2-1)c,\,a-b,a-c,a-Jz\bigr),\\
 d^1(p,q,r,s,u,v,w)={}&\bigl(KN_1r,LN_2s,
 p-r-(A_1-1)u,\ q-s-(A_2-1)v,\\
 &\hspace{39mm}-A_0p-A_0A_1q-(A_0-1)w\bigr),\\
 d^2(x,y,z_1,z_2,z_0)={}&\bigl((A_1-1)x,(A_2-1)y\bigr).
\end{split}
\]
The pair-of-pants and the three annuli give the last three
summands of \(C^2\).  The first two are the degree-two terms
of the finite cyclic resolutions; the cusp contributes its
invariant lattice \(J\mathbb Z^2\) in degree zero.  These
are precisely the gluing maps of the lattice sheaf, including
the cyclic degree-two terms.  In particular, no finite norm
relation is replaced by a rational invariant projector.
Direct multiplication gives \(d^1d^0=d^2d^1=0\).

Write
\[
 \delta=(0,0,0,1)^t,\quad
 \epsilon_1=(1,2,-4,0)^t,\quad
 \epsilon_2=(1,3,-3,0)^t.
\]
The two invariant lattices have primitive bases
\(B_i=(\delta,\epsilon_i)\), and the norm matrices in
these bases are
\[
 B_1^{-1}N_1=
 \begin{pmatrix}0&2&1&3\\3&0&0&0\end{pmatrix},
 \qquad
 B_2^{-1}N_2=
 \begin{pmatrix}0&2&2&4\\4&0&0&0\end{pmatrix}.
\]
Here \(B_i^{-1}\) denotes the inverse coordinate map on its
image, so these displayed expressions are integral maps
\(\Lambda\to\mathbb Z^2\).  A primitive basis of
\(\ker d^2\) is \(\operatorname{diag}(B_1,B_2,I_{12})\).
The exact computation eliminates twelve unit pivots in the
matrix of \(d^1\) in that basis.  Every operation is an
elementary operation over \(\mathbb Z[K,L]\); the exported
left and right matrices have determinant \(\pm1\).
The remaining matrix has the same image as the three columns
\[
 R_0=
 \begin{pmatrix}
 K&0&0\\0&0&-3K\\0&2L&0\\0&0&4L
 \end{pmatrix}.
\]
This last image equality is also certified integrally: the
export gives matrices \(C,Q\) with
\(R_{\rm tail}=R_0C\), \(CQ=I_3\), and
\(R_{\rm tail}Q=R_0\).  Thus it is a proof for symbolic
\(K,L\), in addition to the executed Smith forms.
Equivalently, adjoining the eliminated generator \(h_c\),
the presentation is
\[
\begin{gathered}
 K\delta_1=0,\qquad 2L\delta_2=0,\\
 3K\epsilon_1=h_c=4L\epsilon_2.
\end{gathered}
\]
Since \(\gcd(3K,4L)=1\), the last relation gives a free
rank-one group and no torsion.  Moreover \(K\) is odd and
\(\gcd(K,L)=1\).  Therefore
\[
 H^2(\widehat B,\mathcal H)
 =\mathbb Z\oplus\mathbb Z/K\oplus\mathbb Z/(2L)
 =\mathbb Z\oplus\mathbb Z/(2KL).
\]
The complete matrices and elementary transformations are in
`code/part3_fourfold/higher_parameter.json`.
The same script computes the full integer complex, rather than
only this reduced presentation, for
\((K,L)=(1,1),(1,2),(1,5),(3,1),(5,1),(5,2),(7,5),(13,7)\).
Their torsion orders are respectively
\(2,4,10,6,10,20,70,182\), with free rank one in every case.

**Proof: the actual torsor period.** In the fixed period
coordinates, changing \(c\) to \(c'=c-b\) is the integral
shear
\[
 S_b=I+bE_{41},\qquad
 \Pi_c=\Pi_{c'}S_b,\qquad b\in\mathbb Z.
\]
It fixes \(\delta\) and sends each \(\epsilon_i\) to
\(\epsilon_i+b\delta\).  The logarithmic vectors are
\(r_i\delta+n_i\epsilon_i\).  Their actual logarithmic
annulus cocycles therefore change the characteristic class
by
\[
             b(n_0\delta_1+n_1\delta_2).
\]
This follows either by inserting the two vectors in the
displayed cochain complex, or by taking the logarithms in the
gluing maps \(x\mapsto x+\log(s_i)v_i/(2\pi i)\).
The coefficient \(r_i\) is fixed by the shear and contributes
zero to the difference.  Primitivity implies
\(\gcd(n_0,K)=\gcd(n_1,2L)=1\), so the displayed torsion
element has order exactly \(2KL\).  A change of logarithm
branch changes its cochain representative by a coboundary
and leaves this conclusion unchanged.

For completeness, the zero of this characteristic obstruction
is realized by actual holomorphic translations.  The vector
bundle of Lie algebras on the higher root base is the pullback
of the original bundle.  The added stabilizers act trivially
on its fibres.  Taking their invariants is exact in
characteristic zero, and the coarse pushforward is unchanged.
Consequently the explicit original calculation
\(H^1(\widehat B,\mathcal V)=H^2(\widehat B,\mathcal V)=0\)
continues to hold.  In the exponential sequence
\(0\to\mathcal H\to\mathcal V\to\mathcal V/\mathcal H\to0\),
the connecting map from torsors to \(H^2(\mathcal H)\) is
therefore an isomorphism.  When \(2KL\mid b\), solve the
integer coboundary equation above and subtract its logarithms
on the overlapping charts.  The remaining vector-valued
cocycle is a coboundary by \(H^1(\mathcal V)=0\); exponentiating
its chartwise primitives gives the required translation
isomorphism.  Reversing these primitives is its inverse.
At the cusp the shear changes the bounded beta term by an
integer; its toric factors \(\exp(2\pi i C\lambda)\), fan,
and monomial transition maps are identical.  Thus these chart
translations extend through the actual filling, as in the
explicit sheaf construction of P5.6.  Conversely a marked
translation isomorphism makes the characteristic difference
zero, so \(2KL\mid b\).  This proves the asserted exact
period in the marked family, with an extending morphism in
both directions.

**Proof: the loop and its characteristic numbers.** The scalar
relation is \(u=\kappa\exp(-2\pi i c)\).  Quotienting the
marked parameter by its just-proved period \(2KL\) gives
\(w_h=\exp(-\pi i c/(KL))\), and consequently
\(u=\kappa w_h^{2KL}\).  Put \(d=12KL\),
\(u=\kappa r^d\), and \(v=\log r/(2\pi i)\).
We retain the sign of the actual origin calculation.  The
finite-cap parameter descent is translation by
\[
 H(t)\delta=-\frac{4L n_0\log t+3K n_1\log(t-1)}{2\pi i}\delta.
\]
At the cusp it is \((as+U(q))\delta\), where \(U\) is a
single-valued holomorphic unit logarithm.  Write the period
\(\gamma=(\Gamma,C-s-dv)^t\).  On \(q=Q^d\), the
actual extending origins are
\[
\begin{split}
 o&=\binom{-a\Gamma s/d}{a s^2/(2d)-aCs/d+v(as+U)},\\
 \sigma&=\binom{a\Gamma v}{vU+aCv-ad v^2/2+ad v/2}.
\end{split}
\]
Their parameter differences are respectively \(H\delta\)
and \(H\delta+a\gamma\).  Their \(Q\)-differences are
integral lattice periods because \(d\) is even.  The
bounded cusp expression for \(\sigma\), and the invariant
zero coordinate after subtracting \(o\), give precisely the
extending sections in the node charts used in P2.2--3.
This checks the same morphisms with \(12\) replaced by
\(d\); it retains the signed twist.  Subtracting gives
\[
 F=\sigma-o
 =a\binom{\Gamma(s+dv)/d}{C(s+dv)/d-(s+dv)^2/(2d)+dv/2},
\]
and hence
\[
 F(s,v+\theta)-F(s,v)
 =a\theta\gamma+\frac{ad}{2}\theta(1-\theta)\delta.
\]
The last term is a periodic unitary gauge with both endpoint
values zero.  Thus the quotient clutch is the signed gamma
loop \(a\gamma\).  Equating the scalar expressions gives
the exact sixfold map \(w_h=r^6\), independently of the sign.

For \(a=1\), the page calculation P3F.17 gives
\[
 s_\delta=-2KL,\qquad p_{\rm rel}=-24KL.
\]
The normal-frame calculation of P3K.9 applies with page degree
\(12KL\).  Its transition factors into a two-dimensional
factor and a circle factor, exactly as in that proof;
the cubic clutch integral remains zero.  Thus
\(p_1(\bar\nu)=0\), whereas the Euler determinant has
square \(b^2=4s_\delta=-8KL\).  The oriented sphere-bundle
comparison P3K.7 gives
\[
 k_\gamma=\frac{3(-8KL)}4=-6KL,
 \qquad \ell_\gamma=-24KL.
\]
To descend the framing, choose any framing over the
\(w_h\)-circle.  Its sixfold pullback differs from the
rotating framing by a class in
\(\pi_1\operatorname{Map}(S^2,SO(3))=\mathbb Z/2\oplus\mathbb Z\).
The free difference is \(-6KL-6k_0\), which is divisible
by six.  Remove the constant-axis torsion loop, which extends
over the fixed \(D^3\) and changes neither characteristic
number.  The remaining class is the sixfold pullback of an
integral framing class, exactly as proved in P3K.9.  The
resulting descended rotating framing therefore gives
\(6k=-6KL\) and \(6\ell=-24KL\).  This proves the
stated pair and \(A=(4k-\ell)/24=0\).  For \(a=-1\),
the just-computed clutch traverses the gamma loop inversely.
The actual real trace of P3K.6--7 applies to this source
page with the corresponding boundary orientation; the index
of the inverse loop is the negative of the forward index.
That forward index is zero since
\(12s_\delta-p_{\rm rel}=0\).  Consequently the covered
index is zero also for \(a=-1\), and integral additivity
implies that the original \(w_h\)-loop has index zero.
The displayed individual pair is assigned to the stated
positive-gamma marking, so it involves no implicit reversal
of a negative sphere datum.

The original expression \(w\) and the higher expression
\(w_h\) satisfy \(w=w_h^{KL}\).  A single positive
\(w\)-loop only advances \(c\) by its original period two;
the higher characteristic obstruction vanishes for that
advance exactly when \(KL=1\).  This explicitly accounts
for the otherwise different-looking cover counts.  Changing
the final normal framing still changes \((k,\ell)\) by
\(n(1,4)\), as in P3F.11; the displayed values use the
descended rotating convention throughout.  **End of proof.**
