# A.3.3 — derivation before reading the receiving proof

Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation.

The receiving proof and its historical check-record narrative have not been opened for this derivation. The statement/Uses packet was opened; A.3.1 is an already checked input. PDF visual QA exposed A.3.2 and other separately recorded pages, not A.3.3. This note proves precisely the stated finite-translation/lifting assertion and no adjacent assertion.

## 1. Actual translations

Put I=O_Y(-S), with the specified effective Cartier divisor S. For j=0,...,m-1 the map tau_j on Pic(Y) sends B to B tensor I^j. Given transition functions b_ab for B and i_ab for I, its output has transitions b_ab i_ab^j. Multiplication by i_ab^(-j) gives the inverse tau_-j, including the identity isomorphisms on cocycles. Thus these are mutually inverse holomorphic translations of the Picard space (tensoring an analytic family by the fixed line I^j gives the corresponding analytic family); on the components named in the assertion they are homeomorphisms. No component is silently identified with a different component.

For a preserved component P and the given dense open U in P, V_j=tau_j^(-1)(U) is open and dense in P. Their finite intersection V is dense: if W is any nonempty open in P, intersect successively with each V_j. At every step the previous intersection is a nonempty open and meets the next dense set. This proves density without an irreducibility assumption. V is open as a finite intersection.

For a finite union of relevant components, fix each source component P_a, use the dense open U_{tau_j(P_a)} in the actual target component, and set V_a=intersection_j tau_j^(-1)(U_{tau_j(P_a)}). The same proof applies in P_a. The union of these V_a is relatively open and dense in the finite union, with the component translations retained in the formula.

## 2. Actual restriction and layer maps

Take B in V and write E=Omega_Y^1 tensor B. Since Y is a complex manifold, E is locally free. On S, I|_S is the conormal line N^*. The explicit multiplication map supplied in A.3.1 identifies I^j/I^(j+1) with (I|_S)^j: a local generator s of I sends a tensor of j copies of its conormal class to s^j mod I^(j+1). Replacing s by h s multiplies both sides by h^j, so the map is independent of the chosen equation.

Consequently the j-th layer G_j=E|_S tensor (N^*)^j is the restriction to S of Omega_Y^1 tensor tau_j(B), through the actual tensor-associativity map and the multiplication map just described. B in V implies tau_j(B) in U, hence H^0(S,G_j)=0 for every j=0,...,m-1. This uses exactly the defining property of U.

## 3. Induction retaining all extensions

For k=2,...,m, multiplication of ideal powers and quotient of the truncated module give the exact sequence

0 -> G_(k-1) -> E tensor O_(kS) -> E tensor O_((k-1)S) -> 0.

The first arrow sends a tensor represented by e tensor a s^(k-1) to the same tensor modulo s^k. The second is reduction modulo s^(k-1). Local freeness preserves this sequence. Begin with H^0(S,E|_S)=H^0(S,G_0)=0. Left exactness gives

0 -> H^0(S,G_(k-1)) -> H^0(kS,E|_(kS)) -> H^0((k-1)S,E|_((k-1)S)).

Both outside groups vanish at each induction stage, so the middle group vanishes. At k=m this is exactly the full-fibre ambient vanishing asserted in A.3.3. No splitting or vanishing of a connecting map is used, and every nilpotent layer remains present.

## 4. Fresh bounded computation

A newly written exact rational program checks unsplit finite filtered Cech-degree-zero maps: injective diagonal layer maps, arbitrary off-diagonal couplings, and the induced filtration quotients. It also checks actual finite component-translation permutations and their inverses. These finite tests verify only their stated cases; the universal assertion is proved in Sections 1–3. This code does not read an earlier producer, its output, or the receiving proof.

## 5. Source scope

The actual Cartier multiplication and left-exact cohomology maps are the same precisely identified input maps already opened for A.3.1: Stacks Divisors Lemmas 31.15.2 (Tag 0B3P) and 31.15.3 (Tag 0C4T), p.26, and Cohomology Tag 01DZ, pp.2–3, in the preserved PDFs. The analytic specialization is the local multiplication by a nonzerodivisor and unit transition calculation written above. The finite dense-open argument and the Picard cocycle inverse have been proved explicitly here. This is a supporting result; no new main-result priority claim is made.
