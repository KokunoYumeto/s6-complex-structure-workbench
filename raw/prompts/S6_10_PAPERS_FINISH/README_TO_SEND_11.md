# Finish prompts (18 Nov 2026), written by the main session (Claude Opus 5.5 Max)

The user, 18 Nov 2026 (P6849): [the user's words, omitted]

- `SGA_ES_READERS_FINISH/` (GPT-6 Astra, ChatGPT Pro mode; any account): continues the Spanish SGA readers from the
  earlier run's checkpoint 06 (18 Nov 08:00 UTC, "incomplete": 66,980 of 110,808 French decisions pending; no cumulative
  books, README, PDF check or delivery ZIPs yet). Send all 11 files, no text. Passes push_rule_pro_prompts.py --lint.
  Its checkpoints continue the numbering from 07, so the filer files them with the earlier run.
- `S6_10_PAPERS_FINISH/` (GPT-6 Astra, ChatGPT Pro mode): continues the S6 papers from the earlier run's checkpoint
  06 (18 Nov 07:32 UTC: six papers written; the run "INCOMPLETE solely at the stated final delivery/administrative
  gates"). **Send it on account 2**, where S6_10 ran: the prompt tells the run to fetch checkpoints 02-05 from that
  account's Library (1,187 files, about 80 MB, that checkpoint 06 does not repeat). Send PROMPT.md, the six S6 zips and
  `S6_10_PAPERS_checkpoint_06_restore.tar.xz`, no text. Passes --lint-math and paper_completeness_lint.py.
  For our archive: checkpoints 02-05 of S6_10_PAPERS were never downloaded; they are in account 2's Space.
