# One-eigenvalue Hopf boundary: source and scope audit

Owner: boundary_d. Date: 2026-11-15. B.4.25.
Full source: B_hopf_resonance_obstruction.tex. Integrated with results CSV after independent full-proof PASS by root and limits_ab on 2026-11-15, approximately 20:58 UTC. Root also independently checked the original Oda construction and the two-eigenvalue basis conversion.

The proof is an explicit automorphy calculation and a direct coherent-
image exact sequence. It does not require a classification of central
normalizations, a Kähler hypothesis, a normal-crossings central fibre,
or an unproved comparison between arbitrary fillings.

The invariant bivector f dz^-1 dw^-1 obeys
f(alpha z,beta w)=alpha beta f(z,w), so monomial sections satisfy
alpha^(i-1) beta^(j-1)=1. For |alpha|<|beta|<1 there is the section zw,
and exactly one extra section w^(N+1) at alpha=beta^N. Rouche on radius
(2|beta(0)|^N/|kappa(0)|)^(1/m) gives infinitely many distinct resonances
approaching zero. Coherence of pi_*K^-1 and R1 pi_*K^-1 over a disc
forces h0 constant on some punctured neighbourhood by the displayed
multiplication exact sequence. This avoids the old Grauert Section7
closedness statement affected by the erratum.

## Opened primary sources

1. Grauert, H. (1960). Ein Theorem der analytischen Garbentheorie und
   die Modulräume komplexer Strukturen. Publications Mathématiques de
   l'IHÉS, 5, 5–64. DOI10.1007/BF02684746.
   https://www.numdam.org/article/PMIHES_1960__5__5_0.pdf .
   Original Section6 HauptsatzI, printed p59, opened again for this
   argument. Retrieval turn592view0/1. Existing key Grauert1960D reused.

2. Bierstone, E., & Milman, P. D. (1995 author preprint). Canonical
   desingularization in characteristic zero by blowing up the maximum
   strata of a local invariant. https://arxiv.org/pdf/alg-geom/9508005 .
   Theorem1.6, the analytic noncompact paragraph, and the explicit
   isomorphism-away-from-the-original-singular-locus condition opened.
   Retrieval turn590view0/1/2. Existing key BM95AB reused. The proof
   retains the unique reduced component dominating the disc; its entire
   punctured family is smooth, so resolution leaves it unchanged.

3. Oda, T. (1978). Lectures on torus embeddings and applications.
   TIFR Lectures58. Springer-Verlag.
   https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr58.pdf .
   Original Section13 pp113–118 and Section14 Theorem14.1 pp121–122
   opened independently of root. Retrieval turn587view0/1.
   In the degeneration on pp116–118, the cover basis is n, -n+a n',
   so n'=(v1+v2)/a; after lambda=t^a both contraction eigenvalues are t.
   This does not give a degeneration with one eigenvalue tending to a
   nonzero contraction. New bibliography key Oda1978D was coordinated
   with root, who had not introduced a duplicate.

Scope: no proper analytic completion of the specified diagonal Hopf
family (including finite base changes), not nonexistence of the actual
S6 torus-family cap. The generic blow-up in the Kato family changes its
anticanonical section space and is not a counterexample. No novelty
claim is made.
