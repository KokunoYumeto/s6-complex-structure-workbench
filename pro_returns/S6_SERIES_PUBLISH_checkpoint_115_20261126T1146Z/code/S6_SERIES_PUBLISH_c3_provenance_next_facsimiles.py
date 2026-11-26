#!/usr/bin/env python3
"""Open bounded primary facsimiles outside the checkpoint and record metadata."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
import csv
import hashlib
import subprocess

ROOT = Path(__file__).resolve().parents[1]
TMP = ROOT.parents[1] / 'tmp' / 'c3_provenance_primary'
OUT = ROOT / 'agents' / 'continuation3_provenance' / 'next_part'
SOURCES = [
 ('BHPV2004_VI', 'pdf', 'https://page-one.springer.com/pdf/preview/10.1007/978-3-642-57739-0_7'),
 ('Grauert1960_article', 'pdf', 'https://www.numdam.org/article/PMIHES_1960__5__5_0.pdf'),
 ('Demailly2012_legacy', 'pdf', 'https://www-fourier.ujf-grenoble.fr/~demailly/manuscripts/agbook.pdf'),
 ('BS76', 'html', 'https://djvu.online/file/2hQiOnz8WuoQk'),
 ('Grauert1962_p364', 'jpg', 'https://images.p.sub.uni-goettingen.de/iiif/image/gdz:PPN235181684_0146:00000382/full/1600,/0/default.jpg'),
 ('Grauert1962_p365', 'jpg', 'https://images.p.sub.uni-goettingen.de/iiif/image/gdz:PPN235181684_0146:00000383/full/1600,/0/default.jpg'),
]

class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts=[]
    def handle_data(self, data):
        self.parts.append(data)

def fetch(item):
    key, suffix, url = item
    path = TMP / (key + '.' + suffix)
    row=dict(key=key,url=url,opened_utc=datetime.now(timezone.utc).isoformat(),temporary_path=str(path),status='',sha256='',bytes='')
    try:
        subprocess.run(['curl','--location','--fail','--silent','--show-error','--max-time','35',url,'-o',str(path)],check=True,capture_output=True,timeout=40)
        content=path.read_bytes()
        if suffix=='pdf' and not content.startswith(b'%PDF'):
            raise ValueError('response is not PDF')
        row.update(status='downloaded',sha256=hashlib.sha256(content).hexdigest(),bytes=str(len(content)))
        if suffix=='pdf':
            subprocess.run(['pdftotext','-layout',str(path),str(path.with_suffix('.txt'))],check=True,capture_output=True,timeout=20)
        elif suffix=='html':
            parser=Text();parser.feed(content.decode('utf-8'))
            path.with_suffix('.txt').write_text('\n'.join(parser.parts))
    except Exception as exc:
        row['status']=type(exc).__name__+': '+str(exc)
    return row

def main():
    TMP.mkdir(parents=True,exist_ok=True);OUT.mkdir(parents=True,exist_ok=True)
    with ThreadPoolExecutor(max_workers=6) as pool:
        rows=list(pool.map(fetch,SOURCES))
    with (OUT/'S6_SERIES_PUBLISH_next_facsimiles.tsv').open('w',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=list(rows[0]),delimiter='\t')
        writer.writeheader();writer.writerows(rows)
    for row in rows:
        print(row['key'],row['status'],row['bytes'],row['sha256'])

if __name__=='__main__':
    main()
