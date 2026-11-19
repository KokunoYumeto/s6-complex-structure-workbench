"""Render all post09 proofs and repaired/changed regions in frozen checkpoint10."""
from pathlib import Path
import json,re,subprocess
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parents[1]
pdf=root/'S6_04_MAPS_MANIFOLDS_paper.pdf';out=root/'records/pdf_qa'
textfile=root/'records/checkpoint_10_paper.txt'
subprocess.run(['pdftotext','-layout',str(pdf),str(textfile)],check=True)
pages=textfile.read_text().split('\f')
head=re.compile(r'(?:Theorem|Proposition|Corollary|Lemma|Problem|Conclusion|Resolved conclusion|Remaining task)\s+([A-F]\.\d+\.\d+)\s+\(')
starts={}
for i,page in enumerate(pages):
 for m in head.finditer(page):starts.setdefault(m[1],i+1)
tags=[f'D.2.{i}' for i in range(37,44)]+[f'E.2.{i}' for i in range(19,22)]
changed=['D.2.4','E.2.4']
selected=set();locations={}
for tag in tags+changed:
 assert tag in starts,(tag,starts)
 begin=starts[tag]
 later=[p for k,p in starts.items() if p>begin]
 end=min(later) if later else len(pages)-1
 locations[tag]={'start':begin,'through':end}
 selected.update(range(begin,end+1))
# Include the final proof page and the complete current bibliography,
# which contains the repaired and newly verified primary entries.
selected.update(range(max(1,len(pages)-8),len(pages)))
selected=sorted(selected);out.mkdir(exist_ok=True)
for p in selected:
 subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-r','100','-singlefile',
                 '-png',str(pdf),str(out/f'cp10_{p:03}')],check=True)
for group in range((len(selected)+7)//8):
 part=selected[group*8:group*8+8]
 sheet=Image.new('RGB',(1100,790*((len(part)+1)//2)),'#ddd')
 for i,p in enumerate(part):
  im=Image.open(out/f'cp10_{p:03}.png').convert('RGB');im.thumbnail((530,750))
  x,y=550*(i%2),790*(i//2);sheet.paste(im,(x+(550-im.width)//2,y+25))
  ImageDraw.Draw(sheet).text((x+12,y+6),f'Page {p}',fill='black')
 sheet.save(out/f'cp10_contact_{group+1}.png')
record={'statement_pages':locations,'extra_rendered_pages':selected,
        'repaired_regions':['D.WP5 freeness display','E.T1 curve classes','D.GC5 introductory sentence','E.H9a bank formula','new bibliography entries'],
        'changed_scope_paragraphs':changed}
(out/'checkpoint_10_extra_pages.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
