#!/usr/bin/env python3
"""Add SeriesRef/CompendiumRef cited inputs without changing frozen packets."""
from pathlib import Path
import collections,datetime,hashlib,importlib.util,json,os,re
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'agents/ii_infra';DEST=OUT/'statement_supplements_v1'
spec=importlib.util.spec_from_file_location('packet',ROOT/'code/S6_SERIES_PUBLISH_II_packets.py');base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
base.relative=lambda p:os.path.relpath(p,ROOT)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def references(text,context):
 masked=base.mask_comments(text);result=[]
 for m in base.REF.finditer(masked):
  for label in m[1].split(','):result.append(('local',context,label.strip()))
 for m in re.finditer(r'\\SeriesRef\s*(?=\{)',masked):
  vs,_=base.read_args(text,m.end(),1);result.append(('series',None,vs[0]))
 for m in re.finditer(r'\\CompendiumRef\s*(?=\{)',masked):
  vs,_=base.read_args(text,m.end(),2);result.append(('compendium','comp:'+vs[0],vs[1]))
 return result
sources={}
for paper in ['I','II','III','IV','V']:
 p=(OUT/'S6_SERIES_PUBLISH_II_original_source_embargoed.tex') if paper=='II' else ROOT/f'S6_SERIES_PUBLISH_{paper}.tex'
 sources['series:'+paper]=base.parse_source(p,paper)
for paper in ['I','II','III']:
 p=ROOT.parent/'S6_SERIES_PUBLISH_work/S6_GRIND_4_s6_09_compendium'/f'S6_09_PAPERS_{paper}.tex'
 sources['comp:'+paper]=base.parse_source(p,paper)
index_path=OUT/'S6_SERIES_PUBLISH_II_packet_index.json';index=json.loads(index_path.read_text())
required={x['current_statement_owner'] for x in index['candidates']};held={x['current_statement_owner'] for x in index['candidates'] if x['packet_readiness']!='statement_inputs_ready'}
DEST.mkdir(exist_ok=False);receipts=[]
for row in index['candidates']:
 src=sources['series:II'];owner=src['statement_labels'][row['current_statement_owner']]
 target=src['text'][owner['start']:owner['end']]+'\n'+'\n'.join(src['text'][p['start']:p['end']] for p in owner['proofs'])
 queue=references(target,'series:II');seen=set();texts=[];entries=[];known_hashes={x.get('sha256') for x in row['referenced_inputs']}
 while queue:
  kind,context,label=queue.pop(0);key=(kind,context,label)
  if key in seen:continue
  seen.add(key)
  if kind=='compendium':order=[context] if context in sources else []
  elif kind=='series':order=[k for k in sources if k.startswith('series:')]
  else:
   family=context.split(':')[0]
   order=[context]+[k for k in sources if k.startswith(family+':') and k!=context]
  selected=next((k for k in order if label in sources[k]['labels'] or label in sources[k]['statement_labels']),None)
  if selected is None:
   entries.append({'reference_kind':kind,'scope':context,'label':label,'status':'unresolved_reference'});continue
  meta,segment=base.input_for_label(label,{selected:sources[selected]},owner,required,held)
  meta.update({'reference_kind':kind,'resolved_source_edition':selected,'requested_scope':context})
  if segment:
   queue.extend(references(segment,selected))
   if meta.get('sha256') in known_hashes:meta['supplement_disposition']='already_bound_in_original_packet'
   else:
    texts.append((selected,label,segment));known_hashes.add(meta.get('sha256'));meta['supplement_disposition']='included_exact_input'
  entries.append(meta)
 text='% Immutable cited-input supplement. Target proofs remain embargoed.\n'
 text+=f'% Target: {row["current_statement_owner"]}; tag {row["tag"]}.\n% Frozen source SHA256 {index["source_sha256"]}.\n'
 text+='% CompendiumRef is resolved against the cited S6_09 source edition, not silently identified with the current series statement.\n\n'
 for edition,label,segment in texts:text+=f'% Exact cited input: {edition} / {label}\n'+segment+'\n\n'
 assert not re.search(r'\\begin\{proof\*?\}',base.mask_comments(text))
 p=DEST/f'S6_SERIES_PUBLISH_II_{row["tag"]}_cited_input_supplement.tex';p.write_text(text)
 record={'tag':row['tag'],'statement_owner':row['current_statement_owner'],'source_sha256':index['source_sha256'],
         'original_packet':row['packet_path'],'original_packet_sha256':row['packet_sha256'],
         'supplement_path':base.relative(p),'supplement_sha256':sha(p),'added_input_blocks':len(texts),'dependencies':entries,
         'target_proof_read':False,'events_added':0}
 q=DEST/f'S6_SERIES_PUBLISH_II_{row["tag"]}_supplement_metadata.json';q.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
 receipts.append(record)
result={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':index['source_sha256'],
        'original_packet_index_path':base.relative(index_path),'original_packet_index_sha256':sha(index_path),
        'scope':'Supplementary dependency closure for ref-family commands, SeriesRef one-argument labels, and CompendiumRef paper/label pairs. Original packet files remain byte-identical. Cited compendium edition is explicit. No required-target proof-internal formula is released.',
        'source_editions':{k:{'path':v['path'],'sha256':v['sha256']} for k,v in sources.items()},
        'targets':len(receipts),'added_input_blocks':sum(x['added_input_blocks'] for x in receipts),
        'dependency_status_counts':dict(collections.Counter(d['status'] for x in receipts for d in x['dependencies'])),
        'supplements':receipts,'target_proofs_displayed':False,'events_added':0}
p=OUT/'S6_SERIES_PUBLISH_II_input_supplement_index.json';assert not p.exists();p.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['supplements','source_editions']},indent=2));print('index_sha256',sha(p))
