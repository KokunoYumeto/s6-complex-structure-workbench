#!/usr/bin/env python3
"""Receive cp36's exact remaining boundary, preserving the prior reduction.

New source proof claims stay explicitly under continuation review; this
metadata/scope patch never promotes them to receiving proved status.
"""
from pathlib import Path
from datetime import datetime,timezone
import csv,json,hashlib
csv.field_size_limit(16 * 1024 * 1024)
P=Path(__file__).resolve().parents[2];W=P.parents[1];N=W/'night36/S6_06_BLIND';A=P/'analysis/continuation_IV'
source=next(r for r in csv.DictReader((N/'S6_06_BLIND_results.csv').open()) if r['id']=='P3K.75')
mark='% continuation: cp36 K75 boundary'
new=r'''The checkpoint36 source reports the additional completed sectors in
\cref{night:P3K.109,night:P3K.110,night:P3K.111,night:P3K.112,
night:P3K.113,night:P3K.114,night:P3K.115,night:P3K.116,
night:P3K.117,night:P3K.118,night:P3K.119}. Their complete supplied
arguments are retained below with their receiving check scopes.
The current receiving review of those arguments remains explicit in
each record; the source's proof status is preserved separately.

The latest source boundary consists of the remaining marked source-moduli
generators, including the OS45 \(I_9\), handle and infinity sectors,
additional ordinary clutch slots with nonzero total norm, and endpoint
loci outside the completed domains. Their full source, line, root,
annular and closing comparisons remain open. The continuation also
retains the pending whole-proof, new-computation and credit gates on
the newly received results. No numerical return is assigned to an
unfinished attachment.
% continuation: cp36 K75 boundary'''
changes=[]
for rel,needle in [
 ('papers/IV/body.tex','The remaining attachment problem is the selected-'),
 ('papers/IV/body_source.tex','The selected-I3 \\(M_2\\) return, its remaining cap/norm/fan')]:
 path=P/rel;s=path.read_text();i=s.index('\\label{night:P3K.75}');end=s.index('\\end{theorem}',i)
 before=s[i:end]
 if mark in before:continue
 a=s.index(needle,i);assert a<end
 after=s[i:a]+new+'\n\n';s=s[:i]+after+s[end:]
 # The existing receiving proof's final item repeated the old boundary.
 if rel.endswith('/body.tex'):
  old=r'''\item These constructions leave the selected-\(I_3\) return for
\(M_2\), its remaining cap, signed-norm and fan comparisons,
additional marked singular-site sectors, and the remaining
holomorphic endpoint scopes open. The required data are the actual
source and line arrows, their root and annular extensions, the full
endpoint words and the two separate integral characteristic
comparisons on those remaining attachments. The completed
\(M_2\) order-three proof includes its stated selected-\(I_3\)
coefficient and phase comparison; the compact return and remaining
attachment data just named are the residual problem.'''
  replacement=r'''\item The checkpoint36 intake places the eleven further source results
named above in this paper with their complete arguments and receiving
review records. Its exact source comparison finds the preceding
287 theorem/proof blocks unchanged and this reduction record enlarged.
The source's remaining mathematical boundary is the OS45 \(I_9\),
handle and infinity sectors, additional ordinary clutch slots with
nonzero total norm, and endpoint loci outside the completed domains.
The new receiving proof checks remain separately recorded, with no
promotion from source status alone.'''
  assert old in s;s=s.replace(old,replacement,1)
 path.write_text(s);changes.append(dict(file=rel,prior_statement_tail=before,new_statement_tail=after))

ip=P/'S6_10_PAPERS_inventory.csv'
with ip.open() as f:rd=csv.DictReader(f);fields=rd.fieldnames;rows=list(rd)
for row in rows:
 if row['label']!='night:P3K.75':continue
 notes=json.loads(row['notes'])
 if notes.get('night_checkpoint')!='36':
  notes.setdefault('continuation_prior_source_rows',[]).append({k:notes.get(k) for k in ['night_checkpoint','source_file','source_statement','source_status','where_proved','current_source_proof_block']})
 notes.update(night_checkpoint='36',source_file='night36/S6_06_BLIND/S6_06_BLIND_results.csv',source_statement=source['statement'],source_status=source['status'],source_notes=source['notes'],where_proved=source['where_proved'],continuation_cp36_delta='Only earlier source theorem/proof block changed; strongest source reduction enlarged by K109–119. Current receiving verification remains explicit and pending where not recorded.',continuation_remaining_source_boundary='OS45 I9, handle and infinity sectors; extra ordinary clutch slots with nonzero total norm; endpoint loci outside completed domains.',continuation_changed_source_review_pending=True)
 exact=next(x for x in json.loads((A/'cp36_exact_block_comparison.json').read_text())['changed'] if x['label']=='night:P3K.75')
 full=N/exact['file'];inputs=[dict(file=exact['file'],sha256=hashlib.sha256(full.read_bytes()).hexdigest())]
 notes['current_source_proof_block']=dict(file='night36/S6_06_BLIND/'+exact['file'],start=exact['new_start'],end=exact['new_end'],sha256=exact['new_sha256'],source_status='Unresolved; exact remaining obligations',proof_input_files=inputs,included_proof_manifest_sha256=hashlib.sha256(json.dumps(inputs,sort_keys=True,separators=(',',':')).encode()).hexdigest(),unresolved_literal_inputs=[])
 if notes.get('continuation_prior_source_rows'):
  history_path=A/'K75_prior_source_rows.json'
  previous=json.loads(history_path.read_text()) if history_path.exists() else []
  for prior in notes.pop('continuation_prior_source_rows'):
   if prior not in previous:previous.append(prior)
  history_path.write_text(json.dumps(previous,ensure_ascii=False,indent=2)+'\n')
  notes['continuation_source_history_receipt']=dict(file=str(history_path.relative_to(P)),sha256=hashlib.sha256(history_path.read_bytes()).hexdigest(),scope='Exact prior source fields preserved outside the inventory cell to avoid duplicating long source statements.')
 row['notes']=json.dumps(notes,ensure_ascii=False);row['status']='open'
 current=[x.strip() for x in row['uses'].split(';') if x.strip()]
 for sid in range(109,120):
  lab='night:P3K.'+str(sid)
  if lab not in current:current.append(lab)
 row['uses']='; '.join(current)
with ip.open('w',newline='') as f:wr=csv.DictWriter(f,fields);wr.writeheader();wr.writerows(rows)
if changes:
 (A/'K75_cp36_boundary_receipt.json').write_text(json.dumps(dict(recorded_at=datetime.now(timezone.utc).isoformat(),source_row=source,changes=changes,proof_checks_awarded=0),ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'changed_files':len(changes),'source_status':source['status'],'receiving_status':'open','proof_checks_awarded':0},indent=2))
