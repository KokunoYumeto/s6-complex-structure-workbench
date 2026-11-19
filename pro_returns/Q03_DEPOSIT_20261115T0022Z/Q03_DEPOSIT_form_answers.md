# Q03_DEPOSIT — deposit form answers

Date: 2026-11-15. Record: Q03. Version: 1.

These answers are prepared for the user’s review. No remote publication or form submission has been performed. The contributor enters their identity and approves the deposit after reviewing the PDF, record, and answers.

## Title

```text
Polynomial-time unit-job scheduling for every fixed number of machines m >= 3
```

## Abstract

The following block is the exact abstract body from the current LaTeX source, including its mathematical notation. Copy it unchanged.

```text
For every fixed $m\geq3$, unit-job scheduling with explicitly listed precedence constraints on $m$ identical machines admits exact deadline decision and optimal-schedule construction in $O_m((L+2)^{60m^2+129m+2})$ deterministic multitape steps; a parsed, padded deadline of size $N=mT$ costs $O_m(N^{60m^2+129m+1})$.
OpenAI proved the three-machine result (2026); drbh supplied four-machine Lean code (2026); Jansen states the fixed-machine result in arXiv:2611.09392 (2026).
This generalization gives a self-contained proof with leaf budget $12m+25$ and an itemized tape-cost derivation, without a priority claim.
A finite dynamic program uses Boolean descriptions; an injection into one boundary slot bounds the lists, and local restriction identities control direction changes.
GPT-6 Astra, ChatGPT Pro mode, produced the proof and the current step-by-step, computational and source audit. Three earlier reports are by Claude Opus 5.5, effort max, Message Batches API. Human understanding: none.
Source-access and archival qualifications are recorded in Limits and open points.
```

## Classification and disclosure fields

| Form field | Answer |
|---|---|
| Primary subject | cs.DS |
| Cross-lists | cs.DM, cs.CC, math.CO, math.OC |
| MSC codes | 90B35, 68Q25, 68W40, 06A07 |
| Text origin | primarily AI-generated (`no-human-author-claimed`) |
| Human understanding | none |
| Formalizations | Leave the links field empty. none for this proof. |
| Licence | CC0 1.0 (`CC0-1.0`) |
| Contributor | Entered by the human contributor at deposit. |

## Tags

- scheduling
- precedence constraints
- unit jobs
- identical machines
- makespan
- fixed number of machines
- polynomial-time algorithm
- dynamic programming
- partially ordered sets

## Tools

- GPT-6 Astra, ChatGPT Pro mode
- Claude Opus 5.5, effort max
- Claude Opus 5.5, effort max, Message Batches API
- Claude Opus 5.5, effort not recorded
- Claude Fable 5.2, effort high
- pandoc 3.9.0.2
- Python 3
- pdfLaTeX

## Provenance statement

The following text reproduces the post’s Provenance and Declarations sections, with prose formatting and reference labels rendered as plain text.

