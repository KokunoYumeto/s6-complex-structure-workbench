from pathlib import Path
import csv
import datetime
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation3_foundations'
p4 = (OUT / 'S6_SERIES_PUBLISH_II_construction_P4_input.tex').read_text()
d27 = (OUT / 'S6_SERIES_PUBLISH_II_construction_D27_input.tex').read_text()
received = (OUT / 'S6_SERIES_PUBLISH_II_single_torus_construction.tex').read_text()
guards = json.loads((OUT / 'S6_SERIES_PUBLISH_torus_consolidation_guards.json').read_text())

def write_tsv(name, header, rows):
    with (OUT / name).open('w', newline='') as stream:
        writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
        writer.writerow(header)
        writer.writerows(rows)

def source_owner(label):
    pos = p4.index('\\label{' + label + '}')
    start = p4.rfind(r'\begin{proposition}', 0, pos)
    end = p4.index(r'\end{proof}', pos) + len(r'\end{proof}')
    return p4[start:end]

def part(stem):
    return (OUT / f'S6_SERIES_PUBLISH_II_single_torus_{stem}.tex').read_text()

def d_steps(first, after=None):
    steps = re.split(r'(?=\\item\b)', d27[d27.index(r'\begin{proof}'):])
    return ''.join(steps[first:after]).split(r'\end{enumerate}')[0]

rows = []
def add(kind, owner, place, old, new, reason, pending=False):
    rows.append([f'II-C3-TORUS-{len(rows)+1:03}', kind, owner, place,
                 'cp35/current receiving source; final page concordance pending',
                 'Single earlier torus construction unit', 'integrated build pending',
                 old, new, reason,
                 ('Root front-matter concordance remains.' if pending else
                  'Complete originals and receiving proofs read; exact gluing and integral basis maps supplied. Root admission pending.')])

add('D12','def:II:identity-example-lattice','Square elliptic curve and lattice',
    d_steps(1,2),part('P241'),
    'P241 owns the explicit square lattice and the exponential group isomorphism once. The first period 1 maps to multiplier1 and the second i to q; base meridian orientation at infinity is retained.')
add('D12','night:P4.1','Repeated local holomorphic construction',
    d_steps(2,4),part('P41'),
    'The identities on the blown-up base, exceptional divisor and O(R), commuting with scalar q, descend to the precise local biholomorphism. The canonical sections agree, hence so do the punctured product markings. P4.1 retains its complete coordinate proof, including tautological evaluation and the same two central surfaces.')
add('D12','night:P4.3','Repeated local homology and meridian proof',
    d_steps(4,6),part('P43'),
    'The exact local construction identification carries old (w,u) to (a,c). The single retained cellular proof proves the same primitive H1/H2 quotients, all meridian products, all local free ranks and the central retraction. The former Serre-sequence route is removed only as a parallel proof of these same maps.')
add('D12','cdp:st:D.2.7','Repeated compact gluing',
    source_owner('night:P4.2'),part('global'),
    'Both constructions use exactly Psi1(z,w)=(w,z), Psi2(z,w)=(iz,iz+w), Psi3(z,w)=(z,iz+w), with identical ordered discs0,1,infinity and clutch log(t)/(2pi i) in the first A factor. Identity maps on common exterior and local charts commute with every transition and glue to a holomorphic isomorphism over P1. P4.2 labels/tag are aliases at the global owner.')
add('D12','cdp:st:D.2.7','Repeated global homology result',
    source_owner('night:P4.4'),part('global'),
    'P4.4 is consolidated into the identical global Y. Its explicit S_i, inverse/exterior quotient definitions, signed F0/F1/F2 matrices, primitive relation matrices and fundamental-group conclusion remain once. Both old P4.4 labels and tag02XD are aliases at D.2.7.')
add('D12','cdp:st:D.2.7','Repeated global invariant result',
    source_owner('night:P4.5'),part('global'),
    'All integral homology ranks, torsion-freeness, c3=0,b3=2,a=1 and exact f^* function-field identification are retained at the single global owner. The E1 application from the root edit is preserved with every hypothesis checked on this same f. P4.5 labels/tag are aliases.')
add('D12','cdp:st:D.2.7','Second Mayer--Vietoris calculation',
    d_steps(8,11),part('global') + '\n' + part('basis_remark'),
    'The common matrices represent the same signed boundary morphisms. The Q_v coordinate realization is retained in one exact conversion remark; F1=diag(I6,M_1i)F1hat and F2=diag(I14,M_2i)F2hat. The old determinant+1 and receiving determinant-1 are related by the displayed target isomorphism of determinant-1, and Smith factors are unchanged.')
