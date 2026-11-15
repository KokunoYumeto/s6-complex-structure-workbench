# Cusp-twist investigation: exact progress and unresolved comparison

This is a supplementary research and source audit for Part C and Lead 7. It does not assign a value in `Theta_7`. The complete Part D results are in `D_push.tex`; they are unaffected by the unresolved Part C computation.

## Established comparisons

1. `C_closing_cocycle.tex`, C.3.5, verifies the known even-shift formula against both finite root charts and the full cusp toric filling. For the twelve-unit closing shift the ordinary scalar is `K=t^4/(t-1)^3`, while its cusp representative is a holomorphic two-coordinate torus unit. Their ratio is exactly the gamma deck transformation. The scalar pole alone is therefore not an obstruction to extending the actual map.
2. `C_orbit_lift_comparison.tex`, C.3.6, proves directly that smooth equivariant lifts of the same orbit map differ by an isotopically trivial gauge. It also lifts orbit isotopies supported in the free stratum. This does not supply the missing orbit isotopy.
3. `code/d_push_cusp_twist_linear.py` and its output multiply the prescribed integral monodromy matrices exactly. In the ordered basis `(gamma,u,w,delta)`, the cusp monodromy fixes `w,delta`, sends `u` to `u+w`, and sends `gamma` to `gamma-delta`.
4. `C_cusp_orbit_topology.tex`, C.3.7, proves the conductor pushout, including its attaching word, all integral homology groups, and the primitive nonzero fixed-sphere class. `C_cusp_retraction.tex`, C.3.8, supplies the previously missing equivariant strong deformation retraction of a sufficiently small compact cusp body onto the central fibre. The fixed sphere therefore does not bound a three-chain anywhere in that cusp body modulo the circle.
5. `C_cusp_marking.tex`, C.3.9, uses the actual matrix `B0=[[0,1],[-1,0]]` and the triangle labels of the Mumford fan. Its two conductor generators are exactly `a=u`, `b=gamma+u`; the real normalization circle `ab^-1` is therefore `-gamma`, primitive. Neither an extra factor two nor an unmarked change of basis is permitted.
6. `C_annular_reduction.tex`, C.3.10 (classification agent), constructs actual smooth equivariant transports through the finite root and cusp charts. After two explicit equivariant isotopies, the orbit map for six positive parameter loops is `z -> z+chi(q) v_gamma(q)`, supported in a free cusp annulus. The full lift can retain a gauge outside that annulus. The finite logarithmic overlap signs and the exact identity `a-u=v_gamma` were independently checked here.
7. `C_cusp_normal_euler.tex`, C.3.11, proves that the real normalization is immersed with one transverse double circle and that its oriented normal two-plane has Euler number `-2` on the fixed sphere for the complex orientation of the Hopf coordinate `a=xz`. Its absolute value is two regardless of orientation. Thus a compression to an immersed three-sphere must change the normal data; it cannot simply carry this two-plane bundle across a three-disc.
8. `C_translational_quotient_obstruction.tex`, C.3.12, proves that every Hausdorff-valued continuous map constant on the literal regular `ker(gamma)` translational subtori collapses all of `W`. The key is the nonunit modulus of the actual cusp `u` multiplier, `|exp(2 pi i mu0)|=5+2 sqrt(6)`. This supersedes the earlier tentative use of Engel's claimed global Seifert quotient below. The supplied notes already recorded failure of the raw invariant-circle map; C.3.12 proves the stronger universal collapse statement without any priority claim.
9. `C_corrected_seifert_comparison.tex`, C.3.13, now constructs a corrected actual smooth map `X_c -> S^3`, invariant under delta, retaining the actual finite quotient outside a chosen cusp body and changing its leaves inside that body. It uses an invariant integral closed one-form upstairs to extend the exact boundary character. The transverse `q` meridian is the toric section `z1=z2=1`, has raw gamma value zero and bounds an actual disc. The explicit weighted-model formula includes the finite radial logarithm corrections and gives cusp gauge `vartheta=theta-Re(kappa0)`. Thus a positive marked gamma circle on the outer collar really maps to a positive `(3,4)` regular fibre, with target push-off linking twelve. E independently refereed all signs, smoothness and the target inverse. The six-dimensional normal-framing comparison is still open.

