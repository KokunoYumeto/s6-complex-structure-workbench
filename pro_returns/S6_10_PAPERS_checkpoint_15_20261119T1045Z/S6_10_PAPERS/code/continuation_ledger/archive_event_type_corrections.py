#!/usr/bin/env python3
"""Preserve exact old events before applying owner-issued type supersession.

Run before reconcile.py while the former event is still in the provenance
ledger. Re-runs use the preserved record. No source event is fabricated.
"""
from pathlib import Path
import hashlib,json

P=Path(__file__).resolve().parents[2]
A=P/'analysis/continuation_ledger'
prior=[json.loads(line) for line in (A/'event_provenance.jsonl').open()]
archive_path=A/'superseded_event_records.json'
archive=json.loads(archive_path.read_text()) if archive_path.exists() else []
prefix_path=A/'prefixes_before_step_type_correction.json'
prefixes={r['label']:r for r in json.loads(prefix_path.read_text())} if prefix_path.exists() else {}
current_prefixes={r['label']:r for r in json.loads((A/'printed_typed_check_prefixes.json').read_text())}
new=[]
for source in sorted((P/'analysis').glob('continuation_*/crossreview_event_type_correction.json')):
 rel=str(source.relative_to(P));raw=source.read_bytes();data=json.loads(raw)
 for index,change in enumerate(data['changes'],1):
  key=rel+':'+str(index)
  if any(x['correction_key']==key for x in archive):continue
  matches=[e for e in prior if e['statement_id']==change['statement_id'] and e['type']==change['old_type'] and e['outcome']==change['outcome']]
  if len(matches)!=1:raise ValueError('Exact prior event unavailable or ambiguous: '+key)
  archive.append({'correction_key':key,'correction_source':rel,'correction_sha256':hashlib.sha256(raw).hexdigest(),
                  'original_source_sha256':data['old_file_sha256'],'new_source_sha256_at_correction':data['new_file_sha256'],
                  'reason':data['reason'],'new_type':change['new_type'],'superseded_canonical_event':matches[0]})
  label=change['statement_id'];prefixes.setdefault(label,current_prefixes[label]);new.append(label)
archive_path.write_text(json.dumps(archive,ensure_ascii=False,indent=2)+'\n')
prefix_path.write_text(json.dumps(list(prefixes.values()),ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'archived_superseded_events':len(archive),'new_labels':new},indent=2))