add('D12','cdp:st:D.2.8','Repeated central-fibre retraction',
    guards[3]['old'], guards[3]['new'],
    'Retain the earlier asserted base retraction and its principal-bundle lift at one local homology owner. The complete coherent-cohomology consumer is read; it now cites that exact input and retains the same annihilator, coefficient map, frame argument, full-fibre surjectivity and torsion locus.')
add('D14','night:P4.1','Unused forward dependency in statement record',
    r'\StatementRecord{night:P4.1}{proved}{02WG}{\SeriesRef{night:P4.3}}',
    r'\StatementRecord{night:P4.1}{proved}{02WG}{\SeriesRef{def:II:identity-example-lattice}}',
    'The complete local-geometry proof is self-contained after the square-lattice definition and its cited surface classification; it never uses P4.3. Remove the spurious forward edge, then place P4.3 after local construction.')
add('D14','cdp:st:D.2.7','Single earlier dependency order',
    'Early D.2.7 followed by a later repeated P241/P4.1-P4.5 subsection.',
    'P241, P4.1, P4.3, one D.2.7 global owner with P4.2/P4.4/P4.5 aliases, then P214.',
    'All local construction and homology premises precede the global result, which precedes C.3.11. P214 explains coordinates after the proved result and is not a construction premise. Root can delete the now-empty later construction subsection by the exact supplied guard.')
add('D13','rem:II:torus-quotient-coordinates','Coordinate-conversion owner',
    'Two numerical determinant signs in separate construction proofs with different implicit quotient targets.',
    part('basis_remark'),
    'The exact basis conversion, its determinants and its effect on both full signed matrices are one numbered mathematical remark, tagP214. No identity or difference of constructions is asserted from numerical invariants alone.')
add('D20','rem:II:extended-torus-groups','Local killed-cycle name',
    guards[2]['old'],guards[2]['new'],
    'The local exponential marking gives old w=a, the positively oriented angular cycle1 in E. The quotient and attempted left inverse are identical. Point the filling to the actual earlier local owner P4.1; all hypotheses and obstruction maps remain.')
add('D20','cdp:st:D.2.8','Global annihilator names',
    r'\lambda(w_i)=0; \operatorname{ann}(w_i)',
    r'\lambda(a_i)=0; \operatorname{ann}(a_i)',
    'Old w_i is exactly a_i=Psi_i(1,0), the first column of S_i. The vectors are e3,e2+e4,e1+e4, so the three annihilator equations and primitive solution(1,1,0,-1) are unchanged.')
add('D20','cdp:st:D.2.7','Boundary notation and exterior-square coordinates',
    'Old local cycles(w_i,u_i), clutch vectors c_i, base meridians mu_i, and surface classes[C_i].',
    'Receiving (a_i,c_i), clutch g_i, meridians s_i with coordinate columns v_i, and eta_i=a_i wedge c_i.',
    'The identifications are w_i=a_i,u_i=c_i,c_i(old clutch)=g_i,mu_j=s_j and[C_i]=eta_i. Kunneth sends x wedge mu_i to x tensor v_i, with fibre-first orientation; the clutch term remains x wedge g_i.')
add('D22','night:P4.3','Retraction needed by the coherent consumer',
    'Old D.2.7 asserts V retracts onto B0 union R; D.2.8 lifts this retraction through the principal torus bundle.',
    'The inclusion Bprime union R into V induces an isomorphism on pi1 and on the homology of simply connected covers, where the exceptional spheres are the same generators. A compatible triangulation makes it a cofibration; a strong deformation retraction and its relative bundle lift follow.',
    'Preserve the actual inherited retraction scope needed by D.2.8, with its explicit inclusion and sphere maps, rather than replacing that input by only an abstract B wedge S2 equivalence.')
add('D22','night:P4.3','Orientation of the second elliptic cycle',
    'The logarithm of the norm modulo log q gives S1_c.',
    'Orient S1_c by the lattice period i, whose norm-logarithm increment is log q.',
    'The exponential map sends i to q=e^(-2pi). This fixes the radial-circle orientation relative to the complex lattice and the product cell differential partial(rc)=a wedge c.')
