# Actual regular-place torus germ: a central Hopf insertion

Owner: limits_ab. 15November2026,18:29UTC. **Working proof for reserved B.4.15; not yet integrated or entered in the result registry.** This construction preserves the actual punctured local family at a regular point of the elliptic base. It does not repair the global component-cover obstruction B.3.1. In particular it is not a completed S6 filling.

## Precise proposed statement

Choose a small simply connected disc Δ_z centred at a regular point q0 of the elliptic base, avoiding its three special values. After the already specified cover w=r^6, let X→Δ_z×Δ_r be its standard twelve-cycle rank-one semistable model. Its restriction over r≠0 is the prescribed local family of two-tori, including the actual affine family after its local holomorphic origin is chosen.

There is another proper model X_new→Δ_z×Δ_r, isomorphic to X away from the base point (z,r)=(0,0), with smooth total fourfold and reduced normal-crossings divisor r=0. The composite map to Δ_r is flat. The map to the bidisc is deliberately not asserted flat: its fibre over (0,0) contains new compact threefold components.

Each of its twelve new vertical normalization components is either a P1-bundle over one scalar Hopf surface or the blow-up of that P1-bundle along two disjoint elliptic curves. In particular every new vertical normalization has b1=1 and fails the ddbar lemma. The generic punctured two-tori are exactly those of X, so generic simplicity is preserved. Thus generic simplicity does not exclude such non-ddbar components in a two-parameter local degeneration. This does not assert an analogous result for a one-parameter degeneration of compact surfaces.

## 1. Actual translation group and its cocharacter

On the chosen disc write the fixed rank-three period subsystem as

u(z)=(τ(z),μ(z)), w=(1,0), δ=(0,1).

Its quotient

G_z=C²/(Z u(z)+Z w+Z δ)

is the semiabelian complex Lie group extending the elliptic curve E_z=C/(Z+τ(z)Z) by C*_δ. In multiplicative coordinates it is the punctured degree-zero line bundle determined by the actual period μ. No product splitting and no torsion assumption on that line is made.

The map

χ_z:C*→G_z,  χ_z(t)=[u(z) Log(t)/(2πi)]

is single-valued: changing the logarithm adds the actual lattice period u(z). It varies holomorphically with z. The r-monodromy fixes u, so no r-branch ambiguity occurs. Its projection to E_z is [τ(z)Log(t)/(2πi)]. The map into a generic compact two-torus may have nonclosed image; no closed elliptic subgroup is used.

The group G acts on the whole standard rank-one twelve-cycle model. To verify rather than assume this, each normalization component is the equivariant compactification

R_z=G_z×^(C*_δ)P1=P_Ez(O⊕L_z).

Translation in G preserves its zero and infinity sections. The smoothing glues adjacent line directions by their natural dual pairing, with local equation xy=r. The closing translation is a chosen element of G over 6P multiplied by the scalar r^12; all G translations commute with it. Hence the action descends to the generic quotient and extends to all twelve components and their plumbing charts. On a node chart it preserves the two branches; a defining function x of either branch is carried to a holomorphic unit times x, with the elliptic coordinate translated. This is the same semiabelian construction already used in B.1; no elliptic-product model is substituted.

The local actual affine family can be compared with its Jacobian before making this construction. Over Δ_z×Δ_r*, the lattice local system has cohomological dimension one and H²=0. The relative Lie sheaf is coherent and the base is Stein, so the exponential sequence and CartanB give H¹ of the torus-section sheaf equal to zero. Thus the actual affine torsor admits a holomorphic section on this local punctured base. Choosing it gives the required holomorphic comparison. This is only a punctured local comparison; it is not asserted to extend over r=0.

## 2. Blow up the base and resolve the actual node equations

Let β:B~→Δ_z×Δ_r be the blow-up at (0,0), with exceptional curve F≅P1. Pull back X. Near a double curve of the twelve-cycle, the only new singularity occurs in the chart r=zs and has equation

xy=zs.

There is one further smooth elliptic coordinate, suppressed in this display. Label the twelve original central components cyclically by i mod12. At every node choose x=0 to be its even-indexed branch. Blow up the ideal (x,z). Globally this is the sum of the pulled-back invertible ideal of that central component and the invertible ideal O_B~(−F). It is G-invariant because G preserves the component and acts over the base. Distinct even components give disjoint non-Cartier loci, so the six small resolutions are compatible.

The two charts are

z=xQ, y=Qs, r=xQs,

and

x=zX, s=Xy, r=zXy.

They are smooth and make r a product of three distinct coordinates. On the other base chart z=rζ, the pulled-back equation is xy=r and the same ideal is (x,r)=(x), so no modification occurs there. Away from the node loci the ideal is likewise invertible. Consequently the resulting total fourfold is smooth and r=0 is reduced normal crossings, including at F∩strict(r=0).

For later identification retain the component chart calculation. Before the small resolution, the four branches over r=0 are

