#!/usr/bin/env python3
"""Freeze the completed, attributed conifold source-local review packet."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import csv,json
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation8_iii_later'
SOURCE=ROOT/'agents/continuation8_iii_integration/units/later/conifold_constructions.tex'
assert sha256(SOURCE.read_bytes()).hexdigest()=='757aeac25dc9df0a2ad3ed44f2c5860a7054eb1e218b932a6e8b86e1e5a93ae0'
stamp=datetime.now(timezone.utc).isoformat()
who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed'
def write_tsv(p,fields,rows):
 with p.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
def meta(p):
 b=p.read_bytes();return dict(path=str(p.relative_to(ROOT)),lines=len(b.splitlines()),bytes=len(b),sha256=sha256(b).hexdigest())
p=OUT/'S6_SERIES_PUBLISH_III_conifold_publication_defects.tsv'
with p.open(newline='') as f:
 r=csv.DictReader(f,delimiter='\t');fields=r.fieldnames;rows=list(r)
assert len(rows)==29
for row in rows:
 row['review_status']='whole repaired and v001 proofs, entire changed v002 M1/MK proofs, all 390+38 diff lines and all 29 exact rows read; exposed source-local review complete; root/global/render gates pending'
write_tsv(p,fields,rows)
review=OUT/'S6_SERIES_PUBLISH_III_conifold_publication_review.md'
events_path=OUT/'S6_SERIES_PUBLISH_III_conifold_publication_CHECK_EVENTS.tsv'
fields=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where']
spec=[
('maps:src:D.3.1','02M0',4,'Whole admitted moving-zero proof and publication proof read: full core/neck/collars, frame cocycles, compact representatives, properness, both flatness maps, full original finite twists, unique node, chosen diagonal and section-coordinate inverse retained. Existing joint-flatness conclusion now explicit in statement.'),
('maps:src:D.3.2','02M1',272,'Whole admitted smoothing topology proof and final proof read. Entire theorem/proof precedes its actual M2 use; exact complex-linear quadric map and inverse supplied. Tube, actual exterior flow, Thom/Mayer-Vietoris generators, integral extension, pairing and oriented classification remain.'),
('maps:src:D.3.3','02M2',386,'Whole admitted and publication complex-invariants proof read. Full residues/root orders, canonical divisor/powers, divisor-area obstruction, field descent/inverse, period/line comparison, contraction formal functions and proper-flat-family cohomology retained.'),
('maps:src:D.3.4','02M3',584,'Whole admitted and publication comparison proof read. Actual published action, Hopf/torus fibres, algebraic-reduction field maps, Mobius base map and inverse fibre homology obstruction retained in the exact original subfamily.'),
('maps:src:E.2.2','02MK',652,'Whole repaired original and final transverse-pullback proof read as exposed input, with no c4-c7 receiver claimed. Fixed original f/X/B and three critical values explicit. Exact differential, holomorphic and smooth product maps, Kunneth cross-product/cap inverse and fundamental-group inverse preserve every formula.')]
events=[]
for j,(sid,tag,line,description) in enumerate(spec,2):
 events.append(dict(statement_id=sid,date=stamp[:10],who=who,type='used and rechecked in this run',
  outcome=description+' Exposed source-local publication recheck only; no independent derivation, historical program output, new required-check closure or global/render/placement credit.',
  event_id='publish:c8:III:'+tag+':conifold-publication-recheck',phase='continuation8-later-publication',
  source_file=str(SOURCE.relative_to(ROOT)),source_row=str(line),source_event_type='used and rechecked in this run',
  evidence_group='publish:c8:III:later-unit-editing',publish_input_file=str(events_path.relative_to(ROOT)),
  publish_input_row=str(j),date_utc=stamp,where=str(review.relative_to(ROOT))))
write_tsv(events_path,fields,events)
files=[SOURCE,review,OUT/'S6_SERIES_PUBLISH_III_conifold_actual_units.md',p,events_path,
 OUT/'S6_SERIES_PUBLISH_III_conifold_publication_v001.diff',OUT/'S6_SERIES_PUBLISH_III_conifold_publication_v002.diff']
for stem in ['compare','edit','maps']:
 for ext in ['py','out','err']:
  files.append(ROOT/'code'/('S6_SERIES_PUBLISH_c8_later_conifold_'+stem+'.'+ext))
manifest=OUT/'S6_SERIES_PUBLISH_III_conifold_publication_packet.json'
manifest.write_text(json.dumps(dict(frozen_utc=stamp,reviewer=who,new_identities=[],
 scope='Complete exposed source-local proof review; no changed theorem conclusion; root owns final admission and global gates.',
 records=[meta(f) for f in files]),indent=2)+'\n')
print('FROZEN_UTC',stamp)
for f in files+[manifest]:print(json.dumps(meta(f),sort_keys=True))
print('DEFECTS',len(rows),'EVENTS',len(events),'NEW_IDENTITIES',0)
print('NO_CANONICAL_OR_SHARED_LEDGER_WRITES; NO_INDEPENDENT_OR_GLOBAL_CREDIT')
