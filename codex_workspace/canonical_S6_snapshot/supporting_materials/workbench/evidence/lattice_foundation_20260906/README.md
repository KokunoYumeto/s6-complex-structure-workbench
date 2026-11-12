# Exact lattice and canonical-ring checks — 6 September 2026

The proof-bearing text is in the research modules
`es_niemeier_cubic_arithmetic.tex`,
`es_niemeier_residue_fixed_neighbor.tex`,
`es_niemeier_wilson_cyclic.tex`, and `analytic_canonical_ring.tex`.

Run each Python checker from its containing directory. The cubic and
canonical-ring checks use only the Python standard library. The neighbour
and Wilson checks additionally require SymPy. Each run prints exact JSON;
the saved JSON, execution logs and reproduction receipt record the released
calculation. No floating-point approximation is used in these checks.

The cubic value-module proof reduces the entire infinite lattice to the
displayed finite polarization generators, with both upper and lower
certificates. The neighbour proof establishes completeness of the root
classification. The Wilson proof establishes evenness, unimodularity and
rootlessness from the defining lattice conditions. Their finite checks
supplement those arguments. The canonical-ring checker tests finite order
and degree identities; the written sheaf and graded-ring proofs, not those
samples, establish the assertions for all integers.

Primary sources are cited in the papers. In particular Wilson's octonionic
Leech construction and the Niemeier holy construction are not claimed as
new discoveries here. These lattice calculations do not certify the
claimed global complex structure on a six-sphere, nor an interacting
Yang–Mills spectrum.
