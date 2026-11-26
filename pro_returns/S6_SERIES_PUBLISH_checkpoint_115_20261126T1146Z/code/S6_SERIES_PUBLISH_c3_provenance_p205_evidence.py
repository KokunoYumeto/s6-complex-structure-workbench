#!/usr/bin/env python3
"""Record the completed, exposed P205 proof comparison; no shared writes."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation3_provenance/p205'
old=(ROOT.parents[1]/'tmp/c3_provenance_p205_old.tex').read_text()
new=(OUT/'S6_SERIES_PUBLISH_p205_proposed.tex').read_text()
main=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
assert main.count(old)==1

def statement(s):
    a=s.index(r'\begin{example}')
    b=s.index(r'\end{example}',a)+len(r'\end{example}')
    return s[a:b]
assert statement(old)==statement(new)
for pattern in (r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}'):
    for label in re.findall(pattern,old):
        assert re.findall(pattern,new).count(label)==re.findall(pattern,old).count(label)
old_displays=re.findall(r'\\\[(.*?)\\\]',old,re.S)
removed=[x for x in old_displays if x not in new]
assert len(removed)==2
assert '1&0&0&-1/2' in removed[0] and r'\det=-16' in removed[1]
for e in re.findall(r'\\begin\{equation\}(.*?)\\end\{equation\}',old,re.S):
    assert e in new
stack=[]
for op,env in re.findall(r'\\(begin|end)\{([^}]+)\}',new):
    if op=='begin':stack.append(env)
    else: assert stack.pop()==env
assert not stack
for body in re.findall(r'\\\[(.*?)\\\]',new,re.S):
    assert not re.search(r'\n[ \t]*\n',body)
labels=set(re.findall(r'\\label\{([^}]+)\}',main+new))
for keys in re.findall(r'\\(?:cref|Cref|ref|eqref|SeriesRef)\*?\{([^}]+)\}',new):
    assert all(k in labels for k in keys.split(',')),keys
assert not re.search(r'\b(actual|requested|candidate|certificate|diagnostic|survivor)\b',new)
assert r'\tag{' not in new and '\r' not in new
assert 'push:src:E.5.2' not in old+new and 'push:src:E.5.3' not in old+new

def read(name):
    with (OUT/name).open(newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
def write(name,rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t',lineterminator='\n')
        w.writeheader();w.writerows(rows)
defects=read('S6_SERIES_PUBLISH_p205_defects.tsv')
for row in defects:
    row['review_status']='Complete original and receiving unit/proof read, with each final bounded clarification reread. Exact construction and consumer comparison completed. Used and rechecked after proof exposure; no independent or final-PDF-page credit.'
write('S6_SERIES_PUBLISH_p205_defects.tsv',defects)

now=datetime.now(timezone.utc).isoformat()
who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 provenance'
events=[]
for suffix,kind,outcome in [
('proof','used and rechecked in this run',
 'Read the complete original P205 subsection and complete receiving proof, plus the full P233 and P294 receiving input proofs. The statement is byte-identical. Preserve every original construction display, integral marking, lattice intertwiner, Klein-four cover and inverse, canonical extension, twistor row map, fixed-disc positivity argument, local period normalization, chain gluing, free action, normalization/isogeny, affine translation and inverse, local restriction/transfer map, integral loop value, gluing cover, transgression and Betti conclusion. Add the exact finite deck matrix, projector sections in an initial holomorphic frame, exterior derivation convention, invariant chart norms and chain separation. The compact tube and conductor graph applications identify their exact source/target maps. Replace only the two rank-verification displays by their identical linear equations; all six exterior forms and determinant -16 remain. Primary Grauert statements and their printed arguments, with the full erratum, were reread at the exact loci. There is no new analytic construction or independent derivation event. The example has no outward mathematical consumer in II beyond its front-matter listing and program row.'),
('arithmetic','computation or formal certificate',
 'Executed the unchanged code/S6_SERIES_PUBLISH_II_P205_printed_data_check.py: all displayed integral monodromy products/conjugacies, nilpotents, lattice orientation, fixed spaces, exterior determinant -16, affine loop sums, twistor row maps and determinant passed. Executed code/S6_SERIES_PUBLISH_c3_provenance_p205_logarithms.py: the three limiting-frame logarithmic determinants are exactly 4(1+2 epsilon y), 16(1+2 epsilon y), 16(1+epsilon^2 y). These are exact finite algebra checks after proof exposure; no analytic realization, uniform-transversality, properness or independent proof claim is inferred from the programs.')]:
    events.append(dict(statement_id='ii:three-doubled-nodal-fibres',date=now[:10],who=who,type=kind,
        outcome=outcome,event_id=f'publish:c3:p205:{suffix}',phase='publication full-unit comparison',
        source_file='agents/continuation3_provenance/p205/S6_SERIES_PUBLISH_p205_CHECK_EVENTS.tsv',source_row='',
        source_event_type=kind,evidence_group=f'publish:c3:p205:{suffix}',publish_input_file='',publish_input_row='',
        date_utc=now,where='Complete Three doubled nodal supports subsection and exact input/application maps'))
write('S6_SERIES_PUBLISH_p205_CHECK_EVENTS.tsv',events)

pdfroot=ROOT.parents[1]/'tmp/c3_provenance_primary'
sources=[]
for key,file,url,locus,paraphrase,application in [
('Grauert1960D','Grauert1960.pdf','https://www.numdam.org/item/PMIHES_1960__5__5_0.pdf',
 '§7 setup and Satz3 statement/printed argument, pp.62–63; Satz5 and preceding printed argument, pp.63–64; Satz6 statement p.64 (its proof is explicitly omitted there)',
 'For a proper surjective holomorphic map, reduced base and a coherent sheaf flat over that base, fibre cohomology dimensions are upper semicontinuous. Constant dimensions give the indicated locally free direct image and restriction isomorphisms; on a connected base the alternating fibre-cohomology sum is constant.',
 'Take q:P1×Delta_epsilon→Delta_epsilon and the jointly holomorphic bundle E. Flatness follows from the parameter being a nonzerodivisor on its locally free stalks. E_0=O^4 gives h1=0, chi=4, h0=4; q_*E is rank4 and evaluation is an isomorphism near zero. The proper image of the evaluation degeneracy set is closed and misses zero.'),
('Grauert1963ErratumD','Grauert1963.pdf','https://www.numdam.org/item/PMIHES_1963__16__35_0.pdf',
 'Full corrigendum, pp.35–36',
 'The corrigendum changes the nested radius conditions in the main proof and the corresponding induction details. It also corrects the claim that the exceptional base-change locus in §7 Satz2 is always closed. The cited semicontinuity, constant-cohomology and Euler-characteristic statements remain the stated conclusions.',
 'P205 uses Sätze3,5,6 and the separate closed degeneracy set of its concrete evaluation map; it does not use the corrected Satz2 closed-locus claim.')]:
    raw=(pdfroot/file).read_bytes()
    sources.append(dict(source_key=key,url=url,version='Original journal facsimile, Numdam',locus_read=locus,
        sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw),own_paraphrase=paraphrase,
        exact_application=application,read_extent='Complete cited statements and printed context/arguments read; no unprinted proof claimed; online primary PDF and metadata reopened',date_utc=now))
write('S6_SERIES_PUBLISH_p205_sources.tsv',sources)

statuses=[]
for n in range(1,26):
    t=f'D{n:02d}';state='done in source unit'
    note='Complete original and receiving subsection read; changed instances have exact rows; no remaining local instance found.'
    if n in (10,16):
        state='inherited done, preserved';note='The existing statement tag, title, labels and hidden metadata renderer are preserved.'
    if n==12:note='P205 remains the one complete compact construction. P233 and P294 provide the precise previously owned tube and pushout maps.'
    if n==14:note='The entire example stays in its own subsection immediately after R13. All construction premises precede their uses. No new owner or tag is needed.'
    if n in (15,24):note='The complete example statement and front-matter claim scope are unchanged; no instance of this class occurs inside this unit. Root owns the final first-part consistency pass.'
    if n==23:
        state='source checked; integrated typesetting pending';note='Balanced environments, no blank display paragraphs, no manual tags. The chart norms use an aligned display. Root owns the current rendered-page pass.'
    if n==25:note='Every local algebraic, analytic and topological map was checked at its stated domain, including the full real deformation, free action, integral index-two restriction and primitive affine transgression.'
    statuses.append(dict(unit='subsec:II:three-doubled-nodal-supports',statement_id='ii:three-doubled-nodal-fibres',
        defect_type=t,status=state,note=note,scope='This example only; no whole-section or final-publication closure.'))
write('S6_SERIES_PUBLISH_p205_unit_status.tsv',statuses)

report=r'''# Three doubled nodal supports: complete P205 comparison

## Outcome

The complete example remains one owner, with the same permanent tag P205 and a byte-identical statement. It stays in the subsection immediately after R13. No new statement tag is allocated. One whole-unit guard contains 31 exact text changes. Both the complete original and receiving proofs were read; the final bounded clarifications were reread. This is exposed work.

Every original displayed construction map and numerical construction input survives unchanged. The only two original displays removed are the pair of row-reduction arrays and the six-by-six exterior-power verification array. Their complete linear equations and solution spaces replace them, and the exterior determinant −16 remains. This preservation was checked directly against every old display and every original equation, label and permanent target.

## Exact mathematical comparison

| Proof component | Original and receiving mathematical data | Receiving change / verification |
|---|---|---|
| Integral monodromy | The three A_i, determinant-one C_i, A_i C_i=C_i A_loc and all four local lattice generators | All matrices and maps are unchanged; the delivered original arithmetic program passed. |
| Real deformation | The B_i(epsilon), rank-one square-zero N_i, P, D_epsilon and lattice Lambda_epsilon | Explicitly extend N_i by zero on e0; name D_epsilon P as the intertwining lattice isomorphism. |
| Fourfold base cover | t=(z+z^-1)^2/4, the three deck maps, triangle, square-root inverse and vertices 0,−i,1 | Every map and orientation convention is unchanged. |
| Joint extension | The canonical cohomology frame and Grauert application to q:P1×Delta→Delta | The finite deck matrix is diag(1,B_i) exp(−N_i/2), whose square is one. The inverse transpose is the cohomology map. Projector generators are applied to an arbitrary holomorphic frame with the specified central real character basis. |
| Twistor plane | The two rows, three K_i maps and cubic z↦−1/z^3 | All displayed matrices are unchanged. The limiting frames are explicitly Pi_infinity, Pi_tw(i), Pi_tw(−1), in place of the undefined axis shorthand. |
| Transversality | D=D0+2 i Im(Z)(N^t omega wedge bar omega), normalized coefficients and fixed puncture discs | Specify the induced exterior derivation and distinguish the central-frame arithmetic from the moving-frame continuity argument by their evaluation map. Exactly recompute all three printed limiting determinants. The real transition matrices of determinant one are named; the negative lattice-basis determinant remains in the next step. |
| Local periods | p=2a−c; a,b,c,d columns; half-turn matrix R; all four parity identities; Im(tau)<0; r=s exp(pi i gamma) | Every column, parity relation, coordinate change and sign argument is unchanged. |
| Infinite chain | U_k coordinates, adjacent gluing, P/B/T actions, invariant u norm and kappa | Prove Hausdorff separation using x_j=r^(k−j)x_k and y_j=r^(j−k)y_k; define both chart norms, their product |r| and their relation to u. The proper-discontinuity bounds and compact fundamental annulus remain unchanged. |
| Finite quotient | g(z,u,r)=(z+1/4,r/u,−r), chart map, g²=h and g⁴=P | The full free-action proof and two-to-one root-fibre translation are unchanged. |
| Central support | The finite normalization map from (E×P1)/h, the sign line L, its nontrivial order two, two conductor sections and degree-two isogenies | All maps are unchanged. The inverse of the local étale quotient chart gives the node product. P294 gives the precise Euler formula with N, the two sections and their two images. |
| Affine descent | v=(−ell/2,−ell/2+1/8), Phi=x+v, its inverse and Phi_- g_aff=g_lin Phi | All affine maps and their multivalued lattice increments are unchanged. |
| Rational local restriction | Root tube E×I2, fundamental class [P]+[Q], eta, graph class d*, and dimensions (1,2,2,2,1) | Apply P233 to the same proper root family. Its inclusion is g-equivariant, which gives the cohomology equivariance. The graph collapse sends c to zero and the U0-to-U2 longitudinal d path to one circuit. The degree-four tube and degree-two fibre transfer maps remain. |
| Moving periods | Linear deformation of alpha,beta and tau, fixed r², parameter vector fields, marked tube/boundary diffeomorphisms | The full proper family, norm bounds, parity and marking checks remain. No equivariant choice of a central-fibre retraction is used. |
| Integral local restriction | H1(M)=Zt+Zb+Z/2, j_*c=0, 2j_*d=0, free j_*a=2t, and image 2Za*+Zb* | P233 identifies the local tube homology with S; P294 uses N→S with the two section edges. Each edge map is (p/2,b)↦(2t_i,b), yielding 2t1=2t2 and torsion generator t1−t2. |
| Affine loop and global gluing | Zero section −v, quarter z increment, value u/2; the exact B0/D_i cover and full annulus gluing | All formulae and inverse maps remain unchanged, including free tube class t and the original full exceptional fibres 2S_i. |
| Global obstruction | alpha=(1,1,1,2), C_i^t alpha, values (−1/2,−1/2,1/2), global integral sections 2Zalpha | The Mayer–Vietoris argument and primitive d2(2alpha)=−[P1] are unchanged. |
| Betti calculation | R^q f_*Q=j_* wedge^q V, local fixed dimension two, Euler value two and compact-support duality | The exact inverse-kernel identity applies the displayed transpose equations to the inverse-transpose parallel matrices. Direct linear equations give the same two common fixed lines and the zero exterior fixed space. All Leray terms and the final b1=b2=0, e=0, b3=2 remain. |

## Single ownership and uses

The only II occurrences outside the owner are its further-result listing and Programs row; no mathematical consumer proof is redirected. The same local tube and conductor-pushout objects are now explicitly passed to their earlier owners P233 and P294, whose complete receiving proofs were read. The matrices of the identity-monodromy construction at D.2.7/P4.4 are also compared at their statement and initial construction maps, and the complete P4.3 proof was read for this comparison: its quotient maps kill a and a wedge c, whereas P205 has the displayed index-two cohomology restriction and full affine loop calculation. P205's own marked construction and maps are retained; no identification of these two constructions is asserted.

## Source check

The primary Numdam PDFs for Grauert 1960 and its 1963 erratum were reopened online. The full printed §7 setup, Satz3 statement and argument on pp.62–63, the Satz5 argument and conclusion on pp.63–64, the Satz6 statement on p.64, and the complete erratum pp.35–36 were reread. Satz6 explicitly omits its proof, so no reading of that unprinted proof is claimed. The application verifies properness, flatness, reducedness of the base, h1=0, chi=4 and h0=4 before invoking the rank-four base-change and evaluation maps. The closed degeneracy set of that concrete evaluation is used; the corrected claim about the general exceptional base-change locus in Satz2 is not invoked. The existing bibliography entries and locators remain correct.

No primary text or image is included in this package; the source table gives URLs, versions, hashes, loci and own paraphrases.

## Validation and remaining gates

The whole-unit guard matches the current source. The statement, every original label and permanent target, all original construction displays and both numbered equations are preserved. The two verification displays are replaced by the exact equivalent equations documented above. The reference keys resolve; environments balance; display paragraphs contain no blank line; no manual tags or process vocabulary remain.

The two recorded events are the exposed complete proof comparison and the bounded exact algebra computations. The example is the only unit covered. Root owns integration, the current pdfLaTeX build and rendered-page reading, final first-part consistency and final counts. No whole-section or final-paper closure is claimed.
'''
(OUT/'S6_SERIES_PUBLISH_p205_comparison.md').write_text(report)
print('P205 ready: statement identical; all construction displays preserved; only two equivalent verification displays replaced; 31 exact rows, 2 events, 25 unit outcomes.')
