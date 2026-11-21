#!/usr/bin/env python3
"""Integrate the exact, individually reviewed editorial edits."""
from pathlib import Path
import csv,json
from S6_SERIES_PUBLISH_editing import Editor,ROOT
p=ROOT/'agents/provenance';e=Editor('V')
old=(p/'S6_SERIES_PUBLISH_V_shifted_original.tex').read_text()
new=(p/'S6_SERIES_PUBLISH_V_shifted_revised.tex').read_text()
if old in e.text:
 e.replace(old,new,'D14','Integrate individually reviewed shifted-product definitions and prose, preserving original mathematical displays and anchors.','sec:shifted')
 for r in csv.DictReader((p/'S6_SERIES_PUBLISH_V_shifted_edits.tsv').open(),delimiter='\t'):
  e.record(r['type'],r['old_text'],r['new_text'],r['reason'],r['location'])
conflicts=[]
files=['S6_SERIES_PUBLISH_V_classification_replacements.json','S6_SERIES_PUBLISH_V_classification_orphan_followup.json']
for name in files:
 for i,r in enumerate(json.loads((p/name).read_text())):
  count=e.text.count(r['old_text'])
  if r['new_text'] and r['new_text'] in e.text:pass
  elif count==1:e.replace(r['old_text'],r['new_text'],r['type'],r['reason'],r['location'])
  elif count==0 and not r['new_text']:pass
  else:conflicts.append({'file':name,'index':i,'count':count,**r})
e.save()
(ROOT/'records/S6_SERIES_PUBLISH_V_classification_edit_conflicts.json').write_text(json.dumps(conflicts,indent=2)+'\n')
print('Unapplied conflicts:',len(conflicts))
for r in conflicts:print(r['file'],r['index'],r['location'],r['old_text'][:100])
