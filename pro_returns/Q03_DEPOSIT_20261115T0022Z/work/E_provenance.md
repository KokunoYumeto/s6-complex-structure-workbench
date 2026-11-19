# E: provenance, preservation, and ancillary-file audit

Audit date: 15 November 2026 (Europe/Berlin). Auditor: GPT-6 Astra, effort ChatGPT Pro mode.

## Findings

The supplied return is preserved byte for byte and has the requested SHA-256. The three supplied reports have the stated model/effort headings and the stated verdicts. Their mathematical scope is the original answer: its structural proof and finite-search argument, with comments on the earlier runtime sketch and on unverified source claims. They do not document an S-type source comparison or a C-type execution of the attached code. This audit of the supplied records does not turn those older reads into checks of the revised post.

The dates, Message Batches API mode, and description of the three reports as independent runs on the same input are expressly supplied in the present task and in the original post/register. The report files themselves contain no execution timestamps or API request logs. Preserve this information as supplied provenance metadata. The numerical assertion “47,788 input tokens each” and the assertion that no run saw another report occur only in the original post's Independence paragraph; no underlying logs are included. They add nothing needed to assess the theorem and should be omitted from the revised concise record, or explicitly identified as assertions of the supplied post.

One exact provenance discrepancy remains: the supplied `Q03_PROMPT.txt` has 9,551 bytes and SHA-256 `792b1a676ab01162d40d78ac73440d5a0dbe5e31b626cac398bcb882358fa54a`; the old artifact manifest instead records an `inputs/PROMPT.txt` of 9,383 bytes and SHA-256 `41db4774893d4ee075889202411db254e3884a111734b07d6959c5670faec13b`. That particular manifest-listed file is absent from the supplied background. The task identifies `Q03_PROMPT.txt` as its supplied prompt as sent; it is preserved unchanged under that description. Its byte identity to the different manifest entry has not been established. This is a version-history qualification, with no use in the proof.

No genuine machine-local absolute path, private contributor identity, email address, private key, or credential was found in the six mandatory ancillary files. Public bibliographic author names and the source URLs remain as required credits. The automated Windows-drive heuristic produced two matches on TeX function notation `f:\mathscr`; inspection establishes the exact mathematical context, so neither is a filesystem path. No ancillary bytes were altered.

## 1. Records opened, with exact locators

| Record | Locator | What it supports | Qualification |
|---|---|---|---|
| `provenance/Q03_PROMPT.txt` | Lines 1–2; task paragraphs 0–4, lines 7–61 | Original task Q03, internally dated 22 October 2026; explicit scheduling model, all-machine extension request, proof/source and deliverable requirements | The file does not name the question-writing model or its effort. Those fields come from the supplied post. |
| `provenance/Q03-solution.md` | Title and date, lines 1–4; mathematical sections 2–9; bibliography and Further consequences | Return internally dated 23 October 2026, with the original statement numbering and +8 input bound | Model/effort credit is supplied by the current task and original post, rather than a model-signature field in this return. |
| `provenance/artifacts/MANIFEST.json` | `files` entry `Q03-solution.md`, lines 5–8 | Return length 94,789 and SHA-256 `3ebeb452d6f461c23b4f8fa6f04ba6ed15abac541b5d2562fa814ba77977e60c` | Recomputed hash matches both attached copies and the ancillary copy. |
| Same manifest | `files` entry `inputs/PROMPT.txt`, lines 60–63 | A recorded 9,383-byte input prompt, hash `41db4774893d4ee075889202411db254e3884a111734b07d6959c5670faec13b` | That file is absent; the supplied 9,551-byte `Q03_PROMPT.txt` has a different hash. |
| `provenance/reports/Q03-check.md` | Header, line 1; Verdict, lines 3–4; Check of the argument, lines 21–85; External results used, lines 87–95 | Claude Opus 5.5, effort max; “PROVED WITH FIXABLE GAPS”; structural steps followed and re-derived, input exponent gap, source claims unverified | No report date or API invocation metadata inside the report; no source or code execution certification. |
| `provenance/reports/Q03-b-check-b.md` | Header, line 1; Verdict, lines 3–4; Minor issues M1–M3, lines 88–98; External results, lines 101–108 | Claude Opus 5.5, effort max; “PROVED AS STATED”; expressly says structural steps were re-derived; flags runtime itemization and source correspondence | No report date or API invocation metadata inside the report. Its bibliographic wording includes reliance on recall; retain no S-type classification. |
| `provenance/reports/Q03-c-check-c.md` | Header, line 1; Verdict, lines 3–4; §9, lines 78–81; §11, line 83; External results, lines 85–92 | Claude Opus 5.5, effort max; “PROVED AS STATED”; key proof steps followed; input exponent informal; code unavailable to inspect; sources not checked | The explicit “code was not available to inspect” excludes a C-type run for this report. |
| `register/REVIEW_REGISTER_row_Q03.md` | Dated heading, line 1; Q03 row, line 5 | Register snapshot of 14 November 2026; three Opus-max verdicts dated 23 October; separate lesson-chain activity dated 24 October | Cost estimates and later lesson checks are recorded assertions. Their underlying session files are not supplied. |
| Present task, `anc/Q03_DEPOSIT_prompt.md` | Lines 3, 9, 28, 57, 97, 111 | Current task written 15 November 2026 by Claude Opus 5.5, effort max; return by GPT-6 Astra in ChatGPT Pro mode; three report dates/API/independent-input description; Fable effort high for the two proof layouts; current audit attribution | These are the user's supplied provenance statements. No broader authentication claim is made. |
| Original post | POST-RECORD lines 25–34 | Question model effort not recorded; proof model ChatGPT Pro mode; Fable effort high; prior classifications F,D / D / F | Preserve the exact attribution, while updating the record for the present revision. |
| Original post | Independence paragraph, lines 1523–1525 | Separate runs, same input, claimed 47,788 input tokens per run, no cross-report exposure | No supporting raw batch log is supplied. Prefer concise attributed wording without the numerical token claim. |
| Original post | Checks of other texts, lines 1528–1531; Provenance, lines 1563–1564 | The post records additional lesson writing/checking sessions and public lessons 9–11 | Do not count these as checks of the revised post. Source verification of the public lessons is recorded separately in the source audit. |
| Original post | Provenance, lines 1548–1562; Declarations, lines 1571–1578 | Question, proof, original conversion and layout attribution; human-understanding/formalization declarations; prior-work credits | The present revision must name GPT-6 Astra, effort ChatGPT Pro mode, as its reviser/checker as well. |

