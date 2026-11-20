# DGKX v1 primary PDF locator and exact family transport

Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort, same model family. Fresh primary reading on 19 November 2026, after the atlas derivation. This is a targeted source check, not a new independent proof event.

## Edition and pages actually opened

Downloaded original `https://arxiv.org/pdf/2610.00250v1`, not a local recompile. The title is *Oka Geometry and Deformations of Torus-Fibred Complex Six-Spheres*. The PDF has 107 pages and 907000 bytes; SHA256 `7facc6e55c7a578315a981224c45f184d3033b6159773304968508aca2710ab3`. It is saved as `DGKX_v1_primary.pdf`; layout text is `DGKX_v1_primary.txt`.

The complete six-arrow scalar table, Lemma 6.14, and its complete proof are all on printed page 84, which is PDF page 84. The derivative convention (6.41), composition rule (6.42), and core arrows (6.43) are on p. 82; finite/collar/cusp arrows (6.44)–(6.49) are on p. 83. Page 84 was rendered and visually opened at 1800 pixels. Pages 5 and 8 were also rendered and visually opened; the other pages below were read in the primary PDF text.

## Precise original-family hypotheses

- Lemma 2.1 p. 4: marked oriented (3,4,infinity) orbifold cover, original inverse vertex generators, primitive cusp generator, ordinary free locus after deleting the two elliptic orbits.
- Ordered lattice and matrices (2.2), pp. 4–5: (gamma-hat,u-hat,w-hat,delta-hat), exactly the order in the receiving period matrix.
- Proposition 2.2 p. 5: fixed holomorphic tau, mu, beta0 and vertical R_g, Omega_a=[[6mu,tau,1,0],[beta0+a,mu,0,1]], Im(tau)>0, exact affine transformation laws, cusp extension of beta0+tau and mu.
- Proposition 2.3, statement p. 5 and complete proof p. 6: D_a=Im(beta0+a)-6(Im mu)^2/Im tau, M0=sup D0, A={Im a<-M0}; det_R Omega_a=Im(tau) D_a in its stated real-coordinate order.
- Finite data (F1)–(F3), vectors (2.19), character (2.21), p. 8: m1=3,m2=4, v1=(1,2,-4,0)^t, v2=(-1,-3,3,0)^t, gamma(v1)=1,gamma(v2)=-1. Affine generators (2.22), their complete freeness Lemma 2.6 and quotient Proposition 2.7 are on p. 9.
- Cusp period decomposition (2.30) pp. 11–12 retains the full holomorphic C_a(q) and B0=[[0,1],[-1,0]]. Proposition 2.9 p. 12 specifies the same two unit-square triangles. The exponential connector (2.49) and Proposition 2.22 pp. 18–19 are untranslated.
- Theorem 2.24 and Proposition 2.25 p. 20 give the proper holomorphic family and canonical comparison under changing cutoff/parameter disc. Definition 2.26 p. 20 fixes each representative.
- Lemma 2.29 pp. 21–22 gives the identity on all four pieces for the same original data, retaining vectors, fan, and absence of a cusp translation. Corollary 2.30 p. 22 transports the original sphere topology through the actual proper smooth family.
- Section 6.4 starts on p. 82 by fixing an admissible a in A and explicitly uses this family. Lemma 6.14 does not claim a broader family of arbitrary twists.

## Exact transport to Paper I

Let delta=beta_part-beta0. Both functions have the same affine laws and cusp-regular sum with tau, so delta descends holomorphically to P1 and is constant. Set a=c+delta, with inverse c=a-delta. Then Omega_a=Pi_c, D_a=D_part+Im(c), and M_part=M0+Im(delta). The parameter map sends P={Im c<-M_part} bijectively to A. Paper I's evaluated maximum is M_part=-3log(6)/pi, hence P={Im c<3log(6)/pi}. The identity on the four pieces respects the original finite affine actions, logarithmic connectors and untranslated cusp action. No change of vectors, fan or marking occurs. Also a'-a=c'-c.

The receiving scalar cochain is f=-eta_DGKX on each of the six named arrows. This follows by substitution on lattice, base, finite, finite connector, cusp lattice, and exponential connector; the sign follows the receiving line-coordinate convention. The factor 12 in G,Q belongs to the separately proved receiving normalization; no factor 12 is inserted into the source's scalar statement.

## Guarded publication proposal

`page_locator_followup_patches.json` contains two unique exact replacements against the receiving body read in this check: the p.84 credit and the explicit original-family/parameter-domain first sentence. No shared file was changed. The p.84 citation closes the missing source-page locator. Publication integration and current rendered-page inspection remain root-owned.
