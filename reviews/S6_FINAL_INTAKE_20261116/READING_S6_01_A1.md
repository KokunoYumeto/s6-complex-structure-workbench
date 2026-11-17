# S6_01_INVARIANTS A1.1 and A1.2: one reading

By Claude Fable 5.2 at effort max (the S6 expert, aa7b8224), 16 November 2026, 14:25 UTC. No sub-agents. The return
is by GPT-6 Astra (ChatGPT Pro mode), 12 November 2026.

Read in full, step by step: `returns\S6_01_INVARIANTS_unzipped\S6_01_INVARIANTS\fragments\part_A.tex`, l. 1-302:
A1.0, A1.1, A1.2, A1.3 with their proofs, and the opening of A.2. The two statements are shorter than expected:
A1.1 is l. 98-147, A1.2 is l. 149-219. Nothing was rerun; the degree and extension counts below were redone by hand.

Notation of the return: D = W + S_1 + S_2 (reduced), Sigma = {p_0, p_1, p_2}, L = Omega^1_B(log Sigma) = O(1),
A = Omega^1_X(log D), E = A / f^*L, omega_f = K_X (x) f^*K_B^-1, H = 2 S_1 + 3 S_2, G = R^1 f_* O = O gamma + O(-1).

## A1.1 (local freeness and the determinant line): holds as stated

Statement: A and E are locally free of ranks 3 and 2; the vertical field xi is a nowhere-zero section of the dual of
E; 0 -> N -> E -> O_X -> 0 is exact with N = det E = omega_f(-2 S_1 - 3 S_2).

What I checked.
- A is locally free: D has normal crossings (locally t_c = x, xy or xyz at the cusp fibre; the S_j are smooth), and
  the logarithmic cotangent sheaf of a normal-crossings divisor is locally free, also when the divisor is
  irreducible and crosses itself. The proof says this ("no simplicity of the global divisor is assumed").
- f^*L is a line subbundle of A that is locally a direct summand: at the cusp its generator is the sum of the
  logarithmic basis forms; at S_j it is m_j dlog(sigma) plus a holomorphic form, sigma a local equation of S_j, and
  its coefficient m_j on the basis element dlog(sigma) is a non-zero constant. The proof does this on the free
  cyclic cover, which is the same computation. So E is locally free of rank 2.
- xi is non-zero in the relative logarithmic tangent bundle everywhere: constant and monodromy-invariant on the torus
  family (delta is the invariant vector), constant on the covers at S_j, and a constant element of the rank-two
  lattice of invariant logarithmic fields on the toric charts at the cusp. That xi vanishes as an ordinary vector
  field on one double curve does not matter, as the proof says.
- The determinant: det E = K_X(D) (x) f^*L^-1 with f^*L = f^*K_B (x) O(W + 3 S_1 + 4 S_2), so
  det E = omega_f(D - f^*Sigma) = omega_f(-2 S_1 - 3 S_2). Redone; correct.

## A1.2 (the logarithmic direct images): holds as stated

Statement: R^q f_* E = O + O(-1), O^2 + O(-1)^2, O + O(-1) for q = 0, 1, 2, compatible with base change to every full
scheme fibre.

What I checked.
- R^q f_* O(H). Near p_j the direct image is the invariant part of the direct image on the cyclic cover, where
  O(H) is s^-(m-1) O. For the trivial character the least invariant exponent stays 0; for the character of b_1 it
  drops from a to a - m, that is, by one power of t_j. So one upper modification at each finite point on the
  O(-1) summand and on R^2: f_* O(H) = O, R^1 = O + O(1), R^2 = O(1). Redone with (m, a) = (3, 2) and (4, 1);
  correct. The splitting uses H^1(O(-1)) = 0.
- Duality. R^q f_*(omega_f(-H)) is the dual of R^(2-q) f_* O(H): f is flat with Gorenstein fibres (Cartier
  divisors in a smooth threefold), Serre duality holds on every scheme fibre, the fibre dimensions are constant, so
  both sides are locally free with base change and the cup-and-trace map is an isomorphism. This gives
  (f_* N, R^1 f_* N, R^2 f_* N) = (O(-1), O + O(-1), O). Correct.
- The connecting maps of 0 -> N -> E -> O -> 0 vanish: the sequence splits on every regular fibre, the maps are
  morphisms of vector bundles, and they vanish on a dense open set. Correct.
- The three extensions: O by O(-1); G by O + O(-1); O(-1) by O. The extension groups are sums of H^1(O(-1)),
  H^1(O), H^1(O(1)), all zero. So the three bundles are as stated. Redone; correct.
- Base change for R^q f_* E follows because all three direct images are locally free.

## Two remarks, neither a gap

- The paper should cite a standard source for analytic relative duality (the proof gives the fibrewise argument,
  which is enough) and for cohomology and base change in the analytic category (Grauert).
- A1.2 takes the characters (1, zeta^-a), (m, a) = (3, 2), (4, 1), from A1.0. I read A1.0 as well: its degree count
  (the quotient line Q with Q^12 = O(-p_0) from the discriminant; R^2 f_* O = det V; coarse degree -1) is correct
  and agrees with [AC26] Proposition 9.13 and with arXiv:2610.00250v1 (`p2:prop:structure-direct-images`).

## Also read: A1.3

The residue sequence 0 -> Omega^1_X -> A -> nu_* O of the normalization of D -> 0, its direct images, and the
cancellation of the two torsion summands are correct as far as they go; they use A2.1, A2.2 and A2.4 (the maps
kappa_0, kappa_1 and the scalar), which the intake read. f_* Omega^1_X = O(-2) checks: the kernel of evaluation
O(1) -> C^3 with multipliers 1, 3, 4.

## Consequence

Both statements hold. Sections 5.1 and 5.2 of the paper stay theorems, and the writing prompt
(`s6_pro_prompts_20261112\07_S6_PAPER_WRITING\PROMPT.md`) is unchanged. With the intake's readings of A1.3, A2.1,
A2.2, A2.4 and A3.1, every statement under the Hodge table has now been read once outside the producing run.
