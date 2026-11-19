# The two remaining two-torsion points and their actual order-two quotients

This local calculation adds the non-O/T finite strata to the selected-infinity assembly. It retains the source, point-line, deck, and determinant arrows. The global normal ledger and return remain unfinished.

On the good ordinary source
\[
 \bar Y^2=\bar X^3+a_2\bar X^2+d\bar X+\sigma^2,\qquad
 a_2=A(\epsilon)\chi^2,\quad d=1-3\epsilon^2,\quad
 \epsilon=\chi\sigma,
\]
the central points \((\bar X,\bar Y)=(i,0),(-i,0)\) are exchanged by
the actual fourth-root map
\[
 (\chi,\sigma,\bar X,\bar Y)\mapsto
       (i\chi,-i\sigma,-\bar X,-i\bar Y).
\]
Its square fixes these two points. The derivative of the cubic with
respect to \(\bar X\) is \(-2\) there. Consequently
\((\chi,\sigma,\zeta=\bar Y)\) are analytic coordinates in two
neighbourhoods, with \(\bar X\) the unique local implicit root.
The fourth-root map exchanges the two neighbourhoods by the displayed
formula, and its square is
\((\chi,\sigma,\zeta)\mapsto(-\chi,-\sigma,-\zeta)\).

Here \(\bar X\) is a unit, so the pullback of the original source blowup
ideal \((x_o,y_o,t_o)\) is \((\sigma^2)\). Its actual morphism to the
resolved original source uses
\[
 t_o/x_o=\sigma^2/(d\bar X),\qquad
 y_o/x_o=\sigma\zeta/(d\bar X).
\]
No O/T section graph is inserted at these points.

Use the actual ordinary line chart
\[
 X_jY_j=\sigma,\qquad V_{\rm phys}=\sigma^jX_j.
\]
The four free coordinates are \((\chi,\zeta,X_j,Y_j)\). The full
fourth-root arrow, from one source neighbourhood to the other, has
weights \((1,-1,j,-j-1)\) modulo four. Its square has weights
\((1,1,j,j+1)\) modulo two: three coordinates are odd and one is
fixed. For even \(j\) the fixed coordinate is \(X_j\), and the actual
fixed-stratum ideal is
\[
 I_j=(\chi,\zeta,Y_j).
\]
For odd \(j\) it is \(Y_j\), and \(I_j=(\chi,\zeta,X_j)\).

## The proper quotient resolution and its complete polynomial maps

Write the three odd coordinates as \(w_1,w_2,w_3\) and the fixed
coordinate as \(u\). Blow up the actual ideal
\((w_1,w_2,w_3)\) on the cover. On its \(a\)-th chart write
\[
 w_a=t,\qquad w_b=t z_b,\qquad w_c=t z_c.
\]
The involution fixes \(u,z_b,z_c\) and sends \(t\) to \(-t\).
The quotient chart therefore has the four smooth coordinates
\[
 (\rho=t^2,z_b,z_c,u).
\]
Its map to the original coarse quotient sends every quadratic
invariant to
\[
 w_iw_k=\rho z_i z_k,\qquad z_a=1,
\]
and retains \(u\). These six quadratic invariants and \(u\)
generate the whole invariant ring: every invariant monomial has even
total degree in the three odd variables, so it is a product of such
pairs and a power of \(u\).

The charts glue by the literal arrows
\[
 \rho_b=\rho_a z_b^2,\qquad
 z_a^{(b)}=z_b^{-1},\qquad
 z_c^{(b)}=z_c/z_b .
\]
In particular, their exceptional divisor is the projective plane of
the odd directions with its square radial transition, over the
unchanged \(u\)-axis.

This quotient is also the actual blowup of the coarse ideal generated
by the six quadratics. Indeed the second Veronese subalgebra of
the cover Rees algebra has degree \(n\) part \(I_j^{2n}\).
Its invariant part consists exactly of invariant monomials whose total
degree in the three odd coordinates is at least \(2n\), which is the \(n\)-th power of the quadratic
ideal in the invariant ring. Passing to Proj gives the displayed
coarse blowup. This proves properness and the comparison to the given
finite quotient, with no replacement of the quotient by its cover.

The exact program code/part3_root/e6_selected_infinity_mu2_pair.py
uses the actual quotient lattice in every one of the four values of
\(j\) modulo four. It inserts the primitive half-sum of the three odd
coordinate rays. The three resulting cones each have determinant
one in that quotient lattice. It writes all invariant-generator
monomial maps and checks their nonnegative integral exponents.
It also compares each toric chart to the explicit
\((\rho,z_b,z_c,u)\) coordinates by a saved permutation matrix.
All twelve charts, their full fourth-root phase powers and their
physical circle weights are saved. The present certificate passes
251 exact checks; the earlier structural-equality test failure is
retained with its correction.

## The entire source and line map lifts through this blowup

