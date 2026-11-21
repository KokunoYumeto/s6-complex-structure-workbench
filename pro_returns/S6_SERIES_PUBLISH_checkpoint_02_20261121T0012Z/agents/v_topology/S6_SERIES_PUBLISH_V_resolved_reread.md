# Paper V: rereading the resolved-product block

## Identity, sources and scope

Recorded on 20 November 2026 at 23:44 UTC by GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited (no separate numeric setting exposed), S6_SERIES_PUBLISH topology-check agent.

I reread the statements and the complete current proofs of `maps:src:E.1.2` (tag `02M5`), `maps:src:E.1.4` (`02M7`), `maps:src:E.1.5` (`02M8`), and `maps:src:E.2.1` (`02M9`) in `work/S6_SERIES_PUBLISH_V.tex`, comparing them with `source/S6_series_V_corrected_20261120.tex`. The comparison is saved as `S6_SERIES_PUBLISH_V_resolved_comparison.diff`. This is a post-edit proof reread, not an independent re-proof before access to the printed proofs. In particular, I did not rerun the complete rational/integral cohomology programs for this block. The small fresh arithmetic checks listed below have their actual restricted scope.

The principal mathematical edit to the original four proofs is the invocation of the earlier common cusp theorem in place of the repeated local properness argument. The dual integral cusp specialization theorem is now at the earlier common-cusp location, with its original label retained as an alias. The other three proofs preserve their steps and calculations; equation numbering and references changed. No theorem conclusion disappeared in these moves.

The six guarded suggestions in `S6_SERIES_PUBLISH_V_resolved_guarded_patch.json` preserve every existing label and tag. The patch generator only writes suggestions and does not edit the main manuscript. The current source was checked against every old string. Final PDF reading has not yet occurred.

## The resolved datum and the morphisms in the headline

The definition `def:V:resolved-product-data` (tag `PV21`) now needs to define the inherited symbols `f`, `B`, `B^circ`, the elliptic surface `S`, and the integral markings used in the proofs. Its line-bundle comparisons are correct. In the divisor group modulo linear equivalence, `3S1=4S2=W` gives

\[
3(S_1-S_2)=S_2,\quad
4(S_1-S_2)=S_1,\quad
6(S_1-S_2)=2S_2,\quad
12(S_1-S_2)=W.
\]

The stated meromorphic functions provide these as holomorphic line-bundle isomorphisms, rather than merely rational cohomology equalities. The newly printed `L^3=O(S2)` is precisely the input used for the coefficient `b` in the first proof.

I opened the attached primary Engel source `source/S6_GRIND_6_literature/papers/arXiv_2609.38442_Engel_src/S6.tex`, section 2, lines 283–304. It specifies the surface by

\[
y^2=x^3-3t^3(t-1)x+2t^4(t-1)^2,
\]

with `j=1728t` and fibres `IV*`, `III`, `I1`. The provenance agent separately confirmed this text on printed/PDF page 3 of the official arXiv v1 PDF; that agent's page inspection is not recorded as my own PDF read. The guarded definition cites section 2, page 3.

The four-dimensional sphere monodromies are exactly those in the attached Paper I, `S6_SERIES_GRIND_I.tex`, the canonical marking at `def:common-conventions` and the following notation dictionary, especially lines 6442–6485. They are also recovered from this proof's displayed three-dimensional vertical blocks by the explicit unimodular maps below. The period symbol `Pi_c` in the structure-sheaf proof is now defined in this datum, including the last-two-columns identity used there.

The original body statement `maps:src:E.1.2` proves a small crepant resolution `r:Z→Wscr` of the Weierstrass model `Wscr→X`, and proves that `Z` is bimeromorphic to `X×_B S`. Its projection `Pi:Z→X` is the composite of those two morphisms. The rewritten headline `series:V:A` had compressed this into a claim of a small crepant resolution of the literal fibre product, and had denoted the projection to the threefold `X` as that resolution. The patch restores the exact body scope and the dimensions of the maps, and makes the same clarification in the abstract. This is a proof-scope correction. No counterexample to another possible resolution is claimed.

