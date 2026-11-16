# Frame comparison supporting D.2.44

The unnumbered proof is `code/maps_D2_frame_proof.tex`. It is an independently
auditable input for the fourfolds-owned theorem, not a duplicate register row.

## Primary sources inspected

Steve J. Kaplan, *Constructing framed 4-manifolds with given almost framed
boundaries*, Trans. Amer. Math. Soc. **254** (1979), 237–263,
DOI 10.1090/S0002-9947-1979-0539917-X.

The original journal scan was opened through the primary-paper mirror at
https://scispace.com/pdf/constructing-framed-4-manifolds-with-given-almost-framed-1vq4kmmbg3.pdf
The verified source is the complete 27-page original journal scan.
The publisher URL returned HTTP 403, which is an access result only.
A guessed Ranicki `kaplan.pdf` download was initially assigned the local
cache name, then rejected on inspecting its first page: it was Kaplan's
different 1982 knot paper. It is not evidence for this theorem, and its
external cache files have been renamed `maps_kaplan82_slice.pdf` and `.txt`.
Direct HTTP download of the correct mirror returned an empty response;
the full primary text and screenshots were instead inspected through
the web PDF reader. No local 1979 PDF is claimed at this stage.

Exact locations read: Definition 1.7 and Remark 1.8, printed p.239; the
relative second-Stiefel–Whitney obstruction paragraph and Definition 1.10,
p.240; Theorem 3.1 and its complete constructive proof, pp.243–246;
Example 3.2, p.246. The introduction on p.237 explicitly states that the
constructed fillings have one zero-handle and all other handles of index
two. Remark 1.8 identifies almost framings with the specified H1(-;Z/2)
choice. Example 3.2 explicitly distinguishes the exceptional spin structure
on T³ with index-eight filling. These are exactly the features needed for
the spin-compatible ambient surgery, and exclude a tacit use of the wrong
Borromean spin structure.

Web retrievals: `turn434view0`, `turn437view0`, `turn437view1`.

A. V. Zhubr, *On the definition of the exotic invariant for simply connected
closed six-dimensional spin manifolds*, Izvestia Komi **4(16)** (2013), 4–10,
was read from the full original issue already cached externally as
`primary_Zhubr13_issue.pdf` and `.txt`.
Lemma 1, printed p.5, gives π3(V6,3)=Z/2, π4(V6,3)=0 and the index-two map
π3(SO3)→π3(SO5). Theorem 1, p.6, identifies the obstruction for fields
nontrivial relative to embedded torsion spheres; Section 5, pp.8–9,
supplies the actual quaternionic surgery proof. Conjecture 1 on p.6 is
explicitly *not* invoked. Instead, the Spin6/Spin3 Serre transgression proves
the required Bockstein identity for the globally trivial ambient bundle on
the punctured manifold.

## Exact checks and remaining audit

`code/maps_D2_frame_checks.py` verifies the actual xy and xyz syzygies,
the Hilbert–Burch maximal minors at the triple point, the unit Bott matrix,
and all seven row parities. It does not substitute for the embedded
spin-surgery argument. The latter is given in full in the proof and was
sent to root and fourfolds for independent review before integration.
