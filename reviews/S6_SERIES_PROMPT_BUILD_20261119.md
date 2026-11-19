# S6_SERIES_GRIND: the consolidated S6 prompt, as built (19 Nov 2026)

Built by Claude Opus 5.5 at effort max (agent a1704602), 19 Nov 2026, about 19:35 UTC, at the main session's request.
It carries out the user's decision of about 18:2x UTC.

- **The prompt** is for GPT-6 Astra (ChatGPT Pro mode). It is not sent; the user sends it.
- **Send folder:** `TO_SEND/PRO/9_S6_papers/05_S6_SERIES_GRIND/`: `PROMPT.md` (34,520 bytes) and one flat ZIP,
  `S6_SERIES_GRIND.zip`.
- **Build folder:** `s6_pro_prompts_20261112_work/S6_SERIES_GRIND_build/`: the prompt as written, the six component
  ZIPs with their manifests, and `build_components.py`, which rebuilds them.

## What the prompt asks

The target is the five papers of the split, in the standardized form of `S6_SERIES_DESIGN_20261119.md`.
- **The form:**
  - the first ~20 pages (abstract, table of contents, §1 with lettered main theorems at rung 0, their outline proofs,
    known and new, a one-page methodology, the organization);
  - the body by the mathematics;
  - a final part for results not yet established;
  - tags, uses lines, back-links, links across papers, and check files per paper.
- **Every result integrated:** the corrections and findings since cp15, the night run's last rows, and the open rows
  attacked under the push rule.
- **Checked to confidence,** with no count: independent methods aimed at the error-prone points, and each main
  theorem's check entry saying how we know it and what risk remains.

**The split** is section 3 of the prompt, one paragraph headed "THE SPLIT", for editing before sending:
- VI into II;
- III §6 into V.

To keep six papers, replace that paragraph with: "The series has six papers, one per S6_10 paper (I to VI), each on its
own topic; Paper II cites Paper VI for the sign theorem in general." Then change "five" to "six" in sections 1, 4.1,
"Done" and "What to deliver" (`_I` to `_VI`).

## Account independence and resuming

- **No account dependence.** No Library, Space, project or account is named, except in the instruction not to search
  any of them.
- **The same PROMPT.md resends from any account.** With `S6_SERIES_GRIND_checkpoint_NN.zip` attached, the run restores
  from it and the base ZIP, verifies the file list, reads the ledger and the report, and continues with checkpoint
  NN+1.
- **Checkpoints:**
  - one fixed tag (`S6_SERIES_GRIND_checkpoint_NN.zip`; the final ZIP is `S6_SERIES_GRIND_final.zip`);
  - every 45 minutes and at no other time;
  - lean: earlier checkpoints are not copied in;
  - self-contained apart from the base ZIP, so one checkpoint suffices to resume;
  - under 500 MB, in parts if needed.

## The ZIP

`S6_SERIES_GRIND.zip`: 25,962,053 bytes, 956 members, 120 MB unpacked. The integrity test passes, and no file in it
carries the user's name or a local path (checked by script).

| Folder | Files | Packed | What |
|---|---:|---:|---|
| `S6_GRIND_1_papers_cp15/` | 19 | 7.65 MB | the six S6_10 cp15 papers (standalone TeX) with `preamble.tex`, the inventory, `CHECK_EVENTS.tsv` (6,492 events), the notation sheet, the bibliography, the report, `PROGRESS_LEDGER.md`, and the final gate tables |
| `S6_GRIND_2_checks_and_plan/` | 42 | 0.19 MB | the series design, the readiness report and the deposit prep (corrected); the consistency import list and its scripts; the cp36 intake with its events and scripts; the S6_10 cp06 intake with its events and code; the S6_09 intake; sweep 1 (all files); the check ledger and summary; KEEP_SKETCH and LAYOUT_DESIGN; the Paper V check-record and link example |
| `S6_GRIND_3_night_run_cp36/` | 3 | 0.17 MB | the night run's register (299 rows), report and literature log at cp36 |
| `S6_GRIND_4_s6_09_compendium/` | 17 | 8.17 MB | the three S6_09 papers (TeX, .aux and .bbl), their inventory, notation sheet and report |
| `S6_GRIND_5_research_runs_tex/` | 781 | 5.44 MB | the research runs' TeX, results tables and reports (as in the last S6 prompt) |
| `S6_GRIND_6_literature/` | 88 | 4.06 MB | the literature's LaTeX sources, Duke-Imamoglu as a PDF, [AC26] as published and our transcription (as in the last S6 prompt) |
| top level | 6 | 0.05 MB | one manifest per folder (path, size, SHA-256) |

Our own notes and scripts (folder 2) were scrubbed as for GitHub: no name, local path, e-mail address or quotation of
the user.

## Lint results

- `push_rule_pro_prompts.py --lint-math`: 0 failing. Checked on the build copy and on the packed `PROMPT.md`.
- `paper_completeness_lint.py`: ok, on both.
- The required house paragraphs are present:
  - the push rule;
  - the progress check with the dated ledger, "Movement means only" and "two consecutive reviews";
  - the checkpoint rule (every 45 minutes, never a JSON file);
  - the failure clause, with no in-conversation fallback;
  - the lean-checkpoint sentence;
  - the CHECK_EVENTS paragraph;
  - "known results are cited".

No file was edited in place on a hard link: the send folder got copies, and pack_one_zip replaced them.

## Left out, and why

**S6_10 checkpoint 15:**
- `code/` (816 MB) and `analysis/` (103 MB): the run's programs and check receipts. They are provenance, on GitHub at
  the cp15 commit. The prompt asks for new, independent code.
- `records/` (2.2 MB): already merged into `CHECK_EVENTS.tsv`.
- `papers/` (25 MB): the source folders, which the standalone TeX files duplicate.
- The PDFs: the LaTeX is attached.

**The night run's cp36 shards** (5.0 GB, in the run's own codecs): its notes and programs.
- The papers print the proof of every row they carry, including P3K.75 and P3K.109-P3K.119 in Paper IV's final part.
- P1.6 and P1.14 rest on Wall's classification and Kramer-Stolz, already the inputs of Paper V's F.4.1. P5.7's statement
  is in the inventory.
- GitHub holds the night run up to cp35. cp36 itself still waits for the filer (the -data repository).

**Other material:**
- The research runs' code (23 MB in the last S6 prompt): independent computation means new code; provenance on GitHub.
- The S6_09 PDFs and logs, and the S6_10 restore archive of the last prompt (122 MB): superseded by cp15.
- The Hexagon post format: replaced by the series design.
- The Paper V deposit copy (TeX): replaced by the design's check files. Its scripts and records are included as the
  example.

## For the main session

- **The filer** (`github_backup_20261113/file_and_push_auto.py`) does not yet know the run `S6_SERIES_GRIND`. Its
  checkpoints and final will need an entry in `RUNS`, pointing at the prompt as sent, before the watcher files them.
- **S6_10_PAPERS has ended at cp15.** This prompt replaces its FINISH prompt for all further S6 writing.
