# S6 annotated mathematical proof audit

This is the editable, page-linked proof-audit edition of a 108-page manuscript claiming a complex structure on the smooth six-sphere. It combines two independent ChatGPT Pro-mode audits with a third Codex mathematical and TeX review. It is a literal model-peer review artifact, not conventional journal-administered human peer review.

## The two files to click

1. **Annotated version:** [`main.tex`](main.tex) - the default 121-page edition: one findings guide above the existing 120-page manuscript-and-audit document.
2. **Raw version:** [`clean_transcription.tex`](clean_transcription.tex) - the standalone, unannotated 108-page transcription.

That pair is the complete reader-facing core. Everything in the folders is supporting review evidence, source provenance, or reproducibility material. In the annotated version, click a colored badge at the top right of any manuscript page to jump to its reviewer-separated entry. Open `reviews/README.md` only when you want the complete reports, ledgers, and exact-check evidence.

## Current mathematical disposition

**Major revision; the central theorem is not presently mathematically certifiable.** The complete-source audits found substantial reproducible finite algebra and no decisive contradiction in the completed manuscript. They did not independently establish the integral geometric maps on which the claimed identification with $S^6$ depends. The result is therefore unconfirmed: neither accepted as proved nor classified here as disproved.

The earlier packet-only rejection based on CDP20 is superseded. Complete Section 10 supplies a substantive proposed response, but it has not been externally adjudicated. A plausible gap in a published proof is not itself a proof that the published theorem is false.

## Human-readable project tree

```text
README.md                       start here
main.tex                        default 121-page annotated edition
clean_transcription.tex         standalone 108-page clean reconstruction
annotations/                    reader guide, badge layer, appendix, index
docs/                           build, QA, rights, exclusions, Reddit handoff
manuscript/                     one-file edition, modular source, source PDFs,
                                and reconstruction audit
reference_pdfs/                 compiled annotated and clean PDFs
reviews/                        Reviewer A, Reviewer B, Reviewer C/Codex,
                                and the clearly superseded packet-06 review
reproducibility/                exact checks and structural PDF verification
metadata/                       file tree, manifest, checksums, Zenodo template
archive/                        original small review-package ZIP containers
```

The top level deliberately contains only the three principal reader/editing entry points and plainly named subject folders. Machine ledgers remain available under `metadata/` without obscuring the project.

## Annotation badges

- `E` - an independently reproduced finite calculation; never whole-page certification.
- `N` - reviewed for coherence with no concrete error found; not formal verification.
- `C` - conditional on earlier construction, topology, or analytic hypotheses.
- `U` - critical unresolved proof obligation or literature conflict.
- `X` - confirmed localized mathematical or TeX defect with a repair or workaround.
- `P` - source, reconstruction, bibliography, build, or verification provenance.

Badge precedence is `X > U > C > E > N > P`. The detailed page entry can contain more nuance than the single highest-precedence badge.

## Review streams

- **Reviewer A / first Pro audit:** 17-page full-manuscript report; 28 passing exact checks; major revision and specialist replication. It withdraws the earlier packet-only rejection and treats Section 10 as technically substantive but externally unresolved.
- **Reviewer B / second Pro audit:** 6-page primary report; 38 passing exact checks; 92-row theorem ledger; major revision, main theorem not certified. It isolates four load-bearing topology obligations.
- **Reviewer C / Codex:** reconciles both streams, audits the TeX and exact harnesses, keeps its own issue ledger, and records precise local repairs and build defects.
- **Packet-06 review:** retained as historical evidence with its exact local checks, but its immediate-rejection recommendation is superseded because it lacked the complete manuscript and Section 10.

The 28- and 38-check harnesses overlap substantially. They must not be added and reported as 66 independent checks.

## Methodology and model provenance

The depositor reports that Claude produced the mathematical manuscript, which was supplied as a PDF. The 108-page PDF was then fed through the ChatGPT web interface in ten packetized strips: 11 pages for packets 1-8 and 10 pages for packets 9-10. ChatGPT re-transcribed each strip into LaTeX. This was reconstruction from the PDF, not recovery of an author-controlled original TeX source.

Codex consolidated the packet sources into a coherent monolithic reconstruction, reconciled boundaries, checked the TeX, and audited it against the supplied PDF pages. Two separate ChatGPT web-interface threads then performed the mathematical proof audits. Codex conducted a third mathematical and TeX review, reconciled the three records, created the annotations and reader guide, checked the exact-arithmetic harnesses, organized this project, and prepared the Overleaf edition.

As reported for this workflow, the web transcription and review sessions used **ChatGPT 5.6 Sol** (`S-O-L`) in **Pro mode**. The local Codex review, consolidation, annotation, QA, packaging, and upload used **GPT-5.6 Sol** in **Ultra mode**.

## What the audit establishes

Exact checks establish only the encoded finite calculation under its stated inputs. They do not establish missing geometric constructions, smoothness, attaching maps, specialization morphisms, integral lattices, analytic base-change hypotheses, or applicability or failure of an external theorem.

The clean transcription preserves the manuscript without review marks. The annotated edition does not silently repair its 108 source pages; corrections are recorded in the guide, badges, appendix, and ledgers so readers can compare every finding with the supplied text.

## Build and contribution

In Overleaf, choose `main.tex`, **pdfLaTeX**, and the latest TeX Live image. No shell escape, external font, bibliography tool, or network fetch is required. See `docs/BUILD.md` for local builds and QA commands.

Readers are encouraged to copy the project, rerun checks, and propose precise corrections. Modified versions should identify substantive changes and preserve `docs/RIGHTS_AND_PROVENANCE.md` so the supplied manuscript, AI review layers, and later contributions remain distinguishable.
