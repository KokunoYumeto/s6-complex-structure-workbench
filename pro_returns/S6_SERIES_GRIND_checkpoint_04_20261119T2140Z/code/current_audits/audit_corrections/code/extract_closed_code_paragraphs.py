from pathlib import Path
import re,json
root=Path(__file__).resolve().parents[1]
source=root.parent/'parts/IV.body.tex'
text=source.read_text()
matches=list(re.finditer(r'\\begin\{theorem\}(?:\[[^\n]*\])?\\label\{night:P3K\.(\d+)\}',text))
targets={109,110,113,114,115,118}
selected=[]
for i,m in enumerate(matches):
    n=int(m.group(1))
    if n not in targets:continue
    end=matches[i+1].start() if i+1<len(matches) else len(text)
    block=text[m.start():end]
    (root/f'IV_K{n}_current_block_snapshot.tex').write_text(block)
    for j,p in enumerate(re.finditer(r'\S[\s\S]*?(?:\n\s*\n|\Z)',block)):
        para=p.group().strip()
        if re.search(r'(?:code/|\.py\}|\.json\}|\.out\}|audit|manifest|worker|preread|certificate|independent check|program|script)',para,re.I):
            line=text.count('\n',0,m.start()+p.start())+1
            selected.append({'label':f'night:P3K.{n}','paragraph_index':j,'source_line':line,'text':para})
(root/'IV_closed_code_paragraphs.json').write_text(json.dumps(selected,ensure_ascii=False,indent=2)+'\n')
for i,q in enumerate(selected):
    print(f"{i:03d} K{q['label'].split('.')[-1]} L{q['source_line']} chars={len(q['text'])} "+q['text'][:210].replace('\n',' '))
print('paragraphs',len(selected))