add('D25','cdp:st:D.2.7','Fundamental-group relation notation',
    r'\pi_1(W)=\Lambda\times F(s_1,s_2); a_1=a_2=a_3=0, s_1+e_1=0, s_2=0, s_1+s_2=0.',
    r't_xt_y=t_{x+y}, [t_x,s_j]=1; t_{a_i}=1, t_{e_1}s_1=1, s_2=1, (s_1s_2)^{-1}=1.',
    'Clarify the inherited additive shorthand inside an explicitly nonabelian product. Positive based meridians satisfy s1*s2*s3=1 and the exact boundary maps give the displayed multiplicative relations. This proves the same pi1=1 conclusion; no original theorem is called refuted.')
add('D09','cdp:st:D.2.7','Matrix presentation and program citation',
    'Separate D.2.7 and P4.4 matrix recipes, in addition to the root-deduplicated P4 arrays.',
    'One S_i display, one inverse/exterior quotient definition, one signed block recipe for F1,F2,F0, and one pair of relation matrices; programs cited through the existing end table.',
    'Preserve the root removal of eighteen repeated arrays. The exact computational inputs, integer elimination, determinant and Smith results remain in the body; code paths stay in the pinned program table.')
add('D16','cdp:st:D.2.7','Common global title',
    'A compact torus fibration with trivial monodromy; separate fundamental-group and invariant propositions.',
    'A simply connected compact torus fibration.',
    'The title describes the strongest already established property of this same explicitly identified Y. Original tags and labels remain at the one owner.')
add('D10','cdp:st:D.2.7','Alias targets and machine apparatus',
    'Four separate global statement records for the identical construction/result.',
    'One visible global statement/tag01GE and retained hypertargets01GE,02WR,02XD,02XO with every old label; one hidden dependency record.',
    'The complete unit preserves all24 old labels and19 old hypertargets once, adds only P214, and retains the D10 closure. The alias map retains stronger original scopes at their shared current owner.')
add('D24','cdp:st:D.2.7','Front-matter further-results listing',
    'Separate list entries for P4.1,P4.2,P4.3,P4.4,P4.5.',
    'One local geometry entry P4.1; one local homology entry P4.3; one compact simply connected torus-fibration entry D.2.7.',
    'The three global aliases now have one printed owner. Root is rewriting front matter and must remove the resulting duplicate list entries while keeping the local results.', True)

eq_specs = {
    21: ('cdp:st:D.2.7', 'The exact original H1,H2,a,c3,b3 display is preserved; stronger pi1, full integral homology and field-map conclusions follow as additional statement clauses.'),
    22: ('def:II:identity-example-lattice', 'Same exponential map; only imaginary-unit typography changed. The images of the two lattice generators are explicit.'),
    23: ('night:P4.1', 'Same L-times/q^Z to V to disc morphism; identity on the divisor line bundle and scalar action.'),
    24: ('night:P4.1', 'Same canonical-section product trivialization; C times B identifies with A by the explicitly given identity in copy coordinates.'),
    25: ('night:P4.3', 'Same regular-fibre quotient maps with old w=a,u=c; surjection arrows and free targets are explicit.'),
    26: ('night:P4.3', 'Same positive meridian and all fibre-first mixed-cycle images, with coefficients Z declared in P241.'),
    27: ('cdp:st:D.2.7', 'Old phi_i(z)=Psi_i(z,0); the complementary factor completes Psi_i. Old w_i,u_i are exactly the first two columns a_i,c_i of the displayed S_i. All old table entries are preserved through these explicit maps.'),
    28: ('cdp:st:D.2.7', 'Same principal A-bundle clutch log(t)/(2pi i) in its first factor; positive loop adds e1.'),
    29: ('cdp:st:D.2.7', 'Identity on Lambda and ordered base coordinates sends old(mu_i+c_i) to(v_i+g_i); v1=(1,0),v2=(0,1),v3=(-1,-1),g=(e1,0,0).'),
    30: ('cdp:st:D.2.7', 'Same induced map on exterior products; Kunneth x wedge mu_i is x tensor v_i, and old c_i=g_i.'),
    31: ('cdp:st:D.2.7', 'Same integral quotient, with w_i=a_i and the identical determinant-minus-one four-column relation matrix.'),
    32: ('cdp:st:D.2.7', 'Same exterior-square quotient, with[C_i]=eta_i=a_i wedge c_i; the identical full relation matrix proves the added displayed equality to zero.'),
}
eq_rows = []
for n, (owner, comparison) in eq_specs.items():
    label = f'cdp:eq:D.{n}'
    eq_rows.append([f'D.{n}',label,owner,'equation','equation',comparison])
    add('D19',owner,f'Equation D.{n} owner transport',
        f'{label} in the early D.2.7 proof/result',
        f'{label} retained once at {owner}; automatic section numbering unchanged',comparison)

