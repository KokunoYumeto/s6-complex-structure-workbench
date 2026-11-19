# Independent integration audit of the assembled mathematical post

Checker: GPT-6 Astra (OpenAI), effort ChatGPT Pro mode. Date: 15 November 2026.

**Verdict: all requested mathematical integration checks pass.** The assembled post retains the reviewed proof, the statement CSV covers every statement exactly once, the Uses lines agree with the dependency table and CSV, and every source counterpart agrees with the source audit's concordance. Two integration defects observed during the review were corrected by the assembling agent and checked again: incomplete renaming of the numeric state bound, and the empty capacity-transfer explanation for Lemma 8.1. No main-post edit was made by this checker.

The reproducible checks are in `code/E_check_proof_integration.py`; the exact checked artifact hashes and complete output are in `code/E_check_proof_integration_output.json`. The checker reads each artifact once, so its hashes identify the actual snapshot compared. It can be rerun after final typesetting or record updates.

## 1. Complete statement coverage

| Proof section | Numbered identifiers | Count |
|---|---|---:|
| 2 | 2.1–2.10, including Definition 2.9 | 10 |
| 3 | 3.1–3.7 | 7 |
| 4 | 4.1–4.5 | 5 |
| 5 | 5.1–5.5 | 5 |
| 6 | 6.1–6.5 | 5 |
| 7 | 7.1–7.3 | 3 |
| 8 | 8.1–8.5 | 5 |
| 9 | 9.1–9.4 | 4 |
| **Proof total** | | **44** |
| Front matter | Theorem A, Theorem B, Cited result 1 | 3 |
| **CSV total** | | **47** |

The program parses all 44 actual statement environments and reads the CSV with the standard CSV parser, which respects multiline quoted statement cells. It verifies that every expected identifier occurs once, that no additional identifier occurs, and that every proof statement's kind, title, and complete statement text equal its CSV statement. The status of Definition 2.9 is “definition checked”; the other 43 proof statements have “proved as stated.” The front rows separately cover both main theorems and the single cited result. There are zero missing, duplicate, or mismatched rows.

Theorem A's CSV dependencies are exactly 9.1, 9.2, and 9.3. Theorem B's dependencies are exactly Definition 2.9, Proposition 7.3, and Lemmas 8.2–8.4. These are the same direct dependencies displayed beneath their actual statements, with the range 8.2–8.4 expanded to individual identifiers.

## 2. Preservation of the reviewed Sections 2–8

The program extracts the entire assembled text from the start of Section 2 through the end of Section 8, including every unnumbered definition and explanatory paragraph. It compares that text with `work/B_proof_revised.tex` after precisely these recorded assembly transformations:

1. Remove the two obsolete descriptive proof headings above 3.3 and 5.5; their actual numbered steps remain present.
2. In Theorem 8.5 write the standing range explicitly: “For m≥3, every full schedule…” The earlier standing model and notation table already fix m≥3, and the newly written range states that same domain within the theorem itself.

The resulting texts are equal. Thus the full reviewed proof, its unnumbered construction data, and all equations are retained. The explicit selection in Lemma 5.5 is present verbatim as “let x_K be the least-rank job of K∩W′.” Its map f remains an explicitly selected function into the genuine slot b′, and the four-step injection proof remains unchanged apart from this reviewed clarification.

The corresponding scope clarifications in 9.1 and 9.4 also appear in their actual statements and their regenerated CSV rows: “For m≥3…” and “For each fixed m≥3…”.

## 3. Uses lines, dependency table, and construction order

Every proof statement and Definition 2.9 has a Uses line immediately following its environment. Independently parsing the 44 rows of the typeset dependency table gives the same statement identifiers, kinds, and Uses text. The CSV `depends_on` cell equals that text for every proof statement. There are zero discrepancies among these three representations.

For every named result invoked in a Uses line, the referenced statement exists and precedes the current result in the proof order. The program expands same-section ranges before checking them. Definitions and standing data are retained as such: in particular, the Uses line of Lemma 5.3 cites the stipulated switch-upset property (5.3), together with the earlier qualifier/cone results and I1. It introduces no invocation of the later Lemma 6.4. Proposition 7.3 establishes the ancestor-first construction order before invoking 5.3 with the constructed switch upset.

The dependency table's row 8.1 originally still had the inherited placeholder “Unchanged argument: ---”. The assembling agent replaced it with the concrete statement that the same restriction identities use the capacity-dependent carry bound A_m=6m+9, and marked the row changed. The current row agrees with Lemma 8.1's identity and leaf-count proof.

