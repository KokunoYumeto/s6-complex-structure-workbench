# Independent referee: B.4.24 associated log-torsor obstruction

Referee: boundary_d. Date: 2026-11-15. Full source read:
`B_log_torsor_obstruction.tex`. Verdict: PASS in the stated fixed
associated-log-torus category; no unrestricted analytic-cap conclusion.

I independently opened the original Kajiwara–Kato–Nakayama paper at
https://www.ms.u-tokyo.ac.jp/journal/pdf/jms150104.pdf . Section 1.2.2
explicitly uses ordinary open covers with the induced log structure.
Sections 1.3.1–1.3.4 define the bounded-character quotient, so its
restriction to the underlying analytic site gives the exact sequence
used in the proof. Theorem 5.3.2 distinguishes the proper fan model
A(Sigma) as a subfunctor of A; the source now preserves this distinction.

The diagonal monoid pairing (q,q+12r) passes every face test of
Definition 1.2.3; the residual unit pairings are nondegenerate after
shrinking. The real-log determinant has the stated positive sign.
The two marked origins check directly: B.4.9's actual sigma has no
q-log and is a genuine unit gauge along q=0; the normalized root
pullback on q nonzero recovers the rotating root fan with its
extending (1,1) origin, because the twelfth affine deck is already
a full lattice period. My initial recollection of a sigma representative
containing an s v term was incorrect; I reread B.4.9 and withdrew
that concern before accepting this proof.

The connecting class of F has r-loop component gamma. On B_r,
applying Q-order to a lifting cocycle gives a coboundary, while its
map on constant-lattice first cohomology is diag(12,12), hence
injective. On B_q the r loop contracts. No difference of extending
axial sections can therefore equal F. The same calculation after
q=Q^(12m), r=R^n has nonzero n gamma and injective diagonal ghost
map. A finite Kummer chart is dominated by a coordinate-root chart
by clearing the denominators of its finite set of monoid generators.

The ordinary gauge k v delta is not an extending q-log section,
so the exact raw cancellation F-sigma-k v delta does not undo this
fixed-category obstruction. The source explicitly leaves arbitrary
proper caps with vertical threefolds outside its conclusion.

Primary retrieval audit: turn574view0 (original full PDF),
turn574view1/2 (definitions and proper-model theorem),
turn575view0 (usual-open topology and face definition),
turn575view1 (bounded-character quotient), and turn575view2
(A(Sigma) subset A and properness). Existing key KKN2008Root reused.