write_tsv('S6_SERIES_PUBLISH_torus_consolidation_defects.tsv',
          ['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status'], rows)
write_tsv('S6_SERIES_PUBLISH_torus_consolidation_equation_map.tsv',
          ['old_tag','target_label','owner','old_environment','new_environment','formula_comparison'], eq_rows)

aliases = [
    ['def:II:identity-example-lattice','P241','def:II:identity-example-lattice','P241','Definition moved earlier; same square elliptic curve, exponential map, ordered lattice and meridian orientations.'],
    ['night:P4.1;stmt:P4.1','02WG','night:P4.1','02WG','Single local holomorphic construction owner; all geometry and full coordinate proof retained.'],
    ['night:P4.3;stmt:P4.3','02X2','night:P4.3','02X2','Single local integral homology owner; exact quotient, meridian and retraction maps retained.'],
    ['cdp:st:D.2.7','01GE','cdp:st:D.2.7','01GE','Existing global owner enriched by all conclusions of the same construction through its explicit chartwise biholomorphism.'],
    ['night:P4.2;stmt:P4.2','02WR','cdp:st:D.2.7','01GE','Global gluing maps, properness, connectedness, exactly three stated singular fibres and identity monodromy retained.'],
    ['night:P4.4;stmt:P4.4','02XD','cdp:st:D.2.7','01GE','Integral H1=H2=0 and pi1=1, including the exact boundary presentation and matrices, retained.'],
    ['night:P4.5;stmt:P4.5','02XO','cdp:st:D.2.7','01GE','All integral homology groups free of ranks(1,0,0,2,0,0,1), a=1,c3=0,b3=2 and exact field pullback retained.'],
]
write_tsv('S6_SERIES_PUBLISH_torus_consolidation_aliases.tsv',
          ['old_labels','old_tag','receiving_owner','printed_owner_tag','preserved_scope'],aliases)

scope_rows = [
    ['Local bases','Both V=Bl_(0,0)(E times disc), R exceptional, L=O(R),q=e^(-2pi)',
     'Identity of E times disc lifts to identity on V and R; induced identity of O(R) fixes its canonical section and commutes with q.',
     'P4.1; D.23-D.24','The quotient identity U_D to U_P is holomorphic, invertible, over the same disc, and agrees with the punctured product marking.'],
    ['Complex and integral product markings','Both lists use the same ordered discs0,1,infinity and square E lattice',
     'Psi1(z,w)=(w,z), Psi2(z,w)=(iz,iz+w), Psi3(z,w)=(z,iz+w); inverses(y,x),(-ix,y-x),(x,y-ix); S_i are their real lattice matrices.',
     'D.27 and S_i display','Old(w_i,u_i)=(a_i,c_i) exactly, not merely up to a rational or orientation-forgetting isomorphism.'],
    ['Global threefold','Both principal A-bundles have clutch a_out=a_in+(log(t)/(2pi i),0)',
     'On a common refinement use identity on A times exterior base and the quotient identity on each U_i. The identical Psi_i and clutch maps commute on each overlap, so the chart maps and their inverses glue.',
     'D.2.7/P4.2/P4.4/P4.5 common owner','The resulting Phi:Y_D to Y_P is a biholomorphism with f_P Phi=f_D and identity marked regular-fibre H1 map. Hence every stronger global conclusion and f^* commute with transport.'],
    ['Integral quotient coordinates','D.2.7 Q_v coordinates and P4.4 coordinates from S_i^-1 and wedge2 S_i^-1',
     'R1_i=M1_i Q_ai; R2_i=M2_i Q_etai, with all six matrices and their determinants explicit in P214. Full signed matrix identities use diag(I6,M1_i) and diag(I14,M2_i).',
     'P214','detF1hat=+1 and detF1=-1 are exactly related by target determinant-1; Smith invariants and all inclusion maps are preserved.'],
    ['Coherent consumer D.2.8','Same Y, local fillings, marked periods, central retraction and integral annihilators',
     'w_i=a_i; retraction is the same local inclusion, now proved at P4.3. The three annihilator equations stay lambda3=0,lambda2+lambda4=0,lambda1+lambda4=0.',
     'D.2.8 exact bounded guard','All direct-image bundles, all four coherent dimensions, integral comparison, full-fibre restriction and dense torsion locus are unchanged.'],
    ['Albanese comparison P213','Same local marked U and group extension A times disc',
     'old w=a; the exact map Lambda to Lambda/Z a is followed by the hypothetical alpha_* and cannot give the identity on nonzero a.',
     'P213 exact bounded guard','Same obstruction and all extension hypotheses; only the local owner citation and the primitive-cycle name change.'],
    ['Further filling consumer C.2.UN.3','Same n=1 local construction, central surfaces, canonical section and compact Y0/Y gluing',
     'C.UC.2 is D.23 via identity on V,L; C.UC.3 is D.24 via its canonical section; C.UC.4 is P4.1 central description and local integral transgression.',
     'Documented for root/assigned owner; no wider edit made','Its full ten-step proof was read. The finite-base-change and n>=1 non-bimeromorphic-family results remain unchanged. Its repeated n=1 steps3-4 can use the earlier owner.'],
]
write_tsv('S6_SERIES_PUBLISH_torus_consolidation_conclusion_map.tsv',
          ['scope','exact_hypotheses','exact_morphism','receiving_owner_or_consumer','preserved_conclusion'],scope_rows)