```text
Provenance

- The question is attributed in the supplied records to Claude Opus 5.5, effort not recorded, 22 October 2026. The supplied prompt is preserved at anc/ai-provenance/Q03_PROMPT.txt; the manifest discrepancy is specified above. The present audit request, attributed to Claude Opus 5.5, effort max, is anc/Q03_DEPOSIT_prompt.md.

- The proof return is attributed to GPT-6 Astra, ChatGPT Pro mode, 23 October 2026. Its preserved file anc/ai-provenance/Q03-solution.md has 94,789 bytes and SHA-256 3ebeb452d6f461c23b4f8fa6f04ba6ed15abac541b5d2562fa814ba77977e60c. The three supplied reports remain unchanged in the same directory.

- The 14 November format text was assembled by Claude Fable 5.2, effort high, using pandoc 3.9.0.2 for the Markdown-to-LaTeX conversion. Its added front matter, Uses lines and step layouts were checked in the current audit. The statement numbering is preserved. The present editor/checker is GPT-6 Astra, ChatGPT Pro mode.

- Current edits: explicit input encoding and coefficients; complete Section 9 accounting and exponent correction; numbered proof steps and direct dependencies; explicit choice domain in Lemma 5.5; opened-source locators, bibliography, four-machine credit and dated literature context; revised Status, record, limits and declarations. A complete edit ledger and statement CSV accompany this file.

- Register: supplied row Q03 of REVIEW_REGISTER_PRO_RESULTS_20261114. Course lessons 9–11 [L, dated 24 October 2026] describe the return. The anc/ files are provided as ancillary deposit material; no external publication was made by this audit.

Declarations

- AI use. Question: Claude Opus 5.5, effort not recorded. Present audit request: Claude Opus 5.5, effort max. Proof return: GPT-6 Astra, ChatGPT Pro mode. Three earlier reports: Claude Opus 5.5, effort max, Message Batches API. Format text: Claude Fable 5.2, effort high. Current mathematical, computational, source and typesetting checks, and editing: GPT-6 Astra, ChatGPT Pro mode.

- Status. Kind: generalization. Claim: proved. Current text: F, D, C, S by GPT-6 Astra, ChatGPT Pro mode, 15 November 2026; verdict: proved as stated. Human understanding: none. Formalization: none for this proof. No mathematical gap found in Sections 2–9; source-access and archival qualifications are listed above.

- Credits. OpenAI [P, Sections 2–9] supplied the three-machine construction. drbh [D, commit bbd3013] supplied the earlier four-machine adaptation and full release-theorem code. The classical authors and the other opened works are credited in the references. No human authorship of this proof and no priority are claimed.

- Licence and version. CC0 1.0 for this post. Rights in cited works remain with their authors. Version 1 incorporates the cost derivation, proof and source audit, credit corrections and format verification described above.
```

## Comments

```text
Current text audited F,D,C,S by GPT-6 Astra, ChatGPT Pro mode; cost exponent corrected to 60m^2+129m+2. Source-access and archival qualifications stated. No human proof check or formalization of this text. No novelty/priority claim.
```

## Supplementary files

The requested delivery is one ZIP. Its ancillary files for the deposit are:

- `anc/ai-provenance/Q03_PROMPT.txt` — supplied original prompt, preserved verbatim.
- `anc/Q03_DEPOSIT_prompt.md` — the present audit request.
- `anc/ai-provenance/Q03-solution.md` — supplied proof return.
- `anc/ai-provenance/Q03-check.md` — supplied referee report.
- `anc/ai-provenance/Q03-b-check-b.md` — supplied referee report.
- `anc/ai-provenance/Q03-c-check-c.md` — supplied referee report.
- `code/` — reproducible audit and verification programs, with their outputs.
- `Q03_DEPOSIT_report.md`, `Q03_DEPOSIT_results.csv`, `Q03_DEPOSIT_sources.md`, and `Q03_DEPOSIT_literature.md` — the current mathematical, computational, source, and literature records.

Public repository status, exactly as recorded: ancillary files supplied with this deposit package; no external publication by this audit.

## Model and effort provenance by role

| Role | Model or tool | Effort / execution setting | Date |
|---|---|---|---|
| question | Claude Opus 5.5 | effort not recorded | 2026-10-22 |
| proof return | GPT-6 Astra | ChatGPT Pro mode | 2026-10-23 |
| format text | Claude Fable 5.2 | high | 2026-11-14 |
| conversion | pandoc 3.9.0.2 | software version as listed | 2026-11-14 |
| deposit-task author | Claude Opus 5.5 | max | 2026-11-15 |
| current audit and editing | GPT-6 Astra | ChatGPT Pro mode | 2026-11-15 |
| Prior report H1 | Claude Opus 5.5 | max, Message Batches API | 2026-10-23 |
| Prior report H2 | Claude Opus 5.5 | max, Message Batches API | 2026-10-23 |
| Prior report H3 | Claude Opus 5.5 | max, Message Batches API | 2026-10-23 |

The prior question and the present audit request have separate effort records. The supplied reports record the Message Batches API mode; no API mode is assigned to the present request’s author beyond the supplied metadata.

## Recorded status and qualifications

- Kind: generalization.
- Claim: proved.
- External results: none load-bearing.
- Current check: F,D,C,S; GPT-6 Astra (OpenAI), ChatGPT Pro mode; 2026-11-15; proved as stated.

### Open points / retained qualifications

