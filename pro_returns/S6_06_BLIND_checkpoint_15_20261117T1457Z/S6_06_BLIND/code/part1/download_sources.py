from pathlib import Path
from urllib.request import urlopen
root=Path(__file__).resolve().parents[3]
dest=root/'external_source_cache';dest.mkdir(exist_ok=True)
urls={
'Hirzebruch_Topological_Methods.pdf':'https://hirzebruch.mpim-bonn.mpg.de/id/eprint/114/6/Hirzebruch-TopologicalMethodsInAlgebraicGeometry.pdf',
'Mandal_2609.27929.pdf':'https://arxiv.org/pdf/2609.27929',
'Milivojevic_2022.pdf':'https://www.degruyterbrill.com/document/doi/10.1515/coma-2021-0133/pdf',
'CCPS_2023.pdf':'https://pure.mpg.de/pubman/item/item_3490930_4/component/file_3559887/Conway-Crowley-Powell-Sixt_Simply-connected%2Bmanifolds%2Bwith%2Blarge%2Bhomotopy%2Bstable%2Bclasses_2023.pdf'}
for name,url in urls.items():
 try:
  b=urlopen(url,timeout=30).read();(dest/name).write_bytes(b);print(name,len(b),b[:5],flush=True)
 except Exception as e:print(name,type(e).__name__,str(e),flush=True)