Consequently the orbit collar modulo the delta circle has boundary `S^1_gamma x Nil^3`, where `Nil^3` is the mapping torus of the two-torus shear `u -> u+w`. The principal delta-circle bundle on that collar is nontrivial: its Euler class has evaluation of absolute value one on the cusp-angle/gamma two-torus. For an explicit sign convention use the mapping-torus relation `(theta+1,a,b)~(theta,a,b-a)`, with `a,b` the gamma and delta coordinates. Its covering deck map is `(theta,a,b)->(theta+1,a,b+a)`; the invariant connection `db-theta da` has curvature `-dtheta wedge da`, giving Euler number `-1`. This `theta` orientation is the stated monodromy convention and must not be silently replaced by a positive `q`-loop convention.

This mixed Euler class is the concrete reason that a fractional gamma translation on the orbit collar cannot simply be lifted with identity phase at both ends. A full smooth equivariant lift nevertheless exists for the original monodromy, with its outside gauge. C.3.6 removes the ambiguity only after an orbit map or orbit isotopy has actually been constructed.

## Cusp conductor geometry independently checked

The classification agent computes the conductor pushout. Independent checks made here are:

- On the toric normalization `dP_6`, the delta circle fixes two opposite divisors and also the two toric vertices not incident to them. The latter have normal weights `(1,-1)` and quotient neighbourhood `R^3`; they are not extra boundary components.
- The orbit quotient of the normalization is an oriented three-manifold with two spherical boundary components, identified by the toric argument as `S^2 x I`.
- At a fixed divisor of normal circle weight `+1`, the boundary orientation of the orbit quotient is the complex curve orientation; at weight `-1`, it is the opposite. Thus the two fixed divisors with their complex orientations represent the same class in the quotient's second homology. Both conductor maps have degree `+1` on the resulting fixed sphere.
- Gluing just those two fixed boundary spheres gives an oriented `S^2` bundle over the circle, hence `S^2 x S^1`: the gluing is a holomorphic automorphism of `P^1`, isotopic to the identity. The four remaining toric-edge intervals then form two disjoint embedded circles. Each crosses the glued fixed sphere once, and the other two opposite-side identifications identify these circles with an interchange of their two distinguished vertices.

These observations are now proved, with the precise scope of each step, in C.3.7--C.3.11. The invariant gradient flow of `|q|^2` gives the equivariant retraction used for the full cusp body. In a normal-crossing chart `q=z1...zk`, `k<=3`, the estimate `|grad |q|^2| >= c |q|^(5/3)` gives a uniformly finite tail length. No retraction theorem is assumed without checking its hypotheses. The nonzero fixed-sphere class excludes a bounding three-chain in the entire small cusp body modulo the circle.

## Global structure that may supply the missing framing

**Superseded inference, retained for audit.** An earlier version of this note treated Engel's attached Remark 8.3 as providing the actual continuous rank-three quotient onto `S^3`, and thereby viewed the regular gamma circle as a marked `(3,4)` torus knot. The literal extension in that remark is false. The supplied `background/notes/A1_notes.md`, Section 2, A1--1, and `background/S6_SURVEY_20261112.md`, F9, already record nonextension of the raw invariant-circle coordinate. C.3.12 now proves that every continuous map preserving those regular translational leaves collapses the entire cusp fibre; no base-dependent circle reparametrization can retain a central circle. Thus the earlier inference of an actual marked global `S^3` quotient is withdrawn. The finite Seifert pieces and the abstract `(3,4)` filling remain valid comparison data, but a modified cusp map and its framing would have to be constructed and checked.

There is a second numerical/geometric match: AB's component cover `b^3=a^4+1` is the affine Milnor fibre of the `(3,4)` plane-curve singularity. Its compactification has genus three and one point at infinity. The split elliptic pullback studied in B.3.4 has `chi(O)=1`, a single `I_12` fibre, and signature `-8`. No map has been constructed that makes this elliptic surface a Seifert four-manifold for the orbit knot. Its signature cannot be substituted into a Haefliger or Eells--Kuiper formula without that construction and the normal Euler-class comparison.

