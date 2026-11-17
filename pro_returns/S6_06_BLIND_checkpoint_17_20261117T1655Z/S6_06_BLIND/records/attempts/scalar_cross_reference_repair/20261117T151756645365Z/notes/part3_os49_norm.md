# P3F.30. The exact OS49 norm quotient and its two normal charges

**Proved.** The OS49 component line admits the norm modification
\[
 N=M\otimes T^*M=M^{\otimes2}(-C_0),
 \qquad T^*N=N(-F).                                  \tag{P3F.30.1}
\]
The actual morphism \(\phi:T^*M\to M\) induces
\(\phi\otimes T^*\phi:T^*N\to N\), with divisor \(F\).
On the ordinary locus the quadratic map to this norm construction
is the quotient by the order-two subgroup of the delta circle.
Its completion is the actual analytic quotient \(X/\mu_2\).
This quotient has a transverse \(A_1\) singularity along the fixed
curve \(F_{\mathrm{fix}}\). Its minimal resolution has two fixed
sections over that curve. Their normal weight decompositions are
\[
 \bigl(\mathcal O(-2)_{-1},\mathcal O(0)_{+1}\bigr),
 \qquad
 \bigl(\mathcal O(0)_{-1},\mathcal O(-2)_{+1}\bigr).
                                                               \tag{P3F.30.2}
\]
After conjugating the negative-weight line, the two determinant
degrees are respectively \(+2\) and \(-2\). Thus the two
Hopf-line base shifts are \(+1\) and \(-1\), in the same
circle convention. These charges are part of this exact quotient
and resolution; no return-index equality is inferred by discarding
them.

**Proof: the morphism on the ordinary locus.** Tensor the exact
line identities of P3F.28. Since \(T\) interchanges \(C_0,C_1\),
the two successive zero divisors add to \(F=C_0+C_1\), giving
(P3F.30.1). In local frames write \(\phi_p\) as multiplication
by \(f(p)\). Away from its zero divisor the precise quadratic
map is
\[
 M_p\longrightarrow N_p=M_p\otimes M_{Tp},
 \qquad v\longmapsto v\otimes\phi_p^{-1}(v).
                                                               \tag{P3F.30.3}
\]
It has kernel \(\{1,-1\}\) on the nonzero fibre. A scalar
\(\lambda\phi\) in the original suspension gives scalar
\(\lambda^2(\phi\otimes T^*\phi)\) in the norm suspension.
Compatibility is the explicit identity
\[
 \frac{(\lambda f(p)v)^2}{f(p)}
 =\lambda^2 f(p)f(Tp)\frac{v^2}{f(Tp)}.
\]
Consequently (P3F.30.3) descends to the specified quotient of
the ordinary torus family, with its actual scalar parameter.

There is also an exact Tate-chart description. In the source
period marking of P3F.26 the change
\[
                        W=V^2/Z
\]
puts the norm line into its degree-zero extension on both
\(I_2\) components. Multiplication of this frame by a nonzero
base monomial merely changes the chosen integral toric origin.
The period valuations change by the integral matrix
\((\begin{smallmatrix}1&0\\-1&2\end{smallmatrix})\):
\[
 (2,1)\longmapsto(2,0),\qquad
 (-3,-1)\longmapsto(-3,1).
\]
The scalar becomes \(\lambda^2\). These are the periods of
the whole-fibre linearization of \(N\). The matrix has
determinant two, exactly the degree of (P3F.30.3). It maps the
unimodular source fan to the quotient fan in the larger target
lattice. The affine invariant rings of those cones are precisely
the order-two invariant rings, so the toric map extends to the
analytic quotient. At the other source fibres the original delta
action is free, and the quotient is its usual unramified local
quotient. Thus these chart maps glue to \(X\to X/\mu_2\),
not merely to a comparison of valuation matrices.

**Proof: resolution and the retained charges.** At the actual
fixed curve the normal coordinates \((a,b)\) lie in
\(L_-\oplus L_+\), where both line bundles are
\(\mathcal O_{\mathbb P^1}(-1)\), and delta acts with weights
\((-1,+1)\). The order-two invariant coordinates are
\[
 x=a^2,\qquad z=ab,\qquad y=b^2,
 \qquad xy=z^2.
\]
They give exactly the transverse \(A_1\) equation, with the
fixed curve as its singular locus. The two charts of its minimal
resolution are
\[
 (x,\zeta):\quad z=x\zeta,\quad y=x\zeta^2;
 \qquad
 (y,\eta):\quad z=y\eta,\quad x=y\eta^2,
 \quad\eta=\zeta^{-1}.
\]
They glue over the original fixed curve by its line-bundle
transitions. In the first chart,
\(x\) is a coordinate in \(L_-^{\otimes2}\) and
\(\zeta\) in \(L_+\otimes L_-^{-1}\). In the second,
\(y\) lies in \(L_+^{\otimes2}\) and
\(\eta\) in \(L_-\otimes L_+^{-1}\). The residual circle
coordinate is \(\tau=\delta^2\), and its two chart actions are
\[
 (x,\zeta)\longmapsto(\tau^{-1}x,\tau\zeta),
 \qquad
 (y,\eta)\longmapsto(\tau y,\tau^{-1}\eta).
\]
Their two fixed sections are \(x=\zeta=0\) and
\(y=\eta=0\). The stated bundle transitions and weights prove
(P3F.30.2). They also show that the exceptional ruled surface is
\(\mathbb P(L_-\oplus L_+)\cong\mathbb P^1\times\mathbb P^1\).
All maps are defined over the parameter and commute with its
actual closing identifications, so the quotient and resolution
are family morphisms.

Conjugating the negative-weight line makes the circle representation
positive on both summands. The first resulting bundle is
\(\mathcal O(2)\oplus\mathcal O\), and the second is
\(\mathcal O\oplus\mathcal O(-2)\). Factoring out respectively
\(\mathcal O(1)\) and \(\mathcal O(-1)\) leaves
\(\mathcal O(1)\oplus\mathcal O(-1)\), a topologically trivial
\(SU(2)\) bundle on the sphere. The factored line is precisely
the additional base factor in the associated Hopf line. Its
degrees are \(+1\) and \(-1\). In particular an index
comparison through this actual norm quotient must retain both
opposite base factors. This norm-quotient route does not yet
identify its total correction with the mixed-circle trace of
P3F.27. The actual zero return for both diagonal fillings is
proved separately by P3F.31--32 and P3K.17. **End of proof.**
