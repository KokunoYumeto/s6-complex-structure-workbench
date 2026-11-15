# Actual axial origins and the restricted log-torsor obstruction

Owner: classification_e. 15 November 2026, 20:36 UTC. **Historical working proof, superseded at 20:46 UTC by the independently refereed B.4.24 in `B_log_torsor_obstruction.tex`.** Root and boundary_d opened the original KKN definitions and passed the full source. The final version explicitly works with the associated log-torus sheaves; a chosen fan model itself need not be a group object or torsor. This note retains the conditional stages of the audit. The result concerns only locally trivial torsors under the specific KKN log complex torus, including after finite Kummer base changes. It does not exclude arbitrary proper analytic caps, modifications of the base, or non-Kähler vertical threefolds.

## 1. The log group and the exact overlap

Let q=Q^12, let `B=Δ_Q×Δ_r`, `B_q=Δ_Q*×Δ_r`, `B_r=Δ_Q×Δ_r*`, and `U=B_q∩B_r`. The Jacobian log torus A has multiplicative pairing

`[[qA(q), a(q)^6], [a(q)^−1, q r^12 D(q)]]`

in characters `(Z,W)` and period lattice `Y=Zu⊕Zγ`. Its nondegenerate/admissible nature and proper models are checked in `E_B_general_completion_attempt.md`, using the original KKN Definitions 1.2.3, 1.2.6, 1.3.4 and Theorems 5.2.1, 5.3.2. The names A(q),a(q),D(q) in this matrix denote holomorphic units, not the log group itself.

The auxiliary translation is

`F=(μ(s+12v)/2, C(s+12v)/12−(s+12v)^2/24+6v)`,

where `s=log q/(2πi)`, `v=log r/(2πi)`. Its exact differences are

`F(s+12,v)−F(s,v)=γ−6δ`,

`F(s,v+1)−F(s,v)=γ`.

Thus on U it is a well-defined ordinary A-section. For the multiplicative presentation `0→Y→T→A→0`, where `T=(C*)²` on U, the connecting class of this section has Y-monodromy γ around both Q and r. The δ term disappears in T, as it must.

It is essential to distinguish this from the raw actual overlap. B.4.19 proves

`F−σ−kvδ=G(s)+6vδ`,

with `k=−s+12κ0` and `G=(μs/2,Cs/12−s²/24)`. Consequently the raw comparison after the ordinary gauge has only 6δ r-monodromy. Studying F as though it were that raw comparison is invalid. The following use of F is justified only if the two **extending log-group origins** in §3 are actually established.

## 2. A precise ghost-valuation lemma

On the underlying analytic site, KKN's definition gives the exact sequence

`0→Y→T_log^(Y)→A→0`,

where the middle sheaf consists of bounded multiplicative log characters. Along `D_Q={Q=0}⊂B_r`, evaluation of the characteristic monoid gives a homomorphism

`ord_Q:T_log^(Y)→i_*Z²`.

The composite with Y is `u↦(12,0)`, `γ↦(0,12)`. In particular it is injective. These are the actual valuations of the displayed pairing; bounded holomorphic units do not affect them.

If h is a section of A on B_r, choose local multiplicative log lifts. Their overlap differences are Y-periods representing `∂h∈H¹(B_r,Y)`. Applying ord_Q makes this cocycle a coboundary, the difference of the local integral ghost vectors. The restriction `H¹(B_r,Y)→H¹(D_Q,Y)` is an isomorphism, since B_r retracts onto D_Q, and the induced map to `H¹(D_Q,Z²)` is multiplication by diag(12,12). Hence `∂h=0`. In particular every such h has zero Y-monodromy around the r loop.

For a section h on B_q, its class in `H¹(B_q,Y)` also has zero r-loop component, because that loop contracts in B_q. It follows that F cannot be expressed on U as the difference of one A-section from B_q and one from B_r.

Consequently the A-torsor obtained by gluing **trivial A-torsors** on B_q and B_r by F is nontrivial on B minus the origin, and it has no extension which is an A-torsor locally trivial for the usual analytic topology near the origin. Such an extension would admit a local section; after shrinking the bidisc, that section would provide exactly the forbidden splitting. This conclusion does not require any computation of the full H¹ group.

The same calculation survives `q=Q^(12m), r=R^n` with positive m,n. The r-loop class becomes nγ, while the Q-ghost map on Y is diag(12m,12m), still injective. Thus finite Kummer covers do not trivialize this particular torsor obstruction. This statement is about finite Kummer covers of the fixed bidisc; no assertion about arbitrary log modifications is included.

## 3. The axial-origin application requiring independent verification

The candidate application to the actual family is based on the following two explicit identifications, rather than on F alone.

1. **Actual cusp axis B_r.** B.4.9 proves that σ is a global section of the actual affine family for r≠0, including q=0, and that exponentiating σ is a torus-unit automorphism of every cusp fan chart. Its coefficients are holomorphic at q=0. Therefore `ζ↦ζ−σ` should identify this axial log model with the group model of A, with the origin at the section σ. Normalized toric base change q=Q^12 retains that extending section and the same multiplicative period pairing.

2. **Rotating r-axis B_q.** B.4.18 constructs the rotating model as a finite free quotient of its q-root toric model. On the root cover the twelfth affine deck is the actual period γ−6δ; its multiplicative action is precisely the second lattice period. Normalized pullback by q=Q^12 should therefore recover the original root fan model. Its point `(Z,W)=(1,1)` extends in the toric chart over r=0 and supplies the group origin. This assertion is about the normalized pullback; the unnormalized fibre product at Q=0 must not be mistaken for it.

If both identifications are verified as log-group identifications with the stated global sections, the actual comparison `ζ↦ζ−σ+F` becomes translation by F between these origins. Section 2 then applies to the actual axial **log torsor**. Any other extending choice of origin differs by a section on its own axis, so cannot change the tested r-loop class. The ordinary gauge kvδ is not a section extending at q=0, and hence is not an allowed simultaneous change of both origins in this argument.

The two origin identifications have been sent to root and D for independent challenge. Until that verification is complete, this note is an exact conditional log-category calculation. Even if accepted, it would establish no unrestricted analytic nonexistence result: a proper cap with vertical components need not be a locally trivial log-A torsor, and no theorem supplies that implication under the allowed non-Kähler hypotheses.

## 4. Provenance and checks

- Kajiwara, T., Kato, K., & Nakayama, C. (2008). *Logarithmic abelian varieties, Part I: Complex analytic theory*. Journal of Mathematical Sciences, the University of Tokyo, 15, 69–193. Original PDF: https://www.ms.u-tokyo.ac.jp/journal/pdf/jms150104.pdf. The quotient-sheaf definition is §1.3.1–1.3.4, printed pp.81–82. No general torsor-extension theorem from this source is invoked.
- Actual sections and overlap: `ab_push_torus_log_cocycles.tex` (B.4.9), `ab_push_corrected_cusp_overlap_working.md` (B.4.18), and `ab_push_global_partial.tex` (B.4.19). These were read in full for this check.
- `code/e_push_completion_diagnostics.py` checks the exact F differences, the full σ and kv cancellation, and the Jacobian valuation/unit matrices. It does not verify the sheaf geometry or assert an origin cap.
