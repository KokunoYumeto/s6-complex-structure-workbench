# Paper V: integral canonical classification and the 56 involution classes

Checked on 20 November 2026 by the S6_SERIES_PUBLISH topology-check agent, GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited (no separate numeric setting exposed). Source: the attached `S6_series_V_corrected_20261120.tex`. No prior implementation or earlier conversation was used. The separate pre-read note was written before accessing the proof bodies of `maps:src:F.2.37`, `maps:src:F.2.38`, and `maps:src:F.2.39`.

## Result and scope

The independent derivations and new computations agree with the three statements and their printed proofs. The relevant exact anchors are:

| Statement | Tag | Check actually performed |
|---|---|---|
| `maps:src:F.2.36` | `02NR` | Printed proof read and its algebra reduction checked against the exact primary algorithm; this was not a pre-proof derivation. |
| `maps:src:F.2.37` | `02NS` | Independent pre-proof derivation of canonical enumeration, explicit input bound, witness transport, and the absence of a global bound; then compared with the full printed proof. |
| `maps:src:F.2.38` | `02NT` | Independent pre-proof derivation of integral involution normal forms, the exact anticommutator quotient, binary similarity action, count, free affine lifts, and the orbifold obstruction; then compared with the full printed proof. |
| `maps:src:F.2.39` | `02NU` | Independent compositional derivation of the classification scope, followed by a check of the explicit maps transporting all marked affine and cusp data in the full printed proof. |

This check does not certify execution of the general number-field principal-ideal algorithm or a general implementation of the entire F.2.31–35 homology pipeline. It verifies the mathematical reduction used by F.2.36 and the complete finite involution enumeration. The separate analytic agent checks the analytic inputs of the headline theorem F. The earlier topology check notes contain the independent F.2.28 and F.2.30 derivations on which the final compositional statement relies.

## Canonical classification and its precise bound

Let an input tuple have maximum entry height H. Listing integral tuples by height and then lexicographically gives a total order whose initial box has at most `(2H+1)^(36(k+1))` elements, the preserved display `maps:eq:F.CN2` (`02FM`). The original tuple occurs in that box. Exact admissibility and simultaneous-conjugacy decisions therefore find the least member of the orbit after finitely many tests. The returned conjugator is recorded; equality of least representatives gives the explicit conjugator between two inputs by multiplying their witnesses. This proves the canonical representative claim without a bound on conjugator entries.

The independent derivation used the trace invariant in `maps:eq:F.CN3` (`02FN`). The polynomial `-v^4+v^3-v^2+2` is unbounded on the integral affine subfamily specified by the preceding source theorem. Every fixed finite entry box contains only finitely many values of that trace. It therefore cannot represent every simultaneous-conjugacy orbit. Here the preceding theorem's displayed family and trace formula were accepted as inputs; that family was not reconstructed again in this check.

The printed proof also supplies an explicit free lift for any finite-order integral M with a primitive fixed vector u. For linear order d>1, put `g(x)=Mx+u/d^2`. A fixed point of its j-th power, after applying the norm `S_d=I+...+M^(d-1)`, forces `d | j`. Writing j=dr in the original equation then forces `d | r`. Thus the affine order is d² and every nonidentity power is free. For M=I the translation u/2 has order two and is free. Conversely an invertible I-M gives an explicit fixed point `(I-M)^(-1)a` for every affine translation a. These equations justify the proof's finite admissibility test. The identity-slot convention preserves the ordered conjugacy problem and is explicitly compatible with the subsequent affine-data deletion formula.

## Exact integral maps behind the 56 classes

For a primitive rank-three square-zero N, the cusp-adapted integral basis gives `N=[[0,I3],[0,0]]`. The relation for two involutions yields `M1 N M1=-N`, hence

`M1=[[A,B],[0,-A]], M2=[[A,B-A],[0,-A]], A²=I3, AB=BA`.

