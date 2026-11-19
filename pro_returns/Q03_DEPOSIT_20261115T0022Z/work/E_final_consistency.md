# Final assembled-text consistency audit

Audit date: 15 November 2026 (Europe/Berlin). Auditor: GPT-6 Astra, effort ChatGPT Pro mode.

Files examined: `Q03_DEPOSIT_post.tex`, `work/frontmatter.tex`, `work/endmatter.tex`, `Q03_DEPOSIT_results.csv`, the current assembly script, and the final-build log. The exact assembled-source hash inspected by the reproducible checker is recorded in `code/E_check_final_consistency.out`. Root's final rendering inspection is recorded separately; this audit checks the text, metadata, CSV correspondence, and reported build counts.

## Verdict

The inspected assembled post and CSV are consistent on the proved exponents, effective constants, input model, theorem ranges, source-statement range, historical/current check scopes, model/effort/date fields, original-prompt qualification, and numbered-statement coverage. Two concrete assembly/scope defects were identified and corrected during this review, and one source-range clarification was incorporated. No remaining mathematical or metadata inconsistency was found within this audit's scope.

## 1. Numeric state-bound rename: defect found and corrected

The first assembly renamed standalone `S` to `\mathcal{S}` but left adjacent products such as `qSN`, `BS^4N`, `DSN`, and the table entries unchanged. Its definition therefore used the new symbol while several costs still used the old one. The defect arose from a word-boundary text substitution.

The revised assembly performs the replacement inside every Section 9 mathematical segment. The exact map is: every occurrence of the old numeric-state-bound symbol `S` in those segments becomes `\mathcal{S}`; prose is unchanged. Section 9 contains no cutoff using that old symbol, and the earlier proof's cutoffs retain their original `S`. The notation table records the correspondence `\mathcal{S}=S_{\text{old Section 9}}=BN^m` in words. This is a rename of the same integer bound.

The checker finds 24 occurrences of `\mathcal{S}` in Section 9 and no unconverted `S` in its mathematical segments after removing those exact command strings. In particular, the corrected dominant expression is

\[
B\cdot\mathcal S\cdot\mathcal S^2\cdot3D\mathcal S N
=3DB\mathcal S^4N=3DB^5N^{4m+1}.
\]

All intermediate record and witness costs now use the same numeric parameter.

## 2. Input model, exponents, and coefficients

Theorem A and the abstract state the common input bound with exponent `60m^2+129m+2`. Equation (1.2) states the padded exponent `60m^2+129m+1` and explicitly begins from the parsed, canonically numbered padded DAG. Section 9's encoding contains explicit vertices, canonical binary integer fields and distinct arcs, so `n≤L`. Its nontrivial padded branch satisfies `1≤T<n`, `n≤mT` and `N=mT≤mn≤mL`. The elementary branches use the original arc list and fit the separately accounted degree-four input cost.

The coefficient formulas in the assembled Proposition 9.2 and Corollary 9.3 match the independently reviewed accounting exactly:

\[
q=64(m+1)(K+1),\qquad D=2^{20}q^2,
\]
\[
A(m,K)=2^{40}(m+1)^4(K+1)^4(K512^K)^5,
\]
\[
G(m)=A(m,12m+25)m^{60m^2+129m+1}+2^{31}(m+1)^4.
\]

The record block makes the same claims with these named coefficients. The common input exponent includes the at most `n≤L` deadline trials. The small-m table is 928/929, 1477/1478, 2146/2147 and 2935/2936 for the padded/input exponents at m=3,4,5,6. No obsolete `60m^2+129m+8` remains in the assembled post. Historical +8 claims remain only in the preserved original provenance, as intended.

The report of the theorem's scope includes decision, a witness on acceptance, and optimal-schedule construction. The description theorem uses global budget `12m+25`, relative-prefix budget `6m+16`, and a one-leaf root. The declarations retain the stated limits: no practical algorithm, no bound polynomial in m, no unsupported variants, and no formalization of this proof.

