# D.2.48: source locations and exact scope

The theorem is the simply connected sector of the **actual weighted Engel
profile IV*, III, I1**, with both additive caps replaced by good logarithmic
caps. It includes every positive weight d and every pair of finite orders
3k, 4l and marked twists with determinant ±1. It does not assert a smooth
classification for original additive caps, further regular logarithms, or
arbitrary weighted profiles.

## Primary sources checked

- **A. V. Zhubr (1975), Math. USSR Izvestija 9, 793–812.**
  The original English primary PDF was reopened on 16 November 2026 from
  https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=rus&paperid=2054&what=fullteng
  (web references turn450view0, turn451view0–2, turn453view0).
  Definitions of the complete invariants: §1.2, pp.794–795.
  Smooth classification: Theorem 1, p.795.
  Spin-bordism fundamental-class image: Lemma 3.7 and (3.4), pp.805–806.
  Epimorphism on coefficient groups: Lemma 3.11, pp.806–807.
  Free generators epsilon and reduced CP3, and the explicit equality
  ker(alpha)=H6=Z/(2^a) for a two-power coefficient group: §3.12, p.807.
  The general cyclic H6 order is derived in the new proof, not quoted
  from an unverified table: its generator has both d^3 and 3d relations,
  and the ordinary/Thomas cube supplies the matching lower bound.
  Direct local download returned HTTP403; no local PDF is claimed.

- **E. Thomas (1956), PNAS 42, 266–269.**
  The actual primary scans/OCR are outside the deliverable archive at
  ../external_cache/primary_Thomas56.pdf and the corresponding page files.
  Equation (2.1), p.267, has coefficients Z/(p m) to Z/(p^2 m);
  hence it applies to every even d for the square and every 3-divisible d
  for the cube, with the full moduli 2d and 3d.
  Equation (2.8), p.267, gives the projective-space generator evaluation.
  The cochain formula (3.4), p.268, reduces to the ordinary power on an
  integral cocycle. Fourfolds independently reread these primary lines
  and supplied the full scalar-circle localization proof and certificate.

- **J. H. C. Whitehead (1950), PNAS 36, 55–60.**
  Theorem 1 and §2 are the exact-sequence/universal-quadratic inputs
  already primary-verified in E.2.18. For K(A,2), the adjacent higher
  homotopy groups vanish, giving H4=Gamma(A). The cyclic computation
  Gamma(Z/d)=Z/gcd(d^2,2d) is derived explicitly in D.2.48.

- **S. J. Kaplan (1979), Trans. AMS 254, 237–263.**
  Definition 1.7 and Remark 1.8, p.239; Theorem 3.1 and its proof,
  pp.243–246. Correct original primary source and spin/almost-framing
  hypotheses were independently read by root. See
  records/maps_D2_frame_source_audit.md for the corrected provenance.
  The unrelated 1982 Kaplan PDF is not used.

## Geometric comparisons retained

1. The degree-d covering is used only on the regular core and the cusp,
   before either finite cap is filled. It is not a global-cover claim.
2. Equality of the integral boundary classes is proved first at weight one,
   where H1 of the cusp boundary is free, then pulled back. Thus the actual
   Z/d cusp-boundary torsion is not discarded.
3. The finite Gysin test uses all three marked core generators a, gamma,
   and the affine root loop g, including its zero first-row coefficient.
4. The refined-class computation retains the actual order-four mapping
   torus and its **odd** reference framing parity. The critical-link
   half-integer is canceled by that parity, not discarded.
5. The two mixed power targets are Zd and Z/(d gcd(d,2)); the pure target
   is Z/(d gcd(d,3)). All of them are evaluated before Zhubr is applied.

## Checks

- code/maps_weighted_engel_invariants.py: polynomial bounding-chain and
  covering identities, literal critical value −5d, all 264 finite-core
  residue checks, 50 cyclic component matrices, support degrees and full
  square normalization. The arbitrary-parameter proof is symbolic; the
  finite ranges are supplementary.
- code/fourfolds_D48_thomas.py: universal arithmetic identity and 4920
  supplementary character checks, independently supplied by fourfolds.
- code/maps_weighted_engel_build.py: two LuaLaTeX passes exited zero.
  The local PDF is in the external TeX runtime, not the source archive.

Root completed the full independent proof and primary-source audit and reran
both exact certificates successfully. Fourfolds independently audited the
full refined and fundamental-class computations and reran the maps certificate.
D.2.48 is registered and input after D.2.47 in the working manuscript.