The exact cusp centralizer is `G=[[P,Q],[0,P]]`. Its diagonal block P changes A by integral conjugation; its upper block changes B by the anticommutator `D -> AD+DA`, after the corresponding P transport. The eigensublattice/glue calculation in the pre-read note proves that

`A=I_p ⊕ (-I_q) ⊕ J^r`, where `J=[[0,1],[1,0]]` and `p+q+2r=3`.

The quotient for B is identified by an explicit homomorphism, not merely by a count. A commuting B induces endomorphisms of

`K+=ker(A-I)/(I+A)L` and `K-=ker(A+I)/(I-A)L`.

These are respectively `F2^p` and `F2^q`. On each pure-sign diagonal block, the anticommutator image is twice the full matrix group. On every swap-to-swap or sign-to-swap block, the formulas in the pre-read note show that it is the whole commuting block; opposite-sign commuting blocks vanish. Thus the induced map has exactly the anticommutator image as its kernel and identifies the quotient with `Mat_p(F2) ⊕ Mat_q(F2)`. Integral centralizer units induce independent similarity transformations on the two summands. Conversely elementary integral lifts realize every binary invertible transformation. The remaining zero-residue difference is removed by an integral anticommutator solution. These are the precise maps furnishing the normalizer and its witness.

The printed proof's more restrictive binary lift observation is also valid in the dimensions used: a 0–1 matrix of size at most three with odd determinant has determinant ±1, since the absolute determinant bound in size three is two. The elementary-lift construction already proves the required surjectivity without this bound.

## Fresh exhaustive computation

The independently written program is `S6_SERIES_PUBLISH_V_involution_56.py`; the full output is `S6_SERIES_PUBLISH_V_involution_56.out`. It was run successfully at the UTC time recorded in that output. It imports no earlier program, representatives, or saved classification result.

For every n from zero to three, the program enumerates all binary n-by-n matrices and the entire group GL_n(F2), forms every similarity orbit, and chooses its smallest binary-encoded member. The group orders and class counts are:

| n | Number of matrices | Order of GL_n(F2) | Similarity classes |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 |
| 1 | 2 | 1 | 2 |
| 2 | 16 | 6 | 6 |
| 3 | 512 | 168 | 14 |

The six integral involution types give:

| (p,q,r) | Classes |
|---|---:|
| (0,3,0) | 14 |
| (1,2,0) | 12 |
| (2,1,0) | 12 |
| (3,0,0) | 14 |
| (0,1,1) | 2 |
| (1,0,1) | 2 |
| Total | 56 |

For each of the 56 representatives the output contains A, B, the full six-by-six M1 and M2, and a primitive fixed vector for each. Integer arithmetic verifies both involution equations and `(M1 M2)^(-1)=I+N` with the fixed primitive rank-three N. The program then uses full Smith transformations of `M^j-I` to test the torus-image equation for translation `j u/4`, for j=1,2,3 and each of the two finite matrices. Every test excludes a fixed point. As the fourth power is the integral translation u, the affine order is exactly four.

The all-twists simple-connectivity obstruction is a separate proof step: every finite affine order over a linear involution is divisible by two, while the marked two-point orbifold quotient is cyclic of order `gcd(m1,m2)`. It is therefore nontrivial for every such pair. No finite computation is being substituted for that universal argument.

## Primary algorithm check for F.2.36

The source proof computes the saturated integral intertwiner lattice H and centralizer order O. Rational invertibility is decided by the determinant polynomial on a basis of H; successive evaluations in `{0,...,6}` suffice because its degree in each variable is at most six. An invertible rational intertwiner D gives the exact right-module map `H -> L=D^(-1)H` inside `E=Q O`.

The primitive cusp hypothesis is unnecessary here: a rational cusp-adapted basis suffices. The centralizer of N maps to a subalgebra S of `Mat_3(Q)`, with square-zero kernel. Every simple factor of `S/rad(S)` appears on a composition factor of its faithful three-dimensional module. A factor `Mat_n(D)` with center K and division degree d needs a simple rational module of dimension `n d² [K:Q]`. That dimension is at most three; thus d=1. This proves the split-algebra hypothesis needed for the external algorithm. Passing to the opposite algebra converts its left-module convention to the manuscript's right-module convention.