## 2. Exact preservation checks

The six files below were compared to the supplied originals. All copies match. Public filenames in this table are relative to the final package.

| File | Bytes | SHA-256 |
|---|---:|---|
| `anc/Q03_DEPOSIT_prompt.md` | 17,129 | `aa9d96d9e3a4125df1dc9151f5cf69de6580ce79c99208a7bc48df0dad5bb706` |
| `anc/ai-provenance/Q03_PROMPT.txt` | 9,551 | `792b1a676ab01162d40d78ac73440d5a0dbe5e31b626cac398bcb882358fa54a` |
| `anc/ai-provenance/Q03-solution.md` | 94,789 | `3ebeb452d6f461c23b4f8fa6f04ba6ed15abac541b5d2562fa814ba77977e60c` |
| `anc/ai-provenance/Q03-check.md` | 8,900 | `0ce501f1241a87fcffe637657effbceb84b487bf20021b2dc95fa1a465f06079` |
| `anc/ai-provenance/Q03-b-check-b.md` | 10,676 | `15ea0b95e4b23f68bb0b50a2eda1d08cae99793cf3ce46a9e15b5a5c95071b2a` |
| `anc/ai-provenance/Q03-c-check-c.md` | 10,207 | `e1a821b14067ec136f80b6c6e0e2705dc04ffe84d28a4c7f15564de12bbdb30b` |

The original return copy in `provenance/artifacts/Q03-solution.md` is also 94,789 bytes with the same hash. Thus the map from either supplied return copy to the published ancillary copy is the identity on every byte. The dated original proof, including its superseded +8 input exponent and historical source claims, remains preserved as provenance; corrected assertions belong in the revised post and report.

### Prompt-manifest discrepancy: exact transformations tested

The supplied prompt is ASCII with 61 LF bytes and no CR or CRLF. The following exact byte maps were computed without changing the preserved file:

| Map | Output bytes | Matches old manifest? |
|---|---:|---|
| Identity | 9,551 | No |
| Replace every CRLF by LF | 9,551; identical to input | No |
| Replace each LF by CRLF after CRLF-to-LF replacement | 9,612 | No |
| Remove an initial UTF-8 BOM | 9,551; identical to input | No |
| Remove all terminal CR/LF bytes | 9,550 | No |

All output hashes are in `code/E_verify_provenance.out`. None equals the old manifest's hash, so no reconstruction of the absent file is asserted or created. The next evidence needed to resolve this version question is the original manifest-listed `inputs/PROMPT.txt` or its enclosing original artifact archive. That uncertainty changes no theorem premise or cost bound.

## 3. Check types and scopes to carry into the post