V_x={x=z=0}, V_y={y=z=0}, H_x={x=s=0}, H_y={y=s=0}.

Here V denotes vertical over F and H denotes the strict horizontal branch. In the resolution, V_x is the blow-up of its former normalization at the elliptic curve over y=s=0; V_y is unchanged. H_y is the corresponding curve blow-up, and H_x is unchanged. This follows explicitly from (Q,s)→(y=Qs,s) and (X,y)→(y,s=Xy) on V_x; these are the two blow-up charts of (y,s). The same calculation applies at both neighbours of each even component.

Therefore vertical even components undergo two disjoint elliptic-curve blow-ups; vertical odd components undergo none. Horizontal odd components undergo the corresponding two curve blow-ups, and horizontal even components undergo none. This is an identification, not an inference from Betti numbers.

## 3. Cartier twisting and its properness

Take the line bundle M=O_B~(F). Choose a local trivializing cover with transition units g_ij. Glue the resolved pulled-back models over that cover by the automorphisms χ_z(g_ij). They satisfy the cocycle identity because χ_z is a group homomorphism. This is Fujimoto's Definition1.1 Cartier-logarithm construction, applied to an actual analytic semiabelian translation action; the displayed formulas prove its applicability here without requiring his principal-elliptic hypothesis.

The action lifts to the small resolutions because each ideal used above is invariant. Alternatively one can twist first and then blow up the descended ideals; the results agree. The glued analytic space is Hausdorff: over every base chart it is the original Hausdorff proper model, while points over distinct base points are separated in the base. Properness is local on the target and therefore follows from properness of the resolved pullbacks. Composition with the proper base blow-up makes X_new→Δ_z×Δ_r proper.

The canonical divisor section of O(F) is nonvanishing on B~\F and trivializes the twist there. Together with the isomorphism β off (0,0), it gives a specified holomorphic identification with the original model on the complement of that point, including every r≠0 fibre. The local action is needed only near F; the same trivialization allows this operation to be inserted into any larger model already standard at q0, without extending u around the special points of the elliptic base.

All charts still have r as a product of distinct coordinates, so r=0 is reduced SNC. The map to the r-disc is flat: the smooth local rings are torsion-free modules over the one-dimensional regular local base, equivalently r is a nonzero divisor. Properness over the r-disc itself follows only when this local replacement is inserted into a model whose q-base is compact. Locally we assert properness over the bidisc, as in the statement.

## 4. Identify the new compact components

Before the small resolutions, the normalization of the preimage of F consists of twelve copies of R_(q0)×F. After twisting, each becomes

V_i^0=O_P1(−1)^××^(C*)R_(q0),

because O(F)|F=O_P1(−1). The structure homomorphism is χ_(q0). Passing to the elliptic quotient gives a principal E_(q0)-bundle H→P1 whose Chern cycle is primitive ±u.

This surface is explicitly a scalar Hopf surface. Put τ0=τ(q0), η=−1/τ0 and a'=exp(2πiη), so |a'|<1. After dividing the elliptic additive coordinate by τ0, the projection of χ is [Log(t)/(2πi)] in C/(Z+ηZ). Its kernel is (a')^Z. Hence

H=O_P1(−1)^×/(a')^Z=(C²\{0})/〈a'·id〉.

The principal G-bundle O(−1)^××^(C*)G maps to H with fibre C*_δ. Associated compactification of this C* fibre by P1 shows that V_i^0 is an actual P1-bundle over H, with two global conductor sections. It can equivalently be written P_H(O⊕M_H) for the line bundle determined by that principal C* bundle. Its restriction to each elliptic fibre of H retains the original nontrivial degree-zero semiabelian line L_(q0).

The two conductor sections intersect the fibre over the distinguished point F∩strict(r=0) in two disjoint elliptic curves. By the charts in §2, the final vertical even components are exactly the blow-ups of V_i^0 along those two curves; the final odd components equal V_i^0. Since π1(P1)=0, each V_i^0 has π1(H)=Z. Blowing up smooth curves in a smooth threefold preserves π1 by the already proved modification argument, so every final vertical normalization has b1=1. A compact ddbar manifold has even b1; these components therefore fail ddbar.

All translations used in twisting preserve the twelve component labels. Thus this construction leaves the rotations +4,−3,0 of the original attempted global assembly unchanged. It does not solve B.3.1 and cannot be inserted as an unexplained correction there. Its positive result is a fully specified local replacement of the actual regular-place punctured torus germ with non-ddbar central components, even when those punctured tori are generically simple.

## Verification still requested

Independent referee should check the global G action on the rank-one plumbing (especially the closing translation), the local affine-Jacobian comparison over Δ×Δ*, and the component chart identifications above. No new primary theorem beyond the already opened semiabelian construction, CartanB and Fujimoto's explicit cocycle is being imported. Exact chart and primitive-Chern calculations will be saved separately.
