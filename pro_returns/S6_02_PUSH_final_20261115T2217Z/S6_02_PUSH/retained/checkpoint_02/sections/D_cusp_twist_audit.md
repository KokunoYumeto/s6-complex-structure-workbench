# Cusp-twist investigation: exact progress and unresolved comparison

This is a supplementary research and source audit for Part C and Lead 7. It does not assign a value in `Theta_7`. The complete Part D results are in `D_push.tex`; they are unaffected by the unresolved Part C computation.

## Established comparisons

1. `C_closing_cocycle.tex`, C.3.5, verifies the known even-shift formula against both finite root charts and the full cusp toric filling. For the twelve-unit closing shift the ordinary scalar is `K=t^4/(t-1)^3`, while its cusp representative is a holomorphic two-coordinate torus unit. Their ratio is exactly the gamma deck transformation. The scalar pole alone is therefore not an obstruction to extending the actual map.
2. `C_orbit_lift_comparison.tex`, C.3.6, proves directly that smooth equivariant lifts of the same orbit map differ by an isotopically trivial gauge. It also lifts orbit isotopies supported in the free stratum. This does not supply the missing orbit isotopy.
3. `code/d_push_cusp_twist_linear.py` and its output multiply the prescribed integral monodromy matrices exactly. In the ordered basis `(gamma,u,w,delta)`, the cusp monodromy fixes `w,delta`, sends `u` to `u+w`, and sends `gamma` to `gamma-delta`.

Consequently the orbit collar modulo the delta circle has boundary `S^1_gamma x Nil^3`, where `Nil^3` is the mapping torus of the two-torus shear `u -> u+w`. The principal delta-circle bundle on that collar is nontrivial: its Euler class has evaluation of absolute value one on the cusp-angle/gamma two-torus. For an explicit sign convention use the mapping-torus relation `(theta+1,a,b)~(theta,a,b-a)`, with `a,b` the gamma and delta coordinates. Its covering deck map is `(theta,a,b)->(theta+1,a,b+a)`; the invariant connection `db-theta da` has curvature `-dtheta wedge da`, giving Euler number `-1`. This `theta` orientation is the stated monodromy convention and must not be silently replaced by a positive `q`-loop convention.

This mixed Euler class is the concrete reason that a fractional gamma translation on the orbit collar cannot simply be lifted with identity phase at both ends. A full smooth equivariant lift nevertheless exists for the original monodromy, with its outside gauge. C.3.6 removes the ambiguity only after an orbit map or orbit isotopy has actually been constructed.

## Cusp conductor geometry independently checked

The classification agent computes the conductor pushout. Independent checks made here are:

- On the toric normalization `dP_6`, the delta circle fixes two opposite divisors and also the two toric vertices not incident to them. The latter have normal weights `(1,-1)` and quotient neighbourhood `R^3`; they are not extra boundary components.
- The orbit quotient of the normalization is an oriented three-manifold with two spherical boundary components, identified by the toric argument as `S^2 x I`.
- At a fixed divisor of normal circle weight `+1`, the boundary orientation of the orbit quotient is the complex curve orientation; at weight `-1`, it is the opposite. Thus the two fixed divisors with their complex orientations represent the same class in the quotient's second homology. Both conductor maps have degree `+1` on the resulting fixed sphere.
- Gluing just those two fixed boundary spheres gives an oriented `S^2` bundle over the circle, hence `S^2 x S^1`: the gluing is a holomorphic automorphism of `P^1`, isotopic to the identity. The four remaining toric-edge intervals then form two disjoint embedded circles. Each crosses the glued fixed sphere once, and the other two opposite-side identifications identify these circles with an interchange of their two distinguished vertices.

These observations support the classification agent's pushout calculation `H_*(W/S^1)=(Z,Z^2,Z^2,Z)` and the nonzero primitive class of the fixed `S^2`. They do not prove that this sphere bounds a three-ball in the cusp body. In fact its nonzero homology class excludes a bounding three-chain in the central orbit fibre; transfer of this exclusion to a full cusp neighbourhood requires the stated equivariant deformation-retraction comparison.

## Global structure that may supply the missing framing

Engel's attached source, `background/papers/arXiv_2609.38442_Engel_src/S6.tex`, final remarks following the degeneration conjecture, describes the quotient by the invariant rank-three torus system as `S^3`, Seifert fibred with exceptional multiplicities `(3,4)`. A regular gamma fibre is therefore the regular `(3,4)` torus-knot fibre, with orientations and framing still to be compared to the present cusp collar. This gives a concrete candidate for the global attaching loop; it does not identify the high-dimensional knot produced by the annular twist.

There is a second numerical/geometric match: AB's component cover `b^3=a^4+1` is the affine Milnor fibre of the `(3,4)` plane-curve singularity. Its compactification has genus three and one point at infinity. The split elliptic pullback studied in B.3.4 has `chi(O)=1`, a single `I_12` fibre, and signature `-8`. No map has been constructed that makes this elliptic surface a Seifert four-manifold for the orbit knot. Its signature cannot be substituted into a Haefliger or Eells--Kuiper formula without that construction and the normal Euler-class comparison.

