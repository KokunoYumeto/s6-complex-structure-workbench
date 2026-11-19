# Paper IV: receiving corrections and two high-risk proofs

## Outcome and one repair

There are **33**, not 34, printed `iv:correction:*` statements. I wrote the correction implications before reading those 33 receiving proofs, then compared every printed proof. Their physical sign, directed fixed-edge factor seven, literal shorter endpoints, ordered-fan scopes and retained order-two ambiguity agree with the named inputs.

Opening the retained primitive-profile construction after this comparison found one error in the receiving statement **iv:correction:P3K.22**. It calls the cap contribution a first-homology contribution, while the actual source map in night:P3K.22, equation (P3K.22.1), is

\[
0\longrightarrow\bigoplus_i(\mathbb Z/m_i)^2
\longrightarrow H_2(Y;\mathbb Z)\longrightarrow\ker D_1\longrightarrow0.
\]

The exact correction now proposed says explicitly that this is an injective degree-two term in `H_2(Y;Z)`. The sphere restriction `m_i=1` follows from that injection. The physical index table is unchanged. This is a source/statement correction found by opening the actual morphism. The frozen prereading note inherited the receiving statement's `H1` wording; it remains frozen so the later discovery and correction are visible.

The exact replacement is the fifth entry in `proposed_patches.json`. The individual proof locators and verdicts are in `IV_high_risk_audit.tsv`.

## Integral rank-two specialization

The complete proof of `iv:rank_two_specialization` was opened before I wrote its independent computation, so no before-reading re-proof is claimed. Its actual family morphism first deforms the four holomorphic units through their disc logarithms, with the valuation matrix unchanged. Uniform logarithmic domination supplies compact fundamental regions; local lifts of the deformation parameter preserve the base coordinate and every branch stratum. A partition of unity and completeness give the invertible family flow. This is the transport of the specialization diagram used in the calculation.

The new program derives the opposite-curve restriction matrix directly from the six toric ray divisors, then checks its Smith form together with the dual-complex matrix. It separately constructs every exterior-power matrix of the integral nearby monodromy `b_i -> b_i+a_i`, computes the invariant ranks and primitive constraints, and obtains `(1,2,4,2,1)` on both sides. The proof's cross generator is a genuine descended Cartier line: the exact multiplier `z_1^(nu_2) z_2^(nu_1) q^(nu_1 nu_2)` satisfies the full quadratic cocycle, and its unitary connection gives `a_1 b_2+a_2 b_1` with coefficient one. These generator maps prove integral surjectivity; equal free ranks then give the actual isomorphism.

No rank-only inference about an integral index is used. No topology-only comparison is substituted for the family map with its units.

## All reduced caps, with both characteristic integers

I read all nine steps of `night:P3K.108` / `iv:i3_all_reduced_caps`, and the explicit `night:P3K.103` OC.1--3 inputs that construct its source, point line, translation and full norm root.

The exact ordinary/root comparison retains

\[
H=\frac{1-t_c(s)z^m}{1-t_o(s)z^m},\qquad H(s,0)=1,
\]

with its unique deck-invariant logarithmic root. The source substitutions produce the displayed `UV=X^3` root resolution. The proper graph of `(tau',z^(2l+1))` retains the separate point-section Cartier modules at their coincidence. The full formal addition calculation gives `tau'(6G')=z^(2l+1) s ell(s,z^m)` with `ell(0,0)=-1`; this full rational unit was recomputed independently, rather than accepting only its leading term.

The normalized line lift and all its translated coefficients satisfy `A^m=B^n` and `(A^n)^m=B` for both signs. The weighted norm gives a strict compact quotient. The original annular arrow, not a boundary isotopy class alone, pulls the same prescribed boundary horizontal field into both caps. Relative extension and circle averaging give cap products over the source disc with exactly matched boundary products.

This last point proves the strong conclusion. On each physical quotient cap, the tangent and line connections can be taken as pullbacks from its five-dimensional body. On its product with the source circle, the degree-six representatives of both `x^3` and `p1 x` vanish. The complete collar line maps and tangent derivatives match these to identical exterior connections, including their transgressions. Thus **k and ell agree separately**, not only their linear combination. The selected Hopf completion lies in the unchanged exterior, so the same physical coordinates are used on both sides.

The signed integral meridian comparison is checked with its inverse, including the norm sign. The sphere reference is transported along the specified ordered source arc. Every subsequent native fan replacement takes place in the common selected tube; hence the quadratic-reference pair, its vertical polynomial and its complete witness words transport through the same actual maps to every reduced cap in the theorem's stated scope.

