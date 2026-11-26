from pathlib import Path
import re,json,datetime,hashlib
from S6_SERIES_PUBLISH_editing import Editor
r=Path(__file__).resolve().parents[1];ed=Editor('I')
prior=json.loads((r/'records/S6_SERIES_PUBLISH_I_tag_placement_receipt.json').read_text())
for x in prior['printed_tag_records']:
 line=r'\StatementRecord{'+x['statement_id']+r'}{proved}{'+x['tag']+r'}{}'
 if line in ed.text:
  ed.replace(line,'','D25','Remove a misplaced tag record from the first automatic formatting pass; insertion offsets must be computed against an immutable source snapshot.',x['statement_id'])
snapshot=ed.text;guards=[]
for m in re.finditer(r'\\begin\{(theorem|proposition|lemma|corollary|definition|remark|cited|computed)\}(?:\[[^\]]*\])?',snapshot):
 en=snapshot.index('\\end{'+m[1]+'}',m.end());b=snapshot[m.start():en]
 tag=re.search(r'\\hypertarget\{tag-([^}]+)\}',b);lab=re.search(r'\\label\{([^}]+)\}',b)
 if tag and lab and '\\StatementRecord' not in b:
  anchor=lab.group(0);new=b.replace(anchor,anchor+'\n'+r'\StatementRecord{'+lab[1]+r'}{proved}{'+tag[1]+r'}{}',1)
  guards.append((b,new,lab[1],tag[1]))
for old,new,lab,tag in guards:
 ed.replace(old,new,'D10','Print the permanent tag after the mathematical heading, using immutable-source guarded spans.',lab)
ed.save()
(r/'records/S6_SERIES_PUBLISH_I_tag_placement_correction.json').write_text(json.dumps({
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'cause':'The first formatting loop read offsets from the old text while taking slices from the changing text. This misplaced some printable tag records, including an equation tag that caused an upshape-in-math-mode build error.',
 'correction':'Removed only lines listed by the first insertion receipt, preserving subsequent mathematical edits, then generated all guarded environment replacements from one immutable snapshot.',
 'supersedes':'S6_SERIES_PUBLISH_I_tag_placement_receipt.json tag placement only; the whole-span subsection relocation was correct and is retained.',
 'corrected_tag_records':[{'statement_id':l,'tag':t} for _,_,l,t in guards],
 'source_sha256':hashlib.sha256(ed.text.encode()).hexdigest()},indent=2)+'\n')