Use the three original report verdicts verbatim, alongside their stated findings:

1. **Claude Opus 5.5, effort max, Message Batches API; 23 October 2026; F,D.** Original answer: structural and dynamic-program proof checked; verdict **proved with fixable gaps**. Findings: input exponent not derived and source claims unverified.
2. **Claude Opus 5.5, effort max, Message Batches API; 23 October 2026; D.** Original answer: structural steps expressly re-derived; verdict **proved as stated**. Findings M1–M3: input exponent, subroutine itemization, and source correspondence needed further work.
3. **Claude Opus 5.5, effort max, Message Batches API; 23 October 2026; F.** Original answer: key proof steps checked one by one; verdict **proved as stated**. Findings: informal input exponent and unchecked bibliography; code not available to inspect.

For all three, dates and API mode are the supplied task/register metadata. The files' headings independently support model/effort and their Verdict sections support the exact verdict words. The numerical number of original runs is three because three distinct report files are supplied. The task describes them as independent runs on the same input; preserve that description with an attribution to the supplied provenance, without implying independently authenticated execution logs.

The current check must be a separate record for **GPT-6 Astra, effort ChatGPT Pro mode, 15 November 2026**, with the actual F,D,S scopes and verdict reached by the root audit. Its C-type computations, where listed, are the actual rerun/new programs and outputs. The current source-opening checks have their own precise source/version/locator rows. There is no formalization of the present general-m proof in this work, and no human check has been performed in this session.

## 4. Recommended concise provenance and record wording

### Provenance prose

> The original task is dated 22 October 2026. The supplied post attributes it to Claude Opus 5.5, effort not recorded. The 23 October return is attributed in the supplied task to GPT-6 Astra, effort ChatGPT Pro mode. Its preserved ancillary copy has SHA-256 `3ebeb452d6f461c23b4f8fa6f04ba6ed15abac541b5d2562fa814ba77977e60c`. The three supplied Claude Opus 5.5 reports, effort max, have verdicts “proved with fixable gaps”, “proved as stated”, and “proved as stated”; the task/register date them 23 October 2026 and describe independent Message Batches API runs on the same input. Claude Fable 5.2, effort high, assembled the 14 November post and the numbered layouts of Lemmas 3.3 and 5.5. GPT-6 Astra, effort ChatGPT Pro mode, audited and revised this text on 15 November 2026. The supplied prompt and all returns/reports are preserved unchanged in `anc/`; the prompt-file discrepancy described in Limits concerns the older artifact manifest.

### Metadata fields requiring precise wording

- `produced_by` includes original question / proof / 14 November assembly, plus current deposit-task author (Claude Opus 5.5, effort max) and current reviser/checker (GPT-6 Astra, effort ChatGPT Pro mode).
- `checks` retains the three original exact verdicts and marks their scope as the original answer.
- `checks_of_this_text` is a new current-date entry with the complete revised-text audit scope and its actual verdict.
- Independence wording: **“The supplied task describes the three prior reports as independent runs of the same model on the same input; raw execution logs were not supplied.”**
- Prompt provenance wording: **“Supplied original-task text preserved unchanged; byte identity to the different `inputs/PROMPT.txt` entry of the old artifact manifest is unverified.”**
- Historical lesson checks may be mentioned as supplied-register history; they must not enlarge the count of proof checks of this text.
- Human understanding remains **none** as the supplied declaration; no human checking is added by this audit. Formalization remains **none** for the present general-m theorem.

## 5. Ancillary privacy and reproducibility check

`code/E_verify_provenance.py` verifies all six byte hashes and screens the text for absolute Unix paths, home-relative paths, file URIs, possible Windows drives, credential patterns, private-key markers, and email addresses. Its complete output is `code/E_verify_provenance.out`. It reports six preserved copies, two manually resolved TeX false positives, zero actual local paths, and zero observed credentials. Manual reading found only public bibliographic names and source credits, with no private contributor identity added.

The scan is reported as a finite inspection of these exact files. It does not authenticate old API sessions and does not imply that a regex can decide every possible privacy question. No credentials or suspected credential strings are echoed by its output. The original files were neither normalized nor redacted.

## 6. Section 9 layout update

`work/A_replacement.tex` now contains 20 numbered `\step` headings across the proofs of 9.1–9.4. Each heading states its step's claim and names its dependencies in brackets. The mathematics and exponents of the previous accounting are preserved. Proposition 9.4's stronger explicit-output sentence now has a concrete family: fixed m, n=2^k independent jobs, T=n, and an empty arc list. Its compact input has O(k) bits; every literal schedule lists all 2^k jobs and has at least 2^k output symbols.
