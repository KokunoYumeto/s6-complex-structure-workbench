# Auxiliary torsor plumbing: complete working derivation

Saved 15 November2026 during the 14:30–14:38 checkpoint freeze of AB_push.tex. This is AI-produced working mathematics, with no priority claim. It concerns an auxiliary family, not the actual S6 family.

## Data already constructed

Let C be the smooth projective curve b³=a⁴+1, with unique infinite point o. Its degree12 map toB=P1 is t=b³; its deck generator is σ(a,b)=(ia,ωb). The Jacobian elliptic surface E_C has equationY²=X³−3bX+2a², sole singular fibreI12 ato, χ(O)=1, e=12. LetP=(0,−sqrt2a), a narrow section of height2.

PropositionB.3.6 constructs an everywhere-locally-trivial genus-one torsorπ:V→C and an affine automorphismA:V→V coveringσ, withA¹²=t6P. V is smooth projective and locally isomorphic toE_C, so its only singular fibre is the reducedI12 fibreF_o, with twelve ordinary nodes. No section ofV is selected or asserted.

## The relative-degree-zero line

The Jacobian sectionP lies in the identity component of the relative Picard sheaf, including ato. Thus it defines a relative line-bundle class of degree zero on every irreducible component of every fibre ofV. The obstruction to a global line bundleM representing it lies inBr(C)=0. The precise relative Picard statement is in Cossec–Dolgachev–Liedtke's author manuscript Enriques SurfacesI, Proposition0.9.2 and the opening of§4.2, p.370 (PDFp.385). This primary text was opened on15November2026.

One can also constructM locally on a trivializing cover forV. Translation by a local section acts trivially on the relativePic0 classP, so the local Poincaré lines differ on overlaps only by lines from the base. Their obstruction is aG_m gerbe onC, killed byBr(C)=0. The resultingM has multidegree zero on theI12 fibre. Any ambiguity by a base line does not affectM², becauseM·F=F²=0.

Take a finite multisection coverC'→C which trivializesV generically, resolve the base change and identify its relative minimal model with the Jacobian. The pulled-backM is the narrow Poincaré line for the pulled-backP, up to a base line. Its square is minus the height, namely−2deg(C'/C). Intersection pullback has the same degree factor, soM²=−2. The height base-change formula is Shioda1990, Proposition8.12, equation(8.25), independently opened and checked.

SinceA coversσ andσ fixesP, the lineJ=M⊗(A* M)^−1 has trivial relativePic0 class on every fibre. It has multidegree zero atI12 as well. Fibrewise it is trivial; Grauert base change withh0=1 and the evaluation map therefore giveJ=π*J_C for a lineJ_C onC.

The translation formula is(t6P)*M=M⊗π*D^−1 where degD=⟨P,6P⟩=12. The sign agrees with the original conventionJ=M⊗T*M^−1. It can be checked after the same finite multisection cover: on a Jacobian surface, pullback by translationQ sends the narrow Poincaré classp to p−⟨P,Q⟩F. IteratingA* twelve times consequently gives12degJ_C=12, hence degJ_C=1.

TwistingM byπ*N changesJ_C byN⊗(σ*N)^−1. The endomorphism1−σ* ofPic0(C) is an isogeny: its differential has no invariant vector becauseC/G=P1 and invariant holomorphic one-forms are pullbacks fromP1. It is therefore surjective on complex points. ChooseN so that the newJ_C isO_C(o). This gives an isomorphismM⊗(A*M)^−1≅π*O_C(o) and a holomorphic sectionφ with divisorF_o. This is sufficient line data for compact-core plumbing; it does not identify the resulting family withS6.

## Typed auxiliary family and charts

PutR=P_V(O⊕M), with its zero and infinity sections. Form the pinchingQ_V by identifying s0(x) withs∞(Ax), x∈V. The mapR→B is the compositeR→V→C→B, which is constant on each pair becauset∘σ=t.