units = ['def:II:identity-example-lattice','night:P4.1','night:P4.3','cdp:st:D.2.7','rem:II:torus-quotient-coordinates']
status_rows = []
for unit in units:
    for number in range(1,26):
        kind=f'D{number:02}'
        state='done'
        reason='Complete original and receiving text checked at this construction-unit scope; no additional instance found.'
        if kind == 'D10':
            reason='All24 inherited labels and19 inherited targets are retained once; existing D10 closure preserved, with one printed common-global tag and nonprinting aliases.'
        elif kind == 'D12':
            reason='One local construction proof, one local homology proof and one global construction/result proof, justified by the exact chartwise biholomorphism and integral coordinate transport. The distinct later C.2.UN.3 unit is documented for its assigned owner.'
        elif kind == 'D13':
            reason='P241 is the definition; P4.1/P4.3/D.2.7 own all construction results; P214 is the one numbered basis-conversion remark.'
        elif kind == 'D14':
            state, reason='open','The fully written earlier ordered block and exact removal guard are supplied; root must admit them before C.3.11 and remove the empty later subsection.'
        elif kind == 'D16':
            reason='Every receiving statement has a mathematical title; the global title states its already established simple connectivity.'
        elif kind == 'D17':
            reason='The retained local construction proof carries its existing exact BHPV locator. The removed construction proofs are compared through explicit identity/gluing maps, not removed on a new unverified literature attribution.'
        elif kind == 'D18':
            reason='Existing citation keys and exact locators preserved. No new publication/source claim added.'
        elif kind == 'D19':
            reason='All12 D.21-D.32 labels and targets occur once in equation environments, with automatic section numbering and exact coordinate-transport explanations.'
        elif kind == 'D20':
            reason='Primary matrices use (a_i,c_i),g_i,s_i,eta_i. Exact old-name maps and both consumer guards supplied; alternate quotient coordinates occur only in P214 with all six integral isomorphisms.'
        elif kind == 'D22':
            reason='Radial-circle orientation, primitive Chern transgression, actual retraction inclusion and the differing determinant signs have explicit reasons at their uses.'
        elif kind == 'D24':
            state, reason='open','Root front matter must represent the three global aliases as one result and retain the two local results; final numbering and PDF check remain root-owned.'
        elif kind == 'D25':
            reason='Every original and receiving proof read; exact global gluing, both inclusion matrices, central-retraction maps and nonabelian van Kampen presentation compared. No theorem refutation or independent new check claimed.'
        status_rows.append([unit,kind,state,reason])
    status_rows.append([unit,'restructuring','open','One finished earlier construction block with all aliases, exact equation maps and bounded consumer guards; parent admission remains.'])
write_tsv('S6_SERIES_PUBLISH_torus_consolidation_unit_progress.tsv',['unit','row','status','basis'],status_rows)

