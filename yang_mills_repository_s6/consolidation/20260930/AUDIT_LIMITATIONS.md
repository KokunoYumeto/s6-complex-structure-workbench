# Audit limits and evidence boundaries

## What was exhaustively registered

All nine custody ZIPs were reopened, their full-file SHA-256 values were recomputed, and their 71,426 direct central-directory entries were registered by ordinal. V2.1 records 214 direct nested-package placements, 56 distinct package byte versions, 13,671 package-entry definitions, and 12,822 package-file definitions. Expanding every placement and containment edge with multiplicity gives 29,324 logical nested entry occurrences, including 24,564 logical nested text occurrences. Exact archive identity, member ordinal and path, byte length, compressed length, CRC32, package identity, container chain, and available content or text hash are retained.

Every registered text byte version can now be decoded. V2.1 has 41,695 direct text occurrences, 24,564 logical nested text occurrences, and 7,637 distinct decoded text versions. Two TeX files needed explicit encodings; exact decode/encode round trips prove that no source byte was altered. The CP932 recovery contains one U+3000 encoded by `81 40`; the CP1252 recovery contains one degree sign encoded by `B0`. The additional version is the exact 52,910,440-byte outer `MANIFEST.json` that V1 failed to distinguish from a nested file with the same name.

This is exhaustive outer-entry registration and exhaustive recursive occurrence modeling for the stated custody scope. Opaque member contents remain custody objects rather than semantically read texts. This is not exhaustive mathematical understanding.

## What the structural index means

The index contains 55,659 TeX spans or routing locators:

- 30,269 display environments;
- 6,021 theorem, lemma, proposition, definition, remark, or related statement/note environments;
- 5,042 proof environments;
- 282 manual statement-heading locators;
- 217 manual proof-heading locators;
- the remaining records are headings.

It also contains 87,272 literal label, reference, include, and citation records. These are lexical facts about exact decoded versions. The parser does not expand macros, execute TeX conditionals, decide which historical branch is authoritative, infer every custom theorem style, resolve every dynamically constructed include, or verify that a reference points to the intended mathematical object. Manual heading locators mark only a heading; their body boundaries were deliberately not guessed.

The 31 unmatched opening counts and 28 unmatched closing counts in the original extraction are audit signals. They can arise from custom macros, inactive branches, fragments, or genuinely incomplete structure. They have not been silently repaired.

## Occurrences, versions, and works differ

An occurrence is a path inside a source or archive. A version is a distinct byte hash. A mathematical work may occur in many paths and versions, while a single large version may contain many works or historical branches. Consequently:

- 66,259 direct-plus-logical-nested text occurrences do not mean 66,259 independent documents;
- 7,637 text versions do not mean 7,637 independent papers;
- 5,042 lexical proof environments do not mean 5,042 correct proofs;
- repetition across versions is provenance evidence, not independent confirmation.

## Topic routing is intentionally provisional

Filename and member-path rules, followed by one evidence-backed cue-reading tranche, route versions into overlapping lanes. Current distinct-version counts are 315 analytic-candidate, 371 cusp/spectral, 1,243 arithmetic-selector, 354 lattice/Jordan, 538 quaternionic/gauge, 190 measured-fibre, 409 finite-quantum, 1,022 zeta/heat, 7 GCT/arithmetic, 23 primary S6, 8 Yang--Mills cross-reference, and 2 Navier--Stokes cross-reference. A version can belong to several lanes.

Another 4,228 versions remain `unclassified`. This label means that the conservative routing rules and completed cue-reading tranche found no sufficiently specific inspected cue for them. It does not mean that the content lacks mathematical relevance. `checks/UNCLASSIFIED_TRANCHE_2026-09-30.json` records the exact cue line, byte hash, assigned lanes, and a custody occurrence for each of the 40 moved TeX versions. Those line readings establish routing only. The two recovered non-UTF-8 works demonstrate the general issue: content inspection was needed to route an exceptional-Lie-groups source that had an opaque filename. The corrected outer manifest remains conservatively unclassified rather than assigned a mathematical lane from its filename.

## Unsupported and binary material

There are 29,517 direct opaque placements and 2,910 logical nested opaque occurrences. Their paths, ordinals, sizes, archive locations, package routes, and custody status are retained. This group includes figures, PDFs, build products, databases, and formats for which the text extractor has no semantic reader. Nested ZIP files are represented separately as package placements and containment edges.

The present audit did not inspect every image, render every PDF, reverse-engineer every database, or treat generated build products as source evidence. PDF text is not used as a substitute when original author TeX is available. The four current mathematical figures were inspected separately in their rendered PNG forms because they are part of the current argument.

## Conversation-history boundary

The first source tree names 2,884 task rows. Original JSONL was located for 845 of them. For the remaining 2,039 task IDs, available projected metadata and histories are retained, but those projections are not represented as original raw conversation bytes. This limits any audit of exact user wording, tool output, abandoned branches, or timing for those tasks.

The located histories have been preserved and structurally routed. They have not all received line-by-line semantic mining. A historical agent assertion remains an assertion even if the surrounding task reported success.

## Actual reading coverage

The exact read passages are in `literature/SOURCE_READING_LEDGER.jsonl`. For the new mathematics, the material actually read includes:

- the retained Gaussian source, lines 334--688 of hash `107932c0...`;
- the residual-measure source, lines 1--465 of hash `c3c53021...`;
- Chruściński--Pascazio original TeX, lines 135--239 of hash `5106e5c0...`;
- Hornberger original TeX, lines 151--272 and 1240--1321 of hash `2d1ed46d...`.

Other exact readings from the custody pass remain in the same ledger. No bounded reading is described as a complete audit of its file, paper, or surrounding literature.

The first unclassified-source tranche adds 40 one-line cue readings to the ledger. Each record identifies the exact version and line and expressly leaves the remainder of that version semantically unread.

## Mathematical verification boundary

R1--R8 have complete arguments in `MATHEMATICAL_NOTE.md` and `TOMOGRAPHY_DESIGN.md`. The replacement verification separates twenty exact check groups from five numerical evidence groups. The earlier 42-check count is superseded because it counted repeated numerical samples individually and its tomography example was diagonal. Numerical agreement and positive-semidefinite samples can reveal mistakes and test stated finite examples. They cannot prove a universal claim unless an accompanying argument covers the full domain. The note and appendix supply those arguments for their stated results.

The current work is not a formal proof-assistant verification. No Lean run was needed or started. It also is not a literature-exhaustiveness or novelty audit. Two original-author TeX sources were read for the finite quantum comparison, and the canonical disk-literature index was queried first, but the surrounding literature has not been exhausted.

## Build boundary

`CONSOLIDATION.tex` is a generated standalone TeX source. The built-in compiler returned `compile-failed` because it could not locate standard directories for the platform. That message did not identify a source-line TeX error. The source is retained, but no successful PDF compilation is claimed. A Pandoc parse and structural checks can test source construction; they cannot replace an actual TeX engine run.

## Claims expressly outside current acceptance

The audit has not accepted a global S6 identification, sphere recognition, global analytic atlas, bosonic field theory, quantum Darwinism statement, decoherent-histories functional, interacting Yang--Mills gap, Navier--Stokes theorem, or Riemann-hypothesis result. It has not reconstructed all historical heat and determinant formulas from the original zeta function. Each remains a named receiving problem in `UNMINED_QUEUE.md`.