## 4. Source counterpart consistency

Every one of the 44 source-column entries was compared with `code/C_dependency_source_map.json`. The comparison checks the exact displayed source statement number or prose section and, where present, the source's LaTeX label, after removing typesetting-only `allowbreak` commands. All entries match. Each CSV notes cell also contains the corresponding source display, exact locator, and audit note from that concordance.

This includes the corrected prose counterparts for 4.3, 5.4, 6.3, and 8.1; the source's Theorem 3.4 for Q03 Theorem 8.5; Section 9 accounting for Q03 9.2–9.3; and source Remark 9.1 for Q03 9.4. Their primary-source comparison is documented in the S-P source audit. The present check verifies faithful integration of that already recorded comparison into the post and CSV.

## 5. Standing data and domains of the principal results

| Result | Identifiable standing data and exact scope |
|---|---|
| Cited result 1 | m=3, the explicitly listed DAG model immediately preceding it, polynomial deterministic multitape decision, feasible-schedule construction, and optimization; source [P], Theorem 1.1, S-P. |
| Theorem A | One algorithm receives the explicit DAG and binary m≥3,T; n≥1; a schedule is the stated capacity-m map into integer slots. Section 9 specifies the canonical self-delimiting encoding and L. The common bound covers decision, witness construction, and optimization. Its N-only bound starts from the parsed canonical padded graph with 1≤T<n and n≤mT. A(m,K) and G(m) are displayed explicitly in 9.2–9.3. |
| Theorem B | m≥3, padded universe J with |J|=mT, the full-schedule definition in 2.3, and the precise hierarchy definition 2.9. Its global and relative budgets are 12m+25 and 6m+16, with no dependence on depth. |
| Theorem 8.5 | m≥3 is now explicit. J, full schedules, permitted formulas and K_m, and hierarchy clauses have all been defined before this statement. The proof invokes 7.3 and 8.2–8.4 in that established order. |
| Theorem 9.1 | m≥3 is explicit; the actual finite procedure is Section 2's state graph with K=K_m. Acceptance is for the padded J, padding/removal uses 2.3, and the theorem's proof specifies the elementary deadline branches and increasing optimization trials. |
| Proposition 9.2 | m≥3, K≥1, parsed canonically numbered J=[N] with N=mT≥m; one deterministic machine with a fixed number of tapes. B, the numeric state bound, q, h and C are defined before their cost uses. The explicit coefficient A(m,K) bounds the complete padded computation, including its witness. |
| Corollary 9.3 | K_m=12m+25, e_m=60m²+129m+1, explicit input length L with n≤L, N≤mn≤mL, and at most n trials. The resulting exponent is e_m+1=60m²+129m+2, with the displayed coefficient G(m). |
| Proposition 9.4 | Each fixed m≥3; total vertex count n in binary and explicitly listed arc endpoints. The proof defines d, derives n≤N<2m|E| in its expansion branch, and states the decision-output scope. Its last paragraph specifies the zero-makespan convention for the empty instance. |

Proposition 2.8 explicitly states its own wider domain m≥1 and arbitrary description family for the soundness argument. The symbols L,Z,R are local set variables in state triples; L in the complexity formulas is explicitly identified as input length. The notation paragraph also distinguishes the leaf budget K from the indexed entry sets K_j by their definitions.

## 6. Numeric state-bound renaming

The assembly introduced calligraphic S for the numeric state bound and retained S for low cutoffs. The first assembly substituted only isolated occurrences, leaving ordinary S in juxtaposed expressions such as qSN, BS(BN²+N⁴), and 3BS⁴N. That was a genuine notation inconsistency because the new notation paragraph stated the renamed quantity explicitly.

The assembling agent replaced S throughout Section 9's mathematical segments, including juxtaposed products. The current check scans all inline and displayed mathematics in that section, removes the declared calligraphic-S token, and confirms that no plain uppercase S remains. The renaming preserves the explicitly declared value B N^m at every use. Thus its arithmetic products and all eight subroutine bounds continue to denote the same numeric quantities audited in Part A.

## 7. Conclusion of this integration check

The current JSON output reports zero missing/duplicate statement rows, zero statement or dependency mismatches, zero source-counterpart mismatches, zero forward named Uses references, and zero unconverted numeric-state symbols. All 47 CSV rows are present; the reviewed Sections 2–8 and the explicit choice domain in 5.5 pass their comparisons. No mathematical integration correction remains outstanding in this check. PDF compilation and visual review are being recorded separately by the assembling agent.
