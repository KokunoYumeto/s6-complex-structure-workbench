# P1.4: complete receiving-proof comparison

## Chronology

The fresh derivation and forty-assertion exact certificate were frozen before the receiving proof was requested. The final pre-release freeze is 2026-11-20T00:39:09.842972+00:00, with proof SHA256

`f35dfe1d632983bcba98dc233b7870eb36d1e35d73d529ace2da35516482b71d`.

An earlier receipt at 00:38:50 is retained. Before requesting the receiving proof, one missing TeX backslash was restored in the displayed double-cover algebra; the final receipt records that formatting-only change and both hashes.

The parent released the complete three-step receiving proof at 2026-11-20T00:39:54.914259+00:00 as `audit_root/packets/P14_receiving_proof_08.tex`, SHA256

`ce73fd3c7e7c01583b0770a884ba23b7b059e3fb11fa04cc2d09ef8ee091ac59`.

All three steps have now been read and compared. The expected statement was already exposed in the isolated packet; the receiving proof, previous P1.4 producer, and previous check records were not exposed before the freeze. No earlier P1.4 producer was imported, and no earlier P1.4 producer or output was needed for this comparison. The canonical row was read only after the complete proof comparison, to prepare an exact proposal without modifying it.

## Step 1: discriminant, ordinary node, and compactification

The receiving discriminant agrees exactly with the fresh calculation:

\[
\operatorname{disc}_x(x^5+\lambda^3x+\lambda^4)
=\lambda^{15}(3125\lambda+256).
\]

At `lambda_*=-256/3125`, the repeated root is `r=64/625`. The frozen proof gives the full factorization

\[
(x-r)^2(x^3+2rx^2+3r^2x+4r^3),
\]

with cubic discriminant `-200r^6` and value `10r^3` at `r`. Both are nonzero. The receiving assertions of exact multiplicity two and simplicity of the other roots therefore have complete exact checks. The transverse parameter derivative is `lambda_*^3/4`, also nonzero.

The frozen reciprocal chart is `v^2=u+lambda^3u^5+lambda^4u^6`; its `u` derivative at the point over infinity is one. Thus the compactification adds no other singularity. The explicit local factorization into two smooth transverse branches proves the ordinary node. Its normalization is the smooth cubic double cover `z^2=q(x)`, of genus one. This covers every assertion of receiving step 1.

## Step 2: root charts, full deck maps, and minimality

The receiving variable `u` is the frozen variable `t`; there is no change of base orientation or ramification convention. The complete coordinate maps are:

| chart | original coordinates | good equation | full deck map |
|:---|:---|:---|:---|
| zero | `lambda=t^8`, `x=t^6X`, `y=t^15Y` | `Y^2=X^5+X+t^2` | `(X,Y,t)->(zeta_8^2 X,zeta_8 Y,zeta_8 t)` |
| infinity | `lambda=t^-5`, `x=t^-4X`, `y=t^-10Y` | `Y^2=X^5+tX+1` | `(X,Y,t)->(zeta_5^4 X,Y,zeta_5 t)` |

Thus the receiving `i` is `zeta_8^2`, and its `zeta_5^-1` is `zeta_5^4`. Both compact root families are smooth, including the point over infinity, by the explicit two-chart Jacobian checks.

The two Hodge characters are exactly

\[
(\zeta_8,\zeta_8^3),\qquad
(\zeta_5^4,\zeta_5^3)
=(\zeta_5^{-1},\zeta_5^{-2}).
\]

Together with their conjugates these are all primitive eighth roots in the first case and all nonidentity fifth roots in the second. Consequently the receiving characteristic polynomials are precisely

\[
T^4+1,\qquad T^4+T^3+T^2+T+1.
\]

The frozen proof supplies the geometric bridge compressed in the receiving phrase “proving minimality”: an equivariant radial trivialization of the proper smooth root family identifies the original peripheral monodromy with the inverse central deck action. The actual monodromy therefore has exact order eight or five. A ramification of order `m` takes its `m`th power, while good reduction supplies trivial monodromy on the full disk. This gives `8|m` and `5|m`; the displayed root families realize those minima. The inverse convention does not alter either characteristic polynomial or order.

The receiving fourth-power assertion at zero is exact. The map fixes `X` and sends `Y` to `-Y`; it negates both holomorphic differentials and their conjugates. Hence it acts as `-I` on complex first cohomology and therefore on integral first cohomology, whose inclusion into its complexification is injective. Its exterior-square action is the actual map `(-I) wedge (-I)=I`.

## Step 3: canonical nodal extension and exact line isomorphisms

The receiving proof explicitly uses the **dualizing Hodge extension** at the nodal parameter. This agrees with the canonical object constructed in the frozen derivation: the pushforward of the relative dualizing line of the stable family on the root orbifold.

That scope is essential and is fully accounted for. On the ordinary chart `P^1\{0,infinity}`, including the node, the residue transition

\[
\frac{dx}{2y}=-u\frac{du}{2v}
\]

identifies the relative dualizing line with the pullback of `O(1)`. The finite double-cover algebra is `O direct-sum O(-3)`, so its dualizing pushforward to the projective `x`-line is `O(1) direct-sum O(-2)`. Taking sections gives the actual base frame

\[
dx/y,\qquad x\,dx/y
\]

over this whole ordinary chart. This direct calculation also establishes local freeness at the node.

The receiving residue argument matches the explicit normalization maps:

\[
\omega_1=\frac{dx}{(x-r)z},\qquad
\omega_2-r\omega_1=\frac{dx}{z}.
\]

The first has opposite nonzero residues at the two branches; the second is the nonzero regular elliptic differential. They are independent dualizing sections. Thus neither an extra base divisor nor an unspecified modification at `lambda_*` enters the line calculation.

The exact root-chart form transitions are

\[
(\omega_1,\omega_2)
=(t^{-9}\alpha_0,t^{-3}\beta_0)
=(t^6\alpha_\infty,t^2\beta_\infty),
\]

with each equality used on its respective overlap. Their divisors are therefore exactly the two receiving divisors. For

\[
T=\mathcal O\bigl((2/5)[\infty]-(3/8)[0]\bigr),
\]

the frozen proof constructs actual equivariant isomorphisms `T -> L_2` and `T^3 -> L_1`. The local frames of `T` are `t^3` and `t^-2`, sent to `beta_0` and `beta_infinity`; the local frames of its cube are `t^9` and `t^-6`, sent to `alpha_0` and `alpha_infinity`. Their deck characters agree, and the inverse maps use the coefficients in the displayed Hodge frames. This proves the direct sum `H=T^3 direct-sum T` and the identification of the `dx/y` line, in addition to the equality of divisor classes.

The degree calculation is `2/5-3/8=1/40`. There is no residual geometric or integral-marking obligation comparable to the separate P1.19 issue: every map needed here is the explicit coordinate scaling, residue transition, or equivariant line-frame map above.

## Assessment and integration scope

All three receiving proof steps pass the complete comparison. The root-chart and line-bundle conventions agree exactly. The canonical extension across the nodal fibre is explicitly present in the receiving proof and is independently constructed before receiving exposure in the frozen derivation. No additional mathematical source guard is required for this target.

The fresh route fills the previously documented absence of a complete written derivation before receiving all current proof steps. Its scope is precisely the literal isolated pencil, the stated root orbifold, and the canonical relative-dualizing Hodge bundle. It does not claim that the expected answer was unknown or that the model family differs from the parent.

The shared row remains untouched. Final completion awaits the root's verification of the current source snapshot and actual current P1.4 page QA. Earlier build28 layout evidence remains an earlier snapshot until the root supplies that current evidence.
