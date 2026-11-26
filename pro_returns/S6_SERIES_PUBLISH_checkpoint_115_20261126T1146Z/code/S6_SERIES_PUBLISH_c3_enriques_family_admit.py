"""Admit the complete Enriques/Kummer family consolidation and common cover."""
from S6_SERIES_PUBLISH_c3_edit import *
import json

folder=ROOT/'agents/continuation3_occurrence_root'
prefix='S6_SERIES_PUBLISH_c3_enriques_family_'
before=SOURCE.read_text(); after=before
for row in json.loads((folder/(prefix+'guards.json')).read_text()):
    assert after.count(row['old'])==1,row['key']
    after=after.replace(row['old'],row['new'],1)
preserve_identifiers(before,after)
for old,new in zip(identifiers(before),identifiers(after)):
    assert all(new[k]==v for k,v in old.items())
    assert all(new[k]==1 for k in new-old)
SOURCE.write_text(after,newline='\n')
_,rows=read_tsv(folder/(prefix+'defects.tsv'))
for row in rows:
    row['review_status']='Root read complete old UN25/27/30 and complete receiving merged family/UN30/P347, plus complete original and receiving UN18 covering block. Final bounded origin, Jacobian-spacing, projectivity-source and line-name changes reread. Exposed used-and-rechecked comparison only.'
print('Defects',append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',rows,'change_id'))

fields,progress=read_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
for row in progress:
    if row['paper']=='II' and row['unit_id']=='sec:II:09':
        row.update(unit_title='Elliptic torsors and Hopf components; remaining occurrence units',date_utc=now(),
            evidence='CHECK_EVENTS.tsv: II-C3-ROOT-ENRIQUES-FAMILY-ADMISSION',
            detail='Original section9 open identity remains on subsec:II:enriques-elliptic-occurrence, now immediately before UN34. The newly reviewed Enriques/Kummer subdivisions earn no original-row movement credit; the assigned UN34/35/37 and UN41/42/43/45 receivers remain pending.')
for unit,title in [('subsec:II:projective-root-covers','Projective covers of signed elliptic roots'),
    ('subsec:II:enriques-family-occurrence','Enriques and elliptic components with coherent Euler characteristic one'),
    ('subsec:II:kummer-elliptic-occurrence','Elliptic components in the Kummer family')]:
    for kind in [f'D{i:02}' for i in range(1,26)]+['structure']:
        status='open' if kind in ['D14','D23','D24','structure'] else 'done'
        progress.append(dict(zip(fields,['II',unit,title,'structure' if kind=='structure' else 'defect',
            '' if kind=='structure' else kind,status,now(),
            'CHECK_EVENTS.tsv: II-C3-ROOT-ENRIQUES-FAMILY-ADMISSION',
            'Complete original/receiving statements and proofs read against every register class. Exact covering, quotient, canonical, cohomology and divisor-persistence morphisms compared; r=2 aliases have explicit identity specialization. Original section9 remains open on its remaining actual subsection. Final placement, typography and front matter stay open.'])))
keys=[(r['paper'],r['unit_id'],r['defect_type'] or r['row_kind']) for r in progress]
assert len(keys)==len(set(keys))
write_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',fields,progress)
source=dict(source='ColtoiuGasitoiJoita2012 (third-continuation projective root covers)',
    url='https://www.numdam.org/item/10.1016/j.crma.2012.02.002.pdf',
    version='Published Comptes Rendus Mathematique350(5-6),2012,239-241; DOI10.1016/j.crma.2012.02.002',
    locus='Complete title/metadata and introduction p239; complete printed text pp240-241, including Theorem2 and its entire proof p241. Root rendered and viewed/read p241.',
    date_utc=now(),sha256='b03e9716a93f5f1c22286286617b871bf908ee5d314f4b49aba9e35eda39e22f',
    own_word_summary='A surjective holomorphic map from a projective reduced compact complex space to a normal compact complex space with constant fibre dimension has projective target. The printed proof invokes Remmert--van de Ven for discrete fibres and reduces positive fibre dimension by projective hypersurfaces. No reading of the cited 1961 proof is claimed.',
    use='Apply the zero-dimensional-fibre case to the explicit finite map C-prime times E_q to P, the finite Klein-four quotient C_r times E to X_r, and the involution quotient B_r to its normal target. The stated hypotheses hold for each identical constructed map. The ordinary blowups of the A1 points then give the projective resolutions.')
print('Sources',append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',[source],'source'))
add_event('lem:II:torsion-root-product-cover;cdp:st:C.2.UN.18;cdp:st:C.2.UN.25;cdp:st:C.2.UN.27;cdp:st:C.2.UN.30',
    'II-C3-ROOT-ENRIQUES-FAMILY-ADMISSION','used and rechecked in this run',
    'Root read every complete original UN25/27/30 statement/proof, the full old UN18 covering block, complete receiving P347, merged UN25/27, full receiving UN30 and the bounded UN18 receiver. Every final amended paragraph was reread. P347 owns the full torsion-line signed-root product-cover proof on an arbitrary compact curve, including connected cyclic normalization, torsion frame, both root Jacobians and a freshly opened exact projectivity theorem. UN18 uses the same B=E,D=points,m,q; the r-family uses B=P1,N=O,m=2 and identity frame; UN30 uses B=E0 and its explicitly torsion signed point divisor with N=mathcalN. UN25 is the exact r=2 member of one complete UN27 statement/proof: compact Weierstrass base, involutions, both parity cases, ambient quotient/resolution, full multiplicities, canonical divisor/floor pushforward, all incidence maps and ranks, six unchanged-component balancing blocks, essentiality and distinct growth slopes remain. Every old statement/equation label and target occurs once; aliases have their exact identity specialization. UN30 retains both special supports, all32 ambient quotient points, canonical/euler/cohomology computations and20 blocks on each support. P339/P337/P234/P236 applications name their actual maps. Programs already listed in appendix160 remain there. No statement is refuted, no independent-check or final-page credit is claimed, and the original section9 remainder stays open.',
    'Projective product covers and complete Enriques/Kummer occurrence families',source=__file__)
print('P347, merged UN25/27, complete UN30 and bounded UN18 admitted.')