The full primitive \(-G\) chord on this source has the exact expressions
\[
 \bar X'=\frac d{\bar X}
          +\frac{2\sigma(\zeta+\sigma)}{\bar X^2},\qquad
 \zeta'=-\frac{\bar X'}{\bar X}\,\zeta
              +\left(1-\frac{\bar X'}{\bar X}\right)\sigma.     \tag{M2a}
\]
They follow by substituting the cubic into the chord slope
\((\zeta+\sigma)/\bar X\). Both \(\bar X\) and \(\bar X'\) are
units on the chosen two neighbourhoods. Thus
\[
 \zeta'=A_b\zeta+B_b\sigma
\]
has a full holomorphic unit \(A_b\). For \(b=1\), its two exact
coefficients are those in M2a. For \(b=3\), compose M2a three
times: the new \(A_b\) is the product of the three carried
coefficients, and \(B_b\) is the corresponding three-term
composition, with each coefficient evaluated at its actual
intermediate source point. This retains the complete functions.
They are invariant under the involution; the displayed fourth-root
arrow transports them to the coefficients in the other neighbourhood.

Let \({\cal C}=\lambda H\mathcal B_{a,b}\) be the entire genuine
point-line unit from EIR.53. The actual line reset is
\[
 j\mapsto j+4,\qquad
 X_j\mapsto{\cal C}X_j,\quad
 Y_j\mapsto{\cal C}^{-1}Y_j .
\]
For even \(j\), the induced map on the ordered generators of \(I_j\) is
\[
 \begin{pmatrix}\chi\\\zeta\\Y_j\end{pmatrix}
 \longmapsto
 \begin{pmatrix}
 1&0&0\\0&A_b&B_bX_j\\0&0&{\cal C}^{-1}
 \end{pmatrix}
 \begin{pmatrix}\chi\\\zeta\\Y_j\end{pmatrix}.                  \tag{M2b}
\]
Its determinant is \(A_b{\cal C}^{-1}\), a unit. For odd \(j\)
replace \(Y_j\) by \(X_j\), replace the off-diagonal entry by
\(B_bY_j\), and replace the final diagonal entry by \({\cal C}\).
The inverse chord and inverse line arrow give the inverse ideal map.
This proves equality of the actual pulled-back ideals.

Here is its complete chart lift, including the nonmonomial source
mixing. Let \(M\) be the appropriate matrix in M2b and let
\(w=t z\), with \(z_a=1\), be a source blowup chart. Put
\(L=M z\), with every coefficient evaluated at the actual source
coordinates. On a target chart with \(L_\beta\ne0\), the quotient
map is
\[
 \rho'=\rho L_\beta^2,\qquad
 z'_\gamma=L_\gamma/L_\beta .
\]
The neutral coordinate has its entire factor
\({\cal C}\) or \({\cal C}^{-1}\). The coefficients are invariant
under the involution and hence are holomorphic functions in the
quotient chart. Since \(M\) is invertible, these target domains
cover the image. The inverse ideal map proves invertibility of
the resulting lifted source-reset map.

The same ideal comparison applies on neighbouring line-chain charts:
on their actual nonzero-coordinate overlap, the two odd line
coordinates differ by the retained square of that nonzero
coordinate. Their fixed ideals and their Rees blowups agree through
that unit. The fourth-root arrow also preserves these ideals and
lifts by its explicit coordinate phases. If one source point is
chosen as the representative of the exchanged pair, the reset
closing is the actual \(\gamma^{-1}B\) representative change; its
saved fourth-root phases remain in the normal and line maps.

## Original source-volume comparison

At these two source points the invariant differential is
\[
 \bar\omega=u\,d\zeta,\qquad
 u=(3\bar X^2+2a_2\bar X+d)^{-1}.
\]
Its actual central value at either point is \(-1/2\).
The original source scaling used in MFe gives
\[
 2\Omega_o\wedge d\epsilon\wedge d\log V_{\rm phys}
 =8\sigma^3d^{-2}u\,
       d\chi\wedge d\zeta\wedge d\sigma\wedge d\log V_{\rm phys}.
\]
Directly from \(\sigma=X_jY_j\) and
\(V_{\rm phys}=(X_jY_j)^jX_j\),
\[
 d\sigma\wedge d\log V_{\rm phys}=-dX_j\wedge dY_j.
\]
Thus the exact coefficient in the displayed four free coordinates is
\[
 -8(X_jY_j)^3d^{-2}u .
\]
The logarithmic character is \((1,1,4,4)\), which is invariant under
the full fourth-root arrow. In the oriented unimodular quotient
charts the lattice determinant gives the full unit
\(-4d^{-2}u\). The certificate saves every ray order; its exceptional
ray has original marked-volume order two. It also saves the exact
nonnegative exponents of \(\epsilon\), \(q_{\rm new}=\chi^4\),
and \(\sigma^4\), and verifies
\(q_{\rm new}\sigma^4=\epsilon^4\).

The source-volume unit is transported by the full invariant
differential identity, including the derivative of M2a; it is not
replaced by its central value. The global determinant line, its
relative framing, the physical finite-isotropy faces, and the
original cap word \(AB^{j_\gamma}\) remain in the global assembly
ledger. This local resolution assigns no characteristic number.