The elementary weighted model was initially only abstract; C.3.13 supplies the corrected comparison map. On the standard sphere in `C^2`, use the action `(z1,z2)->(lambda^3 z1,lambda^4 z2)` and the quotient coordinate `t=z2^3/(z2^3-z1^4)`. If `F^3=t`, `G^4=t-1`, use `(z1,z2)=(r^3 G exp(6 pi i Theta), r^4 F exp(8 pi i Theta))`, with the unique positive `r` making the norm one and `Theta=theta_gamma-Re(ell)+d(t)`. The function `d` explicitly cancels the actual finite radial logarithm term from `sigma_j=w_j Pi v_j`; it is zero near the cusp. The root deck changes are `(s0,theta0)->(zeta3^-1 s0,theta0+1/3)` and `(s1,theta1)->(zeta4^-1 s1,theta1-1/4)`. Near `q=1/t=0`, the smooth target fibre coordinate is `Theta-Re(s)/12=theta_gamma-Re(kappa0(q))`, where `q=exp(2 pi i s)`. The relative integral-one-form extension replaces `theta_gamma` inside the cusp, so no false literal-quotient extension is used. Its positive target push-off linking number is twelve; this number has still not been transferred to the six-dimensional framing needed for the Haefliger invariant.

Roseman--Takase's explicit generator resolves an immersion with two ordered crossings, with a two-angle parameter torus. Their Remark 5.1 changes the Haefliger invariant by the product of the two angular speeds. Our real normalization has one double circle. No matching of these resolution parameters, nor a global normal framing, has been constructed. The equality `v2(T(3,4))=5` therefore supplies no value for the present twist. Koytcheff's 2025 Remark 5.9 relates graphing phenomena at the graded finite-type level; it does not supply a canonical operation identifying this specific annular map with a knot formed from `T(3,4)`.

A separate arithmetic consistency check is mandatory: the annular map represents `6[Phi]` in `Theta_7=Z/28`, so its residue is even. A direct claim that its Davis residue is the odd number five would contradict this already proved relation. This check does not determine the even residue.

## Relative mapping-class route: source correction and exact scope

Krylov's 2004 author preprint, Lemma 1, describes the relative pseudo-isotopy group of `S^2 x D^3` as the framed-knot group `FC^3_3`, since `Theta_6=0`. The preceding sentence in that preprint claims `FC^(p+1)_q = pi_q SO(p+1)` whenever `q<2p`. This simplification cannot be used at `(p,q)=(2,3)`: Haefliger's original 1966 Theorem 5.17 explicitly gives `FC^3_3=Z+Z`, and Section 5.16 exhibits the independent knot and framing generators. Olbermann (2010), Section 4, independently states this same two-integer result. The actual classification therefore retains the framing and knotting information sought here.

In Haefliger's Section 5.16 the knotted generator has stable differential class zero and its normal push-off gives six times the Hopf generator of `pi_3(S^2)`; the framing generator is the standard unknotted sphere with one generator of `pi_3(SO(3))`, whose stabilization is twice a generator of `pi_3(SO)`. These are potential computable invariants, but neither has been evaluated for the present annular map. Applicability to a selected identification of the actual orbit complement, and the resulting comparison map to the framed-knot group, must be proved before using the classification.

The orbit-complement prerequisite can be justified by the primary results just checked: Fintushel--Pao's Section 1 assumes `n>5`, its Proposition 1.3 smooths the orbit space with the Hopf slice model, and Proposition 1.4(a) makes it a homotopy `(n-1)`-sphere. For `n=6`, `Theta_5=0` gives the standard `S^5`; Haefliger's Corollary 6.6 gives `C_2^3=0`, so the fixed `S^2` is unknotted and its free exterior is `S^2 x D^3`. The classification agent is writing the resulting capped-six-manifold reduction. No characteristic numbers of that cap have been evaluated here.

There is also an explicit harmless framing generator in the linear Hopf model. If `r:(D^3,partial)->(SO(3),id)` lifts to `R:D^3->SU(2)` with `R=1` near the boundary, the quotient map `(x,y)->(r(y)x,y)` on `S^2 x D^3` lifts on `S^6=partial(D^4_H x D^3)` to `(a,y)->(R(y)a,y)`. It commutes with the right-complex circle and extends over the seven-disc. Its homotopy-sphere class is therefore zero. Applying this to the actual action requires the equivariant comparison with that linear model; no integer for the actual annular map is supplied by this observation.

## Page-preimage route under investigation

The corrected map of C.3.13 gives a concrete place to seek a filling. A page of `z2^3-z1^4` is transverse to the weighted Seifert fibres with degree twelve. Over the finite base its marked cover is the affine curve `F^3-G^4=1`, the same genus-three one-ended curve appearing in the elliptic pullback. In the free orbit five-manifold the residual fibres are real two-tori with lattice `(u,w)` and cusp shear `u->u+w`; pulling around the end twelve times gives the `I_12` shear (with the sign determined by whether the boundary is oriented as the complement of a cusp disc). Thus a truncated page preimage has a torus-bundle boundary, not a three-sphere.

