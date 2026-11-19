# Published CDP step and E18 source/computation comparison

19 November 2026. GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro,
S6_10_PAPERS continuation.

## CDP20 p. 692

Opened the published Compositio Mathematica PDF, volume 156 (2020),
pp. 679–696, DOI 10.1112/S0010437X19007802. Published p. 692 is the
fifteenth PDF page including the publisher cover. Its page image was
rendered and visually read. The supplied source's section 7 was also
read; the published sentence has different punctuation/order from that
source. The quotation inserted in Paper II's opening follows the
published page, including its equation (11), before the paper's reading.

The displayed conormal map is multiplication by the derivative vector
of a local reduced defining equation F. Its kernel is zero: at each
generic component point some derivative is nonzero, and the reduced
ring injects into the product of its component fields. Let T be the
torsion submodule of Omega_S, Q=Omega_S/T, and K its inverse image in
Omega_X|S. Then the actual maps give

    0 -> N* -> K -> T -> 0,
    0 -> K -> Omega_X|S -> Q -> 0.

Tensoring by the line A preserves exactness. H0(QA)=0 gives an isomorphism
H0(KA) -> H0((Omega_X|S)A); H0(N*A)=0 makes H0(KA) the kernel of the
connecting map H0(TA) -> H1(N*A). Thus the endpoint vanishings require
the injectivity of that connecting map to yield the ambient vanishing.
This is the neutral reading used in the opening and the exact criterion
already proved in A.1.1. The opening and a search excerpt of the old proof
had already been visible: this receipt is a targeted check, not a fresh
unseen whole-proof rederivation. It neither attributes an ambient section
to a section supported on the singular locus nor suppresses the map from
the torsion term.

## E18

`cdp_E18_derivation_before_full_proof.md` was written before the full
receiving E18 proof was opened, but after its checker summary and isolated
search excerpts were visible. The exact independence limit is recorded
there. The full receiving proof subsequently matched the written
calculation. It specifies a proper family of compact two-tori, the
theta-quotient linearization, the actual index-six isogeny, the nonzero
determinant at tau=i, and all tangent direct-image ranks. The prior
source-normalization gate has now been checked against the opened primary
formulas. The proof is retained, now explicitly numbered in six steps in
the revision and both receiving body files.

NIST DLMF was opened at equations 20.2.1–4 (series), 20.2.6 (multipliers),
20.2.12 (half-period shift), 20.5.1–4 (products), 20.7.5 (quartic identity),
20.13.1 (heat equation), 23.6.1–2 (nome/period and half-period value), and
23.17.8 (eta product). The transformation of argument is
vartheta_j(z,tau)=theta_j(pi*z|tau), hence the heat coefficient is
1/(4*pi*i). The Weierstrass periods are 2omega_1=1, 2omega_3=tau.
These are source openings and matches, without a claim to reading the
books named in DLMF's references.

The freshly written program `code/continuation_root/theta_E18_fresh.py`
uses exact rational coefficient convolution and a divisor-sum expansion
to compare 121 coefficients with the fourth powers of theta_3 and theta_4.
All agree exactly. Its symbolic determinant difference and wedge-boundary
determinant difference are both the zero polynomial. The infinite
identity and strict negativity at tau=i follow from the analytic product
derivation, with no numerical truncation used as an analytic certificate.
No producing program was opened, imported or reused.

## Renewed credit comparison

`E18_credit_search.json` stores the exact queries, files, hashes, every
match and its line/page location for the AC26 original PDF text, E26,
DGKX v1 and DGKX v2. The theta, half-period, determinant, linearization
and Kodaira–Spencer searches were inspected. AC26's theta match is a
topological theta graph. E26's theta symbols label geometric actions or
angles. The DGKX determinant matches are the real lattice determinant;
v1's Kodaira–Spencer statements concern its parameter deformation and
are credited there. No counterpart of the arbitrary-section square-only
counterexample was found in this specific search. The received E18
corrects the internal Lead 9 generalization; it preserves the valid
formula on the AC branch wp(mu)=0. NIST's classical identities remain
credited inputs, including the extra elliptic term's normalization.

The renewed new-code and opened-source checks for E18 are complete at
the stated scopes. A second checker with no exposure to its printed
steps is still required for the task's strict whole-proof prereading
protocol. This receipt does not turn a targeted check into that event.
