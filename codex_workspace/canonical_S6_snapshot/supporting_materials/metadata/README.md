# Deposit metadata

`zenodo_metadata.template.json` is a human-editable starting point for a later Zenodo deposit. Replace the creator and license placeholders after the depositor chooses the public attribution and confirms an appropriate rights instrument. No Zenodo record or DOI is created merely by including this file.

The Overleaf project is the primary live, editable distribution. If a frozen Zenodo version is later published, deposit the verified project ZIP and `supporting_materials/metadata/SHA256SUMS.txt`, then record the DOI in a new version of this README rather than rewriting historical hashes.

The machine-generated `FILE_TREE.txt`, `PROJECT_MANIFEST.json`, and
`SHA256SUMS.txt` live here so ordinary readers see a clean project root. They
cover the complete consolidated project, beginning with root `main.tex`,
`original_clean_transcription.tex`, `workbench.tex`, and
`workbench_and_manuscript_overview.tex`. The checksum
ledger excludes itself; the JSON manifest records its own exclusion policy
explicitly.
