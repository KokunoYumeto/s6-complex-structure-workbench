# Reproducibility tools

- `annotated_qa/` builds the one-file annotated source and verifies the
  108-page source layer, page destinations, badge links, page geometry, and
  maintainable-versus-standalone PDF identity.
- `verify_direct_boundary_picard.py` replays the 14 exact integer checks used
  by the direct boundary-Picard certificate. Its complete machine result and
  execution receipt are `direct_boundary_picard_results.json` and
  `direct_boundary_picard_execution.log.txt`.
- `verify_analytic_picard_completion.py` replays the 25 exact support-function,
  central-degree, polarization, mixed-block, unimodularity, and boundary
  coefficient checks used by the purely analytic all-Picard certificate. Its
  complete result and deterministic receipt are
  `analytic_picard_completion_results.json` and
  `analytic_picard_completion_execution.log.txt`.
- `verify_cusp_spectral_relations.py` replays 13 exact symbolic checks for the
  radial real period determinant, full inverse transpose, dual-coordinate
  norms and pairing, integral coframe wedge, ambient Koide discriminant,
  finite coordinate eigenvalues, cusp covolume expansion, and the two first
  spectral corrections.  It contains no Python `assert`, is tested under both
  ordinary and optimized Python, and writes
  `cusp_spectral_relations_results.json`; the runtime, commands, exits, and
  hashes are recorded in `cusp_spectral_relations_execution.log.txt`.
- `generate_project_metadata.py` regenerates the complete file tree, payload
  manifest, and SHA-256 ledger under `../metadata/`.
- `extract_public_provenance.py` verifies selected source-event ordinals and
  hashes against a byte-exact frozen private-session prefix, then emits only
  the edited mathematical chronology and its redaction receipt.
- `generate_complete_conversation_provenance.py` streams the same frozen
  prefix, structurally excludes platform-injected records, redacts every
  human/assistant event, and substitutes independently prepared,
  source-hash-anchored summaries for abusive/profane user turns.
  `validate_complete_conversation_provenance.py` independently replays that
  derivation and fails unless coverage, hashes, privacy scans, editorial
  certifications, and the zero-unresolved release gate all agree.
- `verify_publication_pdf.py` performs strict page-geometry, rotation,
  content-stream, text-extraction, destination, and font-embedding checks.
  The five 1 September snapshot reports are under `publication_pdf_qa/`;
  regenerate them after the live sources are frozen.
- `build_zenodo_release.py` materializes the DOI source tree from an explicit
  allowlist, excludes session/history/archive material, scans every selected
  text file and PDF for private data, creates a deterministic source ZIP, and
  proves an extracted inventory and second pack are byte-identical.
- `deterministic_release_roundtrip.py` validates the generated ledgers and
  five reference PDFs, writes the deterministic sibling ZIP, extracts it to a
  unique temporary directory, compares every path/byte count/hash, and
  requires a byte-identical second pack. Run it with `--check-only` before the
  final packaging run.

Run these commands from the project root. Generated TeX/PDF build products
belong outside the source tree except for the five reviewed reference PDFs and
the deliberately retained standalone annotated source.
