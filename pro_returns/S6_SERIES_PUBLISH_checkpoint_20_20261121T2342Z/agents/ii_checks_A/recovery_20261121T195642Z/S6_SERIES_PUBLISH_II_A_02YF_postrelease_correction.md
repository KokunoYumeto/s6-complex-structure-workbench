# 02YF: explicit postrelease correction to the independent derivation

This record is written after release of the printed target proof. It preserves
the original frozen derivation, SHA256
`e288245f431add9a6d7a5e5487e348da7cb548d58a7418d5942c05f1aed7d7df`,
without alteration. It adds no independent-check event or prereading credit.

Section 2 of that derivation states: “Thus R0 is connected, and collapsing each
rational fibre to its attachment point is a homotopy equivalence R0→H.”
The asserted homotopy equivalence is too strong when a rational fibre is
present. The required assertion about the induced fundamental-group map is
correct, with the following precise maps and proof.

Write R0 as the smooth section H together with the distinct ruling fibres
F1,...,Fv, each isomorphic to P1, with Fj meeting H at its own single transverse
point pj and no other Fi. Let i:H→R0 be inclusion. Define q:R0→H by the identity
on H and the constant map with value pj on Fj. These maps agree at every
attachment point and therefore define a continuous quotient map, with
q∘i=id_H. Van Kampen, using small connected neighbourhoods of H and each Fj
whose intersection retracts to pj, gives

π1(R0)=π1(H)*π1(F1)*...*π1(Fv)=π1(H),

because every Fj is simply connected. The displayed isomorphism is i_* itself;
q_* is its inverse by q∘i=id_H. Composing i with R0→T0 is the actual section of
the P1-bundle T0→B, so the inclusion R0→T0 induces the same isomorphism to
π1(T0) as the section. This proves exactly the topological conclusion used in
the target and in the subsequent blowup induction.

For the higher homology, Mayer–Vietoris at the same one-point attachments gives

H2(R0;Z)=H2(H;Z) ⊕ ⊕_(j=1)^v Z[Fj].

The actual induced map q_* on this direct sum is (a,b1,...,bv)↦a, and i_*
maps a to (a,0,...,0). In particular q_* kills each nonzero fundamental class
[Fj]. A homotopy equivalence induces an isomorphism on integral H2; this
explicit kernel proves the limitation of the former stronger assertion when
v is positive. The Euler calculation in the frozen derivation is unaffected:
e(R0)=e(H)+v, since each P1 adds 2−1. The new postrelease cellular program
`code/S6_SERIES_PUBLISH_II_A_02YF_quotient_cells_postrelease.py` records these
actual chain maps and images. The displayed argument proves the formulas for
every v; finite program examples are certificates of the stated maps, not a
replacement for that proof.

The original printed proof, item 4, claims only the fundamental-group
isomorphism. The proposed source retains exactly that claim and its blowup
transport. Neither original nor proposed source contains the incorrect
homotopy-equivalence assertion. The comparison and event proposal disclose
this correction to my independent derivation rather than assigning it to
the manuscript or silently changing the frozen evidence.
