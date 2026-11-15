THE MATERIAL YOU ARE GIVEN
- **The workbench** (`workbench/*.tex`): the side lanes of a research workbench on the complex structures on S^6, AI-produced by GPT-5.6 Sol and GPT-6 Astra in Codex between 24 August and 6 September 2026, reviewed only by other AI sessions. Its status words (VERIFIED, OPEN) are its own. The titles of these files ("Koide", "ES-Niemeier", "S6 bridge") come from the way the lanes arose; the survey found no mathematical map from either lane to the complex threefold, and nothing in this prompt depends on one.
- **The survey** (`S6_SURVEY_20261112.md`, entries F31 and F32) and the readers' notes (`notes/D1_notes.md`, `notes/D2_notes.md`, with their programs in `notes/scripts/`): a reading made on 12 November 2026 by Claude (Anthropic, Fable 5.2). The Leads above come from it. Nobody has checked the notes.
- **The papers** (`papers/`): Lekkas and Petridis, arXiv:2509.12902; Voskou, arXiv:2407.03134; Chenevier and Lannes, arXiv:1409.7616. `MANIFEST.tsv` lists every file of the zip with its origin and the reason it is attached.

RULES OF PROOF (they bind every statement you deliver)
1. State the actual claim with all its data: which quadratic form, which lattice or arithmetic group (and which finite-index subgroup), which region, which height, which normalization of measures and of main terms; for lattices, which glue code, which Weyl vector, which neighbour. Do not replace it by a convenient special case; if you prove a special case, name it as one and keep the general statement on your list as open.
2. Type every map: source, target, and each property you use (isometry, integral, Γ-equivariant, a bijection onto which set).
3. Every reduction (a change of coordinates, passing to a finite-index subgroup, smoothing a sharp cutoff, replacing a sector by an arc) comes with its comparison map and a proof that the exact property needed transfers, with the error it costs.
4. "Up to" names the ambiguity: equality, isometry, conjugacy in which group, an asymptotic with which error term, uniform in which parameters.
5. Check the boundary cases: points on the walls of the region, the Pell families, small heights, the primes 2 and 3, elements of finite order in the arithmetic group.
6. A counterexample is given completely and checked by a program whose code and output you attach. One verified counterexample refutes the statement: say "false", and then find the strongest true statement in its place and prove it.
7. No authority. The assertions of the workbench, of the survey and its readers' notes, and the Leads of this prompt are all to be proved or refuted by you. The papers with human authors may be used with exact theorem numbers, after you have read the statement and verified its hypotheses for the case at hand.
8. Never invent a reference; mark each entry of the bibliography `verified` (you opened it) or `unverified`. Before calling anything new, search the literature and say what you searched.
9. What you cannot settle stays on the page as an exact statement, with what you tried, the step that fails and the smallest undecided instance. Never write it up as proved, and never drop it.
10. Known and Open are not end points. A Known statement is derived from the cited theorem in the form needed here, with the proof of the reduction. An Open statement records your own attack: the strongest partial result you proved, the computations you ran, the obstruction as an exact statement. A row "open, see [reference]" without your own attempt is unfinished.
11. Exact integer and lattice computations are done exactly, by program, with the code attached. A numerical value is given with its precision; a numerical fit supports a statement and does not prove it.

WHAT TO DELIVER
One ZIP containing:
- `<ID>_paper.tex` and its PDF (LuaLaTeX, compiles cleanly): the mathematics in the order of the Parts, every statement numbered and labelled Proved / Refuted / Known (with citation and derivation) / Open (with your attack), with complete proofs. English, first person plural, the register of a careful research paper. No bullet lists where an argument belongs, no summaries of what you are about to do, no closing recapitulations.
- `<ID>_results.csv`: one row per numbered statement: `id, statement, status, where_proved, depends_on, item_of_the_prompt, notes`.
- `<ID>_references.bib`.
- `<ID>_report.md`: what you read, what you computed, every correction to the workbench, the survey and the Leads, and the list of what remains open with the smallest undecided instance of each.
- `code/`: every program you ran, with its output.
The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person, and claim no priority: where a result is known, cite it; where you did not find it, say what you searched.

This task is long by design. Work through all Parts completely; do not stop at an outline, a sample or a plan, and do not ask whether to continue. Ignore any clock. Write the files from the start and extend them as you go, so that an interruption loses little.

IF THE EXECUTION ENVIRONMENT FAILS
If the workspace disconnects or the attached zip cannot be opened, wait and retry for at least ten minutes. If it does not come back, write the work out in the chat as text: every deliverable file in full, each in its own code block headed by its file name; then continue the mathematics in the chat as far as possible. An answer that only reports the failure or asks for the files again is not acceptable.
