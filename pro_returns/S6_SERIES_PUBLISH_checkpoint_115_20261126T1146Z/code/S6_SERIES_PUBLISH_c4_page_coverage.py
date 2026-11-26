"""Match actual reading rows to current rendered images, without reading credit.

The supplied logs contain human-visible image inspections by the named model
readers. This program can carry their evidence only to identical page images.
It cannot close an unread or visibly unresolved page. --complete writes the
canonical final table only after every current page has such evidence.
"""
from pathlib import Path
import argparse
import hashlib
import re
import fitz

ROOT=Path(__file__).resolve().parents[1]
BASE_LOGS=[
    'S6_SERIES_PUBLISH_c4_pages_001_200.md',
    'agents/continuation4_reductions/S6_SERIES_PUBLISH_c4_pages_101_200.md',
    'agents/continuation4_horizontal/S6_SERIES_PUBLISH_c4_pages_201_400.md',
    'agents/continuation4_conductor/S6_SERIES_PUBLISH_c4_pages_401_600.md',
    'agents/continuation4_reductions/S6_SERIES_PUBLISH_c4_pages_601_787.md',
]
FIXED_FINDINGS={26,35,39,43,44,72,78,111,234,250,265,269,300,307,311,314,
                350,370,377,392,410,428,527,536,551,553,554,605,611,698,731,746}

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def read_log(path):
    text=Path(path).read_text()
    records=[]
    for line in text.splitlines():
        m=re.match(r'^\|\s*(\d+)(?:\s*/\s*(\d+))?\s*\|',line)
        if not m:
            continue
        assert m[2] is None or int(m[1])==int(m[2]),('Physical/printed page distinction needs explicit mapping',path,line)
        hashes=re.findall(r'(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])',line)
        assert len(hashes)==1,(path,m[1],hashes)
        records.append((int(m[1]),hashes[0],line))
    assert len({r[0] for r in records})==len(records),('Repeated physical page',path)
    return records

def intervals(values):
    spans=[]
    for value in sorted(values):
        if spans and value==spans[-1][-1]+1:
            spans[-1][1]=value
        else:
            spans.append([value,value])
    return ', '.join(str(a) if a==b else f'{a}–{b}' for a,b in spans) or 'none'

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--pdf',type=Path,required=True)
    p.add_argument('--log',type=Path,action='append',default=[])
    p.add_argument('--complete',action='store_true')
    a=p.parse_args()
    pdf=a.pdf.resolve()
    image_folder=pdf.parent/'pages_120dpi'
    with fitz.open(pdf) as doc:
        count=len(doc)
    evidence={}
    original_pages=[]
    for name in BASE_LOGS:
        for page,image_hash,line in read_log(ROOT/name):
            original_pages.append(page)
            if page not in FIXED_FINDINGS:
                evidence[(page,image_hash)]=(name,line,'Previously viewed identical image')
    assert sorted(original_pages)==list(range(1,788)), 'Original actual-page log is incomplete.'
    for path in a.log:
        path=path.resolve()
        relative=str(path.relative_to(ROOT))
        for page,image_hash,line in read_log(path):
            if '| OPEN |' in line or '| PENDING |' in line:
                evidence.pop((page,image_hash),None)
                continue
            evidence[(page,image_hash)]=(relative,line,'Actual current or identical-image reading')
    covered=[]
    pending=[]
    current=[]
    for page in range(1,count+1):
        image_hash=sha(image_folder/f'page-{page:04d}.png')
        key=(page,image_hash)
        if key in evidence:
            covered.append(page)
            current.append((page,image_hash,evidence[key]))
        else:
            pending.append(page)
    print('Current physical pages:',count)
    print('Image-bound actual reading coverage:',len(covered))
    print('Pages still requiring image reading:',len(pending))
    print('Pending physical ranges:',intervals(pending))
    if not a.complete:
        return
    assert not pending,'Unread or unresolved current images remain.'
    source_hash=sha(ROOT/'S6_SERIES_PUBLISH_II.tex')
    pdf_hash=sha(pdf)
    path=ROOT/'S6_SERIES_PUBLISH_reading_II.md'
    text=path.read_text()
    heading='## Fourth-continuation final page coverage\n'
    assert heading not in text, 'The final canonical table already exists.'
    pieces=text.split('\n\n',2)
    assert len(pieces)==3
    pieces[1]=(f'Final-candidate status: complete. All {count} physical pages have actual image-reading evidence, '
        f'bound below to the current 120 dpi image hashes. Current source SHA-256 {source_hash}; '
        f'current PDF SHA-256 {pdf_hash}. Every changed image was viewed again; exact unchanged images retain '
        'their named earlier reading evidence. The fixed-candidate defects were repaired and their rebuilt '
        'images inspected. Rendering, extraction and this correspondence computation supply no reading or mathematical proof credit.')
    text='\n\n'.join(pieces)
    text+='\n\n'+heading+'\n'
    text+='The physical page number and image hash identify the exact page read. Each evidence path retains the reviewer, actual finding and exposure scope. Earlier candidate findings remain historical records.\n\n'
    text+='| Physical page | Image SHA-256 | Actual reading evidence and finding |\n| --- | --- | --- |\n'
    for page,image_hash,(name,line,kind) in current:
        detail=line.strip().strip('|').strip().replace(image_hash,'image hash above').replace('|',r'\|')
        text+=f'| {page} | {image_hash} | {kind}: `{name}`, page {page}. {detail} |\n'
    path.write_text(text,newline='\n')
    print('Canonical final reading table written; all evidence is from supplied actual-image logs.')

if __name__=='__main__':
    main()
