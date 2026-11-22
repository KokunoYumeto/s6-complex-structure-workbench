from pathlib import Path
import re,json,datetime,hashlib
from S6_SERIES_PUBLISH_editing import Editor
r=Path(__file__).resolve().parents[1];ed=Editor('I');tag_rows=[]
for m in list(re.finditer(r'\\begin\{(theorem|proposition|lemma|corollary|definition|remark|cited|computed)\}(?:\[[^\]]*\])?',ed.text)):
 en=ed.text.index('\\end{'+m[1]+'}',m.end());b=ed.text[m.start():en]
 tag=re.search(r'\\hypertarget\{tag-([^}]+)\}',b)
 lab=re.search(r'\\label\{([^}]+)\}',b)
 if tag and lab and '\\StatementRecord' not in b:
  anchor=lab.group(0)
  new=b.replace(anchor,anchor+'\n'+r'\StatementRecord{'+lab[1]+r'}{proved}{'+tag[1]+r'}{}',1)
  ed.replace(b,new,'D10','Print the permanent tag after the mathematical heading; retain every existing anchor and show no machine metadata.',lab[1])
  tag_rows.append({'statement_id':lab[1],'tag':tag[1]})
start=ed.text.index(r'\subsection{The Albanese coordinates and real structures}')
end=ed.text.index(r'\subsection{CM and torsion}',start)
span=ed.text[start:end]
assert 'ari:C.2.1' in span and 'ari:C.2.2' in span
ed.replace(span,'','D23','Place both Albanese/real-form results directly after the full real-structure construction.', 'ari:C.2.1')
anchor=r'\section{The uniform corner obstruction}'
ed.replace(anchor,span+anchor,'D23','Keep the exact Albanese and real-form application with the preceding real-structure proofs.', 'ari:C.2.2')
ed.save()
(r/'records/S6_SERIES_PUBLISH_I_tag_placement_receipt.json').write_text(json.dumps({
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'printed_tag_records':tag_rows,
 'movement':'Complete two-result Albanese/real-form subsection moved unchanged after the real-structure section.',
 'scope':'Typesetting and whole-span relocation only; no mathematical check credit.',
 'source_sha256':hashlib.sha256(ed.text.encode()).hexdigest()},indent=2)+'\n')
