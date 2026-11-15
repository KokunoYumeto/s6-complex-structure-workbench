"""Fetch exact Niemeier Gram matrices from the Nebe--Sloane catalogue.
The index, the pages and the parsed integer matrices are retained.
Every lattice is subsequently verified independently by determinant,
evenness, positivity, and exhaustive exact root enumeration.
"""
from pathlib import Path
import urllib.request,re,json,concurrent.futures
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'records'/'B_catalogue';OUT.mkdir(exist_ok=True)
URL='https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/'
def fetch(name):
 p=OUT/name
 if not p.exists():p.write_bytes(urllib.request.urlopen(URL+name,timeout=30).read())
 return p.read_text()
index=fetch('index.html')
names=sorted(set(re.findall(r'href="([^"\n]*NIEM[^"\n]*)"',index,re.I)))
assert len(names)==23
def parse(name):
 s=fetch(name)
 a=re.search(r'<a NAME="GRAM">.*?</a><br>(.*?)(?:<p>|<a NAME=)',s,re.I|re.S).group(1)
 a=re.sub('<[^>]*>',' ',a);v=list(map(int,a.split()));n,k=v[:2];v=v[2:]
 assert n==24
 if k==0:
  assert len(v)==n*(n+1)//2
  g=[[0]*n for _ in range(n)];q=0
  for i in range(n):
   for j in range(i+1):g[i][j]=g[j][i]=v[q];q+=1
 else:
  assert k==n and len(v)==n*n
  g=[v[i*n:(i+1)*n] for i in range(n)]
 return name[:-5],g
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:gg=dict(ex.map(parse,names))
(OUT/'grams.json').write_text(json.dumps(gg))
for name,g in gg.items():print(name,len(g),URL+name+'.html')
