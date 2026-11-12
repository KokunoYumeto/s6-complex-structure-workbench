# Source and proof receipt: homogeneous quantum continuation

4 September 2026. This delta applies the existing adjoint-plus-triplet
gauge--scalar density. It does not change the gauge group, delete scalar
coordinates, or verify the original global S6 claim.

## Primary literature actually checked

- Barry Simon, *Some quantum operators with discrete spectrum but
  classically continuous spectrum*, Annals of Physics 146 (1983),
  209–220, [DOI](https://doi.org/10.1016/0003-4916(83)90057-X).
  Original [author-hosted scan](https://math.caltech.edu/SimonPapers/158.pdf),
  610,699 bytes, SHA-256
  df9c5af529ad41ed92a78d848a6ffaafb7e85f4cbb6f788a55a03ab76e57dcb7.
  Section 2's oscillator mechanism and Section 7's equation (3),
  Theorem 3 and Corollary 4 were read. The underlying discreteness
  phenomenon is classical. The full specialized proof in the draft
  derives the retained su(3) frequencies and constants directly.
- Barry Simon, *A Feynman–Kac Formula for Unbounded Semigroups*,
  [arXiv:math-ph/9907022v1](https://arxiv.org/abs/math-ph/9907022v1),
  27 July 1999. Original TeX source downloaded and read, including
  the bounded-below Brownian-bridge formula in Theorem 1.1.
  The gzip source download has 4,888 bytes, SHA-256
  f2dc3fa7d47415df5f20a6790c6b375c9ede7a3315f8d979844aa25f4301d961.
  Extracted original TeX has 11,759 bytes, SHA-256
  427ae55d97ed0c7355058beb200550c368f8f1337539e4125c8c1d71186eca2e.
  The draft retains its full diffusion matrix, hbar and measure constant;
  it proves the needed bounded-below case rather than using a
  differently scaled formula without a coefficient map.
- David Tong, *Lectures on Gauge Theory*,
  [official text](https://www.damtp.cam.ac.uk/user/tong/gaugetheory/gt.pdf),
  Section 2.2.1, equations (2.27)–(2.31). The existing local text
  was read on Gauss law after temporal gauge and physical states.
  Its different Hermitian-field coefficients are not substituted.
- Martin Lüscher, *Some analytic results concerning the mass spectrum
  of Yang–Mills gauge theories on a torus*, Nuclear Physics B219
  (1983), 233–261, [DOI](https://doi.org/10.1016/0550-3213(83)90436-4).
  Bibliographic identity and scope only were checked; no detailed
  coefficient or theorem from this paper is used in the proof.

Primary downloads remain reference-corpus sources. This mathematical
delta distributes its own proofs and source links, not those journal scans.

## Independent calculation and integration

The root and one bounded reviewer independently derived the sharp real
root trace and the six-directed-pair oscillator allocation. A second
reviewer independently derived all momenta, Gauss pairings, operator
domains and heat-kernel argument. A third reviewed the coupled
compactness and scalar bound. Their reports are preserved alongside
three portable exact algebra checkers (82, 124 and 18 assertions).

The canonical proof integrates those complete calculations, replacing
duplicate compactness arguments by one full direct proof. All thirty-eight
coordinates and interactions remain in the Hamiltonian. The sharp scalar
estimate is proved directly in complex-Hermitian coordinates. The last
Fourier-subsector argument includes its operator-domain justification.
The absolute pure-matrix energy-origin bound is not misreported as
an excitation-gap bound.

The standalone root is s6_homogeneous_quantum_confinement.tex. The
same proof module is included in workbench.tex. Status, abstract,
overview, claim/morphism/dependency ledgers, literature log, README,
Pro feedback and AI source closure are updated together. Original
reviewer annotations, prior companion papers, source packets and
frozen publication PDFs remain unchanged.