## `maps:src:E.1.2`: smooth compact model

I checked all six proof items against the corrected original.

1. The coefficient `a` is a section of `L^4`; `b` is the square of a divisor section of `L^3`, hence a section of `L^6`. Their cubic and square lie in `L^12`. The two divisor lines are identified with the pullbacks of the two independent sections of `O_B(1)`, so the scalar choice making the discriminant vanish at `p0` is available. The section at infinity remains outside the singular locus.
2. At the finite points, the specified root atlases give good reduction. Freeness of the diagonal quotient follows from freeness on the `X` factor, and the same marked zero section descends. The full multiplicities remain three and four. The explicitly defined block matrices now make the stated action reproducible.
3. For the cusp comparison, the displayed maps `A=(P;r)` and `B=(Q;r)` have determinant one and satisfy the exact matrix identity `A Z3 B^{-1}=diag(Z2,s+c_E)`. The bounded correction is carried through that identity. The program below independently multiplied these symbolic matrices after the proof read.
4. The replacement invocation of `night:P1.9` uses the bounded holomorphic matrix `C3` and the identical fan and action under `(q,C)=(t_c,C3)`. The model identification is the identity on the dense torus, so the earlier theorem supplies precisely the removed smoothness and properness argument. The root metadata should explicitly list that theorem and the resolved datum; this is included in the guards.
5. The original toric map, its subdivision without new rays, its height-one crepancy argument and its zero-section extension are all retained. The section's two lattice maps are angular `S` and deck `S B0`: the identity `Z3 S B0=S Z2` verifies the exact period compatibility. Thus the local section is not inferred only from a map of angular lattices. I have not claimed a fresh exhaustive enumeration of the prism subdivision in this reread.
6. The marked product identifications on the overlaps still supply the cocycle, global maps and section. The same proper local fillings and compact remaining base give compactness. The final bimeromorphic identification has the same explicitly stated dense-open domain as in the original.

The move to the shared cusp input loses no proof component. The scope of the small crepant morphism remains the Weierstrass model.

## `maps:src:E.1.4`: fundamental group and rational homology

All four original proof items remain. The section kills the section loops in the simply connected `X`; the remaining elliptic coinvariants vanish. I recomputed the Smith factors `(1,1)` of `(C1-I | C2-I)` using the newly explicit matrices. The Euler argument still counts the six zero-dimensional cusp strata.

The shared integral cusp theorem, under the alias `maps:src:E.1.3`, supplies its rational specialization: the full invariant lattice in every degree and one degree-four cusp kernel. This is the exact input needed for the displayed Leray rows. The retained exterior-matrix computation, the naturality from `X`, the permanent elliptic divisor class, and Poincare duality give the same ranks `(1,1,2,2,1,1)` and Betti numbers `(1,0,2,1,2,1,2,0,1)`. The boundary relation matrices for the finite affine quotients and their Smith outputs are retained. Those full exterior-power and finite-relation computations were not freshly rerun in this reread.

## `maps:src:E.1.5`: integral homology

All nine original proof items remain, with the earlier specialization theorem at the retained alias. The argument still needs the integral, not merely rational, surjectivity of the cusp specialization; the common theorem supplies it, with the sole free degree-four kernel.

The one notation hazard is the use of `M0⊕C0` in the list of cohomology monodromies. In the preceding headline part, `M0` denotes a six-dimensional cusp matrix. Here the sphere block has dimension four. The correct explicit list is `(A1⊕C1,A2⊕C2,A0⊕C0)`, with `A0=(A1 A2)^(-1)`. The patch makes that replacement and defines all blocks in the datum.

