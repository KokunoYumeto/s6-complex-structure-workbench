# Main sign theorem: derivation written before opening its printed proof

Checker: GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation, 19 November 2026.

Inputs exposed: statement of cdp:st:C.2.G.1; statements only of its printed dependencies (listed in main_dependencies_statements.json); statements of INT.1--3 and IRR.1. No printed G.1 proof has been read. The preliminary source header read accidentally exposed UN.1 proof steps 1--2; UN.1 will therefore receive targeted-check provenance, not full independent re-proof provenance.

## Derivation

1. Connected fibres give f_*Q=Q. The low-degree Leray edge map injects H¹(B;Q) into H¹(Y;Q). Thus b₁(Y)=0 forces g(B)=0 and the smooth compact connected complex curve B is P¹.
2. P4.26's single-support assertion applies to every irreducible support of this fibration: the local hypotheses comprise smooth total threefold, nearby two-tori and ambient b₁=b₂=0; its separate global conclusion is not needed. Each such Euler number is nonnegative. INT.3 applies to every reducible support because H²(Y;Q)=0, so those Euler numbers are nonnegative too.
3. C2a gives e(Y)=Σ_b e(S_b): regular tori have Euler number zero, and scheme multiplicities do not alter the underlying support. Poincaré duality on the closed oriented real six-manifold gives e(Y)=2+2b₂−2b₁−b₃=2−b₃. The middle cup pairing on H³(Y;Q) is nondegenerate and alternating, so b₃ is even. Hence e(Y) is a nonnegative even integer at most two, namely zero or two. The top Chern number equals e(Y).
4. A rational normalization resolution has strictly positive Euler number by P4.26. UN.1 supplies evenness for each individual support. Since all support Euler numbers are nonnegative and their sum is at most two, this support has e(S)=2. This argument obtains the claimed value without using the stronger finite-character MH.2 formula.
5. For an irreducible singular support, A.5.3 produces an effective anticanonical-type divisor on a resolution. The requisite minimal-surface alternatives must be supplied precisely; the excerpted dependencies by themselves do not explicitly enumerate all alternatives. Once the actual classification statement is opened, the nonrational possibilities must be exhausted. P4.37 excludes positive-b₂ class-VII minimal models, P4.36 gives the Hopf case, and P4.32 identifies exactly the zero-Euler cases. The elimination of ruled base genus g≥2 can use MH.2 plus P4.26, since 2−2g<0. Alternatively, an independently proved genus exclusion would remove MH.2 here. This step has a pending explicit dependency, not a completed re-proof.
6. A sum of finitely many nonnegative Euler numbers is zero exactly when each summand is zero. P4.32's single-support equivalence then supplies the stated irreducible descriptions. INT.3 supplies the stated reducible descriptions, including the actual conductor maps. The description is local per support and imposes no all-support irreducible-or-normal-crossings restriction on the fibration.

## Pre-comparison gate

Steps 1--4 and 6 are formally derived from the exact cited input statements. Step 5 still requires the exhaustive surface list and the higher-genus exclusion; this is recorded before reading the printed G.1 proof. The current result is a targeted logical-chain check, not yet a full independent re-proof of G.1. Its input proofs remain individually subject to the continuation review.
