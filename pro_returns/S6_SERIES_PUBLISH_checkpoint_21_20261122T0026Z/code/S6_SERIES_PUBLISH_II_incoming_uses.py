#!/usr/bin/env python3
"""Extract coded receiving-use metadata and statements, never receiver proofs."""
from pathlib import Path
import argparse,datetime,hashlib,importlib.util,json,re
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('packet',ROOT/'code/S6_SERIES_PUBLISH_II_packets.py');base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--label',required=True);ap.add_argument('--output-prefix',type=Path,required=True);ns=ap.parse_args()
 prefix=ns.output_prefix.resolve();assert prefix.is_relative_to(ROOT/'agents');prefix.parent.mkdir(parents=True,exist_ok=True)
 held={'cdp:st:D.1.5','cdp:st:D.1.6','inv:wb:uniform-nontorsion-provenance'};uses=[];sources={}
 for paper in ['I','II','III','IV','V']:
  src=base.parse_source(ROOT/f'S6_SERIES_PUBLISH_{paper}.tex',paper);s=src['text'];masked=src['masked'];sources[paper]={'path':src['path'],'sha256':src['sha256']}
  occurrences=[]
  for m in base.REF.finditer(masked):
   if ns.label in [x.strip() for x in m[1].split(',')]:occurrences.append((m.start(),m.end(),'local',None))
  for name,count in [('SeriesRef',1),('CompendiumRef',2)]:
   for m in re.finditer(r'\\'+name+r'\s*(?=\{)',masked):
    vs,end=base.read_args(s,m.end(),count)
    if vs[-1]==ns.label:occurrences.append((m.start(),end,name,vs[0] if count==2 else None))
  records=[]
  for m in re.finditer(r'\\StatementRecord\s*(?=\{)',masked[masked.index(r'\begin{document}'):]):
   offset=masked.index(r'\begin{document}');_,end=base.read_args(s,m.end()+offset,4);records.append((m.start()+offset,end))
  for pos,end,kind,edition in sorted(occurrences):
   proof=next((p for p in src['proofs'] if p['start']<=pos<p['end']),None)
   statement=next((x for x in src['statements'] if x['start']<=pos<x['end']),None)
   owner=proof['owner'] if proof else statement['owner'] if statement else None
   row=src['statement_labels'].get(owner) if owner else None
   metadata=any(a<=pos<b for a,b in records)
   heading=max((h for h in src['headings'] if h['start']<pos),key=lambda x:x['start'],default=None)
   item={'paper':paper,'source_sha256':src['sha256'],'source_line':s.count('\n',0,pos)+1,
         'literal_reference':s[pos:end],'reference_kind':kind,'compendium_paper':edition,
         'receiving_owner':owner,'inside_proof':bool(proof),'inside_statement':bool(statement),
         'record_metadata_only':metadata,'nearest_heading':heading}
   if row and owner not in held:
    text=base.safe_statement(s[row['start']:row['end']]);dest=Path(str(prefix)+f'_receiver_{len(uses)+1:03d}_statement.tex');assert not dest.exists();dest.write_text(text+'\n')
    item.update({'receiver_statement_path':str(dest.relative_to(ROOT)),'receiver_statement_sha256':sha(dest),'receiver_title':row['title'],'receiver_statement_start_line':row['start_line'],'receiver_statement_end_line':row['end_line']})
   elif row:item['receiver_statement_status']='held_embedded_argument_block; use root manual statement packet or request root disposition'
   uses.append(item)
 result={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'target_label':ns.label,'sources':sources,'uses':uses,
         'actual_body_or_front_references':sum(not x['record_metadata_only'] for x in uses),'record_metadata_references':sum(x['record_metadata_only'] for x in uses),
         'scope':'All coded ref-family, SeriesRef and CompendiumRef occurrences in the five current sources. Receiving proof prose is not displayed or extracted. Historical compendium references are explicitly identified. This does not claim coverage of uncited prose allusions.',
         'events_added':0}
 p=Path(str(prefix)+'.json');assert not p.exists();p.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'path':str(p.relative_to(ROOT)),'sha256':sha(p),'uses':len(uses),'actual_body_or_front_references':result['actual_body_or_front_references'],'owners':sorted({x['receiving_owner'] for x in uses if x['receiving_owner']})},indent=2))
if __name__=='__main__':main()
