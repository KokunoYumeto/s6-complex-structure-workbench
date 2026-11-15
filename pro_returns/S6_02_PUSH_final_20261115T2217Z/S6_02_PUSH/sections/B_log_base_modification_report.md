# B.4.27: no logarithmic repair by modifying the base

Owner: classification_e. 15 November 2026. **Proved and integrated after B.4.26; root and boundary_d complete-source referees passed.** Root independently opened the original KKN base-change Lemma1.2.9 on pp.80–81.

Let q=Q^(12m), r=R^n, and blow up any finite sequence of points over the bidisc origin. If E is the exceptional divisor, the exact bounded-character sheaf is the product of the meromorphic-unit sheaf with support on strictQ+E and that with support on the full reduced boundary. The first character is not allowed a pole or zero on strictR. This distinction is retained throughout the proof.

The Picard group of the blown-up bidisc is generated integrally by exceptional curves, with unimodular intersection matrix. The divisor-order exact sequences therefore give H1=0 for both bounded factors and H2=Z per exceptional P1. Under restriction to such a curve with orders(Q,R)=(a,b), the period map in degree2 is diag(12ma,12ma+12nb). Both entries are positive. Consequently H2(Y) injects into H2(Tlog), and the quotient sequence gives H1(A)=0. The actual punctured torsor is nontrivial by B.4.24, so it cannot be the restriction of an extending torsor on the modified base.

The analytic cohomology calculation is supplied directly: two-chart Laurent splitting gives higher O-direct-image vanishing for a point blowup; Hartogs gives its O-direct image; the exponential and divisor-order sequences compute the required Picard and log groups. The finite exact program checks 124 marked blowup sequences including smooth exceptional points and crossings with either strict boundary axis. The proof is by the stated all-length geometric argument, not by that finite enumeration.

This blocks an attempt to repair the specified logarithmic torsor by first blowing up the base and then taking a proper KKN fan model. It does not block every analytic cap. Flattening an arbitrary cap produces local finite multisections on the modified base, but need not give a global finite multisection over the exceptional curve, an extending log origin, or the quotient sequence used here. That missing implication is explicitly retained. The actual proper origin cap and B.5 invariants remain Open.

Files: `B_log_base_modification.tex`, `B_log_base_modification_results.csv`; exact code/output/json `code/e_push_log_blowup.*`; independent D referee saved separately. The original KKN source access is updated in `B_analytic_comparison_references.bib`.
