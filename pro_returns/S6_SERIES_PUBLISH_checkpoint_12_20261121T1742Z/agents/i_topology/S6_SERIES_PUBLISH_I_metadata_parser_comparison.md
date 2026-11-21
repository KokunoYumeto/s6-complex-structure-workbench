# Paper I metadata parser and proof-alias review

## Outcome

One guarded code replacement restores immediate proofs preceded by source-credit text or a retained label/tag gap. Two guarded TeX relocations make the proof markers refer to their owning statements. No shared file was edited, no check row was modified, and no mathematical event or independence credit was added.

The review is bound to source SHA256 `38fd3831cb7be2eb60d856024571f9f8ec9105df45b445714251c41932580bbb`, current metadata script SHA256 `76ef16c490df27cd6452362b748b1b3b6a70bfc3c06ef2cba7e7db46f51cc1cd`, and authoritative recompute script SHA256 `43a628b37883435e01e52fadbfe8a892c39b686bc019026268e5621033752484`.

## Parser comparison

The former `re.match` accepted only whitespace between a numbered statement and its proof. The source-credit paragraph after `inv:A3.1` therefore excluded that proof from the current metadata region. The replacement searches only the gap before the next numbered environment, section/subsection/subsubsection/part heading, program table, or bibliography. It includes the first immediate proof through its balanced closing token. This is the same bounded immediate-proof policy used by the authoritative recompute parser; the closing-token scan is additionally constrained to that gap.

Read-only execution of the original and proposed parser fragments over all 333 current Paper I environments found exactly these changes:

| Statement | Original region | Proposed region | Reference effect |
|---|---|---|---|
| `inv:A3.1` (12.15) | Through statement end at source line11728 | Through proof end at line11752 | Adds exactly `inv:A1.0`, `inv:A2.4`, `inv:eq:A-absolute-table`; matches the authoritative recompute result |
| `fam:src:A.5.1` (7.8) | Through statement end at line8834; legacy fallback already read its proof | Through immediate proof end at line8865 | Reference set unchanged; gap marker is now in the owned region |

Every primary statement identifier, its order, and every retained statement-identity sequence are unchanged. The existing deferred-proof fallback is retained; reference extraction is set-valued, so its repeated reading does not duplicate an edge or a check event. Five fixtures passed: source-credit gap, retained-label gap, next-numbered-environment boundary, next-subsection boundary, and balanced nested proofs.

## Proof-marker ownership

| Marker | Candidate12 auxiliary number/anchor | Owning statement | Proposed number/anchor |
|---|---|---|---|
| `I:coherent-descent-proof` | 7.2 / `subsection.7.2` | `fam:src:A.3.1` | 7.5 / `proposition.7.5` |
| `app:rederive:fam-src-A.5.1` | 7.4 / `theorem.7.8` | `fam:src:A.5.1` | 7.8 / `theorem.7.8` |

The original current-metadata parser assigns neither marker an owner. The authoritative recompute parser assigns the intended owners through its explicit deferred-proof map. The bounded parser alone owns the classification marker; moving both markers into their owner headers makes both ownership maps agree. The classification marker's current auxiliary entry mixes a subsection number/title with a theorem hyperlink anchor, so relocation is required for a correct displayed reference.

The coherent-descent marker moves alone; subsection label `fam:section:A.3` and permanent tag01PC remain at subsection7.2. The classification marker moves together with its permanent tag000C. Every label and permanent tag is preserved with the same multiplicity. After stripping only these relocated markers and whitespace, the old and proposed TeX are identical: all mathematical prose, statements, proofs and formulas remain unchanged.

An isolated pdfLaTeX fixture using the paper's theorem/aliascnt/cleveref declarations reproduced the old numbers7.2/7.4 and verified the new owner numbers7.5/7.8 and their anchors. The separate subsection labels remain7.2/7.4. The first unconfigured system-TeX attempt lacked its format; both fixtures subsequently compiled successfully using the already existing publication runtime, without invoking the runtime-writing helper. Final publication page locations require the next root-owned full build.

## Artifacts and scope

- `S6_SERIES_PUBLISH_I_metadata_parser_code_guard.json`: exact old/new code replacement.
- `S6_SERIES_PUBLISH_I_metadata_parser_alias_guards.json`: two exact source relocations.
- `S6_SERIES_PUBLISH_I_metadata_parser_comparison.json`: input hashes, actual parser changes, ownership comparison and fixture assertions.
- `S6_SERIES_PUBLISH_I_metadata_parser_label_fixture.json`: actual old/new auxiliary entries and fixture file hashes.
- `S6_SERIES_PUBLISH_I_metadata_parser_review.py`: reproducible read-only parser review and guard generator.
- `S6_SERIES_PUBLISH_I_metadata_parser_output.json`: complete execution output.

The programs were compared for these proof regions and marker ownership. Their other reference-scope features, such as outline attachment and range expansion, were not newly certified. This is a metadata/label correction and creates no mathematical check event.
