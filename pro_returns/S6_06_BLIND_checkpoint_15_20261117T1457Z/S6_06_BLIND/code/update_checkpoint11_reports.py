"""Record the audited eleventh-hour mathematical progress in the report source."""
from pathlib import Path

root=Path(__file__).resolve().parents[1]
p=root/'code/update_report.py'
s=p.read_text()
s=s.replace("P3F.1–P3F.2, P3F.16–P3F.54, P3K.6–P3K.36", "P3F.1–P3F.2, P3F.16–P3F.56, P3K.6–P3K.38")
s=s.replace("Its relative smooth return remains under computation.",
            "P3F.55–56 now compute its actual relative smooth return on the specified vertical-edge fan, including the full circle-line, normal-frame and source-collar comparison.")
old="The component-supported shorter loop and the general source/cap-data loop transports remain under proof; no uncomputed loop is assigned a class."
new=("P3K.37 constructs the component-supported OS49 shorter scalar loop lambda=w^k, "
     "with pair(-2k,-8k), relative coordinates(2k,0,0), and all-fan class k*(S-1)*(S-3)/4. "
     "As the order and fan vary its exact range consists of every even class modulo28. "
     "P3K.38 proves intrinsic minimality of the scalar cover: for all thirty canonical fixed-source branches every biholomorphic endpoint winding is a multiple of M/b, and this bound is attained; for the component-supported OS49 branch the minimum is k. "
     "The proof retains the full good-cap and reduced-cap Albanese lattices and applies to arbitrary endpoint biholomorphisms. "
     "P3F.55 computes the exact lifted link of (s,rho) mapped to (s^2-rho^2,s*(s^2-rho^2),rho): its double-link linking is1, the required tangent push has Ekholm invariant2, and the literal Whitehead-to-Stiefel arrow gives coefficient1/2. "
     "Its Haefliger invariant is1. A nonzero punctured-Kummer test identifies the two published invariant normalizations with every sign fixed. "
     "P3F.56 carries the actual closed twofold E7 source family to that link through an embedded trace, the actual Hopf circle line, an explicitly capped S4 correction, and both boundary orientation reversals. "
     "On the standard vertical-edge fan, both one-cap E7 sectors have positive source-loop class1, a nonproduct sphere mapping torus, and an obstruction to smooth descent through the degree-two source cover. "
     "The remaining source puncture v=0 is being attacked by its marked simultaneous small resolution, the normalization blowup, exact Cartier-line specialization and source-Hom winding. "
     "The actual source-suspension transport across its component flop is still under proof, as are general remaining source/cap-data loops and the other-fan transports of the new source loop; no uncomputed loop is assigned a class.")
count=s.count(old)
assert count==2, count
s=s.replace(old,new)
p.write_text(s)
print('Updated both current-state report passages and the Part3.4 statement range.')
