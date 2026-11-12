# Build and source verification

Reviewed input: `s6_canonical_108_pages_audited.zip`.

- Input ZIP SHA-256: `5cb503a66ed3ba66b4e42ff507ba381194b8fba8911a90fca18dd4ef391aaabb`.
- Monolithic canonical source SHA-256: `c20f12fdaf68fe37ab9d19abc8c432f5c21f2974656cefed62e40307cc79841a`.
- Canonical 108-page PDF SHA-256: `7eddbed85b2817d068d3757ee2247bfcd02d4b410dbb348f7416bc50a3771ccb`.

The archive includes all ten source packets, modular and monolithic source forms, a 108-page PDF, an authority reassembly, build scripts, page audits, and checksum manifests. Its verification script passed. The modular and monolithic forms compile to byte-identical PDFs in the audited environment.

The archive is explicitly an independent reconstruction of the supplied authority PDF, not the author's original TeX. Its audit establishes reconstruction fidelity, not mathematical validity. The mathematical review was therefore performed on the reconstructed canonical content while retaining this provenance limitation.
