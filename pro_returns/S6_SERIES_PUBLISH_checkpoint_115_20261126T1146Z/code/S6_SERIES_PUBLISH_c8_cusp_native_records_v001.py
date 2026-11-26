"""Record the two complete unit reviews without shared/canonical writes."""
import csv
from datetime import datetime, timezone
from pathlib import Path

root=Path(__file__).resolve().parent.parent
lane=root/'agents/continuation8_iii_weighted_units'
fields=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where']
attribution='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical reasoning effort not separately exposed; continuation eight unit editor'
now=datetime.now(timezone.utc).isoformat()
items=[
    ('CUSP_NULLBORDISM','cusp_nullbordism',411,62,[
        ('Q258','wb:def:marked-cusp-nullbordism-data','Whole numbered actual input read: original member, global cusp p_0 with t(p_0)=0, complete C(t), ordered beta/inverse, deck map/inverse, skeleton and reduced target, d/phi/g_C and inverses. Bounded Paper I8386-8455 supports the final fam:src:A.3.1 locator; no whole Paper I claim.'),
        ('038S','wb:cusp-null:thm','Whole original statement and320 proof lines, entire receiving proof/comparison/primary record, whole final410-line source plus the exact final global-cusp input change read. Every original period, complete torus, uniform chart, ordered derivative, exact Q255 application, frame cylinder, full collared cap/inverse, frame extension and arbitrary x_0 exclusion checked. One full theorem/proof remains.'),
        ('03A6','wb:cusp_s12_carrier_homotopy:L567','Whole original/receiving/comparison and final statement/proof read. Actual based H and both ordered suspension homotopies checked. The native coefficient is defined after proved zero through the exact delta isomorphism onto the even subgroup and inverse; all additive/multiplicative characters retain full scope. No later038X premise is needed.')
    ]),
    ('NATIVE_SPHERE','full_sphere_nullity',623,88,[
        ('Q256','wb:def:native-sphere-carriers','Whole numbered native input read. Same original Q258 d/phi/g coordinates with inverses; literal q2,p,g on every collapsed piece, A two-pole basepoint, P/Q and ordered block maps. Duplicate coordinate formulas replaced only by their exact permanent owner.'),
        ('Q254','wb:cusp-s12-native-smash-null','Whole native application read with the full earlier038V proof and actual035X/036J construction. Literal mu33(g_C smash g_C)mu66 inverse and all inverse transports identify the exact quotient; apply x=y=g_C with unchanged continuity/surjectivity/quotient scope.'),
        ('038X','wb:cusp-s12-one-copy-invariant','Whole original47-line proof, entire receiver/comparison/primary records, complete final candidate1-622 and exact bounded six-cell product statement correction read. Integral L/kernel/inverse, E6 even injection and fixed-generator coefficient inverse, every radius/open-cell whole fibre, monodromy/product inverse, exact Q255 frame application, and the full same-torus quaternion/J degree-unit0/1 witness with homology transport checked.'),
        ('038W','wb:cusp-s12-nullity-scope','Whole original11-line proof and full143-line receiver/comparison read; whole final statement/proof read. Exact P Q and pinch homomorphism, actual C2 retract, seven-piece based wedge equivalence, C4 retract, J/R and nonzero beta detector checked. Complete036J prior proof read; both initial quotient maps, moving four-spheres, entire-ball isometries/inverses and thresholds T-C>4R,ell_T>4R retained.'),
        ('Q257','wb:remark:two-cusp-postcompositions','Entire final numbered comparison read after both frame owners. Full moved retained/cusp content retained: same A/q2, actual p3/hat_p2 composites, inverse parameter inclusion, exact ordered frame/cylinder/cap relation, eta4 eta5 versus0 images and detected q2, actual phi4/inverse Hopf smash and stable inverse proving12nu6. No unsupported equality of framings or identification of native Q with beta is asserted.')
    ])
]
def write(path,header,rows):
    temporary=path.with_suffix(path.suffix+'.tmp')
    with temporary.open('w',newline='') as f:
        writer=csv.writer(f,delimiter='\t',lineterminator='\n');writer.writerow(header);writer.writerows(rows)
    temporary.replace(path)
for prefix,fragment,linecount,defectcount,events in items:
    relative='agents/continuation8_iii_integration/units/root/'+fragment+'.tex'
    text=(root/relative).read_text()
    assert len(text.splitlines())==linecount
    assert '\r' not in text
    review=lane/('S6_SERIES_PUBLISH_'+prefix+'_unit_review.md')
    criteria=[]
    for line in review.read_text().splitlines():
        if line.startswith('| '):
            cells=[x.strip() for x in line.strip('|').split('|')]
            if cells[0] in {f'D{i:02}' for i in range(1,28)}|{'Structure'}:
                assert len(cells)==2
                criteria.append([cells[0],'source-local complete; root admission/global gates open',cells[1]])
    assert len(criteria)==28
    table=lane/('S6_SERIES_PUBLISH_'+prefix+'_publication_defects.tsv')
    with table.open(newline='') as f:
        reader=csv.DictReader(f,delimiter='\t');defect_fields=reader.fieldnames;defects=list(reader)
    assert len(defects)==defectcount
    assert len({row['change_id'] for row in defects})==defectcount
    for row in defects:
        row['review_status']='whole final statement/proof and exact bounded refinements read; source-local complete; root canonical consolidation, progress admission and global gates open'
    write(table,defect_fields,[[row[key] for key in defect_fields] for row in defects])
    write(lane/('S6_SERIES_PUBLISH_'+prefix+'_unit_criteria.tsv'),['criterion','proposed_state','evidence'],criteria)
    output=[]
    for tag,owner,scope in events:
        event='III-C8-'+prefix.replace('_','-')+'-'+tag+'-PUBLICATION-READBACK'
        full=scope+' No new required or independent-check credit; root owns actual admission and global gates.'
        output.append([owner,'2026-11-25',attribution,'used and rechecked in this run',full,event,'continuation-eight-publication',str(review.relative_to(root)),'whole substantive review','used and rechecked in this run',event,'','',now,relative])
    write(lane/('S6_SERIES_PUBLISH_'+prefix+'_CHECK_EVENTS.tsv'),fields,output)
    print('UNIT',prefix,'LINES',linecount,'CRITERIA',len(criteria),'EXACT_DEFECT_ROWS',len(defects),'EVENTS',len(output))
    for tag,owner,scope in events:
        print('READ_EVENT',tag,owner,scope)
print('UTC',now)
print('CANONICAL_AND_SHARED_WRITES 0; INDEPENDENT_CHECK_CREDIT 0; NO_MATHEMATICAL_RERUNS; NO_HASH_COMPUTATIONS')
