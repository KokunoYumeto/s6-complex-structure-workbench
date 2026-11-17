# P4.32: complete zero-Euler classification

Status: Proved from independently audited constituent statements. Exact positive Euler values remain separately unresolved.

```tex
\subsection{Complete zero-Euler classification in the requested classes}

\begin{statement}{P4.32}{Proved}
An irreducible support in Part~4.2 has Euler number zero exactly
in the following cases: it is smooth with a finite unramified
torus cover, or it is singular with smooth minimal elliptic ruled
normalization, or it is singular with smooth minimal Hopf
normalization. In the ruled double-horizontal case the conductor
image is a smooth elliptic curve; the local germs are product
cusps, product tacnodes, or product ordinary plane triple points,
and the reduced conductor maps have degrees one, two, or three
respectively and are unramified.

For a fibration whose supports are all irreducible or normal
crossing, $c_3(Y)=0$ exactly when every irreducible support has
one of these forms and every reducible support has the
zero-Euler normal-crossing form of P4.8.
\end{statement}
\begin{proof}
Normal irreducible supports are smooth with the stated finite
unramified cover by P4.8 and P4.12. For a singular irreducible
support, use its minimal normalization resolution $T$.
P4.26 excludes rational resolutions and class-VII minimal
models with positive second Betti number from equality.
The Inoue minimal model has no conductor curves and is
excluded there as well. A Hopf minimal model is covered
completely by P4.27: equality makes the actual normalization
a smooth minimal Hopf surface, and the converse is P4.24.

It remains to use the positive-genus ruled resolution.
The reduced-horizontal alternatives of P4R.9 already give
smooth minimal elliptic ruled normalization. In the remaining
case the pole support is a section $H$ with rational trees,
and the coefficient of $H$ is two. Its inclusion in $T$
induces an isomorphism on fundamental groups. The conductor
pushout and the curve-group calculation of P4R.7--P4R.9 give
$\pi_1(S)=\pi_1(C)$ and $e(C)\ge0$ for the reduced image
conductor $C$. Equality in
$e(S)=e(S_{\rm reg})+e(C)$ makes $C$ a connected curve
with elliptic normalization and no point-identification
cycles. Every rational pole component is contracted, since
there is no finite nonconstant map from a rational curve
to an elliptic curve. Thus $H$ is the sole strict conductor
component, and every branch of a generic transverse
plane-curve singularity has conductor exponent two.

We enumerate those transverse germs explicitly. For a branch
$B_i$ of a reduced plane curve, its conductor exponent is
\[
 c_i=2\delta(B_i)+\sum_{j\ne i}I(B_i,B_j).
\]
If a branch is singular, $c_i=2$ forces
$\delta(B_i)=1$ and no other branch. The one-gap
parametrization of a delta-one irreducible plane curve
has orders two and three and gives the ordinary cusp.
If all branches are smooth, two branches have intersection
multiplicity two and give a tacnode, or three branches
have all pairwise intersection multiplicities one and
give an ordinary triple point. Four branches would give
each conductor exponent at least three. One smooth branch
is nonsingular and has exponent zero. These exhaust the
possibilities.

P4.29, P4R.11, and P4.31 respectively treat the cusp,
tacnode, and ordinary-triple cases, without assuming that
the initial normalization or image conductor was smooth.
They give the asserted smooth minimal elliptic ruled
normalization and the precise local conductor maps.
The converse for a smooth minimal elliptic ruled
normalization is P4.22. This proves the entire irreducible
zero-Euler classification.

Finally P4.26 expresses $c_3(Y)$ as a finite sum of
nonnegative fibre Euler numbers. Its vanishing is therefore
equivalent to vanishing of every summand. The irreducible
summands have just been classified, and P4.8 gives the
complete reducible normal-crossing zero case. This proves
the final assertion.
\end{proof}
```