The initial `(47,-4)` is an input from the full K106 calculation. This audit has not independently repeated K106's several-thousand-line compact-stratum and moving-cap construction, and gives no new whole-proof credit for it.

## Independent exact computations

`code/independent_IV_checks.py` was written without reading, importing or running any earlier S6 verification code. Its retained output is `code/independent_IV_checks.json`. The initial execution passed **22,697 exact checks**. That count is a count of assertions in the program, not a count of independent proofs.

For fan updates the program solves the prism equations by rational Gaussian elimination, including consistency and uniqueness, and only then compares the printed reconstruction formula. It independently reconstructs the actual fixed-word outputs for K71, K73, K77 and K106. In particular:

| Actual word / family | Fresh exact result |
|---|---|
| K106, `C0,C1` | additions 48 and 300; integer 356; residue 20 |
| K106, words from `T0` of length at most seven | all 28 residues, with full intermediate matrices saved |
| K71, `C0,C1` | integer -55; residue 1 |
| K73, primitive OS45, `C0,C1` | integer 123; residue 11 |
| K73, original shorter family, `Q0,Q0` | residue 3 |
| K77, shorter OS49, `C0,C1` | integer -49; residue 7 |
| K73 original and K77 at k=1, explicit finite words | all 28 residues |

The actual words and all intermediate period matrices, variation matrices, derivative vectors, weights, prism traces and native additions are saved. A compact K106 witness table is in `code/independent_K106_witnesses.md`. These are new exact computations of the stated geometric algorithm, not independent new proofs of its geometric derivation.

For the K100 and K107 closed formulas, `S -> S+112` changes each integer by a multiple of 28. Every primitive residue vector modulo 112 lifts to a primitive integer vector: fix a nonzero representative of one coordinate (use 112 if it is zero) and choose the other modulo 112 to avoid its finitely many additional prime divisors. The Chinese remainder theorem provides that choice. Every primitive pair extends to a determinant-one basis by Bezout. Exhaustion of all 9,216 primitive residue vectors is therefore an exhaustive finite calculation for every basis fan, not a bounded search in integer coefficients. Both exact images are

`{0,3,4,5,7,10,11,12,14,17,18,19,21,24,25,26}`.

The source/cap computation additionally checks the discriminant, rational selected-height map, three resolution charts, nine exact root substitutions together with their universal exponent identities, signed meridian inverses, the full sixfold point by chord-and-tangent addition, the translated x-coordinate on the middle chart by polynomial division, and the exact fan reflection adapter

\[
-\operatorname{diag}(-1,1)T_j R_0^2\begin{pmatrix}0&1\\1&0\end{pmatrix}=T_{1-j},
\qquad R_0=\begin{pmatrix}-1&-1\\1&0\end{pmatrix}.
\]

The affine height translation and the complete point-line unit in the actual reflection are retained in the paper's map; this matrix identity identifies its periodic fan label.

## Frontmatter and the source-opening boundary

`frontmatter_IV.tex` and its mapping JSON group all nineteen inherited rung blocks into seven main theorems. Each statement retains the physical line, positive parameter, fan, cap, signed norm, finite character, annular reference and scalar range actually used. There are 5, 6, 7, 6, 6, 7, 7 outline steps. The complete existing family/construction/class/positive-cover table is retained, preceded by the explicit mapping-torus covering morphism. The optional abstract has fewer than 250 words.

At the first audit stage the normalizing Jin coordinates `(1,4)` and `(8,8)` had not been newly opened in the external primary source. That source-opening gate was subsequently closed on19November2026: the exact arXiv v2 PDF and complete mathematical HTML were retrieved, and Proposition3.1, Lemmas4.4/4.8, the g=1 table, Theorem4.9 and the complete Lemma6.2 collar proof were read. The precise current scope, original seam and PDF hash are in `Jin_primary_verification.md`. The independent Eells–Kuiper and physical-line computations remain distinct from this source reading.

The attached original AC26 PDF, E26 source and both DGKX versions were searched in full for the IV-specific constructions, invariant and return terms. The actual relevant hits concern the original local torus mapping tori, one-vertex toroidal filling, smooth six-sphere classification, and the full physical action. None of those search hits states the numerical IV source-loop returns. Three additional primary-domain online searches on 19 November 2026 returned no results. Their exact queries and attached-source match data are retained separately. This is a bounded search record; it does not prove global absence of a prior theorem. The frontmatter accordingly records the actual source-specific comparisons and internal corrections without turning an outstanding novelty/source-opening gate into a mathematical assertion.

