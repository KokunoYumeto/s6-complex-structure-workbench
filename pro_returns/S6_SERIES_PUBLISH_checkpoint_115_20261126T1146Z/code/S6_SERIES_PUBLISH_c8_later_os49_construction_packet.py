#!/usr/bin/env python3
"""Record the completed attributed construction review; no shared writes."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import csv,json

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation8_iii_later'
SOURCE=ROOT/'agents/continuation8_iii_integration/units/later/os49_construction.tex'
assert sha256(SOURCE.read_bytes()).hexdigest()=='98f4eadfe59097087f7810205ed21441e8a3731ed825dc923e0a7929219a632c'
stamp=datetime.now(timezone.utc).isoformat()
who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed'

def write_tsv(path,fields,rows):
    with path.open('w',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=fields,delimiter='\t',lineterminator='\n')
        writer.writeheader();writer.writerows(rows)

def metadata(path):
    content=path.read_bytes()
    return dict(path=str(path.relative_to(ROOT)),bytes=len(content),
                lines=len(content.splitlines()),sha256=sha256(content).hexdigest())

defects=OUT/'S6_SERIES_PUBLISH_III_os49_construction_publication_defects.tsv'
with defects.open(newline='') as stream:
    reader=csv.DictReader(stream,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
assert len(rows)==88
for row in rows:
    row['review_status']='whole repaired proofs, full v002/v003, complete v004 diff and changed scopes read; all 88 exact rows read; source-local publication review complete; root/global/render gates pending'
write_tsv(defects,fields,rows)

event_fields=['statement_id','date','who','type','outcome','event_id','phase',
              'source_file','source_row','source_event_type','evidence_group',
              'publish_input_file','publish_input_row','date_utc','where']
events_path=OUT/'S6_SERIES_PUBLISH_III_os49_construction_publication_CHECK_EVENTS.tsv'
review=OUT/'S6_SERIES_PUBLISH_III_os49_construction_publication_review.md'
specific=[
('night:P3F.26','02S2',6,'Complete explicit cubic, line divisor, modular/peripheral marking, original and toric fillings, affine cap, integral specialization/parabolic complexes, signed differentials and sphere recognition read against the exact admitted proof.'),
('night:P3F.27','02S3',603,'Complete angular clutch proof read with the full F_(p,q) directed-period map, both branch integers, unit-chart inverses, moving endpoint, positive full line winding and based-lift unit transport.'),
('night:P3F.28','02S4',863,'Complete section-line iterate and direct-image proof, compact regular-binding cover, minimalization, common resolution, exact exceptional correction, both squares and all integer translates read against the admitted proof and pullback comparison.'),
('night:P3F.29','02S5',1240,'Complete all-3k coprime cap proof read; all full specialization lattices, four signed +n differentials and proper r-family retained. Common homology and sphere conclusions use KL through the exact source/period/root/collar/normal/fan and parameter maps of Q30N.'),
('os49:rem:type-c-marking','Q30N',1099,'Complete actual geometric marking bridge read: source and linearization scalar/inverse, G0 inverse, full periods, Poincare frame, finite/cusp values and Yang affine laws, parameter inverse, inverse Hurwitz/F0, roots/collars/positive normals and every toric chart. Root and foundations complete cross-readings are attributed in the review.')]
events=[]
for j,(sid,tag,line,description) in enumerate(specific,2):
    events.append(dict(statement_id=sid,date=stamp[:10],who=who,
       type='used and rechecked in this run',
       outcome=description+' Exposed source-local publication recheck only; no independent proof, historical-computation, global-reference/bibliography, final-placement or rendered-page credit.',
       event_id='publish:c8:III:'+tag+':os49-construction-publication-recheck',
       phase='continuation8-later-publication',source_file=str(SOURCE.relative_to(ROOT)),
       source_row=str(line),source_event_type='used and rechecked in this run',
       evidence_group='publish:c8:III:later-unit-editing',
       publish_input_file=str(events_path.relative_to(ROOT)),publish_input_row=str(j),
       date_utc=stamp,where=str(review.relative_to(ROOT))))
write_tsv(events_path,event_fields,events)

program_fields=['program_id','purpose','source_file','source_lines','source_sha256',
                'stdout_file','stdout_lines','stdout_sha256','stderr_file','stderr_bytes',
                'stderr_sha256','review_scope','publication_placement']
program_rows=[]
for suffix,purpose,scope,placement in [
('compare_v001','Exact admitted proof extraction comparison',
 'Whole 32-line source, all 33 actual stdout lines and empty stderr read; byte identity is an input guard, not mathematical proof.',
 'Audit record only; no program narration in theorem proofs.'),
('marking','Integral OS49 and Type C candidate marking identities',
 'Whole 36-line source, all 12 actual stdout lines and empty stderr read; matrix products and inverses only. Geometric identification is the written bridge.',
 'Supplementary program table: exact marking algebra.'),
('bridge_v002','Actual period affine laws and signed boundary algebra',
 'Whole 53-line source, all 11 actual stdout lines and empty stderr read; G0, all affine entries, parameter inverse, contractions and cross product. Geometry remains in the written chart/roof proofs.',
 'Supplementary program table: period and transfer identities.')]:
    stem=ROOT/'code'/('S6_SERIES_PUBLISH_c8_later_os49_'+suffix)
    src=metadata(stem.with_suffix('.py'));stdout=metadata(stem.with_suffix('.out'));err=metadata(stem.with_suffix('.err'))
    program_rows.append(dict(program_id='c8-III-os49-'+suffix,purpose=purpose,
      source_file=src['path'],source_lines=src['lines'],source_sha256=src['sha256'],
      stdout_file=stdout['path'],stdout_lines=stdout['lines'],stdout_sha256=stdout['sha256'],
      stderr_file=err['path'],stderr_bytes=err['bytes'],stderr_sha256=err['sha256'],
      review_scope=scope,publication_placement=placement))
program_path=OUT/'S6_SERIES_PUBLISH_III_os49_program_table_proposals.tsv'
write_tsv(program_path,program_fields,program_rows)

files=[SOURCE,review,OUT/'S6_SERIES_PUBLISH_III_os49_construction_actual_units.md',
       defects,events_path,program_path,
       OUT/'S6_SERIES_PUBLISH_III_os49_equation_aliases.tsv',
       OUT/'S6_SERIES_PUBLISH_III_os49_marking_bridge.md']
for v in ['v002','v003','v004']:
    files.append(OUT/('S6_SERIES_PUBLISH_III_os49_construction_publication_'+v+'.diff'))
manifest=OUT/'S6_SERIES_PUBLISH_III_os49_construction_publication_packet.json'
manifest.write_text(json.dumps(dict(frozen_utc=stamp,reviewer=who,
   scope='Source-local exposed whole-proof publication recheck; root owns final admission and global gates.',
   records=[metadata(p) for p in files]),indent=2)+'\n')
print('FROZEN_UTC',stamp)
for p in files+[manifest]:
    print(json.dumps(metadata(p),sort_keys=True))
print('DEFECTS',len(rows),'EVENTS',len(events),'PROGRAM_PROPOSALS',len(program_rows))
print('NO_CANONICAL_OR_SHARED_LEDGER_WRITES; NO_INDEPENDENT_OR_GLOBAL_CREDIT')
