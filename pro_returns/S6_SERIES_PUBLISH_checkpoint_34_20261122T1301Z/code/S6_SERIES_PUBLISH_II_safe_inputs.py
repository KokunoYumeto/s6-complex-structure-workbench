#!/usr/bin/env python3
"""Export requested exact statement/formula inputs while holding target proofs."""
from pathlib import Path
import argparse,datetime,hashlib,importlib.util,json,os
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'agents/ii_infra'
spec=importlib.util.spec_from_file_location('packet',ROOT/'code/S6_SERIES_PUBLISH_II_packets.py');base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
base.relative=lambda p:os.path.relpath(p,ROOT)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--label',action='append',required=True);ap.add_argument('--paper',default='II');ap.add_argument('--edition',choices=['series','compendium'],default='series');ap.add_argument('--output-prefix',type=Path,required=True);ns=ap.parse_args()
 prefix=ns.output_prefix.resolve();assert prefix.is_relative_to(ROOT/'agents');prefix.parent.mkdir(parents=True,exist_ok=True)
 if ns.edition=='compendium':p=ROOT.parent/'S6_SERIES_PUBLISH_work/S6_GRIND_4_s6_09_compendium'/f'S6_09_PAPERS_{ns.paper}.tex'
 elif ns.paper=='II':p=OUT/'S6_SERIES_PUBLISH_II_original_source_embargoed.tex'
 else:p=ROOT/f'S6_SERIES_PUBLISH_{ns.paper}.tex'
 src=base.parse_source(p,ns.paper);index=json.loads((OUT/'S6_SERIES_PUBLISH_II_packet_index.json').read_text());required={x['current_statement_owner'] for x in index['candidates']};held={x['current_statement_owner'] for x in index['candidates'] if x['packet_readiness']!='statement_inputs_ready'}
 text='% Exact safe statement/formula inputs; target proof prose remains embargoed.\n';entries=[]
 for label in ns.label:
  meta,segment=base.input_for_label(label,{'requested':src},{'owner':'__input_request__'},required,held);meta['edition']=ns.edition;entries.append(meta)
  if segment:text+=f'% Input {label}; {ns.edition} Paper {ns.paper}; source SHA256 {src["sha256"]}.\n'+segment+'\n\n'
  else:text+=f'% Input {label} is held or unresolved; see bound metadata.\n'
 t=Path(str(prefix)+'.tex');assert not t.exists();t.write_text(text)
 rec={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_path':src['path'],'source_sha256':src['sha256'],'entries':entries,'packet_path':str(t.relative_to(ROOT)),'packet_sha256':sha(t),'target_proofs_displayed':False,'events_added':0}
 p=Path(str(prefix)+'.json');assert not p.exists();p.write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'receipt':str(p.relative_to(ROOT)),'receipt_sha256':sha(p),'packet':str(t.relative_to(ROOT)),'packet_sha256':sha(t),'entries':[{k:e.get(k) for k in ['label','status','owner']} for e in entries]},indent=2))
if __name__=='__main__':main()
