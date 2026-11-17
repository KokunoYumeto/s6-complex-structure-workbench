SUPERSEDED WORKING ATTEMPT. Section2 incorrectly identified a marked suspension period with a toric cocharacter. The corrected proof retains the actual fan and changes the generating period only; see notes/part3_expanding_action_comparison.md. No numbered result used this attempt.

# Exact inverse-action comparison for the expanding sector

Working proof for independent audit; proposed statement P3F.50.
The source data are exactly the fixed marked data of E26 Remark 8.5
on a rational elliptic surface with Mordell--Weil group \(\mathbb Z\).
This statement supplies the comparison for the large-scalar expanding
case as well as the small-scalar contracting case. Every parameter
circle below is specified in its own coordinate.

Let \(\pi:S\to\mathbb P^1\) be the marked source, let \(M\) be its
actual line, and put \(S^\circ=S\setminus\pi^{-1}E\). Write
\(B_\lambda=\lambda B_0\) for the expanding automorphism of
\(M^{\times}|_{S^\circ}\), where \(B_0\) covers a translation \(t\).
The zero/pole assertion in the remark means that its actual
meromorphic line map has poles along the whole inverse image of
the effective base divisor \(E\). Define
\[
 \mu=\lambda^{-1},\qquad
 B^\vee_\mu=B_\lambda^{-1}=\mu B_0^{-1}.
 \tag{EX.1}
\]
The inverse covers \(t^{-1}\). Since \(t\) is over the source base,
the divisor of \(B_0^{-1}\) is the whole zero divisor \(\pi^{-1}E\).
It is the contracting case of the same construction. The inverse
formula is an identity of holomorphic automorphisms on the indicated
line complement, and a meromorphic line-map identity on the source.

## 1. The family quotient and every finite cap

For every permitted scalar and every point of the line complement,
\[
 \langle B_\lambda\rangle=\langle B^\vee_{\lambda^{-1}}\rangle.
 \tag{EX.2}
\]
Consequently
\[
 (\lambda,[v])\longmapsto(\lambda^{-1},[v])
 \tag{EX.3}
\]
is a biholomorphism from the expanding quotient family over
\(\{|\lambda|>R\}\) to the pullback of the contracting quotient
family over \(\{0<|\mu|<R^{-1}\}\). Its inverse has the identical
coordinate formula. It preserves the actual associated line
circle and every marked source base point.

Retain an actual cap on the source root \(q=z^m\), with commuting
line maps \(A_\lambda,B_\lambda\) satisfying
\[
 A_\lambda^m=B_\lambda^n,\qquad \gcd(m,n)=1.
\]
Set \(A^\vee_\mu=A_{\mu^{-1}}\), \(n^\vee=-n\). Then, as literal
maps of the same root line,
\[
 (A^\vee_\mu)^m=(B^\vee_\mu)^{n^\vee},\qquad
 \langle A^\vee_\mu,B^\vee_\mu\rangle
       =\langle A_{\mu^{-1}},B_{\mu^{-1}}\rangle.
 \tag{EX.4}
\]
The root source, its resolved components, its line, all finite
characters, and its divisor comparison diagrams are unchanged by
this identity. It gives inverse holomorphic maps on the cap
quotients and the same map on their outer collars. In particular
it retains their full nonreduced fibre structure and their
integral boundary maps.

In the actual outward-period convention
\(\gamma_{\rm out}=B_\lambda^{-1}\), the new outward period is
\[
 \gamma_{\rm out}^\vee=(B^\vee_\mu)^{-1}
             =B_\lambda=-\gamma_{\rm out}
\]
in the additive integral period notation. The source meridian
\(\alpha\) and the positive line circle \(\delta\) are retained.
Thus the marked killed meridian has the exact expression
\[
 m\alpha+n\gamma_{\rm out}
       =m\alpha+n^\vee\gamma_{\rm out}^\vee.
 \tag{EX.5}
\]
The identity also retains the signed norm at an order-one site.
For a fixed base framing
\(\sum\alpha_i+b_0\gamma_{\rm out}=0\), its new coefficient is
\(b_0^\vee=-b_0\). Hence each effective signed determinant changes
sign. Its absolute value, every effective order, and every
primitivity condition are preserved by the displayed maps.

## 2. The exact extension across the Mumford charts

