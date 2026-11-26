#!/usr/bin/env python3
"""Write bounded, explicit existing-row D24 proposals; never change central data."""
from pathlib import Path
from datetime import datetime, timezone
import csv, re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation4_horizontal'
s=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
units=list(csv.DictReader((ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv').open(),delimiter='\t'))
stamp=datetime.now(timezone.utc).isoformat(timespec='seconds')

# Every group is an explicit list of stable unit keys. Current status alone is
# never used to select a unit for completion. A source locator and an admitted
# whole-unit D12 record are required below for each individual proposal.
groups=[
('front-II-row', '''the-series-and-this-paper''',
 'The current Paper II series-table entry names the Campana--Demailly--Peternell argument and the sign theorem for all degenerations. Main A supplies the exact integral-CDP normalization criterion; main C/G1 supplies the arbitrary-multiplicity compact Betti-zero sign theorem. The full series paragraph/table was read and its other-paper rows remain unchanged. This proposal concerns the current Paper II front/body description; the final five-paper coordination gate remains separately required.'),
('front-known-new', '''known-and-new''',
 'Each A-G entry names a conclusion actually stated and proved by the current main/body owners: A conormal/normalization, B integral counts and three-type classification, C unrestricted sign/equality, D parity and fixed-punctured-family refinements, E twists/ranks, F the stated open twelve-tooth and deformation conclusions, G the fixed-data minimal covering. The full table was read with the root main-statement and exact outline comparisons. Literature/provenance criteria are separately recorded; this is the D24 body-correspondence criterion.'),
('smooth-classification', '''sec:II:fibre-properties
sec:II:secondary-surfaces
sec:II:elliptic-exclusions
sec:II:kodaira-exclusions
sec:II:inoue-exclusion
sec:II:fibre-classification
sec:II:complete-fibres''',
 'Part I explicitly promises the smooth-fibre classification and contains this unit. Main B and all four B outline steps were compared with C3.1, C3.6-C3.12 and D2.7. The identity on the same smooth fibre gives the tangent/Chern calculations; the exact Albanese, Picard, period and meridian maps supply the exclusions; the quotient/filling maps give the occurrence clauses. Rational Betti assumptions and the stronger integral clause remain exactly as stated in B.'),
('global-tests', '''cdp:st:C4c''',
 'Part I ends with the global normalization criterion, and this unit is its global-cohomology test subsection. Main A and outline A4 were compared with the complete C4f and P263 proofs; root also read C4c completely. The same full fibre, Picard component and full Cartier filtration connect these tests to the stated criterion. The current route points to the actual final normalization-criterion section.'),
('direct-images', '''sec:II:direct-image-comparisons''',
 'The Part I route explicitly includes direct-image calculations. Main A and outline A5 use the same Poincare family and O_P1(-2) tensor in E12 and the exact divisor/associated-component morphisms in E17. Both complete proofs were read, and the existing complete-unit record covers the remaining direct-image examples and full-Cartier comparisons. The reader route names their actual part without asserting a broader vanishing theorem.'),
('irreducible-local-inputs', '''night:P4.52
night:P4.53
night:P4.54
night:P4R.19
night:P4.56
night:P4.57
night:P4R.20''',
 'The Part II route promises local transverse singularities, normalization geometry and irreducible Euler equality; this unit stands in its contracted-section/spectral-cover or conductor-junction sequence. Its admitted complete comparison retains the exact local ring, normalization and spectral-cover maps. Main C applies the completed irreducible classification to the same compact full fibre and its reduced support; the local support is obtained by restricting that same f to a disc. The front makes no additional assertion about these local sectors.'),
('doubled-supports', '''ii:three-doubled-nodal-fibres''',
 'The abstract and revised Part II route name exactly the compact construction with three doubled nodal supports and elliptic ruled normalizations. The entire P205 construction was read: the same source-line/root quotients and annular gluings give 2S, and the exact integral restriction/transgression maps prove the asserted compact topology. The route now points to this actual subsection.'),
('marked-resonance', '''cdp:st:C4g
def:II:marked-Picard-parameter''',
 'Part III explicitly promises marked-period/Picard resonance and tangent cohomology. Main E and all five E outline steps use the identical normalized physical-line parameter and root characters in C5b/C5c; complete proofs and their exact invariant/coarse maps were compared. The hexagonal normalization calculation and parameter definition stand in the named marked-family section. The finite-support premise has been corrected in E4.'),
('identity-monodromy', '''cdp:st:D.2.1
cdp:st:D.2.5
cdp:st:D.2.6''',
 'The abstract and main C name the equality forced by identity monodromy; outline C5 uses D2.3/D2.5 and the logarithmic period obstruction. The separate admitted main-C comparison covers the complete required owners and their same full-fibre/finite-root/normalization maps. These supporting period and direct-image units stand in Part III; the final equality conclusion stands in Part VI. Their different source locations are explicit in the current route.'),
('fibration-deformations', '''sec:II:14
sec:II:explicit-deformations''',
 'The Part III route and abstract promise fibration persistence and the stated deformation spaces. Main F and outline F1-F4 were compared with complete E5/E6/E13/E14/E15. The same cup map, every Artin lift and nilpotent graph locus, fixed affine attachments, period derivatives and full Kuranishi ideals give precisely those conclusions in their stated families.'),
('theta-ranks', '''sec:II:period-rank''',
 'Part III names period ranks and tangent cohomology. Main E and outline E5 were compared with complete E8/E18. The explicit identity-induced degree-six isogeny preserves the period tensors, and the exact determinant retains its Weierstrass term. The original zero-branch rank statement and the separately parameterized half-period example retain their displayed maps and domains.'),
('specialization-chain', '''sec:II:push-stability
sec:II:critical-fibre-extension
sec:II:normal-crossing-cusps
sec:II:analytic-cusp-identification
sec:II:connected-deformation-chains
sec:II:two-independent-periods''',
 'These units stand in the Part III route for deformation spaces and marked periods. Their admitted complete-unit comparison records the canonical-pencil, finite-root, torus-action and cusp-extension maps. Main F and outline F5-F6 were compared with complete E2.23/E2.24: finite curve projection and normalization preserve the fixed coprime ordered pair through connected bases/chains, and the explicit Kuranishi retraction gives the stated smooth-topology quotient. The protected two-period statements retain their original marked-parameter isomorphisms.'),
('analytic-conductor-support', '''sec:II:uniform-nontorsion
sec:II:analytic-duality
sec:II:conormal-relative-maps
sec:II:analytic-picard-boundary
wbII:subsec:local-cusp-picard-obstruction
wbII:subsec:analytic-all-picard
sec:II:analytic-vanishing''',
 'The Part III route explicitly names conductor nonvanishing, and these units provide its full analytic sequence. The admitted complete analytic comparison retains the marked Picard coordinate and inverse, Cartier duality/base-change maps, conormal connecting morphism, cusp restriction factors and global boundary cocycles. Main A retains its exact integral-CDP criterion; the standard-family all-twist conductor applications retain their full stated normalized cusp and Picard hypotheses. The front route identifies the existing sequence and supplies no additional general vanishing assertion.'),
('LR-covering', '''sec:II:lr-parameter-covering''',
 'The abstract, main G and all four G outline steps describe this actual final Part III section. The complete LR proof and receiving outline were read. The marked lattice and Albanese inverse maps give the one-turn obstruction; U=C^-1, the endpoint norm t^-1 B_u^-1, cap theta/t and fixed cusp period relabelling give the free quotient w=r^2, u=w^2. Every fixed-character and physical-line datum is retained.'),
('comb-kernel', '''sec:II:combs
subsec:II:twelve-tooth-smoothings''',
 'The abstract, main F/F7 and Part III/VII routes retain exactly the nonempty open twelve-tooth fixed-marking family. Complete E2.2/E2.5/P320/P321 readings compare the same tangent cup kernel, exact node/conic maps, collapse and semicontinuity, degree -26 and explicit splitting to O(-8)+O(-9)^2. The Hodge substitution gives 49,48. The current route locates the established degree/duality proofs here and the remaining general/special problem in Part VII.'),
('component-boundaries', '''subsec:II:contracted-ruled-boundaries
subsec:II:normal-irreducible-supports
subsec:II:local-numerical-conductor-inputs
subsec:II:class-vii-canonical-boundaries
subsec:II:anticanonical-hopf-boundaries''',
 'The Part IV route names component geometry and horizontal conductors, ending with INT3. These admitted boundary and normal-support units supply the stated contraction, conductor and canonical-model maps to the final horizontal/interface owners. Main C, G1 and all six C steps were compared with the current receiving owners, keeping the compact full-fibre/reduction/normalization inclusion and exact conductor ideals. The local proper-family results retain their own domains through the explicit disc-restriction maps.'),
('component-lattices', '''subsec:II:normal-product-collars
subsec:II:marked-cycle-lattices
subsec:II:moving-marked-cycles''',
 'The revised Part IV route explicitly names integral component lattices and horizontal conductors. This unit retains the admitted normal-product, marked-lattice and overlap maps used by the subsequent Part V constructions. The complete placement comparison verifies those supplying/receiving positions. Main C uses the compact normalization/conductor criterion; the front does not replace these marked construction data by that equality statement.'),
('original-sec07', '''sec:II:07''',
 'This stable identity covers the complete distributed original sec07 remainder, not just the surviving section anchor. The admitted horizontal comparison maps every original label to P360/P380 and the exact P361/P362, UN7/UN12/MH4 and INT1-3 owners. Its separate main-C comparison then verifies all six outline steps, G1 and abstract equality claims on the exact full-fibre/reduction/normalization maps. The Part II and IV reader routes describe the actual irreducible and component/interface locations.'),
('original-occurrence', '''sec:II:09
sec:II:10''',
 'This stable original-section identity is assessed across the complete admitted distributed owner correspondence, rather than the current old-label position. The Part V route promises the stated compact component occurrences and marked Hopf/ruled/elliptic classifications with their full multiplicities. The complete placement assessment locates every supplying torsor, period, pruning/restoration, root and finite-action owner before its receiver. Stages20/21 retain the merged UN60/UN62, arbitrary elliptic-root UN61, P376 and weighted UN63 conclusions. Main C remains the exact separate compact Betti-zero sign/equality application.'),
('signed-component-occurrence', '''subsec:II:signed-root-fibrations
subsec:II:paired-root-occurrence
subsec:II:secondary-kodaira-occurrence
subsec:II:projective-root-covers
subsec:II:enriques-family-occurrence
subsec:II:kummer-elliptic-occurrence''',
 'The Part V route names compact fibrations with the stated component types. This unit retains the admitted signed-root, equivariant period and finite-quotient maps for precisely its named component construction. The placement comparison locates the common supplying owners before these applications. The route makes this construction claim with its stated data; it does not identify these component occurrences with the very-general smooth-fibre list of main B.'),
('Hopf-ruled-occurrence', '''subsec:II:diagonal-hopf-occurrence
subsec:II:nonlinear-hopf-occurrence
subsec:II:secondary-hopf-occurrence
subsec:II:ruled-component-occurrence
subsec:II:enriques-elliptic-occurrence''',
 'The Part V route names the stated compact Hopf, ruled and elliptic component occurrences. The admitted complete comparisons retain the exact torsor/source-line quotient, affine gluing, marked lattice and boundary normal-character maps for each construction. Their common owners occur earlier, as the complete placement comparison records. The component-to-full-fibre inclusions are the actual ones used later; no new smooth-general-fibre classification is asserted here.'),
('marked-cycles', '''subsec:II:marked-cycle-criterion
subsec:II:explicit-marked-cycles
subsec:II:logarithmic-period-families
subsec:II:cycle-elliptic-suspensions''',
 'The Part V route explicitly promises marked support classifications with full multiplicities. This unit carries the admitted common period, normal-character, marked-cycle and suspension maps. P331 and the normal-product/lattice owners precede the receivers, and the complete placement comparison retains the arbitrary-parameter and compact rank-four clauses. The front description therefore has exactly the stated constructed/classified support scope.'),
('elliptic-stars', '''subsec:II:elliptic-star-data
subsec:II:star-boundary-periods
subsec:II:hopf-leaf-pairs
subsec:II:compact-elliptic-star-insertion
subsec:II:reduced-hopf-star-criterion''',
 'The Part V route names compact marked elliptic supports. The final shared P370-P375/P353 sequence supplies exact one-/two-mark torsors, pruning, core periods, weighted insertion, finite stabilizers and compact restoration before UN49 and the later tree criteria. The admitted complete comparisons and placement note preserve every multiplicity and boundary/quotient map. The subsection title correction to elliptic pruning and compact restoration reflects that full receiving scope.'),
('weighted-cycles', '''subsec:II:weighted-cycle-data
subsec:II:weighted-cycle-roots
subsec:II:weighted-cycle-affine-data
subsec:II:finite-equivariant-periods
subsec:II:weighted-cycle-criterion
subsec:II:weighted-cycle-suspensions
subsec:II:weighted-cycle-examples''',
 'The Part V route names marked supports with full multiplicities. The admitted complete weighted-cycle comparison retains the exact normal data, root cover/inertia, finite affine action, period-family power substitution, quotient criterion and examples. P355-P359 and the earlier P331 period owner occupy the actual supplying positions. The front makes the corresponding marked construction/classification claim on these unchanged data.'),
('elliptic-trees', '''subsec:II:tree-pruning-remainder''',
 'The Part V route names the full elliptic support constructions and classifications. Stage20/21 completely compares the same one-/two-mark torsor maps, canonical height recursion, core period charts, compact insertion, finite actions and eigensheaf quotients for merged UN60/UN62, UN61, P376/P377 and UN63. The conductor reviewer reconfirmed this exact reader-route scope. Main C uses its separately proved compact normalization/conductor equality maps.'),
('canonical-reduction', '''subsec:II:section-fibre-contractions
subsec:II:anticanonical-bisections
subsec:II:canonical-flat-reduction
subsec:II:canonical-bimeromorphic-maps
subsec:II:modification-records
subsec:II:cyclic-root-normalization
subsec:II:weighted-toric-descent''',
 'Part VI explicitly promises component contractions and canonical-order reduction. This unit retains the admitted exact boundary/canonical-line transport, bimeromorphic maps, cyclic roots, full-multiplicity comparison and overlap inverses. The current placement note identifies its earlier supplying owners. Main C/G1 uses the same compact full-fibre and conductor maps at the end of the part; the route does not enlarge any bounded contraction or root-construction hypothesis.'),
('torsion-normal-cores', '''subsec:II:elliptic-alignment
subsec:II:torsion-normal-rational-obstruction
subsec:II:section-preserving-rulings
subsec:II:vertical-field-divisors
subsec:II:torsion-interface-models''',
 'Part VI develops the canonical reduction from boundary intersection, normal lines and cyclic roots. This admitted unit supplies its precise ruling, elliptic alignment, vertical-field or torsion-normal model maps to the later contractions. The current placement comparison checks those earlier owner locations, while main C/G1 retains the exact compact normalization/conductor equality scope established separately.'),
('toric-maximum', '''subsec:II:toric-central-log-spaces
subsec:II:compact-toric-occurrence
subsec:II:rational-boundaries-maxima''',
 'Part VI promises canonical-order reduction and finite rooted generation. The admitted exact toric log-space, compact occurrence and maximum-boundary maps in this unit occur before their canonical/finite-reduction receivers, as the complete placement comparison verifies. The rational-boundary P365 and toric UN71/UN73 inputs are retained. The final G1 conclusion is reached through its separately compared irreducible/interface proof.'),
('Hopf-exceptional-reduction', '''subsec:II:maximal-hopf-leaves
subsec:II:compact-negative-curve
subsec:II:maximal-hopf-reduction
subsec:II:negative-interface-reduction
subsec:II:vertical-elliptic-models''',
 'Part VI names component contractions and canonical-order reduction. The admitted complete comparisons retain P366/P367, the maximum-component and Hopf-boundary maps, the compact negative-curve example and the full UN82 vertical model. The reduction reviewer compared these current scopes against the Part VI introduction/route and G1/main C and found the same maps and hypotheses. No bounded finite-generation branch is promoted to all degenerations.'),
('finite-roots', '''subsec:II:rooted-generation
subsec:II:canonical-flat-root-descent
subsec:II:no-triple-contractions
subsec:II:reduced-finite-reduction''',
 'The Part VI route explicitly names finite rooted generation. The admitted complete comparisons retain the exact fixed tuple, component-prime correspondence, roots/full multiplicities and endpoint/overlap maps. UN85 keeps its explicit C.RK.3 resolution-and-root branch; UN86 follows every reconstruction owner. The reduction reviewer has compared this scope with the current front route and final G1. The route asserts the stated generation results and then the separately proved arbitrary-fibre Euler conclusion.'),
('original-sec11', '''sec:II:11''',
 'This stable original-section identity covers all 252 original labels through their admitted exact current-owner correspondence. The seven complete reduction comparisons exhaust its local remainder, including UN82, and preserve every contraction/canonical/finite-generation conclusion. Part VI names those exact topics and ends with G1; the reduction reviewer reconfirmed the current route and main-C/G1 maps. The final arbitrary-fibre Euler theorem uses its separately compared irreducible/interface proof, without enlarging a bounded generation branch.'),
]

heads=[]
for m in re.finditer(r'\\(part|section|subsection)\*?\{',s):
    i=m.end();j=i;depth=1
    while depth:
        if s[j]=='{' and s[j-1]!='\\':depth+=1
        if s[j]=='}' and s[j-1]!='\\':depth-=1
        j+=1
    heads.append((m.start(),m.group(1),s[i:j-1]))

def source_place(unit,title):
    marker='\\label{'+unit+'}'
    if marker in s:
        assert s.count(marker)==1,unit
        pos=s.index(marker)
    else:
        matches=[h for h in heads if h[1]=='subsection' and h[2]==title]
        assert len(matches)==1,(unit,title)
        pos=matches[0][0]
    prev=[h for h in heads if h[0]<=pos]
    part=next((h[2] for h in reversed(prev) if h[1]=='part'),'Front matter')
    sec=next((h for h in reversed(prev) if h[1]=='section'),None)
    sub=next((h for h in reversed(prev) if h[1]=='subsection' and (sec is None or h[0]>sec[0])),None)
    return ' / '.join([part]+([sec[2]] if sec else [])+([sub[2]] if sub else []))

lookup={(r['paper'],r['unit_id'],r['row_kind'],r['defect_type']):r for r in units}
proposals=[];seen=set()
for group,keys,detail in groups:
    for unit in keys.splitlines():
        assert unit and unit not in seen,(group,unit)
        seen.add(unit)
        key=('II',unit,'defect','D24');old=lookup[key]
        complete=lookup[('II',unit,'defect','D12')]
        assert old['status']=='open',(key,old['status'])
        assert complete['status']=='done',(key,'complete-unit evidence not admitted')
        place=source_place(unit,old['unit_title'])
        evidence='agents/continuation4_horizontal/S6_SERIES_PUBLISH_D23_D24_closure_comparison.md; admitted D12 row (II,'+unit+',defect,D12): '+complete['evidence']
        proposals.append(dict(paper='II',unit_id=unit,unit_title=old['unit_title'],row_kind='defect',defect_type='D24',prior_status=old['status'],proposed_status='done after parent admission of this exact D24 comparison',date_utc=stamp,evidence=evidence,detail='Current source placement: '+place+'. '+detail+' No fresh proof-reading, independent-check, derived-refresh or rendered-page credit is proposed.'))

remaining={r['unit_id'] for r in units if r['paper']=='II' and r['row_kind']=='defect' and r['defect_type']=='D24' and r['status']=='open'}
assert seen==remaining-{'methodology'},(sorted(seen-remaining),sorted(remaining-seen))
assert len(proposals)==107,len(proposals)
fields=['paper','unit_id','unit_title','row_kind','defect_type','prior_status','proposed_status','date_utc','evidence','detail']
with (OUT/'S6_SERIES_PUBLISH_D24_closure_unit_proposals.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(proposals)
print(len(proposals),'explicit existing D24 closure proposals; methodology held; no D23 closure or shared write.')
