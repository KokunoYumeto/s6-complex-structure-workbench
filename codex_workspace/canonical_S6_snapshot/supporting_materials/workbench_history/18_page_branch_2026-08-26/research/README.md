# Live mathematical workstreams

The TeX files are the human-readable notebook. The four JSONL ledgers make its proof state mechanically inspectable:

- `claim_ledger.jsonl` — one status-bearing mathematical claim per line;
- `dependency_ledger.jsonl` — logical-use edges only;
- `morphism_ledger.jsonl` — the maps whose geometric identification is load-bearing;
- `uncertainties.jsonl` — unresolved questions with explicit closure tests.

`VERIFIED` means the stated finite certificate was independently replayed or proved from the displayed hypotheses. `CONDITIONAL` means an explicitly listed upstream claim is still assumed. `OPEN` means neither a proof nor a counterexample is recorded. `REFUTED` applies only to the exact statement named, not automatically to the central theorem.

The frozen manuscript and audit are outside this folder. Never repair their
text in place.  The current topology conclusion is intentionally
`CONDITIONAL`: the exact matrices must first be identified with the actual
geometric maps.  The dated log records every promotion, failed test, and
remaining bridge lemma.

The local SGA comparison layer used the clean cumulative LaTeX editions of
SGA 6 and SGA 7 I. Those third-party files are not bundled. The publication
bibliography supplies portable edition data; machine-specific locators were
removed during consolidation.