## Exact remaining step

Construct, with the actual finite-root and cusp overlap maps, either:

- an isotopy of the annular gamma orbit twist through maps that lift smoothly, or
- the associated embedded `S^3` in the six-dimensional orbit sphere together with an embedded Seifert four-manifold and its normal Euler class, or
- a projected immersion of that specific knot with its double-linking, Ekholm and Smale data.

The central conductor incidence and the collar monodromy do not supply these framings. Counting its two triple points or its one double circle, or using generic circle equivariance, does not determine a residue in `Z/28`. No order bound is asserted.

## Primary sources opened and the precise use attempted

The bibliographic records are in `D_cusp_twist_references.bib`.

| Source | Material read | Outcome for this problem |
|---|---|---|
| Davis (1982), *Some group actions on homotopy spheres of dimension seven and fifteen*, AJM 104(1), 59–90; https://people.math.osu.edu/davis.12/old_papers/AJM-82.pdf | Introduction, Example 7.14, Proposition 7.15, Corollary 7.16 | Confirms the orbit-knot route and generator examples; does not identify our clutching knot. |
| Fintushel and Pao (1983), *Circle actions on homotopy spheres with codimension 4 fixed point set*, PJM 109(2), 349–362; https://msp.org/pjm/1983/109-2/pjm-v109-n2-p09-p.pdf | Introduction, Propositions 1.1–1.4 | Checks orbit-space smoothing and the scope of the semifree classification; supplies no numerical value here. |
| Haefliger and Salem (1991), *Actions of tori on orbifolds*, AGAG 9(1), 37–59 | Original Theorem 3.1 and Lemma 3.2 facsimile on pp. 5–6 of Karshon's slides below | Equivariance is essential in the general theorem. The printed non-equivariant slice lemma is false. C.3.6 avoids it with a direct proof. Full original paper was not opened. |
| Karshon, *Equivariant orbit preserving diffeomorphisms*, joint work with Schwarz; https://www.fields.utoronto.ca/talk-media/1/23/28/slides.pdf | All 20 slides | Contains the original excerpt, counterexample to its overbroad lemma, and corrected proof outline. No date invented. |
| Karshon and Tolman (2014), GT 18, 669–716; https://msp.org/gt/2014/18-2/gt-v18-n2-p03-s.pdf | Theorem 4.9, p. 690 | Led to the exact orbit-preserving statement; no Hamiltonian structure on `X_c` is assumed. |
| Roseman and Takase (2007), AGT 7, 359–377; https://msp.org/agt/2007/7-1/agt-v7-n1-p17-s.pdf | Theorem 2.1; §§2.2–2.3; Theorem 3.1; beginning of §4 | Provides graphing and an explicit generator construction; a comparison to our annular twist is still missing. |
| Sakai (2015), HHA 17(2), 317–341; https://arxiv.org/pdf/1405.1947 | Theorems 2.5 and 2.11, Corollary 2.7, §3 | Double-point linking determines crossing-change differences, with a separate invariant of the projected immersion. No projection of our knot has been constructed. |
| Gauniyal and Turchin (2026), PEMS 69(4), 1466–1505, https://doi.org/10.1017/S0013091526101485 | Introduction and §4 | The formula requires tangential Smale/Ekholm terms as well as double-linking. In particular a small conductor double-locus count cannot establish vanishing. |

The attempted Springer PDF for Levine (1973), *Semi-free circle actions on spheres*, Inventiones 22, 161–186, https://doi.org/10.1007/BF01392300, redirected to an access page; its theorem was not read or applied. The attempted Schwarz (1980) Numdam PDF was not retrieved within the tool's content limit; no assertion depends on it. The publisher-hosted Sakai PDF returned an access error, so the arXiv author preprint was used.

## Search audit

Queries were run through both search engines where coverage was incomplete. Exact strings included:

```text
"semifree circle" "homotopy spheres" fixed 3 7 spheres
"semi-free" "circle" "7-spheres" fixed
"semifree" "homotopy 7" fixed
"boundary twist" "Haefliger"
"torus twist" "exotic" sphere
"Gromoll" "circle" "Haefliger"
Levine "Semi-free circle actions on spheres" 1973 pdf
"Haefliger" "torus" "twist" diffeomorphism
"boundary twist" "circle action" high dimensional
"Haefliger" "Salem" "Actions of tori on orbifolds" pdf
"Actions of tori on orbifolds" "3.1"
"Levine" "Semi-free circle actions" brandeis pdf
"Haefliger invariant" "torus knot"
"Haefliger invariant" "spinning"
"Haefliger" "Seifert" "circle action" knot
"deform spinning" "S3" "S6"
"Lin–Wang type formula for the Haefliger invariant" Sakai arxiv
"Haefliger" "circle" "torus knot" invariant
"Haefliger invariant" "double point" "linking"
"exotic" "sphere" "torus twist"
"Haefliger" "point pushing"
"diffeomorphism" "S6" "Seifert"
"semifree" "torus knot" spheres
```

No directly applicable theorem identifying this gamma twist with a numbered homotopy sphere was located. This is a record of the searches performed, not a novelty or exhaustive-literature claim.
