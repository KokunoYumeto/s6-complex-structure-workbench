# P1A.2: complete direct-residue derivation and printed comparison

19 November 2026, GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro.

The complete independent derivation in `P1A2_before_read.md` was written
before the target proof was opened. Its frozen SHA256 is
e7c40e6c4a84f83483577724d0c6decf543b809d40056654c124e0693e68b49c.
The prereading exact program and its successful output are preserved
byte-for-byte as `P1A2_hodge_fresh.prereading.py` and
`P1A2_hodge_fresh.prereading.output.json`. Their SHA256 values are
0b3cea29a5cb3dc6ed963e795d81f4142ca3636095fd2c7c9a34cfb9688986fc
and6d1d48c57df58221f70a31c32fb4f4938187c06474ce866f29358c1f173f813d.

Every new geometric and connecting-map step in printed steps1--8
matches the prereading derivation. In particular:

* The quotient projection is (x_e+r x_w0,x_w-1,x_w-2). Its derivative
  gives the actual connection residue Q; reversing the F basis by
  the permutation(2,1,0) and substituting z=-625 pi c/128 gives exactly
  the printed R, entry by entry. The post-comparison additions to the
  new program verify this explicit change of basis and both printed
  determinant identities without reading the old producing program.
* The local deck-period derivatives give the logarithmic cotangent
  extension and its exterior connecting maps. The independent line
  weights, monomial frames, absolute cohomology dimensions and ranks
  agree with the paper's displayed arrays.
* The unique exceptional point pi c=5/3 is excluded by the separate
  P1.16 point bound h_b(1)<-1 and P1.8 admissibility. The polynomial
  matrices have that same single zero over the complex parameter line;
  excluding this real point also handles the complex parameter family.
* The branch-normalization residue complexes, toric acyclicity, seven
  opposite pairs and degree-zero rank2 map all match. The independent
  proof additionally computes the degree-one residue map as the
  quadratic evaluation v -> m(v)g(v). Its six-dimensional
  symmetrization determinant is nonzero on the admissible domain,
  so it obtains h22=6 directly from the long exact sequence.

The original printed step9 instead obtains h22 by the analytic
Riemann--Roch polynomial after applying Serre duality. That particular
universal polynomial was not written in the root prereading derivation.
The full direct-residue proof of the statement is independently
re-proved, while the requested every-printed-step chronology for the
additional RR route was explicitly assigned to the fresh ledger
reviewer before that reviewer read it. Its separate receipt governs
that step; the root record does not silently award it prereading credit.

Classical sources reopened by the root: Cox--Little--Schenck,
Theorem9.2.3, printed p.410 of the September2010 prepublication text,
read in the primary-host indexed original-text result. The direct PDF
request returned403 and is not claimed successful. Its zero nef
divisor and convex complete fan hypotheses hold for the actual cusp
normalization and every double-stratum normalization. Serre1955,
Section13 Theorem4, printed p.22, and the wedge/cup pairing in
Section15, p.23, were opened in the original scan; the theorem applies
to compact complex manifolds and holomorphic vector bundles. No
Kähler hypothesis is inserted. The shared bibliography's formerly
unverified Serre entry has now been updated at precisely this scope.

The main-result credit check belongs to the Paper V owner's renewed
eighteen-row source comparison. It positively credits the DGKXv1
conductor/KS method and the actual Yang cusp-construction specialization.
This root receipt supplies the newly required exact specialization
and its maps, rather than claiming those earlier methods as new.
