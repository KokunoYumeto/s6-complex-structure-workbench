# The exact equivariant tangent clutch at a toric flop

Working local comparison for the cross-edge problem, 17 November 2026.
This note identifies a universal relative characteristic class and
retains the separate global cycle map needed to evaluate it.

Use the Cox action with weights \((-r-s,0,r,s)\), and the actual
quaternion products of P3K.23. Put
\[
 a_\theta=e^{-i(r+s)\theta/2},\qquad
 b_\theta=e^{i(r-s)\theta/2}.
\]
The old and new products have actions
\[
 (y,q)\mapsto(a_\theta y a_\theta^{-1},a_\theta q b_\theta),
 \qquad
 (y',q)\mapsto(b_\theta^{-1}y'b_\theta,a_\theta q b_\theta).
\]
Their actual boundary identification is
\[
                      y'=q^{-1}yq.                 \tag{ET.1}
\]
Substitution proves equivariance, including odd half-angle endpoints.

Give the real four-plane \(q\) the orientation \((1,i,j,k)\).
Writing \(q=z_0+j\overline{z_1}\) identifies it with an oriented
complex two-plane of weights \((-s,-r)\). Its equivariant Euler
class is consequently
\[
                      e_{S^1}(q)=rs\,u^2 .
\]
The old three-plane \(y\) is a trivial real line plus a rotation
plane of weight \(-(r+s)\). The new three-plane \(y'\) has
rotation weight \(s-r\). Thus the actual equivariant tangent
representations give
\[
 \begin{aligned}
 p_{1,S^1}^{\rm old}&=2(r^2+rs+s^2)u^2,\\
 p_{1,S^1}^{\rm new}&=2(r^2-rs+s^2)u^2,\\
 p_{1,S^1}^{\rm new}-p_{1,S^1}^{\rm old}
                  &=-4rs\,u^2=-4e_{S^1}(q).
 \end{aligned}                                      \tag{ET.2}
\]
This retains the real orientation of \(q\); treating its second
quaternion coefficient as an unconjugated complex coordinate
would reverse the Euler sign.

Here is the relative map behind (ET.2). Over \(D^4_q\), let
\(V_{\rm old}\) and \(V_{\rm new}\) be the two rank-three real
representation bundles just described. On \(S^3_q\), (ET.1)
is the equivariant bundle isomorphism
\[
 \operatorname{Ad}_{q^{-1}}:
        V_{\rm old}|_{S^3_q}\longrightarrow
        V_{\rm new}|_{S^3_q}.
\]
It defines the relative new-minus-old characteristic class in
\(H^4_{S^1}(D^4_q,S^3_q;\mathbb Z)\). Let \(U\) be the Thom
generator fixed by the orientation \((1,i,j,k)\); its restriction
to the zero section is \(rs\,u^2\). This relative group is
\(\mathbb ZU\), directly from the oriented four-disc Thom
construction over \(BS^1\).

For \(rs\ne0\), restriction to the zero section is injective in
degree four. Equation (ET.2) therefore proves that the relative
class is exactly
\[
                               -4U.                 \tag{ET.3}
\]
The coefficient is the same when \(rs=0\). To fix it without
dividing by the zero Euler class, forget the circle and double
the four-disc. Put the new bundle on the positively oriented
disc and the old bundle on the oppositely oriented disc. The
left-to-right clutch is the inverse of (ET.1), namely
\(\operatorname{Ad}_q\). In the northern frame on an equatorial
collar directed north to south, use
\(A_\theta=\theta q^{-1}dq\). At the southern end this transforms
to the zero connection in the southern frame. The collar
orientation is \(d\theta\wedge[S^3_q]\). With
\(\omega=q^{-1}dq\), its curvature is
\(d\theta\,\omega+(\theta^2-\theta)\omega^2\).
Therefore
\[
 \frac1{8\pi^2}\int\operatorname{tr}(F^2)
 =\frac1{8\pi^2}
   \left(2\int_0^1(\theta^2-\theta)d\theta\right)
   \left(-24\pi^2\right)=1 .
\]
The adjoint Pontryagin number is \(-4\).
Thus its ordinary relative Thom coefficient is \(-4\),
and the equivariant generator restricts to the ordinary one.
This proves (ET.3) in all cases.

The next required map for the actual family is not a point-weight
restriction: it is the pullback of this relative bundle pair
along the doubled four-cycle used to read the selected edge's
integer \(n\). In the K23 marking that cycle has Pontryagin
pairing \(4n\), after the variation \(m+n\) has been removed by
the actual extending \(L\) map. The three cusp double curves
give three choices of this marked cycle. Neither (ET.2) nor
(ET.3) identifies their integral pullbacks with each other.
In particular \(rs=0\) leaves an ordinary nonzero Thom class
although its equivariant zero-section restriction vanishes.
Both independent relative coordinates \(m,n\), including the
original \(k\), remain in the cross-edge calculation.

The polynomial identities, orientation convention and coefficient
are retained in code/part3_fourfold/equivariant_flop_thom.py and
its exact JSON output. No further fan return class is assigned
by this local calculation.
