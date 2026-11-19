"""Import missing metadata only; current source readings remain separately scoped."""
from pathlib import Path
import json,re
P=Path(__file__).resolve().parents[1]
path=P/'S6_10_PAPERS_references.bib';bib=path.read_text()
seen=set(re.findall(r'^@\w+\{([^,]+),',bib,re.M));added=[]
for paper in ['II','IV']:
    src=P/f'papers/{paper}/references_additions.bib'
    if not src.exists():continue
    for block in re.split(r'(?m)(?=^@)',src.read_text()):
        m=re.match(r'@\w+\{([^,]+),',block)
        if not m or m[1] in seen:continue
        block=re.sub(r'(?m)^(\s*)note\s*=',r'\1source_note =',block)
        prefix=block.rstrip()[:-1].rstrip()
        if not prefix.endswith(','):prefix+=','
        block=prefix+'\n  verification = {unverified},\n  note = {Metadata imported in this writing; current exact source reading is recorded separately and no proof depends on an inherited note alone.}\n}\n'
        bib+='\n'+block;seen.add(m[1]);added.append({'key':m[1],'source':str(src.relative_to(P))})
path.write_text(bib)
record=P/'analysis/reference_additions_imports.json'
history=json.loads(record.read_text()) if record.exists() else []
record.write_text(json.dumps(history+added,indent=2))
print(json.dumps(added,indent=2))
