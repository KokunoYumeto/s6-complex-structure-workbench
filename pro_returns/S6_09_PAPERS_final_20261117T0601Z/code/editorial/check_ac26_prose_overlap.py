"""Locate long identical prose runs for manual originality review.

Displayed/inline mathematics, labels and citations are ignored. A match is
not by itself plagiarism: standard phrases require contextual inspection.
The output contains our text plus line locators, not an AC26 transcription.
"""
from pathlib import Path
import re,json,collections,sys
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'deliverables'
paper=sys.argv[1] if len(sys.argv)>1 else 'I'
source=(ROOT/'sources/original/AC26_transcription.tex').read_text()
ours=(OUT/f'S6_09_PAPERS_{paper}.tex').read_text()
def tokens(s):
    def blank(m):return re.sub(r'[^\n]',' ',m[0])
    s=re.sub(r'(?<!\\)%[^\n]*',blank,s)
    s=re.sub(r'\\begin\{(equation\*?|align\*?|gather\*?|multline\*?|displaymath)\}.*?\\end\{\1\}',blank,s,flags=re.S)
    s=re.sub(r'\\\[.*?\\\]|\\\(.*?\\\)|\$\$.*?\$\$|(?<!\\)\$(?:\\.|[^$])*?(?<!\\)\$',blank,s,flags=re.S)
    s=re.sub(r'\\(?:label|ref|eqref|cref|Cref|cite\w*|path|url|begin|end)(?:\[[^\]]*\])*\{[^{}]*\}',blank,s)
    s=re.sub(r'\\[A-Za-z]+\*?',blank,s)
    found=list(re.finditer(r"[A-Za-z]+(?:['’-][A-Za-z]+)*",s))
    return [m[0].lower() for m in found],[m.start() for m in found]
a,ap=tokens(source);b,bp=tokens(ours);n=14
ix=collections.defaultdict(list)
for i in range(len(a)-n+1):ix[tuple(a[i:i+n])].append(i)
hits=[];covered=-1
for i in range(len(b)-n+1):
    if i<covered:continue
    best=None
    for j in ix.get(tuple(b[i:i+n]),[]):
        k=n
        while i+k<len(b) and j+k<len(a) and b[i+k]==a[j+k]:k+=1
        if best is None or k>best[0]:best=(k,j)
    if best:
        k,j=best;covered=i+k
        hits.append({'words':k,'paper_line':ours[:bp[i]].count('\n')+1,
                     'AC26_transcription_line':source[:ap[j]].count('\n')+1,
                     'our_prose':' '.join(b[i:i+k])})
hits.sort(key=lambda x:-x['words'])
out={'paper':paper,'minimum_words':n,'long_identical_runs':hits,
     'meaning':'Manual review locator, not a proof or automatic originality verdict; math and citation keys excluded.'}
(OUT/'records'/f'{paper}_AC26_prose_overlap.json').write_text(json.dumps(out,indent=2)+'\n')
print('Long prose matches:',len(hits))
for h in hits[:12]:print(h)
