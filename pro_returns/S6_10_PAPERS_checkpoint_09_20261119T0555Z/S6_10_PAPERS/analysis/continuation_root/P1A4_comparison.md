# P1A.4: full prereading proof and exact comparison

19 November 2026. GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro.

## Chronology

`P1A4_before_read.md` was completed at 05:23:09 UTC before the target
proof was opened. The independent integral program and its output were
already complete at 05:19:22–23 UTC. Their frozen hashes and timestamps
are in `P1A4_replacement_receipt.json`. Only the clean statement and
construction packet was used. No prior producing program was read.

The target extraction inadvertently also exposed P1.17, which appears
between P1A.4 and P1A.5 in the body. This exposure grants no root
prereading credit to any P1.17 step and is recorded here for later
review assignments.

## Step comparison and changes

1. **Algebraic reduction.** The root proof derived the divisor
   restriction directly: invariant alternating forms J satisfy
   A^tJA=J=B^tJB, and the exact fifteen-variable system has zero
   kernel. The printed proof used the stronger global H2(M;Z)=0
   input. Its opening has now been replaced by the independently
   derived restriction argument, with the same positive divisor
   pairing and proper graph descent. This changes no conclusion and
   removes reliance on the separate global topology calculation for
   this step. The graph map and its exact proper-image citation are
   now explicit.
2. **Linear parts.** The common integral commutant and the finite
   affine obstruction agree. The new code independently solves all
   thirty-six commutator variables and obtains QI. Applying the actual
   invariant covector to the order-five affine equation gives 2/5;
   the extra order-four check gives -1/2. Both obstruct -I. The code
   reference now names the independent continuation program.
3. **Translation sheaf.** The root derivation includes every special
   stalk: the equivariant torus evaluation sequence on finite root
   covers, and removal of integral cusp valuations by actual period
   deck maps, followed by logarithms of holomorphic units. The finite
   root descent is now explicit in print. Its cohomology stays on the
   orbifold, so finite stabilizer torsion is retained.
4. **Integral parabolic cohomology.** The root derivation eliminates
   the cusp coboundary and identifies the cohomology with
   (ker N1 intersect ker N2)/(B-I)ker(AB-I). The paper now prints its
   primitive bases K,T and actual 3-by-3 relation matrix Z, with Smith
   factors (1,1,2), so this argument is fully in the paper. The former
   eleven-generator presentation is preserved. A separate fresh
   post-comparison program constructs its matrices from the supplied
   monodromies and computes explicit maps X,Y and integral H,R with
   YX=I3, I6-XY=coboundary*H and Y*coboundary=Z*R. These identities
   prove the two quotient presentations are isomorphic. The larger
   matrix has Smith factors (1,1,1,1,1,2). This comparison program was
   written after target exposure; its chronology is not described as
   prereading.
5. **Group splitting.** The root prereading proof gave a canonical
   order-two element by dividing the double of any component lift in
   the additive identity subgroup. The printed proof instead gives
   the explicit half-period tau. That additional representative has
   been assigned to the fresh VI reviewer, who saved its independent
   derivation before opening the isolated printed step. Its separate
   comparison receipt is required for the aggregate current-proof
   gate; the root alternative argument is not used to claim that
   representative was checked before it was read.
6. **Parameter equality.** The same intrinsic-base argument applies
   to an isomorphism between two members. The scalar linear parts
   carry the actual graph planes to one another exactly at equal
   parameters. This matches the root prereading proof, with the
   common w2,w1,w0,e frame and nonzero parameter coefficient specified.

## Programs and opened source

`code/continuation_root/P1A4_integral_fresh.py` uses explicit unimodular
Euclidean row operations for primitive integer kernels, a direct
commutator system and a direct alternating-form system. Its exact
output passes every check. The independent post-comparison file is
`P1A4_cochain_comparison_fresh.py`, with all actual matrices and maps in
its output. Neither reads an older producing program or its exports.

Remmert's proper-image theorem was opened in Grauert (1960), Section7,
Satz1, printed p.60. The text explicitly credits Remmert and proves
the theorem there. The reduced compact meromorphic graph and the map
to P1 times P1 satisfy its stated hypotheses. The exact short source
statement and a rejected search-snippet mismatch are preserved in
`literature/Grauert1960_proper_image_receipt.json`. The bounded renewed
main-result credit comparison remains the V owner's recorded event.

## Preserved material

The complete former proof is retained as
`P1A4_superseded_proof.tex`. The replacement records its precise maps
to the current proof and asserts no fault in the prior route. The
explicit half-period paragraph is unchanged pending its separate
fresh-review receipt. The theorem's hypotheses and conclusions are
unchanged.