- No mathematical gap found in Sections 2-9. The three original cost/source audit items are addressed by the recorded checks.
- Original FKN 1969 full text unavailable; publisher metadata/abstract and 1971 erratum opened.
- Course provenance.json endpoint returned HTTP 404; first-publication dates are unverified.
- Supplied original prompt is 9551 bytes; historical manifest lists an absent 9383-byte variant with a different hash. Supplied prompt preserved verbatim.
- Historical run dates, API mode and independence are supplied-record metadata; raw API logs absent.
- OpenAI/drbh Lean builds and Jansen/Giraudin full proofs were not independently replayed or audited; their declared scope was checked.

### Not claimed

- a bound polynomial in m
- a practical algorithm
- release dates, individual deadlines, unequal machine speeds or unequal job lengths
- formalization of this proof
- novelty or priority
- optimality of the displayed exponent

### Literature record

- Date: 2026-11-15.
- Scope: arXiv; STOC, FOCS, SODA, ICALP, IPCO, ESA, APPROX; authors pages; GitHub; general web; Hexagon; title/citation searches for the OpenAI preprint.
- Outcome: found drbh four-machine code, Jansen all-fixed-m theorem statement and linear budgets, Giraudin three-machine exponent statement; no fixed-m>=4 hardness result located; no priority claim.

## Form-limit checks

| Field | Characters or entries | Limit |
|---|---:|---:|
| title | 77 | 240 |
| abstract | 1080 | 8000 |
| provenance_statement | 2868 | 12000 |
| comments | 232 | 2000 |
| cross_lists | 4 | 8 |
| msc | 4 | 5 |
| tags | 9 | 12 |
| tools | 8 | 10 |

## Machine-readable record

The following is the post’s complete opening record, with only the LaTeX comment prefixes removed. Its values are identical to `work/record.json`.

