"""Write the A/B statement ledger from explicit reviewed descriptions."""
import csv
from pathlib import Path
root=Path(__file__).resolve().parents[1]
fields=['id','statement','status','where_proved','depends_on','item_of_the_prompt','R_items_and_Leads_used','notes']
entries=[
('A.1.1','The prism cones form a fan with the stated period shears and chart xy=uzv, q=zv.','Proved','','A.1','R8; R10; Lead 2','Exact character monoid and fan proof.'),
('A.1.2','A proper flat global nodal plumbing has central fibre Q and contracts exactly the chosen diagonal (-1,-1) curve of Engel X(u).','Proved','A.1.1','A.1','R8; R10; Lead 2(i)','Direct compact-core construction; independently reviewed.'),
('A.2.1','Exactly two smooth refinements exist with fixed bottom, joint flatness and reduced central divisor; without joint flatness infinitely many exist.','Proved','A.1.1','A.2','Lead 2(ii); Lead 3','The no-new-ray enumeration is exhaustive; unrestricted two-model assertion is false.'),
('A.2.2','The two minimal refinements yield smooth proper flat semistable fillings with explicit normalized nodal-curve blow-up and small resolution.','Proved','A.1.2; A.2.1','A.2','R10; Lead 2(iii)','Central fibres irreducible; conductor S; no triples; T1=O; side flops specified.'),
('A.3.1','The Euler number in a proper flat analytic lci smoothing equals the virtual top Chern number of its reduced central fibre.','Proved','','A.3','Lead 1','Perfect topological K-class and radial triangulation; Levy08 and Loj64 independently checked.'),
('A.3.2','Q has virtual Euler number zero and cannot be a central fibre of Engel X(u), even without a map to B.','Proved','A.3.1; A.1.2; A.2.2','A.3(i)-(ii)','R10; Lead 1; Lead 3; E26 Conjecture 8.2','Refutes Conjecture 8.2; corrected nodal and semistable alternatives constructed.'),
('A.3.3','Unrestricted uniqueness of the two semistable fillings is false, even with joint flatness over B times the disc.','Refuted','A.2.2','A.3(iii)','Lead 3','Horizontal centre over 2P gives arbitrarily many further smooth reduced-NC fillings.'),
('A.4.1','Integral homology, fundamental groups and Euler numbers of Q and the two minimal central fibres are tabulated without torsion.','Proved','A.2.2','A.4','R10; Lead 2(iii)','Q Betti (1,1,8,7,10,0,1); corrected (1,1,9,7,11,0,1); pi1=Z; Euler 12 and 14.'),
('A.4.2','Untwisted X(u) has free homology with Betti (1,1,8,14,8,1,1); N squared is zero, rank six, with nonzero Smith entries 1,1,1,1,1,11 on H3 and identity elsewhere.','Proved','A.4.1; A.2.2','A.4','R10','Integral Thom/Gysin/Mayer-Vietoris computation; exact E8 and Smith certificate.'),
('A.4.3','The nodal nearby Euler function is one everywhere on S_infinity and zero on its complement in the conductor; it is zero on the conductor of the semistable models.','Proved','A.1.2; A.2.2','A.4','Lead 1','Corrects pointwise/integrated confusion on C*; nearby Euler numbers 1 and 2.'),
('A.4.4','Untwisted fibres and corrected normalizations are non-Kahler; the monodromy filtration in degree three has graded ranks 6,2,6.','Proved','A.4.1; A.4.2','A.4','Lead 1','No polarized limiting mixed Hodge structure or classical Kahler Clemens-Schmid is asserted.'),
('B.1.1','The product assertion over a finite root disc is false; the actual semiabelian bundle admits a smooth proper flat twelve-cycle filling after u=r^12.','Refuted','A.1.2','B.1','R8; R11; Lead 4','Product specialization holds only after the special torsion isogeny.'),
('B.1.2','The finite generators extend freely across the twelve-cycle with shifts +4,-3; the smooth quotient has multiplicities 3,4 and stated normal characters.','Proved','B.1.1','B.1','R1; R2; R11; Lead 4','All nonidentity powers checked on components and nodes; local punctured-family gauge explicit.'),
('B.2.1','The plain u=r^n cusp fan has n+1 joint-flat reduced smooth bridge refinements: 13 at n=12 and 3 at n=2; cusp component monodromy is trivial.','Proved','A.1.2; A.2.1','B.2','Lead 2; Lead 5','Exact common-face, volume, determinant and periodicity certificates.'),
('B.3.1','The finite-place models and plain cusp model cannot glue because their component monodromies violate the peripheral relation.','Refuted','B.1.2; B.2.1','B.3','Lead 5','Plus/minus 4 plus/minus 3 never equals 0 mod12; independently reviewed.'),
('B.3.2','A corrected twelve-cycle assembly requires cusp shift -1; its connected component cover has degree12, ramification (3,4,12), genus3.','Proved','B.3.1','B.3','Lead 5','Necessary condition only; no central threefold is inferred.'),
('B.4.1','Existence of a corrected global S6 filling, equivariant descent, resolution, multiplicities and least semistable exponent.','Open','B.3.1','B.3-B.4','R2; Lead 5','Alternative cusp constructions and the two-logarithm overlap remain under investigation.'),
('B.5.1','Topology and nearby-cycle/Hodge comparison for an actual corrected global S6 limit and its descent resolution.','Open','B.4.1','B.5','Lead 5','No invariants assigned before construction.')]
target=root/'sections'/'AB_push_results.csv'
with target.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields)
    writer.writeheader()
    for ident,statement,status,deps,item,used,notes in entries:
        writer.writerow(dict(zip(fields,[ident,statement,status,'sections/AB_push.tex, '+ident,deps,item,used,notes])))
print('Wrote',len(entries),'statement rows to',target)
print('Statuses:',{s:sum(e[2]==s for e in entries) for s in sorted({e[2] for e in entries})})
