"""Move each reviewed complete endpoint subsection out of the open part.

Statements and their entire supporting proofs are transported byte-for-byte.
Permanent labels are preserved; the next build regenerates numbers and pages.
"""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'parts/IV.body.linked.tex';t=p.read_text()
marker='\\part{Results not yet established}'
final=t.index(marker)
starts=[]
for n in range(109,120):
    label=f'night:P3K.{n}'
    at=t.index('\\label{'+label+'}')
    if at<final:continue
    a=t.rfind('\\subsection{',0,at)
    assert a>final
    status=re.search(r'\\StatementRecord\{'+re.escape(label)+r'\}\{([^}]+)\}',t[at:]).group(1)
    starts.append((a,label,status))
starts.sort();blocks=[]
for i,(a,label,status) in enumerate(starts):
    b=starts[i+1][0] if i+1<len(starts) else len(t)
    blocks.append((a,b,label,status,t[a:b]))
moving=[x for x in blocks if x[3]=='proved']
if not moving:
    print('No established subsections remain in the open part.');raise SystemExit
remaining=t
for a,b,*_ in reversed(moving):remaining=remaining[:a]+remaining[b:]
heading='\\section{Marked endpoints and source-parameter returns}\n'
prefix=''
if heading not in remaining:
    prefix=heading+r'''
Each construction retains its original source section, point line,
finite roots, affine characters, ordinary reference and specified fan.
The statements give the exact parameter domain and all construction maps.

'''
    obsolete=r'''\subsection{Further marked endpoints and source-moduli loops}
The following statements retain the original source section, point line,
finite roots, affine characters, ordinary reference and specified fan.
Their separate construction maps and exact parameter domains are given
with each statement.'''
    assert remaining.count(obsolete)==1
    remaining=remaining.replace(obsolete,'',1)
at=remaining.index(marker)
# Place before the clearpage which introduces the final part.
if remaining[max(0,at-12):at].endswith('\\clearpage\n'):at-=len('\\clearpage\n')
new=remaining[:at]+prefix+''.join(x[4] for x in moving)+'\n'+remaining[at:]
records=[]
for a,b,label,status,block in moving:
    assert new.count(block)==1
    assert new.index('\\label{'+label+'}')<new.index(marker)
    records.append({'label':label,'bytes':len(block.encode()),'sha256':hashlib.sha256(block.encode()).hexdigest(),'old_character_range':[a,b],'new_character_start':new.index(block),'scope':'Entire subsection and supporting proofs moved without changing a byte.'})
p.write_text(new)
out=ROOT/'analysis/IV_established_block_moves.json'
previous=json.loads(out.read_text()) if out.exists() else []
previous+=records;out.write_text(json.dumps(previous,indent=2)+'\n')
print(json.dumps({'moved':[x['label'] for x in records],'total_moved':len(previous)}))
