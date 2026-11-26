"""Admit four complete cyclic/elliptic/K3 model units in dependency order."""
from S6_SERIES_PUBLISH_c3_edit import *

folder=ROOT/'agents/continuation3_conductor';prefix='S6_SERIES_PUBLISH_c3_conductor_11_'
before=SOURCE.read_text();after=before
old=(folder/(prefix+'input.tex')).read_text();new=(folder/(prefix+'replacement.tex')).read_text()
assert after.count(old)==1
after=after.replace(old,new,1)
_,remote=read_tsv(folder/(prefix+'remote_repairs.tsv'));assert len(remote)==1
for row in remote:
 assert after.count(row['old_text'])==1,row['statement_id']
 after=after.replace(row['old_text'],row['new_text'],1)
preserve_identifiers(before,after)
for oldids,newids in zip(identifiers(before),identifiers(after)):
 for name,count in oldids.items():assert newids[name]==count,name
 for name,count in (newids-oldids).items():assert newids[name]==1,name
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
 _,rows=read_tsv(folder/(prefix+suffix));print(suffix,append_rows(ROOT/target,rows,key))

path=ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv';fields,rows=read_tsv(path)
oldunits={'subsec:II:cyclic-component-models','cdp:st:C.2.UN.32'}
assert len([r for r in rows if r['paper']=='II' and r['unit_id'] in oldunits])==52
rows=[r for r in rows if not(r['paper']=='II' and r['unit_id'] in oldunits)]
_,incoming=read_tsv(folder/(prefix+'unit_status.tsv'));assert len(incoming)==104
seen={(r['paper'],r['unit_id'],r['defect_type'] or r['row_kind']) for r in rows}
for item in incoming:
 kind=item['criterion'];assert ('II',item['unit'],kind) not in seen
 seen.add(('II',item['unit'],kind))
 status='open' if kind in ['D14','D18','D23','structure'] else item['status']
 rows.append(dict(paper='II',unit_id=item['unit'],unit_title=item['title'],row_kind='structure' if kind=='structure' else 'defect',defect_type='' if kind=='structure' else kind,status=status,date_utc=now(),evidence=str((folder/(prefix+'comparison.md')).relative_to(ROOT)),detail=item['reason']+' Complete exposed old/receiving comparisons by conductor; root read all 1001 receiving lines. Replacement of subsection boundaries supplies no movement credit.'))
write_tsv(path,fields,rows)
_,sources=read_tsv(folder/(prefix+'sources.tsv'));mapped=[]
for r in sources:
 mapped.append(dict(source=r['source_id'],url=r['url'],version=r['version'],locus=r['exact_locus'],date_utc=r['date_utc'],sha256=r['sha256'],own_word_summary=r['own_paraphrase'],use=r['reader']+'. '+r['bytes']+' bytes where a downloaded PDF exists. '+r['storage']))
print('Primary readings',append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',mapped,'source'))
add_event('lem:II:local-cyclic-elliptic; lem:II:elliptic-minimal-descent; lem:II:elliptic-canonical-character; cdp:st:C.2.UN.33; cdp:st:C.2.UN.24; cdp:st:C.2.UN.32; cdp:st:C.2.UN.31',
 'II-C3-ROOT-CYCLIC-MODELS-ADMISSION','used and rechecked in this run',
 'The conductor reviewer read every full original and receiving proof, and root read all 1001 receiving lines plus the complete map comparison and exact remote move. The shared local quotient proves both averaging coordinate changes, the finite translation kernel quotient, full root coordinate, fixed-point-adjusted lift and m|s plus gcd(m,s)=1. The root-coordinate permutation proves the sole equation alias. P318 gives the same positive canonical-intersection and connected-fibre descent maps, including relative-minimality implying absolute minimality; P319 gives the exact canonical character and graph pullback. Root compared all eleven elliptic configurations, the K3 rank-one/rank-two and all-algebraic-dimensions cases, Chern cocycle, Dolbeault/translation lattice, quotient fixed points, isotropic pencil, compact occurrence and full Enriques bielliptic construction. All original formula identities survive; full K3 precedes UN31. Program157 is already admitted; no program execution, independent derivation, unit-migration movement or final-page credit is claimed. D14/D18/D23/structure remain whole-paper gates.',
 'S6_SERIES_PUBLISH_II.tex: four cyclic elliptic/K3 component model subsections',source=__file__)
print('Four receiving units admitted with shared owners P317-P319; original statements and full constructions preserved.')
