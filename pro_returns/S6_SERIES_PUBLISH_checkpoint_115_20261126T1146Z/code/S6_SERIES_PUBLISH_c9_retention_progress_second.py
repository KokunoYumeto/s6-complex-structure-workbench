"""Admit the next actual source dispositions; keep remaining PDF gates open."""
from pathlib import Path
from datetime import datetime, timezone
import csv

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
now = datetime.now(timezone.utc).isoformat()
def read(name):
    with (ROOT/name).open(newline='') as f:
        r=csv.DictReader(f,delimiter='\t');return r.fieldnames,list(r)
def write(name,fields,rows):
    with (ROOT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)

closed={
 'maps:src:D.2.9':('C9-III-RETAINED-02LZ-USED-001','agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_retained_02LZ_review.md','All ten finite homology-generator uses now have u_fib, preserving the actual root coordinate and complete abelianization/section/transfer inverse.'),
 'maps:src:D.2.10':('C9-III-RETAINED-02KK-USED-001','agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_retained_02KK_review.md','The invariant class and CRT coefficients have their exact distinct names, with both existing quotient/CRT composites unchanged. Remaining Smith/formal-argument roles are documented from current source.'),
 'maps:src:D.2.13':('C9-III-RETAINED-02KN-USED-001','agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_retained_02KN_review.md','All concrete deformation-site, transvection, centralizer, cochain and local-period roles are propagated through their actual formulas and inverses.'),
 'maps:src:D.2.37':('ce:c9-iii-current02-02ld-retention-reconciliation','agents/continuation9_findings/S6_SERIES_PUBLISH_c9_current02_02LD_retention_review.md','All15 fragments for E_perm/E_att, additive/multiplicative primitive vectors, c_Ch and upright count labels are admitted; actual option-label fonts and the t_cyc import are retained.'),
 'maps:src:D.2.49':('C9-III-RETAINED-02LQ-USED-001','agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_retained_02LQ_review.md','The averaging operator and every marked Wang-generator use are qualified. The normalization inverse, central extension and torsion group retain their exact maps.'),
 'night:P3F.26':('C9-III-RETAINED-02S2-USED-001','agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_retained_02S2_review.md','Modular loops, cubic coefficients, uniformizing root and all height-coordinate uses are qualified; the actual cusp units and02S3 imports remain fixed. The enlarged isomorphism/inverse display is set on two rows with identical ordered expressions.'),
}
_,events=read('CHECK_EVENTS.tsv')
uf,units=read('S6_SERIES_PUBLISH_unit_progress.tsv')
for subject,(event,evidence,detail) in closed.items():
    assert sum(e['event_id']==event for e in events)==1,event
    assert (ROOT/evidence).is_file()
    row,=[r for r in units if r['paper']=='III' and r['unit_id']==subject and r['defect_type']=='D20']
    assert row['status']=='open',subject
    row.update(status='done',date_utc=now,evidence=row['evidence']+'; '+evidence,
       detail=row['detail']+' Final retained-role source packet admitted: '+detail+' Exact full-source reversal and permanent identifiers checked; changed-page gates remain.')
subject='night:P3F.34'
row,=[r for r in units if r['paper']=='III' and r['unit_id']==subject and r['defect_type']=='D20']
assert row['status']=='done'
row.update(status='open',date_utc=now,evidence=row['evidence']+'; continuation9 current02SB retained-role source reassessment',
    detail=row['detail']+' Reopened for the actual initial affine root-gluing vector a and the final Bezout coefficients a,b. The exact affected maps and inverse coefficients are being compared; no paragraph-only retention is accepted.')
radial='agents/continuation9_root_image_repairs/S6_SERIES_PUBLISH_c9_root_radial_imports_review.md'
for subject,tag in [('mapsIII:sec:regular-quotients','039U'),('wb:cusp-cone-obstructions','0374'),('wb:cusp-cone-optimal-exponents','0375')]:
    row,=[r for r in units if r['paper']=='III' and r['unit_id']==subject and r['defect_type']=='D20']
    assert row['status']=='done',subject
    assert sum(e['event_id']=='publish:c9:III:'+tag+':radial-import-readback' for e in events)==1
    row.update(date_utc=now,evidence=row['evidence']+'; '+radial,
      detail=row['detail']+' Actual radial-import comparison admitted: the limiting coefficient is bound directly by Im b(0), pointwise matrices retain their established native T-indexed entries, and all affected remainder/slice uses are exact. Entrywise identity and inverse, source reversal and existing quotient maps were compared; final changed images remain.')
ff,findings=read('S6_SERIES_PUBLISH_findings_III.tsv')
row,=[r for r in findings if r['id']=='P15'];assert row['status']=='open'
row['date_utc']=now
row['source_resolution']+=' Six further retained-role source rows are now closed by their admitted exact packets. The root radial-import packet resolves the concrete remaining B import through the actual time-indexed period entries and limiting value. The newly confirmed02SB affine-vector/Bezout case is explicitly reopened.'
row['remaining_gate']='Finish actual02LL and02LS packets, the remaining02LB/02LE/02LF/02LJ/02LT/02LV/02SB roles, and the final authored-retention readback of the early Theorem3.8 candidate note. Admit each exact affected-use comparison before the final whole-paper P11/P15 source disposition, counts and builds. Actual final-page/layout gates remain separately open.'
write('S6_SERIES_PUBLISH_unit_progress.tsv',uf,units)
write('S6_SERIES_PUBLISH_findings_III.tsv',ff,findings)
print('Closed six further exact source scopes:',', '.join(closed))
print('Reopened02SB; appended the resolved actual radial-import evidence to three existing done rows.')
print('Whole-paper P15 and all final rendering gates remain open. No raw event or derived count changed.')
