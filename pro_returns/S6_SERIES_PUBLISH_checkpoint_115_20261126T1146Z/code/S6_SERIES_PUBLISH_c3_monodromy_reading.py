"""Record the complete receiving reading after the monodromy consolidation."""
from S6_SERIES_PUBLISH_c3_edit import *

event='II-C3-ROOT-MONODROMY-SINGLE-OWNER'
add_event('night:P4.13;cdp:st:C.2.UN.11;cdp:st:C.2.UN.4',event,
 'used and rechecked in this run',
 'Root read the complete original P413 and 14-item UN11 proof, the complete receiving P413 and 11-item UN11 proof, and the exact UN4 blowup application. All nineteen table rows are byte-identical. Nearby-cycle stalks, two-step degree-one filtration, transpose evaluation, Mobius inversion, minimum multiplicity, cyclotomic support, Jacobian and Gaussian torus automorphisms, positive-meridian inverse, compact quotient, Euler adjustments and final two reducible SNC fibres are preserved. The broad proof is transferred to P413 and UN11 applies it on identical maps. All original identifiers are preserved; manual equation numbers become section numbers. No independent derivation or final-page reading is claimed.',
 'Complete P413/UN11 before and after, and UN4 same (r,u,v) chart maps',source=__file__)
add_event('cdp:st:C2c','II-C3-ROOT-TORIC-EULER-UNIT',
 'used and rechecked in this run',
 'Root read the complete old and receiving C2c proofs and actual images of Mumford 1972 printed pp264–268. Retained all fan charts, lattice shear, proper-discontinuity bounds, compact fundamental-domain representatives, fibre quotient and Euler counts. The displayed base-change t to pi identifies each dual-cone monomial semigroup with the source affine ring; face inclusions are the same monomial localizations. Read the printed statements and available proofs only: Mumford omits the regularity assertion proof and Proposition6.7 proof. The complete complex-disc properness argument remains in the paper.',
 'C2c complete unit; Mumford1972 pp264–268 images',source=__file__)
add_event('cdp:st:C.2.UN.11;cdp:st:C.2.UN.44;cdp:st:C.2.UN.64;cdp:st:C.2.UN.66',
 'II-C3-ROOT-PROGRAM-158-ADMISSION','used and rechecked in this run',
 'Admitted the four plain repository paths verified by the provenance agent against the attached inventory and prescribed pinned bytes. Root read the full scope/hash table and receiving appendix rows. Agent read all four full sources; no execution claimed. UN11 body file bookkeeping is removed and its explicit I4 versus I4+E12 calculation is retained with the two minimal polynomials. Records-table regeneration remains at text-final.',
 'agents/continuation3_provenance/S6_SERIES_PUBLISH_c3_provenance_program_checks158.tsv',source=__file__)

fields,rows=read_tsv(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv')
for row in rows:
 if row['change_id'].startswith(('II-C3-MONODROMY-OWNER-','II-C3-MONODROMY-RANGE-','II-C3-TORIC-EULER-')):
  row['review_status']='Complete old and new proofs read and compared by root; exact maps and every numerical consequence checked against the originals. CHECK_EVENTS: '+event
write_tsv(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',fields,rows)

source=dict(source='Mumford 1972 (third-continuation toric Euler model)',
 url='https://www.numdam.org/article/CM_1972__24_3_239_0.pdf',
 version='Compositio Mathematica24(1972),239–272; original Numdam journal scan',
 locus='Section6, complete printed pp264–268 read as text and five individual page images; (6.1)–(6.7), including the explicitly omitted-proof notices',
 date_utc=now(),sha256='9a1349cbd2869357427149e3339629c016f9a9c9398676d21a225cc2c4f7e1a5',
 own_word_summary='The valuation map identifies torus-invariant affine models with polyhedra; a monomial is admitted by its nonnegative affine valuation inequality. Open faces correspond to central torus orbits with complementary dimensions. Faces give monomial localizations, and invariant polyhedral decompositions give the period action. The source states regularity for unimodular simplices and the Delaunay polarization result with their proofs omitted.',
 use='C2c: base change C[t] to C[[pi]], t maps to pi, takes the exact dual-cone semigroup monomial to the source monomial; face maps and lattice shears coincide. The full analytic free-action and properness proofs are given in the manuscript.')
append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',[source],'source')

path=ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv'
fields,rows=read_tsv(path)
oldunit='subsec:II:euler-monodromy-signatures'
newunit='subsec:II:rank-four-monodromy-signatures'
assert not any(r['paper']=='II' and r['unit_id']==newunit for r in rows)
oldrows=[r.copy() for r in rows if r['paper']=='II' and r['unit_id']==oldunit]
assert len(oldrows)==26
for row in rows:
 if row['paper']=='II' and row['unit_id']==oldunit:
  kind=row['defect_type'] or row['row_kind']
  row['unit_title']='Semistable toric Euler models'
  if kind not in ['D10','D16']:
   row.update(status='open' if kind in ['D14','D23','structure'] else 'done',date_utc=now(),
    evidence='CHECK_EVENTS.tsv: II-C3-ROOT-TORIC-EULER-UNIT',
    detail='Complete old and receiving unit read. All local instances logged, including exact primary-source comparison. Final placement and rendered typography remain open.' )
for row in oldrows:
 kind=row['defect_type'] or row['row_kind']
 row.update(unit_id=newunit,unit_title='Rank-four monodromy stratum signatures',
  status='open' if kind in ['D14','D18','D23','structure'] else 'done',date_utc=now(),
  evidence='CHECK_EVENTS.tsv: '+event,
  detail='Migrated from the complete old Euler/monodromy unit; migration itself is not movement credit. Complete receiving unit read. Final whole-paper placement, bibliography and PDF typography remain open.')
 rows.append(row)
write_tsv(path,fields,rows)
print('Complete receiving comparisons, primary reading and program158 admission recorded.')