For the deformation parameterh (deliberately not identified with the actualr-family), use a core annulus inM and a node neighbourhood overV with coordinatesa∈M_x, b∈M^−1_Ax satisfyinga⊗b=hφ_x. Glue thea collar to(x,a) in the core and theb collar to(Ax,b^−1). The compact-core proof ofA.1.2 applies verbatim becauseV is compact,A is an automorphism, andφ has bounded norm. It gives a Hausdorff proper flat holomorphic mapZ^flat→Δ_h, with central fibreQ_V and a holomorphic mapZ^flat→B. The proof does not requireA to fixC pointwise.

At a smooth point ofF_o choose a base coordinatez_C onC, so the local equation isab=h z_C. At one of its twelve nodes writez_C=uv inV; the fourfold chart isab=h uv. Forh≠0 there is oneODP in each of the twelve node charts, at(a,b,u,v)=0. There are exactly twelve distinctODPs.

This count remains valid ifA rotates theI12 components or its nodes. The node chart is indexed byx inV. Its centrea=b=0 lies in neither annular collar, so the gluing never identifies the centre atx with the centre atAx. The double locus ofQ_V isV itself, notV moduloA. An additional quotient byA would be a separate construction, not part of the collar gluing.

The two compatible prism subdivisions can be made uniformly at these nodes, with the corresponding blow-up ofF_o in one section. Translations and the deck action preserve the orientation of theI12 cycle, so the two global side conventions are compatible. This gives smooth-total-space semistable auxiliary familiesZ^+,Z^-→Δ_h, with the punctured nodal family small-resolved at all twelve nodes. Their normalization is the blow-up ofR alongF_o in the selected section, followed by the twelve indicated small resolutions. The normal product changes fromπ*O_C(o) to the trivial line, exactly as inA.2.2.

## Euler and cusp comparison: why this is notS6

TheI12 fibre has Euler number12: each of its twelve components isP1, adjacent pairs share twelve nodes. Its smooth strata are twelve copies ofC*, each of Euler0. The nearby constructible function of the unmodified pinching is1 onF_o and0 on the rest ofV. The complement of the conductor is aC* bundle and contributes0. Thus e(Z^flat_h)=12 for h≠0. Replacing eachODP point byP1 adds1, givinge(Z^±_h)=24.

Independently,e(R)=2e(V)=24. At each of the twelve nodes, the blow-up plus small resolution replaces a point of the centre by a chain of twoP1s, of Euler3. The openC* parts contribute0. Thereforee(R^±)=24+12(3−1)=48. The central pinching hasEuler48−12=36; its semistable nearby count subtracts the double locus once more, giving36−12=24. This agrees with the node calculation.

Nearo onC, z=a/b is a uniformizer andq_B=1/t=z¹²/c³ withc a unit. Thus q_B has order12 alongF_o. In every generic smooth point of the auxiliaryq-fibre, the local map toB isq_B=(z_C)¹² times a unit. Consequently the cusp fibre ofZ^±_h→B has multiplicity12 for h≠0. At the other two branch values the corresponding multiplicities are3 and4. The prescribedS6 family has a reduced cusp fibre and Euler2. Hence this auxiliary family cannot be the required family, even though it realizes the component-cover and affine-torsor data.

A simple pinching with two disjoint global conductor sections also has a continuous map toS1 inducing a surjection onπ1: choose a continuous functionR→[0,1] taking the values0,1 on the two sections and exponentiate it after gluing. A path joining the sections gives a loop of degree1. This is another reason that an eventualS6 semistable model needs additional cusp geometry; no general topological specialization theorem is asserted here beyond that elementary pinching statement.

## Remaining actual construction

The missing operation must remove the auxiliary multiplicity12 cusp while preserving the actual finite logarithmic transforms and the given punctured complex family. It cannot be a mere change of the normal line, since that ambiguity has now been solved. It cannot identify the twelveODPs by the existing collar gluing. A further quotient, contraction, or different central cusp chart would need a genuine holomorphic family construction and an explicit comparison onh≠0. Neither the affine torsor nor the auxiliaryEuler24 calculation supplies that operation.
