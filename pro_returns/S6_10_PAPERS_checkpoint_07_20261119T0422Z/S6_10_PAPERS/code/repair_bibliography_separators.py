"""Insert only missing top-level commas between adjacent BibTeX fields."""
from pathlib import Path
import json,re
P=Path(__file__).resolve().parents[1];f=P/'S6_10_PAPERS_references.bib';s=f.read_text();changes=[];out=[]
for block in re.split(r'(?m)(?=^@)',s):
 m=re.match(r'@\w+\{([^,]+),',block)
 if not m:out.append(block);continue
 depth=0;positions=[]
 for i,c in enumerate(block):
  escaped=i>0 and block[i-1]=='\\'
  if c=='{' and not escaped:depth+=1
  if c=='}' and not escaped:
   depth-=1
   if depth==1 and re.match(r'\s+[A-Za-z_][A-Za-z0-9_]*\s*=\s*\{',block[i+1:]):positions.append(i+1)
 for i in reversed(positions):block=block[:i]+','+block[i:]
 if positions:changes.append({'key':m[1],'commas_inserted':len(positions),'scope':'BibTeX syntax repair; all field contents unchanged'})
 out.append(block)
f.write_text(''.join(out));(P/'analysis/bibliography_separator_repairs.json').write_text(json.dumps(changes,indent=2));print('Inserted',sum(r['commas_inserted'] for r in changes),'missing field separators.')
