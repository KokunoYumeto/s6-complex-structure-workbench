# E.2.21 working proof: global identification of a one-sided smooth completion

Owner: classification_e. This is a full working argument for review, not an integrated result or an arbitrary-chain conclusion. It assumes the actual cusp identification E.2.20 once that source has been finalized and refereed.

## Proposed exact statement

Let pi: Xcal -> Delta be a proper holomorphic submersion with fibres diffeomorphic to S6, and suppose every noncentral fibre is a member of the fixed coprime pair (3k,4l) in E.2.1. Then its central fibre is a member of that same pair. Its normalized isomorphism parameter is the interior value z(0) proved in E.2.7. After choosing a logarithm c(s), the actual family is locally over the parameter disc isomorphic to the prescribed family at c(s), up to the connected translation automorphisms already computed in E.1.

The last family assertion can be omitted if only the central identification is required. It must be justified by the parameter-dependent version of the same cocycle solution, not by pointwise isomorphisms alone.

## 1. What is already known about the actual completion

E.2.10 extends the intrinsic pencil to a proper flat map g: Xcal -> P1 x Delta. E.2.7 supplies a holomorphic interior nonzero parameter z(s); a logarithm on the disc gives c(s). E.2.12 excludes additional critical values, and E.2.14--15 exclude target collapse. The three labelled sections therefore extend distinctly and are sent to 0,1,infinity by a holomorphic PGL2 normalization on the whole parameter disc.

On the ordinary locus, the actual marked torus Jacobian is the one with period matrix Pi_(c(s))(t). This is equality of holomorphic period subbundles with their integral markings: it holds for s nonzero by the given family comparison, and extends to s=0 by the identity theorem. Translation automorphisms of a fixed marked member act trivially on H1, as proved in E.1. Consequently the local choices introduce no additional homology return. The identity monodromy around s=0 also follows from the actual smooth family at any fixed ordinary t.

E.2.13 gives the actual normalized finite root covers, of degrees 3k and 4l. They are smooth proper torus families, with the same marked Jacobians and free deck actions. E.2.16--19 give the actual relative normal-crossing cusp, normalized toric pair, and marked torus action. E.2.20 then identifies the actual cusp neighbourhood with the prescribed Mumford neighbourhood over the full (q,s) bidisc, including its period multipliers.

## 2. The finite affine data really persist

Choose local holomorphic origins on the smooth finite root torus families. A deck map is affine on each compact torus fibre. Its linear part is the fixed marked finite monodromy; subtracting this linear part leaves a holomorphic translation section. Over a simply connected small root-parameter chart, lift that translation to the Lie bundle. The finite-order power relation has the form that the sum of its successive linear translates is an integral period. This integral vector is locally constant in s, because both the lifted translations and the period map are continuous and the lattice is discrete. Changing the lift changes that vector by exactly the integral coboundary already allowed in E.1.

Thus the actual finite deck cocycle has the same integral class at s=0 as for s nonzero. Its varying holomorphic part is removed by the explicit finite averaging used in E.1: the difference of two cocycles with identical lattice class is a cocycle in the complex vector sheaf, and multiplication by the finite group order is invertible there. This produces holomorphic local comparisons in the finite root charts. No assertion that a smooth reduced finite fibre is itself a torus is needed; it is the free finite quotient of the root torus.

One may work with a finite cover of the root disc and its deck translates rather than impose a global origin. The same averaging solves the resulting equivariant comparison. All terms depend holomorphically on s, so the solution does as well.

## 3. Integral collar data and the global affine comparison

Choose a finite cover of the t-sphere by the two finite-root neighbourhoods, the cusp neighbourhood, and ordinary simply connected charts, with fixed annular collars. Choose local holomorphic origins on ordinary torus charts. On overlaps, every comparison is fibrewise affine, because every biholomorphism of compact complex tori is affine. The common integral marking makes the linear parts the prescribed ones, so the remaining maps are translation sections.

Lift these translation sections on simply connected refinements of the collars to the corresponding Lie bundles. Their differences on deck translates, and the sums on triple overlaps, are integral periods. Each resulting integral vector is constant in the parameter s. This statement uses fixed finite collars away from the singular centres, where the actual and reference torus families are smooth; no logarithm is evaluated at a singular point.

For s nonzero the family is a prescribed member, so these integral classes are exactly the classes of its logarithmic-transform data, modulo the changes of origins already allowed in E.1. The same is true at s=0. Equivalently, one can normalize the discrete classes once over the connected parameter disc; their local constancy prevents a new central class. This includes the cusp winding class. The cusp chart comparison in E.2.20 has the actual marked period action, so no unaccounted translation or fan change enters there.

After this discrete normalization, the remaining comparison is the additive holomorphic cocycle in the extension sheaf V used in E.1. Its root extension conditions are those of the already identified finite root charts, and its cusp extension condition is the actual toric collar condition, now supplied by E.2.20. In particular it fits the exact sequence

`0 -> O_(P1) delta -> V -> O_(P1)(-infinity) -> 0`.

Both end sheaves have vanishing first cohomology. E.1 gives the explicit analytic solution, by finite averaging and splitting the collar Laurent series into the two convergent parts. This kills the remaining cocycle and glues the local comparisons to a biholomorphism of the actual central threefold with the prescribed member at c(0).

For a family comparison, perform precisely the same splitting with coefficients holomorphic in s on a fixed finite collar cover. Cauchy coefficient formulas preserve holomorphic dependence, and the finite averaging is holomorphic in s. The resulting comparisons therefore glue over a smaller parameter disc. Their ambiguity is the connected scalar translation group from E.1; this does not change the central isomorphism class.

## 4. What this does not yet imply

The known-pair locus is open by E.2.2 and is stable under full punctured-disc smooth specializations by the proposed statement. Those two facts alone do not prove that it is topologically closed in an arbitrary reduced analytic base. An arbitrary open set can have a real boundary through which no holomorphic disc has its entire punctured image in that open set. Analytic curve selection is unavailable until the known locus has a suitable analytic or constructible description.

The following separate propagation route is under investigation. On any smooth disc carrying a smooth family and containing a nonempty known open set, the unique fractional canonical root L exists on the whole total space because H1 and H2 with integer coefficients vanish. Its direct image is a free rank-two sheaf, since rank two holds on that nonempty open set. The evaluation base locus is a closed analytic subset of the proper total space, so its image is a closed analytic subset of the disc. It misses the known open set and is therefore discrete. Thus the actual relative pencil exists off a discrete analytic set, without first assuming the whole punctured disc consists of known members.

The critical image, finite root covers, cusp normalization and conductor must then be controlled by finitely many proper analytic exceptional sets. If this yields the original local charts off a discrete set, the ordinary holomorphic periods can be continued from the known open set and the above global comparison would identify the generic disc fibres. Full punctured-disc closure would then fill the remaining isolated points. This generic propagation step is not asserted here until its finite normalization/conductor argument is written and reviewed. In particular E.2.4 remains Open while it is missing.
