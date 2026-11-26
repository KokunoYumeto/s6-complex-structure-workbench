from pathlib import Path
import concurrent.futures
import hashlib
import subprocess
import urllib.request

OUT=Path('/workspace/scratch/9fcd229a9ed4/base/S6_PUBLISH_c3_foundations_sources')
def retrieve(data):
    name,url,terms=data
    dest=OUT/f'S6_SERIES_PUBLISH_{name}.pdf'
    if not dest.exists():
        request=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
        with urllib.request.urlopen(request,timeout=35) as response:
            content=response.read()
        assert content.startswith(b'%PDF'),(name,len(content))
        dest.write_bytes(content)
    content=dest.read_bytes()
    pages=subprocess.check_output(['pdftotext','-layout',str(dest),'-'],text=True).split('\f')
    text='\f'.join(pages)
    dest.with_suffix('.txt').write_text(text,newline='\n')
    locations=[i+1 for i,page in enumerate(pages) if any(term in page for term in terms)]
    return name,url,hashlib.sha256(content).hexdigest(),len(pages)-1,locations

sources=[
 ('Dloussky2006_arxiv','https://arxiv.org/pdf/math/0406387',['2.22','2.25','2.27','2.29','2.38','Theorem 0.2']),
 ('DOT2003','https://www.jstage.jst.go.jp/article/tmj/55/2/55_2_283/_pdf/-char/en',['284','285','296']),
 ('KamenovaTori','https://www.math.stonybrook.edu/~kamenova/homepage_files/degen.pdf',['Theorem 3.1'])
]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    for data,result in zip(sources,executor.map(lambda d: retrieve(d),sources)):
        print(result)