event_specs = [
    ('def:II:identity-example-lattice','definition','Complete original P241 and D.2.7 first step, and receiving definition read. Exact exponential group map and both lattice-generator images, ordered e-basis and meridian orientation retained.'),
    ('night:P4.1','local-geometry','Complete original P4.1 and D.2.7 local construction proof passages read; complete receiving P4.1 proof read. Identity on the blowup and O(R), fixing canonical section and commuting with q, proves the exact local equivalence. Root coordinate proof and all geometric conclusions retained.'),
    ('night:P4.3','local-homology','Complete original local cellular and Serre-route proofs and complete receiving P4.3 read. Actual regular-fibre and meridian maps coincide under w=a,u=c. The same central-base inclusion is checked on pi1 and universal-cover exceptional-sphere homology, made a cofibration by compatible triangulation, and lifted relatively through the principal elliptic bundle.'),
    ('cdp:st:D.2.7','D27-full','Complete original twelve-step D.2.7 and full receiving seven-step global proof read. Common chart identities and identical three complex markings/clutch descend to a biholomorphism over P1 preserving the marked regular fibre. All original statement and proof scopes used by direct consumers retained.'),
    ('night:P4.2','P42-full','Complete original P4.2 proof and full receiving global proof read. Every product map and its inverse, both local and global properness/Hausdorff arguments, connectedness, three critical values and marked identity monodromy have the same actual maps. Labels and tag are aliases of the common global owner.'),
    ('night:P4.4','P44-full','Complete original P4.4 proof and full receiving global proof read. All S_i matrices, quotient definitions, signed Mayer-Vietoris maps, relation matrices and primitive eliminations retained once. The fundamental-group argument uses the same boundary maps, now written multiplicatively with t_x and s1*s2*s3=1. Its pi1=1 conclusion is preserved at the common owner.'),
    ('night:P4.5','P45-full','Complete original P4.5 proof and receiving global proof read. All integral homology, Euler/top-Chern and b3 conclusions, torsion arguments, and exact E1 application with f^* field map are retained for the explicitly identical Y.'),
    ('rem:II:torus-quotient-coordinates','basis-transport','Complete receiving P214 read. All six integral coordinate maps were derived from the exposed S_i inverse/exterior-square matrices and Q_v definition. Exact Fraction-based arithmetic verifies R1_i=M1_i Q_ai, R2_i=M2_i Q_etai and both full signed block identities; target determinant-1 converts F1hat determinant+1 to F1 determinant-1. This is dependent editorial coordinate verification, not a rerun of either legacy program or a new independent computation check.'),
    ('cdp:st:D.2.8','coherent-consumer','Complete original and receiving D.2.8 statements and five-step proofs read. Only the exact w_i=a_i names and the central-retraction owner citation change. Annihilator equations, primitive integral solution, coefficient map, coherent frame and cup-product arguments, every full-fibre restriction and the dense torsion locus are unchanged.'),
    ('rem:II:extended-torus-groups','Albanese-consumer','Complete original and receiving P213 read. Direct local citation and exact w=a name preserve the same marked quotient and impossible left-inverse composite. All group-extension hypotheses and the nonconstant-period example remain.'),
    ('cdp:st:C.2.UN.3','further-filling-consumer','Complete statement and all ten proof steps read solely as a direct construction consumer. Its n=1 V,L,U, canonical marking and compact Y0/Y gluing coincide through the exact maps documented in the conclusion map. No edits or new check credit for its separate birational/base-change/infinite-family proof; repeated local steps3-4 are passed to root/assigned owner.'),
]
now=datetime.datetime.now(datetime.timezone.utc)
event_file='agents/continuation3_foundations/S6_SERIES_PUBLISH_torus_consolidation_CHECK_EVENTS.tsv'
events=[]
for owner,key,outcome in event_specs:
    event_id='publish:c3:torus-consolidation:'+key
    events.append([owner,now.date().isoformat(),
                   'GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 foundations',
                   'used and rechecked in this run',
                   outcome+' Exposed editorial/proof comparison only; no independent re-proof or final PDF credit. Existing required checks198/198 unchanged.',
                   event_id,'publication construction consolidation',event_file,'',
                   'used and rechecked in this run',event_id,'','',now.isoformat(),
                   'Earlier P241/P4.1/P4.3/common D.2.7/P214; exact P213 and D.2.8 consumer transports'])
write_tsv('S6_SERIES_PUBLISH_torus_consolidation_CHECK_EVENTS.tsv',
          ['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where'],events)
print(len(rows),'defect instances;',len(eq_rows),'equation maps;',len(aliases),'owner/alias maps;',len(scope_rows),'scope/morphism maps;',len(status_rows),'unit status rows;',len(events),'exposed reading events.')
