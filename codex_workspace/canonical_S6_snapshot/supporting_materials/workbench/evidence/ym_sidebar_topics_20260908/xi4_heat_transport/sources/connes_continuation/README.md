# Arithmetic trace quotient and exact heat transport

The reader is `connes_quotient_heat_transport.pdf`. The complete standalone source is `tex/main.tex`; the inclusion-ready mathematical fragment is `tex/connes_quotient_heat_transport.tex`.

This work keeps the actual Connes–Consani–Moscovici closed trace-image quotient and transports its topology, relation subspace, multiplication operator, and original-coordinate spectrum through the globally convergent heat operator. It also proves direct descent failures in two explicitly defined analytic topologies, constructs derivative relations and correlated jet extensions, and proves the inverse-root cover's branch domains. The actual source topology is named but not specified by seminorms in the inspected primary texts; that missing identification is recorded honestly. No RH outcome is claimed.

The continuation proves that the compact and growth closed relation subspaces both equal Xi times the original entire-function ring, by a complete division estimate. It computes their different quotient topologies, the compact quotient's product completion, every derivative domain and finite ambiguity image, and exact source-coordinate kernels and cokernels. The arithmetic bridge retains the full Schwartz Mellin factorization, all local zeta units and principal parts, and a unique Möbius inverse for each heated finite Hermite trace. For every nonzero heat time some such inverse is unbounded at the origin. Every new assertion has a written proof in the standalone fragment.

## Reproduce

Run `python checks/verify_exact.py` with SymPy installed. This is one worker, and on Windows it installs an exact 5,000,000,000-byte process-tree memory ceiling before importing SymPy. Run `pdflatex -interaction=nonstopmode -halt-on-error main.tex` twice from `tex/`. Copy the resulting `tex/main.pdf` to the reader filename above. No network, Lean, index rebuilding, or numerical zero search is needed.

## Include in another TeX document

The fragment requires `amsmath`, `amssymb`, `amsthm`, `mathrsfs`, and `hyperref`. Copy the `cqtheorem`, `cqproposition`, `cqlemma`, `cqdefinition` declarations and the `cq*` macro definitions from `tex/main.tex` into the receiving preamble, then input the fragment. Bibliographic dependencies are the three entries in `tex/bibliography.tex`; merge these entries into the receiving bibliography. All new labels and citation keys use the `cq` prefix. The fragment has no figure or external-file dependencies. No changes to the parent manuscript are made by this folder.

## Artifact boundaries

The shareable mathematical bundle comprises the PDF, `tex/`, `checks/verify_exact.py`, `checks/verification_receipt.json`, `claims.json`, and `sources/provenance.json`. `logbook/`, primary extracted text, routing results, the internal subagent review, and `sources/private_source_paths.json` are private provenance and are not reader dependencies. Primary source texts are not redistributed as part of the mathematical bundle.
