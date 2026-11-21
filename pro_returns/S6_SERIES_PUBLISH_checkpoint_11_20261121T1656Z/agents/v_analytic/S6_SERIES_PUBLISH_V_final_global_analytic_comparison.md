# Paper V: final global analytic comparison, candidate02

## Evidence type and exact source

This is a final **used-and-rechecked source/proof comparison**. It compares the candidate02 main statements and every assigned outline step with their current body statements, proof mechanisms, exact parameter maps, and established special cases. It uses the earlier exact computations, interval rerun and independently typed checks in this agent's existing records. It is not a fresh blind re-proof and receives no new independent or targeted credit. Rendered-page reading is recorded separately and creates no mathematical events.

Source: `work/S6_SERIES_PUBLISH_V.tex`, SHA256 `56de5560038d186d41491df6d678d76d6d2fc4054287fbd91a7278757674b1c5`.
Candidate02 PDF SHA256: `d3f80520bce3433fdc23997e4c1d4668b73672ed556c625653d4558ce7202b82`.

The printed letters differ from the preserved original statement IDs:

| Printed main theorem | Original ID | Scope actually compared here |
| --- | --- | --- |
| B, exact family | `series:V:E` | Entire analytic statement and outline steps1–6 |
| C, genus-two periods | `series:V:C` | Entire statement and steps1–5 as a dependency comparison; analytic splitting, normalization, real transversality, cusp and compact-family maps rechecked directly; integral-pencil inputs use the topology agent's established checks |
| E, integral classification | `series:V:F` | Analytic/Oka paragraph and abelian-source paragraph, with outline steps5–6; integral classification and smooth-type paragraphs remain the topology agent's scope |
| F, resolved fibre product | `series:V:A` | Entire statement and steps1–5 as a dependency comparison, with construction, canonical/direct-image/Hodge/algebraic-dimension/class-C/characteristic arguments read directly; exact integral homology input uses the topology agent's checks |

The source main-theorem block and all four outline blocks were read directly in this pass. The supporting current analytic proofs were reread in source and/or in the assigned rendered pages; candidate01 pages20–54 and123–129 had already been read in full, and all35 changed candidate02 pages were then read in full. The earlier event's scope is not used as a substitute for this final comparison.

## Printed B: exact family and both parameter ends

The parameter is Definition1.1's canonical `sigma_b`, `alpha`, fixed real `e`, and `F_xi=(sigma_b+xi alpha e)(P)`. The body proves the scalar conversion `alpha_0=alpha_alg/8`, `alpha=(625 pi i/16)alpha_0`, and `omega_norm=(16/(625 pi i))omega_alg`. The scaled wedge map takes `omega_norm` to `omega_c/2`; therefore the normalized intersection vector is real with `alpha(n)=1`. These identities are the normalization behind the height, not a change inferred from matching decimal values.

The actual compact periods are `Fhat_xi=K F_xi=conjugate(F_{-conjugate(xi)}(conjugate(lambda)))`. The body supplies the real integral involution K, `K e0=e0`, `KA=A^{-1}K`, `KB=B^{-1}K`, and proves the equality with `X conjugate(X)^{-1}` using the common scalar commutant and specified based meridians. The map preserves Im(xi), and fixes the imaginary subfamily. The cusp correction is `-conjugate(C_{-conjugate(xi)}(conjugate(q)))`; the exact equality to a fixed linear image establishes joint holomorphicity. Uniform shrinking on relatively compact parameter neighbourhoods yields the compact holomorphic family in the canonical coordinate.

The main formula `c_*=(96/(625 pi)) Re(X H_infinity)_{03}` matches the body's negative endpoint height. `H_infinity` is the regularized infinity-root limit `lim H(u^{-5})D_infinity(u)=U_infinity(1)^{-1}`. The root normalization at lambda=1, gauge, comparison X, and sign agree. The unique infinity minimum is supported by the common certificate proof: root symmetry and strict Hessian near the root; convergent continuation and exact closed covers away from it; positive cusp determinant for the inner cusp disc. The supplied Arb rerun and the new exact cover/Bernstein comparison are already recorded separately. This final event neither reruns them nor upgrades their evidence type.

Outline step1 is exactly that minimum proof. Step2 matches the effective root line `L=O((4/5)[infinity]-(3/4)[0])`, its stabilizer characters, `R^q h_*O=exterior^q(O+L^{-1}+L^{-2})` and `K_M=h^*L^{-6}`. The cusp normalization complex gives the dual three-torus and exterior cup product, its invariant flat classes identify the quotient extension, and proper flat root-disc base change supplies the coherent direct images. The root-degree calculation and logarithmic determinant give the stated canonical class.

Step3 and the displayed main Hodge table agree with `night:P1A.2`. The coordinate `z=(625 pi i/128)xi` is introduced before the connecting matrices. Their exceptional zero is `xi=5i/(3pi)`, below the certified half-plane; the point theorem now explicitly names this determinant reason. The residue comparison uses the full branch sequence. The tangent tuple agrees with the weight computation, nonzero residue and Serre duality in `night:P1A.3`. The rank-one parameter derivative is independent of the invertible base derivative, and the resulting nonzero derivative into the one-dimensional miniversal germ forces its defining ideal to vanish.