Use the two-dimensional marked lattice with coordinates
\((\gamma_{\rm out},\delta)\). Replacing its first marked basis
vector by its negative gives the integral isomorphism
\[
 U=\begin{pmatrix}-1&0\\0&1\end{pmatrix}.
 \tag{EX.6}
\]
For an expanding periodic fan \(\Sigma\), use the contracting fan
\(U\Sigma\), with the period sublattice also carried by \(U\).
On the lattice of the Mumford cones, use
\(\widetilde U(v,h)=(Uv,h)\); the source height \(h\) is fixed.
For every cone \(\sigma\), the actual affine toric chart morphism
is the isomorphism on its semigroup algebra
\[
 \mathbb C[(\widetilde U\sigma)^\vee\cap\widetilde N^\vee]
 \longrightarrow
 \mathbb C[\sigma^\vee\cap\widetilde N^\vee],
 \qquad \chi^a\longmapsto\chi^{\widetilde U^*a}.
 \tag{EX.7}
\]
It fixes the base monomial and commutes with face localization.
It therefore glues to an isomorphism of the full toric charts,
all their strata and overlaps. Carrying the period sublattice
by the same map makes it equivariant for the period action,
so it descends to the actual Mumford quotient. Its inverse is
given by the same matrix. This is the extension of (EX.3)
expressed in the two marked integral bases, with all bounded
line units retained from (EX.1). No complex conjugation is used.

The integral map preserves primitivity and unimodularity of
every cone. It carries every permitted one-vertex fan and every
finite flop diagram to its corresponding fan and diagram.
As a biholomorphism it preserves the complex orientation of the
six-manifold. The negative determinant of its lattice-coordinate
matrix does not change that orientation: every complex linear
Jacobian has positive real determinant \(|\det_{\mathbb C}|^2\).
The fixed line circle \(\delta\) is literally the same action.

For a fan written \(T(v,w)\), the transformed cocharacter
identity is the actual equality
\[
 \delta=a v+b w
 \quad\longmapsto\quad
 U\delta=a\,Uv+b\,Uw.
 \tag{EX.8}
\]
Here \(U\delta=\delta\). Reordering the two transformed basis
vectors to restore a chosen determinant convention exchanges
\(a,b\). Thus the fan integer \(a^2-ab+b^2\) used in the
common-exterior calculation is preserved by the exact lattice
map. This observation is an equality under (EX.8), rather than
an identification of unrelated fan markings.

## 3. The specified parameter arrows and return classes

Fix \(R\) in the expanding range. Its counterclockwise scalar
circle is
\[
 \lambda(\theta)=R e^{2\pi i\theta},\qquad 0\le\theta\le1.
 \tag{EX.9}
\]
Under (EX.3) it is exactly
\(\mu(\theta)=R^{-1}e^{-2\pi i\theta}\), the reverse of the
positive small-\(\mu\) circle. The quotient and cap identities
give a diffeomorphism of the corresponding mapping-torus
families over this actual base-circle map. Hence their endpoint
returns, with initial fibres identified by (EX.3), are inverse
mapping classes. Under the fixed oriented identification
\(\Theta_7=\mathbb Z/28\), this gives
\[
 [\Phi_{\lambda,+}]=-[\Phi_{\mu,+}].
 \tag{EX.10}
\]
The sign follows from the displayed loop map. A positive
meridian of the end \(\lambda=\infty\), defined in its local
coordinate \(\mu=1/\lambda\), instead gives
\([\Phi_{\mu,+}]\) itself.

The individual characteristic numbers and relative group
coordinates use the product framing transported by (EX.3)
and (EX.7). Reversing the parameter cylinder reverses the
mapping-torus circle orientation and the exact relative
return. The characteristic integral and group morphisms
already proved in K23 therefore give
\[
 (k,\ell)_{\lambda,+}=-(k,\ell)_{\mu,+},\qquad
 (m_{\rm rel},n_{\rm rel},s)_{\lambda,+}
       =-(m_{\rm rel},n_{\rm rel},s)_{\mu,+}.
 \tag{EX.11}
\]
These are integral equalities for \(k,\ell,m_{\rm rel},n_{\rm rel}\)
and the stated equality modulo \(28\) for \(s\).
They retain the normal reference frame; no division of a
covered-loop class occurs.

For a root parameter \(\lambda=r^L\), use the exact inverse
root parameter \(r^\vee=r^{-1}\), so
\(\mu=(r^\vee)^L\). Equations (EX.4)--(EX.11) hold on this
same cover. For any shorter descended loop whose original
endpoint map has been proved, (EX.3) carries that endpoint
map as well. This last comparison applies to the proved
endpoint map itself and supplies no unproved descent.

## 4. Generator signs

The contracting source classification may choose the sign of
the marked generator \(G\) so that its coefficients have the
displayed signs. This choice has an exact source map. The
holomorphic elliptic inversion
\(\iota:S\to S\), \(p\mapsto-p\), sends the zero section to
itself, sends \(G\) to \(-G\), and satisfies
\(\iota t_Q\iota^{-1}=t_{-Q}\). Pullback carries the actual
line divisor and every vertical component divisor to their
inverse-image divisors, with the canonical induced map of
line complements. Carry the source roots and the resolution
centres by this same map. It conjugates every source and
line norm diagram and preserves the base and scalar
parameter. This records the comparison used when both
generator coefficients change sign. It introduces no
additional parameter reversal beyond (EX.9).

The proof accounts for both uniform-action alternatives of
the literal construction. The remaining source-model and
shorter-parameter-loop audits are recorded separately.
