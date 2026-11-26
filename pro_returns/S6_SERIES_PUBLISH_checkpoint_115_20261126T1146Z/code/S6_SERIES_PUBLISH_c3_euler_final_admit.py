"""Record the complete Euler-proof comparison and bounded local closures."""
from S6_SERIES_PUBLISH_c3_edit import *
import hashlib

s=SOURCE.read_text();a=s.index(r'\section{Euler sign and equality for arbitrary torus fibres}');b=s.index(r'\clearpage',a)
unit=s[a:b]
assert unit.count(r'\item ')==7
assert r'\tag{C.G.' not in unit
assert r'\SeriesRef' not in unit and r'\ref{' not in unit
assert 'Its equality characterization says that' in unit
assert all(r'\label{'+x+'}' in unit for x in ['sec:II:all:12','cdp:st:C.2.G.1','cdp:eq:C.G.1','cdp:eq:C.G.2'])
add_event('cdp:st:C.2.G.1','II-C3-EULER-COMPLETE-TEXT-COMPARISON','used and rechecked in this run',
 'Root read the entire original and receiving Euler theorem and all seven proof steps. The statement keeps b1=b2=0, arbitrary full multiplicities/singularities, exact values0/2, rational irreducible value2, all other irreducible value0, and both directions of the conductor equality criterion. Same-map receiver checks read the standing definition, A.3.4 root-cover paragraph, P4.26/P4.32 local clauses and Hopf/class-VII statements. The Kähler classification application now specifies canonical intersections, area and the degree-m unramified Euler formula. The normalization open isomorphism is explicit. The two equation targets and all statement labels persist. Seven items replace one item with manual step labels. All25 classes were reviewed in this complete unit; final global placement/front correspondence, rendered typography and the pending full INT1–3 receiving admission stay open. This is a used-and-rechecked comparison, not an independent reproof, required-check refresh or final-page reading.',
 'Complete Euler theorem; code/S6_SERIES_PUBLISH_c3_euler_final_text.py/.out; exact syntax defect row',source=__file__)
append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',[
 dict(source='Peters2021-third-continuation-Euler-classification',
 url='https://nyjm.albany.edu/j/2021/27-32p.pdf',version='Published New York Journal of Mathematics27(2021),840–847',
 locus='Section2 setup and complete Proposition2.1, p.842; complete Theorem2.2 and classification table, p.843',
 date_utc=now(),sha256=hashlib.sha256(Path('/workspace/scratch/9fcd229a9ed4/tmp/Peters2021_c3.pdf').read_bytes()).hexdigest(),
 own_word_summary='The even first Betti number criterion identifies the Kähler compact surfaces. The classification lists the negative-Kodaira classes and their first Betti numbers, and identifies tori as the Kodaira-dimension-zero class with b1=4.',
 use='Apply Proposition2.1 to the central normalized-root cover with transported b1=4. Its rationally trivial c1 excludes exceptional/ruling curves and positive pluricanonical growth by explicit Kähler-area pairings; Theorem2.2 then selects the torus. Apply the negative-Kodaira portion to the same normalization resolution Z. The source states and cites these background facts; no proof of the classification or full article reading is claimed.')], 'source')
excluded={'D10','D14','D15','D16','D23','D24','D25'}
for n in range(1,26):
 kind=f'D{n:02}'
 if kind not in excluded:
  set_unit_status('sec:II:all:12',kind,'done',
   'Complete old/receiving unit read against all25 classes; all found instances of this class are logged. Same-map local statements and the exact Peters classification loci were read. Final placement, first-part correspondence, rendered typography and INT1–3 receiver completion remain in their open rows.',
   'CHECK_EVENTS.tsv: II-C3-EULER-COMPLETE-TEXT-COMPARISON')
print('Complete final Euler proof comparison recorded;18 stable local defect rows closed. D25 interface receivers and final global/rendered rows remain open.')
