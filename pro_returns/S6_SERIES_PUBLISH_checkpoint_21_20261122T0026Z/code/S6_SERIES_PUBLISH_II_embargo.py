#!/usr/bin/env python3
"""Freeze a checker-authored derivation before releasing the exact target proof.

No automatic assertion about correctness or check-event eligibility is made.
The command records explicit checker attestation and immutable byte bindings.
"""
from pathlib import Path
import argparse,datetime,hashlib,json,shutil
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'agents/ii_infra'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,d):
 p.parent.mkdir(parents=True,exist_ok=True);assert not p.exists();p.write_text(json.dumps(d,indent=2)+'\n')
def current_packet_row(index,tag):
 row=dict(next(x for x in index['candidates'] if x['tag']==tag))
 manual=OUT/'S6_SERIES_PUBLISH_II_manual_statement_packets_receipt.json'
 if row['packet_readiness']!='statement_inputs_ready' and manual.exists():
  binding=next((x for x in json.loads(manual.read_text())['packets'] if x['tag']==tag),None)
  if binding:
   assert binding['label']==row['current_statement_owner']
   assert binding['target_argument_sentences_excluded'] and binding['construction_and_conclusions_manually_compared']
   assert sha(ROOT/binding['packet_path'])==binding['packet_sha256']
   row['packet_path']=binding['packet_path'];row['packet_sha256']=binding['packet_sha256'];row['packet_readiness']='statement_inputs_ready'
   row['manual_statement_receipt']={'path':str(manual.relative_to(ROOT)),'sha256':sha(manual)}
 return row
def main():
 ap=argparse.ArgumentParser();sub=ap.add_subparsers(dest='command',required=True)
 f=sub.add_parser('freeze');f.add_argument('--tag',required=True);f.add_argument('--checker',required=True);f.add_argument('--derivation',type=Path,required=True)
 f.add_argument('--attest-derived-before-target-proof',action='store_true',required=True)
 r=sub.add_parser('release');r.add_argument('--freeze-receipt',type=Path,required=True)
 ns=ap.parse_args()
 index_path=OUT/'S6_SERIES_PUBLISH_II_packet_index.json';index=json.loads(index_path.read_text())
 if ns.command=='freeze':
  row=current_packet_row(index,ns.tag)
  assert row['packet_readiness']=='statement_inputs_ready','This target awaits a root-bound safe statement/argument split.'
  derivation=ns.derivation.resolve();assert derivation.is_file() and derivation.stat().st_size>0
  assert not derivation.is_relative_to(OUT/'embargoed_proofs_v2')
  text=derivation.read_text();assert row['current_statement_owner'] in text,'Derivation must identify its exact statement owner.'
  assert len(text.split())>=40,'Freeze a substantive derivation, not an empty/template file.'
  target=ROOT/row['target_proof_path'];packet=ROOT/row['packet_path']
  assert sha(target)==row['target_proof_sha256'] and sha(packet)==row['packet_sha256']
  now=datetime.datetime.now(datetime.timezone.utc);stamp=now.strftime('%Y%m%dT%H%M%S%fZ')
  folder=OUT/'derivation_freezes'/ns.tag/stamp;folder.mkdir(parents=True,exist_ok=False)
  archive=folder/'S6_SERIES_PUBLISH_derivation_frozen.md';shutil.copyfile(derivation,archive)
  receipt={'created_utc':now.isoformat(),'tag':ns.tag,'statement_owner':row['current_statement_owner'],'checker':ns.checker,
   'source_sha256':index['source_sha256'],'packet_path':row['packet_path'],'packet_sha256':row['packet_sha256'],
   'target_proof_path':row['target_proof_path'],'target_proof_sha256':row['target_proof_sha256'],
   'input_derivation_path':str(derivation),'frozen_derivation_path':str(archive.relative_to(ROOT)),
   'derivation_sha256':sha(archive),'checker_attestation':'I wrote this derivation from the statement and cited inputs before reading the target printed proof.',
   'attestation_source':'explicit --attest-derived-before-target-proof flag supplied by the named checker',
   'proof_released':False,'correctness_certified':False,'check_events_added':0,'packet_index_sha256':sha(index_path)}
  if row.get('manual_statement_receipt'):receipt['manual_statement_receipt']=row['manual_statement_receipt']
  supplements=OUT/'S6_SERIES_PUBLISH_II_input_supplement_index.json'
  if supplements.exists():
   supplement=next(x for x in json.loads(supplements.read_text())['supplements'] if x['tag']==ns.tag)
   receipt['cited_input_supplement']={'path':supplement['supplement_path'],'sha256':supplement['supplement_sha256'],'index_sha256':sha(supplements)}
  p=folder/'S6_SERIES_PUBLISH_derivation_freeze_receipt.json';write(p,receipt)
  print(json.dumps({'receipt':str(p.relative_to(ROOT)),'sha256':sha(p),'owner':receipt['statement_owner'],'events_added':0}))
 else:
  p=ns.freeze_receipt.resolve();rec=json.loads(p.read_text());row=current_packet_row(index,rec['tag'])
  assert rec['statement_owner']==row['current_statement_owner']
  assert sha(ROOT/rec['frozen_derivation_path'])==rec['derivation_sha256']
  assert sha(ROOT/rec['target_proof_path'])==rec['target_proof_sha256']==row['target_proof_sha256']
  folder=OUT/'released_proofs'/rec['tag']/sha(p)[:16];folder.mkdir(parents=True,exist_ok=False)
  dest=folder/'S6_SERIES_PUBLISH_target_proofs.tex';shutil.copyfile(ROOT/rec['target_proof_path'],dest)
  source=OUT/'S6_SERIES_PUBLISH_II_original_source_embargoed.tex';assert sha(source)==rec['source_sha256']
  s=source.read_text()
  # The full owning block includes the exact statement and intervening context.
  lines=s.splitlines(keepends=True);a=sum(len(x) for x in lines[:row['statement_start_line']-1]);b=(max(x['end'] for x in row['proofs']) if row['proofs'] else sum(len(x) for x in lines[:row['statement_end_line']]))
  full=folder/'S6_SERIES_PUBLISH_full_owning_block.tex';full.write_text(s[a:b])
  receipt={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'statement_owner':rec['statement_owner'],
   'checker':rec['checker'],'freeze_receipt':str(p.relative_to(ROOT)),'freeze_receipt_sha256':sha(p),
   'derivation_sha256':rec['derivation_sha256'],'released_proof_path':str(dest.relative_to(ROOT)),'released_proof_sha256':sha(dest),
   'full_owning_block_path':str(full.relative_to(ROOT)),'full_owning_block_sha256':sha(full),
   'release_only':True,'actual_comparison_completed':False,'correctness_certified':False,'check_events_added':0,
   'next_required_actions':['Actually read every target proof step and compare with the frozen derivation.','Recompute each computational step with new code and a different method/library where available.','Resolve every discrepancy; record exact hypotheses, scopes and conventions.','Prepare presentation guards with complete original/proposed blocks and actual comparative-rereading record; preserve formulas/references or prove an exact justified map.','Only actual completed work can support one event per printed statement owner; parent integrates events.']}
  out=folder/'S6_SERIES_PUBLISH_release_receipt.json';write(out,receipt)
  print(json.dumps({'receipt':str(out.relative_to(ROOT)),'sha256':sha(out),'proof':str(dest.relative_to(ROOT)),'full_block':str(full.relative_to(ROOT)),'events_added':0}))
if __name__=='__main__':main()