Step4 matches the vertical-divisor argument, the zero simultaneous alternating-invariant space, intrinsic field C(lambda), fixed three special values, scalar centralizer, excluded negative unit at the order-five cap, and translation sheaf with its displayed half-period. The canonical graph comparison now uses sigma_b. Exact common splitting translation `xi_b=xi_alt-a` proves that the old fixed-splitting formulation gives the same injective classification. The full automorphism group remains C times Z/2.

Step5 matches the two exact anti-intertwiners, finite affine exclusion and the based cusp action `-P`. The image of e2 is `(0,-1,1)`, absent from the fixed fan's primitive component rays. The consolidated Step1 cites the intrinsic algebraic reduction already proved in `night:P1A.4`, and retains the anti-Mobius/three-real-values step. No anti-isomorphism conclusion is obtained by an unsupported comparison of two different fans.

Step6 preserves the precise extension notion in Definition9.1. Its moving anticanonical pencil has two sections lambda^18 and lambda^19. Proper-image/coherent support arguments recover regular tori on an analytically open dense set. Applying the explicit fixed real K^{-1} marking identifies their periods with raw canonical F_xi. The real-hypersurface failure locus cannot be contained in the proper complex analytic exceptional set, at either finite boundary or infinity; finite ramified changes preserve those noncentral hypersurface pieces. The statement is about the proper filling specified in that definition. The punctured-disc theorem uses miniversality and injectivity to obtain its unique classifying map; the Cayley transform extends to an interior value. The degree-at-most-two cover removes the finite torsor and H^1(Delta*,O)=0 removes the additive torsor, giving the asserted smooth filling. The main statement and outline retain these hypotheses.

**Outcome:** all clauses of printed B and all six outline steps match their current supporting proofs and scopes. The canonical normalization, root-frame limit, sign, fixed fan and two different parameter-end questions are stated with their actual maps and hypotheses.

## Printed C: genus-two lifted-period construction

The root statement agrees with `night:P1.4`: the nodal parameter is -256/3125, good roots are eight at zero and five at infinity, and the Hodge bundle is `T^3+T` with degree(T)=1/40. The main statement's meromorphic generator dx/y is the same line ell0 used by the wedge construction.

Outline step2 uses the exact index-two primitive-to-quotient map with Smith factors `(1,1,1,1,2)`. This supplies the rational identification together with the explicitly stated integral defect; it does not silently replace the primitive lattice by its quotient. The body identifies the lower rank-five blocks by the marked map.

Steps3–4 use `P=p(ell0 wedge H_dR)`, rank three, and the decomposable-wedge square argument to exclude the invariant bivector line. The root decomposition gives H^1(Pdual)=0 and H^0(Pdual)=C alpha. `night:P1.15` then supplies the full extension row, its exact constant gauge maps fixing e and the normalization of alpha; the well-definedness proof preceding the merged theorem supplies the real normalized intersection vector. Dependency order is correct: the height definition no longer invokes the later transversality theorem for its own existence.

Step5 matches `F_xi intersect conjugate(F_xi)=0` exactly when `h_b+Im(xi)` is nonzero at all nonsingular points including finite roots. The logarithmic cusp computation gives `h_b=y+O(1)` tending to positive infinity and `N:F_{xi,0}->ker N` an isomorphism. Its exact integral Jordan marking yields `Z=s I3+C_xi`, C holomorphic at zero. Connectedness and the attained minimum give the full upper half-plane; the order-eight fourth power acts as -I before the exterior square and hence descends to order four. The other root remains order five. The body's phrase completed base is implemented by the finite root extensions together with this explicitly logarithmic cusp model; the proof does not posit an ordinary flat limiting torus at the singular cusp.

The canonical parameter map used for compactification is the same K map checked above, and the finite affine/cusp charts in `maps:src:F.3.7` match the marked smooth gluing through their exact real comparisons. The current theorem's bounded-cusp assertion and transversality domain agree with that construction.

**Outcome:** printed C and its five outline steps match the current body. The integral pencil/marking calculations are compared through their established supporting statements and topology records; this row does not claim a new independent calculation of them.

## Printed E: punctured-base periods and abelian-source obstruction

Only the analytic paragraphs and outline steps5–6 are certified by this row. The bounded-cusp theorem assumes k>=1, a GL^+(6,R) representation on the punctured sphere, and rank-three square-zero cusp monodromy. The source's chosen component is the one selected by the positive logarithmic model; every GL^+ transition preserves it. A real marking puts N in the displayed Jordan form, and the primitive integral case has an integral marking.

The current LSAP proof supplies nine independent complex-line directions (determinant -16), a uniform least-singular-value bound >=1/sqrt(3), and Frobenius-radius1/4 spanning tubes. The precise Oka v5 results previously opened give LSAP and the bundle Oka-1 property at the cited scope. The isolated-extension lemma is proved as a relative vertical-spray exhaustion: all new arcs avoid the exceptional point, the old spray preserves the prescribed jets and dominates the attaching region, and summable errors retain the open target. The statement is not replaced by an unsupported assertion that the exceptional fibre is an LSAP bundle fibre.