An affine torus torsor on that punctured surface can be smoothly trivialized because its degree-two obstruction group vanishes. Such a trivialization does not fix the boundary marking, which can retain the entire cusp correction. To turn this route into a Seifert four-manifold for the actual orbit knot, one must build the specified cusp surgery and calculate its normal Euler class. Simply closing the torus-bundle end by an `I_12` neighbourhood and removing a ball does not prove the required ambient embedding or boundary-knot identification.

As a consistency check only, the genus-three elliptic surface of holomorphic Euler characteristic one has characteristic class `w2=F mod2`. An even proposed normal Euler class would not satisfy the necessary characteristic condition for a Seifert four-manifold embedded in `S^6`. Adding `F` can repair that parity while leaving its square unchanged when the other class pairs trivially with `F`; consequently parity alone does not determine or exclude a cancellation in the Haefliger formula. The proved normal Euler value `-2` on the fixed sphere must also be matched to an actual handle class; identifying it with a narrow `I_12` component would give the wrong pairing.

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
| Fintushel and Pao (1983), *Circle actions on homotopy spheres with codimension 4 fixed point set*, PJM 109(2), 349–362; https://msp.org/pjm/1983/109-2/pjm-v109-n2-p09-p.pdf | Introduction, Propositions 1.1–1.4; scope rechecked at pp. 351--353 | The hypothesis is `n>5`, so the smooth orbit and homotopy-sphere conclusions apply to our `n=6`. Supplies no numerical monodromy value. |
| Haefliger and Salem (1991), *Actions of tori on orbifolds*, AGAG 9(1), 37–59 | Original Theorem 3.1 and Lemma 3.2 facsimile on pp. 5–6 of Karshon's slides below | Equivariance is essential in the general theorem. The printed non-equivariant slice lemma is false. C.3.6 avoids it with a direct proof. Full original paper was not opened. |
| Karshon, *Equivariant orbit preserving diffeomorphisms*, joint work with Schwarz; https://www.fields.utoronto.ca/talk-media/1/23/28/slides.pdf | All 20 slides | Contains the original excerpt, counterexample to its overbroad lemma, and corrected proof outline. No date invented. |
| Karshon and Tolman (2014), GT 18, 669–716; https://msp.org/gt/2014/18-2/gt-v18-n2-p03-s.pdf | Theorem 4.9, p. 690 | Led to the exact orbit-preserving statement; no Hamiltonian structure on `X_c` is assumed. |
| Roseman and Takase (2007), AGT 7, 359–377; https://msp.org/agt/2007/7-1/agt-v7-n1-p17-s.pdf | Theorem 2.1; §§2.2–2.3; Theorem 3.1; beginning of §4 | Provides graphing and an explicit generator construction; a comparison to our annular twist is still missing. |
| Sakai (2015), HHA 17(2), 317–341; https://arxiv.org/pdf/1405.1947 | Theorems 2.5 and 2.11, Corollary 2.7, §3 | Double-point linking determines crossing-change differences, with a separate invariant of the projected immersion. No projection of our knot has been constructed. |
| Gauniyal and Turchin (2026), PEMS 69(4), 1466–1505, https://doi.org/10.1017/S0013091526101485 | Introduction and §4 | The formula requires tangential Smale/Ekholm terms as well as double-linking. In particular a small conductor double-locus count cannot establish vanishing. |
| Krylov (2004), *Relative mapping class group of S^p x D^q*, https://arxiv.org/pdf/math/0409342 | Definitions, Proposition 1, Lemma 1, Theorem 1 | Provides a possible relative mapping-class route. Its preceding range simplification is not used at `(2,3)`, where it conflicts with the original framed-knot computation. The expanded 2007 publication was located, but both publisher PDF URLs returned 403. |
| Haefliger (1966), *Differentiable embeddings of S^n in S^(n+q) for q>2*, Annals 83(3), 402–436, https://www.maths.ed.ac.uk/~v1ranick/tda/haefliger.pdf | §5.1; Theorem 5.3; Corollary 5.9; §§5.16--5.17, pp. 417--421; Corollary 6.6, p. 422 | Defines the framed-knot group and proves its two-integer structure in dimension `(3,6)`; supplies the distinct push-off and stable differential data. Corollary 6.6 proves the fixed `S^2` in the orbit `S^5` is unknotted. |
| Olbermann (2010), *Involutions on S6 with 3-dimensional fixed point set*, AGT 10, 1905–1932, https://msp.org/agt/2010/10-4/agt-v10-n4-p03-p.pdf | Introduction and §4, especially p. 1922 | Independently confirms the framing integer in addition to the ordinary Haefliger integer. Its involution classification is not applied to our circle action. |

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
"Haefliger" "3,4"
"torus knot" "exotic 7"
"torus knot" "homotopy 7-sphere"
"circle actions" "Seifert" "Haefliger invariant"
"Haefliger invariant" "Casson"
"Haefliger" "torus" "Sakai" knot
"Haefliger" "Brieskorn" embedding
"diffeomorphisms" "S2" "D3" "mapping class"
"mapping class group" "S^2" "D^3"
"Haefliger" "S2" "D3"
"Diff" "S^2" "D^3" homotopy
"diffeomorphisms" "S^p" "D^q" Sato
"S^2" "D^3" diffeomorphism group Sato
"relative mapping class" "sphere" "disk" Krylov
"S^2" "D^3" "diffeomorphisms" Sato
"S^p" "D^q" "relative" "mapping class" Krylov
Krylov "Relative Mapping Class Group" "2007"
"FC" "Sato" "Haefliger" "q <"
"S^2" "D^3" "Krylov"
site:intlpress.com "FC" "q < 2p" Krylov
"Relative Mapping Class" "FC" "3"
Haefliger "framed" "C" "3" "3" embeddings Sato
"Sato" "Diffeomorphism groups" "255" pdf
Levine "Self-equivalences" "523" pdf
"torus twist" "S^2" "D^3"
```

No directly applicable theorem identifying this gamma twist with a numbered homotopy sphere was located. This is a record of the searches performed, not a novelty or exhaustive-literature claim.

## Actual cap progress after checkpoint03

The following advances are proved and independently refereed; they replace several earlier speculative routes without changing the retained source-correction record.

* **C.3.14:** the actual six-loop orbit clutching has the specified cap `(S2 × D4) union_double(psi) −(S2 × D4)`. Wall's original Theorem4 on pp360–361 gives `k=6φ+β'` and `p1x=4β'`, hence `J=−φ`. His corrigendum changes Theorem14 only. Independent note: `D_C314_referee.md`.
* **C.3.16:** the global function `h=G2^3−G1^4`, with generic positive normal degree one on the actual central cycle, gives the actual cusp-link inclusion `(γ,u,q)→(12,0,1)` by Alexander duality. This promotes the number12 from a target-knot datum to an actual linking datum in the orbit five-sphere. Source and exact algebra: `C_actual_linking.tex`, `d_push_actual_linking.py/.out/.json`.
* **C.3.17:** deforming the bounded period units to zero at fixed fan gives a marked cusp orbit product `E_I1 × S1`. Prescribed boundary period transport and unitary fixed-tube transport ensure smooth orbit comparison. The zero-unit small-resolution quotient projects to the first Tate family as a circle bundle with the actual second identity section. A normalized positive vertical density extends the exact boundary γ action. Its cutoff isotopy moves the fixed sphere and ends at the actual annular map. The γ-u-w three-torus is a primitive, locally nonbounding H3 generator. Source and checks: `C_cusp_product_extension.tex`, `d_push_cusp_product.py/.out/.json`.
* **C.3.18:** the exterior torus bundle and marked interior product glue to an actual positive genus-one Lefschetz map `Q→S3` with critical knot `(3,4)`. A Milnor page for a nearby weighted circle meets that critical knot in twelve positive points. Its inverse image is a concrete embedded four-manifold bounding the marked three-torus. Relative determinant evaluation through the nodes makes c1 base-pulled, so c1 squared is zero; the outward relative Euler class is12. The relative p1 defect is−24 in the boundary orientation `(γ,w,u)`, or+24 in the ordered `(γ,u,w)` convention. The page/q-normal-frame difference rotates twelve times and is stably null; the defect therefore belongs to the actual affine stable frame. Source/checks: `C_affine_frame_defect.tex`, `d_push_affine_frame_defect.py/.out/.json`.
* **C.3.19:** using the actual cohomology suspension of p1, the relative circle trace of the derivative clutching, and the actual delta Euler class selects precisely this γ-u-w period. Thus the cap's Pontryagin pairing has absolute value24 and Wall's framing coordinate has absolute value6. No primitive H3(SO) or Spin generator normalization is silently inserted. Source/checks: `C_cap_pontryagin_transgression.tex`, `d_push_cap_p1.py/.out/.json`.
* **C.3.20 (E-owned):** after compressing the interior fixed-sphere phase, the actual bounding four-manifold avoids the fixed sphere. Its actual delta-circle line bundle has a boundary-gauge-independent relative Euler square `s_delta`. The cap cubic is one common orientation sign times `3 s_delta`; the same square is the marked lifted-three-torus linking coefficient. Independent referee: `D_C320_referee.md`.

The outstanding numerical step is the identification and square of that **actual** line bundle, including its mixed base–fibre cohomology class. The earlier auxiliary split/torsor surfaces do not supply it automatically. The cap orientation must remain common in the cubic and Pontryagin calculations. No value of J or of the monodromy class is asserted in this audit.

Additional primary source opened while checking possible boundary-loop comparisons: Hatcher (1999), *Spaces of Incompressible Surfaces*, <https://arxiv.org/pdf/math/9906074>, Theorem2 p2. It explicitly identifies the positive homotopy groups of the smooth T3 diffeomorphism group with those of its translation torus. The exact boundary transport in C.3.17 made this theorem unnecessary for that proof.

Additional searches included `diffeomorphism hypersurface circle action twist Pontryagin class logarithmic transform six manifold`, `generalized Dehn twist circle action hypersurface mapping class exotic spheres torus twist`, `"circle action" "Dehn twist" "signature" manifold`, `"torus twist" "Haefliger"`, `"hypersurface" "circle action" "twist" diffeomorphism characteristic`, `Hatcher Homeomorphisms sufficiently large P2 irreducible 3 manifolds torus identity diffeomorphism group T3 pdf`, `nodal torus fibration circle family self plumbing unit fishtail neighborhood monodromy product`, and `transgression p1 H3 SO generator twice spin stable Hurewicz`. They were used to check scope and normalization, not to infer the new numerical cap claim from an unrelated theorem.

## Closure of the actual numerical comparison after checkpoint04

The outstanding steps in the preceding checkpoint paragraph are now closed by actual comparisons. The historical paragraph is retained to distinguish the earlier open state from the later proof.

* **C.3.21 (E-owned, independently refereed):** the actual page is the affine curve `b^3=a^4+1` with marked map `(a^4+1)/(1+epsilon*a^4)`. On its untouched exterior the actual delta line has precisely the varying Picard section P. Excision makes restriction injective across the twelve actual I1 fillings. Integral Leray multiplicativity then compares its mixed-class square with the Jacobian Poincare square without asserting a holomorphic torsor or a global Jacobian diffeomorphism. The explicit Jacobian has twelve I1 fibres, holomorphic Euler characteristic one, and disjoint P and O. Thus the **actual** relative square is minus two. Referee: `D_C321_referee.md`.
* **C.3.22:** direct Chern--Weil calculations distinguish the negative relative boundary-frame transgression from the positive coordinate-clutch suspension. With one common cap sign, `p1x=epsilon_cap*p_rel` and `x^3=epsilon_cap*3*s_delta`. Therefore the actual cap integer vanishes. Source: `C_signed_cap_comparison.tex`; exact check: `d_push_signed_cap.py/.out/.json`. Root and E independently checked the sign, without using the expected cancellation.
* **C.3.23 (E-owned, independently refereed):** the unframed orbit-knot integer is additive on the equivariant component group. Fixed-tube normalization uses actual equivariant isotopies, and compact supports are compressed into disjoint invariant balls in `R2 plus C2`; composition becomes equivariant connected sum. This proves integer additivity before reduction modulo 28. Referee: `D_C323_referee.md`.
* **C.3.24 (E-owned, independently refereed):** coherent positive-shift closings and invariant transport identify the actual annular lift with the sixth power in that equivariant group. The cap integer zero gives `6q(Phi)=0` in Z, hence `q(Phi)=0`. The ordinary smooth monodromy class is therefore zero; its mapping torus is the oriented product `S1 times S6`. Referee: `D_C324_referee.md`.

This conclusion rests on the actual line, its mixed class, the actual annular framing, and the integer group operation. It is not inferred from the classical `(3,4)` knot number, an auxiliary elliptic surface, or a local unipotent derivative. It does not imply an analytic extension of the complex family.
