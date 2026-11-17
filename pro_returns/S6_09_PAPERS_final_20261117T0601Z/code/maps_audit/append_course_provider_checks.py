"""Append full provider proof reads supplied as JSON on stdin; preserve history."""
from pathlib import Path
import csv,hashlib,json,re,shutil,sys
ROOT=Path(__file__).resolve().parents[3]
SRC=ROOT/'sources/codex_workspace/courses/CG-S6/src'
OUT=ROOT/'deliverables/work/maps_audit'
META=dict(reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)',effort='Pro',date='2026-11-17')
rows=json.load(sys.stdin)
path=OUT/'course_geometric_provider_full_checks.json';events=json.loads(path.read_text())
known={e['event_id'] for e in events};added=[]
for r in rows:
 p=SRC/r.pop('name'); ls=p.read_text().splitlines(); key=r.pop('key')
 raw=r.pop('raw_producer_header',ls[2]);m=re.search(r'(?:\d{1,2}(?:[–-]\d{1,2})? )?October 2026',raw)
 producer=r.pop('producer','GPT-6 Astra (OpenAI)')
 producer_effort=r.pop('producer_effort','Ultra')
 producer_date=r.pop('producer_date',m.group(0) if m else 'date not recorded')
 numerical=r.pop('numerical_program_rerun','not yet rerun by this event')
 e=dict(event_id=f'new-course-provider-{key}-full-20261117',source=str(p.relative_to(ROOT)),source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),locator=f'{p.relative_to(ROOT)}:1–{len(ls)}',line_count=len(ls),raw_producer_header=raw,producer=producer,producer_effort=producer_effort,producer_date=producer_date,full_proof_read=True,numerical_program_rerun=numerical,**r,**META)
 if e['event_id'] not in known:events.append(e);added.append(e)
path.write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n')
h=OUT/'check_events.json';hist=json.loads(h.read_text());known={e.get('event_id') for e in hist};hist.extend(e for e in added if e['event_id'] not in known);h.write_text(json.dumps(hist,ensure_ascii=False,indent=2)+'\n')
proofdir=OUT/'checked_course_providers';proofdir.mkdir(exist_ok=True)
manifest=[]
for e in events:
 src=ROOT/e['source'];out=proofdir/src.name;shutil.copyfile(src,out)
 manifest.append(dict(source=e['source'],source_sha256=e['source_sha256'],retained_complete_proof=str(out.relative_to(ROOT)),retained_sha256=hashlib.sha256(out.read_bytes()).hexdigest(),checked_event=e['event_id'],full_receiving_proof_read=True,dependency_closure='See the exact remaining imported dependencies in the full-check event',producer=e['producer'],producer_effort=e['producer_effort'],producer_date=e['producer_date'],raw_producer_header=e['raw_producer_header'],**META))
(OUT/'course_geometric_retained_proofs_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
# This source-level DAG inventories operative links; a full receiving read does not
# erase an unchecked target edge. Navigation/forward links are marked for review.
checked={Path(e['source']).name:e['event_id'] for e in events}
graph=[]
for p in sorted(SRC.glob('*.md')):
 text=p.read_text();lines=text.splitlines();edges=[]
 for n,line in enumerate(lines,1):
  for m in re.finditer(r'\]\(([^)#\s]+\.md)(?:#([^)]*))?\)',line):
   target=m.group(1)
   if '://' not in target:edges.append(dict(target=target,anchor=m.group(2) or '',source_line=n,kind='source link; operative versus forward use must be assessed in the check event'))
 graph.append(dict(source=str(p.relative_to(ROOT)),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),line_count=len(lines),full_provider_event=checked.get(p.name),links=edges))
(OUT/'course_source_dependency_graph.json').write_text(json.dumps(graph,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'new_full_proof_events':len(added),'total_geometric_provider_reads':len(events),'source_graph_nodes':len(graph)}))