The author/publisher primary source was opened at:

- Bley, Hofmann and Johnston, *Computation of lattice isomorphisms and the integral matrix similarity problem*, Forum of Mathematics, Sigma 10, e87 (2022), DOI `10.1017/fms.2022.74`.
- Published PDF, [institutional copy](https://epub.ub.uni-muenchen.de/94856/1/computation-of-lattice-isomorphisms-and-the-integral-matrix-similarity-problem.pdf): hypothesis (H), p. 2; Theorem 3.4 and proof, p. 6; Propositions 8.1–8.2, p. 21; Algorithm 8.3 and its correctness proof, p. 21; Theorem 8.4, p. 22.
- [Publisher HTML](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/computation-of-lattice-isomorphisms-and-the-integral-matrix-similarity-problem/C1E2B6BA9E5607EC4C39BE2500DDF95F), same exact statements. Web source references: `turn497421661view0`, `turn863834440view0`, `turn863834440view1`, `turn593819468view1`, `turn593819468view2`.

Their algorithm returns a generator of a principal full lattice in the split semisimple algebra. Their radical-reduction result justifies testing one lifted generator: when a full lattice is principal, every lift of the quotient generator is a generator. The manuscript's final determinant test then decides unimodularity. The nilpotent inverse is a finite geometric series in the integral order, so this final test does not omit another possible lift. The cited exact locators and hypotheses match the manuscript. No claimed polynomial runtime is needed for its unconditional termination statement.

## Marked geometry in the final synthesis

The proof of `maps:src:F.2.39` explicitly transports all data by

`M_i'=R M_i R^(-1), v_i'=R v_i, kappa'=R kappa, P'=R P`.

The torus map `x -> R x` intertwines every affine quotient. At the cusp, `(P')^(-1)x'=P^(-1)x`; hence the marked toric chart coordinates, translated face identifications, and collapse map agree exactly. The same map takes the clutch path to the path with vector `kappa'`. These maps agree on the collars and give the asserted diffeomorphism of fully marked gluings. The statement therefore uses the canonical linear representative without changing the chosen cusp filling independently.

For an affine order-one site, the formula `kappa -> kappa+(M_(i+1)...M_k)^(-1)v_i` is the exact previously proved deletion map retained in this synthesis. The theorem subsequently invokes the specified integral group presentation and finite gluing complex, and invokes both directions of F.2.30 for the retained three-connected data. Its scope is consistent with those inputs. No additional classification of arbitrary affine gluings solely by their homology is asserted by these verified maps.

## Editorial and verification status

No mathematical discrepancy was found in this scope. The canonical-enumeration and involution proofs are complementary and should remain separate: the first is a general per-input decision argument, and the second supplies a complete finite normal form with explicit witnesses and a universal obstruction for that stratum. The earlier consolidation file handles the actual repeated topology proofs elsewhere in V. A final read of the integrated rewritten manuscript remains necessary after root applies the shared-cusp and theorem-merger edits.

## Additional exact trace certificate

After the foregoing source comparison, the trace input of F.2.37 was independently recomputed in `S6_SERIES_PUBLISH_V_trace_polynomial.py`, with saved output. The new method uses direct integer arrays and five evaluations, combined with a proved degree-four bound from the displayed X and Y in F.U1. The five traces are 2, 1, -10, -61, and -206 at v=0,1,2,3,4. Exact interpolation gives `-v^4+v^3-v^2+2` and successive difference `-4v^3-3v^2-3v-1`. The degree bound makes this a polynomial identity certificate, rather than a finite sampling claim. Transpose and cyclicity identify the homology word, the diagonal one-dimensional extension contributes one, and the displayed rational conjugation preserves trace. These are the precise maps relating the computed rank-five arrays to the marked six-dimensional word. The earlier pre-read note remains unchanged as a record of what had been derived before access to the proofs. This additional computation is the sixth row event in the classification event file.
