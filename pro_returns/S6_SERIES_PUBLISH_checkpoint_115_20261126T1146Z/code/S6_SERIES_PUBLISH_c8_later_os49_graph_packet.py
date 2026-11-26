#!/usr/bin/env python3
"""Freeze the attributed graph-cap publication packet; local records only."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import csv,json

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation8_iii_later'
SOURCE=ROOT/'agents/continuation8_iii_integration/units/later/os49_graph_caps.tex'
assert sha256(SOURCE.read_bytes()).hexdigest()=='32db96ede02a8925e5aa6e29670cb21fb24cad4facfe49942810710e6867436e'
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

defects=OUT/'S6_SERIES_PUBLISH_III_os49_graph_caps_publication_defects.tsv'
with defects.open(newline='') as stream:
    reader=csv.DictReader(stream,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
assert len(rows)==63
owner_counts={}
for index,row in enumerate(rows,1):
    if index>=37:
        assert row['statement_id']=='sec:III:os49-night'
        owner='night:P3F.31' if index<=39 else 'night:P3F.33' if index<=45 else 'night:P3F.34'
        row['statement_id']=owner
        owner_counts[owner]=owner_counts.get(owner,0)+1
    row['review_status']='whole original and final statements/proofs, all diffs and all 63 exact rows read; source-local exposed publication recheck complete; bounded SB orientation repair explicit; root/global/render gates pending'
write_tsv(defects,fields,rows)

event_fields=['statement_id','date','who','type','outcome','event_id','phase',
              'source_file','source_row','source_event_type','evidence_group',
              'publish_input_file','publish_input_row','date_utc','where']
events_path=OUT/'S6_SERIES_PUBLISH_III_os49_graph_caps_publication_CHECK_EVENTS.tsv'
review=OUT/'S6_SERIES_PUBLISH_III_os49_graph_caps_publication_review.md'
specific=[
('night:P3F.31','02S8',2,'Whole latest admitted positive-fan graph/page/trace/return proof and complete publication proof read. All actual source, line, caps, inverse charts, primitive lattice, normal/framing signs and characteristic/return conclusions retained; the missing graph display closer is repaired.'),
('night:P3F.32','02S9',913,'Whole latest admitted all-k, both-sign and every-d sphere-return proof and publication proof read. All finite/original/toric cap maps, full character inverses, numerator involution and negative-fan base-change values remain; the existing final negative-family conclusion is now in the theorem.'),
('night:P3F.33','02SA',1345,'Whole repaired original and rewritten free-sector proof read. Every deck power, primitive quotient and inverse, fixed-point sufficiency, arbitrary-integer freeness criterion and exact fundamental-group quotient remain. No c4-c7 receiver or blind recheck is claimed.'),
('night:P3F.34','02SB',1454,'Whole repaired original and rewritten homology proof, full 189-line sign note, historical source-scope report and 98-line historical code read. Exact based roofs, normal inversion and Thom generator maps repair the intermediate final pair arrow to -n while preserving all transfer columns and every final group. KL scope remains unchanged; historical actual outputs were unavailable and are not credited.')]
events=[]
for j,(sid,tag,line,description) in enumerate(specific,2):
    events.append(dict(statement_id=sid,date=stamp[:10],who=who,
      type='used and rechecked in this run',
      outcome=description+' Exposed source-local publication recheck only; no independent proof, new required-check closure, global-reference/bibliography, final-placement or rendered-page credit.',
      event_id='publish:c8:III:'+tag+':os49-graph-publication-recheck',
      phase='continuation8-later-publication',source_file=str(SOURCE.relative_to(ROOT)),
      source_row=str(line),source_event_type='used and rechecked in this run',
      evidence_group='publish:c8:III:later-unit-editing',
      publish_input_file=str(events_path.relative_to(ROOT)),publish_input_row=str(j),
      date_utc=stamp,where=str(review.relative_to(ROOT))))
write_tsv(events_path,event_fields,events)

files=[SOURCE,review,OUT/'S6_SERIES_PUBLISH_III_os49_graph_caps_actual_units.md',
       defects,events_path,OUT/'S6_SERIES_PUBLISH_III_os49_graph_equation_aliases.tsv',
       OUT/'S6_SERIES_PUBLISH_III_os49_boundary_sign.md']
for v in ['v002','v003','v005']:
    files.append(OUT/('S6_SERIES_PUBLISH_III_os49_graph_caps_publication_'+v+'.diff'))
manifest=OUT/'S6_SERIES_PUBLISH_III_os49_graph_caps_publication_packet.json'
manifest.write_text(json.dumps(dict(frozen_utc=stamp,reviewer=who,
  scope='Source-local exposed whole-proof publication recheck; root owns admission and global gates.',
  existing_program_proposal='agents/continuation8_iii_later/S6_SERIES_PUBLISH_III_os49_program_table_proposals.tsv',
  historical_program_scope='Whole source and report only; actual historical output unavailable, no rerun or output credit.',
  owner_metadata_corrections=owner_counts,
  records=[metadata(p) for p in files]),indent=2)+'\n')
print('FROZEN_UTC',stamp)
print('OWNER_METADATA_CORRECTIONS',json.dumps(owner_counts,sort_keys=True))
for p in files+[manifest]:
    print(json.dumps(metadata(p),sort_keys=True))
print('DEFECTS',len(rows),'EVENTS',len(events),'NEW_EQUATION_IDENTITIES',9)
print('NO_CANONICAL_OR_SHARED_LEDGER_WRITES; NO_INDEPENDENT_OR_GLOBAL_CREDIT')