For the cusp decision, adjoining only the graph chart transverse to ker N gives an open subset of the Grassmann bundle: `y(t)I+Im C` stays positive-determinant for bounded C as y(t) tends to infinity. A polynomial realizes every prescribed finite jet. Connectedness and simple connectivity extend the initial section continuously, and the isolated-point lemma preserves the jet in the holomorphic section. Undoing exp(-sN) gives exactly the stated C(t) holomorphic at zero. Both main statement and outline keep all other marked points punctured. No compact filling at those points is inferred from this Oka theorem, and no general admissible datum is asserted to be a compact holomorphic realization by this paragraph.

The abelian-source clause matches `maps:src:F.3.4` and outline step6. Its algebraic polarized middle rank-four system is semisimple by the opened Deligne source. The maximal toric-rank-two cusp forces its invariants and coinvariants to vanish. The actual filtration from the degree-zero punctured line bundle and quotient by lifted translation has outer trivial rational lines and that middle quotient. Since im N_T=ker N_T, its invariant and dual-invariant dimensions are both one; `maps:src:F.3.1` gives the Euler-parity contradiction to b1=b2=0. Proportionality of the source sections is not used. The pending Engel locator wording credits the two operations exactly; the higher-dimensional filtration and obstruction are proved here.

**Outcome:** the analytic/Oka and algebraic-source portions of printed E and outline steps5–6 agree with the current body and their hypotheses. Its canonical-representative algorithms,56classes, integral homology and smooth classification remain the topology checker’s separately recorded final scope.

## Printed F: resolved transverse fibre product

The entire body section17, candidate02 rendered pages122–128, was read. The main statement takes exactly the canonical marked (3,4,infinity) member X and the specified elliptic surface, with aligned cusp and `L=O_X(S1-S2)`. The root identities L^3=O(S2), L^4=O(S1), L^12=O(W) are the ones used by the Weierstrass construction. The scalar choices give the discriminant fibre at the prescribed cusp and the model's j-function1728t.

Outline steps1–2 match the explicit integral comparison `A Z3 B^{-1}=diag(Z2,s+c_E)`, det A=det B=1, PS=I, and `C3=S C Q+k c_E r`. The bounded-correction common cusp lemma applies in rank three. The fan subdivision adds no rays and all generators have height one, giving the asserted small crepant resolution of the displayed local equations. The marked lattice map S sends the zero-section faces to Kuhn faces, proving extension of the section. The finite diagonal root actions are free because their projection to the marked X model is free; the full fibre multiplicities remain three and four. Proper local models and literal overlap identifications give the compact Hausdorff smooth model, its proper Pi map, and the bimeromorphic comparison on their common dense open set.

Step3 agrees with `maps:src:E.2.1`: root-floor pushforward, direct images `(O,O+O(-1),O(-1))` for X, canonical K_X=L^{-6}, crepant Weierstrass adjunction `K_Z=Pi^*(K_X tensor L)=Pi^*L^{-5}`, and flat genus-one Pi with its section splitting the derived direct image. These yield `(h^{0,q})=(1,1,0,0,0)`. The meromorphic x coordinate gives the finite meromorphic comparison to X times P1, and traces/symmetric functions give a(Z)=a(X)+1=2. The b1=0 input agrees with the preceding simply-connected body theorem; its integral computation remains the topology agent’s checked input.

Step4 uses precisely the cited smooth-centre modification in class C: b1 and h^{0,1} are preserved, so their displayed values contradict b1=2h^{0,1} on the Kahler model. Step5 uses H^2(X,Z)=0 for integral c1(L)=0, hence c1(Z)=0. The current chi(O_Z)=0, c4=6, Riemann–Roch and signature identities give c2^2=2 and signature2. The middle lattice is unimodular of rank2 by the integral homology theorem, hence positive definite; the cited rank-at-most-four classification gives `<1>+<1>`. Main statement, mechanism and all five outline steps agree with these calculations.

**Outcome:** printed F and its outline match the current supporting proofs. This is a final dependency/proof reread, not a new independent reconstruction of integral homology, the referenced six-sphere construction, or the full cited lattice-classification theorem.

## Remaining work and event accounting

No assigned final analytic global comparison remains missing after this pass. No new mathematical contradiction or unproved extension of the stated analytic scope was found. Two rendered-page citation-locator completions (pages124,128) and the separately assigned Grauert/Engel locator repairs are bibliographic work, not mathematical check events. Reflowed pages after those edits must be image-compared/read by the final layout owner.

The separate final-global TSV has four rows, one for each original main ID listed above, under one evidence group. The54-row analytic baseline and five-row final-reading rewrite file are unchanged. Every new row is exactly `used and rechecked in this run`; none is independent or targeted. The complete original anti-isomorphism Step1 and its exact consolidated replacement remain in the separate final-reading rewrite record.