The finite adapted markings, the Wang/norm description of covering pullback, and the finite kernels and cokernels are unchanged. The proof that the global invariant two-form hits the degree-two covering cokernel restricts along the elliptic zero section to the original surface `S2`; the cited surface has its own integral even pairing. This argument does not replace that surface by the six-dimensional finite fibre, whose torsion differs. The common degree-three image matrix and the two norm matrices are all retained, as are the primitive Smith conclusion and the restriction orders `3,2,1` which remove global parabolic torsion.

The sheaf exact sequences still give `H1(R2)=0`, `H1(R3)=Z` and the two free targets `H2(R1)=Z`, `H2(R2)=Z^2`. Naturality from the sphere and multiplication by the degree-one elliptic section class still supply primitive, independent transgression images. The free kernels, absence of later differentials, UCT and Poincare duality then give the stated torsion-free integral homology. I checked preservation and use of these exact proof steps, not a new independent Smith reduction of every displayed matrix.

## `maps:src:E.2.1`: complex invariants and middle form

All five original proof items remain.

The root-line coarse-degree formula gives `d(-1)=d(-2)=-1`, and gives the vanishing of `H1(O(1))` used to split the rank-two direct-image extension. The cusp dual two-torus and its exterior cup pairing are still the input for its ranks and the nowhere-zero deck class. The canonical marking's last two identity columns prove that the first-coordinate covector `gamma` has nonzero image modulo the period rows; this is why the new datum explicitly records that period convention.

The relative-duality and canonical calculations retain `KX=L^{-6}` and `KZ=Pi^*L^{-5}`. The section splits the derived unit map, giving `RPi_*OZ=OX⊕L^{-1}[-1]`; projection formula gives the same Hodge numbers. The meromorphic `x` coordinate has degree two on the generic elliptic fibre and supplies the asserted finite generic field extension, giving algebraic dimension two. The argument using the cited class-C model theorem and invariance of `b1,h01` is unchanged.

The final Chern-class sentence is made exact: `H2(X;Z)=0` implies `c1(L)=0`, and the already proved canonical formula gives `c1(Z)=5 Pi^* c1(L)=0`. The Todd and signature identities then give `c2^2=2`, signature two, and the rank-two positive unimodular form. This characteristic calculation should remain in this proof: the earlier fourfold characteristic proposition assumes rational `H2=H6=0` and middle rank four, whereas this fourfold has second and middle Betti numbers two. I have not substituted that proposition across different hypotheses.

## Saved limited arithmetic and exact outputs

`S6_SERIES_PUBLISH_V_resolved_marking.py` and `.out` verify:

- The explicitly defined unimodular changes `U_j=[v_j/(v_j)_gamma,e2,e3,e4]` have determinant one and satisfy `U_j^{-1} A_j U_j=diag(1,D_Xj)`, with exactly the two vertical blocks printed in the proof; `A_j v_j=v_j` and the finite orders are three and four.
- `A0=[[1,0,0,0],[0,1,0,0],[0,1,1,0],[-1,0,0,1]]`, `C0=[[1,1],[0,1]]`, and the elliptic coinvariant Smith factors are `(1,1)`.
- Engel's displayed Weierstrass coefficients give `4a^3+27b^2=-108 t^8(t-1)^3` and `j=1728t`.
- The arbitrary-symbol cusp corrections obey the product identity, projection identity and exact section identity, with both product lattice changes unimodular.

These checks passed after the proof read. They support the notation repairs and explicit morphisms. They do not constitute a new independent pre-read check of all four theorems.

## Applied-text verification

After the parent applied all six guarded suggestions, I checked their complete replacement strings against the integrated source; each occurred exactly once. The parent proposes renaming the resolved-part period symbol `Pi_c` to `Pi_X`. A complete exact-string search found only three occurrences of `Pi_c`: its new datum definition and the two uses in the single structure-sheaf argument. Thus that scoped replacement preserves the identical matrix of the already chosen `X`; it makes no change of member or parameter. These are source checks, not final-PDF checks.