## 3. Standalone theorem and source ranges

The first assembled Proposition 9.4 said merely “For fixed m”, although its cited computation in Proposition 9.2 explicitly requires m≥3. The revision states “For each fixed m≥3”. The assembled Theorem 8.5 and Theorem 9.1 now also explicitly state m≥3, agreeing with Theorems A and B without requiring an unstated global convention.

The opened OpenAI Theorem 1.1 restricts its deadline input to `1≤T≤n`. The first front-matter cited-result statement omitted that range after an input description allowing an arbitrary integer deadline. The revision now names `1≤T≤n` explicitly for the source's deadline and witness statements; its optimization statement is retained. The main theorem's broader integer-deadline handling is proved by its own elementary branches in Section 9.

The compact-output qualification has its explicit example in Proposition 9.4: fixed m, n=2^k isolated jobs and T=n. The compact input has O(k) bits, while a literal schedule lists 2^k jobs. This supports the stated exponential-output possibility within the same input convention.

## 4. Metadata and verification language

The assembled record, abstract, Status, Verification record, Provenance and Declarations agree on:

- Version 1 and current audit date 15 November 2026.
- Kind: generalization; claim: proved; current mathematical verdict: proved as stated.
- Current checker/editor: GPT-6 Astra, effort ChatGPT Pro mode; current check types F,D,C,S.
- Original question: Claude Opus 5.5, effort not recorded, 22 October 2026.
- Original proof return: GPT-6 Astra, effort ChatGPT Pro mode, 23 October 2026.
- Original format text: Claude Fable 5.2, effort high, 14 November 2026.
- Present deposit-task author: Claude Opus 5.5, effort max, 15 November 2026.
- Three earlier reports: Claude Opus 5.5, effort max, Message Batches API, 23 October 2026 as supplied metadata; verdicts one “proved with fixable gaps” and two “proved as stated”.
- Human understanding: none; formalization: none for this proof; no novelty or priority claim.

The current and historical scopes are separated. The three earlier verdicts refer to the original return; the current FD1 entry refers to the revised text. Historical execution dates, API mode and independence descriptions are identified as supplied-record metadata, with absent raw logs disclosed. The three reports receive no fabricated source-opening or code-execution credit. The source checks identify their actual scope, including original FKN full-text unavailability, the course archival endpoint failure, and unreplayed Lean builds. The latest S-F wording names both the target declaration and actual proof source; the comparator placeholder is not used to describe the separate proof body as absent.

The 9,551-byte supplied original prompt, the historical manifest's absent 9,383-byte variant, and the unsuccessful exact newline/BOM maps are stated in Limits and in the metadata. The original return's SHA-256 is unchanged. The machine-readable record includes the present-task author and effort, matching the updated Provenance and Declarations. No `demonstration` field or obsolete demonstration notice remains.

## 5. Statement CSV and build-count check

The post contains 44 distinct numbered statements in Sections 2–9, including Definition 2.9. The CSV has exactly 47 rows: those 44, Theorems A and B, and Cited result 1. Every numbered statement's complete extracted body matches its CSV `statement` field exactly after the assembly's explicitly defined wrapper construction: kind, number, parenthesized title, newline, and the source body with outer whitespace removed. No mathematical text is rewritten by that comparison. All 44 comparisons pass.

The final-build log inspected during this audit reports zero overfull-box messages, zero undefined-reference/citation messages, and zero fatal error messages. Its `build_check.json` reports 38 pages, zero overfull boxes, and zero boxes over 2pt; the current E1 table row reports the same values. The page images and their visual inspection remain part of the root's rendering record, not a claim derived from these numerical checks.

`code/E_check_final_consistency.py` performs the exact correspondence and metadata tests and records their output in `code/E_check_final_consistency.out`. Re-run it after any later assembly change so its source hash and measured fields identify the delivered source.