```yaml
format: "hexagon-post-format/1"
record_id: "Q03"
version: 1
date: "2026-11-15"
title: "Polynomial-time unit-job scheduling for every fixed number of machines m >= 3"
kind: "generalization"
claim_status: "proved"
statement_plain: "For every fixed integer m >= 3, explicitly listed unit jobs with arbitrary acyclic precedence on m identical machines admit exact deadline decision, witness construction and optimum construction in at most G(m)(L+2)^(60m^2+129m+2) deterministic fixed-multitape steps. A parsed canonical padded deadline with N=mT jobs uses at most A(m,12m+25)N^(60m^2+129m+1) steps. The description hierarchy has 12m+25 global leaves and 6m+16 relative-prefix leaves."
statement_tex: "For each fixed $m\\geq3$, $Pm\\mid\\mathrm{prec},p_j=1\\mid C_{\\max}$ is solvable in deterministic multitape time $O_m((L+2)^{60m^2+129m+2})$; a parsed padded deadline uses $O_m(N^{60m^2+129m+1})$ steps, $N=mT$."
extends: "OpenAI, preprint of 24 September 2026, Theorem 1.1 (three machines); all steps are proved here."
known_before: "Two machines: Fujii-Kasami-Ninomiya with erratum, Coffman-Graham; variable-machine NP-completeness: Ullman; three machines: OpenAI; four-machine theorem code: drbh bbd3013; all-fixed-m theorem and linear budgets stated by Jansen arXiv:2611.09392v1."
new_here: "Self-contained audited capacity-m proof and itemized costs of the supplied Q03 construction; no novelty or priority claim."
main_statements: ["Theorem A = Theorem 1.1 of the supplied return, established in 9.1-9.3", "Theorem B = Theorem 8.5"]
statements_in_proof: 44
hard_step: "Lemma 5.5; Lemmas 6.2 and 6.5; Lemma 7.1; Lemma 8.4"
external_results: "none load-bearing"
produced_by: [{"role": "question", "model": "Claude Opus 5.5", "effort": "effort not recorded", "date": "2026-10-22"}, {"role": "proof return", "model": "GPT-6 Astra", "effort": "ChatGPT Pro mode", "date": "2026-10-23"}, {"role": "format text", "model": "Claude Fable 5.2", "effort": "high", "date": "2026-11-14"}, {"role": "conversion", "tool": "pandoc 3.9.0.2", "date": "2026-11-14"}, {"role": "deposit-task author", "model": "Claude Opus 5.5", "effort": "max", "date": "2026-11-15"}, {"role": "current audit and editing", "model": "GPT-6 Astra", "effort": "ChatGPT Pro mode", "date": "2026-11-15"}]
checks: [{"id": "H1", "by": "Claude Opus 5.5", "effort": "max, Message Batches API", "date": "2026-10-23", "type": "F,D", "scope": "supplied return", "verdict": "proved with fixable gaps"}, {"id": "H2", "by": "Claude Opus 5.5", "effort": "max, Message Batches API", "date": "2026-10-23", "type": "D", "scope": "supplied return", "verdict": "proved as stated"}, {"id": "H3", "by": "Claude Opus 5.5", "effort": "max, Message Batches API", "date": "2026-10-23", "type": "F", "scope": "supplied return", "verdict": "proved as stated"}]
checks_of_this_text: [{"by": "GPT-6 Astra (OpenAI)", "effort": "ChatGPT Pro mode", "date": "2026-11-15", "type": "F,D,C,S", "scope": "all 44 numbered statements in Sections 2-9; main theorems; rewritten proofs; costs; source attribution; finite checks; post consistency", "verdict": "proved as stated", "limits": "S-FKN original full text unavailable; S-L archival endpoint 404; historical prompt manifest discrepancy; no independent Lean build"}]
human_understanding: "none"
text_origin: "primarily AI-generated"
formalization: "none for this proof"
open_points: ["No mathematical gap found in Sections 2-9. The three original cost/source audit items are addressed by the recorded checks.", "Original FKN 1969 full text unavailable; publisher metadata/abstract and 1971 erratum opened.", "Course provenance.json endpoint returned HTTP 404; first-publication dates are unverified.", "Supplied original prompt is 9551 bytes; historical manifest lists an absent 9383-byte variant with a different hash. Supplied prompt preserved verbatim.", "Historical run dates, API mode and independence are supplied-record metadata; raw API logs absent.", "OpenAI/drbh Lean builds and Jansen/Giraudin full proofs were not independently replayed or audited; their declared scope was checked."]
not_claimed: ["a bound polynomial in m", "a practical algorithm", "release dates, individual deadlines, unequal machine speeds or unequal job lengths", "formalization of this proof", "novelty or priority", "optimality of the displayed exponent"]
literature_search: {"date": "2026-11-15", "scope": "arXiv; STOC, FOCS, SODA, ICALP, IPCO, ESA, APPROX; authors pages; GitHub; general web; Hexagon; title/citation searches for the OpenAI preprint", "outcome": "found drbh four-machine code, Jansen all-fixed-m theorem statement and linear budgets, Giraudin three-machine exponent statement; no fixed-m>=4 hardness result located; no priority claim"}
licence: "CC0-1.0"
provenance: {"prompt": "anc/ai-provenance/Q03_PROMPT.txt", "current_request": "anc/Q03_DEPOSIT_prompt.md", "return": "anc/ai-provenance/Q03-solution.md", "return_sha256": "3ebeb452d6f461c23b4f8fa6f04ba6ed15abac541b5d2562fa814ba77977e60c", "reports": ["anc/ai-provenance/Q03-check.md", "anc/ai-provenance/Q03-b-check-b.md", "anc/ai-provenance/Q03-c-check-c.md"], "current_report": "Q03_DEPOSIT_report.md", "repository": "ancillary files supplied with this deposit package; no external publication by this audit"}
hexagon: {"subject": "cs.DS", "cross_lists": ["cs.DM", "cs.CC", "math.CO", "math.OC"], "msc": ["90B35", "68Q25", "68W40", "06A07"], "tags": ["scheduling", "precedence constraints", "unit jobs", "identical machines", "makespan", "fixed number of machines", "polynomial-time algorithm", "dynamic programming", "partially ordered sets"], "tools": ["GPT-6 Astra, ChatGPT Pro mode", "Claude Opus 5.5, effort max", "Claude Opus 5.5, effort max, Message Batches API", "Claude Opus 5.5, effort not recorded", "Claude Fable 5.2, effort high", "pandoc 3.9.0.2", "Python 3", "pdfLaTeX"], "comments": "Current text audited F,D,C,S by GPT-6 Astra, ChatGPT Pro mode; cost exponent corrected to 60m^2+129m+2. Source-access and archival qualifications stated. No human proof check or formalization of this text. No novelty/priority claim.", "provenance_statement": "See the Provenance and Declarations parts of the post, reproduced in the accompanying form answers."}
```
