# Historical 18-page workbench branch

> **Checkpoint only.** Current mathematical work is in project-root
> `workbench/workbench.tex`, and the consolidated public project is
> <https://www.overleaf.com/read/rtmyqxyrzprn#fa24eb>.

This is a separate, owner-only Overleaf workbench for the mathematical phase
following the proof audit.  It is not the public project and is not a revised
copy of that project.  Sharing controls are deliberately outside this
workflow; the owner may change them separately.

Historical owner project: `https://www.overleaf.com/project/6a8e36c973b98042c96f85ce`

The project was created separately with that distinct ID. Its sharing
controls were neither opened nor changed by this workflow.

## Start here

1. `main.tex` — the short live proof-repair/disproof notebook.
2. `research/` — exact algebra, topology obligations, the Section 10/CDP
   analysis, repairs, dated log, and typed JSONL ledgers.
3. `audit_baseline/annotated_audit.tex` — the frozen self-contained
   121-page annotated audit.
4. `audit_baseline/clean_transcription.tex` — the frozen self-contained
   108-page clean transcription.
5. `comparative_context/` — bounded comparative work on the prior
   Fable/Jacobian certificate; it is methodology only and supplies no S⁶
   lemma.

The notebook keeps exact finite algebra separate from unresolved geometric and
analytic certification.  `VERIFIED` applies only to a proved statement or
replayed finite certificate; `CONDITIONAL` names an implication whose
hypotheses are listed; `OPEN` means no proof or counterexample is recorded;
`REFUTED` applies only to the exact local statement named.  In particular,
the terminal Smith forms do not by themselves prove the topology of $X$.

The current Section 10 work has independently retraced the candidate's smooth
compact analytic construction, proper map, full reduced normal-crossings
fibre, $\mathrm{dP}_6$ normalization, and local canonical trivialization.
Together with the verified conductor construction, compact-Cartier duality,
and top-degree base change, this proves
`R^2 f_*(T_X tensor L) != 0` for every `L in Pic^0(X)` without using the
unresolved global topology.  Extending that argument to every line bundle is
equivalent to the still-open restriction statement
`eta^* i^*: Pic(X) -> Pic(dP6) = 0`; the claimed `H^2(X;Z)=0` would suffice.
The integral topology and final CDP theorem verdict remain open.

## Build in Overleaf

Use pdfLaTeX, the latest TeX Live image, and select root `main.tex` as the main document. The page count of the live notebook may change as the research develops.

To inspect a frozen baseline, temporarily select
`audit_baseline/annotated_audit.tex` or
`audit_baseline/clean_transcription.tex` as the main document. Their expected
page counts are 121 and 108 respectively. Restore root `main.tex` afterward.

## Editing boundary

Do not edit the files in `audit_baseline/`; they are fixed reference artifacts.
Mathematical attempts, counterexamples, and revised lemmas belong in
`research/`, with hypotheses, dependencies, conventions, and source-page
references explicit.  No third-party literature PDFs or local build logs are
bundled; the bibliography gives human-resolvable citations.
